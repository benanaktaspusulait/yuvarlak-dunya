# 07 — Production Pipeline

---

## Pipeline Overview

```
Idea → Story → Shot Planning → Prompt Writing → OpenArt → Continuity → Rendering → Editing → Audio → Thumbnail → Metadata → Publishing → QC
```

---

## 1. Idea

Every episode starts with a single emotional idea.

Simple enough for a 3-year-old. Relatable to everyday life. Warm and comforting.

---

## 2. Story

Brief summary: beginning → discovery → interaction → ending.

One emotional idea. Maximum 2–3 characters. One world. No conflict.

---

## 3. Shot Planning

4 shots × 15 seconds = 60 seconds.

| Shot | Purpose |
|------|---------|
| 01 | Establishing — world and characters |
| 02 | Development — emotional moment builds |
| 03 | Climax — key emotional beat |
| 04 | Resolution — gentle ending |

---

## 4. Prompt Writing

### Visual Prompt Structure

```
Continue directly from @image1.
The first frame must match @image1 exactly.
Treat @image1 as frame zero.
Do not reinterpret @image1.
Do not reposition the camera.
Continue the action naturally from @image1.
[Scene description]
[Lighting lock]
[Character presence]
[Text safety]
```

### Rules

- Environment LOCKED
- Character LOCKED
- Lighting LOCKED
- Camera distance preserved
- No close-ups unless necessary

---

## 5. OpenArt Workflow

1. Load World Reference
2. Load Character Reference
3. Load Continuity Frame
4. Write Visual Prompt
5. Generate Shot
6. Apply Reject Rules
7. Accept or Regenerate

---

## 6. Continuity Workflow

1. Render shot
2. Review all frames
3. Select best continuity frame
4. Use as reference for next shot
5. Verify continuity

---

## 7. Rendering

### Pre-Render Checklist

- [ ] Reference image correct
- [ ] Frame Lock included
- [ ] Camera Lock included
- [ ] Lighting Lock included
- [ ] Character presence verified
- [ ] Text safety confirmed

### Settings

| Setting | Value |
|---------|-------|
| Resolution | 1920×1080 |
| FPS | 24 |
| Duration | 15 seconds/shot |

---

## 8. Editing

1. Import shots in order
2. Verify continuity
3. Add transitions (soft crossfade)
4. Adjust timing

---

## 9. Audio

1. Mute original shot music
2. Add continuous music track
3. Add ambient sounds
4. Add dialogue
5. Add SFX
6. Fade in/out

---

## 10. Music

- Soft, acoustic, low-stimulation
- One continuous track per episode
- Episode-level, not shot-level

---

## 11. Thumbnail

- 1280×720 px
- One happy face
- Clear action
- Warm colours

---

## 12. Metadata

- Title: Character + Action + Object + Emoji + "PomPom Hills"
- Description: Summary + learning + characters + CTA
- Tags: 15–20 relevant terms

---

## 13. Publishing

- Made for Kids
- Comments off
- Subtitles (TR + EN)
- Playlist added

---

## 14. Quality Control

| Check | Item |
|-------|------|
| Character consistency | ✓ |
| World consistency | ✓ |
| Lighting continuity | ✓ |
| Camera continuity | ✓ |
| Emotional arc | ✓ |
| Age appropriateness | ✓ |

---

## 15. Lessons Learned

- Continuity frame is not always the last frame
- Close-ups can cause environment regeneration
- Character presence must be explicit
- Lighting must be locked, not suggested
- Music is episode-level, not shot-level

---

## 16. Common Mistakes

- Using "close-up" in prompts
- Not locking lighting
- Using final frame automatically
- Adding shot-level music
- Not including character presence notes

---

## 17. Best Practices

- Always use Frame Lock
- Always match lighting from reference
- Always include negative prompts
- Always verify before rendering
- Always reuse existing assets

---

*This document defines the complete production workflow.*
*Source of truth for: How content is created*
