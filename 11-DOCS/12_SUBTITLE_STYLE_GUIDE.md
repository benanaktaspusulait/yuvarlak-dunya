# 12 — Subtitle Style Guide

> *Source of truth for: subtitle format, timing, language rules, upload standards.*
> *Every subtitle file in this project must follow this guide.*

---

## Purpose

Subtitles are first-class production assets. They are not an afterthought. Every published episode must include professionally timed EN subtitles. Additional language subtitles are added as the library grows.

This guide ensures that whether 1 episode or 1,000 episodes exist, every subtitle file meets the same quality standard.

---

## Timing Rules

| Rule | Value |
|------|-------|
| Minimum duration | 1 second |
| Maximum duration | 7 seconds |
| Ideal duration | 2–4 seconds |
| Gap between entries | 0.5 seconds minimum |
| Sync point | Subtitle appears when speech begins |
| End point | Subtitle disappears when speech ends |

### Principles

- One natural speech unit per subtitle entry
- Never split a single sentence across two entries
- Never combine two sentences into one entry
- If a character pauses, the subtitle pauses too
- Subtitle duration follows speech rhythm, not arbitrary timing

---

## Text Rules

| Rule | Value |
|------|-------|
| Maximum lines per entry | 2 |
| Maximum characters per line | 42 |
| Maximum words per entry | 8 (for preschool content) |
| Language level | 3–4 year old comprehension |

### Text Principles

- Write how the character speaks, not how text reads
- Match punctuation to natural speech pauses
- Use exclamation marks when the character's voice rises
- Use periods when the character's voice falls
- Never use ALL CAPS (except for emphasis in specific cases)
- Never use italics or special formatting in SRT

---

## English Standard

### Dialogue

```srt
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

### Rules

- Sentence case (not ALL CAPS)
- Contractions allowed: "I'm", "Let's", "What's"
- Simple vocabulary only
- Match the character's speech exactly

---

## Turkish Standard

### Dialogue

```srt
1
00:00:01,000 --> 00:00:04,000
Merhaba!

2
00:00:04,500 --> 00:00:07,000
Ben Kiko.

3
00:00:07,500 --> 00:00:10,000
Bakmayı seviyorum.

4
00:00:10,500 --> 00:00:14,000
Birlikte bakalım!
```

### Rules

- Turkish punctuation rules apply
- İ/ı distinction must be correct
- Compound words should not be split across lines
- Match the English timing exactly

---

## Spanish Standard

### Dialogue

```srt
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
¡Miramos juntos!
```

### Rules

- Inverted punctuation (¡¿) required
- Accent marks must be correct
- Match the English timing exactly

---

## SRT Format Rules

### Structure

```srt
[index]
[timestamp start] --> [timestamp end]
[subtitle text]

[blank line]
```

### Timestamp Format

```
HH:MM:SS,mmm --> HH:MM:SS,mmm
```

- Separator between time units: colon (`:`)
- Separator between seconds and milliseconds: comma (`,`)
- Arrow: ` --> ` (space-arrow-space)

### Encoding

- UTF-8 without BOM
- LF line endings (not CRLF)
- File must end with a newline after the last entry

---

## VTT Format Rules

### Structure

```vtt
WEBVTT

[index]
[timestamp start] --> [timestamp end]
[subtitle text]

[blank line]
```

### Timestamp Format

```
HH:MM:SS.mmm --> HH:MM:SS.mmm
```

- Separator between time units: colon (`:`)
- Separator between seconds and milliseconds: dot (`.`)
- Arrow: ` --> ` (space-arrow-space)

### Encoding

- UTF-8 without BOM
- LF line endings (not CRLF)
- File must start with `WEBVTT` header
- File must end with a newline after the last entry

---

## File Naming

### Episodes

```
s01eXX-LANG.ext
```

Examples:
- `s01e01-EN.srt`
- `s01e01-TR.vtt`
- `s01e01-ES.srt`

### Intros

```
[character]-intro-LANG.ext
```

Examples:
- `kiko-intro-EN.srt`
- `opa-intro-TR.vtt`
- `mimi-intro-ES.srt`

---

## File Organization

```
14-SUBTITLES/
├── s01e01/
│   ├── srt/    (EN.srt, TR.srt, ES.srt)
│   └── vtt/    (EN.vtt, TR.vtt, ES.vtt)
├── s01e02/
│   ├── srt/
│   └── vtt/
├── s01e26/
│   ├── srt/
│   └── vtt/
└── intros/
    ├── kiko/
    │   ├── srt/ (3 files)
    │   └── vtt/ (3 files)
    ├── mimi/
    ├── opa/
    ├── arda/
    ├── noah/
    └── luca/
```

---

## Quality Checklist

Before any subtitle file is published, verify:

- [ ] Timing matches speech exactly
- [ ] No overlapping entries
- [ ] Maximum 2 lines per entry
- [ ] Maximum 42 characters per line
- [ ] Proper punctuation for the language
- [ ] UTF-8 encoding
- [ ] Correct file extension (.srt or .vtt)
- [ ] File ends with newline
- [ ] No placeholder text remaining
- [ ] Language-specific rules followed

---

## YouTube Upload Rules

- Upload via YouTube Studio > Subtitles > Add Language
- SRT and VTT are both accepted; VTT preferred
- One language per upload
- Verify timing matches video after upload
- Preview all subtitles before publishing

---

## Language Progression

| Language | Priority | Status |
|----------|----------|--------|
| English (EN) | 1 — Required | ✅ Template ready |
| Turkish (TR) | 2 — High | ✅ Template ready |
| Spanish (ES) | 3 — Medium | ✅ Template ready |
| Arabic (AR) | 4 — Future | Planned |
| Portuguese (PT) | 5 — Future | Planned |
| French (FR) | 6 — Future | Planned |

---

*This document is the master reference for all subtitle standards.*
*Source of truth for: format, timing, language rules, upload standards.*
*Last updated: 2 Temmuz 2026*
