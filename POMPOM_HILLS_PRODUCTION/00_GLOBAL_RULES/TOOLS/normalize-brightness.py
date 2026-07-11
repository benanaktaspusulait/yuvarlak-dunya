#!/usr/bin/env python3
"""
normalize-brightness.py — Shot'lar arası parlaklık/kontrast normalizasyonu
S01E12'den çıkarılan kalıcı çözüm: video üretim modelleri her shot'ta
karanlaştırıyor ve kontrastı yükseltiyor.

Kullanım:
  python3 normalize-brightness.py <video_dizini> [hedef_parlaklık] [hedef_kontrast]

Örnek:
  python3 normalize-brightness.py ./01_SHOTS/video/ 109 52
"""

import sys
import os
import subprocess
import tempfile
from PIL import Image, ImageStat

def measure_frame(video_path, frame_time=7):
    """Videonun orta frame'inden parlaklık ve luma kontrastı ölç."""
    with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as tmp:
        tmp_path = tmp.name

    subprocess.run([
        'ffmpeg', '-y', '-ss', str(frame_time), '-i', video_path,
        '-vframes', '1', '-q:v', '2', tmp_path
    ], capture_output=True)

    img = Image.open(tmp_path)
    img = img.convert('L')
    stat = ImageStat.Stat(img)
    mean = stat.mean[0]
    contrast = stat.stddev[0]
    os.unlink(tmp_path)
    return mean, contrast

def correct_brightness(input_path, output_path, target_brightness, current_brightness, target_contrast, current_contrast):
    """Parlaklığı hedefe eşle, kontrastı asla artırma."""
    diff = target_brightness - current_brightness
    # diff pozitifse video çok karanlık (parlaklaştır)
    # diff negatifse video çok parlak (karart)
    brightness_adjust = diff / 255.0  # 0-255 scale'den -1..1 scale'e

    # Sınırla
    brightness_adjust = max(-0.15, min(0.15, brightness_adjust))

    # Kontrast sadece yüksekse azaltılır; düşükse artırılmaz.
    if current_contrast > target_contrast + 1.0:
        contrast_adjust = max(0.88, min(1.0, target_contrast / current_contrast))
    else:
        contrast_adjust = 1.0

    subprocess.run([
        'ffmpeg', '-y', '-i', input_path,
        '-vf', f'eq=brightness={brightness_adjust:.4f}:saturation=1.0:contrast={contrast_adjust:.4f}',
        '-c:v', 'libx264', '-crf', '18', '-preset', 'medium',
        '-c:a', 'copy',
        output_path
    ], capture_output=True, check=True)

def main():
    if len(sys.argv) < 2:
        print("Kullanım: python3 normalize-brightness.py <video_dizini> [hedef_parlaklık] [hedef_kontrast]")
        sys.exit(1)

    video_dir = sys.argv[1]
    target_brightness = float(sys.argv[2]) if len(sys.argv) > 2 else 109.0
    target_contrast = float(sys.argv[3]) if len(sys.argv) > 3 else 52.0

    print(f"Hedef parlaklık: {target_brightness}")
    print(f"Hedef luma kontrastı: {target_contrast}")
    print()

    # Tüm shot mp4'lerini bul
    shots = sorted([f for f in os.listdir(video_dir) if f.startswith('shot-') and f.endswith('.mp4') and 'original' not in f and 'fixed' not in f])

    results = []
    for shot_file in shots:
        shot_path = os.path.join(video_dir, shot_file)
        brightness, contrast = measure_frame(shot_path)
        brightness_diff = brightness - target_brightness
        contrast_diff = contrast - target_contrast
        results.append((shot_file, brightness, contrast, brightness_diff, contrast_diff))
        print(f"{shot_file}: parlaklık={brightness:.1f} (fark: {brightness_diff:+.1f}), kontrast={contrast:.1f} (fark: {contrast_diff:+.1f})")

    print()

    # Düzeltme gerekli mi?
    needs_fix = [(f, b, c, bd, cd) for f, b, c, bd, cd in results if abs(bd) > 2.0 or cd > 1.0]

    if not needs_fix:
        print("Tüm shot'lar hedefe yakın — düzeltme gerekmiyor.")
        return

    print(f"{len(needs_fix)} shot'ta düzeltme gerekli:")
    for f, b, c, bd, cd in needs_fix:
        print(f"  {f}: parlaklık {b:.1f} → {target_brightness:.1f} ({bd:+.1f}), kontrast {c:.1f} → <= {target_contrast:.1f} ({cd:+.1f})")

    print()

    # Düzeltmeleri uygula
    for shot_file, brightness, contrast, brightness_diff, contrast_diff in needs_fix:
        input_path = os.path.join(video_dir, shot_file)
        output_path = os.path.join(video_dir, shot_file.replace('.mp4', '-normalized.mp4'))

        print(f"Düzeltiliyor: {shot_file}...")
        correct_brightness(input_path, output_path, target_brightness, brightness, target_contrast, contrast)

        # Orijinali yedekle, düzeltmeyi koy
        original_backup = input_path.replace('.mp4', '-original.mp4')
        if not os.path.exists(original_backup):
            os.rename(input_path, original_backup)
        os.rename(output_path, input_path)

        # Kontrol et
        new_brightness, new_contrast = measure_frame(input_path)
        print(f"  Sonuç: parlaklık {brightness:.1f} → {new_brightness:.1f} (hedef: {target_brightness:.1f}), kontrast {contrast:.1f} → {new_contrast:.1f} (hedef üst sınır: {target_contrast:.1f})")

    print()
    print("Tamamlandı!")

if __name__ == '__main__':
    main()
