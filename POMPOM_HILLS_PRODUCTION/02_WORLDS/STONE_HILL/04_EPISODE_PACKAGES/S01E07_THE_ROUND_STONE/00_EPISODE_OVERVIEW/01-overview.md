# S01E07 — The Round Stone

---

## Duration

Story: 1:30 (6 shots × 15 seconds) — this is the canonical episode length.

Total video: ~1:33-1:34 with the optional Stone Hill Adventures micro-opening as pre-roll
(see § Optional Pre-Roll below, ~3-4s). The pre-roll is NOT part of the 90-second story;
it is a calm lead-in that hands off into Shot 01. The story stays Shot 01-06 = 90 seconds
regardless of whether the pre-roll is used.

## Optional Pre-Roll: Stone Hill Adventures Micro-Opening

| Field | Value |
|---|---|
| Duration | 4 seconds |
| Source | `POMPOM_HILLS_PRODUCTION/02_WORLDS/STONE_HILL/03_OPENINGS/STONE_HILL_ADVENTURES_MICRO_OPENING/` |

The pre-roll is not part of the 90-second story. The story starts at Shot 01. Shot 01
remains the first story shot and Episode Colour Master. This is a reusable world asset,
not an episode-specific shot — see
`POMPOM_HILLS_PRODUCTION/02_WORLDS/STONE_HILL/03_OPENINGS/STONE_HILL_ADVENTURES_MICRO_OPENING/s01e07-preroll-reference.md`
for the S01E07-specific production reference (colour hand-off, sound, negative prompt).

---

## Theme

Curiosity, noticing shapes, sharing discovery, gentle friendship.

---

## Learning

Noticing shapes • Curiosity • Sharing discoveries • Gentle observation • Friendship

---

## Characters

| Character | Role |
|---|---|
| Luca | Discoverer |
| Kiko | Friend |

---

## World

Stone Hill — Rounded Stone Discovery Area

---

## Story Summary

Luca finds a smooth round stone on Stone Hill and shows it to Kiko. Together they notice
its shape, wonder what it looks like, and see that Stone Hill is full of round shapes.
Instead of keeping the stone only for themselves, they place it gently where everyone
can see it. They end with a warm, shared discovery.

## QA Status

| Shot | QA Score | Production Ready |
|------|:--------:|:----------------:|
| 01 | /10 | ⬜ |
| 02 | /10 | ⬜ |
| 03 | /10 | ⬜ |
| 04 | /10 | ⬜ |
| 05 | /10 | ⬜ |
| 06 | /10 | ⬜ |

---

## Transition QA

After each shot is generated, export:
- first frame
- final frame

Before approving the next shot, compare:
- previous shot final frame
- next shot first frame

Approve the transition only if:
- colour does not fade or shift
- camera does not visibly reset
- character scale stays consistent
- background stones and pebble path stay in the same layout
- the round stone prop stays consistent
- the new shot feels like a continuation, not a new setup

**If a transition has a small jump:**

1. Keep the previous shot. Do not regenerate it.
2. Regenerate only the next shot.
3. Use the previous shot's final frame as `@image1`.
4. Add this line to the OpenArt prompt: *"Match @image1 extremely closely for the first
   second before continuing the action. Do not reset the camera, do not change character
   scale, and do not shift the Stone Hill background layout."*

### Transition Repair Prompt (reusable add-on)

Use this add-on whenever a regenerated shot needs a stricter first-frame match to fix a
visible jump:

```text
TRANSITION REPAIR PROMPT ADD-ON:

Use @image1 as the exact first-frame continuity reference.

The first second must match @image1 very closely: same camera angle, same lens feel,
same character scale, same character positions, same pebble path position, same stone
cluster layout, same lighting and same colour grading.

After the first second, continue the planned action slowly and naturally.

Do not reset the camera. Do not recompose the shot. Do not move the characters to a new
location. Do not redesign Stone Hill. Do not change the background layout. Do not change
exposure, saturation, contrast or colour temperature.
```

Each shot file's own § Transition Continuity Rule points back here for the full repair
workflow.
