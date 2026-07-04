# Episode Template v1.0

> **LOCKED** — 3 July 2026
> This template is production-ready. Do not modify without a real production problem that cannot be solved within the existing structure.
> Changes must be driven by observed failures in actual production runs, not theoretical improvements.

---

## What This Template Is

S01E13 — Where Does Rain Come From is the reference implementation of Episode Template v1.0.

Every future episode should follow this structure unless a specific story requires a deliberate exception.

---

## Template Structure

### Files Required Per Episode

```
s01eXX-episode-name/
  ├── 01-overview.md          Episode lock, theme, characters, world, emotional flow,
  │                           Episode Master Frame, Emotional Voice Progression
  ├── 02-beat-sheet.md        Story rhythm, Cloud/World progression, shot micro beats,
  │                           dialogue principle
  ├── 03-storyboard.md        Shot-by-shot visual description
  ├── 04-assets.md            Characters, environment, identity anchors,
  │                           spatial continuity of key props
  ├── 05-camera.md            Shot-by-shot camera plan
  ├── 06-dialogues.md         All lines, silence beats, character line summary
  ├── 07-sfx.md               Sound effects, ambience, music rules
  ├── 09-render-prompts.md    Global rules, Episode Master Frame, World/Cloud progression,
  │                           shot-by-shot prompts, negative prompt
  ├── shots/
  │   ├── shot-01-[name].md
  │   ├── shot-02-[name].md
  │   ├── shot-03-[name].md
  │   ├── shot-04-[name].md
  │   ├── shot-05-[name].md
  │   └── shot-06-[name].md
  └── SXXeXX_PRODUCTION_REPORT.md   Completed after production run
```

### Required Sections Per Shot File

```
Scene Context          (episode, shot number, duration, location, characters, time)
Purpose                (what this shot does for the story)
Continuity             (previous shot state + world/cloud progression — one sentence)
Start Frame            (@image1 lock — shots 02–06 only)
Visual Prompt          (generation prompt)
Emotional Voice Progression  (one sentence — voice performance tone for this shot)
Voice Continuity       (maintain same voice identity)
Colour Continuity      (match previous shot — never rebalance)
Camera Direction       (movement, framing, forbidden moves)
Dialogue               (exact lines — code block)
Shot Breakdown         (time / action / camera table)
Sound                  (ambience and SFX notes)
Lighting               (rules for this shot)
Emotion                (one word or phrase)
Negative Prompt        (full list)
QA Checklist           (shot-specific checks)
```

---

## Key Production Rules

### Episode Master Frame
Before Shot 01, generate one canonical opening still using the world's Hero View + character references. Shot 01 begins from this still. All subsequent shots chain from the previous shot's last frame.

### Emotional Voice Arc
Define a voice performance tone per shot. Tone shifts across the episode but the voice identity stays the same.

### World Progression
Track a single evolving world element across all shots (cloud state, light change, approaching destination). One sentence per shot in the Continuity section.

### Spatial Anchor
Identify one key world prop that appears across shots and define its position per shot. Use it to build spatial memory.

### Colour Lock
Every shot treats the previous shot as the colour master reference. Never rebalance between shots.

### Story Structure
```
6 shots × 15 seconds = 90 seconds

Shot 01  Arrive + notice
Shot 02  Wonder + question
Shot 03  Observe + think
Shot 04  Wait + listen
Shot 05  Discovery
Shot 06  Joy + closing wide with silent hold
```

---

## Reference Implementation

| File | Path |
|------|------|
| Full episode | `POMPOM_HILLS_PRODUCTION/02_WORLDS/CLOUD_HILL/04_EPISODE_PACKAGES/S01E13_WHERE_DOES_RAIN_COME_FROM/` |
| Production report template | `S01E13_PRODUCTION_REPORT.md` |

---

## When to Update This Template

Update only when a real production run reveals a repeating problem that cannot be fixed within the current structure.

Document the problem in the episode's Production Report first. If the same problem appears in two or more episodes, update the template.

Do not update based on theoretical improvements.

---

*Locked: 3 July 2026*
*Reference episode: S01E13*
