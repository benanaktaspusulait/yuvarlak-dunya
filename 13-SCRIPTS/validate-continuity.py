#!/usr/bin/env python3
"""validate-continuity.py — Karakter ölçek ve renk paleti doğrulama"""

import glob
import os
import re
import sys

# Standart değerler
STANDARDS = {
    "Kiko": {"scale": "100", "color": "#F8BBD0"},
    "Mimi": {"scale": "80", "color": "#90CAF9"},
    "Opa": {"scale": "120", "color": "#A5D6A7"},
}

def check_scene_file(filepath):
    """Sahne dosyasında ölçek ve renk kontrolü"""
    errors = []
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Ölçek kontrolü
    for char, values in STANDARDS.items():
        if char in content:
            if values["scale"] not in content:
                errors.append(f"{char} ölçeği ({values['scale']}) bulunamadı")
            if values["color"] not in content:
                errors.append(f"{char} rengi ({values['color']}) bulunamadı")
    
    return errors

def main():
    print("=== Pompom Hills Süreklilik Doğrulama ===\n")
    
    errors_total = 0
    # Bölümler artık dünya-bazlı üretim paketlerinde yaşıyor:
    #   POMPOM_HILLS_PRODUCTION/02_WORLDS/<WORLD>/04_EPISODE_PACKAGES/<EPISODE>/
    worlds_dir = "POMPOM_HILLS_PRODUCTION/02_WORLDS"

    if not os.path.exists(worlds_dir):
        print(f"❌ {worlds_dir}/ dizini bulunamadı")
        return 1

    episode_dirs = sorted(glob.glob(os.path.join(worlds_dir, "*", "04_EPISODE_PACKAGES", "*")))

    for episode_path in episode_dirs:
        episode = os.path.relpath(episode_path, worlds_dir)
        for root, _dirs, files in os.walk(episode_path):
            for filename in sorted(files):
                if filename.endswith('.md') and not filename.startswith('README'):
                    filepath = os.path.join(root, filename)
                    errors = check_scene_file(filepath)
                    if errors:
                        rel = os.path.relpath(filepath, episode_path)
                        print(f"⚠️  {episode}/{rel}:")
                        for e in errors:
                            print(f"   - {e}")
                        errors_total += len(errors)
    
    print(f"\n{'✅' if errors_total == 0 else '❌'} Toplam: {errors_total} hata")
    return 1 if errors_total > 0 else 0

if __name__ == "__main__":
    sys.exit(main())
