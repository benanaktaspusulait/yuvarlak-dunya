# E08 — Shot 06 — New Plan

---

## Scene Context

| Alan | Değer |
| --- | --- |
| Episode | S01E08 — Building Together |
| Shot | 06 / 08 |
| Duration | 15 seconds |
| Location | Central Square |
| Characters | Noah, Arda |
| Time of Day | Morning |

---

## Shot Contract

- **Role:** Problem-solving — Noah shows the plan: big block on the bottom, small block on top.
- **Uses:** the 6 scattered blocks; Noah places one large flat block as the new base.
- **Tower ledger:** start 6 scattered → end 6 scattered with 1 big block placed as base.
- **Preflight status:** RISKY (pointing/gaze alignment must be clear).
- **Gate:** C.

---

## Continuity

Continues directly from Shot 05. Same Central Square, same six blocks, same morning light. `@image1` = Shot 05 exported final frame.

---

## Start Frame

Use Shot 05's exported final frame as the exact first frame. Hold close to `@image1` for the first 1 second. Maintain character appearance/scale, environment, morning lighting, camera composition. Both characters already present.

---

## Background Object Lock

The background is locked from the first frame. Maintain all visible background objects; do not remove, replace, repaint or transform any of them. Only the characters and the 6 blocks may move.

---

## Pointing & Gaze Lock (per 18_OPENART_CONTINUITY_AND_MOTION_RULES.md §17)

- **Target 1:** the large flat block (the base). It must be visible in frame while Noah indicates it.
- **Target 2:** a small round block (goes on top). It must be visible in frame while indicated.
- When Noah points at a target block, his **pointing hand, eyes, head, shoulders and upper body all align toward that same block**.
- When Noah indicates a block, **Arda turns toward the same block**.
- No pointing at empty space; no gaze/point mismatch.

---

## Visual Prompt

```text
Noah shows Arda a simple plan at Central Square, warm morning light. Noah points clearly at the large flat block on the ground — his hand, eyes, head and body all aimed at it — then places it down as the base; then he points at a small round block to show it goes on top. Arda follows Noah's point, turning to look at the same block, and nods with understanding. Calm, encouraging, cooperative. The six blocks are the same set from before. Big Pompom Tree behind them, no other characters, {style} {camera} {lighting}

Match the lighting and colour grading exactly from the supplied continuity reference image.
Do not display dialogue as on-screen text. No speech bubbles. No captions. No subtitles. No text.
The Central Square background is locked from the first frame; keep all visible trees, paths, landmarks and environment elements stable throughout the shot.
```

---

## Reference Usage

`@image1` = Shot 05 exported final frame — only visual continuity source, priority for camera, lighting, composition, scale, environment. Supplied by the production workflow.

---

## Camera Direction

Begin identical to `@image1`; static eye-level medium framing. Only a very subtle settle allowed — no pan, tracking, zoom, reset or reframing. Warm morning light throughout.

---

## Dialogue

```
Noah: Big block first.
Arda: Small block on top?
Noah: Yes.
```

---

## Shot Breakdown

| Time | Action | Camera |
|---|---|---|
| 0-1 sn | Continuity hold — scattered blocks, both seated | Medium |
| 1-4 sn | Noah points clearly at the large flat block (hand+eyes+head+body aligned) | Medium |
| 4-7 sn | Noah places the flat block as the base; Arda watches | Medium |
| 7-11 sn | Noah points at a small round block; Arda turns to the same block | Medium |
| 11-15 sn | Arda nods, understanding the plan; both ready | Established composition |

---

## Natural Character Motion Rule

Calm but alive: clear aligned pointing, gentle head turns, following gaze, nodding, small hand gestures. Do not freeze the characters; no static talking pose, no long empty pauses or silent staring.

---

## Sound

- Birds chirping, soft wind
- Soft block-placing sound
- Natural ambience only. No music. No background music.

---

## Lighting

Warm morning sunlight (matched to `@image1`).

---

## Negative Prompt

```text
low quality, blurry, deformed, extra limbs, text, watermark, photorealistic, horror, scary, dark lighting, violence, weapons, sharp objects, extra characters, redesigned environment, lighting change, colour grading change, camera reset, new establishing shot, character entrance, ambiguous pointing, pointing at empty space, gaze mismatch, static talking pose, characters frozen, no movement, long empty pause, silent staring, dead air, background music, music, melody, song, soundtrack, musical bed, new blocks, extra blocks, missing blocks, disappearing blocks, changing block colours, blocks turning into toys, furniture, stones, food, boxes, tools, letters or signs, tower taller than the children, giant tower, oversized tower, duplicated blocks, morphing blocks, floating blocks
```

---

## QA Checklist

Reference: 16_VIDEO_QA_SPEC.md

- [ ] Character integrity/consistency/scale verified
- [ ] Same 6 blocks; no spawn/vanish/morph/duplicate/colour change
- [ ] **Pointing, gaze, and body orientation all aligned to a visible target block** (both targets)
- [ ] **Arda turns toward the same block Noah indicates**
- [ ] Camera and lighting consistent with `@image1`
- [ ] Background stable; environment not reinterpreted
- [ ] Shot feels calm but alive; beat every 2–3s; dialogue supported by action
- [ ] No music; natural ambience only
- [ ] No dialogue line repeated from an earlier shot
- [ ] Final frame usable as `@image1` for Shot 07
