# Micro-Opening and Closing Standard

> This is a global standards document only. It defines the two opening/closing systems used
> across Pompom Hills productions and how they differ. It does NOT move any existing files,
> does NOT rewrite the Opa's Storytime bumper files, does NOT create new episode files, and
> does NOT create image prompts for every world. Those are separate, later production steps.
>
> This document builds on top of `00-CORE/18_VIDEO_STYLE_AND_RETENTION_STANDARD.md` §9c
> (Micro-Opening / Warm Closing System) and does not contradict it. §9c remains the source
> of truth for the underlying length/priority rules; this document organizes those rules into
> two clearly separated systems and defines file/folder conventions for each.
>
> Reference model used: the existing Opa's Storytime series bumper files
> (`POMPOM_HILLS_PRODUCTION/03_EPISODES/OPAS_STORYTIME_SERIES/OPENING_BUMPER/opening-bumper.md`,
> `.../CLOSING_BUMPER/closing-bumper.md`) and the existing Stone Hill Adventures world
> micro-opening (`POMPOM_HILLS_PRODUCTION/02_WORLDS/STONE_HILL/03_OPENINGS/STONE_HILL_ADVENTURES_MICRO_OPENING/opening-stone-hill-adventures.md`).

---

## 1. Purpose

Pompom Hills uses very short opening and closing elements to support series identity, world
recognition, and YouTube end-screen usability — without delaying the story. These elements are
never a replacement for the in-story hook (`00-CORE/18_VIDEO_STYLE_AND_RETENTION_STANDARD.md` §4)
and never a lecture-style ending (§9). They are small, reusable, or semi-reusable production
pieces added on top of the story, not carved out of it.

This document exists because Pompom Hills has two different kinds of opening/closing needs that
must not be confused with each other:

- A **named recurring series** (like Opa's Storytime) needs a fully reusable, place-neutral
  opening and closing that repeats identically across every episode of that series.
- A **world-based episode family** (like Stone Hill Adventures) needs a reusable opening that
  shows that specific world's identity, but does not need a reusable closing at all.

Mixing these two up leads to either over-branding world episodes with a generic bumper, or
under-branding a named series by treating its opening as just another world micro-opening.

---

## 2. Two Types

### A. Series Bumper

Used for recurring named formats such as:

- Opa's Storytime

Rules:

- reusable opening allowed
- reusable closing allowed
- can be place-neutral if the series happens in multiple worlds
- 3–4 seconds opening
- 4–5 seconds closing
- no loud logo
- no aggressive CTA
- no readable text generated inside AI video by default
- story body duration is not reduced; bumper is added on top

**Example:** Opa's Storytime uses a shared rounded storybook opening and closing. The same book
motif appears in both, is place-neutral (no specific world shown), and is added before/after the
episode's own story beats without shortening them. See
`POMPOM_HILLS_PRODUCTION/03_EPISODES/OPAS_STORYTIME_SERIES/OPENING_BUMPER/opening-bumper.md` and
`.../CLOSING_BUMPER/closing-bumper.md` for the production-ready version of this pattern.

### B. World Micro-Opening

Used for world-based episode families such as:

- Stone Hill Adventures
- Cloud Hill Moments
- Flower Hill Friends
- Central Square Friends

Rules:

- reusable opening allowed
- usually 3–4 seconds
- must show the world identity
- must show the world landmark or visual hook
- no characters by default
- no readable text generated inside AI video
- no logo animation
- no title card generated inside AI video
- final frame should visually connect into Shot 01
- used only for 90–120 second episodes
- not used for Shorts
- avoid using it for 60 second videos unless it is only 1–2 seconds

World micro-openings do not have a matching reusable closing (see §3). See
`POMPOM_HILLS_PRODUCTION/02_WORLDS/STONE_HILL/03_OPENINGS/STONE_HILL_ADVENTURES_MICRO_OPENING/opening-stone-hill-adventures.md`
for the production-ready version of this pattern.

---

## 2C. Music Motif Rule for World Micro-Openings

World micro-openings may include a very short, soft music motif. The sound should support
world recognition without feeling like a loud logo or a long intro sting. This is a **mood
cue**, not a jingle — it should make the world feel present, not announce a brand.

Music must be:

- 3–4 seconds
- soft
- warm
- preschool-friendly
- non-vocal
- low volume
- simple and repeatable

Avoid:

- loud jingles
- fast logo stings
- whooshes
- drums
- lyrics
- spoken branding
- sudden sound effects
- aggressive subscribe-style audio

This follows the general music/volume rules in `00-CORE/AUDIO_GUIDE.md` § Ses Seviyesi Kuralları
(müzik -12 dB, ambiyans -18 dB) and § Yasak Enstrümanlar (no electric guitar, hard drums, hard
synth, orchestra, deep bass, hard horn) — a world micro-opening motif is not exempt from those
limits just because it is short.

### Per-World Sound Identity (Suggested)

Each world may have its own short sound motif, matching its own visual identity. These are
starting points, not locked audio assets — treat them as production notes until an actual
music motif is recorded and approved.

| World | Suggested Motif |
|---|---|
| Stone Hill | Soft marimba / rounded wooden tones, one tiny pebble-like chime, very light ambient wind |
| Flower Hill | Light bells / glockenspiel, soft flower breeze, calm and cheerful but childlike |
| Cloud Hill | Airy pad, soft chime, a light breath-like wind sound |
| Central Square | Warm, light, friendship-feeling short motif; very light percussion allowed but never noisy |
| Opa's Storytime (series bumper, not a world) | Single soft chime + warm ambient as the book opens — already defined in `POMPOM_HILLS_PRODUCTION/03_EPISODES/OPAS_STORYTIME_SERIES/OPENING_BUMPER/opening-bumper.md` § Sound; unchanged by this rule |

### Stone Hill — Ready-to-Use Sound Note

```text
Sound: A soft warm 3–4 second music motif with gentle marimba or rounded wooden tones, very
light ambient wind, and one tiny pebble-like chime. Calm, tactile, safe and curious. No loud
logo sting, no vocals, no fast whoosh.
```

This is already applied in
`POMPOM_HILLS_PRODUCTION/02_WORLDS/STONE_HILL/03_OPENINGS/STONE_HILL_ADVENTURES_MICRO_OPENING/`
(see `opening-stone-hill-adventures.md` § Sound and `render-prompts.md` § Sound).

---

## 3. Closing Rule for Normal World Episodes

Normal world-based episodes do **NOT** need a reusable closing bumper by default.

Instead, the final story shot should act as the closing:

- emotional resolution
- 2–3 second quiet warm hold
- clean peaceful final frame
- end-screen friendly space if naturally available
- no lesson card by default
- no aggressive CTA
- no generated readable text

This matches the general Warm Closing rule in
`00-CORE/18_VIDEO_STYLE_AND_RETENTION_STANDARD.md` §9c — a world micro-opening does not create
an obligation for a matching reusable closing. Only named series (§2A) get a reusable closing.

**Music in the final shot:** No separate closing music cue is needed. Instead, the last 2–3
seconds of the final story shot may carry a very soft, warm ending tone under the ambient sound
(e.g. ambient wind, distant birds, and one very soft warm ending tone — see
`00-CORE/AUDIO_GUIDE.md` § Ses Seviyesi Kuralları for volume limits). This is already the
pattern used in
`POMPOM_HILLS_PRODUCTION/02_WORLDS/STONE_HILL/04_EPISODE_PACKAGES/S01E07_THE_ROUND_STONE/01_SHOTS/shot-06-together.md`
§ Sound ("Quiet ambient wind, Distant birds, Soft, warm ending tone") — that file is left
untouched, it already matches this rule.

---

## 4. When to Use

Opening/closing use by content type:

| Content type | Opening/Closing |
|---|---|
| Shorts | no bumper |
| 60 second story | usually no bumper |
| 90 second story | optional 3–4 second world micro-opening |
| 120 second story | recommended 3–4 second world micro-opening |
| Opa's Storytime | shared series opening and closing required |
| Character intro videos | no reusable world bumper unless the intro belongs to a named series |

---

## 5. World Examples

Concise templates for world micro-openings. Stone Hill, Flower Hill and Cloud Hill now have
full production packages (spec + render prompts) built from these templates — see the file
links below. Central Square does not have a package yet; its template remains description-only
until a package is built for it.

### Stone Hill Adventures — Micro-Opening

- **Visual:** smooth rounded toy-like stones, pebble path, warm moss patches, small grass tufts,
  gentle slope, warm morning daylight.
- **Motion:** gentle camera glide or soft push-in.
- **Avoid:** sharp rocks, cliffs, quarry, dark cave, extra characters, readable text.
- **Production package (built):**
  `POMPOM_HILLS_PRODUCTION/02_WORLDS/STONE_HILL/03_OPENINGS/STONE_HILL_ADVENTURES_MICRO_OPENING/`
  (`opening-stone-hill-adventures.md`, `render-prompts.md`).

### Flower Hill Friends — Micro-Opening

- **Visual:** Flower Hill Home Cluster Zone, flower-covered hill, pink main dome home, two
  smaller pastel dome homes, central stone path, flower fences, pots, warm home charm.
- **Avoid:** readable sign, top-down map view, large bridge, dominant river, ducks, fish,
  rainbow unless later canonised.
- **Production package (built, DRAFT):**
  `POMPOM_HILLS_PRODUCTION/02_WORLDS/FLOWER_HILL/03_OPENINGS/FLOWER_HILL_FRIENDS_MICRO_OPENING/`
  (`opening-flower-hill-friends.md`, `render-prompts.md`). Marked draft — pending Flower Hill's
  own Canon Hero View approval (see `25-flower-hill-bible.md` § Generation Workflow).

### Cloud Hill Moments — Micro-Opening

- **Visual:** smooth dome hill, summit viewing stone, close soft clouds, cloud shadows, tiny
  grass tufts, warm open sky.
- **Avoid:** generic empty hill, houses, cliffs, storm clouds, too many flowers.
- **Production package (built):**
  `POMPOM_HILLS_PRODUCTION/02_WORLDS/CLOUD_HILL/03_OPENINGS/CLOUD_HILL_MOMENTS_MICRO_OPENING/`
  (`opening-cloud-hill-moments.md`, `render-prompts.md`).

### Central Square Friends — Micro-Opening

- **Visual:** Big Pompom Tree, rounded paths, open friendly meeting space, soft benches or
  flowerbeds if canonised.
- **Avoid:** city plaza, roads, cars, shops, cluttered market, modern playground unless
  canonised.
- **Production package:** not yet built.

---

## 6. Text Safety

Do not generate readable text inside AI video.

If a title is needed, add it later in editing, not inside the AI generation. This is consistent
with `00-CORE/17_VIDEO_GENERATION_STANDARD.md` § Text Safety and applies to both series bumpers
and world micro-openings without exception.

---

## 7. File Organization

**For series bumpers:**

```text
POMPOM_HILLS_PRODUCTION/03_EPISODES/{SERIES_NAME}/OPENING_BUMPER/
POMPOM_HILLS_PRODUCTION/03_EPISODES/{SERIES_NAME}/CLOSING_BUMPER/
```

**For world micro-openings:**

```text
POMPOM_HILLS_PRODUCTION/02_WORLDS/{WORLD_NAME}/03_OPENINGS/{WORLD_NAME}_MICRO_OPENING/
```

**For normal episode closings:**

No separate bumper folder by default; use the final shot inside the episode package.

These conventions already match the existing Opa's Storytime series folders and the existing
Stone Hill Adventures world opening folder — this document does not require moving or renaming
anything already in place.

---

## 8. Final Rule

- Series bumpers can have opening and closing.
- Worlds usually get only micro-openings.
- Normal episode endings stay episode-specific.

---

*This document is the single source of truth for the distinction between series bumpers and
world micro-openings, and for where their files belong.*
*It does not duplicate or override `00-CORE/18_VIDEO_STYLE_AND_RETENTION_STANDARD.md` §9c
(length/priority rules) or `00-CORE/31_OPA_INTERACTIVE_STORYTELLING_FORMAT.md` §4/§4a
(Opa's Storytime specifics) — it organizes and cross-references them.*
*Version: 1.0 — 4 Temmuz 2026*
