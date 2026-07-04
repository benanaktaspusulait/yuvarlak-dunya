# E05 — Shot 04 — Yellow Flowers

---

## Scene Context

| Alan | Değer |
| --- | --- |
| Episode | S01E05 — Colours Everywhere |
| Shot | 04 / 08 |
| Duration | 15 seconds |
| Location | Central Square |
| Characters | Kiko, Mimi |
| Time of Day | Morning |

---

## Continuity

This shot continues directly from Shot 03.

Kiko and Mimi are already present in the same Central Square set. They notice yellow
flowers in an existing rounded planter established in the same set.

Apply all Pompom Hills Visual Continuity Rules.

---

## Central Square Visual Identity

Same Central Square layout: Big Pompom Tree, rounded paths, coloured stepping-stone ring,
soft green grass, pastel bench, flower planters, warm morning daylight.

---

## Environment Anchors

- Same physical Central Square area from Shot 03.
- Big Pompom Tree remains the main background landmark.
- The yellow flower planter was seeded in the Central Square Friends Micro-Opening and
  preserved through the previous continuity frames, in an existing rounded planter
  already established nearby in the same Central Square set.
- Kiko and Mimi stay within the same path/bench/planter area.
- No world-to-world travel.

---

## Start Frame

Start from the approved exported final continuity frame from Shot 03. Preserve the
established composition, lighting, background objects, Kiko and Mimi positions and
character proportions.

Kiko and Mimi are already present at the beginning of the shot.

---

## Background Object Lock

The first frame defines the physical Central Square set. All visible benches, trees,
paths, flowerbeds, stepping stones, planters and distant houses remain stable throughout.

Do not introduce a new garden, new meadow, new field or new location.

## Central Square Safety Lock

Do not introduce camera reset, environment redesign, background morphing, new landmarks,
new paths, new buildings, roads, cars, traffic, shops with readable signs, fountain,
water feature, bridge, river, pond, crowd, extra characters, text, readable text,
captions, subtitles, speech bubbles, logo, title card or subscribe graphics.

Preserve the same Central Square layout, Big Pompom Tree position, rounded paths,
coloured stepping-stone ring, grass, benches, planters, bunting or flags if visible,
distant houses only at the far edge, warm morning daylight, Episode Colour Master from
Shot 01, Kiko and Mimi scale and identity, and stable preschool-safe motion.

## Required Global QA Locks

This shot must pass the global QA rules in `00-CORE/17_VIDEO_GENERATION_STANDARD.md` and `11-DOCS/16_VIDEO_QA_SPEC.md` for:

- Hard Background Lock
- Intra-Shot Character Continuity Lock
- Single Visible Path Rule
- Occlusion Is Not A Transition
- Camera Must Not Break Continuity
- First Second Continuity Hold
- Object Identity Lock

These locks are global production gates. Do not restate or weaken them locally. Keep the shot-specific guard below as the local application of the global rules.

## Shot-Specific Continuity Guard

The yellow flowers must stay inside the same rounded planter. Kiko and Mimi may look,
point or react, but they must not walk into the planter, behind the flowers, behind
planters, behind bushes or behind foreground flowerbeds. Use pointing and facial
reaction instead of movement. No garden transition, no Flower Hill and no new flower
field.


## Visual Prompt

```text
Kiko and Mimi already together in the same Central Square area, noticing yellow flowers in an existing rounded planter established in the same set beside the path, soft pastel blue bench still part of the same set if visible, Big Pompom Tree in background, warm morning daylight, gentle happy discovery, no other characters, {style} {camera} {lighting}

Use @image1 as the starting continuity frame from Shot 03.

Preserve Kiko, Mimi, the same Central Square layout, Big Pompom Tree, rounded paths, stepping-stone ring, existing planter, camera position, lighting and Episode Colour Master from @image1.

Match the lighting and colour grading exactly from the Shot 01 Episode Colour Master.

Do not display dialogue as on-screen text. No speech bubbles. No captions. No subtitles. No text.
The Central Square background is locked from the first frame; keep all visible benches, trees, paths, flowerbeds, stepping stones and landmarks stable throughout the shot.
```

---

## Reference Usage

OpenArt Reference Setup:

@image1 = approved exported final continuity frame from Shot 03.

Use `@image1` as the required starting continuity reference. Preserve the same Central
Square layout, lighting, camera position, Kiko and Mimi appearances, existing planter
and Episode Colour Master.

---

## Camera Direction

Begin from the Shot 03 continuity frame with no camera reset. The first 1 second should visually hold close to @image1 before new action begins. After that, the yellow flowers
become the action focus.

Use a calm child-eye-level medium-wide frame. Keep both characters visible. Do not
introduce new characters, new landmarks, new paths, roads, shops, fountains, water
features, gardens or a different Central Square area.

---

## Transition Continuity Rule

@image1 must be the approved final continuity frame of Shot 03.

The first frame should match `@image1` closely: same camera angle, same lens feel, same
character scale, same character positions, same Big Pompom Tree position, same path
layout, same lighting and same colour grading.

---

## Character Presence

Kiko and Mimi are already present at the beginning of the shot. Do not introduce any
character after the shot has started.

---

## Voice Continuity

Kiko and Mimi voices match the earlier speaking shots. Maintain identical voice identity,
pitch, timbre, warmth, pronunciation, accent and recording quality.

---

## Dialogue

```text
Kiko: Yellow flowers!
Mimi: So bright!
```

---

## Shot Breakdown

| Time | Action | Camera |
|---|---|---|
| 0-5 sn | First second holds near Shot 03 frame; Kiko notices the planter | Medium-wide |
| 5-10 sn | Kiko points gently to the yellow flowers | Stable |
| 10-15 sn | Mimi smiles and reacts | Medium-wide hold |

---

## Sound

- Soft breeze through leaves
- Tiny flower-discovery chime
- Gentle ambient morning

---

## Lighting

Warm morning daylight. Match the Shot 01 Episode Colour Master exactly. No exposure,
brightness, contrast, saturation or colour temperature drift. Do NOT desaturate.

---

## Negative Prompt

low quality, blurry, deformed, extra limbs, text, readable text, watermark, logo, title card, subtitles, captions, speech bubbles, subscribe button, like button, arrows, photorealistic, horror, scary, dark lighting, sunset, moonlight, night sky, stars, crickets, violence, weapons, sharp objects, traffic, cars, roads, modern city, crowded square, extra characters, non-canon characters, redesigned environment, camera reset, background morphing, disappearing objects, changing path, new buildings, readable signs, shops with text, complex city skyline, fountain, water feature, bridge, river, pond

teleporting character, disappearing character, character hidden behind bush, character walking through bushes, character clipping through objects, character emerging from opposite side, moving benches, moving trees, moving planters, shifting bushes, changing object positions, object morphing, layout changing, character occluded by foreground plants, walking through flowerbeds, walking through planters, walking through benches

intra-shot character disappearance, character disappearing within the same shot, character reappearing within the same shot, character teleporting within the same shot, character regenerating after occlusion, character hidden by bushes, character entering bushes, character emerging from bushes, character walking behind plants, character fully occluded, character path break, broken character continuity, character side-switching, character clipping through plants, character clipping through bushes, character walking through planters, foreground plants covering character, occlusion transition, hidden character transition

## QA Checklist

Reference: 11-DOCS/16_VIDEO_QA_SPEC.md

- [ ] `@image1` continuity preserved from Shot 03 final frame.
- [ ] The first 1 second visually holds close to `@image1` before the yellow flower discovery begins.
- [ ] Both Kiko and Mimi remain visible and consistent.
- [ ] Yellow flower planter was seeded in the Central Square Friends Micro-Opening and preserved through the previous continuity frames, in an existing rounded Central Square planter.
- [ ] No garden, meadow, Flower Hill, Rosie's Garden or alternate location appears.
- [ ] Big Pompom Tree and rounded paths remain stable.
- [ ] Camera does not reset.
- [ ] Lighting and Episode Colour Master preserved.
- [ ] No on-screen text, captions, logo or title card.
- [ ] No character disappears inside the same shot.
- [ ] No character reappears from a different side inside the same shot.
- [ ] No character is fully hidden by bushes, flowers, benches, trees, planters, flags or foreground plants.
- [ ] No occlusion is used as a transition.
- [ ] Character path remains continuously visible and physically possible.
- [ ] Character does not clip through bushes, planters, flowerbeds, benches, tree trunks, walls or foreground plants.
- [ ] All visible trees, benches, planters, bushes, paths, stepping stones and landmarks keep their position.
- [ ] No object changes identity, duplicates, disappears or shifts side.
- [ ] Camera movement does not hide a character or regenerate the environment.
- [ ] Full video has been watched for intra-shot character continuity, not only first and final frames.
