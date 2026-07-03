# Pompom Hills — Shot Production Standard

---

## Purpose

This document defines the production continuity standard for every Pompom Hills shot.

The goal is not to redesign stories, templates, camera language or worlds.

The goal is production consistency.

Every episode should feel like one continuous animated film, not a collection of separately generated shots.

---

## Core Rule

The audience should never notice where one shot ends and the next begins.

Every continuation shot must preserve:

- camera
- colour
- lighting
- voice
- environment
- character proportions
- atmosphere
- character performance

Nothing should reset between shots.

---

## First Frame Lock

For every continuation shot, the first visible frame must be visually indistinguishable from `@image1`.

Not similar.
Not close.
Identical.

Only after the first frame matches perfectly may animation begin.

Required wording:

```text
Treat @image1 as the complete visual master reference.
Preserve not only framing, but also colour identity, lighting identity, exposure, white balance, atmosphere, environment identity, character proportions, and character performance.
The viewer must not perceive a shot boundary.

The first visible frame must be visually indistinguishable from @image1.
Not similar. Not close. Identical.

Only after the first frame matches perfectly may animation begin.
```

---

## Voice Continuity

The speaking voice must remain identical throughout the entire episode.

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

### Voice Reference

When the production system provides a previous shot, the previous shot is also the voice reference.

Maintain exactly the same voice.

If the production tool supports Voice Reference or Voice ID, use the same Voice ID for the same character in every shot.

If Voice ID is not available, reuse the approved character voice reference and flag any voice drift in QA.

---

## Colour Continuity

Every continuation shot must match the previous shot exactly.

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

The audience should feel that every shot belongs to one continuous film.

---

## Lighting Continuity

The first frame of every continuation shot must preserve:

- light direction
- light intensity
- shadow softness
- ambient lighting
- highlight behaviour
- cloud brightness
- grass brightness

Do not reinterpret the lighting.

Continue it.

Lighting identity and colour identity are separate locks.

---

## Episode Continuity

Every shot must feel as though it belongs to the same uninterrupted camera recording.

The full episode must preserve:

- same camera logic
- same colour grade
- same lighting state
- same voice identity
- same world identity
- same character identity
- same character proportions
- same atmosphere

---

## QA Priority Order

Every new episode should be checked in this order:

1. Voice continuity
2. Colour continuity
3. Lighting continuity
4. Character continuity
5. World continuity
6. Story and tempo

If voice, colour or lighting continuity fails, the episode will feel fragmented even if the story works.

---

## QA Blocks

### Voice QA

- [ ] Same voice identity.
- [ ] Same pitch.
- [ ] Same timbre.
- [ ] Same speaking speed.
- [ ] Same emotional tone.
- [ ] Same pronunciation.
- [ ] Same accent.
- [ ] Same recording quality.
- [ ] No alternate narrator.
- [ ] No older or younger voice interpretation.

### Colour QA

- [ ] Same white balance.
- [ ] Same exposure.
- [ ] Same colour temperature.
- [ ] Same saturation.
- [ ] Same contrast.
- [ ] Same brightness.
- [ ] Same pastel palette.
- [ ] No cool shift.
- [ ] No warm shift.
- [ ] No green tint.
- [ ] No magenta tint.
- [ ] No orange grading.
- [ ] No HDR look.
- [ ] No cinematic LUT.

### Lighting QA

- [ ] Same light direction.
- [ ] Same light intensity.
- [ ] Same shadow softness.
- [ ] Same ambient lighting.
- [ ] Same highlight behaviour.
- [ ] Same cloud brightness.
- [ ] Same grass brightness.

If any item in Voice QA, Colour QA or Lighting QA fails, reject the shot.

---

## Goal

The entire episode must feel like one continuous animated film.

The viewer should never perceive a shot boundary.

---

*This document is the canonical shot-level continuity standard for Pompom Hills.*
*Last updated: 3 July 2026*
