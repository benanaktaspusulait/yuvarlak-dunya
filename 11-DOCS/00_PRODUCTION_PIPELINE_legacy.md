# Pompom Hills — Production Pipeline

---

## Overview

This document defines the complete production workflow for Pompom Hills episodes.

Every episode follows this pipeline from idea to publication.

---

## Pipeline Overview

```
Idea → Story → Shot Planning → OpenArt → Continuity → Rendering → Editing → Audio → Thumbnail → Metadata → Publishing → QC
```

---

## 1. Idea

Every episode starts with a single emotional idea.

The idea should be:
- Simple enough for a 3-year-old to understand
- Relatable to everyday preschool experiences
- Warm, safe, and comforting

**Example:** "What do stars say?"

---

## 2. Story

The story is written as a brief summary covering:

- Beginning (setup)
- Discovery (the emotional moment)
- Interaction (character response)
- Ending (emotional resolution)

**Rules:**
- One emotional idea per episode
- Maximum 2–3 active characters
- One world per episode
- No conflict, no villains, no danger
- Low stimulation throughout

---

## 3. Shot Planning

Each episode consists of 4 shots, approximately 15 seconds each.

| Shot | Purpose |
|------|---------|
| **Shot 01** | Establishing shot — introduces the world and characters |
| **Shot 02** | Development — builds the emotional moment |
| **Shot 03** | Climax — the key emotional beat |
| **Shot 04** | Resolution — gentle ending, emotional resting point |

**Rules:**
- Shot 01 is always a new Take Shot
- Shots 02–04 continue from the previous shot
- Camera movement must remain inside the existing scene
- No dramatic camera moves

---

## 4. OpenArt

### Reference Images

Before generating any shot, prepare:

| Reference | Purpose |
|-----------|---------|
| World Reference | The established environment |
| Character Reference | The character sheet |
| Continuity Frame | The approved frame from the previous shot |

### Visual Prompt Structure

Every continuation shot must include:

```
Continue directly from @image1.

The first frame of this video must match @image1 exactly.

Treat @image1 as frame zero.

The animation begins only after the first frame has matched @image1 exactly.

Use @image1 as the exact starting composition.

Do not reinterpret @image1.

Do not reposition the camera.

Do not recompose the scene.

Do not adjust framing before movement begins.

Continue the action naturally from @image1.
```

### Production Rules

- Environment is LOCKED — never regenerate or redesign
- Character appearance is LOCKED — never change
- Lighting must match the continuity reference exactly
- Colour grading must match the continuity reference exactly
- Camera distance must be preserved
- Maximum 2–3 characters per shot

---

## 5. Continuity

### Reference Frame Selection

The final frame of a rendered shot is NOT automatically the best reference frame.

Always choose the frame that best supports:
- Character continuity
- Pose continuity
- Eye direction continuity
- Camera continuity
- Composition continuity
- Emotional continuity

### Continuity Checklist

- [ ] Correct continuity frame selected
- [ ] Frame shows correct characters
- [ ] Frame shows enough of the world
- [ ] Lighting matches
- [ ] Camera distance matches
- [ ] Composition is stable

---

## 6. Rendering

### Pre-Render Checklist

Before every render, complete the PRE_RENDER_CHECKLIST.md:

- [ ] Reference image correct
- [ ] Frame Lock included
- [ ] Camera Lock included
- [ ] Lighting Lock included
- [ ] Character presence verified
- [ ] Text safety confirmed
- [ ] Negative prompt complete

### Render Settings

| Setting | Value |
|---------|-------|
| Resolution | 1920x1080 (16:9) |
| FPS | 24 |
| Duration | 15 seconds per shot |

---

## 7. Editing

### Video Editing

1. Import all shot videos
2. Place shots in order (01 → 02 → 03 → 04)
3. Verify continuity between shots
4. Adjust timing if needed
5. Add transitions (soft crossfade, 2-3 seconds)

### Audio Editing

1. Mute original shot music if present
2. Add one continuous music track across the full episode
3. Add ambient sound layer
4. Add dialogue or voiceover
5. Add small SFX only where needed
6. Fade music in at the beginning
7. Fade music out at the end

**Rule:** Music is episode-level, not shot-level.

---

## 8. Audio

### Music

- Soft, acoustic, low-stimulation
- Preferred instruments: piano, ukulele, glockenspiel, marimba
- Avoid: electronic beats, loud drums, harsh synths
- One continuous track across the full episode

### Ambient Sound

- Crickets, soft wind, leaf rustle
- Gentle night ambience
- Birds, soft footsteps
- Support the world without distracting

### Dialogue

- Simple, clear, age-appropriate
- Maximum 15–20 unique words per episode
- Repeated phrases for learning

---

## 9. Thumbnail

### Specifications

| Setting | Value |
|---------|-------|
| Size | 1280 × 720 px |
| Safe area (mobile) | 1168 × 658 px |
| Format | JPG or PNG |

### Design Rules

- One happy face (close-up)
- Clear action
- Representative object
- Warm colours
- Large readable text (max 3 words)
- High contrast

### Prompt Template

```text
Pompom Hills thumbnail, [CHARACTER] [ACTION] in [WORLD],
warm pastel colors, round soft shapes, happy expression,
close-up face, child-friendly, 1280x720
```

---

## 10. Metadata

### Title Formula

```
[Character Name] [Action] [Object]? [Emoji] PomPom Hills
```

### Description Structure

```markdown
## [Episode Title] 🎬

[2-3 sentence summary]

### What do we learn?
• [Learning point 1]
• [Learning point 2]

### Characters
• [Character list]

### Location
• [Location name]

---

🔔 Subscribe and ring the bell!
👍 Like and share!

#PompomHills #Preschool #Toddler #KidsAnimation
```

### Tags

```
pompom hills, preschool, toddler, kids animation, baby cartoon,
3 year old, 4 year old, gentle, safe, educational, soft animation,
pastel colors, rounded shapes, bedtime story, kids show
```

---

## 11. Publishing

### YouTube Settings

| Setting | Value |
|---------|-------|
| Audience | Made for Kids |
| Comments | Off |
| Notifications | Off |
| Personalized ads | Off |

### Publishing Checklist

- [ ] Video 1280x720 (16:9)
- [ ] Audio clear (-6 dB peak)
- [ ] Thumbnail ready (1280x720)
- [ ] Title within 60 characters
- [ ] Description written (with chapters)
- [ ] Tags added (15-20)
- [ ] Hashtags added (5-10)
- [ ] Age restriction correct (Made for Kids)
- [ ] Comments off
- [ ] Subtitles added (TR + EN)
- [ ] Added to playlist

---

## 12. Quality Control

### Per-Episode QC

| Check | Item |
|-------|------|
| Visual | Character consistency |
| Visual | World consistency |
| Visual | Lighting continuity |
| Visual | Camera continuity |
| Visual | Colour consistency |
| Audio | Music continuity |
| Audio | Dialogue clarity |
| Audio | SFX balance |
| Content | Age appropriateness |
| Content | Emotional arc complete |
| Content | No fast cuts, no loud sounds |

### QC Checklist

See: `00-CORE/PRE_RENDER_CHECKLIST.md`

---

## Document Relationships

| Document | Purpose |
|----------|---------|
| `PROJECT_ROADMAP.md` | Long-term vision and growth strategy |
| `SEASON_1_EPISODE_GUIDE.md` | Story guide — what stories exist |
| `WORLD_BIBLE.md` | World definitions and descriptions |
| `CHARACTER_BIBLE.md` | Character definitions and descriptions |
| `PRODUCTION_PIPELINE.md` | This document — how content is created |
| `PRODUCTION_STATUS.md` | Current production snapshot |
| `YOUTUBE_STRATEGY.md` | Publishing strategy |

---

*This document defines the production workflow for Pompom Hills.*
*Last updated: 2 Temmuz 2026*
