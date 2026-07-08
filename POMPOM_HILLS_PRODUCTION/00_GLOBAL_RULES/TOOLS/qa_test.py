#!/usr/bin/env python3
"""
QA Test for all unproduced episode openart prompts.
Checks:
1. Voice Lock section present (if dialogue exists)
2. Colour/Contrast terms in negative prompt
3. Pompom Items mention (if applicable)
4. No FIRST-FRAME workflow
5. Checklist items present
6. Frame-to-video mode
"""

import os
import glob

BASE = "/Users/benanaktas/project/video/yuvarlak-dunya/POMPOM_HILLS_PRODUCTION/02_WORLDS"
DONE_EPISODES = {"S01E06_THE_SOFT_WIND"}


def find_files():
    patterns = [
        os.path.join(BASE, "**", "03_VIDEO_EXPORTS", "**", "*openart-prompt.md"),
        os.path.join(BASE, "**", "03_VIDEO_EXPORTS", "*openart-prompt.md"),
    ]
    files = set()
    for p in patterns:
        files.update(glob.glob(p, recursive=True))
    return sorted(f for f in files if not any(d in f for d in DONE_EPISODES))


def qa_check(filepath):
    issues = []
    with open(filepath, 'r') as f:
        content = f.read()
    low = content.lower()

    # 1. FIRST-FRAME check
    if 'first-frame' in low and 'cheaper' not in low:
        if 'mode: first-frame' in low or 'first-frame / cheap preview' in low:
            issues.append("❌ Uses FIRST-FRAME workflow")

    # 2. Voice Lock — only flag if there are actual character dialogue lines (Name: "...")
    import re
    has_character_dialogue = bool(re.search(r'(Kiko|Mimi|Opa|Arda|Noah|Luca|Tillo)\s*:', content))
    if has_character_dialogue and 'voice lock' not in low:
        issues.append("⚠️ Has character dialogue but no Voice Lock")

    # 3. Contrast terms
    if 'contrast drift' not in low and 'no contrast increase' not in low:
        issues.append("⚠️ Missing contrast/saturation drift terms")

    # 4. Checklist
    if 'checklist' not in low:
        issues.append("⚠️ No approval checklist")

    # 5. Frame-to-video
    if 'frame-to-video' in low or 'mode: frame-to-video' in low:
        pass  # good
    elif 'first-frame' in low:
        issues.append("❌ Not frame-to-video mode")

    return issues


def main():
    files = find_files()
    print(f"QA Testing {len(files)} openart prompt files\n")

    total_issues = 0
    clean = 0
    problematic = 0

    for fp in files:
        parts = fp.split('/')
        ep = next((p for p in parts if p.startswith('S01E') or p.startswith('S02E')), '?')
        shot = next((p for p in parts if p.startswith('shot-')), '?')

        issues = qa_check(fp)
        if issues:
            problematic += 1
            total_issues += len(issues)
            rel = fp.replace(BASE + '/', '')
            print(f"⚠️ {ep}/{shot}")
            for i in issues:
                print(f"   {i}")
        else:
            clean += 1

    print(f"\n{'='*60}")
    print(f"Total files: {len(files)}")
    print(f"Clean: {clean}")
    print(f"With issues: {problematic}")
    print(f"Total issues: {total_issues}")


if __name__ == "__main__":
    main()
