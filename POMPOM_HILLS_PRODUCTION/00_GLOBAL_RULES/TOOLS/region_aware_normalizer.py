#!/usr/bin/env python3
"""
region_aware_normalizer.py — Region-Aware Base/Detail Normalization
OpenCV + NumPy. Global gblur YERINE base/detail decomposition kullanır.

Kullanım:
  python3 region_aware_normalizer.py <input_video.mp4> <input_anchor.png> <output_video.mp4> [output_frame.png]
"""

import sys, os, subprocess, tempfile, json
import cv2
import numpy as np
from PIL import Image, ImageStat, ImageFilter

def extract_frame(video_path, timestamp=7.0):
    tmp = tempfile.NamedTemporaryFile(suffix='.png', delete=False).name
    subprocess.run([
        'ffmpeg', '-y', '-ss', str(timestamp), '-i', video_path,
        '-frames:v', '1', '-pix_fmt', 'rgb24', tmp
    ], capture_output=True)
    frame = cv2.imread(tmp)
    os.unlink(tmp)
    return frame

def extract_final_frame(video_path, output_path):
    subprocess.run([
        'ffmpeg', '-sseof', '-0.1', '-i', video_path,
        '-frames:v', '1', '-pix_fmt', 'rgb24', output_path, '-y'
    ], capture_output=True)

def measure_frame(frame_bgr):
    """Global metrikler."""
    gray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY)
    lab = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2LAB).astype(np.float32)
    L = lab[:, :, 0]
    
    return {
        'brightness': float(L.mean()),
        'contrast': float(gray.astype(float).std()),
        'sharpness': float(cv2.Laplacian(gray, cv2.CV_64F).std()),
        'L_p50': float(np.percentile(L, 50)),
        'L_p10': float(np.percentile(L, 10)),
        'L_p90': float(np.percentile(L, 90)),
    }

def create_base_detail(L_float):
    """Base/detail decomposition."""
    L_uint8 = np.clip(L_float, 0, 255).astype(np.uint8)
    base = cv2.bilateralFilter(L_uint8, d=9, sigmaColor=75, sigmaSpace=75).astype(np.float32)
    detail = L_float - base
    return base, detail

def measure_detail_rms(detail):
    return float(np.sqrt(np.mean(detail**2)))

def create_region_masks(frame_bgr):
    """Basit bölge maskeleri oluştur."""
    gray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY)
    h, w = gray.shape
    
    # Merkez maskesi (karakterler genellikle merkeze yakın)
    center = np.zeros((h, w), dtype=bool)
    center[h//4:3*h//4, w//4:3*w//4] = True
    
    # Cilt rengi maskesi (orta parlaklık)
    skin = (gray > 100) & (gray < 200) & center
    
    # Koyu bölgeler (ağaç kabuğu, zemin)
    bark = (gray > 30) & (gray < 120) & (~skin)
    
    # Göz/çerçeve (çok koyu veya çok parlak)
    protected = (gray < 30) | (gray > 220)
    
    return {
        'skin': skin,
        'bark': bark,
        'protected': protected,
        'center': center,
    }

def build_tone_curve(anchor_L, video_L):
    """Monotonic L-channel tone curve."""
    anchor_mean = float(anchor_L.mean())
    video_mean = float(video_L.mean())
    
    # Sadece hafif düzeltme
    diff = anchor_mean - video_mean
    if abs(diff) < 2:
        return np.arange(256, dtype=np.uint8)  # Identity
    
    # Bounded shift
    shift = max(-8, min(8, diff))
    lut = np.clip(np.arange(256, dtype=np.float32) + shift, 0, 255).astype(np.uint8)
    return lut

def apply_region_aware_correction(frame_bgr, anchor_bgr, tone_lut, region_masks):
    """Base/detail decomposition ile bölgesel düzeltme."""
    frame_lab = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2LAB).astype(np.float32)
    L = frame_lab[:, :, 0]
    
    # Tone curve uygula
    L_uint8 = np.clip(L, 0, 255).astype(np.uint8)
    L_corrected = tone_lut[L_uint8].astype(np.float32)
    
    # Base/detail decomposition
    base, detail = create_base_detail(L_corrected)
    
    # Bölge bazlı detail gain
    detail_gain = np.ones_like(detail)
    
    # Skin: 0.82-1.00
    detail_gain[region_masks['skin']] = 0.90
    
    # Bark/ground: 0.58-1.00
    detail_gain[region_masks['bark']] = 0.70
    
    # Protected (eyes, highlights): 0.90-1.00
    detail_gain[region_masks['protected']] = 0.95
    
    # Detail RMS kontrolü — muhafazakâr hedef
    anchor_detail_rms = measure_detail_rms(
        create_base_detail(cv2.cvtColor(anchor_bgr, cv2.COLOR_BGR2LAB).astype(np.float32)[:, :, 0])[1]
    )
    current_detail_rms = measure_detail_rms(detail)
    
    # Hedef: anchor detail'in %110'u (çok agresif azaltma yapma)
    target_rms = min(current_detail_rms, anchor_detail_rms * 1.10)
    
    if current_detail_rms > target_rms:
        gain = target_rms / max(current_detail_rms, 1)
        gain = max(0.70, min(1.0, gain))  # Sınır: %70-100
        detail_gain = detail_gain * gain
    
    # Uygula
    L_out = base + detail_gain * detail
    L_out = np.clip(L_out, 0, 255)
    
    frame_lab[:, :, 0] = L_out
    result = cv2.cvtColor(np.clip(frame_lab, 0, 255).astype(np.uint8), cv2.COLOR_LAB2BGR)
    return result

def main():
    if len(sys.argv) < 4:
        print("Kullanım: python3 region_aware_normalizer.py <input.mp4> <anchor.png> <output.mp4> [output_frame.png]")
        sys.exit(1)
    
    input_video = sys.argv[1]
    anchor_path = sys.argv[2]
    output_video = sys.argv[3]
    output_frame = sys.argv[4] if len(sys.argv) > 4 else None
    
    shot_name = os.path.splitext(os.path.basename(input_video))[0]
    
    print(f'═══════════════════════════════════════')
    print(f'  REGION-AWARE NORMALIZER — {shot_name}')
    print(f'═══════════════════════════════════════\n')
    
    # Anchor
    anchor_bgr = cv2.imread(anchor_path)
    anchor_metrics = measure_frame(anchor_bgr)
    print(f'Anchor: b={anchor_metrics["brightness"]:.1f}, c={anchor_metrics["contrast"]:.1f}, s={anchor_metrics["sharpness"]:.1f}')
    
    # Opening frame
    opening = extract_frame(input_video, 0.5)
    opening_metrics = measure_frame(opening)
    print(f'Opening: b={opening_metrics["brightness"]:.1f}, c={opening_metrics["contrast"]:.1f}, s={opening_metrics["sharpness"]:.1f}')
    
    # Tone curve
    anchor_lab = cv2.cvtColor(anchor_bgr, cv2.COLOR_BGR2LAB).astype(np.float32)
    opening_lab = cv2.cvtColor(opening, cv2.COLOR_BGR2LAB).astype(np.float32)
    tone_lut = build_tone_curve(anchor_lab[:, :, 0], opening_lab[:, :, 0])
    
    # Region masks
    masks = create_region_masks(anchor_bgr)
    
    # Video processing
    print('\nProcessing video...')
    cmd = ['ffmpeg', '-i', input_video, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-']
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    result = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0',
                            '-show_entries', 'stream=width,height', '-of', 'csv=p=0', input_video],
                           capture_output=True, text=True)
    w, h = map(int, result.stdout.strip().split(','))
    
    frames = []
    while True:
        raw = proc.stdout.read(w * h * 3)
        if len(raw) < w * h * 3:
            break
        frame = np.frombuffer(raw, dtype=np.uint8).reshape((h, w, 3))
        frames.append(frame)
    proc.wait()
    
    print(f'  {len(frames)} frames decoded')
    
    # Process each frame
    corrected = []
    for i, frame in enumerate(frames):
        frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        result = apply_region_aware_correction(frame_bgr, anchor_bgr, tone_lut, masks)
        corrected.append(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
        
        if (i + 1) % 100 == 0:
            print(f'  {i+1}/{len(frames)}')
    
    # Encode
    print('\nEncoding...')
    audio_tmp = os.path.join(os.path.dirname(output_video), f'{shot_name}_audio.aac')
    subprocess.run(['ffmpeg', '-y', '-i', input_video, '-vn', '-c:a', 'copy', audio_tmp], capture_output=True)
    
    cmd = ['ffmpeg', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{w}x{h}', '-r', '24', '-i', '-']
    if os.path.exists(audio_tmp):
        cmd += ['-i', audio_tmp, '-c:a', 'copy']
    cmd += ['-vf', 'colorspace=bt709:iall=bt709:all=bt709', '-color_range', 'tv',
            '-c:v', 'libx264', '-crf', '18', '-preset', 'medium', output_video]
    
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    for frame in corrected:
        proc.stdin.write(frame.tobytes())
    proc.stdin.close()
    proc.wait()
    
    # Final frame
    if output_frame:
        extract_final_frame(output_video, output_frame)
    
    # Quality check
    final_frame = extract_frame(output_video)
    final_metrics = measure_frame(final_frame)
    
    b_diff = abs(final_metrics['brightness'] - anchor_metrics['brightness']) / anchor_metrics['brightness'] * 100
    s_diff = abs(final_metrics['sharpness'] - anchor_metrics['sharpness']) / anchor_metrics['sharpness'] * 100
    
    verdict = 'PASS' if b_diff <= 5 and s_diff <= 40 else 'FAIL'
    
    print(f'\nResult: b={final_metrics["brightness"]:.1f}(Δ{b_diff:.1f}%), s={final_metrics["sharpness"]:.1f}(Δ{s_diff:.1f}%)')
    print(f'VERDICT: {verdict}')
    
    if os.path.exists(audio_tmp):
        os.unlink(audio_tmp)

if __name__ == '__main__':
    main()
