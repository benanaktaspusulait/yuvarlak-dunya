# S01E04 — Mimi's Big Yawn — Render Prompts (Consolidated)

> OpenArt-facing reference. Each shot's full prompt, negative prompt and reject
> checklist live in `../01_SHOTS/`. This file is the consolidated index of image
> references and the shared safety rules used by every shot.

## Global Text Safety (all shots)
No text. No subtitles. No speech bubbles. No captions. No on-screen dialogue text.

## Global Character Locks (all shots)
- Kiko: scale 100, coral pink #F8BBD0
- Mimi: scale 80, soft blue #90CAF9

## Image Reference Map

| Shot | @image1 (first-frame continuity) | @image2 (design canon only) |
|---|---|---|
| 01 | approved Shot 01 first-frame still (exterior master — NOT an opening) | — |
| 02 | Shot 01 approved final frame | — |
| 03 | Shot 02 final frame | — |
| 04 | Shot 03 final frame | — |
| 05 | Shot 04 final frame (exterior) | **REQUIRED** — Mimi's Burrow interior canon (`01_HERO_VIEW/mimis-burrow-interior-openart-prompt.md`) |
| 06 | Shot 05 interior final frame (interior master) | — |
| 07 | Shot 06 final frame | — |
| 08 | Shot 07 final frame | — |

## Shared Continuity Rule (Shots 02–08)
Use @image1 as the exact first frame and only visual continuity source. Do not reinterpret @image1. Do not recreate the scene from description. Hold @image1 almost exactly for the first 1 second. Keep the same camera position as @image1 (no reframe wide→medium). Match the lighting and colour grading of @image1 exactly. Characters are already present; do not introduce any character after the shot has started.

## Per-Shot Prompts
See individual files in `../01_SHOTS/`:
- `shot-01-mimi-yawns.md` (EXTERIOR master setup)
- `shot-02-try-flower-patch.md`
- `shot-03-try-tree-grass.md`
- `shot-04-kiko-points-doorway.md`
- `shot-05-stepping-inside.md` (planned crossing → INTERIOR master setup; use @image2)
- `shot-06-cozy-pillow.md`
- `shot-07-settling-down.md`
- `shot-08-goodnight.md`

## Production Gate Reminder
Only SAFE, frame-supported shots proceed. Generate Shot 01 first; do not batch all 8. See `EPISODE_SUMMARY.md` § Staged Production Gates.
