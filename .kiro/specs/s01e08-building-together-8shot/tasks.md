# Implementation Plan

## Overview

Production-document build plan for restructuring S01E08 "Building Together" into an 8-shot / 120s episode. Every task writes or edits markdown artifacts in the episode package; no video is generated in this plan. All shots follow the Shot Document Template and inherit the Block Object Model, continuity chain, and safety rules from `design.md`.

Package root: `POMPOM_HILLS_PRODUCTION/02_WORLDS/CENTRAL_SQUARE/04_EPISODE_PACKAGES/S01E08_BUILDING_TOGETHER/`

## Tasks

- [x] 1. Archive the old 4-shot version (preserve backbone)
  - Create `06_ARCHIVE/OLD_4_SHOT_VERSION/` and move `shot-01-gather-blocks.md`, `shot-02-first-attempt.md`, `shot-03-try-again.md`, `shot-04-tower-stands.md` into it
  - Add `06_ARCHIVE/OLD_4_SHOT_VERSION/README.md` recording the old→new mapping (01→01, 02→03+04, 03→06+07, 04→08) and why the 4-shot version was superseded
  - _Requirements: 1.6, 1.7_

- [x] 2. Define shared episode truth in the overview
- [x] 2.1 Update `00_EPISODE_OVERVIEW/01-overview.md`
  - Duration `1:00 (4 shots)` → `2:00 (8 shots × 15s)`; rewrite story summary to the 8-beat arc; add episode message; add title line ("Building Together" / alt "We Build Together"); expand QA Status table to 8 rows
  - _Requirements: 1.1, 1.2, 1.3, 1.8, 2.9_
- [x] 2.2 Add a "Block Object Model" + "Global Block Object Rule" section to the overview
  - Document the locked 6-block set (2 large flat + 4 round/flat), stable colours, tower height ceiling (≤ head), and the reusable Block negative-prompt block
  - _Requirements: 4.1, 4.3, 4.4, 4.5_
- [x] 2.3 Update `00_EPISODE_OVERVIEW/02-beat-sheet.md` to the 8-beat rhythm
  - _Requirements: 1.4, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8_

- [x] 3. Write Shot 01 — Blocks Are Found (MASTER SETUP)
  - Create `01_SHOTS/shot-01-blocks-are-found.md` per the Shot Document Template
  - Seed all 6 blocks + build area near the Big Pompom Tree; introduce Noah + Arda via edge/entrance (no center pop-in); morning daylight; dialogue "Look at these blocks." / "Can we build?"
  - Include Background Object Lock, Block negative block, music ban, QA checklist with "all 6 blocks + build area seeded" gate; mark preflight status
  - _Requirements: 2.1, 3.1, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 4.7, 5.1, 8.1, 9.1, 9.3, 10.1, 10.2, 10.3, 10.4_

- [x] 4. Write Shot 02 — Choosing Shapes
  - Create `01_SHOTS/shot-02-choosing-shapes.md`; `@image1` = Shot 01 final; static camera; round vs flat shape logic; dialogue "This one?" / "The flat one first."
  - _Requirements: 2.2, 4.8, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 9.4, 9.5_

- [x] 5. Write Shot 03 — First Tower Attempt
  - Create `01_SHOTS/shot-03-first-tower-attempt.md`; wobbly rise, gentle tension; dialogue "Careful..." / "I am careful!"
  - Add Tower State Ledger row (start 0 stacked → end ~4 stacked, chest-high, ≤ head)
  - _Requirements: 2.3, 4.5, 6.3, 6.6_

- [x] 6. Write Shot 04 — Tower Falls
  - Create `01_SHOTS/shot-04-tower-falls.md`; soft, gentle fall; blocks scatter within locked composition; dialogue "Oh no!" / "It fell."
  - Ledger: same 6 blocks before and after (count/identity preserved); QA rows for soft-fall safety + no block leaves/enters set
  - _Requirements: 2.4, 6.1, 6.2, 6.5, 6.7, 8.2_

- [x] 7. Write Shot 05 — Small Feeling Beat (NEW)
  - Create `01_SHOTS/shot-05-small-feeling-beat.md`; `@image1` = Shot 04 final with scatter positions preserved; Arda small shoulder-drop, Noah calm support; dialogue "I can't do it." / "We can try together."
  - QA rows: brief+supportive tone (not distress); scatter positions preserved from Shot 04
  - _Requirements: 2.5, 6.4, 8.3, 10.5_

- [x] 8. Write Shot 06 — New Plan (pointing/gaze lock)
  - Create `01_SHOTS/shot-06-new-plan.md`; Noah shows big block bottom / small on top; dialogue "Big block first." / "Small block on top?" / "Yes."
  - Add explicit Pointing & Gaze Lock section (hand+eyes+head+shoulders+torso aligned to named, visible target block; Arda turns to same block); QA row for alignment
  - _Requirements: 2.6, 7.1, 7.2, 7.3, 7.4, 7.5, 10.6_

- [x] 9. Write Shot 07 — Careful Together Build
  - Create `01_SHOTS/shot-07-careful-together-build.md`; one holds, one places; slow rebuild showing teamwork; dialogue "You hold it." / "I've got it."
  - Ledger: rising tower; height ≤ head
  - _Requirements: 2.7, 4.5, 6.3, 6.6_

- [x] 10. Write Shot 08 — Tower Stands (finale)
  - Create `01_SHOTS/shot-08-tower-stands.md`; tower stands ≤ head-high; both happy; dialogue "We did it!" / "Together!"
  - Keep morning daylight (no golden/sunset drift, no pull-back — deviates from old Shot 04); ledger final full tower
  - _Requirements: 2.8, 5.4, 5.5, 6.3, 6.6_

- [x] 11. Extend remaining overview/metadata to 8 shots
- [x] 11.1 Update `05-camera.md`, `06-dialogues.md`, `07-sfx.md`, `08-animation-notes.md`, `03-storyboard.md`, `04-assets.md`, `09-render-prompts.md` to cover all 8 shots (all static except allowed settle; `09-render-prompts.md` consolidates the 8 prompts + shared Block negative block)
  - _Requirements: 1.1, 5.4, 9.1, 9.3_
- [x] 11.2 Update `COORDINATE_MAP.md`: extend to 8 shots, fix Arda scale to ~85 units (D-1), fill block/tower staging
  - _Requirements: 3.5_
- [x] 11.3 Rewrite `EPISODE_SUMMARY.md` and `EPISODE_SUMMARY_TR.md` to the 8-beat structure + staged gates A–D; update `00_EPISODE_OVERVIEW/README.md` shot inventory to 8
  - _Requirements: 1.4, 5.9_

- [x] 12. Add staged production gates + preflight statuses
  - In `EPISODE_SUMMARY.md`, document Gates A–D (A: Shot 01 only; B: 02–04; C: 05–06; D: 07–08) and require each shot to carry SAFE/RISKY/NOT READY
  - Confirm each shot file includes a Shot Contract + preflight status line
  - _Requirements: 5.9, 5.10, 6.7_

- [x] 13. Update downstream production trackers
  - `08-PRODUCTION/EPISODE_TRACKER.md`: S01E08 row `4 sahne × 15 sn = 60 sn` → `8 sahne × 15 sn = 120 sn` (status stays 🟡 Yazıldı)
  - Check `CHARACTER_ANALYSIS.md` and other S01E08 references for the 60s→120s duration change
  - _Requirements: 1.1, 1.3_

- [x] 14. Full spec-consistency review (joint read-through checkpoint)
  - Read all 8 shot files end-to-end as one episode; verify continuity chain (@image1), Block Object Rule, tower ledger, lighting/cast invariants, pointing lock, and preschool safety; confirm no dialogue-line repeats across shots
  - Fix any inconsistencies found before generation
  - _Requirements: 6.1, 6.2, 6.3, 6.4, 9.4, 10.3, 10.4_

## Task Dependency Graph

```json
{
  "waves": [
    { "wave": 1, "tasks": ["1", "2.1", "2.2", "2.3"], "reason": "Archive backbone and establish shared episode truth (overview, block model, beat sheet) before any shot is written." },
    { "wave": 2, "tasks": ["3"], "reason": "Shot 01 is the master setup frame that seeds all objects; all later shots depend on it." },
    { "wave": 3, "tasks": ["4"], "reason": "Shot 02 continues from Shot 01 final frame." },
    { "wave": 4, "tasks": ["5"], "reason": "Shot 03 continues from Shot 02 final frame." },
    { "wave": 5, "tasks": ["6"], "reason": "Shot 04 continues from Shot 03 final frame." },
    { "wave": 6, "tasks": ["7"], "reason": "Shot 05 continues from Shot 04 final frame with scatter preserved." },
    { "wave": 7, "tasks": ["8"], "reason": "Shot 06 continues from Shot 05 final frame." },
    { "wave": 8, "tasks": ["9"], "reason": "Shot 07 continues from Shot 06 final frame." },
    { "wave": 9, "tasks": ["10"], "reason": "Shot 08 continues from Shot 07 final frame." },
    { "wave": 10, "tasks": ["11.1", "11.2", "11.3", "12", "13"], "reason": "Overview/metadata, gates, and trackers can be finalized once all 8 shots exist; these are mutually independent." },
    { "wave": 11, "tasks": ["14"], "reason": "Final joint read-through consistency review after everything is written." }
  ]
}
```

- Tasks 3–10 are strictly sequential (each shot's `@image1` continuity depends on the previous shot).
- Task 2 (and its subtasks) must precede shot writing (shared block model/truth).
- Task 1 can run first, independently.
- Tasks 11–13 depend on all 8 shots existing; Task 14 is the final checkpoint the user will review jointly.

## Notes

- No video generation in this plan — deliverables are markdown production artifacts only.
- Canon files (`00-CORE/*`, `01-CHARACTERS/*`, Central Square world files) are read-only references; do not edit them.
- Confirmed decisions from design: D-1 Arda ~85 units, D-2 title "Building Together" (alt "We Build Together"), D-3 locked 6-block set.
- Task 14 is the joint read-through the user requested before any generation.
