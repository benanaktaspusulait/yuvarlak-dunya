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

---

*This document is the single source of truth for the shot-to-shot continuity workflow
across episodes and worlds.*
*Validated on: S01E07 — The Round Stone (Stone Hill).*
*Version: 1.0 — 4 Temmuz 2026*
