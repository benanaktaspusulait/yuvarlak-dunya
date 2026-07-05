# Season Begins — Edit Transition Plan

## Purpose

This document defines how separately generated OpenArt shots should be combined in editing.

The goal is to avoid abrupt world changes while keeping OpenArt generation safe.

All location/world transitions happen only in editing.

Do NOT generate transition scenes inside OpenArt.

---

## Shot Order

| Order | Shot | Location | Duration |
|---|---|---|---:|
| 1 | Shot 01 — Kiko Welcome | Central Square | 12s |
| 2 | Shot 02 — Mimi Cozy Hello | Mimi's Burrow | 12s |
| 3 | Shot 03 — Noah & Arda Follow the Little Sound | Central Square | 15s |
| 4 | Shot 04 — Luca & Opa Wonder and Wisdom | Opa's Tree | 15s |
| 5 | Shot 05 — Kiko, Noah & Arda Play Together | Central Square | 15s |
| 6 | Shot 06 — Full Cast Final Tableau | Central Square | 15s |

Raw duration: 84 seconds.

Estimated final runtime with overlapping transitions: approximately 81.5–82 seconds.

---

## Transition Ledger

| Transition | From | To | Type | Duration | Notes |
|---|---|---|---|---|---|
| T1 | Central Square | Mimi's Burrow | Warm cream dip | 0.5s | Biggest visual change; keep soft |
| T2 | Mimi's Burrow | Central Square | Warm cream dip | 0.5s | Cozy burrow back to open square |
| T3 | Central Square | Opa's Tree | Warm cream dip | 0.5s | Different world; avoid hard cut |
| T4 | Opa's Tree | Central Square | Warm cream dip | 0.5s | Return to main world |
| T5 | Central Square | Central Square | Soft crossfade | 0.3–0.5s | Same world, different group size |

---

## Recommended Visual Transition Style

Preferred:
- warm cream dip
- 0.4–0.6 seconds
- no text
- no logo
- no sparkle
- no star wipe
- no flash
- no zoom
- no portal
- no magical effect

For same-location transition:
- soft crossfade
- 0.3–0.5 seconds

Do not use:
- hard cuts between different worlds
- glitch transition
- fast wipe
- dramatic flash
- camera zoom transition
- split-screen
- transition cards with text

---

## Audio Transition Rules

- Natural ambience only.
- No music.
- No background music.
- No hard audio cuts.
- Crossfade ambience under every visual transition.
- Transition audio duration should match visual transition duration.
- Do not add magical chimes, whooshes, bells, sparkles, or musical stingers.
- If using warm cream dip, audio should remain soft and natural.

---

## Edit-Safe Frame Requirements

Every shot must provide:

### Opening frame
- correct location visible
- approved characters visible
- no camera movement
- no surprise object
- no sudden gesture
- no text

### Ending frame
- calm face / smile / blink hold
- no new gesture starts
- no character displacement
- no camera movement
- no new object
- no text

If a shot ends with motion blur, character displacement, extra object, sudden lighting change, or wrong character count, do not use that ending for transition.
Trim slightly earlier or regenerate.

---

## OpenArt Prompt Extraction Rule

Do NOT paste the full shot document into OpenArt.

For OpenArt generation, use only:

- Visual Prompt
- Camera Direction
- Dialogue
- Natural Character Motion Rule
- Lighting
- Negative Prompt

Do NOT paste these sections into OpenArt:

- Edit-Safe Opening and Ending Rule
- QA Checklist
- Final Internal Consistency QA
- First-Frame Generation Gate
- No Salvage Before Output Rule
- Fallback Plan
- Edit Transition Plan
- Any instruction mentioning crossfade, cream dip, transition, next shot, previous shot, montage, cut, dissolve, or moving between worlds

These are production/editing instructions only.

OpenArt should generate clean standalone shots only.

---

## Final Export Rule

The final video should feel like a gentle tour of Pompom Hills, not a rapid jump between unrelated worlds.

Target feeling:
Central Square welcomes us.
Mimi's Burrow feels cozy.
Central Square brings playful curiosity.
Opa's Tree brings wonder and wisdom.
Central Square gathers the friends.
Full cast welcomes the viewer.

Keep the edit soft, warm, slow, and preschool-safe.
