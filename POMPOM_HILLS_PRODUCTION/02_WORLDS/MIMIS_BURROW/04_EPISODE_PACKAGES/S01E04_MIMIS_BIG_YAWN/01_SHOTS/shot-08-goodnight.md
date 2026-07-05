# Shot 08 — Goodnight

## Shot Contract
- **Episode:** S01E04 — Mimi's Big Yawn
- **Shot:** 08 / 08
- **Duration:** 15 seconds
- **Characters:** Mimi, Kiko
- **Location:** Mimi's Burrow interior
- **Time:** Evening (warm interior glow)
- **Camera:** Preserve the exact Shot 07 final frame composition from @image1, static, no movement, no new angle
- **Purpose:** Mimi is already asleep on her pillow; Kiko stays beside her and whispers goodnight — warm ending

## Visual Continuity
**MUST match Shot 07 final frame (@image1) exactly:**
- Same warm blue interior walls
- Same soft green carpet
- Same round blue pillow (Mimi already asleep on it, exactly as in @image1)
- Same visible interior anchors from @image1. Preserve any visible window, shelf, or carrot box exactly if present. Do not add missing anchors.
- Same warm golden interior glow (no sudden night/darkness)

**Anchor rule:** Preserve only the interior anchors that are actually visible in @image1. If the approved Shot 07 final frame shows a window, preserve the window; if it shows a shelf, preserve the shelf; if it shows a carrot box, preserve the carrot box. Do not spawn missing anchors later. Do not require anchors that were not visible in @image1.

## Frame Support Check (Hard Gate — §0)
- **Required objects:** round blue pillow, interior walls, carpet, warm interior glow → all visible in interior @image1. ✅ seeded
- **Optional anchors:** preserve any visible window, shelf, or carrot box from @image1; do not spawn missing anchors.
- **No new objects needed.** No camera movement. No location change. No lighting jump (stays warm interior glow).
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

Mimi is already curled up on her round blue pillow, fully asleep, exactly as shown in @image1. Do not wake Mimi up. Do not make Mimi sit up or move off the pillow. Her breathing is slow and steady. Her ears are completely relaxed. She looks utterly peaceful, warm, and safe in her own little home.

Kiko is already standing beside the pillow, exactly as shown in @image1. Kiko does not kneel, walk away, or change position dramatically. She watches over her sleeping friend with a warm, gentle smile, gives a tiny quiet hand movement, and whispers goodnight. Kiko's expression shows care, contentment, and quiet happiness — she helped her sleepy friend find the coziest spot of all.

The shot must begin from the actual Shot 07 final frame. Mimi is already asleep on the pillow. Do not wake Mimi up. Do not make Mimi move off the pillow. Do not re-stage the settling action. Do not add blanket, bedding, stars, night sky, or new props. Kiko stays beside Mimi in the same position from @image1. Only tiny gentle motion is allowed: a small smile, a tiny hand movement, a soft whisper, and quiet breathing. The camera must remain in the exact same interior angle established by @image1. No new angle, no camera cut, no push-in, no pull-back, no reframe.

The warm golden interior glow stays soft and constant — it does NOT become night, and no stars appear. If a window is visible in @image1, it keeps its gentle, unchanged evening light. If no window is visible in @image1, do not create one. The whole scene holds a calm, cozy, safe bedtime feeling.

Environment remains identical to @image1. The round blue pillow, warm blue walls, soft green carpet, and warm interior glow remain unchanged. Preserve any visible interior anchor from @image1 exactly if present. Do not spawn missing anchors. Lighting stays warm interior glow throughout. No camera movement.

{style} = Pompom Hills v2.1, rounded preschool toy world, pastel colors, matte clay-plush surfaces, toddler-safe emotional clarity
{camera} = preserve the exact Shot 07 final frame composition from @image1, static, no movement, no new angle
{lighting} = warm golden interior glow (identical to @image1), soft warm-blue undertones, cozy, no night, no stars
```

## Dialogue

```
Kiko: (whisper) Goodnight, Mimi.
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
door, closed door, wooden door, rectangular door, dark hole, cave, tunnel, scary, dark, cold, harsh shadows, black shadows, night sky, stars, moonlight, daytime, bright sun, sudden night, darkness falling, camera movement, pan, track, zoom, dolly, pull-back, Dutch angle, fisheye, shaky, motion blur, text, logo, watermark, speech bubbles, captions, subtitles, new objects, new props, pillow not matching @image1, visible window changed, visible shelf changed, visible carrot box changed, new window spawning, new shelf spawning, new carrot box spawning, environment change, lighting change, exterior scene, outside, grass, tree, character scale change, Mimi awake, Mimi waking up, Mimi sitting up, Mimi moving off pillow, Mimi walking, re-staging settling action, Kiko leaving, Kiko kneeling, Kiko walking away, Kiko changing position dramatically, new camera angle, alternate angle, camera cut, camera push-in, camera pull-back, camera reframe, blanket spawning, bedding spawning, stars spawning, darkness falling, sharp edges, clutter, random props, metal, plastic, glass, modern objects, photorealistic, background music, soundtrack, melody, ending jingle, sound effects, dialogue text, wrong first frame, @image1 ignored, recreated scene, camera reset, camera searching, camera reframe, object spawning, late object appearance, new discovery object, background morphing, lighting drift, ghost character, duplicate character, transparent duplicate, double exposure, motion smear, character trail, song, musical bed, chime, music, magical sound effects, sparkles, bells, musical tones
```

## OpenArt Settings
- **Aspect Ratio:** 16:9
- **Seed:** (use consistent seed or empty)
- **@image1:** shot-07-settling-down final frame — Mimi already asleep on the pillow, Kiko already standing beside her; this is the exact first frame and continuity source
- **Model:** (use current production model)
- **Guidance Scale:** (standard production settings)

## Reject Kontrolü

**REJECT if ANY continuity breaks:**
- [ ] Lighting different from @image1 (not warm interior glow)
- [ ] Sudden night sky or stars spawned
- [ ] Pillow missing or changed, OR any visible interior anchor from @image1 changed/moved/disappeared, OR a missing anchor was newly spawned
- [ ] Interior walls/carpet not matching @image1
- [ ] Scene shows exterior/outside (must stay inside)
- [ ] Camera movement or pull-back (should be static)
- [ ] New objects spawned
- [ ] Character scale/position inconsistent
- [ ] Mimi not fully asleep/peaceful
- [ ] Kiko leaving or not watching caringly
- [ ] Shot does not start from the actual Shot 07 final frame
- [ ] Mimi wakes up, sits up, or moves off the pillow
- [ ] Kiko kneels, walks away, or changes position dramatically
- [ ] Shot re-stages the settling action
- [ ] Camera changes angle or reframes
- [ ] Blanket, bedding, stars, night sky, or new props appear

**APPROVE (practical evaluation — tiny micro-differences are acceptable):**

Küçük mikro farklar (hafif ışık titreşimi, minik doku farkı, karakterin doğal idle hareketi) kabul edilebilir. Değerlendirmede asıl bakılacak sorular:

- [ ] Shot gerçek Shot 07 final frame'inden mi başlıyor?
- [ ] Mimi baştan itibaren pillow'da uyuyor mu? (uyanmıyor/kalkmıyor/pillow'dan çıkmıyor)
- [ ] Mimi sadece küçük huzurlu nefes / uyku hareketi mi yapıyor?
- [ ] Kiko yanında kalıp sadece küçük nazik hareketle goodnight fısıldıyor mu? (diz çökmüyor/uzaklaşmıyor)
- [ ] Yeni obje / blanket / bedding / stars / night sky çıkmadı mı?
- [ ] Pillow, window, shelf, carrot box, walls, carpet ve glow tutarlı mı?
- [ ] Kamera aynı açıda mı kaldı?

> Bu sorular OK ise frame kullanılabilir. Literal piksel mükemmelliği aranmaz;
> yukarıdaki REJECT maddelerinden biri gerçekten kırılmadıkça frame'i mikro
> farklar yüzünden reddetme.

## Production Notes
- **Lighting lock:** MUST remain warm interior glow — no night/stars (avoids spawning risk)
- **Emotional resolution:** Sleepy problem solved, comfort found at home, caring friendship
- **Callback complete:** Big yawn (Shot 01) → peaceful sleep (Shot 08)
- **No pull-back:** Static camera maintains interior @image1 continuity
- **Episode conclusion:** Home is the coziest place; a friend helps you find comfort

## Continuity & Safety Locks
- **Character locks:**
  - **Kiko:** approved Kiko character design from the character reference / canon videos, scale 100. Preserve Kiko exactly; do not redesign Kiko and do not turn Kiko into a different creature.
  - **Mimi:** approved soft blue bunny-like character, scale 80, soft blue #90CAF9. Preserve Mimi exactly; sleepy expression, half-closed eyes, drooping ears.
  - Do not change character scale, identity, proportions, or colours.
- **Camera lock:** Keep the same camera position as @image1 — preserve the exact Shot 07 final frame composition. Static, no movement, no new angle. Do not create a new camera angle, cut, rotate, push in, pull back, pan, tilt, zoom, track, or reframe.
- **Lighting lock:** Match the lighting and colour grading of @image1 exactly (warm interior glow; no night, no stars).
- **Character presence:** Characters are already present at the beginning of the shot. Do not introduce any character after the shot has started.
- **Text safety:** No text. No subtitles. No speech bubbles. No captions.
