# Season Begins — Shot 01 — Kiko's Welcome (World Open)

## Scene Context
| Alan | Değer |
| --- | --- |
| Video | Pompom Hills — The Season Begins |
| Shot | 01 / 06 |
| Duration | 12 seconds |
| Location | Central Square |
| Characters | **Kiko only** |
| Time of Day | Warm morning |

## OpenArt vs Edit Instruction Boundary

This file contains both OpenArt generation instructions and production/editing notes.

When generating the video in OpenArt, use only:
- Visual Prompt
- Camera Direction
- Dialogue
- Natural Character Motion Rule
- Lighting
- Negative Prompt

Do NOT paste production/editing sections into OpenArt.

The following sections are for production review and editing only:
- First-Frame Generation Gate
- No Salvage Before Output Rule
- Edit-Safe Opening and Ending Rule
- Post-Production Transition Note
- QA Checklist
- Final Internal Consistency QA

OpenArt must generate only this single standalone shot.
Transitions between worlds are handled later in editing, not inside OpenArt.

## Location Lock Summary
Location is Central Square only.
Approved visible environment: Big Pompom Tree, rounded paths, pastel houses only if already part of the world reference.
No other location may appear.
No cutaway, no transition to another place, no alternate Central Square design.

## ONE-Character Rule
This shot contains **only Kiko**. No other character appears. This is an independent
generation (world ref + Kiko ref), not chained from another shot.
Independent generation means this shot does not inherit characters, props, camera movement, or background objects from any previous shot. It must obey only this shot document and its assigned references.

## Background Object Lock
Central Square environment is locked: Big Pompom Tree, rounded paths, pastel houses stay stable
in identity, position and scale. Only Kiko moves. Do not add other characters or new objects.

## No Surprise Elements Rule

No surprise elements may appear at any point in this shot.

The character list is locked from the first frame. Only Kiko may appear. No extra character, background character, crowd member, animal, toy creature, duplicate character, partial character, shadow character, silhouette character, reflection character, or off-screen entering character may appear.

The object list is locked from the first frame. Only the approved visible Central Square environment listed in this shot may appear. Do not introduce new props, new toys, new signs, new flowers, new furniture, new stones, new houses, new paths, new decorations, new lights, new clouds, new doors, new windows, or any new background detail during the shot.

If an object or character is not visible or clearly established in the first frame, it must not appear later.

The camera must not pan, zoom, pull back, tilt, orbit, or reframe in order to reveal new objects or characters. The shot must adapt to the first frame layout.

## Approved Characters and Props

### Approved characters
- Kiko

### Forbidden characters
- Mimi, Noah, Arda, Luca, Opa
- any unnamed extra character
- any background crowd
- any duplicate version of Kiko

### Approved props
- None — no props are used in this shot
- Central Square environment only: Big Pompom Tree, rounded paths, pastel houses (only if already part of the world reference)

### Forbidden props
- any new prop not visible in the first frame
- any blocks, toys, or animals
- any sign, written text, logo, caption, speech bubble, subtitle, or watermark
- any object that was not listed as approved for this shot

## Visual Prompt
```text
Use Central Square (world reference) as the LOCKED environment. Insert Kiko (character reference) alone. Wide establishing shot of Central Square in warm morning light, the Big Pompom Tree behind. Kiko stands near the center on a clear rounded path, looks toward the viewer, gives a warm bright wave hello. Only Kiko is present. Handcrafted preschool toy-set look, rounded shapes, {style} {camera} {lighting}

No props are used in this shot. No other character appears in the background, foreground, edge of frame, window, path, reflection, or shadow.

Do not display dialogue as on-screen text. No speech bubbles. No captions. No subtitles. No text.
Central Square background locked from the first frame; keep all trees, paths and landmarks stable.
```

## Camera Direction
Wide 35mm child-eye-level composition, height 0.85m. The camera remains locked in the same angle. No pan, no zoom, no pull-back, no push-in, no tilt, no orbit, no reframe, no camera reveal. Kiko's wave and body motion provide the action; the camera does not move to create interest.

## Dialogue
```
Kiko: Hi! Welcome to Pompom Hills!
```

## Shot Breakdown
| Time | Action | Camera |
|---|---|---|
| 0-2 sn | Central Square establishes, warm morning light | Wide |
| 2-5 sn | Kiko is seen on a rounded path, turns toward viewer | Wide |
| 5-8 sn | Kiko waves brightly, tiny in-place happy body bob without changing position | Locked wide / readable wide |
| 8-11 sn | Kiko: "Hi! Welcome to Pompom Hills!" | Same locked composition |
| 11-12 sn | Warm smile, gentle blink, inviting gesture. Final 0.5s: calm still hold. | Same locked composition |

## Natural Character Motion Rule
Calm but alive: small wave, blink, breathe, tiny in-place happy body bob, warm smile, look to viewer. No walking, no running, no jumping, no hopping, no repositioning, no crossing, no long pause.

## Sound
- Birds chirping, soft wind
- Natural ambience only. No music. No background music.

## Lighting
Warm morning sunlight, soft ambient, no hard shadows.

## Reference Usage
- World Reference: Central Square (`POMPOM_HILLS_PRODUCTION/02_WORLDS/CENTRAL_SQUARE/`)
- Character Reference: Kiko sheet. Supplied by production workflow.

## Reference Role Rule
Reference images have separate jobs and must not be mixed.

- The world/location reference controls the environment, camera feel, scale, lighting mood, background identity, and location layout.
- The character reference controls only character identity, proportions, colors, face, body design, and approved scale.
- Character references must NOT bring their original background, props, lighting, pose, camera angle, or extra objects into this shot.
- World references must NOT redesign the characters.
- If references conflict, the shot document controls the allowed characters, props, location, camera, and movement.
- Do not combine references into a collage.
- Do not import props, furniture, scenery, background characters, or lighting from the wrong reference.

## Negative Prompt
```text
multiple characters, other characters, two characters, group, crowd, Mimi, Noah, Arda, Luca, Opa, low quality, blurry, deformed, extra limbs, text, watermark, photorealistic, horror, scary, dark lighting, harsh shadows, violence, weapons, sharp objects, redesigned character, wrong scale, character drift, redesigned environment, cluttered background, static talking pose, frozen character, long empty pause, background music, music, melody, song, soundtrack, musical bed, surprise character, background character, partial character, character entering later, extra prop, new prop, animal, toy creature, duplicate Kiko, reflection character, shadow character, surprise object, surprise prop, character appearing later, duplicate character, duplicate body, extra character, new object, object appearing later, object entering later, camera revealing new object, camera revealing new character, jumping, hopping, walking, running, repositioning, character displacement, bouncing away
```

## First-Frame Generation Gate

Before generating the full video, check the first still / cheap preview.

APPROVE only if:
- approved character count is correct from the first frame
- every approved character identity is correct
- every approved character scale is correct
- no extra character appears
- no duplicate character appears
- no surprise prop or object appears
- the approved location is correct
- camera framing does not require a reveal
- lighting matches the shot document
- no on-screen text, caption, subtitle, watermark, or logo appears

REJECT immediately if:
- any character is missing
- any extra or duplicate character appears
- any surprise object appears
- the world is redesigned
- character scale is wrong
- camera is too close, too wide, cropped, or needs to move to show the subject
- lighting shifts to night, sunset, dramatic orange, or an unapproved mood
- the first frame cannot support the full shot without new elements appearing later

## No Salvage Before Output Rule

Do not plan to fix missing characters, missing props, wrong scale, wrong location, or wrong lighting in later seconds of the same video.

If the first frame is wrong, reject the generation.

Do not rely on:
- characters entering later
- camera pulling back to reveal missing characters
- props appearing later
- lighting correcting itself later
- the model improving the layout over time

For this Season Begins video, the first frame must already contain the approved character set and approved visible elements for that shot.

## Edit-Safe Opening and Ending Rule

This shot will be edited together with other separately generated shots.

The first 0.5 seconds must be visually stable:
- no sudden character movement
- no new gesture starting immediately
- no camera movement
- no character entering
- no object appearing
- location already clear from the first frame

The final 0.5 seconds must be a calm edit-safe hold:
- no new gesture starts
- no character changes position
- no object appears
- no camera movement
- no abrupt expression change
- no sudden lighting change

This allows a soft 0.4–0.6 second transition in editing.

## Post-Production Transition Note

This shot ends in Central Square and transitions to Shot 02 at Mimi's Burrow.

Recommended edit transition after this shot:
- warm cream dip
- 0.4–0.6 seconds
- no text
- no logo
- no sparkle
- no magical effect
- no wipe
- no camera zoom

Audio:
- gently crossfade Central Square outdoor ambience into Mimi's Burrow cozy ambience
- no music
- no chime
- no whoosh
- no hard audio cut

Important:
This transition is done in editing only.
Do not ask OpenArt to generate the transition.
Do not include transition wording inside the OpenArt Visual Prompt.

## QA Checklist
- [ ] **Exactly ONE character (Kiko) in frame — no others**
- [ ] Kiko identity/scale correct (100 units)
- [ ] Central Square environment stable, warm morning light
- [ ] Warm wave hello reads clearly to viewer
- [ ] No on-screen text; no music
- [ ] Calm but alive; a beat every 2–3s
- [ ] Final frame warm and calm hold
- [ ] Approved character count is correct from the first frame
- [ ] No extra character appears at any time
- [ ] No duplicate character appears at any time
- [ ] No surprise prop/object appears at any time
- [ ] No object appears later that was not visible or approved in the first frame
- [ ] Camera does not reveal new characters or objects
- [ ] Background remains locked and stable
- [ ] No internal contradiction between Visual Prompt, Approved Props, Camera Direction, Lighting, Negative Prompt, and Shot Breakdown
- [ ] First 0.5s is stable and edit-safe
- [ ] Final 0.5s is calm and transition-safe
- [ ] No new action begins in the final 0.5s
- [ ] Post-production transition note is present
- [ ] Transition instructions are not inside the OpenArt Visual Prompt

## Final Internal Consistency QA
- [ ] Character count matches the shot title and Scene Context
- [ ] Approved Characters and Props list matches the Visual Prompt
- [ ] Forbidden Characters list does not forbid an approved character
- [ ] Negative Prompt does not forbid an approved character
- [ ] Camera Direction does not contradict No Surprise Elements Rule
- [ ] Lighting section matches Visual Prompt and Shot Breakdown
- [ ] Shot Breakdown does not imply character entrance, reveal, or repositioning unless explicitly approved
- [ ] Reference Role Rule prevents wrong background/props from character references
- [ ] First-Frame Generation Gate is clear
- [ ] The shot can be generated without relying on later fixes

## Scale
Kiko = 100 units. Small, childlike within Central Square but readable (`00-CORE/VARIABLES.md`).

## Scale Lock Summary
Character scale must follow the approved Pompom Hills scale system.

- Kiko = 100 units
- Mimi = 80 units
- Noah = 100 units
- Arda = 85 units
- Luca = 100 units
- Opa = 120 units, low-staged so he does not dominate the frame

Only Kiko appears in this shot.

Do not enlarge a character to fill the frame.
Do not shrink a character because there are multiple characters.
Do not make Opa giant.
Do not make Mimi same size as Kiko/Noah/Luca.
Do not make Arda same size as the 100-unit characters.
Do not change scale during the shot.

## Final Production Reminder

This shot is generated as a clean standalone OpenArt video.

Do not generate transitions inside OpenArt.

Do not combine this world with the previous or next world.

Do not paste editing notes into OpenArt.

World changes are handled later in editing using the Post-Production Transition Note.
