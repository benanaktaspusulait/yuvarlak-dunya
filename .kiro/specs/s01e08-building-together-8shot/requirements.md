# Requirements Document

## Introduction

This feature restructures the existing preschool animation episode **S01E08 — "Building Together"** (alternate/proposed title "We Build Together") from its current 4-shot × 15s = 60s form into a proper 8-shot × 15s = 120s (2 minute) episode.

The episode belongs to the Pompom Hills / Yuvarlak Dunya preschool video production repository. It is set in **Central Square** and features only two characters, **Noah** and **Arda**. The core message is: *"It's easier when we build together, and if it breaks we can try again."*

The expansion MUST NOT be achieved by stretching the existing 4 shots (which causes dead air, silent staring, and OpenArt visual drift). Instead, the episode is rebuilt on a new 8-beat structure, keeping the existing 4 shots as a backbone reference (not deleted outright) and mapping old shots to new shots.

This document defines the requirements for the restructured episode as a set of production artifacts: the episode package, eight shot documents, their OpenArt-facing prompts, and their QA acceptance criteria. All requirements inherit and MUST NOT contradict repository canon defined in `00-CORE/` (video generation, OpenArt continuity, preflight, negative prompts, child safety, continuity rules) and character/world canon (`01-CHARACTERS/`, Central Square world files), per the routing rules in `AGENTS.md`.

This is a documentation and production-planning deliverable. "SHALL" requirements describe what the restructured episode artifacts and their contents must satisfy, not runtime software behavior.

## Glossary

- **Episode_Package**: The full S01E08 production package located at `POMPOM_HILLS_PRODUCTION/02_WORLDS/CENTRAL_SQUARE/04_EPISODE_PACKAGES/S01E08_BUILDING_TOGETHER/`, including overview, shot documents, continuity frames, and metadata.
- **Shot_Document**: A single markdown production document describing one 15-second shot (its context, continuity, start frame, visual prompt, camera, dialogue, beat breakdown, sound, negative prompt, and QA checklist).
- **OpenArt_Prompt**: The OpenArt-facing production instruction contained in a Shot_Document, consisting of the Visual Prompt, Negative Prompt, sound instruction, duration, and reference setup, written per `00-CORE/17_VIDEO_GENERATION_STANDARD.md` and `00-CORE/18_OPENART_CONTINUITY_AND_MOTION_RULES.md`.
- **Continuity_Chain**: The `@image1`-based first-frame continuity mechanism where each continuation shot begins from the previous shot's exported final frame, per `00-CORE/18_OPENART_CONTINUITY_AND_MOTION_RULES.md` and `00-CORE/CONTINUITY_RULES.md`.
- **Blocks**: The set of colourful round/flat building blocks that are the single episode interaction prop.
- **Tower**: The stacked structure Noah and Arda build from the Blocks.
- **QA_Checklist**: The per-shot acceptance checklist embedded in each Shot_Document, referencing repository QA standards.
- **Backbone_Shots**: The four existing shot files (`shot-01-gather-blocks.md`, `shot-02-first-attempt.md`, `shot-03-try-again.md`, `shot-04-tower-stands.md`) retained as reference during restructuring.
- **Noah**: Human boy character, lineup scale 100 units, curly light brown hair, blue striped shirt, khaki shorts, per `01-CHARACTERS/05-noah.md`.
- **Arda**: Human boy character, lineup scale 85 units (younger and slightly smaller than Kiko/Noah), sky blue shirt, per `01-CHARACTERS/04-arda.md`.
- **Central_Square**: The fixed world location for this episode, a permanent visual set per `00-CORE/CONTINUITY_RULES.md` §11 World Identity Lock and Central Square world files.
- **Target_Audience**: Children aged 3–4 years.

## Requirements

### Requirement 1: Episode Structure and Timing

**User Story:** As the episode producer, I want the episode rebuilt as eight distinct 15-second shots totalling two minutes, so that the runtime is reached through genuine story beats instead of stretched footage.

#### Acceptance Criteria

1. THE Episode_Package SHALL define exactly eight Shot_Documents for S01E08.
2. THE Episode_Package SHALL assign each Shot_Document a duration of 15 seconds.
3. THE Episode_Package SHALL define a total episode runtime of 120 seconds.
4. THE Episode_Package SHALL order the eight Shot_Documents as: (1) Blocks Are Found, (2) Choosing Shapes, (3) First Tower Attempt, (4) Tower Falls, (5) Small Feeling Beat, (6) New Plan, (7) Careful Together Build, (8) Tower Stands.
5. WHERE the episode runtime is expanded beyond 60 seconds, THE Episode_Package SHALL achieve the additional runtime through new distinct story beats rather than lengthening existing shots.
6. THE Episode_Package SHALL retain the four Backbone_Shots as reference material rather than deleting them.
7. THE Episode_Package SHALL record the old-to-new shot mapping: old Shot 01 maps to new Shot 01; old Shot 02 splits into new Shots 03 and 04; old Shot 03 splits into new Shots 06 and 07; old Shot 04 maps to new Shot 08.
8. THE Episode_Package SHALL record the episode title as "Building Together" and the alternate title as "We Build Together".

### Requirement 2: Per-Beat Narrative and Emotional Goals

**User Story:** As the episode writer, I want each of the eight shots to carry a defined narrative and emotional purpose, so that the episode communicates the "build together, try again" message clearly to preschoolers.

#### Acceptance Criteria

1. THE Shot_Document for Shot 01 (Blocks Are Found) SHALL establish the Blocks as the episode object, show Noah finding and arranging the Blocks, and introduce Arda arriving, using dialogue equivalent to "Look at these blocks." and "Can we build?".
2. THE Shot_Document for Shot 02 (Choosing Shapes) SHALL depict Noah and Arda choosing shapes and planning with simple shape logic contrasting a round block and a flat block, using dialogue equivalent to "This one?" and "The flat one first.".
3. THE Shot_Document for Shot 03 (First Tower Attempt) SHALL depict the Tower rising while wobbling to build gentle tension, using dialogue equivalent to "Careful..." and "I am careful!".
4. THE Shot_Document for Shot 04 (Tower Falls) SHALL depict the Tower falling softly with the Blocks scattering gently, using dialogue equivalent to "Oh no!" and "It fell.".
5. THE Shot_Document for Shot 05 (Small Feeling Beat) SHALL depict Arda feeling briefly discouraged with a small shoulder drop while Noah gives calm support, serving as the emotional centre, using dialogue equivalent to "I can't do it." and "We can try together.".
6. THE Shot_Document for Shot 06 (New Plan) SHALL depict Noah showing a big block for the bottom and a small block for the top, using dialogue equivalent to "Big block first.", "Small block on top?", and "Yes.".
7. THE Shot_Document for Shot 07 (Careful Together Build) SHALL depict both characters rebuilding slowly with one holding and one placing to show teamwork physically, using dialogue equivalent to "You hold it." and "I've got it.".
8. THE Shot_Document for Shot 08 (Tower Stands) SHALL depict the finished Tower standing with both characters happy, using dialogue equivalent to "We did it!" and "Together!".
9. THE Episode_Package SHALL state the episode message as "It's easier when we build together, and if it breaks we can try again.".

### Requirement 3: Character and World Canon Preservation

**User Story:** As the continuity owner, I want the restructured episode to preserve established character and world canon, so that S01E08 stays consistent with the rest of the series.

#### Acceptance Criteria

1. THE Episode_Package SHALL include only Noah and Arda as characters in every Shot_Document.
2. IF any character other than Noah or Arda would appear in a shot, THEN THE Shot_Document SHALL exclude that character and its OpenArt_Prompt Negative Prompt SHALL list "extra characters".
3. THE Shot_Documents SHALL preserve Noah's canonical appearance from `01-CHARACTERS/05-noah.md`, including curly light brown hair, blue striped shirt with denim pocket, khaki shorts, and blue sneakers.
4. THE Shot_Documents SHALL preserve Arda's canonical appearance from `01-CHARACTERS/04-arda.md`, including fluffy dark brown hair, sky blue shirt, light blue pants, and tan shoes.
5. THE Shot_Documents SHALL keep Arda younger and slightly smaller than Noah in scale, consistent with the lineup scales of 85 units for Arda and 100 units for Noah.
6. THE Shot_Documents SHALL keep character hair, eyes, face, body, outfit, colours, and scale unchanged across all eight shots, per `00-CORE/CONTINUITY_RULES.md` §1.
7. THE Shot_Documents SHALL set the location to Central_Square in every shot and preserve its established identity per `00-CORE/CONTINUITY_RULES.md` §11, including the Big Pompom Tree, rounded paths, and warm morning daylight.
8. THE Shot_Documents SHALL reference the established location by name and SHALL NOT describe Central_Square using generic terms such as "a village" or "a big tree", per `00-CORE/CONTINUITY_RULES.md` §11.1.

### Requirement 4: Global Block Object Rule

**User Story:** As the continuity owner, I want the building blocks locked as the only movable prop with strict identity rules, so that OpenArt does not invent, remove, or transform props across the episode.

#### Acceptance Criteria

1. THE Episode_Package SHALL define the Blocks as the only movable interaction prop across all eight shots.
2. THE Shot_Documents SHALL NOT add Blocks beyond the established set and SHALL NOT remove Blocks from the established set.
3. THE Shot_Documents SHALL keep Block colours stable across all shots and SHALL NOT change Block colours dramatically between shots.
4. THE OpenArt_Prompt Negative Prompt in each Shot_Document SHALL forbid transforming the Blocks into other objects, including toys, furniture, stones, food, boxes, tools, letters, and signs.
5. THE Shot_Documents SHALL keep the Tower height at or below the characters' chest-to-head level.
6. IF a Tower taller than the characters' head level is proposed, THEN THE Shot_Document SHALL require explicit prior approval before that height is used.
7. THE Shot_Documents SHALL seed the Blocks as visible in Shot 01 before they are named, pointed at, or interacted with in later shots, per `00-CORE/18_OPENART_CONTINUITY_AND_MOTION_RULES.md` §11 and §14.
8. THE Shot_Documents SHALL keep the Blocks' identity, general position pattern, and scale consistent once seeded, allowing only character-driven movement of individual Blocks during building actions.

### Requirement 5: OpenArt Continuity and Production Safety

**User Story:** As the video generation lead, I want every shot to follow the OpenArt continuity chain and production-safety rules, so that generated video stays stable and free of drift.

#### Acceptance Criteria

1. THE OpenArt_Prompt for Shot 01 SHALL introduce Noah and Arda using an approved introduction method (camera reveal, visible entrance, or partial edge visibility) rather than a centered pop-in, per `00-CORE/17_VIDEO_GENERATION_STANDARD.md` Character Introduction After Empty Opening Rule.
2. THE OpenArt_Prompt for each continuation shot (Shots 02 through 08) SHALL use the previous shot's exported final frame as `@image1` and as the only visual continuity source.
3. THE OpenArt_Prompt for each continuation shot SHALL hold close to `@image1` for the first 1 second before new action begins.
4. THE OpenArt_Prompt for each continuation shot SHALL forbid camera pull-back, widening, reset, pan, tilt, zoom, tracking, and reframing except the small settle movements permitted by `00-CORE/17_VIDEO_GENERATION_STANDARD.md`.
5. THE OpenArt_Prompt for each shot SHALL inherit sky, lighting, colour grading, exposure, and contrast from `@image1` and SHALL forbid lighting drift to sunset, orange, golden, grey, or dramatic skies, per `00-CORE/18_OPENART_CONTINUITY_AND_MOTION_RULES.md` §7.
6. THE OpenArt_Prompt for each shot SHALL require every character to remain a single solid form and SHALL forbid ghosting, duplicate characters, transparent copies, double exposure, and motion smear.
7. THE Shot_Documents SHALL include a Background Object Lock section keeping all first-frame background objects stable in identity, position, and scale throughout the shot.
8. WHERE a shot uses more than one reference image, THE OpenArt_Prompt SHALL assign each reference image an explicit role and SHALL state that `@image1` has priority for camera, lighting, composition, scale, and environment, per `00-CORE/18_OPENART_CONTINUITY_AND_MOTION_RULES.md` §15.
9. THE Shot_Documents SHALL include a Shot Contract and pass the Preflight Checklist from `00-CORE/19_VIDEO_PRODUCTION_PREFLIGHT_SYSTEM.md` before video generation, and each Shot_Document SHALL carry a status of SAFE, RISKY, or NOT READY.
10. IF any interaction object required by a shot is not visible in `@image1` and was not seeded earlier, THEN THE Shot_Document SHALL be marked NOT READY and SHALL be revised before generation.

### Requirement 6: High-Risk Beat Continuity and QA

**User Story:** As the QA reviewer, I want explicit continuity requirements for the highest-risk beats, so that the tower fall, block scatter, and tower height/count stay controlled and consistent.

#### Acceptance Criteria

1. THE Shot_Document for Shot 04 (Tower Falls) SHALL specify that the Tower falls softly and that the Blocks scatter gently within the locked composition without any Block leaving or entering the established set.
2. THE Shot_Document for Shot 04 SHALL specify that the same Blocks present before the fall remain present after the fall, preserving Block count and identity.
3. THE Shot_Documents for Shots 03 through 08 SHALL record the intended Tower Block count and height at the start and end of each shot so that height and count continuity is verifiable across the Continuity_Chain.
4. THE QA_Checklist for Shots 04 and 05 SHALL include a check that the transition from Tower Falls to the Small Feeling Beat preserves Block positions from the previous shot's final frame.
5. THE QA_Checklist for each Shot_Document SHALL include checks that no Block spawns, disappears, morphs, duplicates, or changes identity during the shot.
6. THE QA_Checklist for each Shot_Document SHALL include a check that the Tower height stays at or below head level.
7. IF a generated shot shows the Tower or Blocks violating count, height, or identity continuity, THEN THE QA_Checklist SHALL mark the shot as rejected.

### Requirement 7: Pointing, Gaze, and Orientation Lock for Shot 06

**User Story:** As the shot director, I want Shot 06 to lock pointing, gaze, and body orientation to the target block, so that the "big block first, small block on top" instruction reads clearly to preschoolers.

#### Acceptance Criteria

1. THE Shot_Document for Shot 06 (New Plan) SHALL name the target Block for each pointing or showing beat.
2. THE Shot_Document for Shot 06 SHALL require the target Block to be visible in frame during each pointing beat.
3. WHEN Noah points at a target Block in Shot 06, THE Shot_Document SHALL require Noah's pointing hand, eyes, head, shoulders, and upper body to all align toward that target Block, per `00-CORE/18_OPENART_CONTINUITY_AND_MOTION_RULES.md` §17.
4. WHEN Noah indicates a target Block in Shot 06, THE Shot_Document SHALL require Arda to turn toward the same target Block.
5. THE Shot_Document for Shot 06 SHALL forbid ambiguous pointing where a character points toward empty space or looks in a different direction than the point.

### Requirement 8: Preschool Safety

**User Story:** As the child-safety owner, I want every shot to be safe for 3–4 year olds, so that the episode contains no fear, shame, loud, or fast content.

#### Acceptance Criteria

1. THE Shot_Documents SHALL keep all content appropriate for the Target_Audience of 3–4 years, per `00-CORE/CHILD_SAFETY_RULES.md`.
2. THE Shot_Documents SHALL depict the Tower fall in Shot 04 as soft and gentle, and SHALL NOT depict it as loud, fast, frightening, or crashing.
3. THE Shot_Document for Shot 05 SHALL depict Arda's discouragement as a small, brief feeling beat resolved by calm support, and SHALL NOT depict shame, scolding, crying meltdown, or exclusion.
4. THE Shot_Documents SHALL depict only slow, calm, gentle character motion and SHALL NOT depict running, sudden gestures, or fast movement.
5. THE Shot_Documents SHALL depict only positive or gently curious emotions and SHALL NOT depict conflict, teasing, or competition between Noah and Arda.
6. THE Shot_Documents SHALL keep all shapes rounded and soft, and their OpenArt_Prompt Negative Prompts SHALL forbid sharp edges, dark shadows, scary imagery, violence, and weapons, per `00-CORE/NEGATIVE_PROMPTS.md`.
7. THE Shot_Documents SHALL keep sound within the child-safety limits of `00-CORE/CHILD_SAFETY_RULES.md` and SHALL forbid shouting, screaming, harsh noise, and sudden loud sound changes.

### Requirement 9: Dialogue and Audio Rules

**User Story:** As the audio lead, I want dialogue and audio handled per repository standards, so that speech stays natural and never appears as on-screen text.

#### Acceptance Criteria

1. THE OpenArt_Prompt for each Shot_Document SHALL state that dialogue is not displayed as on-screen text, and SHALL forbid captions, subtitles, speech bubbles, and text.
2. THE Shot_Documents SHALL keep Noah's and Arda's voice identity, pitch, timbre, speaking speed, and warmth consistent across all eight shots, per `00-CORE/CONTINUITY_RULES.md` §5.
3. THE Shot_Documents SHALL specify natural ambience only, and their OpenArt_Prompt Negative Prompts SHALL forbid music, background music, melody, song, soundtrack, and musical bed, per `00-CORE/18_OPENART_CONTINUITY_AND_MOTION_RULES.md` §9.
4. THE Shot_Documents SHALL NOT repeat a dialogue line already spoken in an earlier shot when continuing from a previous shot, per `00-CORE/CONTINUITY_RULES.md` §13.
5. WHEN a character speaks in a shot, THE Shot_Document SHALL support the dialogue with a physical action rather than a static talking pose, per `00-CORE/18_OPENART_CONTINUITY_AND_MOTION_RULES.md` §10.

### Requirement 10: Per-Shot QA Acceptance Criteria

**User Story:** As the QA reviewer, I want each shot to carry a complete acceptance checklist, so that every shot can be verified against continuity, safety, and liveliness standards before approval.

#### Acceptance Criteria

1. THE QA_Checklist for each Shot_Document SHALL include checks for character integrity, character consistency, object persistence, camera consistency, lighting consistency, and canonical-rule compliance.
2. THE QA_Checklist for each Shot_Document SHALL include the Global OpenArt Continuity Lock checks required by `00-CORE/17_VIDEO_GENERATION_STANDARD.md`, covering Hard Background Lock, Intra-Shot Character Continuity Lock, Single Visible Path Rule, Occlusion Is Not A Transition, Camera continuity, First Second Continuity Hold, and Object Identity Lock.
3. THE QA_Checklist for each Shot_Document SHALL include a check that the shot feels calm but alive with a clear action, reaction, or dialogue beat every 2–3 seconds and no dead air or silent staring.
4. THE QA_Checklist for each Shot_Document SHALL include a check that the shot's final frame is usable as `@image1` for the next shot without unwanted crop, close-up, lighting change, scale change, or new object.
5. THE QA_Checklist for the Small Feeling Beat (Shot 05) SHALL include a check that the emotional beat reads as brief and supportive rather than distressing.
6. THE QA_Checklist for Shot 06 SHALL include a check that pointing, gaze, and body orientation are all aligned to a visible target Block.
