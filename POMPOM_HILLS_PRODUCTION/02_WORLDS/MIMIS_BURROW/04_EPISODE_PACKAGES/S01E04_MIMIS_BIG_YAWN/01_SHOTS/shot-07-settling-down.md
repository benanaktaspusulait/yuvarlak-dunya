# Shot 07 — Settling Down

## Shot Contract
- **Episode:** S01E04 — Mimi's Big Yawn
- **Shot:** 07 / 08
- **Duration:** 15 seconds
- **Characters:** Mimi, Kiko
- **Location:** Mimi's Burrow interior
- **Time:** Evening (warm interior glow)
- **Camera:** Medium 50mm, static, no movement
- **Purpose:** Mimi lies down fully on the pillow; Kiko gently helps her settle

## Visual Continuity
**MUST match Shot 05 interior final frame (@image1) exactly:**
- Same warm blue interior walls
- Same soft green carpet
- Same round blue pillow (Mimi now lying on it)
- Same visible interior anchors from @image1. Preserve any visible window, shelf, or carrot box exactly if present. Do not add missing anchors.
- Same warm golden interior glow

**Anchor rule:** Preserve only the interior anchors that are actually visible in @image1. If the approved Shot 05 interior master frame shows a window, preserve the window; if it shows a shelf, preserve the shelf; if it shows a carrot box, preserve the carrot box. Do not spawn missing anchors later. Do not require anchors that were not visible in @image1.

## Frame Support Check (Hard Gate — §0)
- **Required objects:** round blue pillow, interior walls, carpet, warm glow → all visible in interior @image1. ✅ seeded
- **Optional anchors:** preserve any visible window, shelf, or carrot box from @image1; do not spawn missing ones.
- **No new objects needed.** No camera movement. No location change.
- **Verdict:** SAFE

## Visual Prompt

```text
Use @image1 as the exact first frame and only visual continuity source. Do not reinterpret @image1. Do not use memory of any previous video or previous shot. Do not recreate the scene from description. Only preserve what is visible in @image1. Hold @image1 almost exactly for the first 1 second. Characters may blink, breathe, and make tiny natural idle motion. No camera movement during the first second.

Continuation from @image1: the cozy interior of Mimi's Burrow. Warm golden glow, warm blue walls, soft green carpet, round blue pillow.

Mimi lies down fully on her round blue pillow, curling up softly into the plush surface. Her body relaxes deeper into the cozy spot. She gives one last small, sleepy yawn — a gentle echo of the big yawn from the start of the episode.

Kiko steps close and gently helps Mimi settle — smoothing the pillow, giving a soft, caring pat. Kiko's movements are slow and tender, like tucking in a friend. Mimi's eyes grow heavier. She snuggles in, warm and safe in her own little home.

Environment remains identical to @image1. The round blue pillow, warm blue walls, soft green carpet, and warm interior glow remain unchanged. Preserve any visible interior anchor from @image1 exactly if present. Do not spawn missing anchors, new bedding, or blanket. No camera movement.

{style} = Pompom Hills v2.1, rounded preschool toy world, pastel colors, matte clay-plush surfaces, toddler-safe emotional clarity
{camera} = stable 50mm preschool camera, medium shot, eye-level, static, no movement
{lighting} = warm golden interior glow (identical to @image1), soft warm-blue undertones, cozy
```

## Dialogue

```
Mimi: (soft sleepy yawn)
Kiko: Rest now, Mimi.
```

## Negative Prompt

```text
door, closed door, wooden door, rectangular door, dark hole, cave, tunnel, scary, dark, cold, harsh shadows, black shadows, night sky, stars, moonlight, daytime, bright sun, camera movement, pan, track, zoom, dolly, Dutch angle, fisheye, shaky, motion blur, text, logo, watermark, speech bubbles, captions, subtitles, new objects, new props, pillow not matching @image1, visible window changed, visible shelf changed, visible carrot box changed, new window spawning, new shelf spawning, new carrot box spawning, environment change, lighting change, exterior scene, outside, grass, tree, character scale change, Mimi wide awake, Kiko rough movement, sharp edges, clutter, random props, metal, plastic, glass, modern objects, photorealistic, blanket spawning, complex bedding, wrong first frame, @image1 ignored, recreated scene, camera reset, camera searching, camera reframe, object spawning, late object appearance, new discovery object, background morphing, lighting drift, ghost character, duplicate character, transparent duplicate, double exposure, motion smear, character trail, music, background music, melody, song, soundtrack, musical bed, chime
```

## OpenArt Settings
- **Aspect Ratio:** 16:9
- **Seed:** (use consistent seed or empty)
- **@image1:** shot-06-cozy-pillow final frame (chain) — matches Shot 05 interior master
- **Model:** (use current production model)
- **Guidance Scale:** (standard production settings)

## Reject Kontrolü

**REJECT if ANY continuity breaks:**
- [ ] Pillow not matching @image1 position/size/color
- [ ] Any visible interior anchor from @image1 changed, moved, disappeared, or a missing anchor was newly spawned
- [ ] Interior walls/carpet not matching @image1
- [ ] Lighting different from @image1 (not warm interior glow)
- [ ] Scene shows exterior/outside (must stay inside)
- [ ] Camera movement (should be static)
- [ ] New objects spawned (no new blanket/bedding)
- [ ] Character scale/position inconsistent
- [ ] Mimi wide awake (should be drifting to sleep)
- [ ] Kiko's movements not gentle/caring

**APPROVE only if:**
- [ ] Perfect continuity with interior @image1
- [ ] Mimi lies down fully and snuggles into the pillow
- [ ] Kiko gently helps her settle
- [ ] No new objects spawned
- [ ] Static camera, no movement
- [ ] Warm interior glow consistent

## Production Notes
- **Callback:** Small sleepy yawn echoes the opening big yawn
- **No spawning:** Only the seeded pillow is used — no new blanket
- **Emotional beat:** Tenderness, care, safety
- **Setup for final shot:** Mimi curled on pillow, nearly asleep

## Continuity & Safety Locks
- **Character locks:** Kiko (scale 100, coral pink #F8BBD0), Mimi (scale 80, soft blue #90CAF9). Do not change character scale or colours.
- **Camera lock:** Keep the same camera position as @image1 (preserve the interior composition; no reframe).
- **Lighting lock:** Match the lighting and colour grading of @image1 exactly (warm interior glow).
- **Character presence:** Characters are already present at the beginning of the shot. Do not introduce any character after the shot has started.
- **Text safety:** No text. No subtitles. No speech bubbles. No captions.
