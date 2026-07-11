#!/usr/bin/env python3
"""
normalize_continuity_opencv.py — OpenCV Luminance Tone Curve + Detail Attenuation
Deterministic, non-generative video normalization for Pompom Hills.

Kullanım:
  python3 normalize_continuity_opencv.py \
    --input-video shot-XX.mp4 \
    --input-anchor EXACT_IMAGE_USED_AS_IMAGE1.png \
    --episode-master EPISODE_COLOR_MASTER.png \
    --output-video SHOT_NORMALIZED.mp4 \
    --output-frame SHOT_FINAL_NORMALIZED.png \
    --report SHOT_DRIFT_REPORT.json
"""

import sys, os, json, subprocess, tempfile, argparse
import cv2
import numpy as np

# ─── L-Channel Percentile Extraction ───

def extract_l_percentiles(frame_rgb):
    """RGB frame'den CIE Lab L-channel percentiles."""
    lab = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2LAB)
    L = lab[:, :, 0].astype(np.float32)  # 0-255 range
    percentiles = {}
    for p in [1, 5, 10, 25, 50, 75, 90, 95, 99]:
        percentiles[f'P{p:02d}'] = float(np.percentile(L, p))
    return percentiles

def extract_chroma(frame_rgb):
    """RGB frame'den CIE Lab chroma (C = sqrt(a² + b²))."""
    lab = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2LAB)
    a = lab[:, :, 1].astype(np.float32) - 128
    b = lab[:, :, 2].astype(np.float32) - 128
    C = np.sqrt(a*a + b*b)
    return float(C.mean())

# ─── Tone Curve ───

def build_tone_curve(anchor_p, generated_p):
    """Lineer gain + bias: L_new = gain * L_old + bias."""
    # Hedef: anchor P50'e ulaş
    target = anchor_p['P50']
    current = generated_p['P50']
    
    # Gain: çok hafif (0.98-1.02 arası)
    gain = max(0.98, min(1.02, target / max(current, 1)))
    
    # Bias: kalan fark
    bias = (target - current * gain) * 0.3  # %30 uygula
    
    # Gain 1.0 yap, sadece bias kullan (daha güvenli)
    gain = 1.0
    
    # LUT
    lut = np.clip(np.arange(256, dtype=np.float32) * gain + bias, 0, 255).astype(np.uint8)
    
    return lut

# ─── Detail Attenuation ───

def compute_detail_layer(L_float):
    """L channel'dan base/detail ayrıştırması (bilateral filter ile)."""
    L_uint8 = np.clip(L_float * 255, 0, 255).astype(np.uint8)
    
    # Base: bilateral filter (edge-preserving smoothing)
    base = cv2.bilateralFilter(L_uint8, d=9, sigmaColor=75, sigmaSpace=75)
    base_float = base.astype(np.float32)
    
    # Detail = original - base
    detail = L_float - base_float
    
    return base_float, detail

def measure_detail_energy(detail):
    """Detail layer'in enerjisini ölç."""
    return {
        'rms': float(np.sqrt(np.mean(detail**2))),
        'std': float(np.std(detail)),
        'laplacian_var': float(cv2.Laplacian(np.clip(detail + 128, 0, 255).astype(np.uint8), cv2.CV_64F).var()),
    }

# ─── Frame Processing ───

def process_frame(frame_rgb, tone_lut, detail_gain):
    """Tek frame'i tone curve + detail attenuation ile düzelt."""
    # RGB → Lab
    lab = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2LAB).astype(np.float32)
    L = lab[:, :, 0]
    
    # Tone curve uygula
    L_uint8 = np.clip(L, 0, 255).astype(np.uint8)
    L_corrected = tone_lut[L_uint8].astype(np.float32)
    
    # Detail attenuation
    base, detail = compute_detail_layer(L_corrected)
    L_final = base + detail_gain * detail
    L_final = np.clip(L_final, 0, 255)
    
    # Lab → RGB
    lab[:, :, 0] = L_final
    lab = np.clip(lab, 0, 255).astype(np.uint8)
    result = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)
    
    return result

# ─── Video Processing ───

def decode_video_frames(video_path, start_sec=0, end_sec=None):
    """FFmpeg ile video frame'lerini decode et."""
    if end_sec is None:
        result = subprocess.run([
            'ffprobe', '-v', 'error', '-show_entries', 'format=duration',
            '-of', 'default=noprint_wrappers=1:nokey=1', video_path
        ], capture_output=True, text=True)
        end_sec = float(result.stdout.strip())
    
    cmd = [
        'ffmpeg', '-ss', str(start_sec), '-to', str(end_sec),
        '-i', video_path,
        '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'
    ]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Get frame dimensions
    result = subprocess.run([
        'ffprobe', '-v', 'error', '-select_streams', 'v:0',
        '-show_entries', 'stream=width,height',
        '-of', 'csv=p=0', video_path
    ], capture_output=True, text=True)
    w, h = map(int, result.stdout.strip().split(','))
    
    frames = []
    while True:
        raw = proc.stdout.read(w * h * 3)
        if len(raw) < w * h * 3:
            break
        frame = np.frombuffer(raw, dtype=np.uint8).reshape((h, w, 3))
        frames.append(frame)
    
    proc.wait()
    return frames, w, h

def encode_video(frames, audio_path, output_path, fps=24):
    """Frame'leri video olarak encode et."""
    if len(frames) == 0:
        return
    
    h, w = frames[0].shape[:2]
    
    cmd = [
        'ffmpeg', '-y',
        '-f', 'rawvideo', '-pix_fmt', 'rgb24',
        '-s', f'{w}x{h}', '-r', str(fps),
        '-i', '-',
    ]
    
    if audio_path and os.path.exists(audio_path):
        cmd += ['-i', audio_path]
    
    cmd += [
        '-vf', 'colorspace=bt709:iall=bt709:all=bt709',
        '-color_range', 'tv',
        '-c:v', 'libx264', '-crf', '18', '-preset', 'medium',
    ]
    
    if audio_path and os.path.exists(audio_path):
        cmd += ['-c:a', 'copy']
    else:
        cmd += ['-an']
    
    cmd.append(output_path)
    
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    for frame in frames:
        proc.stdin.write(frame.tobytes())
    proc.stdin.close()
    proc.wait()

def extract_audio(video_path, output_path):
    """Orijinal sesi çıkar."""
    subprocess.run([
        'ffmpeg', '-y', '-i', video_path, '-vn', '-c:a', 'copy', output_path
    ], capture_output=True)

def extract_final_frame(video_path, output_path):
    """Son frame'i PNG olarak çıkar."""
    subprocess.run([
        'ffmpeg', '-sseof', '-0.1', '-i', video_path,
        '-frames:v', '1', '-pix_fmt', 'rgb24',
        '-vf', 'colorspace=bt709:iall=bt709:all=bt709',
        output_path, '-y'
    ], capture_output=True)

# ─── Drift Gate ───

def drift_gate(anchor_p, corrected_p, anchor_chroma, corrected_chroma, master_p=None):
    """Kalite kontrolü."""
    checks = []
    passed = True
    
    for p_name in ['P50', 'P10', 'P90']:
        if anchor_p[p_name] > 0:
            diff = (corrected_p[p_name] - anchor_p[p_name]) / anchor_p[p_name] * 100
            threshold = 3.0 if p_name == 'P50' else 3.0
            ok = abs(diff) <= threshold
            checks.append({'metric': f'L_{p_name}', 'diff_pct': round(diff, 2), 'threshold': threshold, 'pass': ok})
            if not ok: passed = False
    
    # Chroma
    if anchor_chroma > 0:
        chroma_diff = (corrected_chroma - anchor_chroma) / anchor_chroma * 100
        ok = abs(chroma_diff) <= 5.0
        checks.append({'metric': 'chroma', 'diff_pct': round(chroma_diff, 2), 'threshold': 5.0, 'pass': ok})
        if not ok: passed = False
    
    return {'passed': passed, 'checks': checks}

# ─── Main ───

def main():
    parser = argparse.ArgumentParser(description='OpenCV Luminance Tone Curve + Detail Attenuation')
    parser.add_argument('--input-video', required=True)
    parser.add_argument('--input-anchor', required=True)
    parser.add_argument('--episode-master', required=True)
    parser.add_argument('--output-video', required=True)
    parser.add_argument('--output-frame', required=True)
    parser.add_argument('--report', required=True)
    args = parser.parse_args()
    
    shot_name = os.path.splitext(os.path.basename(args.input_video))[0]
    
    print(f'═══════════════════════════════════════')
    print(f'  OPENCV NORMALIZATION — {shot_name}')
    print(f'═══════════════════════════════════════\n')
    
    # 1. Anchor analiz
    anchor_rgb = cv2.cvtColor(cv2.imread(args.input_anchor), cv2.COLOR_BGR2RGB)
    anchor_p = extract_l_percentiles(anchor_rgb)
    anchor_chroma = extract_chroma(anchor_rgb)
    print(f'Anchor L: P50={anchor_p["P50"]:.1f}, P10={anchor_p["P10"]:.1f}, P90={anchor_p["P90"]:.1f}')
    print(f'Anchor Chroma: {anchor_chroma:.1f}')
    
    # 2. Master analiz
    master_rgb = cv2.cvtColor(cv2.imread(args.episode_master), cv2.COLOR_BGR2RGB)
    master_p = extract_l_percentiles(master_rgb)
    print(f'Master L: P50={master_p["P50"]:.1f}')
    
    # 3. Video decode
    print('\nVideo decode ediliyor...')
    frames, w, h = decode_video_frames(args.input_video)
    fps = 24
    print(f'  {len(frames)} frame, {w}x{h}')
    
    # 4. Opening frame analizi (0.2-0.8s)
    opening_start = int(0.2 * fps)
    opening_end = int(0.8 * fps)
    opening_frames = frames[opening_start:min(opening_end, len(frames))]
    
    if opening_frames:
        opening_median = np.median(np.stack(opening_frames), axis=0).astype(np.uint8)
    else:
        opening_median = frames[0]
    
    opening_p = extract_l_percentiles(opening_median)
    opening_chroma = extract_chroma(opening_median)
    print(f'\nOpening L: P50={opening_p["P50"]:.1f}, P10={opening_p["P10"]:.1f}')
    
    # 5. Tone curve hesapla
    print('\nTone curve hesaplanıyor...')
    tone_lut = build_tone_curve(anchor_p, opening_p)
    
    # 6. Detail analizi
    opening_lab = cv2.cvtColor(opening_median, cv2.COLOR_RGB2LAB).astype(np.float32)
    opening_L = opening_lab[:, :, 0]
    _, opening_detail = compute_detail_layer(opening_L)
    opening_detail_energy = measure_detail_energy(opening_detail)
    
    # Master detail
    master_lab = cv2.cvtColor(master_rgb, cv2.COLOR_RGB2LAB).astype(np.float32)
    master_L = master_lab[:, :, 0]
    _, master_detail = compute_detail_layer(master_L)
    master_detail_energy = measure_detail_energy(master_detail)
    
    # Target detail
    target_detail = min(opening_detail_energy['rms'], master_detail_energy['rms'] * 1.10)
    target_sharpness = min(opening_detail_energy['laplacian_var'], master_detail_energy['laplacian_var'] * 1.15)
    
    # Detail gain hesapla
    current_detail_energy = opening_detail_energy
    detail_gain = min(1.0, target_detail / max(current_detail_energy['rms'], 0.01),
                      (target_sharpness / max(current_detail_energy['laplacian_var'], 0.01)) ** 0.5)
    detail_gain = max(0.55, min(1.0, detail_gain))
    
    print(f'  Opening detail RMS: {opening_detail_energy["rms"]:.2f}')
    print(f'  Master detail RMS: {master_detail_energy["rms"]:.2f}')
    print(f'  Target detail: {target_detail:.2f}')
    print(f'  Detail gain: {detail_gain:.3f}')
    
    # 7. Chroma correction
    chroma_gain = max(0.95, min(1.05, anchor_chroma / max(opening_chroma, 0.01)))
    print(f'  Chroma gain: {chroma_gain:.3f}')
    
    # 8. Tüm frame'leri işle
    print('\nFrame\'ler işleniyor...')
    corrected_frames = []
    for i, frame in enumerate(frames):
        corrected = process_frame(frame, tone_lut, detail_gain)
        
        # Chroma correction
        lab = cv2.cvtColor(corrected, cv2.COLOR_RGB2LAB).astype(np.float32)
        a = lab[:, :, 1] - 128
        b = lab[:, :, 2] - 128
        C = np.sqrt(a*a + b*b)
        mask = C > 0
        if mask.any():
            a[mask] *= chroma_gain
            b[mask] *= chroma_gain
        lab[:, :, 1] = np.clip(a + 128, 0, 255)
        lab[:, :, 2] = np.clip(b + 128, 0, 255)
        corrected = cv2.cvtColor(np.clip(lab, 0, 255).astype(np.uint8), cv2.COLOR_LAB2RGB)
        
        corrected_frames.append(corrected)
        
        if (i + 1) % 50 == 0:
            print(f'  {i+1}/{len(frames)}')
    
    # 9. Encode
    print('\nVideo encode ediliyor...')
    audio_tmp = os.path.join(os.path.dirname(args.output_video), f'{shot_name}_audio.aac')
    extract_audio(args.input_video, audio_tmp)
    
    encode_video(corrected_frames, audio_tmp, args.output_video, fps)
    
    # 10. Final frame
    extract_final_frame(args.output_video, args.output_frame)
    
    # 11. Drift Gate
    corrected_frame_rgb = cv2.cvtColor(cv2.imread(args.output_frame), cv2.COLOR_BGR2RGB)
    corrected_p = extract_l_percentiles(corrected_frame_rgb)
    corrected_chroma = extract_chroma(corrected_frame_rgb)
    
    dg = drift_gate(anchor_p, corrected_p, anchor_chroma, corrected_chroma, master_p)
    
    print(f'\nSonuç:')
    print(f'  Anchor:  L={anchor_p["P50"]:.1f}, C={anchor_chroma:.1f}')
    print(f'  Corrected: L={corrected_p["P50"]:.1f}, C={corrected_chroma:.1f}')
    
    for c in dg['checks']:
        s = '✓' if c['pass'] else '✗'
        print(f'  {s} {c["metric"]}: {c["diff_pct"]:+.1f}% (eşik: {c["threshold"]}%)')
    
    verdict = 'PASS' if dg['passed'] else 'FAIL'
    print(f'\n═══ VERDICT: {verdict} ═══')
    
    # 12. Rapor
    report = {
        'shot': shot_name,
        'anchor_l_percentiles': anchor_p,
        'anchor_chroma': anchor_chroma,
        'opening_l_percentiles': opening_p,
        'master_l_percentiles': master_p,
        'detail_gain': detail_gain,
        'chroma_gain': chroma_gain,
        'corrected_l_percentiles': corrected_p,
        'corrected_chroma': corrected_chroma,
        'drift_gate': dg,
        'verdict': verdict,
    }
    
    with open(args.report, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f'\nRapor: {args.report}')
    print(f'Video: {args.output_video}')
    print(f'Frame: {args.output_frame}')
    
    # Temizle
    if os.path.exists(audio_tmp):
        os.unlink(audio_tmp)

if __name__ == '__main__':
    main()
