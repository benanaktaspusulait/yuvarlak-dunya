# Design Document

## Overview

This design describes how to restructure the S01E08 — "Building Together" episode package from a 4-shot / 60s form into an 8-shot / 120s form, as specified in `requirements.md`. The deliverable is a set of **production documents** (episode overview updates, eight shot documents, metadata, and archived backbone shots), not runtime software.

The design keeps the episode's emotional message — *"It's easier when we build together, and if it breaks we can try again."* — and expands the runtime through five genuinely new story beats rather than by stretching the existing four shots. It builds on the repo's proven S01E04 staged-production model (master setup frame + `@image1` continuity chain + preflight gates) and applies a strict **Global Block Object Rule** to control the highest-risk beats (tower fall, block scatter, height/count drift).

Package path: `POMPOM_HILLS_PRODUCTION/02_WORLDS/CENTRAL_SQUARE/04_EPISODE_PACKAGES/S01E08_BUILDING_TOGETHER/`

**Requirements coverage:** This design addresses Requirements 1–10 from `requirements.md`. Each design section notes the requirement IDs it satisfies.

---

## Architecture

The episode is a **linear chain of 8 shot documents** rendered as 8 video clips and concatenated into one 120s episode. The architecture has three layers:

1. **Authoring layer** — the markdown production artifacts (episode overview + 8 shot documents + metadata) in the package folder. These are the "source code" of the episode.
2. **Continuity layer** — the `@image1` first-frame chain: Shot 01 is the master setup frame; each subsequent shot consumes the previous shot's exported final frame as its only visual continuity source. This is the backbone that prevents drift.
3. **Control layer** — the Global Block Object Rule + preflight gates (A–D) + per-shot QA checklists that constrain what the generator may change.

```
Authoring:   overview + shot-01..08 md + metadata
Continuity:  Shot01(master) →@image1→ Shot02 →@image1→ ... → Shot08
Control:     Block Object Rule + Preflight status + QA checklist per shot
```

Detailed structure follows in Package File Structure and Continuity Chain Design.

---

## Components and Interfaces

*(Satisfies R5.2, R5.8, R5.9)*

- **Component: Episode Overview** — holds shared truth (duration, characters, world lock, block model, title). Interface: referenced by every shot; changes here propagate to all shots.
- **Component: Shot Document (×8)** — one per 15s clip. Interface: consumes an `@image1` frame + shared style/negative blocks; produces a final frame that becomes the next shot's `@image1`. Shots 02–08 depend on the prior shot's output frame.
- **Interface: `@image1` continuity contract** — the exported final frame of shot N is the exact first frame of shot N+1; `@image1` has priority for camera, lighting, composition, scale, environment. Optional `@image2` (reference) is subordinate.
- **Interface: Preflight status** — each shot exposes `SAFE` / `RISKY` / `NOT READY`; a `NOT READY` shot blocks the gate it belongs to.
- **Component: Archived backbone** — the 4 old shots in `06_ARCHIVE/` provide reference but are not part of the render chain.

---

## Data Models

*(Satisfies R4, R6.3)*

The two data structures for this episode are the **Block Object Model** and the **Tower State Ledger**, both defined in detail in the *Block Object Model* section below. Summary:

- **Block set** — fixed count (proposed 6), stable colours, round + flat shapes, `≤ head` tower ceiling.
- **Tower State Ledger** — per-shot `(block count, height)` at start and end, tracked for Shots 03–08 to make count/height continuity verifiable.

---

## Package File Structure

*(Satisfies R1.1–R1.8, R3, R5.9)*

### Files to CREATE (8 new shot documents in `01_SHOTS/`)

Kebab-case per `CONTRIBUTING.md`:

| New file | Beat |
|---|---|
| `shot-01-blocks-are-found.md` | Blocks Are Found (MASTER SETUP) |
| `shot-02-choosing-shapes.md` | Choosing Shapes |
| `shot-03-first-tower-attempt.md` | First Tower Attempt |
| `shot-04-tower-falls.md` | Tower Falls |
| `shot-05-small-feeling-beat.md` | Small Feeling Beat |
| `shot-06-new-plan.md` | New Plan (pointing/gaze lock) |
| `shot-07-careful-together-build.md` | Careful Together Build |
| `shot-08-tower-stands.md` | Tower Stands (finale) |

### Files to ARCHIVE (retain backbone, do not delete — R1.6)

Move the four existing shot files into `06_ARCHIVE/OLD_4_SHOT_VERSION/` with a short `README.md` note recording the old→new mapping (R1.7):

- `shot-01-gather-blocks.md` → archive (basis for new Shot 01)
- `shot-02-first-attempt.md` → archive (splits into new Shots 03 + 04)
- `shot-03-try-again.md` → archive (splits into new Shots 06 + 07)
- `shot-04-tower-stands.md` → archive (basis for new Shot 08)

### Files to MODIFY (`00_EPISODE_OVERVIEW/`)

- `01-overview.md` — duration `1:00 (4 shots)` → `2:00 (8 shots × 15s)`; QA Status table to 8 rows; story summary rewritten to the 8-beat arc; add title/alt-title line.
- `02-beat-sheet.md` — replace 4-beat rhythm with the 8-beat rhythm.
- `05-camera.md` — extend camera table to 8 shots (all static except the allowed gentle settle).
- `06-dialogues.md` — replace with the 8-shot dialogue set.
- `07-sfx.md`, `08-animation-notes.md` — extend to 8 shots.
- `COORDINATE_MAP.md` — extend to 8 shots; **fix Arda scale** (see Open Item OI-1); fill block/tower staging.
- `EPISODE_SUMMARY.md` / `EPISODE_SUMMARY_TR.md` — rewrite to the 8-beat structure and staged gates.
- `README.md` — update shot inventory to 8.
- `03-storyboard.md`, `04-assets.md`, `09-render-prompts.md` — extend to 8 shots; `09-render-prompts.md` consolidates the 8 OpenArt prompts + the shared Block negative-prompt block.

Downstream trackers (`08-PRODUCTION/EPISODE_TRACKER.md`, `CHARACTER_ANALYSIS.md`, etc.) reflect the 8-shot/120s change — handled as a task, not canon change.

---

## Block Object Model

*(Satisfies R4.1–R4.8, R6)*

The single source of movable props. Defined once in the overview and referenced by every shot.

| Attribute | Value |
|---|---|
| Block set | A fixed small set (recommended **6 blocks**) — locked count for the whole episode |
| Shapes | Mix of **round** and **flat** blocks (flat = stable base, round = accent) to support the Shot 02 shape-logic beat |
| Colours | Pastel Pompom palette (e.g. coral, yellow, blue, green); colours stable across all shots, no dramatic change |
| Tower height ceiling | **≤ characters' chest-to-head level**; taller requires explicit approval |
| Movability | Only characters move individual blocks during building; blocks never spawn, vanish, morph, duplicate, or transform |

### Reusable Block Negative-Prompt Block (pasted into every shot's Negative Prompt — R4.4)

```text
new blocks, extra blocks, missing blocks, disappearing blocks, changing block colours,
blocks turning into toys, furniture, stones, food, boxes, tools, letters or signs,
tower taller than the children, giant tower, oversized tower, duplicated blocks,
morphing blocks, floating blocks
```

### Tower state ledger (R6.3)

Each of Shots 03–08 records **Tower block count + height at start and at end** so continuity is verifiable along the chain. Example ledger the shot docs will carry:

| Shot | Start (count / height) | End (count / height) |
|---|---|---|
| 03 First attempt | 0 stacked / ground | ~4 stacked / wobbly, chest-high |
| 04 Tower falls | ~4 stacked | 0 stacked / 6 scattered (same 6 blocks) |
| 06 New plan | 6 scattered | 6 scattered (1 big block placed as base) |
| 07 Together build | 1 base | ~5 stacked / rising |
| 08 Tower stands | ~5–6 stacked | full tower standing, ≤ head-high |

---

## Continuity Chain Design

*(Satisfies R5.1–R5.10, R6.1–R6.4)*

Single continuous location (Central Square), single continuous build area → one master setup frame anchors the whole episode.

- **Shot 01 = MASTER SETUP frame.** Seeds everything used later: the full 6-block set (round + flat), the build area on the ground near the Big Pompom Tree, Noah, Arda, warm morning daylight. All later interaction objects must exist here (R4.7, R5.10).
- **Shots 02–08 = continuation.** Each uses the **previous shot's exported final frame as `@image1`** and only visual continuity source (R5.2), holds ≈1s on `@image1` before new action (R5.3), and forbids camera reset/pan/zoom/tracking/pull-back beyond the small allowed settle (R5.4).
- **Lighting locked** to morning daylight from `@image1` across all 8 shots — no drift to sunset/golden/grey (R5.5). Note: the old Shot 04 mentioned "golden light" and stray "moonlight" text; the new Shot 08 stays morning daylight to avoid a lighting jump.
- **Tower Falls → Feeling Beat bridge (Shot 04 → 05):** Shot 05 begins from Shot 04's final frame; the scattered-block positions are preserved exactly (R6.4). No re-scatter, no cleanup, no new arrangement between the two shots.

```
Shot01 (master) → Shot02 → Shot03 → Shot04 → Shot05 → Shot06 → Shot07 → Shot08
   seeds 6 blocks         build   FALL   feeling  plan    rebuild  stands
   + build area                   (scatter preserved into 05)
```

---

## Per-Shot Design Table

*(Satisfies R2.1–R2.9, R5, R7, R8, R9)*

| # | Beat purpose | Camera | Start frame | Key action | Dialogue | Objects (seeded/used) | Primary risk → mitigation |
|---|---|---|---|---|---|---|---|
| 01 | Establish blocks as episode object; introduce pair | Wide→medium, edge/entrance intro (no center pop-in) | Micro-opening env as `@image1` (env only) | Noah arranges blocks; Arda arrives | "Look at these blocks." / "Can we build?" | **Seeds all 6 blocks** + build area | Under-seeding → checklist: all 6 blocks + build area visible before approval |
| 02 | Plan / simple shape logic | Static (settle only) | Shot 01 final | Pick round vs flat block | "This one?" / "The flat one first." | Uses seeded blocks | Blocks morphing → Block negative block |
| 03 | First build, gentle tension | Static | Shot 02 final | Stack wobbly tower | "Careful..." / "I am careful!" | Blocks → tower (~4, chest-high) | Tower grows too tall → height ledger + ≤head check |
| 04 | Problem: soft fall | Static | Shot 03 final | Tower topples softly, blocks scatter gently | "Oh no!" / "It fell." | Same 6 blocks scatter (none leave/enter) | Scary/fast fall, block count change → R8.2 soft-fall + R6.1/6.2 count lock |
| 05 | Emotional centre (NEW) | Static | Shot 04 final (scatter preserved) | Arda small shoulder-drop; Noah calm support | "I can't do it." / "We can try together." | Scattered blocks held in place | Reads as distress → R8.3 brief+supportive check |
| 06 | Problem-solving plan; pointing lock | Static | Shot 05 final | Noah points: big block bottom, small on top | "Big block first." / "Small block on top?" / "Yes." | Names/points target block (visible) | Ambiguous point → R7 hand+eyes+head+torso aligned, target in frame, Arda turns to same block |
| 07 | Teamwork made physical | Static | Shot 06 final | One holds, one places; rebuild slowly | "You hold it." / "I've got it." | Blocks → rising tower | Height/continuity drift → ledger check |
| 08 | Warm resolution | Static (gentle settle only, no pull-back) | Shot 07 final | Tower stands; both happy | "We did it!" / "Together!" | Full tower ≤ head-high | Lighting jump / pull-back → keep morning light, no pull-back (deviates from old Shot 04) |

Every shot: only Noah + Arda (R3.1/3.2); dialogue never on-screen text (R9.1); natural ambience, no music (R9.3); calm-but-alive beat every 2–3s (R10.3); no dialogue-line repeats across shots (R9.4).

---

## Shot Document Template

*(Satisfies R5.7, R5.9, R10.1–R10.6)*

Each of the 8 shot files follows the repo's established shot structure (as in the current S01E08 shots and produced S01E04 shots):

1. **Scene Context** (episode, shot N/08, 15s, location, characters, time)
2. **Shot Contract** + **Preflight status** (`SAFE` / `RISKY` / `NOT READY`) per `19_VIDEO_PRODUCTION_PREFLIGHT_SYSTEM.md`
3. **Continuity** (what it continues from)
4. **Start Frame** (`@image1` source; 1s hold)
5. **Background Object Lock**
6. **Visual Prompt** (`{style} {camera} {lighting}`, no-text line)
7. **Reference Usage** (`@image1` role/priority; `@image2` only if used, with priority note — R5.8)
8. **Camera Direction** (static + allowed settle)
9. **Dialogue**
10. **Shot Breakdown** (0–15s beat table)
11. **Natural Character Motion Rule**
12. **Sound** (natural ambience only)
13. **Negative Prompt** (base + **Block negative block** + music ban)
14. **QA Checklist** (base continuity/safety + shot-specific rows)
15. **Tower State Ledger** row (Shots 03–08)

---

## Pointing / Gaze / Orientation Design (Shot 06)

*(Satisfies R7.1–R7.5)*

Shot 06 carries an explicit **Pointing & Gaze Lock** section per `18_OPENART_CONTINUITY_AND_MOTION_RULES.md` §17:

- Target block named for each pointing beat ("the big flat block", "the small round block").
- Target block must be visible in frame during the point.
- Noah's **pointing hand + eyes + head + shoulders + upper body** all align to the target block.
- Arda **turns toward the same target block** when Noah indicates it.
- Forbid pointing at empty space or gaze/point mismatch.

---

## Preflight & Staged Production Gates

*(Satisfies R5.9, R5.10, R6.7)*

Following the S01E04 staged model. Do NOT generate all 8 at once.

- **Gate A — Shot 01 master setup only.** Approve only if all 6 blocks + build area seeded, pair introduced without center pop-in, morning light, blocks reachable for later stacking. If an interaction object is missing → `NOT READY`, fix Shot 01 (not later prompts).
- **Gate B — Shots 02→03→04.** Per shot, confirm the next shot's required blocks are still visible/usable in the final frame; Shot 04 verified for soft fall + preserved block count.
- **Gate C — Shot 05 (feeling beat) + Shot 06 (pointing).** Verify scatter preserved from Shot 04; verify pointing/gaze alignment.
- **Gate D — Shots 07→08.** Verify tower height ledger and morning-light hold; Shot 08 no pull-back.

Each shot ends with a status of `SAFE` / `RISKY` / `NOT READY` (R5.9). A shot violating block count/height/identity continuity is rejected (R6.7).

---

## Title Decision

*(Satisfies R1.8)*

Keep canonical title **"Building Together"** (already used across trackers, subtitles, SERIES_STRUCTURE). Record **"We Build Together"** as an alternate/marketing title in the overview only. This avoids touching canon naming across many files while preserving the user's suggestion. Final choice deferred to user (Open Item OI-2).

---

## Old vs New Mapping

*(Satisfies R1.7)*

```
Old (60s):  Gather ──── First Attempt/Fall ──── Try Again ──── Success
             │               │                      │              │
New (120s): 01 Blocks   03 First build          06 New plan     08 Tower
            Found       04 Tower falls          07 Together      stands
            02 Choose                            build
            shapes      05 Feeling beat (NEW)
```

- Old Shot 01 → New Shot 01 (clearer "blocks found")
- Old Shot 02 → New Shots 03 + 04
- Old Shot 03 → New Shots 06 + 07
- Old Shot 04 → New Shot 08
- New Shots 02 and 05 are wholly new beats.

---

## Correctness Properties

*(Satisfies R4, R5, R6, R8)*

Invariants that must hold across the whole episode (checked per shot):

### Property 1: Block-count constancy
The same fixed block set is present in every shot from Shot 01 onward; no block spawns, disappears, or duplicates.
**Validates: Requirements 4.2, 6.2, 6.5**

### Property 2: Block-identity stability
Blocks never morph into other objects and their colours stay stable across all shots.
**Validates: Requirements 4.3, 4.4**

### Property 3: Tower height ceiling
The tower never exceeds the children's head level.
**Validates: Requirements 4.5, 6.6**

### Property 4: Lighting constancy
Morning daylight is preserved on every frame; no sunset/golden/grey drift.
**Validates: Requirements 5.5**

### Property 5: Cast constancy
Only Noah and Arda appear in every shot.
**Validates: Requirements 3.1**

### Property 6: Frame continuity
Each shot's first frame equals the previous shot's final frame; scatter positions are preserved across the Shot 04→05 transition.
**Validates: Requirements 5.2, 6.4**

### Property 7: Preschool safety
No fear/shame/loud/fast content; the tower fall is soft only.
**Validates: Requirements 8.2, 8.3**

## Error Handling

*(Satisfies R5.9, R5.10, R6.7)*

- **Missing seeded object** → shot marked `NOT READY`; fix the master setup (Shot 01) rather than the downstream prompt.
- **Object/height/count continuity violation in a generated clip** → shot **rejected** by QA; regenerate from the same `@image1`.
- **Lighting/camera drift** → reject; re-run with the `@image1` lock reinforced.
- **Ambiguous pointing (Shot 06)** → reject; re-run with the Pointing & Gaze Lock section.
- **Gate failure** → do not proceed to the next gate until the failing shot is `SAFE`.

## Testing Strategy

*(Satisfies R6, R10)*

- **Per-shot QA checklist** — every shot carries the base continuity/safety checklist plus shot-specific rows (block ledger, height, pointing, feeling-beat tone).
- **Staged gates (A–D)** — act as integration checkpoints; each gate approves before the next begins.
- **Chain test** — verify each shot's final frame is usable as the next `@image1` without crop/close-up/lighting/scale/new-object change (R10.4).
- **Liveliness test** — confirm a clear action/reaction/dialogue beat every 2–3s, no dead air (R10.3).
- **Full-assembly review** — after all 8 clips pass, review the concatenated 120s cut for arc clarity and message delivery.

## Resolved Decisions (confirmed by user)

- **D-1 — Arda scale.** Character canon wins: Arda is ~85 units (younger, slightly smaller than Noah). The package `COORDINATE_MAP.md` (currently Arda=100) is corrected to match in Tasks.
- **D-2 — Title.** Canonical title stays **"Building Together"**; **"We Build Together"** is recorded as an alternate title in the overview only.
- **D-3 — Block count.** Locked at **6 blocks**: 2 large flat blocks (stable base) + 4 medium round/flat blocks (upper stack). This supports the "big block first, small block on top" plan beat and a tower that rises to ≤ head height.
