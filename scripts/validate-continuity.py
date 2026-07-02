#!/usr/bin/env python3
"""validate-continuity.py — Karakter ölçek ve renk paleti doğrulama"""

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
    scenes_dir = "04-SCENES/season-01"
    
    if not os.path.exists(scenes_dir):
        print("❌ 04-SCENES/season-01/ dizini bulunamadı")
        return 1
    
    for episode in sorted(os.listdir(scenes_dir)):
        episode_path = os.path.join(scenes_dir, episode)
        if not os.path.isdir(episode_path) or episode.startswith('.'):
            continue
        
        for filename in sorted(os.listdir(episode_path)):
            if filename.endswith('.md') and not filename.startswith('README'):
                filepath = os.path.join(episode_path, filename)
                errors = check_scene_file(filepath)
                if errors:
                    print(f"⚠️  {episode}/{filename}:")
                    for e in errors:
                        print(f"   - {e}")
                    errors_total += len(errors)
    
    print(f"\n{'✅' if errors_total == 0 else '❌'} Toplam: {errors_total} hata")
    return 1 if errors_total > 0 else 0

if __name__ == "__main__":
    sys.exit(main())
