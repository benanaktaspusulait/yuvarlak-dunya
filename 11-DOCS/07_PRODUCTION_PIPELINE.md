# 07 — Production Pipeline

---

## Pipeline Overview

```
Idea → Story → Shot Planning → Prompt Writing → OpenArt → Continuity → Rendering → Editing → Audio → Thumbnail → Metadata → Publishing → QC
```

---

## Permanent Identity Locks

Every episode must preserve the identity of the character, world, voice and colour grade across all shots.

Current production priority:

1. Voice Identity
2. Colour Identity
3. Lighting Identity
4. Character Identity
5. World Identity
6. Story and tempo

The goal is not pixel-perfect reproduction. The goal is that the episode feels like one continuous production.

Reference: `00-CORE/SHOT_PRODUCTION_STANDARD.md`

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

6 shots × 15 seconds = 90 seconds.

| Shot | Purpose |
|------|---------|
| 01 | Establishing — world and characters |
| 02 | Development — emotional moment builds |
| 03 | Thinking — quiet observation |
| 04 | Waiting — silence and environment carry the moment |
| 05 | Discovery — key emotional beat |
| 06 | Resolution — gentle ending |

---

## 4. Prompt Writing

### Visual Prompt Structure

```
Continue directly from @image1.
Treat @image1 as frame zero.
Treat @image1 as the complete visual master reference.
The first visible frame must be visually indistinguishable from @image1.
Not similar. Not close. Identical.
Only after the first frame matches perfectly may animation begin.
Do not reinterpret @image1.
Do not reposition the camera.
Preserve colour identity, lighting identity, exposure, white balance, atmosphere, environment identity, character proportions and character performance.
The viewer must not perceive a shot boundary.
Continue the action naturally from @image1.
[Scene description]
[Lighting identity]
[Colour continuity]
[Voice continuity]
[Character presence]
[Text safety]
```

### Rules

- Environment LOCKED
- Character LOCKED
- Lighting LOCKED
- Colour identity LOCKED
- Voice identity LOCKED
- Camera distance preserved
- No close-ups unless necessary

### Voice Continuity

Every Shot Specification with dialogue must include:

```text
## Voice Continuity

For Shot 01, match the approved character Voice ID or voice reference.

For Shot 02+, match the previous speaking shot.

When the production system provides a previous shot, the previous shot is also the voice reference.

The speaking voice MUST remain identical throughout the entire episode.

Maintain:

- same voice identity
- same timbre
- same pitch
- same speaking speed
- same warmth
- same preschool energy
- same pronunciation
- same accent
- same age impression
- same emotional tone
- same recording quality

Never generate a different interpretation of the character voice.
Never replace the voice with a narrator.
Never make the character sound older or younger.

If multiple shots belong to the same episode, their voices must sound as if they were recorded during the same recording session.
```

If the production tool supports Voice Reference or Voice ID, use the same Voice ID for the same character in every shot. If no Voice ID is available, use the closest available character voice reference and treat voice drift as a model limitation to flag in QA.

### Lighting Identity

Lighting identity and colour identity are separate locks.

```text
Preserve:

- light direction
- light intensity
- shadow softness
- ambient lighting
- highlight behaviour
- cloud brightness
- grass brightness

Do not reinterpret the lighting.
Continue it.
```

### Colour Identity

Every shot must match the colour grading of the previous shot.

```text
Maintain:

- identical white balance
- identical exposure
- identical colour temperature
- identical saturation
- identical contrast
- identical brightness
- identical pastel palette

Never introduce:

- cool shift
- warm shift
- green tint
- magenta tint
- orange grading
- HDR look
- cinematic LUT

The entire episode must appear colour graded as one continuous film.
```

Default colour identity:

```text
Warm white balance
Pastel palette
Soft saturation
Low contrast
Matte handcrafted finish
No cool shift
No warm shift
No green tint
No magenta tint
No orange grading
No HDR look
No cinematic LUT
```

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
- [ ] First visible frame must be visually indistinguishable from @image1
- [ ] Camera Lock included
- [ ] Lighting Lock included
- [ ] Colour Identity Lock included
- [ ] Voice Continuity included for speaking shots
- [ ] Previous shot audio or Voice ID selected as voice reference for speaking shots
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
4. Add dialogue using the locked character Voice ID or voice reference
5. Add SFX
6. Fade in/out

### Voice Identity Rule

The same character must sound like the same character across all shots.

Maintain:

- same voice identity
- same age impression
- same personality
- same warmth
- same speaking rhythm
- same pitch
- same timbre
- same pronunciation
- same accent
- same recording quality

Do not allow a shot to introduce a different narrator, alternate performer, older/younger version, or different emotional delivery unless the story explicitly requires it.

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

## 13. Subtitle Workflow

Subtitle creation and upload rules are defined in `SUBTITLE_WORKFLOW.md`.

---

## 14. Publishing

- Made for Kids
- Comments off
- Subtitles uploaded (EN + TR + ES)
- Playlist added

---

## 14. Quality Control

| Check | Item |
|-------|------|
| Character consistency | ✓ |
| World consistency | ✓ |
| Voice identity | ✓ |
| Colour identity | ✓ |
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
- Colour identity must be locked separately from lighting
- Voice identity must be locked across speaking shots
- Previous shot audio must be treated as voice reference
- @image1 must be treated as the complete visual master reference
- The first visible frame must be visually indistinguishable from @image1, not merely similar
- Music is episode-level, not shot-level

---

## 16. Common Mistakes

- Using "close-up" in prompts
- Not locking lighting
- Treating colour as part of lighting only
- Regenerating a new voice for each shot
- Accepting similar-but-not-identical first frames
- Using final frame automatically
- Adding shot-level music
- Not including character presence notes

---

## 17. Best Practices

- Always use Frame Lock
- Always treat @image1 as the complete visual master reference
- Always match lighting from the previous shot without reinterpretation
- Always match colour grading from the previous shot exactly
- Always reuse the locked character Voice ID or voice reference
- Always use the previous shot as voice reference when available
- Always include negative prompts
- Always verify before rendering
- Always reuse existing assets

---

*This document defines the complete production workflow.*
*Source of truth for: How content is created*
