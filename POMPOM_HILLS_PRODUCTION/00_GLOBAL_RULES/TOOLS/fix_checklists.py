#!/usr/bin/env python3
"""Add approval checklists to all openart prompt files that don't have one."""

import os
import glob

BASE = "/Users/benanaktas/project/video/yuvarlak-dunya/POMPOM_HILLS_PRODUCTION/02_WORLDS"
DONE = {"S01E06_THE_SOFT_WIND"}

CHECKLIST = """

## Approval Checklist

- [ ] First frame matches @image1
- [ ] No camera movement
- [ ] Character voices match registered Voice IDs — no drift
- [ ] No contrast / saturation / HDR / glossy drift from @image1
- [ ] Dialogue begins early — no dead air
"""


def find_files():
    patterns = [
        os.path.join(BASE, "**", "03_VIDEO_EXPORTS", "**", "*openart-prompt.md"),
        os.path.join(BASE, "**", "03_VIDEO_EXPORTS", "*openart-prompt.md"),
    ]
    files = set()
    for p in patterns:
        files.update(glob.glob(p, recursive=True))
    return sorted(f for f in files if not any(d in f for d in DONE))


def add_checklist(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    if 'checklist' in content.lower():
        return False

    content = content.rstrip() + "\n" + CHECKLIST
    with open(filepath, 'w') as f:
        f.write(content)
    return True


def main():
    files = find_files()
    updated = 0

    for fp in files:
        if add_checklist(fp):
            updated += 1

    print(f"Updated {updated}/{len(files)} files with checklists")


if __name__ == "__main__":
    main()
