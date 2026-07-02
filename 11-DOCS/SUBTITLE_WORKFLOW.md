# SUBTITLE_WORKFLOW.md

> *The complete subtitle workflow for Pompom Hills.*
> *Source of truth for: subtitle creation, translation, quality control, upload.*

---

## Purpose

Subtitles are first-class production assets.

Every published Pompom Hills video should have properly timed subtitles in:

- English (EN)
- Turkish (TR)
- Spanish (ES)

This includes:

- Character intros
- Full episodes
- Shorts where subtitles are useful
- Compilations

---

## Output Formats

For every video, create:

| Language | SRT | VTT |
|----------|-----|-----|
| English | `[slug]-EN.srt` | `[slug]-EN.vtt` |
| Turkish | `[slug]-TR.srt` | `[slug]-TR.vtt` |
| Spanish | `[slug]-ES.srt` | `[slug]-ES.vtt` |

### File Naming Convention

```
[video-slug]-[LANG].[ext]
```

### Examples

```
kiko-intro-EN.srt
kiko-intro-EN.vtt
kiko-intro-TR.srt
kiko-intro-TR.vtt
kiko-intro-ES.srt
kiko-intro-ES.vtt
```

---

## Subtitle Style Rules

Each subtitle should be a natural speech unit.

Do not split a simple sentence unnecessarily.

Use short, child-friendly language.

Target audience is 3–4 years old.

### Rules

| Rule | Value |
|------|-------|
| Maximum lines per subtitle | 2 |
| Maximum characters per line | 42 |
| Ideal on-screen duration | 2–4 seconds |
| Minimum duration | 1 second |
| Maximum duration | 5 seconds (unless silence) |
| Language level | Preschool (3–4 years) |
| Punctuation | Simple, child-friendly |
| Clauses | Short, no complex structures |
| Idioms | Avoid — they do not translate well |

---

## Language Rules

### English

- Use simple preschool English
- Short sentences
- Warm tone
- No slang
- No idioms

### Turkish

- Use simple natural Turkish
- Avoid overly formal phrasing
- Use child-friendly vocabulary
- Keep emotional warmth
- Avoid literal translations if they sound unnatural

### Spanish

- Use neutral Latin American Spanish unless specified otherwise
- Simple preschool vocabulary
- Warm and gentle tone
- Avoid regional slang
- Avoid complex grammar

---

## Translation Rule

Do not translate word-for-word.

Translate meaning, tone, and emotional intent.

The subtitle should feel natural to a child in that language.

Keep the emotional meaning consistent across EN, TR, and ES.

---

## Timing Rule

All language versions must use the same timing blocks unless a translation becomes too long.

If a translated line is too long:

1. Simplify the wording first
2. Split into two lines if needed
3. Only adjust timing if absolutely necessary

---

## YouTube Workflow

For each video:

1. Create master transcript
2. Create EN subtitle file
3. Create TR subtitle file
4. Create ES subtitle file
5. Export each language as .srt
6. Export each language as .vtt
7. Upload to YouTube Studio
8. Verify subtitles visually in YouTube editor
9. Check mobile readability
10. Save and publish

---

## Quality Control Checklist

Before uploading subtitles:

- [ ] EN .srt exists
- [ ] EN .vtt exists
- [ ] TR .srt exists
- [ ] TR .vtt exists
- [ ] ES .srt exists
- [ ] ES .vtt exists
- [ ] File names follow naming convention
- [ ] Timing matches speech
- [ ] No subtitle is too fast
- [ ] No line is too long
- [ ] No spelling mistakes
- [ ] Translations sound natural
- [ ] Emotional tone is preserved
- [ ] YouTube preview checked

---

## Example — Kiko Intro

### EN

```
1
00:00:01,000 --> 00:00:04,000
Hello!

2
00:00:04,500 --> 00:00:07,000
I'm Kiko.

3
00:00:07,500 --> 00:00:10,000
I like to look.

4
00:00:10,500 --> 00:00:14,000
Let's look together!
```

### TR

```
1
00:00:01,000 --> 00:00:04,000
Merhaba!

2
00:00:04,500 --> 00:00:07,000
Ben Kiko.

3
00:00:07,500 --> 00:00:10,000
Bakmayı severim.

4
00:00:10,500 --> 00:00:14,000
Haydi birlikte bakalım!
```

### ES

```
1
00:00:01,000 --> 00:00:04,000
¡Hola!

2
00:00:04,500 --> 00:00:07,000
Soy Kiko.

3
00:00:07,500 --> 00:00:10,000
Me gusta mirar.

4
00:00:10,500 --> 00:00:14,000
¡Miremos juntos!
```

All three languages share identical timing blocks.

---

## Document Relationships

This document is referenced by:

- `PRODUCTION_PIPELINE.md` — subtitle step in the pipeline
- `YOUTUBE_STRATEGY.md` — subtitle requirement for publishing
- `ASSET_LIBRARY.md` — subtitle file tracking

Do not duplicate subtitle rules in those files. Only add short cross-references.

---

*This document defines the complete subtitle workflow for Pompom Hills.*
*Source of truth for: subtitle creation, translation, quality control, upload.*
*Last updated: 2 Temmuz 2026*
