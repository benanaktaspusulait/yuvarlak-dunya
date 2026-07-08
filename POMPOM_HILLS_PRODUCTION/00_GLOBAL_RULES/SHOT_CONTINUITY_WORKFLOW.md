# Shot Continuity Workflow

> This is a global production standard. It captures the working pipeline validated on
> S01E07 — The Round Stone (Stone Hill) and makes it the default workflow for every future
> episode, in every world. It does not redesign any character or world, and it does not
> replace the underlying continuity rules in `00-CORE/CONTINUITY_RULES.md` — it packages
> those rules into one practical per-episode checklist so the same problems (colour drift,
> camera jumps, object drift between shots) are not re-solved from scratch every episode.

---

## 1. Why This Exists

S01E07 initially had good colour continuity but small visual jumps between 1-2
transitions (camera reset feel, slight object drift, character position mismatch at shot
boundaries). The fix was not a one-off patch — it was a repeatable pattern:

```
opening final frame → Shot 01
Shot 01 final frame → Shot 02 @image1
Shot 02 final frame → Shot 03 @image1
... and so on
```

Once every shot after Shot 01 used the previous shot's approved final frame as a strict
`@image1` reference (not just "the previous shot exists", but the literal exported final
frame), colour stayed locked, the world stayed consistent, and the character chain held
together. This document makes that the standard starting point for every episode instead
of something rediscovered per world.

---

## 2. The Standard Workflow

For every episode:

- World opening is optional pre-roll, not a story shot.
- Shot 01 uses the approved opening final frame as `@image1` environment reference.
- Shot 01's approved still becomes the Episode Colour Master.
- Every next shot uses the previous shot's final frame as `@image1`.
- The first 1 second of each shot must stay very close to `@image1` before the action
  continues.
- Export the first frame and final frame for every shot.
- Create or update the per-episode Object Continuity Map before generating shot video.
- Check every first-frame still / cheap take against the Object Continuity Map before
  spending video credits.
- Watch the full video for intra-shot character continuity, not only first/final frames.
- Watch the full video again for hard background/object stability.
- Apply the Global OpenArt Continuity Locks from
  `00-CORE/17_VIDEO_GENERATION_STANDARD.md` to every generated shot.

This is deliberately short. It is the checklist version of §3-§5 below and of the fuller
rules already defined in `00-CORE/CONTINUITY_RULES.md` §9 (Reference Frame Workflow),
§9.1 (First Frame Master Lock) and §13 (Video Continuation Rules) — this document does not
override those, it is the per-episode application of them plus the world-opening step
that `00-CORE/CONTINUITY_RULES.md` does not cover.

---

## 3. World Opening → Shot 01

If the episode uses a world micro-opening (see
`POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/MICRO_OPENING_AND_CLOSING_STANDARD.md` §2B), treat
its approved final frame as the environment continuity reference for Shot 01 — not as the
Episode Colour Master. Shot 01 itself defines the Episode Colour Master once its own still
is approved.

### Character Introduction After Empty Opening
When the opening has no characters, Shot 01 must introduce the first character naturally using one of the approved methods from `00-CORE/17_VIDEO_GENERATION_STANDARD.md` § Character Introduction After Empty Opening Rule:
- Camera Reveal (Method A)
- Visible Character Entrance (Method B)
- First Frame Character Already Partially Visible (Method C)

Do not allow character pop-in or sudden appearance. The character must not suddenly spawn into the middle of the frame after an empty opening. See the global QA test in `11-DOCS/16_VIDEO_QA_SPEC.md` for rejection criteria.

The micro-opening is not part of the story duration and is not renumbered as `shot-00`
inside the episode's shot list (see `MICRO_OPENING_AND_CLOSING_STANDARD.md` §2B and the
S01E07 example at
`POMPOM_HILLS_PRODUCTION/02_WORLDS/STONE_HILL/03_OPENINGS/STONE_HILL_ADVENTURES_MICRO_OPENING/s01e07-preroll-reference.md`).

If the episode does not use a micro-opening, Shot 01 has no previous-shot reference at
all — it is a fresh take shot per `00-CORE/CONTINUITY_RULES.md` §9.

---

## 4. Shot N → Shot N+1 (the core rule)

For every shot after Shot 01, `@image1` must be the approved final continuity frame of
the previous shot.

The first frame of the new shot should match `@image1` as closely as possible in:

- camera angle
- camera height
- lens feel
- framing
- character positions
- character scale
- background object positions
- world-specific locked landmark positions (e.g. pebble path / stone clusters for Stone
  Hill; whatever the equivalent locked elements are for the world in use)
- lighting
- colour grading
- exposure
- contrast

The new shot may continue the action naturally, but it must not begin with a noticeable
camera reset, jump cut, environment shift, character scale change, or background layout
change.

Practical rule of thumb: the first 1 second of a shot should visually hold close to
`@image1` before the shot's own action becomes noticeable. See
`POMPOM_HILLS_PRODUCTION/02_WORLDS/STONE_HILL/04_EPISODE_PACKAGES/S01E07_THE_ROUND_STONE/01_SHOTS/`
for five worked examples of this per-shot wording (Shot 02 through Shot 06).

The first second hold is also an intra-shot safety gate: no character may teleport,
switch sides, pop in, disappear, or change scale during that first second, and no visible
background object may move, disappear, duplicate, or change identity.

### Colour / Contrast Drift Control Rule

When a shot continues from a previous shot final frame using `@image1`, the visual style
must not become progressively more contrasty, saturated, sharp, glossy, HDR-looking, or
harsh.

OpenArt sometimes increases:
- contrast
- saturation
- sharpness
- glossy plastic highlights
- HDR-like lighting
- harsh shadows
- blown highlights
- deeper dark areas
- over-polished CGI look

This must be prevented globally.

For every frame-to-video continuity prompt, include a Colour / Contrast Stability section:

```
Colour / Contrast Stability:
Match @image1 for continuity, but do not intensify it.
Preserve the soft pastel preschool look.
Preserve medium-low contrast.
Preserve warm morning dappled sunlight.
Preserve gentle golden warmth.
Preserve soft shadows.
Preserve matte handcrafted toy-set materials.
Do not increase contrast.
Do not increase saturation.
Do not add HDR effect.
Do not add extra sharpening.
Do not add glossy plastic highlights.
Do not create harsher shadows.
Do not brighten highlights into a blown-out look.
Do not make dark areas deeper or more cave-like.
Do not make the scene look more intense than @image1.
If any adjustment happens, it should be slightly softer and calmer, never stronger,
sharper, glossier, darker, or more contrasty.
```

Add these terms to the global negative prompt for all OpenArt video prompts:

```
high contrast, contrast increase, overly saturated, saturation increase, HDR, HDR look,
glossy plastic, glossy CGI, harsh highlights, harsh shadows, blown highlights,
oversharpened, extra sharp, over-polished CGI, colour drift, exposure drift, saturation
drift, contrast drift, dark areas growing darker, highlights growing brighter, lighting
becoming harsher
```

Add this checklist item to every frame-to-video approval checklist:

```
- [ ] No contrast / saturation / HDR / glossy / oversharpened drift from @image1
```

### Character Voice Lock Rule

Every character must use the same locked voice across all shots in an episode and across
the entire series. Voice changes between shots break immersion and confuse young viewers.

OpenArt and post-production voice assignment must follow these rules:

1. **One voice per character.** Each character has one locked Voice ID / voice reference
   that never changes.

2. **Voice IDs must be registered** in `08-PRODUCTION/VOICE_TRACKER.md` before production
   begins. No shot may be generated without a confirmed Voice ID for every speaking
   character.

3. **Every shot prompt must specify** the locked Voice ID for each speaking character.
   Never let OpenArt or any TTS system "choose" a voice.

4. **Voice identity includes:**
   - Same pitch
   - Same timbre
   - Same age impression
   - Same speaking speed
   - Same warmth
   - Same preschool energy
   - Same speaking rhythm
   - Same pronunciation
   - Same accent
   - Same recording quality

5. **Reference-based voice lock:** If the system supports voice reference, use the
   approved Shot 01 voice sample as the reference for every subsequent shot. Never
   generate a new voice mid-episode.

6. **Forbidden:**
   - Different narrator voice for the same character
   - Alternate voice or voice variant
   - Older/younger sounding replacement
   - Different performer feel
   - AI-generated voice that drifts from the registered voice
   - Any voice not registered in VOICE_TRACKER.md

Add this to every OpenArt shot prompt that has dialogue:

```
Voice Lock:
Each character must use their registered locked voice from VOICE_TRACKER.md.
Do not let OpenArt choose or generate voices.
Do not change voice between shots.
Same pitch, same timbre, same age, same speed, same warmth.
```

Add this checklist item to every approval checklist:

```
- [ ] Character voices match registered Voice IDs — no drift
```

### Object Continuity Map Gate

Every episode that depends on persistent objects must maintain an Object Continuity Map
before video credits are spent.

The map lists, shot by shot:

- required objects from `@image1`
- optional objects to preserve if visible
- current action object
- usability checks
- forbidden object changes
- final-frame requirements for the next shot

A shot is not approved only because an object is mentioned in the prompt. A shot is
approved only if the required object is visible in `@image1` and usable for the planned
action at its existing size, shape, position, and distance.

Visible is not enough.

If the object is too small, too far away, too crowded, partly cropped, or not shaped for
the planned action, simplify the character action instead of changing the object.

Characters adapt to the environment.
The environment does not adapt to the characters.

Do not enlarge, move, multiply, reshape, replace, relocate, or spawn objects to satisfy
an action.

All environment objects visible in `@image1` are locked in place. Trees, flowers, grass
patches, hills, stones, doorways, props, sky elements, furniture, anchors, and landmarks
must not move, grow, shrink, slide, drift, pop in, enter frame, leave frame, or
reposition.

Only characters may move unless the shot explicitly allows a planned location
transition, such as an entrance crossing. The camera must not move to make an object
more usable.

Before generation, label the shot:

- **SAFE:** all required objects are visible and usable; generate.
- **RISKY:** usable but with quality risk; simplify action or add stricter locks before
  generating.
- **NOT READY:** required object is missing or unusable; do not spend video credits.
- **SALVAGE:** use only if continuing from an already damaged frame; freeze the actual
  layout and reduce action to small character gestures.

Before generating any shot, answer:

1. Which object does this shot interact with?
2. Is the object visible in `@image1`?
3. Is the object usable for the action at its current size, position, shape, and
   distance?
4. Would the character need camera movement to reach or use it?
5. Would the model need to enlarge, move, multiply, reshape, or spawn the object?
6. Does the final frame support the next shot?

If any answer fails, do not generate video. Simplify the action, regenerate the
prerequisite still, or mark the shot as salvage with frozen-layout rules.

---

## 5. Export and QA

After each shot is generated, export:

- first frame
- final frame
- final video

Before approving the next shot, compare:

- previous shot final frame
- next shot first frame

Then watch the full video twice:

1. Once only for character continuity inside the shot.
2. Once only for hard background/object stability.

Approve the transition only if:

- colour does not fade or shift
- camera does not visibly reset
- character scale stays consistent
- background/world-locked elements stay in the same layout
- persistent props (e.g. a discovered object being carried between shots) stay consistent
- the new shot feels like a continuation, not a new setup
- no character disappears, reappears, teleports, regenerates after occlusion, switches
  sides without visible motion, or has an unreadable path inside the shot
- no foreground object fully hides a character
- no background object moves, morphs, duplicates, disappears, changes identity or changes
  side of the frame

**If a transition has a small jump:**

1. Keep the previous shot. Do not regenerate it.
2. Regenerate only the next shot.
3. Use the previous shot's final frame as `@image1`.
4. Add the Transition Repair Prompt (§6) to the regeneration.

This export-and-compare step, plus the repair procedure, is what turns "hope the model
gets it right" into a repeatable QA gate. See
`POMPOM_HILLS_PRODUCTION/02_WORLDS/STONE_HILL/04_EPISODE_PACKAGES/S01E07_THE_ROUND_STONE/00_EPISODE_OVERVIEW/01-overview.md`
§ Transition QA for the worked version of this section.

For same-shot character continuity, QA must not rely only on the first and final frames.
The full video must be watched because disappearance, occlusion transition, teleporting
and character regeneration can happen inside the shot.

---

## 6. Transition Repair Prompt (reusable add-on)

Use this add-on whenever a regenerated shot needs a stricter first-frame match to fix a
visible jump:

```text
TRANSITION REPAIR PROMPT ADD-ON:

Use @image1 as the exact first-frame continuity reference.

The first second must match @image1 very closely: same camera angle, same lens feel,
same character scale, same character positions, same locked background/world layout,
same lighting and same colour grading.

After the first second, continue the planned action slowly and naturally.

Do not reset the camera. Do not recompose the shot. Do not move the characters to a new
location. Do not redesign the world. Do not change the background layout. Do not change
exposure, saturation, contrast or colour temperature.
```

Substitute the world's own locked elements where "same locked background/world layout"
appears (e.g. for Stone Hill: pebble path position, stone cluster positions; for Central
Square: Big Pompom Tree position and stepping-stone ring; etc. — see each world's own
canon bible §Visual Richness & World Charm / §World Identity Lock for its locked list).

---

## 7. Per-Episode Application

Every new episode's shot files and episode overview should apply this workflow the same
way S01E07 does:

- Each shot file (from Shot 02 onward) gets its own `## Transition Continuity Rule`
  section naming the specific previous shot as the `@image1` source, plus a one-line
  "first 1 second should preserve [previous shot]'s final composition/frame before
  [this shot's specific action] begins" note under Camera Direction.
- The episode overview gets one `## Transition QA` section (export rule, approval
  criteria, repair procedure) that every shot file's Transition Continuity Rule section
  points back to, instead of repeating the full repair prompt in every shot file.

This keeps the repair prompt and QA criteria in one place per episode, while keeping the
shot-specific hand-off instruction local to each shot file where it's actually used.

---

## 8. What This Does Not Change

- Character design, world design, dialogue, and story beats are untouched by this
  document — it only governs the technical hand-off between shots.
- This does not introduce a new closing-bumper requirement; normal episodes still close on
  their own final shot per `MICRO_OPENING_AND_CLOSING_STANDARD.md` §3.
- This does not replace `00-CORE/CONTINUITY_RULES.md` — it is the per-episode checklist
  built on top of it, specifically adding the world-opening → Shot 01 step and the
  standard Transition QA / repair procedure.
- This document governs the `@image1` continuity chain between shots inside the same
  world/episode. For multi-shot videos that are generated as separate standalone shots and
  combined later in editing (especially videos that move between different worlds), the
  standalone-shot generation rule and the in-file post-production transition note are defined
  in `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/STANDALONE_SHOT_AND_TRANSITION_STANDARD.md`.
  That standard complements this one: transitions between worlds are never generated in
  OpenArt, they are handled in editing using each shot's Post-Production Transition Note.

---

*This document is the single source of truth for the shot-to-shot continuity workflow
across episodes and worlds.*
*Validated on: S01E07 — The Round Stone (Stone Hill).*
*Version: 1.1 — 5 Temmuz 2026*
