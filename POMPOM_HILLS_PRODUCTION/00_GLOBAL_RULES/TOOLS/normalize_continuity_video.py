#!/usr/bin/env python3
"""
normalize_continuity_video.py — First-Frame Calibration and Colour Drift Gate
@image1 anchor'ına göre tüm videoyu normalize eder.

Kullanım:
  python3 normalize_continuity_video.py \
    --input-video shot-XX.mp4 \
    --input-anchor shot-XX-final-frame-raw.png \
    --episode-master EPISODE_COLOR_MASTER.png \
    --output-video shot-XX-normalized.mp4 \
    --output-final-frame shot-XX-final-frame-normalized.png \
    --report shot-XX-drift-report.json
"""

import sys, os, json, subprocess, tempfile, argparse
from PIL import Image, ImageStat, ImageFilter

def analyze_frame(img):
    """Kapsamlı frame analizi."""
    gray = img.convert('L')
    pixels = list(gray.getdata())
    n = len(pixels)
    sorted_px = sorted(pixels)
    
    mean_lum = sum(pixels) / n
    median_lum = sorted_px[n // 2]
    p10 = sorted_px[int(n * 0.10)]
    p90 = sorted_px[int(n * 0.90)]
    shadow_depth = sorted_px[int(n * 0.05)]
    
    white_clip = sum(1 for p in pixels if p > 250) / n * 100
    black_clip = sum(1 for p in pixels if p < 5) / n * 100
    
    # Local contrast
    laplacian = gray.filter(ImageFilter.Kernel(
        size=(3,3), kernel=[-1,-1,-1,-1,8,-1,-1,-1,-1], scale=1, offset=0
    ))
    lap_stat = ImageStat.Stat(laplacian)
    local_contrast = lap_stat.var[0]
    sharpness = lap_stat.stddev[0]
    
    # Saturation
    r, g, b = img.split()
    r_stat, g_stat, b_stat = ImageStat.Stat(r), ImageStat.Stat(g), ImageStat.Stat(b)
    saturation = ((r_stat.extrema[0][1]-r_stat.extrema[0][0]) + 
                  (g_stat.extrema[0][1]-g_stat.extrema[0][0]) + 
                  (b_stat.extrema[0][1]-b_stat.extrema[0][0])) / 3 / 255 * 100
    
    return {
        'mean_luminance': round(mean_lum, 2),
        'median_luminance': round(median_lum, 2),
        'p10': p10, 'p90': p90,
        'shadow_depth': shadow_depth,
        'white_clip': round(white_clip, 4),
        'black_clip': round(black_clip, 4),
        'local_contrast': round(local_contrast, 2),
        'sharpness': round(sharpness, 2),
        'saturation': round(saturation, 2),
    }

def extract_opening_frame(video_path):
    """Videonun ilk 0.3-0.8s ortasından穩定 frame çıkar."""
    tmp = tempfile.NamedTemporaryFile(suffix='.png', delete=False).name
    subprocess.run([
        'ffmpeg', '-y', '-ss', '0.5', '-i', video_path,
        '-frames:v', '1', '-vf', 'scale=in_color_matrix=bt709:out_color_matrix=bt709',
        '-pix_fmt', 'rgb24', tmp
    ], capture_output=True)
    img = Image.open(tmp)
    os.unlink(tmp)
    return img

def calculate_calibration(anchor_m, video_opening_m):
    """Anchor ve video opening frame karşılaştırarak düzeltme profili hesapla."""
    
    # Sadece parlaklık düzeltmesi (kontrastı etkilemesin)
    avg_lum = video_opening_m['mean_luminance']
    target_lum = anchor_m['mean_luminance']
    
    # Çok küçük farklar için düzeltme yapma
    if abs(target_lum - avg_lum) < 3:
        gamma = 1.0
    else:
        gamma = max(0.90, min(1.10, target_lum / max(avg_lum, 1)))
    
    return {
        'gamma': gamma,
        'saturation': 1.0,
        'lum_shift': target_lum - avg_lum,
    }

def apply_calibration_iterative(input_path, output_path, anchor_mean, max_iterations=3):
    """Döngüsel olarak hedef parlaklığı bulana kadar düzelt."""
    
    current_input = input_path
    
    for iteration in range(max_iterations):
        # Mevcut durumu analiz et
        tmp = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False).name
        subprocess.run([
            'ffmpeg', '-y', '-ss', '0.5', '-i', current_input,
            '-frames:v', '1', '-pix_fmt', 'rgb24', tmp
        ], capture_output=True)
        
        try:
            img = Image.open(tmp)
            gray = img.convert('L')
            stat = ImageStat.Stat(gray)
            current_mean = stat.mean[0]
        except:
            break
        finally:
            if os.path.exists(tmp):
                os.unlink(tmp)
        
        diff = abs(current_mean - anchor_mean)
        if diff < 2:
            # Hedefe ulaşıldı, mevcut dosyayı output'a kopyala
            if current_input != output_path:
                subprocess.run(['cp', current_input, output_path], capture_output=True)
            return
        
        # Gamma hesapla
        gamma = anchor_mean / max(current_mean, 1)
        gamma = max(0.92, min(1.08, gamma))
        
        b_val = gamma - 1.0
        out = f'{output_path}.iter{iteration}'
        
        subprocess.run([
            'ffmpeg', '-y', '-i', current_input,
            '-vf', f'eq=brightness={b_val:.4f}',
            '-c:v', 'libx264', '-crf', '18', '-preset', 'medium', '-c:a', 'copy',
            out
        ], capture_output=True)
        
        if os.path.exists(out):
            current_input = out
    
    # Son sonucu output'a kopyala
    if current_input != output_path:
        subprocess.run(['cp', current_input, output_path], capture_output=True)

def apply_calibration(input_path, output_path, calibration):
    """Tüm videoya sabit düzeltme uygula."""
    b_val = calibration['gamma'] - 1.0
    
    subprocess.run([
        'ffmpeg', '-y', '-i', input_path,
        '-vf', f'eq=brightness={b_val:.4f}:saturation={calibration["saturation"]:.4f}',
        '-color_range', 'tv', '-colorspace', 'bt709', '-color_trc', 'bt709', '-color_primaries', 'bt709',
        '-c:v', 'libx264', '-crf', '18', '-preset', 'medium', '-c:a', 'copy',
        output_path
    ], capture_output=True)

def extract_final_frame(video_path, output_path):
    subprocess.run([
        'ffmpeg', '-sseof', '-0.1', '-i', video_path,
        '-frames:v', '1', '-vf', 'scale=in_color_matrix=bt709:out_color_matrix=bt709',
        '-pix_fmt', 'rgb24', output_path, '-y'
    ], capture_output=True)

def drift_gate(anchor_m, corrected_m, master_m=None):
    """Drift Gate: anchor'a göre onay."""
    checks = []
    passed = True
    
    # Anchor comparisons — sadece temel metrikler
    for metric, threshold in [
        ('mean_luminance', 3.0),  # Ortalama parlaklık
        ('saturation', 7.0),      # Doygunluk
    ]:
        if anchor_m[metric] == 0: continue
        diff = (corrected_m[metric] - anchor_m[metric]) / abs(anchor_m[metric]) * 100
        ok = abs(diff) <= threshold
        checks.append({'metric': metric, 'anchor': anchor_m[metric], 'corrected': corrected_m[metric],
                       'diff_pct': round(diff, 2), 'threshold': threshold, 'pass': ok})
        if not ok: passed = False
    
    # Clipping
    bc = corrected_m['black_clip'] - anchor_m['black_clip']
    checks.append({'metric': 'black_clip', 'diff': round(bc, 4), 'threshold': 1.0, 'pass': bc <= 1.0})
    if bc > 1.0: passed = False
    
    wc = corrected_m['white_clip'] - anchor_m['white_clip']
    checks.append({'metric': 'white_clip', 'diff': round(wc, 4), 'threshold': 1.0, 'pass': wc <= 1.0})
    if wc > 1.0: passed = False
    
    # Episode master limits — geniş eşikler (farklı shot'lar farklı content)
    if master_m:
        for metric, threshold in [('local_contrast', 30.0), ('sharpness', 25.0)]:
            if master_m[metric] > 0:
                diff = (corrected_m[metric] - master_m[metric]) / master_m[metric] * 100
                ok = diff <= threshold
                checks.append({'metric': f'vs_master_{metric}', 'diff_pct': round(diff, 2), 
                               'threshold': threshold, 'pass': ok})
                if not ok: passed = False
    
    return {'passed': passed, 'checks': checks}

def main():
    parser = argparse.ArgumentParser(description='First-Frame Calibration and Drift Gate')
    parser.add_argument('--input-video', required=True)
    parser.add_argument('--input-anchor', required=True)
    parser.add_argument('--episode-master', required=True)
    parser.add_argument('--output-video', required=True)
    parser.add_argument('--output-final-frame', required=True)
    parser.add_argument('--report', required=True)
    args = parser.parse_args()
    
    shot_name = os.path.splitext(os.path.basename(args.input_video))[0]
    
    print(f'═══════════════════════════════════════')
    print(f'  CALIBRATION — {shot_name}')
    print(f'═══════════════════════════════════════\n')
    
    # 1. Analiz
    anchor_img = Image.open(args.input_anchor)
    anchor_m = analyze_frame(anchor_img)
    
    master_img = Image.open(args.episode_master)
    master_m = analyze_frame(master_img)
    
    opening_img = extract_opening_frame(args.input_video)
    opening_m = analyze_frame(opening_img)
    
    print(f'Anchor:  parlaklık={anchor_m["mean_luminance"]:.1f}, kontrast={anchor_m["local_contrast"]:.1f}')
    print(f'Master:  parlaklık={master_m["mean_luminance"]:.1f}, kontrast={master_m["local_contrast"]:.1f}')
    print(f'Opening: parlaklık={opening_m["mean_luminance"]:.1f}, kontrast={opening_m["local_contrast"]:.1f}')
    
    # 2. Kalibrasyon
    calibration = calculate_calibration(anchor_m, opening_m)
    print(f'\nKalibrasyon: gamma={calibration["gamma"]:.4f}, sat={calibration["saturation"]:.4f}')
    
    # 3. Düzeltme (iteratif)
    apply_calibration_iterative(args.input_video, args.output_video, anchor_m['mean_luminance'])
    
    # 4. Final frame
    extract_final_frame(args.output_video, args.output_final_frame)
    
    # 5. Normalized analiz
    norm_img = Image.open(args.output_final_frame)
    norm_m = analyze_frame(norm_img)
    
    # 6. Drift Gate
    dg = drift_gate(anchor_m, norm_m, master_m)
    
    print(f'\nNormalized: parlaklık={norm_m["mean_luminance"]:.1f}, kontrast={norm_m["local_contrast"]:.1f}')
    print(f'\nDrift Gate:')
    for c in dg['checks']:
        s = '✓' if c['pass'] else '✗'
        diff = c.get('diff_pct', c.get('diff', 0))
        print(f'  {s} {c["metric"]}: {diff:+.2f} (eşik: {c["threshold"]})')
    
    verdict = 'PASS' if dg['passed'] else 'FAIL'
    print(f'\n═══ VERDICT: {verdict} ═══')
    
    # 7. Rapor
    report = {
        'shot': shot_name,
        'anchor_metrics': anchor_m,
        'master_metrics': master_m,
        'opening_metrics': opening_m,
        'calibration': calibration,
        'normalized_metrics': norm_m,
        'drift_gate': dg,
        'verdict': verdict,
    }
    
    with open(args.report, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f'\nRapor: {args.report}')
    print(f'Video: {args.output_video}')
    print(f'Frame: {args.output_final_frame}')

if __name__ == '__main__':
    main()
