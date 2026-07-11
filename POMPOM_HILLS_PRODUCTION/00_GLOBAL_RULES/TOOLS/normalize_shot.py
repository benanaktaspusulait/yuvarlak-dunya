#!/usr/bin/env python3
"""
normalize_shot.py — Colour Drift Gate and Anchor Pipeline
PIL only (numpy gerekmez).

Kullanım:
  python3 normalize_shot.py <master_frame.png> <generated_video.mp4> [output_dir]
"""

import sys, os, json, subprocess, tempfile
from PIL import Image, ImageStat, ImageEnhance, ImageFilter

THRESHOLDS = {
    'brightness_pct': 5.0,      # ±5% of master
    'local_contrast_pct': 100.0, # Encoding farkından dolayı geniş eşik
    'sharpness_pct': 100.0,     # Encoding farkından dolayı geniş eşik
    'saturation_pct': 7.0,      # ±7% of master
    'shadow_deeper_pct': 15.0,  # shadows must not deepen significantly
    'highlight_clip_pct': 2.0,  # clipping must not increase
}

def analyze_frame(img):
    """Tek frame'den metrikleri çıkar (PIL only)."""
    stat = ImageStat.Stat(img)
    
    # Ortalama parlaklık
    mean_lum = sum(stat.mean) / len(stat.mean)
    
    # Median luminance
    median_lum = sum(stat.median) / len(stat.median)
    
    # Shadow level (en karanlık %10)
    sorted_pixels = sorted(img.convert('L').getdata())
    n = len(sorted_pixels)
    p10 = sorted_pixels[n // 10]
    p90 = sorted_pixels[int(n * 0.9)]
    
    # Local contrast (Laplacian variance)
    gray = img.convert('L')
    laplacian = gray.filter(ImageFilter.Kernel(
        size=(3,3),
        kernel=[-1,-1,-1,-1,8,-1,-1,-1,-1],
        scale=1, offset=0
    ))
    lap_stat = ImageStat.Stat(laplacian)
    local_contrast = lap_stat.var[0]
    
    # Sharpness
    sharpness = lap_stat.stddev[0]
    
    # Saturation (HSV approximation using R-G-B ranges)
    r_stat = ImageStat.Stat(img.split()[0])
    g_stat = ImageStat.Stat(img.split()[1])
    b_stat = ImageStat.Stat(img.split()[2])
    r_range = r_stat.extrema[0][1] - r_stat.extrema[0][0]
    g_range = g_stat.extrema[0][1] - g_stat.extrema[0][0]
    b_range = b_stat.extrema[0][1] - b_stat.extrema[0][0]
    saturation = (r_range + g_range + b_range) / 3 / 255 * 100
    
    # Shadow level
    shadow_level = p10
    
    # Highlight clipping (>250)
    pixels = list(img.convert('L').getdata())
    highlight_clip = sum(1 for p in pixels if p > 250) / len(pixels) * 100
    
    return {
        'mean_luminance': mean_lum,
        'median_luminance': median_lum,
        'p10_luminance': p10,
        'p90_luminance': p90,
        'local_contrast': local_contrast,
        'sharpness': sharpness,
        'saturation': saturation,
        'shadow_level': shadow_level,
        'highlight_clipping_pct': highlight_clip,
    }

def extract_frames(video_path, count=5):
    """Videodan count adet frame çıkar."""
    result = subprocess.run([
        'ffprobe', '-v', 'error', '-show_entries', 'format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1', video_path
    ], capture_output=True, text=True)
    duration = float(result.stdout.strip())
    
    timestamps = [0.5, duration*0.25, duration*0.5, duration*0.75, duration-0.5]
    
    frames = []
    for ts in timestamps:
        tmp = tempfile.NamedTemporaryFile(suffix='.png', delete=False).name
        subprocess.run([
            'ffmpeg', '-y', '-ss', str(ts), '-i', video_path,
            '-frames:v', '1', '-vf', 'scale=in_color_matrix=bt709:out_color_matrix=bt709',
            '-pix_fmt', 'rgb24', tmp
        ], capture_output=True)
        img = Image.open(tmp)
        frames.append((ts, img))
        os.unlink(tmp)
    
    return frames

def extract_final_frame(video_path, output_path):
    subprocess.run([
        'ffmpeg', '-sseof', '-0.1', '-i', video_path,
        '-frames:v', '1', '-vf', 'scale=in_color_matrix=bt709:out_color_matrix=bt709',
        '-pix_fmt', 'rgb24', output_path, '-y'
    ], capture_output=True)

def calculate_correction(master, video):
    # Tüm video ortalamasını kullan (tek frame değil)
    brightness_diff = master['mean_luminance'] - video['mean_luminance']
    # Çok küçük farklar için düzeltme yapma
    if abs(brightness_diff) < 3:
        b = 1.0
    else:
        b = max(0.90, min(1.10, master['mean_luminance'] / max(video['mean_luminance'], 1)))
    
    return {'brightness': b, 'contrast': 1.0, 'saturation': 1.0}

def calculate_correction_from_frames(master, frames_metrics):
    """Tüm video frame'lerinin ortalamasından düzeltme hesapla."""
    avg_mean = sum(m['mean_luminance'] for _, m in frames_metrics) / len(frames_metrics)
    brightness_diff = master['mean_luminance'] - avg_mean
    
    if abs(brightness_diff) < 3:
        b = 1.0
    else:
        b = max(0.90, min(1.10, master['mean_luminance'] / max(avg_mean, 1)))
    
    return {'brightness': b, 'contrast': 1.0, 'saturation': 1.0}

def apply_correction(input_path, output_path, corrections):
    b_val = corrections['brightness'] - 1.0
    
    # Sadece parlaklık ve doygunluk düzelt (kontrast eq filter'i güvenilmez)
    subprocess.run([
        'ffmpeg', '-y', '-i', input_path,
        '-vf', f'eq=brightness={b_val:.4f}:saturation={corrections["saturation"]:.4f}',
        '-color_range', 'tv', '-colorspace', 'bt709', '-color_trc', 'bt709', '-color_primaries', 'bt709',
        '-c:v', 'libx264', '-crf', '18', '-preset', 'medium', '-c:a', 'copy',
        output_path
    ], capture_output=True)

def check_drift_gate(master, normalized):
    results = []
    passed = True
    
    for metric, threshold in [
        ('mean_luminance', THRESHOLDS['brightness_pct']),
        ('saturation', THRESHOLDS['saturation_pct']),
    ]:
        drift = abs(normalized[metric] - master[metric]) / max(master[metric], 1) * 100
        ok = drift <= threshold
        results.append({'metric': metric, 'drift_pct': round(drift, 2), 'threshold': threshold, 'pass': ok})
        if not ok: passed = False
    
    for metric, threshold in [
        ('local_contrast', THRESHOLDS['local_contrast_pct']),
        ('sharpness', THRESHOLDS['sharpness_pct']),
    ]:
        if master[metric] > 0:
            drift = (normalized[metric] - master[metric]) / master[metric] * 100
            ok = drift <= threshold
            results.append({'metric': metric, 'drift_pct': round(drift, 2), 'threshold': threshold, 'pass': ok})
            if not ok: passed = False
    
    shadow_drift = (normalized['shadow_level'] - master['shadow_level']) / max(master['shadow_level'], 1) * 100
    shadow_ok = shadow_drift <= THRESHOLDS['shadow_deeper_pct']
    results.append({'metric': 'shadow_level', 'drift_pct': round(shadow_drift, 2), 'threshold': THRESHOLDS['shadow_deeper_pct'], 'pass': shadow_ok})
    if not shadow_ok: passed = False
    
    clip_diff = normalized['highlight_clipping_pct'] - master['highlight_clipping_pct']
    clip_ok = clip_diff <= THRESHOLDS['highlight_clip_pct']
    results.append({'metric': 'highlight_clipping', 'drift_pct': round(clip_diff, 2), 'threshold': THRESHOLDS['highlight_clip_pct'], 'pass': clip_ok})
    if not clip_ok: passed = False
    
    return {'passed': passed, 'checks': results}

def check_progressive_drift(frames_metrics):
    if len(frames_metrics) < 3:
        return {'drift_detected': False, 'reasons': []}
    
    b_vals = [m['mean_luminance'] for _, m in frames_metrics]
    c_vals = [m['local_contrast'] for _, m in frames_metrics]
    
    b_decreasing = sum(1 for i in range(1, len(b_vals)) if b_vals[i] < b_vals[i-1])
    c_increasing = sum(1 for i in range(1, len(c_vals)) if c_vals[i] > c_vals[i-1])
    
    drift = False
    reasons = []
    if b_decreasing >= len(b_vals) * 0.6:
        drift = True
        reasons.append(f'Parlaklık düşüyor: {b_vals[0]:.1f} → {b_vals[-1]:.1f}')
    if c_increasing >= len(c_vals) * 0.6:
        drift = True
        reasons.append(f'Kontrast artıyor: {c_vals[0]:.1f} → {c_vals[-1]:.1f}')
    
    return {'drift_detected': drift, 'reasons': reasons}

def main():
    if len(sys.argv) < 3:
        print("Kullanım: python3 normalize_shot.py <master.png> <video.mp4> [output_dir]")
        sys.exit(1)
    
    master_path, video_path = sys.argv[1], sys.argv[2]
    output_dir = sys.argv[3] if len(sys.argv) > 3 else os.path.dirname(video_path)
    os.makedirs(output_dir, exist_ok=True)
    shot_name = os.path.splitext(os.path.basename(video_path))[0]
    
    print(f'═══════════════════════════════════════')
    print(f'  DRIFT GATE — {shot_name}')
    print(f'═══════════════════════════════════════\n')
    
    # Master
    master_img = Image.open(master_path)
    master_m = analyze_frame(master_img)
    print(f'Master: parlaklık={master_m["mean_luminance"]:.1f}, kontrast={master_m["local_contrast"]:.1f}')
    
    # Video analiz
    frames = extract_frames(video_path)
    raw_list = [(ts, analyze_frame(img)) for ts, img in frames]
    for ts, m in raw_list:
        print(f'  {ts:.1f}s: parlaklık={m["mean_luminance"]:.1f}')
    
    raw_m = raw_list[0][1]
    
    # Düzeltme (tüm video ortalamasından)
    corrections = calculate_correction_from_frames(master_m, raw_list)
    print(f'\nDüzeltme: b={corrections["brightness"]:.3f}, c={corrections["contrast"]:.3f}, s={corrections["saturation"]:.3f}')
    
    # Uygula
    norm_video = os.path.join(output_dir, f'{shot_name}-normalized.mp4')
    apply_correction(video_path, norm_video, corrections)
    
    norm_frame = os.path.join(output_dir, f'{shot_name}-final-frame-normalized.png')
    extract_final_frame(norm_video, norm_frame)
    
    # Normalized analiz
    norm_img = Image.open(norm_frame)
    norm_m = analyze_frame(norm_img)
    
    # Drift Gate
    dg = check_drift_gate(master_m, norm_m)
    pd = check_progressive_drift(raw_list)
    
    # Rapor
    verdict = 'PASS' if dg['passed'] and not pd['drift_detected'] else 'FAIL'
    
    print(f'\nNormalized: parlaklık={norm_m["mean_luminance"]:.1f}, kontrast={norm_m["local_contrast"]:.1f}')
    print(f'\nDrift Gate:')
    for c in dg['checks']:
        s = '✓' if c['pass'] else '✗'
        print(f'  {s} {c["metric"]}: {c["drift_pct"]:+.1f}% (eşik: {c["threshold"]}%)')
    
    if pd['drift_detected']:
        print(f'\n⚠️ Progressive drift: {", ".join(pd["reasons"])}')
    
    print(f'\n═══ VERDICT: {verdict} ═══')
    print(f'\n@image1 olarak kullan: {norm_frame}')

if __name__ == '__main__':
    main()
