# E08 — Shot 03 — First Tower Attempt

---

## Scene Context

| Alan | Değer |
| --- | --- |
| Episode | S01E08 — Building Together |
| Shot | 03 / 08 |
| Duration | 15 seconds |
| Location | Central Square |
| Characters | Noah, Arda |
| Time of Day | Morning |

---

## Shot Contract

- **Role:** First build — tower rises but wobbles (gentle tension).
- **Uses:** the 6 blocks seeded in Shot 01.
- **Tower ledger:** start 0 stacked (blocks on ground) → end ~4 stacked, wobbly, chest-high, ≤ head.
- **Preflight status:** RISKY (tower height must stay ≤ head).
- **Gate:** B.

---

## Continuity

Continues directly from Shot 02. Same Central Square, same six blocks, same morning light. `@image1` = Shot 02 exported final frame (flat base block already placed).

---

## Start Frame

Use Shot 02's exported final frame as the exact first frame. Hold close to `@image1` for the first 1 second. Maintain character appearance/scale, environment, morning lighting, camera composition. Both characters already present.

---

## Background Object Lock

The background is locked from the first frame. Maintain all visible background objects; do not remove, replace, repaint or transform any of them. Only the characters and the 6 blocks may move.

---

## Visual Prompt

```text
Noah and Arda carefully stacking the colourful blocks into a small tower at Central Square, warm morning light. They place blocks one by one on the flat base; the little tower rises to about chest height and wobbles slightly. Focused, careful expressions, gentle hands. The tower stays small — no taller than the children. Big Pompom Tree behind them, no other characters, {style} {camera} {lighting}

Match the lighting and colour grading exactly from the supplied continuity reference image.
Do not display dialogue as on-screen text. No speech bubbles. No captions. No subtitles. No text.
The Central Square background is locked from the first frame; keep all visible trees, paths, landmarks and environment elements stable throughout the shot.
```

---

## Reference Usage

`@image1` = Shot 02 exported final frame — only visual continuity source, priority for camera, lighting, composition, scale, environment. Supplied by the production workflow.

---

## Camera Direction

Begin identical to `@image1`; static eye-level medium framing. Only a very subtle settle allowed — no pan, tracking, zoom, reset or reframing. Warm morning light throughout.

---

## Dialogue

```
Noah: Careful...
Arda: I am careful!
```

---

## Shot Breakdown

| Time | Action | Camera |
|---|---|---|
| 0-1 sn | Continuity hold — flat base block placed | Medium |
| 1-4 sn | Noah places a second block on the base | Medium |
| 4-7 sn | Arda hands up a third block, Noah stacks it | Medium |
| 7-10 sn | Arda adds a fourth block; tower reaches chest height | Medium |
| 10-13 sn | Tower wobbles; both lean back a little, watchful | Medium |
| 13-15 sn | Tower holds for now, teetering; both hold their breath | Established composition |

---

## Natural Character Motion Rule

Calm but alive: blinking, breathing, careful hand movements, gentle head turns, looking at the tower and each other, small anticipatory leans. Do not freeze the characters; no static talking pose, no long empty pauses or silent staring.

---

## Sound

- Birds chirping, soft wind
- Soft block-click stacking sounds
- Natural ambience only. No music. No background music.

---

## Lighting

Warm morning sunlight (matched to `@image1`).

---

## Negative Prompt

```text
low quality, blurry, deformed, extra limbs, text, watermark, photorealistic, horror, scary, dark lighting, violence, weapons, sharp objects, extra characters, redesigned environment, lighting change, colour grading change, camera reset, new establishing shot, character entrance, static talking pose, characters frozen, no movement, long empty pause, silent staring, dead air, background music, music, melody, song, soundtrack, musical bed, new blocks, extra blocks, missing blocks, disappearing blocks, changing block colours, blocks turning into toys, furniture, stones, food, boxes, tools, letters or signs, tower taller than the children, giant tower, oversized tower, duplicated blocks, morphing blocks, floating blocks
```

---

## QA Checklist

Reference: 16_VIDEO_QA_SPEC.md

- [ ] Character integrity/consistency/scale verified
- [ ] Object persistence — same 6 blocks; no spawn/vanish/morph/duplicate/colour change
- [ ] **Tower height ≤ head level** (ledger: end ~4 stacked, chest-high)
- [ ] Camera and lighting consistent with `@image1`
- [ ] Background stable; environment not reinterpreted
- [ ] Wobble reads as gentle tension, not scary
- [ ] Shot feels calm but alive; beat every 2–3s; dialogue supported by action
- [ ] No music; natural ambience only
- [ ] No dialogue line repeated from an earlier shot
- [ ] Final frame usable as `@image1` for Shot 04
