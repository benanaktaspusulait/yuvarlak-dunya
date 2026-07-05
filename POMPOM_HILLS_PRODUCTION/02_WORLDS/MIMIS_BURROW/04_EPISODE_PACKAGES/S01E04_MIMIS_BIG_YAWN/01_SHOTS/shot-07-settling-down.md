# Shot 07 — Settling Down

## Shot Contract
- **Episode:** S01E04 — Mimi's Big Yawn
- **Shot:** 07 / 08
- **Duration:** 15 seconds
- **Characters:** Mimi, Kiko
- **Location:** Mimi's Burrow interior
- **Time:** Evening (warm interior glow)
- **Camera:** Preserve the exact Shot 06 final frame composition from @image1, static, no movement, no new angle
- **Purpose:** Mimi is already on the pillow; she becomes sleepier and more peaceful while Kiko reassures her ("Rest now, Mimi.")

## Visual Continuity
**MUST match Shot 06 final frame (@image1) exactly:**
- Same warm blue interior walls
- Same soft green carpet
- Same round blue pillow (Mimi already lying on it, exactly as in @image1)
- Same visible interior anchors from @image1. Preserve any visible window, shelf, or carrot box exactly if present. Do not add missing anchors.
- Same warm golden interior glow

**Anchor rule:** Preserve only the interior anchors that are actually visible in @image1. If the approved Shot 06 final frame shows a window, preserve the window; if it shows a shelf, preserve the shelf; if it shows a carrot box, preserve the carrot box. Do not spawn missing anchors later. Do not require anchors that were not visible in @image1.

## Frame Support Check (Hard Gate — §0)
- **Required objects:** round blue pillow, interior walls, carpet, warm glow → all visible in interior @image1. ✅ seeded
- **Optional anchors:** preserve any visible window, shelf, or carrot box from @image1; do not spawn missing ones.
- **No new objects needed.** No camera movement. No location change.
- **Verdict:** SAFE

## Object Continuity Gate

Before generating this shot, check S01E04_OBJECT_CONTINUITY_MAP.md.

All required objects for this shot must already be visible in @image1.

The current action object must be visible and usable at its existing size, shape, position, and distance.

Do not create, enlarge, move, multiply, reshape, replace, or reposition any object to satisfy the action.

If an object is visible but not usable for the planned action, simplify the character action instead of changing the environment.

Characters adapt to the environment.
The environment does not adapt to the characters.

## Visual Prompt

```text
Use @image1 as the exact first frame and only visual continuity source. Do not reinterpret @image1. Do not use memory of any previous video or previous shot. Do not recreate the scene from description. Only preserve what is visible in @image1. Hold @image1 almost exactly for the first 1 second. Characters may blink, breathe, and make tiny natural idle motion. No camera movement during the first second.

Use only the objects already visible in @image1.
Do not generate new objects.
Do not enlarge, move, multiply, reshape, or reposition any environment object.
The current action must adapt to the existing @image1 layout.
Characters may move; environment objects may not.

Continuation from @image1: the cozy interior of Mimi's Burrow. Warm golden glow, warm blue walls, soft green carpet, round blue pillow.

Mimi is already lying on her round blue pillow at the start of the shot, exactly as shown in @image1. Do not make Mimi stand up, walk, or get onto the pillow again. She only makes tiny sleepy settling motions: a small breath, a slight ear droop, a tiny snuggle into the plush pillow. She gives one last small, sleepy yawn — a gentle echo of the big yawn from the start of the episode. Her eyes grow heavier.

Kiko is already nearby, exactly as shown in @image1. Kiko does not walk across the room or change position dramatically. Kiko makes only a small, gentle caring gesture near Mimi, such as a tiny hand movement or soft reassuring lean, then quietly says: "Rest now, Mimi." Mimi snuggles in, warm and safe in her own little home.

The shot must begin from the actual Shot 06 final frame. Mimi is already on the pillow. This shot is not about getting onto the pillow; it is about becoming sleepier and more peaceful. Do not re-stage the previous action. Do not restart the settling action. Do not move Mimi off the pillow. Do not move, resize, rotate, or recreate the pillow.

The camera must remain in the exact same interior master angle established by @image1. No new angle, no camera cut, no push-in, no pull-back, no reframe.

Environment remains identical to @image1. The round blue pillow, warm blue walls, soft green carpet, and warm interior glow remain unchanged. Preserve any visible interior anchor from @image1 exactly if present. Do not spawn missing anchors, new bedding, or blanket. No camera movement.

{style} = Pompom Hills v2.1, rounded preschool toy world, pastel colors, matte clay-plush surfaces, toddler-safe emotional clarity
{camera} = preserve the exact Shot 06 final frame composition from @image1, static, no movement, no new angle
{lighting} = warm golden interior glow (identical to @image1), soft warm-blue undertones, cozy
```

## Dialogue

```
Mimi: (soft sleepy yawn)
Kiko: Rest now, Mimi.
```

## Sound Design

No music.
No background music.
No melody.
No song.
No soundtrack.
No musical bed.
No chime.
No ending jingle.
No magical sound effects.
No sparkles, bells, or musical tones.

Use natural ambience only.

Exterior shots:
Use very soft evening meadow ambience:
- gentle breeze
- soft grass rustle
- tiny distant meadow insects
- subtle flower meadow atmosphere
- soft character breathing and tiny movement sounds

Interior shots:
Use very soft cozy room ambience:
- warm quiet room tone
- soft character breathing
- tiny fabric / pillow movement sounds
- gentle footstep or paw movement only when characters move

Keep all ambience quiet, warm, preschool-safe, and bedtime-friendly.
Do not let ambience become loud, dramatic, scary, windy, musical, or distracting.

## Negative Prompt

```text
door, closed door, wooden door, rectangular door, dark hole, cave, tunnel, scary, dark, cold, harsh shadows, black shadows, night sky, stars, moonlight, daytime, bright sun, camera movement, pan, track, zoom, dolly, Dutch angle, fisheye, shaky, motion blur, text, logo, watermark, speech bubbles, captions, subtitles, new objects, new props, pillow not matching @image1, visible window changed, visible shelf changed, visible carrot box changed, new window spawning, new shelf spawning, new carrot box spawning, environment change, lighting change, exterior scene, outside, grass, tree, character scale change, Mimi wide awake, Kiko rough movement, Mimi standing up, Mimi walking, Mimi getting onto pillow again, Mimi starting away from pillow, re-staging previous action, repeated settling action, pillow moved, pillow resized, pillow rotated, new camera angle, alternate angle, camera cut, camera push-in, camera pull-back, camera reframe, Kiko walking across room, Kiko changing position dramatically, sharp edges, clutter, random props, metal, plastic, glass, modern objects, photorealistic, blanket spawning, complex bedding, wrong first frame, @image1 ignored, recreated scene, camera reset, camera searching, camera reframe, object spawning, late object appearance, new discovery object, background morphing, lighting drift, ghost character, duplicate character, transparent duplicate, double exposure, motion smear, character trail, music, background music, melody, song, soundtrack, musical bed, chime, ending jingle, magical sound effects, sparkles, bells, musical tones
```

## OpenArt Settings
- **Aspect Ratio:** 16:9
- **Seed:** (use consistent seed or empty)
- **@image1:** shot-06-cozy-pillow final frame — Mimi already lying on the pillow; this is the exact first frame and continuity source
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
- [ ] Mimi starts standing or away from the pillow
- [ ] Mimi walks again before settling
- [ ] Shot re-stages the Shot 06 pillow action
- [ ] Pillow position/size/rotation changes
- [ ] Camera changes angle or reframes
- [ ] Kiko moves dramatically instead of making a small caring gesture

**APPROVE (practical evaluation — tiny micro-differences are acceptable):**

Küçük mikro farklar (hafif ışık titreşimi, minik doku farkı, karakterin doğal idle hareketi) kabul edilebilir. Değerlendirmede asıl bakılacak sorular:

- [ ] Shot gerçek Shot 06 final frame'inden mi başlıyor?
- [ ] Mimi baştan itibaren pillow'un üstünde mi kalıyor? (tekrar ayağa kalkmıyor/yürümüyor)
- [ ] Mimi sadece küçük uykulu settling hareketleri mi yapıyor?
- [ ] Kiko yanında kalıp küçük, nazik bir tepki mi veriyor? (odada yürümüyor)
- [ ] Yeni obje / blanket / bedding çıkmadı mı?
- [ ] Pillow, window, shelf, carrot box, walls, carpet ve glow tutarlı mı?
- [ ] Kamera aynı açıda mı kaldı?

> Bu sorular OK ise frame kullanılabilir. Literal piksel mükemmelliği aranmaz;
> yukarıdaki REJECT maddelerinden biri gerçekten kırılmadıkça frame'i mikro
> farklar yüzünden reddetme.

## Production Notes
- **Callback:** Small sleepy yawn echoes the opening big yawn
- **No spawning:** Only the seeded pillow is used — no new blanket
- **Emotional beat:** Tenderness, care, safety
- **Setup for final shot:** Mimi curled on pillow, nearly asleep

## Continuity & Safety Locks
- **Character locks:**
  - **Kiko:** approved Kiko character design from the character reference / canon videos, scale 100. Preserve Kiko exactly; do not redesign Kiko and do not turn Kiko into a different creature.
  - **Mimi:** approved soft blue bunny-like character, scale 80, soft blue #90CAF9. Preserve Mimi exactly; sleepy expression, half-closed eyes, drooping ears.
  - Do not change character scale, identity, proportions, or colours.
- **Camera lock:** Keep the same camera position as @image1 — preserve the exact Shot 06 final frame composition. Static, no movement, no new angle. Do not create a new camera angle, cut, rotate, push in, pull back, pan, tilt, zoom, track, or reframe.
- **Lighting lock:** Match the lighting and colour grading of @image1 exactly (warm interior glow).
- **Character presence:** Characters are already present at the beginning of the shot. Do not introduce any character after the shot has started.
- **Text safety:** No text. No subtitles. No speech bubbles. No captions.
