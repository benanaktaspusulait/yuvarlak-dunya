# S01E08 — Building Together — Detailed Summary

---

## Overview

| Info | Value |
|---|---|
| Duration | 2:00 (8 shots × 15 seconds) |
| Title | Building Together (alt: "We Build Together") |
| Theme | Cooperation and teamwork |
| Learning | Teamwork • Patience • Trying again |
| Message | "It's easier when we build together, and if it breaks we can try again." |
| Target age | 3-4 |
| Main emotion | Perseverance + joy |
| Characters | Noah (builder, scale 100), Arda (helper, ~85, slightly smaller) |
| Location | Central Square |

---

## Location Flow

| Location | File | Shots |
|---|---|---|
| Central Square | `environment/01-central-square/hero-view.png` | 01–08 |

---

## Block Object Model

The building blocks are the only movable prop: a fixed set of **8 blocks** (2 large flat + 3 medium flat/rounded + 3 small round/soft), stable pastel colours, tower height **≤ head level**. Blocks never spawn, vanish, morph, duplicate, or transform. Seeded in Shot 01. See `01-overview.md` for the reusable Block negative-prompt block and Tower State Ledger.

---

## Shot-by-Shot

### Shot 01 — Blocks Are Found (0-15s) — MASTER SETUP
Noah finds the eight colourful blocks under the Big Pompom Tree; Arda arrives. All exterior objects (8 blocks + build area) are seeded here.
**Dialogue:** Noah: "Look at these blocks." / Arda: "Can we build?" / Noah: "Yes!"

### Shot 02 — Choosing Shapes (15-30s)
They pick shapes: Arda lifts a round block, Noah shows the flat block goes first (the base).
**Dialogue:** Arda: "This one?" / Noah: "The flat one first."

### Shot 03 — First Tower Attempt (30-45s)
They stack a chest-high tower; it wobbles (gentle tension).
**Dialogue:** Noah: "Careful..." / Arda: "I am careful!"

### Shot 04 — Tower Falls (45-60s)
The tower softly topples; the same eight blocks scatter gently. Safe, not scary.
**Dialogue:** Arda: "Oh no!" / Noah: "It fell."

### Shot 05 — Small Feeling Beat (60-75s)
Arda is briefly discouraged; Noah reassures him calmly. Emotional centre. (Scatter positions preserved from Shot 04.)
**Dialogue:** Arda: "I can't do it." / Noah: "We can try together."

### Shot 06 — New Plan (75-90s)
Noah shows the plan — big block bottom, small on top — with clear pointing/gaze aligned to the target block; Arda follows.
**Dialogue:** Noah: "Big block first." / Arda: "Small block on top?" / Noah: "Yes."

### Shot 07 — Careful Together Build (90-105s)
Teamwork made physical: one holds, one places; the tower rises steadily (≤ head).
**Dialogue:** Arda: "You hold it." / Noah: "I've got it."

### Shot 08 — Tower Stands (105-120s)
The tower stands; they celebrate. Warm morning light held (no golden/sunset), no pull-back.
**Dialogue:** Noah: "We did it!" / Arda: "Together!"

---

## Staged Production Gates (DO NOT generate all 8 at once)

Shot 01 is the master setup; if it fails, the rest collapses.

- **Gate A — Shot 01 only.** Approve only if all 8 blocks + build area are seeded and usable, pair introduced without center pop-in, morning light, tower-able layout. If an object is missing → NOT READY; fix Shot 01, not later prompts.
- **Gate B — Shots 02 → 03 → 04.** Per shot, confirm the next shot's required blocks are still visible/usable. Shot 04: verify soft fall + same 8 blocks preserved.
- **Gate C — Shots 05 → 06.** Verify Shot 04 scatter preserved into 05; verify Shot 06 pointing/gaze/orientation alignment.
- **Gate D — Shots 07 → 08.** Verify tower height ledger (≤ head) and warm-morning-light hold; Shot 08 no pull-back.

Each shot carries a preflight status: **SAFE / RISKY / NOT READY**. A shot violating block count/height/identity continuity is rejected.

---

*Learning: Falling down sometimes just means trying again — and trying together is best of all.*
