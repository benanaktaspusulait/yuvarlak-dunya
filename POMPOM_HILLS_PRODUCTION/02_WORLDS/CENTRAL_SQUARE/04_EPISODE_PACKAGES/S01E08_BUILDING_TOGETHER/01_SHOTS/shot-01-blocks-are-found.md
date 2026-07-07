# E08 — Shot 01 — Blocks Are Found (MASTER SETUP)

---

## Scene Context

| Alan | Değer |
| --- | --- |
| Episode | S01E08 — Building Together |
| Shot | 01 / 08 |
| Duration | 15 seconds |
| Location | Central Square |
| Characters | Noah, Arda |
| Time of Day | Morning |

---

## Shot Contract

- **Role:** EXTERIOR MASTER SETUP — seeds every object used in the whole episode.
- **Seeds:** all 8 building blocks (2 large flat + 3 medium flat/rounded + 3 small round/soft), the build area on the ground near the Big Pompom Tree, Noah, Arda, warm morning daylight.
- **Preflight status:** RISKY (master setup — must be approved at Gate A before any other shot).
- **Gate:** A.

---

## Production Gate Note (Gate A — hard stop)

Do not generate Shot 02 until Shot 01's final frame passes Gate A. If Shot 01 has fewer or
more than 8 blocks, blocks placed too far away, cropped blocks, or an unusable build area,
reject Shot 01 immediately and regenerate it. Do not try to fix missing or extra blocks in
later shots — the whole 8-shot chain locks to this frame. See
`00_EPISODE_OVERVIEW/S01E08_OBJECT_CONTINUITY_MAP.md` for the object set and tower ledger.

---

## Continuity

This is the first story shot of the episode. It begins after the optional Central Square Friends Micro-Opening pre-roll (a reusable world asset, not a story shot).

Use the approved Central Square Friends Micro-Opening final frame as `@image1` for environment continuity only. Do not copy `@image1` as an empty frame. Noah and Arda must be introduced naturally after the empty opening using an approved method from `00-CORE/17_VIDEO_GENERATION_STANDARD.md` § Character Introduction After Empty Opening Rule (partial edge visibility or visible entrance on a rounded path — no center pop-in).

Apply all Pompom Hills Visual Continuity Rules.

---

## Start Frame

Preserve the Central Square environment, warm morning daylight, camera height, Big Pompom Tree position, rounded paths and character proportions from `@image1`. The first 1 second holds close to `@image1` (environment continuity) before new action begins; character entrances feel natural, not a pop-in.

**All 8 blocks must be visible on the ground in the build area in this first shot.** They are seeded here and never re-introduced later.

---

## Background Object Lock

The background is locked from the first frame of this shot. Maintain all visible background objects throughout the entire video. Do not remove, replace, repaint or transform any visible background object. If a tree is visible it remains the same tree; if a path is visible it remains the same path; if a landmark is visible it remains in the same relative position. Do not introduce new trees or remove existing background objects. Only the main characters and the 8 blocks may move.

---

## Visual Prompt

```text
Noah and Arda at Central Square in warm morning light, near the Big Pompom Tree. On the ground in front of them is a small set of exactly eight colourful rounded building blocks — two large flat base blocks, three medium flat/rounded blocks and three small round/soft blocks in soft pastel colours (coral, yellow, blue, green). Noah crouches and arranges the blocks, curious; Arda arrives from a rounded path at the edge of frame and comes to join him. Both are child-sized and soft, Arda a little smaller than Noah. Toy-set preschool look, rounded shapes, no other characters, {style} {camera} {lighting}

Do not display dialogue as on-screen text. No speech bubbles. No captions. No subtitles. No text.
The Central Square background is locked from the first frame; keep all visible trees, paths, landmarks and environment elements stable throughout the shot.
```

---

## Reference Usage

`@image1` = Central Square Friends Micro-Opening final frame (environment continuity only). `@image1` has priority for camera, lighting, composition, scale and environment. The reference image is supplied by the production workflow and should not be hardcoded into this document.

---

## Camera Direction

Begin with a static 35mm wide shot establishing Central Square and the eight blocks on the ground. Arda enters from a rounded path and settles next to Noah. Camera gently settles toward the pair and the blocks while preserving the established camera distance — no pan, tracking, zoom or reset. Warm morning sunlight throughout. Avoid sudden zooms, shakes or whip pans.

---

## Dialogue

```
Noah: Look at these blocks.
Arda: Can we build?
Noah: Yes!
```

---

## Shot Breakdown

| Time | Action | Camera |
|---|---|---|
| 0-1 sn | Continuity hold — Central Square, eight blocks on the ground | Wide establishing |
| 1-4 sn | Noah crouches, touches a block, looks at it with curiosity | Wide |
| 4-7 sn | Arda enters from a rounded path, small steps toward Noah | Wide |
| 7-10 sn | Arda sits/kneels next to Noah, leans toward the blocks | Medium |
| 10-13 sn | Noah gestures over the block set, Arda nods eagerly | Medium |
| 13-15 sn | Shared happy look toward the blocks, both blink | Established composition |

---

## Natural Character Motion Rule

This shot should feel calm but alive. Characters may blink, breathe, smile, turn heads gently, make small hand gestures, take one or two soft steps, look at an object or at each other, point gently, and share a reaction. Do not freeze the characters, do not make it a static talking pose, do not leave long empty pauses or silent staring.

---

## Sound

- Birds chirping, soft wind
- Soft block-touch sounds
- Natural ambience only. No music. No background music.

---

## Lighting

Warm morning sunlight.

---

## Negative Prompt

```text
low quality, blurry, deformed, extra limbs, text, watermark, photorealistic, horror, scary, dark lighting, violence, weapons, sharp objects, extra characters, redesigned environment, static talking pose, characters frozen, no movement, long empty pause, silent staring, dead air, characters staring silently, background music, music, melody, song, soundtrack, musical bed, character pop-in, centered sudden appearance, new blocks, extra blocks, missing blocks, disappearing blocks, changing block colours, blocks turning into toys, furniture, stones, food, boxes, tools, letters or signs, tower taller than the children, giant tower, oversized tower, duplicated blocks, morphing blocks, floating blocks
```

---

## QA Checklist

Reference: 16_VIDEO_QA_SPEC.md

- [ ] Character integrity, consistency, and canonical scale (Arda slightly smaller than Noah) verified
- [ ] Object persistence — exactly 8 blocks visible, no more, no fewer
- [ ] Build area near the Big Pompom Tree visible and reachable
- [ ] Camera and lighting consistency (warm morning) verified
- [ ] Background objects stable; environment not reinterpreted
- [ ] Characters introduced by entrance/edge reveal, NOT centered pop-in
- [ ] Shot feels calm but alive; a beat every 2–3s; dialogue supported by physical action
- [ ] No music/soundtrack; natural ambience only
- [ ] **Gate A:** all 8 blocks + build area seeded and usable for later stacking; if any missing → NOT READY, fix this shot (not later prompts)
- [ ] Final frame usable as `@image1` for Shot 02 (no crop/close-up/lighting change/new object)

## Opening Hook

Colourful soft blocks tumble gently from the top of the frame, landing in a playful pile. Noah and Arda look up excitedly.
