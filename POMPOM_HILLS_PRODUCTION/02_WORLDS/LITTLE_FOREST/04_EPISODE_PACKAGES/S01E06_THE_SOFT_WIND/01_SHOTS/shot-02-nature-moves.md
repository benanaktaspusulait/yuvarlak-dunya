# The Soft Wind — Shot 02 — Nature Moves

---

## Scene Context

| Alan | Değer |
|------|-------|
| Episode | S01E06 — The Soft Wind |
| Shot | 02 / 12 |
| Duration | 15 seconds |
| Location | Little Forest |
| Characters | Kiko |
| Time of Day | Warm Morning |

---

## Purpose

Show the wind's effect on nature — flowers sway, leaves dance.

## Continuity

Direct continuation from Shot 01. Kiko is in the same position. Background locked.

## Visual Prompt

```text
Little Forest, warm morning. The wind picks up gently — flowers sway, leaves dance in the air, tree branches move softly. Kiko (coral pink #F8BBD0) watches with wonder, turning her head to follow the movement. Soft dappled sunlight, warm pastel colours, round soft shapes, no other characters, {style} {camera} {lighting}

The Little Forest background is locked from Shot 01; keep all trees, paths and environment stable.

Do not display dialogue as on-screen text. No speech bubbles. No captions. No subtitles. No text.
```

## Camera Direction

Wide shot at child eye level. Slow pan following the wind movement. Kiko visible, 10-15% of frame.

## Dialogue

```text
Kiko: Where is it coming from?
```

## Shot Breakdown

| Time | Action | Camera |
|------|--------|--------|
| 0-3 sec | Flowers sway gently in the breeze | Wide hold |
| 3-6 sec | Leaves lift and dance in the air | Slow pan right |
| 7-10 sec | Kiko turns her head, following the movement | Pan continues |
| 11-15 sec | "Where is it coming from?" — curious expression | Medium on Kiko |

## Sound

Forest ambience intensifies slightly: more leaf rustle, gentle wind whoosh. No music.

## Negative Prompt

low quality, blurry, deformed, extra limbs, text, watermark, photorealistic, horror, scary, dark lighting, sharp objects, extra characters, night sky, stars, moonlight, background music, music, melody, song, soundtrack, sign, signs, readable text, label, symbol, letter, letters, arrow, direction mark, carved mark, painted mark, sign-like shape, marking on tree trunk, tree trunk symbol, yellow Y shape, carved letter, glyph, rune, logo

---

## QA — Shot 02 First-Frame (REJECTED for full video)

**Verdict:** RISKY → **REJECT FOR FULL VIDEO.** Regenerate first-frame / cheap preview before spending video credits.

**Reason (single blocking issue):** A yellow "Y"-like mark appeared on the right-side tree trunk. Even though it is not literally text, in a preschool video a viewer reads it as a sign / symbol / letter, and OpenArt may amplify it in motion. This violates the hard rule: **No signs. No readable text. No labels. No symbols. No arrows. No direction marks** (see `00-CORE/NEGATIVE_PROMPTS.md` and `00-CORE/17_VIDEO_GENERATION_STANDARD.md` § Text Safety).

**What was already good (keep on regenerate):**
- Kiko present, no Mimi, no extra characters
- Little Forest reads well; stepping-stone path clear; mushroom circle readable in the back
- Kiko doing a small gesture, fits Shot 02 (watching nature)
- no water / stream / bridge; no night; camera generally safe

**Minor, non-blocking:** Kiko is a little small — acceptable for Shot 02 (this is an environment-motion shot, not a Shot 01 social hook), so not a reason to reject.

## Regeneration Note (First-Frame Correction)

Use this add-on when regenerating the Shot 02 first-frame / cheap preview:

```text
Regenerate Shot 02 first-frame / cheap preview.

Keep the same composition idea: Kiko stands on the Little Forest stepping-stone path, watching leaves and flowers move gently in the breeze.

Important correction: Do not place any symbol, letter, marking, carved shape, painted mark, arrow, direction mark, sign-like shape, readable mark, or label on any tree trunk, mushroom, stone, leaf, or background object.

Tree trunks must be plain natural toy-like bark only. No yellow Y shape. No carved letters. No symbols. No sign-like markings.

Keep Kiko readable and inside the central safe area. Locked child-eye-level camera. No camera movement. No new objects. No extra characters. No Mimi yet. No water. No giant foreground mushroom.
```
