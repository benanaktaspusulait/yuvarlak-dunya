#!/usr/bin/env python3
"""
Batch update OpenArt prompt files - handles both formats:
1. New format: ## Dialogue section → add ## Voice Lock after it
2. Old format: "Dialogue:" line in Visual Prompt → add Voice Lock section before ## Negative Prompt
3. Also adds contrast terms and checklist items
"""

import os
import glob

BASE = "/Users/benanaktas/project/video/yuvarlak-dunya/POMPOM_HILLS_PRODUCTION/02_WORLDS"
DONE_EPISODES = {"S01E06_THE_SOFT_WIND"}

VOICE_LOCK_BLOCK = """

## Voice Lock

Each character must use their registered locked voice from VOICE_TRACKER.md.
Do not let OpenArt choose or generate voices.
Do not change voice between shots.
Same pitch, same timbre, same age, same speed, same warmth.
"""

CONTRAST_TERMS = ", high contrast, contrast increase, overly saturated, saturation increase, HDR, HDR look, glossy plastic, glossy CGI, harsh highlights, harsh shadows, blown highlights, oversharpened, extra sharp, over-polished CGI, colour drift, exposure drift, saturation drift, contrast drift, dark areas growing darker, highlights growing brighter, lighting becoming harsher"

VOICE_CHECKLIST = "\n- [ ] Character voices match registered Voice IDs — no drift"


def find_openart_files():
    patterns = [
        os.path.join(BASE, "**", "03_VIDEO_EXPORTS", "**", "*openart-prompt.md"),
        os.path.join(BASE, "**", "03_VIDEO_EXPORTS", "*openart-prompt.md"),
    ]
    files = set()
    for p in patterns:
        files.update(glob.glob(p, recursive=True))

    return sorted(f for f in files if not any(d in f for d in DONE_EPISODES))


def process(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    original = content
    changes = []

    # 1. Voice Lock
    if 'Voice Lock' not in content:
        if '## Dialogue' in content:
            # New format: insert after ## Dialogue block
            idx = content.index('## Dialogue')
            # Find end of dialogue block (next ## or end)
            rest = content[idx:]
            # Find the next ## after ## Dialogue
            next_section = rest.find('\n## ', 1)
            if next_section != -1:
                insert_at = idx + next_section
                content = content[:insert_at] + VOICE_LOCK_BLOCK + content[insert_at:]
            else:
                content = content.rstrip() + "\n" + VOICE_LOCK_BLOCK
            changes.append("Voice Lock (section)")
        elif 'Dialogue:' in content or 'dialogue:' in content.lower():
            # Old format: dialogue is inline. Add Voice Lock before ## Negative Prompt or ## OpenArt
            markers = ['## Negative Prompt', '## OpenArt', '## Openart']
            insert_before = None
            for m in markers:
                if m.lower() in content.lower():
                    # Find exact case
                    for i, line in enumerate(content.split('\n')):
                        if line.strip().lower().startswith(m.lower().replace('## ', '## ')):
                            insert_before = line
                            break
                    if insert_before:
                        break

            if insert_before:
                content = content.replace(insert_before, VOICE_LOCK_BLOCK.strip() + "\n\n" + insert_before)
                changes.append("Voice Lock (inline)")
            else:
                content = content.rstrip() + "\n" + VOICE_LOCK_BLOCK
                changes.append("Voice Lock (appended)")

    # 2. Contrast terms in negative prompt
    if 'contrast drift' not in content.lower():
        # Find negative prompt section
        lines = content.split('\n')
        result = []
        in_neg = False
        inserted = False

        for i, line in enumerate(lines):
            result.append(line)
            low = line.strip().lower()

            if low.startswith('## negative prompt') or low.startswith('## negatif'):
                in_neg = True
                continue

            if in_neg and not inserted:
                if low.startswith('## '):
                    # Hit next section - insert before it
                    result.pop()  # remove this ## line
                    # Find last non-empty line
                    while result and result[-1].strip() == '':
                        result.pop()
                    if result:
                        result[-1] = result[-1].rstrip() + CONTRAST_TERMS
                    result.append('')
                    result.append(line)
                    inserted = True
                    in_neg = False

        content = '\n'.join(result)
        if inserted:
            changes.append("Contrast terms")

    # 3. Checklist item
    if 'Character voices match registered Voice IDs' not in content:
        # Find approval checklist
        lines = content.split('\n')
        result = []
        in_check = False

        for i, line in enumerate(lines):
            result.append(line)
            if 'checklist' in line.lower() and line.strip().startswith('##'):
                in_check = True
                continue
            if in_check and line.strip().startswith('- [ ]'):
                if i + 1 >= len(lines) or not lines[i + 1].strip().startswith('- [ ]'):
                    result.append(VOICE_CHECKLIST)
                    in_check = False
                    changes.append("Checklist")

        content = '\n'.join(result)

    if content != original:
        with open(filepath, 'w') as f:
            f.write(content)
        return changes
    return []


def main():
    files = find_openart_files()
    print(f"Found {len(files)} files\n")

    updated = 0
    eps = set()

    for fp in files:
        parts = fp.split('/')
        ep = next((p for p in parts if p.startswith('S01E') or p.startswith('S02E')), '?')

        ch = process(fp)
        if ch:
            updated += 1
            eps.add(ep)
            rel = fp.replace(BASE + '/', '')
            print(f"✅ {rel}")
            print(f"   {', '.join(ch)}")

    print(f"\n{'='*60}")
    print(f"Updated: {updated}/{len(files)}")
    print(f"Episodes: {sorted(eps)}")


if __name__ == "__main__":
    main()
