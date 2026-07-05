# E08 — Shot 05 — Small Feeling Beat (NEW)

---

## Scene Context

| Alan | Değer |
| --- | --- |
| Episode | S01E08 — Building Together |
| Shot | 05 / 08 |
| Duration | 15 seconds |
| Location | Central Square |
| Characters | Noah, Arda |
| Time of Day | Morning |

---

## Shot Contract

- **Role:** Emotional centre — Arda is briefly discouraged; Noah reassures him calmly.
- **Uses:** the 6 scattered blocks from Shot 04 (positions preserved).
- **Preflight status:** SAFE.
- **Gate:** C.

---

## Continuity

Continues directly from Shot 04. Same Central Square, same six scattered blocks, same morning light. `@image1` = Shot 04 exported final frame. **The scattered-block positions from Shot 04 are preserved exactly** — no cleanup, no re-scatter, no new arrangement.

---

## Start Frame

Use Shot 04's exported final frame as the exact first frame. Hold close to `@image1` for the first 1 second. Maintain character appearance/scale, environment, morning lighting, camera composition, and the exact scattered-block layout. Both characters already present.

---

## Background Object Lock

The background is locked from the first frame. Maintain all visible background objects; do not remove, replace, repaint or transform any of them. Only the characters and the 6 blocks may move (and here the blocks stay where they scattered).

---

## Visual Prompt

```text
Noah and Arda beside the six scattered blocks at Central Square, warm morning light. Arda's shoulders drop a little and he looks down, a small, gentle discouraged feeling. Noah turns to him with a warm, calm, encouraging expression and a soft reassuring gesture, as if to say it's okay, we can try again. Tender, supportive, safe — a small feeling, quickly comforted. Big Pompom Tree behind them, no other characters, {style} {camera} {lighting}

Match the lighting and colour grading exactly from the supplied continuity reference image.
Do not display dialogue as on-screen text. No speech bubbles. No captions. No subtitles. No text.
The Central Square background is locked from the first frame; keep all visible trees, paths, landmarks and environment elements stable throughout the shot.
```

---

## Reference Usage

`@image1` = Shot 04 exported final frame — only visual continuity source, priority for camera, lighting, composition, scale, environment; scatter layout preserved. Supplied by the production workflow.

---

## Camera Direction

Begin identical to `@image1`; static eye-level medium framing. Only a very subtle settle allowed — no pan, tracking, zoom, reset or reframing. Warm morning light throughout.

---

## Dialogue

```
Arda: I can't do it.
Noah: We can try together.
```

---

## Shot Breakdown

| Time | Action | Camera |
|---|---|---|
| 0-1 sn | Continuity hold — scattered blocks, both seated | Medium |
| 1-4 sn | Arda's shoulders drop, he looks down softly | Medium |
| 4-7 sn | Noah turns toward Arda with a warm, calm look | Medium |
| 7-11 sn | Noah gives a gentle reassuring gesture (soft pat/nod) | Medium |
| 11-15 sn | Arda lifts his head, a small hopeful smile returns | Established composition |

---

## Natural Character Motion Rule

Calm but alive: blinking, breathing, a small shoulder drop, gentle head turns, a soft reassuring gesture, returning smile. The feeling is small, brief, and resolved by kindness — no shame, scolding, crying meltdown, or exclusion. Do not freeze the characters; no long empty pauses or silent staring.

---

## Sound

- Birds chirping, soft wind
- Natural ambience only. No music. No background music.

---

## Lighting

Warm morning sunlight (matched to `@image1`).

---

## Negative Prompt

```text
low quality, blurry, deformed, extra limbs, text, watermark, photorealistic, horror, scary, dark lighting, violence, weapons, sharp objects, extra characters, redesigned environment, lighting change, colour grading change, camera reset, new establishing shot, character entrance, crying meltdown, sobbing, scolding, shaming, angry face, distress, static talking pose, characters frozen, no movement, long empty pause, silent staring, dead air, background music, music, melody, song, soundtrack, musical bed, new blocks, extra blocks, missing blocks, disappearing blocks, changing block colours, blocks turning into toys, furniture, stones, food, boxes, tools, letters or signs, rearranged blocks, cleaned up blocks, duplicated blocks, morphing blocks, floating blocks
```

---

## QA Checklist

Reference: 16_VIDEO_QA_SPEC.md

- [ ] Character integrity/consistency/scale verified
- [ ] Scatter positions preserved exactly from Shot 04's final frame (no cleanup/re-scatter)
- [ ] Same 6 blocks; no spawn/vanish/morph/duplicate/colour change
- [ ] **Emotional beat reads as brief and supportive, not distressing** (no meltdown/shame)
- [ ] Camera and lighting consistent with `@image1`
- [ ] Background stable; environment not reinterpreted
- [ ] Shot feels calm but alive; beat every 2–3s; dialogue supported by action
- [ ] No music; natural ambience only
- [ ] No dialogue line repeated from an earlier shot
- [ ] Final frame usable as `@image1` for Shot 06
