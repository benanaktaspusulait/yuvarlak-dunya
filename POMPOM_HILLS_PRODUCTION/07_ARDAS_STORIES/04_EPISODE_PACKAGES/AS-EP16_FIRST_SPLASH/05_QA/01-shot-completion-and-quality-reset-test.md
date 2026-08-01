# AS-EP16 — Shot Completion and Quality-Reset QA Test

## Purpose

Run this test after the eight 15-second shot exports exist and before episode assembly. Every
mandatory test must pass. Record the tested filename, take/version, timecode, screenshot or frame
evidence, result, and reviewer initials. A blank result is not an approval.

## Result Codes

| Code | Meaning |
|---|---|
| PASS | Requirement is visibly and audibly satisfied |
| FAIL | Requirement is violated; reject and regenerate or repair the shot |
| BLOCKED | Required export, source record, or evidence is missing |
| N/A | Allowed only where the test explicitly permits it |

## Required Evidence

- Original 15-second export for each shot, before upscale or colour correction.
- Start frame, frame at 13.0 seconds, and final frame for each shot.
- Full-resolution Episode Colour Master.
- OpenArt input/source record proving the start image used for each shot.
- Full 120-second assembly for the final edit test.
- Headphones and a waveform/timeline view for dialogue and sound checks.

## Gate A — Package and Source Compliance

| Test ID | Test | Pass criterion | Result | Evidence / notes |
|---|---|---|---|---|
| A-01 | Export count | Exactly 8 numbered shot exports exist |  |  |
| A-02 | Shot duration | Every export is exactly 15 seconds within the production tool's frame tolerance |  |  |
| A-03 | Production Mode | All 8 records say `FRESH QUALITY-RESET SHOT` |  |  |
| A-04 | Fresh source audit | Each input is a clean shot-specific canonical composition; no previous generated final frame is used |  |  |
| A-05 | Required contracts | Each shot file and prompt contains all six required completion/dependency fields |  |  |
| A-06 | Chain audit | Exact generated-frame chain count is 0 for this episode |  |  |

Any failure in Gate A blocks all eight shots until the source record and affected generation are
corrected.

## Gate B — Per-Shot Action-Completion Tests

Watch each complete export at normal speed, then inspect the final two seconds frame by frame.

| Test ID | Shot | Complete Main Action that must be visible | Required Completed End State at or before 13.0s | Required Stable Final Anchor from 13.0–15.0s | Result | Evidence / notes |
|---|---:|---|---|---|---|---|
| B-01 | 01 | Arda stands at garden door, looks out at wet garden | Arda balanced at door frame | Arda smiles; stable post-rain atmosphere |  |  |
| B-02 | 02 | Arda walks through garden, hops between small puddles | Arda stops near a small puddle | Arda stands balanced; no new hop begins |  |  |
| B-03 | 03 | Arda spots large puddle, walks to edge, looks down | Arda stationary at puddle edge | Reflection stable; Arda mesmesrised |  |  |
| B-04 | 04 | Arda jumps twice into puddle; two clear splash bursts | Arda balanced in puddle; water calming | Calm ripples; Arda wobbles joyfully |  |  |
| B-05 | 05 | Arda stops, looks down, reflection becomes clear | Arda looking down intently | Static reflection visible; Arda gasps |  |  |
| B-06 | 06 | Arda waves at reflection; sync wave from water | Arda finishes wave gesture | Hand returns to side; Arda grins |  |  |
| B-07 | 07 | Arda kneels, reaches finger toward surface | Finger hovers 1cm above water | Frozen anticipation; reflection syncs |  |  |
| B-08 | 08 | Finger touches water; ripples spread and break reflection | Ripples cover puddle surface | Final fascinated gaze at broken reflection |  |  |

Automatic failure conditions for every B test:

- The shot opens mid-air, mid-hop, mid-step, or mid-camera move contrary to its Clean Start State.
- Any required action continues beyond the cut or is completed only by the next shot.
- A new action begins during the final İki seconds.
- The camera is still panning, tilting, zooming, reframing, or searching during the final anchor.
- The character or water freezes unnaturally; natural breathing, blinking, ripples, and breeze are allowed.

## Gate C — Visual Quality and Continuity

| Test ID | Test | Pass criterion | Result | Evidence / notes |
|---|---|---|---|---|
| C-01 | Arda identity | Hair (dark brown fluffy), face, clothing (sky blue shirt, light blue pants), age (2-3), proportions match canonical Arda |  |  |
| C-02 | Puddle identity | Size, reflection properties, and location match screenplay and beat sheet |  |  |
| C-03 | World identity | Arda's Home Garden (wet grass, shrubs, fence, sky) remains stable |  |  |
| C-04 | Object state | Wet garden elements match `00_PREPRODUCTION/02-object-prop-map.md` |  |  |
| C-05 | Colour drift | Each shot remains within ±5% brightness and ±7% saturation of Episode Colour Master |  |  |
| C-06 | Quality reset | No progressive softness, contrast growth, oversharpening, distortion, or scale drift across 01–08 |  |  |
| C-07 | Frame integrity | No duplicate Arda, extra limbs, disappearing puddles, teleport, ghosting, text, watermark |  |  |
| C-08 | Crop safety | Arda's face and active splash/reflection action remain inside the central 60% safe region |  |  |

## Gate D — Dialogue, Sound, and Safety

| Test ID | Test | Pass criterion | Result | Evidence / notes |
|---|---|---|---|---|
| D-01 | Dialogue order | All scripted Arda lines occur in correct shot; no line omitted/invented |  |  |
| D-02 | Voice lock | Arda uses approved v2.1 voice identity; pitch, timbre, age, speed, warmth match reference |  |  |
| D-03 | Object sound | `splash`, `bloop` are soft, natural, correctly timed, and subordinate to dialogue |  |  |
| D-04 | Natural ambience | Garden ambience (soft birds, wind, rain droplets) remains calm; no music, melody, or chimes |  |  |
| D-05 | Movement safety | Puddle play is safe/shallow; no slipping, falling, or aggressive jumping |  |  |
| D-06 | Emotional safety | Surprise stays playful; Arda is never distressed or frightened by his reflection |  |  |

## Gate E — Full Episode Assembly

| Test ID | Test | Pass criterion | Result | Evidence / notes |
|---|---|---|---|---|
| E-01 | Runtime | Assembly is exactly 120 seconds |  |  |
| E-02 | Edit integrity | Every cut occurs after completed end state and stable anchor |  |  |
| E-03 | Story state | Editorial state remains logical across fresh cuts |  |  |
| E-04 | Audio continuity | Ambience and voice edits are clean; no hard pop, unwanted silence, music, or whoosh |  |  |
| E-05 | Ending | Shot 08 ends with ripples spreading; no preview from another episode |  |  |

## Final QA Decision

| Field | Entry |
|---|---|
| Episode version tested |  |
| Test date |  |
| Reviewer |  |
| Failed test IDs |  |
| Regeneration/repair required |  |
| Retest version |  |
| Final status | PASS / FAIL / BLOCKED |

Approval rule: `PASS` is permitted only when every mandatory A–E test is marked PASS and every
failure has been corrected and retested on the final export version.
