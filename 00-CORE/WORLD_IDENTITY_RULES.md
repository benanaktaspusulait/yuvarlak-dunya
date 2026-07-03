# World Identity Rules

---

## Purpose

Define how canonical worlds should remain visually recognizable across different videos while allowing natural AI variation.

The goal is NOT pixel-perfect reproduction.

The goal is consistent world identity.

---

## World Identity Rule

A canonical world does not need to regenerate identically in every video.

Minor AI variation is acceptable.

The viewer should immediately recognize the location as the same canonical world.

Preserve identity, not exact pixels.

---

## Locked Elements

The following elements define the identity of a world and should remain consistent unless explicitly changed by the story.

### Architecture

- building shape
- roof shape
- door shape
- window style
- room layout
- overall proportions

### Colour Identity

- colour palette
- lighting mood
- colour temperature
- white balance
- saturation
- exposure
- contrast
- brightness
- pastel palette
- matte handcrafted finish

### Environment Identity

- major furniture
- reading corner
- toy corner
- dining table
- large windows
- trees
- paths
- fences
- signature decorations

### Atmosphere

- preschool style
- handcrafted look
- rounded shapes
- soft materials
- calm emotional feeling

---

## Allowed Variations

The following may change naturally between generations.

- small prop positions
- book arrangement
- toy placement
- pillow orientation
- flower direction
- small decorative objects
- camera framing
- character position
- facial expression

These variations should never change the identity of the location.

---

## Not Allowed

Do not redesign the world.

Do not change:

- architecture
- room layout
- colour palette
- white balance
- exposure
- colour temperature
- saturation
- contrast
- brightness
- furniture style
- atmosphere
- lighting identity
- overall proportions

Do not create another interpretation of the same location.

Do not introduce cool shift, warm shift, green tint, magenta tint, orange grading, HDR look or cinematic LUT unless explicitly required by the story.

Reference: `SHOT_PRODUCTION_STANDARD.md`

---

## World Recognition Test

Every generated scene should pass this question:

```
If an audience watches this scene several weeks later,
would they immediately recognize this as the same place?
```

If the answer is no, the generation fails the World Identity Rule.

---

## Production Principle

Canonical consistency means preserving identity, not reproducing identical pixels.

A successful world should feel like revisiting the same location, even if minor AI-generated details naturally vary.

---

## QA Checklist

- [ ] Architecture preserved.
- [ ] Colour identity preserved.
- [ ] White balance, exposure, saturation and contrast preserved.
- [ ] Lighting identity preserved.
- [ ] Environment identity preserved.
- [ ] Atmosphere preserved.
- [ ] Minor variations remain acceptable.
- [ ] The location is immediately recognizable.
