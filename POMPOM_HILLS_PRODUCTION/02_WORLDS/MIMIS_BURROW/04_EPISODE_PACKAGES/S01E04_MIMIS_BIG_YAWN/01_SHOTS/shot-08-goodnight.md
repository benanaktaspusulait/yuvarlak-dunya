# Shot 08 — Goodnight

## Shot Contract
- **Episode:** S01E04 — Mimi's Big Yawn
- **Shot:** 08 / 08
- **Duration:** 15 seconds
- **Characters:** Mimi, Kiko
- **Location:** Mimi's Burrow interior
- **Time:** Evening (warm interior glow)
- **Camera:** Medium 50mm, static, no movement
- **Purpose:** Mimi falls asleep peacefully on her pillow; Kiko whispers goodnight — warm ending

## Visual Continuity
**MUST match Shot 05 interior final frame (@image1) exactly:**
- Same warm blue interior walls
- Same soft green carpet
- Same round blue pillow (Mimi asleep on it)
- Same window, shelf, carrot box positions
- Same warm golden interior glow (no sudden night/darkness)

## Frame Support Check (Hard Gate — §0)
- **Required objects:** round blue pillow, interior walls, carpet, window → all visible in interior @image1. ✅ seeded
- **No new objects needed.** No camera movement. No location change. No lighting jump (stays warm interior glow).
- **Verdict:** SAFE

## Visual Prompt

```text
Use @image1 as the exact first frame and only visual continuity source. Do not reinterpret @image1. Do not use memory of any previous video or previous shot. Do not recreate the scene from description. Only preserve what is visible in @image1. Hold @image1 almost exactly for the first 1 second. Characters may blink, breathe, and make tiny natural idle motion. No camera movement during the first second.

Continuation from @image1: the cozy interior of Mimi's Burrow. Warm golden glow, warm blue walls, soft green carpet, round blue pillow.

Mimi is now curled up on her round blue pillow, fully asleep. Her breathing is slow and steady. Her ears are completely relaxed. She looks utterly peaceful, warm, and safe in her own little home.

Kiko kneels softly beside the pillow, watching over her sleeping friend with a warm, gentle smile. She gives a tiny, quiet wave and whispers goodnight. Kiko's expression shows care, contentment, and quiet happiness — she helped her sleepy friend find the coziest spot of all.

The warm golden interior glow stays soft and constant — it does NOT become night, and no stars appear. The little window keeps its gentle, unchanged evening light. The whole scene holds a calm, cozy, safe bedtime feeling.

Environment remains identical to @image1 — all interior objects in same positions. Lighting stays warm interior glow throughout. No camera movement.

{style} = Pompom Hills v2.1, rounded preschool toy world, pastel colors, matte clay-plush surfaces, toddler-safe emotional clarity
{camera} = stable 50mm preschool camera, medium shot, eye-level, static, no movement
{lighting} = warm golden interior glow (identical to @image1), soft warm-blue undertones, cozy, no night, no stars
```

## Dialogue

```
Kiko: (whisper) Goodnight, Mimi.
```

## Shot Breakdown (timed beats — calm but alive)

| Time | Action |
|---|---|
| 0-1 sn | Hold @image1 exactly. |
| 1-3 sn | Mimi's slow breathing is visible on the pillow. |
| 3-5 sn | Kiko leans slightly closer with a caring smile. |
| 5-7 sn | Kiko whispers: "Goodnight, Mimi." |
| 7-10 sn | Kiko gives a tiny quiet wave / soft hand movement. |
| 10-13 sn | Mimi's ears relax fully; breathing remains slow and peaceful. |
| 13-15 sn | Kiko smiles softly; final warm cozy hold. |

## Negative Prompt

```text
door, closed door, wooden door, rectangular door, dark hole, cave, tunnel, scary, dark, cold, harsh shadows, black shadows, night sky, stars, moonlight, daytime, bright sun, sudden night, darkness falling, camera movement, pan, track, zoom, dolly, pull-back, Dutch angle, fisheye, shaky, motion blur, text, logo, watermark, speech bubbles, captions, subtitles, new objects, new props, pillow not matching @image1, missing window, missing shelf, missing carrot box, environment change, lighting change, exterior scene, outside, grass, tree, character scale change, Mimi awake, Kiko leaving, sharp edges, clutter, random props, metal, plastic, glass, modern objects, photorealistic, background music, soundtrack, melody, ending jingle, sound effects, dialogue text, wrong first frame, @image1 ignored, recreated scene, camera reset, camera searching, camera reframe, object spawning, late object appearance, new discovery object, background morphing, lighting drift, ghost character, duplicate character, transparent duplicate, double exposure, motion smear, character trail, song, musical bed, chime
```

## OpenArt Settings
- **Aspect Ratio:** 16:9
- **Seed:** (use consistent seed or empty)
- **@image1:** shot-07-settling-down final frame (chain) — matches Shot 05 interior master
- **Model:** (use current production model)
- **Guidance Scale:** (standard production settings)

## Reject Kontrolü

**REJECT if ANY continuity breaks:**
- [ ] Lighting different from @image1 (not warm interior glow)
- [ ] Sudden night sky or stars spawned
- [ ] Pillow/window/shelf/carrot box missing or changed
- [ ] Interior walls/carpet not matching @image1
- [ ] Scene shows exterior/outside (must stay inside)
- [ ] Camera movement or pull-back (should be static)
- [ ] New objects spawned
- [ ] Character scale/position inconsistent
- [ ] Mimi not fully asleep/peaceful
- [ ] Kiko leaving or not watching caringly

**APPROVE only if:**
- [ ] Perfect continuity with interior @image1
- [ ] Mimi fully asleep and peaceful on her pillow
- [ ] Kiko watches with care and whispers goodnight
- [ ] Warm interior glow consistent (no night/stars)
- [ ] No new objects spawned
- [ ] Static camera, no movement
- [ ] Peaceful, cozy bedtime atmosphere

## Production Notes
- **Lighting lock:** MUST remain warm interior glow — no night/stars (avoids spawning risk)
- **Emotional resolution:** Sleepy problem solved, comfort found at home, caring friendship
- **Callback complete:** Big yawn (Shot 01) → peaceful sleep (Shot 08)
- **No pull-back:** Static camera maintains interior @image1 continuity
- **Episode conclusion:** Home is the coziest place; a friend helps you find comfort
