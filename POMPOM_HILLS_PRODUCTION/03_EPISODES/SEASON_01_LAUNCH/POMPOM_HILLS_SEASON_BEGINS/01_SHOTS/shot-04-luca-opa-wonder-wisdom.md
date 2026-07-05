# Season Begins — Shot 04 — Luca & Opa: Wonder and Wisdom

## Scene Context
| Alan | Değer |
| --- | --- |
| Video | Pompom Hills — The Season Begins |
| Shot | 04 / 06 |
| Duration | 15 seconds |
| Location | Opa's Tree |
| Characters | **Luca + Opa** |
| Time of Day | Warm afternoon |

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
Location is Opa's Tree only.
Approved visible environment: Opa's Tree and existing tree/perch/branch setting.
No cutaway to Stone Hill, no new magical area, no library, no bedroom, no night sky, no star field.

## Duo Character Rule
This shot contains **two characters: Luca and Opa**. They appear together at Opa's Tree.
Independent generation (Opa's Tree ref + Luca ref + Opa ref). This pairing highlights the
"wonder + wisdom" dynamic: Luca's curiosity guided by Opa's warm presence.
Independent generation means this shot does not inherit characters, props, camera movement, or background objects from any previous shot. It must obey only this shot document and its assigned references.

## Background Object Lock
Opa's Tree locked: large warm tree, low story branch/perch, cozy setting stay stable. Opa
and Luca move. No other characters, no new objects.

## No Surprise Elements Rule

No surprise elements may appear at any point in this shot.

The character list is locked from the first frame. Only Luca and Opa may appear. No extra character, background character, crowd member, animal, toy creature, duplicate character, partial character, shadow character, silhouette character, reflection character, or off-screen entering character may appear.

The object list is locked from the first frame. Only the approved Opa's Tree environment already in the reference may appear. Do not introduce new props, new toys, new signs, new flowers, new furniture, new stones, new houses, new paths, new decorations, new lights, new clouds, new doors, new windows, or any new background detail during the shot.

If an object or character is not visible or clearly established in the first frame, it must not appear later.

The camera must not pan, zoom, pull back, tilt, orbit, or reframe in order to reveal new objects or characters. The shot must adapt to the first frame layout.

## Approved Characters and Props

### Approved characters
- Luca
- Opa

### Forbidden characters
- Kiko, Mimi, Noah, Arda
- any unnamed extra character
- any background crowd
- any duplicate version of Luca or Opa

### Approved props
- None beyond the Opa's Tree environment already in the world reference (tree, perch/branch elements)

### Forbidden props
- any new stone pile, book, lantern, or sign
- any glowing object, magical object, floating lights, or appearing stars
- any sign, written text, logo, caption, speech bubble, subtitle, or watermark
- any object that was not listed as approved for this shot

## Visual Prompt
```text
Use Opa's Tree (world reference) as the LOCKED environment. Insert Luca (character reference) and Opa (character reference) together. Medium shot, warm afternoon light, large warm tree behind. Opa sits or stands low-staged near the tree, Luca stands beside him looking up with bright wonder. Luca turns to the viewer with a curious smile, Opa gives a slow gentle nod and warm wise smile. Both characters present. Calm, cozy, safe. Handcrafted preschool toy-set look, {style} {camera} {lighting}

Only Luca and Opa are present. No book, lantern, magical object, glowing prop, extra animal, or background character appears. No new object appears to create wonder; the wonder comes only from Luca's expression, Opa's calm presence, and the existing tree environment.

Do not display dialogue as on-screen text. No speech bubbles. No captions. No subtitles. No text.
Opa's Tree background locked; keep the tree and setting stable.
```

## Camera Direction
Medium, eye-level, locked composition. No pan, no zoom, no pull-back, no push-in, no tilt, no orbit, no reframe, no camera reveal. Frame Luca and Opa comfortably from the first frame, with Opa slightly behind or beside Luca.

## Dialogue
```
Luca: There's so much to discover here!
Opa: And I'll be here to help you explore.
```

## Shot Breakdown
| Time | Action | Camera |
|---|---|---|
| 0-2 sn | Opa's Tree, Luca and Opa together, warm afternoon | Medium |
| 2-5 sn | Luca looks around with wonder, Opa watches kindly | Medium |
| 5-8 sn | Luca turns to viewer with curious smile, Opa slow nod | Medium |
| 8-12 sn | Luca: "There's so much to discover here!" / Opa: "And I'll be here to help you explore." | Medium |
| 12-15 sn | Luca bright smile, Opa warm wise smile, both blink. Final 0.5s: calm still hold. | Medium |

## Natural Character Motion Rule
Calm but alive: Luca looks around, gestures with open arms; Opa nods slowly, warm smile. Gentle and unhurried. No freeze that feels dead.

## Sound
- Soft warm outdoor ambience, gentle leaves, light birds
- Natural ambience only. No music. No background music.

## Lighting
Warm afternoon, soft ambient, cozy. Never dark or dramatic.

## Reference Usage
- World Reference: Opa's Tree (`POMPOM_HILLS_PRODUCTION/02_WORLDS/OPA_TREE/`)
- Character Reference: Luca sheet, Opa sheet.

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
multiple characters, three characters, group, crowd, Kiko, Mimi, Noah, Arda, book, lantern, glowing object, magic object, stars appearing, floating lights, animal, surprise character, extra character, background crowd, duplicate Luca, duplicate Opa, low quality, blurry, deformed, extra limbs, text, watermark, photorealistic, horror, scary, dark lighting, harsh shadows, sharp rocks, redesigned character, wrong scale, character drift, redesigned environment, cluttered background, background music, music, melody, song, soundtrack, musical bed, surprise object, surprise prop, character appearing later, character entering later, duplicate character, duplicate body, partial character, shadow character, reflection character, extra animal, toy creature, new object, new prop, object appearing later, object entering later, camera revealing new object, camera revealing new character
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

This shot ends at Opa's Tree and transitions back to Shot 05 in Central Square.

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
- gently crossfade Opa's Tree outdoor ambience into Central Square outdoor ambience
- no music
- no chime
- no whoosh
- no hard audio cut

Important:
This transition is done in editing only.
Do not ask OpenArt to generate the transition.
Do not include transition wording inside the OpenArt Visual Prompt.

## QA Checklist
- [ ] **Exactly TWO characters (Luca + Opa) in frame — no others**
- [ ] Luca identity/scale correct (100 units)
- [ ] Opa identity/scale correct (120 units, low-staged)
- [ ] "Wonder + wisdom" dynamic reads clearly
- [ ] Both characters properly positioned relative to each other
- [ ] Opa's Tree environment stable, warm afternoon light
- [ ] No on-screen text; no music
- [ ] Calm but alive; natural mentor-mentee feeling
- [ ] Approved character count is correct from the first frame
- [ ] No extra character appears at any time
- [ ] No duplicate character appears at any time
- [ ] No surprise prop/object appears at any time (no book/lantern/glowing object)
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
Luca = 100 units. Opa = 120 units, eye line 0.82–0.92m, low-staged (`00-CORE/VARIABLES.md`).

## Scale Lock Summary
Character scale must follow the approved Pompom Hills scale system.

- Kiko = 100 units
- Mimi = 80 units
- Noah = 100 units
- Arda = 85 units
- Luca = 100 units
- Opa = 120 units, low-staged so he does not dominate the frame

Only Luca and Opa appear in this shot.

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
