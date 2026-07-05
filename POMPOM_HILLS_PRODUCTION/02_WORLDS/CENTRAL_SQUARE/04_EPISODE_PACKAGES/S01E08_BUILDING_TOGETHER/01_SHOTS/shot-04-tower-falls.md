# E08 — Shot 04 — Tower Falls

---

## Scene Context

| Alan | Değer |
| --- | --- |
| Episode | S01E08 — Building Together |
| Shot | 04 / 08 |
| Duration | 15 seconds |
| Location | Central Square |
| Characters | Noah, Arda |
| Time of Day | Morning |

---

## Shot Contract

- **Role:** Problem beat — the tower topples softly and the blocks scatter gently.
- **Uses:** the same 6 blocks; count and identity preserved before and after the fall.
- **Tower ledger:** start ~4 stacked → end 0 stacked / 6 scattered (the SAME 6 blocks).
- **Preflight status:** RISKY (fall must be soft; no block leaves/enters the set).
- **Gate:** B.

---

## Continuity

Continues directly from Shot 03. Same Central Square, same six blocks, same morning light. `@image1` = Shot 03 exported final frame (wobbly chest-high tower).

---

## Start Frame

Use Shot 03's exported final frame as the exact first frame. Hold close to `@image1` for the first 1 second. Maintain character appearance/scale, environment, morning lighting, camera composition. Both characters already present.

---

## Background Object Lock

The background is locked from the first frame. Maintain all visible background objects; do not remove, replace, repaint or transform any of them. Only the characters and the 6 blocks may move.

---

## Visual Prompt

```text
The small block tower gently tips and softly tumbles at Central Square, warm morning light. The six colourful blocks slide and settle onto the ground in a gentle, soft, harmless way — a light, almost funny topple, nothing loud or fast. Noah and Arda lean back with soft surprised faces, safe and unhurt. The same six blocks are all still there, now resting on the ground. Big Pompom Tree behind them, no other characters, {style} {camera} {lighting}

Match the lighting and colour grading exactly from the supplied continuity reference image.
Do not display dialogue as on-screen text. No speech bubbles. No captions. No subtitles. No text.
The Central Square background is locked from the first frame; keep all visible trees, paths, landmarks and environment elements stable throughout the shot.
```

---

## Reference Usage

`@image1` = Shot 03 exported final frame — only visual continuity source, priority for camera, lighting, composition, scale, environment. Supplied by the production workflow.

---

## Camera Direction

Begin identical to `@image1`; static eye-level medium framing. No pan, tracking, zoom, reset or pull-back — the fall happens within the locked composition. Warm morning light throughout.

---

## Dialogue

```
Arda: Oh no!
Noah: It fell.
```

---

## Shot Breakdown

| Time | Action | Camera |
|---|---|---|
| 0-1 sn | Continuity hold — wobbly tower standing | Medium |
| 1-4 sn | Tower leans further; both notice, eyes widen softly | Medium |
| 4-8 sn | Tower gently topples; blocks slide softly to the ground | Medium |
| 8-11 sn | Blocks settle; Arda's small "oh no" reaction | Medium |
| 11-15 sn | Both look at the scattered blocks; soft, safe surprise | Established composition |

---

## Natural Character Motion Rule

Calm but alive: blinking, breathing, soft surprised expressions, gentle leans, looking at the fallen blocks and each other. The fall is soft and gentle — never loud, fast, crashing or frightening. Do not freeze the characters; no static talking pose, no long empty pauses.

---

## Sound

- Birds chirping, soft wind
- Soft, gentle block-settling sounds (light, not a crash)
- Natural ambience only. No music. No background music.

---

## Lighting

Warm morning sunlight (matched to `@image1`).

---

## Negative Prompt

```text
low quality, blurry, deformed, extra limbs, text, watermark, photorealistic, horror, scary, dark lighting, violence, weapons, sharp objects, extra characters, redesigned environment, lighting change, colour grading change, camera reset, camera pull-back, new establishing shot, character entrance, loud crash, fast motion, explosion, frightening, static talking pose, characters frozen, no movement, long empty pause, silent staring, dead air, background music, music, melody, song, soundtrack, musical bed, new blocks, extra blocks, missing blocks, disappearing blocks, changing block colours, blocks turning into toys, furniture, stones, food, boxes, tools, letters or signs, tower taller than the children, giant tower, oversized tower, duplicated blocks, morphing blocks, floating blocks
```

---

## QA Checklist

Reference: 16_VIDEO_QA_SPEC.md

- [ ] Character integrity/consistency/scale verified
- [ ] **Block count preserved** — the SAME 6 blocks before and after the fall; none leave or enter the set
- [ ] No block spawns/vanishes/morphs/duplicates/changes colour
- [ ] Fall is soft, gentle, safe — not loud, fast, crashing or scary
- [ ] Camera static (no pull-back); lighting consistent with `@image1`
- [ ] Background stable; environment not reinterpreted
- [ ] Shot feels calm but alive; beat every 2–3s; dialogue supported by action
- [ ] No music; natural ambience only
- [ ] Final frame (scattered-block layout) usable as `@image1` for Shot 05 — record scatter positions
