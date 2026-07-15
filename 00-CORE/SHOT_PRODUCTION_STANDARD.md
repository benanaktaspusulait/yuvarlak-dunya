# Pompom Hills — Shot Production Standard

---

## Purpose

This document defines the production continuity standard for every Pompom Hills shot.

The goal is not to redesign stories, templates, camera language or worlds.

The goal is production consistency.

Every episode should feel like one continuous animated film, not a collection of separately generated shots.

---

## Core Rule

The audience should experience clear story continuity, but a clean editorial cut between
independently generated high-quality shots is acceptable and preferred over visual degradation.

Every continuation shot must preserve:

- camera
- colour
- lighting
- voice
- environment
- character proportions
- atmosphere
- character performance

Fresh quality-reset shots intentionally restore canonical image quality while preserving
story logic, screen direction, identity, approximate placement, colour and lighting.

## Shot Completion and Reset Contract

Before generation, every shot must declare:

- Production Mode
- Clean Start State
- Complete Main Action
- Completed End State
- Stable Final Anchor
- Next-Shot Dependency

Every major physical action and camera move begins and finishes inside the shot. The final
1–2 seconds are stable, grounded and natural. Exact final-frame chaining is limited to two
linked shots normally and three exceptionally; the next shot then resets from canonical
World and character references.

---

## Global OpenArt Continuity Gate

Every shot must also pass the Global OpenArt Continuity Locks in
`00-CORE/17_VIDEO_GENERATION_STANDARD.md` and the Global OpenArt Continuity Gate in
`11-DOCS/16_VIDEO_QA_SPEC.md`.

This means every shot is checked for:

- Hard Background Lock
- Intra-Shot Character Continuity Lock
- Single Visible Path Rule
- Occlusion Is Not A Transition
- Camera Must Not Break Continuity
- First Second Continuity Hold
- Object Identity Lock

Any disappearance, teleport, same-shot regeneration, full-body occlusion, unreadable
character path, camera-created continuity break, background object movement, background
layout morphing, or object identity change is a rejection issue.

---

## First Frame Lock

For every shot, the first visible frame must follow its pre-planned Production Mode. Fresh
shots use a clean canonical shot-specific `@image1`. Only linked shots must match a
QA-approved previous generated final frame exactly.

Not similar.
Not close.
Identical.

Only after the first frame matches perfectly may animation begin.

Required wording:

```text
Treat @image1 as the complete visual master reference.
Preserve not only framing, but also colour identity, lighting identity, exposure, white balance, atmosphere, environment identity, character proportions, and character performance.
For an explicitly linked shot, the viewer must not perceive a shot boundary. Fresh quality-reset
shots may use a clean editorial cut.

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

Every shot must match the approved Episode Colour Master. Linked shots additionally preserve
the prior frame's placement and exposure unless that frame shows degradation.

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
4. Intra-shot character continuity
5. Hard background and object identity continuity
6. World continuity
7. Story and tempo

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

### OpenArt Continuity QA

- [ ] Global OpenArt Continuity Locks passed.
- [ ] No character disappears, reappears, teleports or regenerates inside the same shot.
- [ ] No character is fully hidden by foreground or background objects.
- [ ] Every character path remains continuously visible and physically possible.
- [ ] Camera movement does not hide characters or reveal a different location.
- [ ] Background objects do not move, morph, duplicate, disappear or change identity.
- [ ] First and final frames are exported for QA.
- [ ] Full video is watched once for character continuity and once for background/object stability.

If any OpenArt Continuity QA item fails, reject the shot.

---

## Goal

The entire episode must feel like one continuous animated film.

The viewer should experience a cohesive episode. Exact seamlessness is reserved for approved
linked shots; a clean cut between stronger fresh shots is preferred to degraded continuity.

---

*This document is the canonical shot-level continuity standard for Pompom Hills.*
*Last updated: 3 July 2026*
