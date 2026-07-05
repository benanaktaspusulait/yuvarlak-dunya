# Season Begins — Shot 02 — Mimi's Cozy Hello

## Scene Context
| Alan | Değer |
| --- | --- |
| Video | Pompom Hills — The Season Begins |
| Shot | 02 / 06 |
| Duration | 12 seconds |
| Location | Mimi's Burrow (entrance / warm interior glow) |
| Characters | **Mimi only** |
| Time of Day | Warm daytime (cozy interior glow) |

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
Location is Mimi's Burrow entrance only.
Approved visible environment: round blue burrow entrance, warm interior glow, exactly 3 grey stepping stones, soft grass, existing flowers.
No alternate burrow, no cave, no tunnel, no bedroom, no house interior, no new room.

## ONE-Character Rule
Only Mimi. No other character. Independent generation (Mimi's Burrow ref + Mimi ref).
Independent generation means this shot does not inherit characters, props, camera movement, or background objects from any previous shot. It must obey only this shot document and its assigned references.

## Background Object Lock
Mimi's Burrow identity locked: round blue entrance (#90CAF9), warm interior glow, exactly 3 grey
stepping stones, green grass, flowers on top. Only Mimi moves. No new objects, no other characters.

## No Surprise Elements Rule

No surprise elements may appear at any point in this shot.

The character list is locked from the first frame. Only Mimi may appear. No extra character, background character, crowd member, animal, toy creature, duplicate character, partial character, shadow character, silhouette character, reflection character, or off-screen entering character may appear.

The object list is locked from the first frame. Only the approved burrow elements listed in this shot may appear. Do not introduce new props, new toys, new signs, new flowers, new furniture, new stones, new houses, new paths, new decorations, new lights, new clouds, new doors, new windows, or any new interior/exterior detail during the shot.

If an object or character is not visible or clearly established in the first frame, it must not appear later.

The camera must not pan, zoom, pull back, tilt, orbit, or reframe in order to reveal new objects or characters. The shot must adapt to the first frame layout.

## Approved Characters and Props

### Approved characters
- Mimi

### Forbidden characters
- Kiko, Noah, Arda, Luca, Opa
- any unnamed extra character
- any background crowd
- any duplicate version of Mimi

### Approved props
- Only the burrow elements already listed: round blue entrance, warm interior glow, exactly 3 grey stepping stones, soft grass, and existing flowers belonging to the burrow design

### Forbidden props
- any new door, new window, or extra stones
- any new pillow, blanket, lamp, or interior furniture
- turning the burrow into a cave, tunnel, dark hole, house, or bedroom
- any sign, written text, logo, caption, speech bubble, subtitle, or watermark
- any object that was not listed as approved for this shot

## Visual Prompt
```text
Use Mimi's Burrow (world reference) as the LOCKED environment. Insert Mimi (character reference) alone. Cozy view at the round blue burrow entrance with warm cozy interior glow inside, three grey stepping stones, soft green grass and flowers on top. Mimi peeks out softly, sleepy and gentle, gives a small warm wave to the viewer. Only Mimi is present. Handcrafted preschool toy-set look, {style} {camera} {lighting}

Only the burrow elements already listed are allowed: round blue entrance, warm cozy glow, exactly 3 grey stepping stones, soft grass, and existing flowers. No new objects appear inside or outside the burrow. No other character appears in the background, foreground, edge of frame, reflection, or shadow.

Do not display dialogue as on-screen text. No speech bubbles. No captions. No subtitles. No text.
Burrow background locked; round blue entrance, 3 stones and flowers stay stable.
```

## Camera Direction
Medium, low child-eye-level composition. The camera remains locked in the same angle. No pan, no zoom, no pull-back, no push-in, no tilt, no orbit, no reframe, no camera reveal. Mimi's peek, wave, blink, and ear-flop provide the action; the camera does not move.

## Dialogue
```
Mimi: Hello... come in, it's cozy here.
```

## Shot Breakdown
| Time | Action | Camera |
|---|---|---|
| 0-2 sn | Burrow entrance, warm glow, soft continuity | Medium |
| 2-5 sn | Mimi peeks out gently, sleepy blink | Medium |
| 5-8 sn | Mimi gives a small soft wave | Medium |
| 8-11 sn | Mimi: "Hello... come in, it's cozy here." | Medium |
| 11-12 sn | Soft cozy smile, ear-flop. Final 0.5s: calm still hold. | Medium |

## Natural Character Motion Rule
Calm but alive: soft wave, sleepy blink, gentle ear-flop, warm smile. No freeze, no long pause.

## Sound
- Soft indoor warm ambience, very light outdoor birds
- Natural ambience only. No music. No background music.

## Lighting
Warm cozy interior glow + soft daylight. Never dark, cold, sunset, orange, evening, or night.

## Reference Usage
- World Reference: Mimi's Burrow (`POMPOM_HILLS_PRODUCTION/02_WORLDS/MIMIS_BURROW/`)
- Character Reference: Mimi sheet.

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
multiple characters, other characters, two characters, group, crowd, Kiko, Noah, Arda, Luca, Opa, door, cave, tunnel, dark hole, dark interior, cold interior, low quality, blurry, deformed, extra limbs, text, watermark, photorealistic, horror, scary, harsh shadows, redesigned character, wrong scale, character drift, redesigned environment, entrance not round, entrance not blue, background music, music, melody, song, soundtrack, musical bed, extra stones, new pillow, blanket, lamp, furniture, new door, new window, new interior objects, surprise character, background character, duplicate Mimi, surprise object, surprise prop, character appearing later, character entering later, duplicate character, duplicate body, partial character, shadow character, reflection character, extra animal, toy creature, new object, new prop, object appearing later, object entering later, camera revealing new object, camera revealing new character, sunset, orange sky, evening, night, golden hour, dramatic golden light
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

This shot ends at Mimi's Burrow and transitions back to Shot 03 in Central Square.

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
- gently crossfade cozy burrow ambience into Central Square outdoor ambience
- no music
- no chime
- no whoosh
- no hard audio cut

Important:
This transition is done in editing only.
Do not ask OpenArt to generate the transition.
Do not include transition wording inside the OpenArt Visual Prompt.

## QA Checklist
- [ ] **Exactly ONE character (Mimi) in frame — no others**
- [ ] Mimi identity/scale correct (80 units, smaller)
- [ ] Burrow identity correct (round blue entrance, warm cozy glow, 3 stones)
- [ ] Cozy soft hello reads to viewer
- [ ] No on-screen text; no music
- [ ] Calm but alive; warm, safe mood (not dark)
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
Mimi = 80 units (smallest of the child characters). Child-proportioned burrow (`00-CORE/VARIABLES.md`).

## Scale Lock Summary
Character scale must follow the approved Pompom Hills scale system.

- Kiko = 100 units
- Mimi = 80 units
- Noah = 100 units
- Arda = 85 units
- Luca = 100 units
- Opa = 120 units, low-staged so he does not dominate the frame

Only Mimi appears in this shot.

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
