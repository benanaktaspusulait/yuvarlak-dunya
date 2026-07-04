# S01E05 — Colours Everywhere

---

## Duration

Story: 2:00 (8 shots x 15 seconds) — this is the canonical episode length.

Total video: about 2:04 with the optional Central Square Friends Micro-Opening as
pre-roll (see § Optional Pre-Roll below, 4 seconds). The pre-roll is NOT part of the
120-second story. The story stays Shot 01-08 = 120 seconds regardless of whether the
pre-roll is used.

## Optional Pre-Roll: Central Square Friends Micro-Opening

| Field | Value |
|---|---|
| Duration | 4 seconds |
| Source | `POMPOM_HILLS_PRODUCTION/02_WORLDS/CENTRAL_SQUARE/03_OPENINGS/CENTRAL_SQUARE_FRIENDS_MICRO_OPENING/` |
| Files | `central-square-micro-opening.md`, `central-square-openart-frame-to-video-prompt.md` |

The pre-roll is a reusable world asset, not an episode story shot. It plays before
Shot 01 and has no matching reusable closing. Normal Central Square episodes close with
their final story shot.

Shot 01 uses the approved Central Square Friends Micro-Opening final frame as `@image1`
environment continuity reference only. Shot 01's approved Kiko-visible still becomes
the Episode Colour Master.

---

## Theme

Colours are everywhere in one happy place.

---

## Learning

Observation • Colour names • Friendship • Noticing details in one familiar world

---

## Characters

| Character | Role |
|---|---|
| Kiko | Primary colour finder |
| Mimi | Friend who joins the discovery |

No other speaking characters.

---

## World

Central Square only.

The episode stays in one physical Central Square set. No world-to-world travel. No
Rosie's Garden. No Stone Hill. No Flower Hill. No new location.

---

## Story Summary

Kiko notices a red detail in Central Square. Mimi joins her from the same path, and
together they notice a blue bench, yellow flowers, green grass and purple flags already
inside the square. They remember the colours together and end by seeing the whole square
as one warm rainbow-like feeling made from existing objects.

---

## Shot Order

| Shot | File | Duration | Characters | Purpose |
|---:|---|---:|---|---|
| 01 | `shot-01-kiko-sees-red.md` | 15 sec | Kiko | Kiko notices red |
| 02 | `shot-02-mimi-joins.md` | 15 sec | Kiko, Mimi | Mimi joins naturally |
| 03 | `shot-03-blue-bench.md` | 15 sec | Kiko, Mimi | They notice blue |
| 04 | `shot-04-yellow-flowers.md` | 15 sec | Kiko, Mimi | They notice yellow |
| 05 | `shot-05-green-grass.md` | 15 sec | Kiko, Mimi | They notice green |
| 06 | `shot-06-purple-flags.md` | 15 sec | Kiko, Mimi | They notice purple |
| 07 | `shot-07-colours-together.md` | 15 sec | Kiko, Mimi | They remember the colours |
| 08 | `shot-08-rainbow-moment.md` | 15 sec | Kiko, Mimi | Warm final colour moment |

---

## OpenArt Reference Workflow

- Shot 01: `@image1` = approved Central Square Friends Micro-Opening final frame.
- Shot 01 uses `@image1` as environment continuity reference only.
- Shot 01 must generate a new story first frame with Kiko already visible in Central Square.
- Shot 01 still becomes the Episode Colour Master.
- Shot 02: `@image1` = approved Shot 01 final continuity frame.
- Shot 03: `@image1` = approved Shot 02 final continuity frame.
- Shot 04: `@image1` = approved Shot 03 final continuity frame.
- Shot 05: `@image1` = approved Shot 04 final continuity frame.
- Shot 06: `@image1` = approved Shot 05 final continuity frame.
- Shot 07: `@image1` = approved Shot 06 final continuity frame.
- Shot 08: `@image1` = approved Shot 07 final continuity frame.

The first 1 second should visually hold close to @image1 before new action begins.
For Shot 01, this applies to the Central Square environment only; Kiko must already be
visible and `@image1` must not be copied as an empty frame.

---

## Transition QA

After each shot is generated, export:

- first frame
- final frame
- final video

Before approving the next shot, compare:

- previous shot final frame
- next shot first frame

Use original downloaded/exported production media only. Never use screenshots for
continuity comparisons or colour approval.

Approve the transition only if:

- colour does not fade or shift
- no desaturation, exposure, contrast, colour temperature or brightness drift appears
- camera does not visibly reset
- character scale stays consistent
- Big Pompom Tree stays in the same relative position when visible
- rounded paths and coloured stepping-stone ring stay in the same layout
- visible benches, planters, grass and bunting remain stable
- the new shot feels like a continuation, not a new setup

If a transition has a small jump:

1. Keep the previous shot. Do not regenerate it.
2. Regenerate only the next shot.
3. Use the previous shot's final frame as `@image1`.
4. Add: "Match `@image1` extremely closely for the first second before continuing the action. Do not reset the camera, do not change character scale, and do not shift the Central Square background layout."

---

## Ending

No reusable closing bumper. Shot 08 ends with a quiet 2-second warm hold and clean
end-screen-friendly frame if natural space is available.

---

## QA Status

| Shot | QA Score | Production Ready |
|------|:--------:|:----------------:|
| 01 | /10 | ⬜ |
| 02 | /10 | ⬜ |
| 03 | /10 | ⬜ |
| 04 | /10 | ⬜ |
| 05 | /10 | ⬜ |
| 06 | /10 | ⬜ |
| 07 | /10 | ⬜ |
| 08 | /10 | ⬜ |
