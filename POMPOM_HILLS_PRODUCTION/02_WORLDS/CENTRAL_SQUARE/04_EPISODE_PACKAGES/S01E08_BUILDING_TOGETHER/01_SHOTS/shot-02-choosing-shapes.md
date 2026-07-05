# E08 — Shot 02 — Choosing Shapes

---

## Scene Context

| Alan | Değer |
| --- | --- |
| Episode | S01E08 — Building Together |
| Shot | 02 / 08 |
| Duration | 15 seconds |
| Location | Central Square |
| Characters | Noah, Arda |
| Time of Day | Morning |

---

## Shot Contract

- **Role:** Planning beat — simple shape logic (round vs flat).
- **Uses:** the 6 blocks seeded in Shot 01. No new objects.
- **Preflight status:** SAFE.
- **Gate:** B.

---

## Continuity

Continues directly from Shot 01. Same Central Square, same six blocks, same morning light. `@image1` = Shot 01 exported final frame.

---

## Start Frame

Use Shot 01's exported final frame as the exact first frame. Hold close to `@image1` for the first 1 second before new action begins. Maintain character appearance/scale, Central Square environment, morning lighting, camera composition. Do not redesign the environment. Both characters are already present; do not re-introduce anyone.

---

## Background Object Lock

The background is locked from the first frame. Maintain all visible background objects; do not remove, replace, repaint or transform any of them. Only the characters and the 6 blocks may move.

---

## Visual Prompt

```text
Noah and Arda kneeling by the six colourful blocks at Central Square, warm morning light. They are choosing which block to use first: Arda lifts a round block and looks questioningly at Noah; Noah gently picks up a large flat block and shows it, as if to say the flat one is the base. Calm, thoughtful, cooperative planning. Big Pompom Tree behind them, no other characters, {style} {camera} {lighting}

Match the lighting and colour grading exactly from the supplied continuity reference image.
Do not display dialogue as on-screen text. No speech bubbles. No captions. No subtitles. No text.
The Central Square background is locked from the first frame; keep all visible trees, paths, landmarks and environment elements stable throughout the shot.
```

---

## Reference Usage

`@image1` = Shot 01 exported final frame — the only visual continuity source, with priority for camera, lighting, composition, scale and environment. Supplied by the production workflow.

---

## Camera Direction

Begin identical to `@image1`; static eye-level medium framing. Only a very subtle settle is allowed — no pan, tracking, zoom, reset or reframing. Warm morning light throughout.

---

## Dialogue

```
Arda: This one?
Noah: The flat one first.
```

---

## Shot Breakdown

| Time | Action | Camera |
|---|---|---|
| 0-1 sn | Continuity hold — six blocks, both kneeling | Medium |
| 1-4 sn | Arda picks up a round block, holds it up, looks at Noah | Medium |
| 4-8 sn | Noah gently takes a large flat block, shows it | Medium |
| 8-11 sn | Arda looks at the flat block, understands, nods | Medium |
| 11-15 sn | Both set the flat block down as the base, small shared smile | Established composition |

---

## Natural Character Motion Rule

Calm but alive: blinking, breathing, small smiles, gentle head turns, small hand gestures, looking at the blocks and at each other, gentle pointing, shared reactions. Do not freeze the characters; no static talking pose, no long empty pauses or silent staring.

---

## Sound

- Birds chirping, soft wind
- Soft block-handling sounds
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

- [ ] Character integrity/consistency/scale verified (Arda smaller than Noah)
- [ ] Object persistence — same 6 blocks, no spawn/vanish/morph/duplicate/colour change
- [ ] Camera and lighting consistent with `@image1`
- [ ] Background stable; environment not reinterpreted
- [ ] Round vs flat shape choice reads clearly
- [ ] Shot feels calm but alive; beat every 2–3s; dialogue supported by action
- [ ] No music; natural ambience only
- [ ] No dialogue line repeated from an earlier shot
- [ ] Final frame usable as `@image1` for Shot 03
