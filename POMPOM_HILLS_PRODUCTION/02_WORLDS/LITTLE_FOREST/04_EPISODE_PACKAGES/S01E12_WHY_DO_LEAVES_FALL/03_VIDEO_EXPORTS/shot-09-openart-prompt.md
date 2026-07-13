# Shot 09 — OpenArt Prompt

## OpenArt Paste Prompt

@image1=sole source; exact first frame/1s hold. Locked camera; no reset/reframe/move. Both leaves stay visible, same hands/colors/positions; Opa fixed. Kiko slowly kneels in place viewing existing ground leaves; no new carpet/objects.
Kiko: The forest is so beautiful...
Kiko: It's like an autumn carpet!
Opa: The forest isn't losing its leaves. It's showing us its autumn colors.
Same Kiko/Opa voice IDs; no new/narrator. Lock @image1 warmth, brightness, saturation, contrast, sharpness. Leaf rustle/breeze; no music.

## Negative Prompt

leaf recolour/copy/loss/swap;leaf carpet/object pop-in;position jump;Opa loss;extra character/blue bird/text;tree hollow/cropped giant mushroom;cooling/desaturation;brightness/contrast/sharpness drift;shadow crush/highlight clip;softening/oversharpening;HDR/gloss/music

## Internal QA Checklist

OpenArt pasted character count: 787 / 800

### Verified Shot 08 Source

- [x] `@image1` is `01_SHOTS/normalized/shot-8-final-frame-normalized.png`, the approved normalized Shot 08 final frame and only visual source.
- [x] The normalized frame is byte-identical to `01_SHOTS/video/shot-8-final-frame.png` (SHA-256: `e03869a20d74b8a14568d03db686f1c1c2a7b69073b5984767419b7b491f728c`).
- [x] Kiko visibly holds exactly two leaves: one light golden leaf in her left hand and one brown-golden leaf in her right hand. No red leaf is visible.
- [x] Opa is visible at the lower right and must remain stable in that position.
- [x] The ground does not contain a dense leaf carpet; only the scattered ground elements already visible in `@image1` may remain.

### Continuity

- [ ] First visible frame matches `@image1` exactly and holds for the first second.
- [ ] Exact leaf count, colours, hands, orientations and positions persist from `@image1`.
- [ ] Neither leaf changes colour, duplicates, disappears, swaps hands or appears from nowhere.
- [ ] Kiko remains in the same ground location and kneels only gradually after the first second; no sudden kneeling reset or position jump.
- [ ] Both existing leaves remain visible in Kiko's hands throughout the kneeling action.
- [ ] Opa remains visible, stable and in the same lower-right position; no disappearance, pop-in or relocation.
- [ ] All visible trees, paths, stones, flowers, mushrooms, leaves and other environment objects remain exactly as shown in `@image1`.
- [ ] No dense leaf carpet, mass of leaves, flower, mushroom or other ground object is added.
- [ ] No extra character, blue bird, animal, text, sign, tree hollow or giant/cropped mushroom appears.

### Look, Camera, Voice and Sound

- [ ] Warmth, brightness, saturation, contrast and sharpness remain locked to `@image1` from first frame to last.
- [ ] No upward or downward brightness, contrast or sharpness drift; no cooling, desaturation, shadow crush, highlight clipping, softening, oversharpening, HDR or gloss.
- [ ] Camera remains locked; no establishing shot, separate first frame, reset, reframe, zoom, pan, tilt, tracking, widen or angle change.
- [ ] Dialogue is exact, starts early and refers only to the visible autumn scene.
- [ ] Exact same approved saved Kiko and Opa voice assets/presets/IDs are selected; no new or narrator voice.
- [ ] Only natural leaf rustle and a light breeze are generated; no music.

## OpenArt Settings

- Duration: 15 seconds
- `@image1`: `01_SHOTS/normalized/shot-8-final-frame-normalized.png`
- Prompt enhancer: Off
- Cinematic/auto camera: Off
