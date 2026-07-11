#!/usr/bin/env python3
"""
region_tracked_stabilizer.py — Region-Tracked Temporal Photometric Stabilizer
Two-pass: Opening Anchor Calibration + Within-Shot Temporal Drift Compensation.

Kullanım:
  python3 region_tracked_stabilizer.py \
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
from scipy.interpolate import PchipInterpolator

# ═══════════════════════════════════════════════
# PASS 1: OPENING ANCHOR CALIBRATION
# ═══════════════════════════════════════════════

def temporal_median_frame(video_path, start_sec=0.20, end_sec=0.80, fps=24):
    """Opening section'dan temporal median frame çıkar."""
    cmd = [
        'ffmpeg', '-ss', str(start_sec), '-to', str(end_sec),
        '-i', video_path, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'
    ]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    result = subprocess.run([
        'ffprobe', '-v', 'error', '-select_streams', 'v:0',
        '-show_entries', 'stream=width,height', '-of', 'csv=p=0', video_path
    ], capture_output=True, text=True)
    w, h = map(int, result.stdout.strip().split(','))
    
    frames = []
    while True:
        raw = proc.stdout.read(w * h * 3)
        if len(raw) < w * h * 3:
            break
        frame = np.frombuffer(raw, dtype=np.uint8).reshape((h, w, 3))
        frames.append(frame.astype(np.float32))
    proc.wait()
    
    if not frames:
        return None, w, h
    
    median = np.median(np.stack(frames), axis=0).astype(np.uint8)
    return median, w, h

def ecc_align(anchor_rgb, moving_rgb):
    """ECC affine alignment — anchor'a göre moving'i hizala."""
    anchor_gray = cv2.cvtColor(anchor_rgb, cv2.COLOR_RGB2GRAY)
    moving_gray = cv2.cvtColor(moving_rgb, cv2.COLOR_RGB2GRAY)
    
    warp_matrix = np.eye(2, 3, dtype=np.float32)
    criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 50, 1e-4)
    
    try:
        cc, warp_matrix = cv2.findTransformECC(anchor_gray, moving_gray, warp_matrix, cv2.MOTION_EUCLIDEAN, criteria)
        aligned = cv2.warpAffine(moving_rgb, warp_matrix, (moving_rgb.shape[1], moving_rgb.shape[0]),
                                  flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP)
        return aligned, warp_matrix, cc
    except:
        return moving_rgb, np.eye(2, 3, dtype=np.float32), 0.0

def create_valid_mask(anchor_rgb, aligned_rgb, residual_threshold=30):
    """Geçerli piksel maskesi oluştur — hareket edenleri, clip edilenleri hariç tut."""
    # Alignment residual
    diff = np.abs(anchor_rgb.astype(float) - aligned_rgb.astype(float)).mean(axis=2)
    residual_mask = diff < residual_threshold
    
    # Clipping mask
    gray = cv2.cvtColor(aligned_rgb, cv2.COLOR_RGB2GRAY)
    not_clipped = (gray > 5) & (gray < 250)
    
    # Character mask (basit: parlak/renkli bölgeleri hariç tut)
    # Hareket eden karakterler genellikle merkeze yakın
    h, w = anchor_rgb.shape[:2]
    center_mask = np.zeros((h, w), dtype=bool)
    center_mask[h//4:3*h//4, w//4:3*w//4] = True
    
    # Renkli bölgeleri hariç tut (yeşil ağaçlar sabit, renkli çiçekler hareketli olabilir)
    r, g, b = anchor_rgb[:,:,0].astype(float), anchor_rgb[:,:,1].astype(float), anchor_rgb[:,:,2].astype(float)
    mx = np.maximum(np.maximum(r, g), b)
    mn = np.minimum(np.minimum(r, g), b)
    saturation = np.where(mx > 0, (mx - mn) / mx * 100, 0)
    low_sat = saturation < 30  # Düşük doygunluk = sabit arka plan (ağaç kabuğu, taş, yol)
    
    # Birleştir: low_sat AND not_clipped AND residual_ok
    valid = low_sat & not_clipped & residual_mask
    
    return valid

def fit_luminance_curve(anchor_L, generated_L, valid_mask):
    """Geçerli piksellerden monotonic luminance curve fitting."""
    anchor_vals = anchor_L[valid_mask].flatten()
    generated_vals = generated_L[valid_mask].flatten()
    
    if len(anchor_vals) < 100:
        return None
    
    # Percentile eşleme
    percentiles = [1, 5, 10, 25, 50, 75, 90, 95, 99]
    anchor_p = [np.percentile(anchor_vals, p) for p in percentiles]
    generated_p = [np.percentile(generated_vals, p) for p in percentiles]
    
    # PCHIP ile monotonic curve
    try:
        pchip = PchipInterpolator(generated_p, anchor_p)
        
        # LUT oluştur
        lut = pchip(np.arange(256))
        
        # Highlight koruması
        p50_gen = np.percentile(generated_vals, 50)
        for i in range(256):
            diff = lut[i] - i
            if i < p50_gen * 0.5:  # Gölge
                lut[i] = i + min(diff, 10.0)
            elif i < p50_gen * 1.2:  # Orta ton
                lut[i] = i + min(diff, 18.0)
            else:  # Highlight
                lut[i] = i + max(min(diff, 3.0), -3.0)
        
        # Monotoniklik
        for i in range(1, 256):
            if lut[i] < lut[i-1]:
                lut[i] = lut[i-1]
        
        return np.clip(lut, 0, 255).astype(np.uint8)
    except:
        return None

# ═══════════════════════════════════════════════
# PASS 2: WITHIN-SHOT TEMPORAL DRIFT COMPENSATION
# ═══════════════════════════════════════════════

def detect_stable_patches(frame_rgb):
    """Sabit arka plan patch'lerini tespit et — ağaç kabuğu, taş, yol, mantar."""
    gray = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2GRAY)
    r, g, b = frame_rgb[:,:,0].astype(float), frame_rgb[:,:,1].astype(float), frame_rgb[:,:,2].astype(float)
    
    # Düşük doygunluk = sabit arka plan
    mx = np.maximum(np.maximum(r, g), b)
    mn = np.minimum(np.minimum(r, g), b)
    saturation = np.where(mx > 0, (mx - mn) / mx * 100, 0)
    
    # Koyu yeşil/kahverengi tonlar (ağaç kabuğu, mantar, zemin)
    brownish = (r > 60) & (r < 200) & (g > 40) & (g < 180) & (b < 120) & (saturation < 40)
    
    # Gri tonlar (taş, yol)
    grayish = (saturation < 20) & (gray > 40) & (gray < 200)
    
    # Birleştir
    stable = brownish | grayish
    
    # Küçük lekeleri temizle
    kernel = np.ones((5, 5), np.uint8)
    stable = cv2.morphologyEx(stable.astype(np.uint8), cv2.MORPH_OPEN, kernel).astype(bool)
    
    return stable

def track_patches_optical_flow(prev_gray, curr_gray, prev_pts):
    """Lucas-Kanade ile patch'leri takip et."""
    if prev_pts is None or len(prev_pts) == 0:
        return None, None
    
    lk_params = dict(winSize=(15, 15), maxLevel=2,
                     criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
    
    next_pts, status, _ = cv2.calcOpticalFlowPyrLK(prev_gray, curr_gray, prev_pts, None, **lk_params)
    
    # Sadece başarılı takipleri koru
    good_mask = status.flatten() == 1
    good_prev = prev_pts[good_mask]
    good_next = next_pts[good_mask]
    
    return good_prev, good_next

def measure_frame_metrics_on_patches(frame_rgb, patches):
    """Belirli patch'lerde metrik ölç."""
    if patches is None or len(patches) == 0:
        return None
    
    gray = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2GRAY)
    lab = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2LAB)
    L = lab[:, :, 0].astype(np.float32)
    
    # Patch boyutu
    patch_size = 20
    luminances = []
    local_contrasts = []
    details = []
    
    for pt in patches:
        x, y = int(pt[0]), int(pt[1])
        if x < patch_size or y < patch_size or x >= gray.shape[1] - patch_size or y >= gray.shape[0] - patch_size:
            continue
        
        patch_L = L[y-patch_size:y+patch_size, x-patch_size:x+patch_size]
        patch_gray = gray[y-patch_size:y+patch_size, x-patch_size:x+patch_size]
        
        luminances.append(float(np.mean(patch_L)))
        
        # Local contrast
        patch_lap = cv2.Laplacian(patch_gray, cv2.CV_64F)
        local_contrasts.append(float(patch_lap.var()))
        
        # Detail RMS
        base = cv2.GaussianBlur(patch_L, (5, 5), 1.5)
        detail = patch_L - base
        details.append(float(np.sqrt(np.mean(detail**2))))
    
    if not luminances:
        return None
    
    return {
        'median_luminance': float(np.median(luminances)),
        'mean_luminance': float(np.mean(luminances)),
        'local_contrast': float(np.mean(local_contrasts)),
        'detail_rms': float(np.mean(details)),
    }

# ═══════════════════════════════════════════════
# FRAME PROCESSING
# ═══════════════════════════════════════════════

def apply_two_pass_correction(frame_rgb, tone_lut, detail_gain):
    """Tone curve + detail attenuation uygula."""
    lab = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2LAB).astype(np.float32)
    L = lab[:, :, 0]
    
    # Tone curve
    L_uint8 = np.clip(L, 0, 255).astype(np.uint8)
    L_corrected = tone_lut[L_uint8].astype(np.float32)
    
    # Detail decomposition
    base = cv2.bilateralFilter(np.clip(L_corrected, 0, 255).astype(np.uint8), d=9, sigmaColor=75, sigmaSpace=75).astype(np.float32)
    detail = L_corrected - base
    
    # Detail attenuation
    L_final = base + detail_gain * detail
    L_final = np.clip(L_final, 0, 255)
    
    lab[:, :, 0] = L_final
    lab = np.clip(lab, 0, 255).astype(np.uint8)
    return cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)

# ═══════════════════════════════════════════════
# REPORTING
# ═══════════════════════════════════════════════

def create_contact_sheet(images, labels, output_path, max_cols=3):
    """Önce/sonra contact sheet oluştur."""
    imgs = []
    for img, label in zip(images, labels):
        if isinstance(img, str):
            img = cv2.cvtColor(cv2.imread(img), cv2.COLOR_BGR2RGB)
        # Label ekle
        h, w = img.shape[:2]
        label_h = 40
        canvas = np.ones((h + label_h, w, 3), dtype=np.uint8) * 255
        canvas[:h, :w] = img
        cv2.putText(canvas, label, (10, h + 28), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
        imgs.append(canvas)
    
    # Eşit boyuta getir
    max_h = max(i.shape[0] for i in imgs)
    resized = []
    for img in imgs:
        if img.shape[0] != max_h:
            scale = max_h / img.shape[0]
            img = cv2.resize(img, (int(img.shape[1] * scale), max_h))
        resized.append(img)
    
    # Yan yana yerleştir
    cols = min(len(resized), max_cols)
    rows = (len(resized) + cols - 1) // cols
    
    # Eşit boyutlu grid
    cell_w = max(r.shape[1] for r in resized)
    cell_h = max(r.shape[0] for r in resized)
    
    grid = np.ones((cell_h * rows, cell_w * cols, 3), dtype=np.uint8) * 255
    for idx, img in enumerate(resized):
        r, c = divmod(idx, cols)
        y_off = r * cell_h
        x_off = c * cell_w
        grid[y_off:y_off+img.shape[0], x_off:x_off+img.shape[1]] = img
    
    cv2.imwrite(output_path, cv2.cvtColor(grid, cv2.COLOR_RGB2BGR))

def create_luminance_graph(metrics_list, output_path, label='Luminance Over Time'):
    """Luminance/contrast zaman grafiği."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))
    
    frames = list(range(len(metrics_list)))
    lums = [m['median_luminance'] if m else 0 for m in metrics_list]
    contrasts = [m['local_contrast'] if m else 0 for m in metrics_list]
    
    ax1.plot(frames, lums, 'b-', linewidth=1.5)
    ax1.set_ylabel('Median Luminance')
    ax1.set_title(f'{label} — Luminance')
    ax1.grid(True, alpha=0.3)
    
    ax2.plot(frames, contrasts, 'r-', linewidth=1.5)
    ax2.set_ylabel('Local Contrast')
    ax2.set_xlabel('Frame')
    ax2.set_title(f'{label} — Local Contrast')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()

# ═══════════════════════════════════════════════
# MAIN PIPELINE
# ═══════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description='Region-Tracked Temporal Photometric Stabilizer')
    parser.add_argument('--input-video', required=True)
    parser.add_argument('--input-anchor', required=True)
    parser.add_argument('--episode-master', required=True)
    parser.add_argument('--output-video', required=True)
    parser.add_argument('--output-frame', required=True)
    parser.add_argument('--report', required=True)
    args = parser.parse_args()
    
    shot_name = os.path.splitext(os.path.basename(args.input_video))[0]
    
    print(f'═══════════════════════════════════════════════')
    print(f'  REGION-TRACKED STABILIZER — {shot_name}')
    print(f'═══════════════════════════════════════════════\n')
    
    # ── PASS 1: OPENING ANCHOR CALIBRATION ──
    print('PASS 1: Opening Anchor Calibration')
    print('─' * 40)
    
    # 1a. Temporal median
    print('  1a. Temporal median frame...')
    opening_median, w, h = temporal_median_frame(args.input_video)
    print(f'      {w}x{h}')
    
    # 1b. Anchor yükle
    anchor_rgb = cv2.cvtColor(cv2.imread(args.input_anchor), cv2.COLOR_BGR2RGB)
    
    # 1c. ECC alignment
    print('  1c. ECC alignment...')
    aligned, warp_matrix, cc = ecc_align(anchor_rgb, opening_median)
    print(f'      CC={cc:.4f}')
    
    # 1d. Valid mask
    print('  1d. Valid pixel mask...')
    valid_mask = create_valid_mask(anchor_rgb, aligned)
    valid_pct = valid_mask.sum() / valid_mask.size * 100
    print(f'      {valid_pct:.1f}% geçerli piksel')
    
    # 1e. Luminance curve fitting
    print('  1e. Luminance curve fitting...')
    anchor_L = cv2.cvtColor(anchor_rgb, cv2.COLOR_RGB2LAB)[:,:,0].astype(np.float32)
    aligned_L = cv2.cvtColor(aligned, cv2.COLOR_RGB2LAB)[:,:,0].astype(np.float32)
    
    tone_lut = fit_luminance_curve(anchor_L, aligned_L, valid_mask)
    if tone_lut is not None:
        print(f'      Curve fitted (PCHIP)')
    else:
        print(f'      Curve fitting failed — identity LUT used')
        tone_lut = np.arange(256, dtype=np.uint8)
    
    # ── PASS 2: TEMPORAL DRIFT COMPENSATION ──
    print('\nPASS 2: Temporal Drift Compensation')
    print('─' * 40)
    
    # Video decode
    print('  Decoding video...')
    cmd = [
        'ffmpeg', '-i', args.input_video,
        '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'
    ]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    raw_data = proc.stdout.read()
    proc.wait()
    
    frame_size = w * h * 3
    n_frames = len(raw_data) // frame_size
    print(f'      {n_frames} frames')
    
    # Stable patches tespiti
    print('  Detecting stable patches...')
    first_frame = np.frombuffer(raw_data[:frame_size], dtype=np.uint8).reshape((h, w, 3))
    stable_mask = detect_stable_patches(first_frame)
    
    # Stable patch noktalarını seç
    ys, xs = np.where(stable_mask)
    if len(ys) > 500:
        indices = np.random.choice(len(ys), 500, replace=False)
        stable_pts = np.array([[xs[i], ys[i]] for i in indices], dtype=np.float32).reshape(-1, 1, 2)
    else:
        stable_pts = np.array([[xs[i], ys[i]] for i in range(len(ys))], dtype=np.float32).reshape(-1, 1, 2)
    print(f'      {len(stable_pts)} stable patches selected')
    
    # Her frame'de metrikleri ölç
    print('  Measuring per-frame metrics on stable patches...')
    all_metrics = []
    prev_gray = cv2.cvtColor(first_frame, cv2.COLOR_RGB2GRAY)
    prev_pts = stable_pts.copy()
    
    for i in range(n_frames):
        frame = np.frombuffer(raw_data[i*frame_size:(i+1)*frame_size], dtype=np.uint8).reshape((h, w, 3))
        curr_gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        
        # Patch'leri takip et
        good_prev, good_next = track_patches_optical_flow(prev_gray, curr_gray, prev_pts)
        
        if good_next is not None and len(good_next) > 50:
            metrics = measure_frame_metrics_on_patches(frame, good_next.reshape(-1, 2))
            prev_pts = good_next.reshape(-1, 1, 2)
        else:
            metrics = measure_frame_metrics_on_patches(frame, stable_pts.reshape(-1, 2))
        
        all_metrics.append(metrics)
        prev_gray = curr_gray
        
        if (i + 1) % 50 == 0:
            print(f'      {i+1}/{n_frames}')
    
    # Temporal smoothing
    print('  Smoothing temporal curves...')
    valid_metrics = [m for m in all_metrics if m is not None]
    
    if valid_metrics:
        lums = [m['median_luminance'] for m in valid_metrics]
        contrasts = [m['local_contrast'] for m in valid_metrics]
        details = [m['detail_rms'] for m in valid_metrics]
        
        # Savitzky-Golay smoothing (window=11)
        from scipy.signal import savgol_filter
        if len(lums) > 11:
            lums_smooth = savgol_filter(lums, 11, 3)
            contrasts_smooth = savgol_filter(contrasts, 11, 3)
            details_smooth = savgol_filter(details, 11, 3)
        else:
            lums_smooth = lums
            contrasts_smooth = contrasts
            details_smooth = details
        
        # Anchor metric
        anchor_metrics = measure_frame_metrics_on_patches(anchor_rgb, stable_pts.reshape(-1, 2))
        if anchor_metrics:
            anchor_lum = anchor_metrics['median_luminance']
            anchor_contrast = anchor_metrics['local_contrast']
            anchor_detail = anchor_metrics['detail_rms']
        else:
            anchor_lum = 125.0
            anchor_contrast = 100.0
            anchor_detail = 100.0
        
        # Temporal correction curves hesapla
        # Exposure correction: anchor_lum / current_lum
        exposure_curve = np.array([anchor_lum / max(l, 1) for l in lums_smooth])
        exposure_curve = np.clip(exposure_curve, 0.70, 1.30)  # ±0.30 EV
        
        # Detail gain: anchor_detail / current_detail
        detail_curve = np.array([min(1.0, anchor_detail / max(d, 1)) for d in details_smooth])
        detail_curve = np.clip(detail_curve, 0.65, 1.0)
        
        # Smooth with Savitzky-Golay
        if len(exposure_curve) > 11:
            exposure_curve = savgol_filter(exposure_curve, 11, 3)
            detail_curve = savgol_filter(detail_curve, 11, 3)
        
        # Per-frame correction interpolation
        frame_indices = np.arange(n_frames)
        valid_indices = np.arange(len(exposure_curve))
        
        if len(valid_indices) > 1:
            exposure_interp = np.interp(frame_indices, valid_indices, exposure_curve)
            detail_interp = np.interp(frame_indices, valid_indices, detail_curve)
        else:
            exposure_interp = np.ones(n_frames)
            detail_interp = np.ones(n_frames)
        
        print(f'      Exposure range: {exposure_interp.min():.3f} - {exposure_interp.max():.3f}')
        print(f'      Detail range: {detail_interp.min():.3f} - {detail_interp.max():.3f}')
    
    # ── FRAME PROCESSING ──
    print('\nProcessing frames...')
    corrected_frames = []
    
    for i in range(n_frames):
        frame = np.frombuffer(raw_data[i*frame_size:(i+1)*frame_size], dtype=np.uint8).reshape((h, w, 3))
        
        if valid_metrics:
            # Per-frame exposure correction
            exp_gain = exposure_interp[i] if i < len(exposure_interp) else 1.0
            det_gain = detail_interp[i] if i < len(detail_interp) else 0.8
            
            # Tone curve: sadece exposure gain uygula
            lab = cv2.cvtColor(frame, cv2.COLOR_RGB2LAB).astype(np.float32)
            L = lab[:, :, 0]
            
            # Exposure correction: L_new = exp_gain * L
            L_corrected = np.clip(L * exp_gain, 0, 255)
            
            # Detail attenuation
            base = cv2.bilateralFilter(np.clip(L_corrected, 0, 255).astype(np.uint8), d=9, sigmaColor=75, sigmaSpace=75).astype(np.float32)
            detail = L_corrected - base
            L_final = np.clip(base + det_gain * detail, 0, 255)
            
            lab[:, :, 0] = L_final
            lab = np.clip(lab, 0, 255).astype(np.uint8)
            corrected = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)
        else:
            corrected = frame
        
        corrected_frames.append(corrected)
        
        if (i + 1) % 100 == 0:
            print(f'  {i+1}/{n_frames}')
    
    # ── ENCODE ──
    print('\nEncoding video...')
    audio_tmp = os.path.join(os.path.dirname(args.output_video), f'{shot_name}_audio.aac')
    subprocess.run(['ffmpeg', '-y', '-i', args.input_video, '-vn', '-c:a', 'copy', audio_tmp], capture_output=True)
    
    # Encode
    h, w = corrected_frames[0].shape[:2]
    cmd = ['ffmpeg', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{w}x{h}', '-r', '24', '-i', '-']
    if os.path.exists(audio_tmp):
        cmd += ['-i', audio_tmp, '-c:a', 'copy']
    cmd += ['-vf', 'colorspace=bt709:iall=bt709:all=bt709', '-color_range', 'tv',
            '-c:v', 'libx264', '-crf', '18', '-preset', 'medium', args.output_video]
    
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    for frame in corrected_frames:
        proc.stdin.write(frame.tobytes())
    proc.stdin.close()
    proc.wait()
    
    # Final frame
    subprocess.run([
        'ffmpeg', '-sseof', '-0.1', '-i', args.output_video,
        '-frames:v', '1', '-pix_fmt', 'rgb24', args.output_frame, '-y'
    ], capture_output=True)
    
    # ── QUALITY GATE ──
    print('\nQuality Gate...')
    corrected_frame = cv2.cvtColor(cv2.imread(args.output_frame), cv2.COLOR_BGR2RGB)
    corrected_L = cv2.cvtColor(corrected_frame, cv2.COLOR_RGB2LAB)[:,:,0].astype(np.float32)
    
    anchor_p50 = float(np.percentile(anchor_L, 50))
    corrected_p50 = float(np.percentile(corrected_L, 50))
    p50_diff = abs(corrected_p50 - anchor_p50) / max(anchor_p50, 1) * 100
    
    # Chroma
    anchor_lab = cv2.cvtColor(anchor_rgb, cv2.COLOR_RGB2LAB)
    a1 = anchor_lab[:,:,1].astype(float) - 128
    b1 = anchor_lab[:,:,2].astype(float) - 128
    anchor_chroma = float(np.sqrt(a1*a1 + b1*b1).mean())
    
    corr_lab = cv2.cvtColor(corrected_frame, cv2.COLOR_RGB2LAB)
    a2 = corr_lab[:,:,1].astype(float) - 128
    b2 = corr_lab[:,:,2].astype(float) - 128
    corrected_chroma = float(np.sqrt(a2*a2 + b2*b2).mean())
    
    print(f'  Anchor:  L_P50={anchor_p50:.1f}, Chroma={anchor_chroma:.1f}')
    print(f'  Corrected: L_P50={corrected_p50:.1f}, Chroma={corrected_chroma:.1f}')
    print(f'  L diff: {p50_diff:.1f}% (eşik: 2%)')
    
    passed = p50_diff <= 2.0
    verdict = 'PASS' if passed else 'FAIL'
    print(f'\n═══ VERDICT: {verdict} ═══')
    
    # ── REPORTS ──
    report = {
        'shot': shot_name,
        'pass1': {
            'temporal_median_shape': [w, h],
            'ecc_cc': round(cc, 4),
            'valid_pixel_pct': round(valid_pct, 1),
            'tone_curve_type': 'PCHIP' if tone_lut is not None else 'identity',
        },
        'pass2': {
            'n_frames': n_frames,
            'stable_patches': len(stable_pts),
            'exposure_range': [round(float(exposure_interp.min()), 3), round(float(exposure_interp.max()), 3)] if valid_metrics else None,
            'detail_range': [round(float(detail_interp.min()), 3), round(float(detail_interp.max()), 3)] if valid_metrics else None,
        },
        'quality_gate': {
            'anchor_L_P50': anchor_p50,
            'corrected_L_P50': corrected_p50,
            'l_diff_pct': round(p50_diff, 2),
            'anchor_chroma': anchor_chroma,
            'corrected_chroma': corrected_chroma,
            'verdict': verdict,
        },
        'luminance_over_time': [round(m['median_luminance'], 1) if m else None for m in all_metrics],
        'contrast_over_time': [round(m['local_contrast'], 1) if m else None for m in all_metrics],
    }
    
    with open(args.report, 'w') as f:
        json.dump(report, f, indent=2)
    
    # Contact sheet
    try:
        contact_sheet_path = args.report.replace('.json', '-contact-sheet.png')
        create_contact_sheet(
            [args.input_anchor, args.output_frame],
            ['@image1 Anchor', 'Corrected Final Frame'],
            contact_sheet_path
        )
        print(f'Contact sheet: {contact_sheet_path}')
    except Exception as e:
        print(f'Contact sheet oluşturulamadı: {e}')
    
    # Luminance graph
    try:
        graph_path = args.report.replace('.json', '-graph.png')
        create_luminance_graph(all_metrics, graph_path, shot_name)
        print(f'Luminance graph: {graph_path}')
    except Exception as e:
        print(f'Graph oluşturulamadı: {e}')
    
    print(f'\nRapor: {args.report}')
    print(f'Video: {args.output_video}')
    print(f'Frame: {args.output_frame}')
    
    if os.path.exists(audio_tmp):
        os.unlink(audio_tmp)

if __name__ == '__main__':
    main()
