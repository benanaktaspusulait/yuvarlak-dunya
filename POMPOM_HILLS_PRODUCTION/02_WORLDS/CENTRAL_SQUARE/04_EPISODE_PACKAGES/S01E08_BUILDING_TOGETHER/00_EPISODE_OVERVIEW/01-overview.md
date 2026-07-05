# S01E08 — Building Together

> **Title:** Building Together (alternate/marketing title: "We Build Together")

---

## Duration

2:00 (8 shots × 15 seconds)

---

## Theme

Cooperation and teamwork.

---

## Learning

Teamwork • Patience • Trying again

---

## Episode Message

"It's easier when we build together, and if it breaks we can try again."

---

## Characters

| Character | Role | Scale |
|---|---|---|
| Noah | Builder | 100 units |
| Arda | Helper | ~85 units (younger, slightly smaller than Noah) |

---

## World

Central Square

---

## Story Summary

Noah finds a set of colourful building blocks in Central Square, and Arda joins him. They pick
shapes and try to build a tower, but their first attempt wobbles and falls. Arda feels a little
discouraged, but Noah gently reassures him — they can try again together. With a new plan (big
block on the bottom, small block on top) and by working as a team (one holds, one places), they
rebuild the tower. This time it stands, and they celebrate: "Together!"

---

## Block Object Model (episode prop lock)

The building blocks are the **only** movable prop in this episode.

| Attribute | Value |
|---|---|
| Block set | **6 blocks, fixed count** for the whole episode |
| Composition | 2 large flat blocks (stable base) + 4 medium round/flat blocks (upper stack) |
| Colours | Pastel Pompom palette (coral, yellow, blue, green); stable across all shots |
| Tower height ceiling | **≤ the children's chest-to-head level** (taller requires explicit approval) |
| Movability | Only characters move individual blocks during building; blocks never spawn, vanish, morph, duplicate, or transform |

### Global Block Object Rule (reusable negative-prompt block)

Paste into every shot's Negative Prompt:

```text
new blocks, extra blocks, missing blocks, disappearing blocks, changing block colours,
blocks turning into toys, furniture, stones, food, boxes, tools, letters or signs,
tower taller than the children, giant tower, oversized tower, duplicated blocks,
morphing blocks, floating blocks
```

### Tower State Ledger

| Shot | Start (stacked / height) | End (stacked / height) |
|---|---|---|
| 03 First attempt | 0 / ground | ~4 / wobbly, chest-high |
| 04 Tower falls | ~4 | 0 stacked / 6 scattered (same 6 blocks) |
| 06 New plan | 6 scattered | 6 scattered (1 big block placed as base) |
| 07 Together build | 1 base | ~5 / rising |
| 08 Tower stands | ~5–6 | full tower standing, ≤ head-high |

---

## Shot List

| # | Shot | Beat |
|---|---|---|
| 01 | Blocks Are Found | Master setup — seeds all 6 blocks + build area |
| 02 | Choosing Shapes | Plan: round vs flat |
| 03 | First Tower Attempt | Wobbly rise, gentle tension |
| 04 | Tower Falls | Soft fall, blocks scatter gently |
| 05 | Small Feeling Beat | Arda discouraged, Noah reassures (emotional centre) |
| 06 | New Plan | Big block bottom, small on top (pointing/gaze lock) |
| 07 | Careful Together Build | One holds, one places (teamwork) |
| 08 | Tower Stands | Finale, "Together!" |

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
