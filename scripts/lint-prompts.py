#!/usr/bin/env python3
"""lint-prompts.py — Prompt değişken ve negatif liste uyumluluk kontrolü"""

import os
import re
import sys

REQUIRED_VARIABLES = ["{style}", "{camera}", "{lighting}"]

NEGATIVE_KEYWORDS = [
    "sharp edges", "angular shapes", "realistic", "horror", "violence",
    "weapons", "blood", "dark shadows", "black background", "neon",
    "photorealism", "text", "watermark", "logo", "extra fingers",
]

def check_prompt_file(filepath):
    """Prompt dosyasında değişken ve negatif liste kontrolü"""
    errors = []
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Değişken kontrolü
    for var in REQUIRED_VARIABLES:
        if var not in content:
            errors.append(f"Değişken {var} bulunamadı")
    
    return errors

def main():
    print("=== Pompom Hills Prompt Lint ===\n")
    
    errors_total = 0
    prompts_dir = "05-AI-PROMPTS"
    
    if not os.path.exists(prompts_dir):
        print(f"❌ {prompts_dir}/ dizini bulunamadı")
        return 1
    
    for filename in sorted(os.listdir(prompts_dir)):
        if filename.endswith('.md'):
            filepath = os.path.join(prompts_dir, filename)
            errors = check_prompt_file(filepath)
            if errors:
                print(f"⚠️  {filename}:")
                for e in errors:
                    print(f"   - {e}")
                errors_total += len(errors)
            else:
                print(f"✅ {filename}")
    
    print(f"\n{'✅' if errors_total == 0 else '❌'} Toplam: {errors_total} hata")
    return 1 if errors_total > 0 else 0

if __name__ == "__main__":
    sys.exit(main())
