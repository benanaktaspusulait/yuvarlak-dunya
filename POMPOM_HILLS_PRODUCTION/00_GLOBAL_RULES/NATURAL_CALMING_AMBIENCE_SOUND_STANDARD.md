# Natural Calming Ambience Sound Standard

> This is a global production standard. It applies to **every Pompom Hills OpenArt video
> prompt**, unless a shot explicitly requires silence for story reasons.
>
> This document does NOT apply to only one episode, does NOT rewrite existing stories, does
> NOT change character canon (`00-CORE/CHARACTER_GUIDE.md`, `01-CHARACTERS/*`), does NOT add
> music, does NOT add songs, and does NOT add magical sound effects.
>
> **Scope note (no conflict with the audio canon):** This standard governs only the
> **OpenArt-facing generation prompt** — the `## Sound` section that OpenArt reads when
> generating a single shot. Episode-level background music is still added later in editing,
> per `00-CORE/EPISODE_AUDIO_WORKFLOW.md` §1 (music is episode-level, not shot-level) and §2
> (OpenArt-generated music is muted/removed in editing). So "no music in the OpenArt prompt"
> and "the finished episode has a continuous music track" are both true — the music simply
> comes from editing, not from OpenArt. Volume levels, instruments and the overall audio
> philosophy remain owned by `00-CORE/AUDIO_GUIDE.md` and `00-CORE/EPISODE_AUDIO_WORKFLOW.md`;
> this document only defines what the OpenArt prompt itself asks for.

---

## 1. Purpose

Pompom Hills should always feel calm, warm, safe, and soothing for preschool children.

Every video should include soft natural ambience when possible.

The sound style should help children feel relaxed, comfortable, and emotionally safe.

The sound must support the world gently without turning the video into a musical, magical,
noisy, or overstimulating scene.

---

## 2. Core Rule

Every OpenArt-facing prompt should include a `## Sound` section.

The sound should be:

- soft
- natural
- gentle
- warm
- low-intensity
- preschool-safe
- calming
- location-appropriate
- non-musical

The sound should never overpower dialogue or character emotion.

---

## 3. Required OpenArt Prompt Section

Every OpenArt-ready prompt should include this section between:

- `## Natural Character Motion Rule`

and

- `## Lighting`

Use the section title:

```markdown
## Sound
```

---

## 4. Default Sound Template

Use this default template when no special sound design is needed:

```markdown
## Sound

Soft natural ambience: gentle birds, light breeze, calm outdoor warmth, very subtle
environmental texture. Natural ambience only. No music, no background music, no melody, no
song, no soundtrack, no chimes, no whooshes.
```

---

## 5. Location-Based Sound Templates

### Central Square

Use for Central Square scenes:

```markdown
## Sound

Soft outdoor Central Square ambience: gentle birds chirping, light breeze, calm warm village
atmosphere, very subtle friendly outdoor presence. Natural ambience only. No music, no
background music, no melody, no song, no soundtrack, no chimes, no whooshes.
```

### Mimi's Burrow

Use for Mimi's Burrow scenes:

```markdown
## Sound

Soft cozy burrow ambience: gentle indoor warmth, quiet outdoor birds in the distance, soft
breeze near the burrow entrance. Natural ambience only. No music, no background music, no
melody, no song, no soundtrack, no chimes, no whooshes.
```

**Important:** Mimi's Burrow must not sound dark, echoey, hollow, cave-like, spooky, or
underground-scary.

### Opa's Tree

Use for Opa's Tree scenes:

```markdown
## Sound

Soft outdoor tree ambience: gentle leaves rustling, light birds, calm breeze around Opa's
Tree, warm peaceful stillness. Natural ambience only. No music, no background music, no
melody, no song, no soundtrack, no magical chimes, no whooshes.
```

### Stone Hill

Use for Stone Hill scenes:

```markdown
## Sound

Soft open-hill ambience: gentle breeze over the hill, distant light birds, calm outdoor air,
warm peaceful quiet. Natural ambience only. No music, no background music, no melody, no
song, no soundtrack, no chimes, no whooshes.
```

### Cloud Hill

Use for Cloud Hill scenes:

```markdown
## Sound

Soft airy hill ambience: gentle high breeze, very light distant birds, calm open sky feeling,
peaceful quiet. Natural ambience only. No music, no background music, no melody, no song, no
soundtrack, no magical chimes, no whooshes.
```

### Flower Hill / Flower Meadow

Use for flower or meadow scenes:

```markdown
## Sound

Soft meadow ambience: gentle breeze through flowers, light birds, very subtle soft outdoor
warmth. Natural ambience only. No music, no background music, no melody, no song, no
soundtrack, no chimes, no whooshes.
```

---

## 6. Dialogue Safety

If a shot includes dialogue:

- ambience must stay soft
- ambience must not compete with voices
- no loud birds
- no loud wind
- no crowd noise
- no sudden sound
- no overlapping musical layer

Use this sentence when dialogue is present:

```markdown
Keep ambience very soft under dialogue.
```

---

## 7. Forbidden Sound Types

Never add:

- music
- background music
- melody
- song
- soundtrack
- musical bed
- theme tune
- jingle
- chime
- bell
- magical sparkle sound
- whoosh
- impact sound
- dramatic sting
- suspense sound
- applause
- cheering
- crowd noise
- loud animal calls
- scary ambience
- echoey cave sound
- hollow tunnel sound
- mechanical noise
- toy sound unless explicitly approved
- block sound unless explicitly approved
- classroom noise unless explicitly approved

---

## 8. Negative Prompt Requirement

Every OpenArt-ready prompt must include these sound negatives inside Negative Prompt:

```text
background music, music, melody, song, soundtrack, musical bed, jingle, chime, bell, magical sparkle sound, whoosh, applause, cheering, crowd noise, loud sound, scary sound
```

Do not remove existing visual negative prompts.

---

## 9. Special Rule: Implied Off-Screen Sounds

If a shot includes an implied off-screen sound, the source must stay invisible unless the shot
explicitly approves it.

For implied sounds, use:

```markdown
## Sound

Soft natural ambience with one very tiny friendly off-screen sound implied quietly. The sound
source is not visible and must not become music, a chime, a bell, an instrument, a magical
sparkle, an animal call, a toy, or a visible object. Natural ambience only. No music, no
background music, no melody, no song, no soundtrack, no chimes, no whooshes.
```

And add to Negative Prompt:

```text
visible sound source, instrument, toy sound, animal call, bell object, chime object
```

---

## 10. Volume / Intensity Rule

Sound must feel like a soft background layer.

Use:

- quiet, gentle, soft, subtle, calm

Avoid:

- loud, exciting, dramatic, energetic, magical, cinematic, intense

This is consistent with the ambience volume limit in `00-CORE/AUDIO_GUIDE.md` § Ses Seviyesi
Kuralları (ambience -18 dB, "çok sessiz") — a natural ambience layer never rises to a
foreground level in the finished mix either.

---

## 11. OpenArt Prompt Structure Update

Every OpenArt-ready file should use this structure:

```markdown
# OpenArt Prompt — Shot XX — [Shot Name]

## Visual Prompt

## Camera Direction

## Dialogue

## Natural Character Motion Rule

## Sound

## Lighting

## Negative Prompt
```

If a shot has no dialogue, keep the Dialogue section empty or write:

```markdown
No dialogue.
```

This structure is compatible with the OpenArt-facing sections listed in
`POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/STANDALONE_SHOT_AND_TRANSITION_STANDARD.md` §3 (the
`## Sound` section is one of the OpenArt-facing sections; production/editing sections are kept
separate from the OpenArt prompt).

---

## 12. Story Exceptions

This rule applies by default to every OpenArt prompt. Two narrow exceptions exist and must be
deliberate, never accidental:

- **Silence for story reasons:** if a shot explicitly needs silence, note it in the `## Sound`
  section (e.g. "Near silence: only the faintest breeze, held very quiet for a still story
  moment.") rather than leaving the section out.
- **Story-driven sound worlds:** a world or episode whose story is explicitly about specific
  sounds (for example the Music Hill "music trees" episode at
  `POMPOM_HILLS_PRODUCTION/02_WORLDS/MUSIC_HILL/04_EPISODE_PACKAGES/S01E24_MUSIC_TREES/`) keeps
  its story-required sounds. This standard does not rewrite those existing stories or their
  `## Sound` sections; it governs the default ambience for all other prompts.

If it is unclear whether a shot qualifies as an exception, default to soft natural ambience.

---

## 13. Final Rule Summary

For all future Pompom Hills OpenArt prompts:

- Always include soft natural ambience.
- Never include music.
- Never include magical sound effects.
- Never include loud or overstimulating sounds.
- Sound should calm the child and support the location.

---

*This document is the single source of truth for the OpenArt-facing `## Sound` section and
natural calming ambience across Pompom Hills video prompts.*
*It does not override `00-CORE/AUDIO_GUIDE.md` or `00-CORE/EPISODE_AUDIO_WORKFLOW.md` (episode
music, mix levels, voice identity) — episode-level music is still added later in editing; this
document only defines what the OpenArt generation prompt itself requests.*
*Version: 1.0 — 5 Temmuz 2026*
