# AS-EP01 — Shot Completion and Quality-Reset QA Test

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
| B-01 | 01 | Ball rises; Arda completes one secure two-handed catch | Ball secured in both hands | Arda holds ball and smiles; only natural micro-motion |  |  |
| B-02 | 02 | Invitation and three-finger gesture complete; both hands return to ball | Arda in balanced ready pose | Ready pose holds; no new gesture or bounce begins |  |  |
| B-03 | 03 | First bounce travels down and returns to Arda's hands | Ball securely hugged | Calm hug holds; no release begins |  |  |
| B-04 | 04 | Second bounce drifts right; one safe side-step and catch complete | Arda balanced with ball secured | Catch pose and smile hold |  |  |
| B-05 | 05 | Stronger third bounce rises, misses, softly boops Arda's nose, lands, and stops | Ball fully at rest on grass; Arda grounded | Arda and ball remain stable |  |  |
| B-06 | 06 | From rest, ball rolls; Arda reaches once; ball slows and stops | Ball stationary before gate; Arda stopped safely | Both remain stationary |  |  |
| B-07 | 07 | Arda reacts, speaks, walks to marker, and stops; ball never moves | Arda balanced behind stationary ball | Both remain stationary |  |  |
| B-08 | 08 | From rest, ball rolls through gate and stops; Arda reaches gate and stops | Ball stationary on path; Arda stopped at gate | Final tableau holds |  |  |

Automatic failure conditions for every B test:

- The shot opens mid-air, mid-bounce, mid-roll, mid-step, or mid-camera move contrary to its Clean
  Start State.
- Any required action continues beyond the cut or is completed only by the next shot.
- A new action begins during the final two seconds.
- The camera is still panning, tilting, zooming, reframing, or searching during the final anchor.
- The character or ball freezes unnaturally; natural breathing, blinking, breeze, and fibre motion
  are allowed.

## Gate C — Visual Quality and Continuity

| Test ID | Test | Pass criterion | Result | Evidence / notes |
|---|---|---|---|---|
| C-01 | Arda identity | Hair, face, clothing, age, proportions, and scale match canonical Arda in all shots |  |  |
| C-02 | Ball identity | Same diameter, pastel blend, fluffiness, softness, and floaty physics in all shots |  |  |
| C-03 | World identity | House, garden, fence/shrubs, gate, path connection, and layout do not redesign or morph |  |  |
| C-04 | Object state | Ball and Arda start/end states match `00_PREPRODUCTION/02-object-prop-map.md` |  |  |
| C-05 | Colour drift | Each shot remains within ±5% brightness and ±7% saturation of Episode Colour Master |  |  |
| C-06 | Quality reset | No progressive softness, contrast growth, oversharpening, distortion, or scale drift across 01–08 |  |  |
| C-07 | Frame integrity | No duplicate Arda, extra limbs, disappearing ball, teleport, ghosting, text, watermark, or new object |  |  |
| C-08 | Crop safety | Arda's face and active ball action remain inside the central 60% safe region |  |  |

If C-05 or C-06 fails, reject the affected fresh generation. Do not solve generation degradation
by linking it to another generated frame. Final episode-wide colour matching may correct small
approved deviations only after all source shots pass identity and structural QA.

## Gate D — Dialogue, Sound, and Safety

| Test ID | Test | Pass criterion | Result | Evidence / notes |
|---|---|---|---|---|
| D-01 | Dialogue order | All scripted Arda lines occur in the correct shot and order; no line is omitted or invented |  |  |
| D-02 | Voice lock | Arda uses the same approved voice identity, pitch, timbre, age, speed, and warmth |  |  |
| D-03 | Object sound | `poof`, `boing`, `boop`, and `frrr-frrr` are soft, correctly timed, and subordinate to dialogue |  |  |
| D-04 | Natural ambience | Garden/path ambience remains calm; no music, melody, chime, whoosh, or dramatic sting |  |  |
| D-05 | Movement safety | No running, falling, collision, unsafe gate/path, vehicle, cliff, hard obstacle, or aggressive play |  |  |
| D-06 | Emotional safety | Surprise stays playful; Arda is never distressed, mocked, frightened, or hurt |  |  |

## Gate E — Full Episode Assembly

| Test ID | Test | Pass criterion | Result | Evidence / notes |
|---|---|---|---|---|
| E-01 | Runtime | Assembly is exactly 120 seconds before optional platform end card |  |  |
| E-02 | Edit integrity | Every cut occurs after the completed end state and stable anchor; no cut hides unfinished action |  |  |
| E-03 | Story state | Editorial state remains logical across fresh cuts without requiring pixel-identical continuity |  |  |
| E-04 | Audio continuity | Ambience and voice edits are clean; no hard pop, unwanted silence, music, chime, or whoosh |  |  |
| E-05 | Ending | Shot 08 ends with ball stationary on path and Arda stationary at gate; no preview from another episode |  |  |

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
