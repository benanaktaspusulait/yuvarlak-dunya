# Flower Hill — World Specification v4.2

> This specification defines the canonical Flower Hill world for generation.
> This document is a dense generation instruction set.
> Aligned with current single Hero View + World Spec pipeline.

---

## Usage

This document is the generation specification for Flower Hill.

### Mode A — Hero View Creation:
Before a Hero View exists, use this text to generate the first Canon Hero View.

### Mode B — Scene Generation:
After a Hero View is approved, use the uploaded Hero View image plus this specification for scene generation.

If the uploaded Hero View and this text disagree, follow the uploaded Hero View.

---

## Identity

Flower Hill is the most colourful hill in Pompom Hills: a soft rounded green hillside covered in abundant but readable colourful flowers, with a curved stepping-stone path.

Flower Hill is a **flower-dominant** world — the colourful counterpart to Cloud Hill's sky-dominant identity. The single defining quality: five flower colours must always be readable, and the path must always be visible.

---

## Must Preserve

- soft rounded green hill
- dense readable flower carpet
- five flower colours (red, yellow, pink, purple, orange)
- curved stepping-stone path forming a clear S-curve
- warm morning daylight
- soft handcrafted preschool style
- rounded shapes only
- no dry/barren ground
- no sharp stones
- no dark mood
- no modern objects
- no harsh realism

---

## Hero View Technical Setup

| Parameter | Value |
|-----------|-------|
| Camera height | ~1.00–1.20 m (wide establishing) |
| Focal length equivalent | 24–35mm — wide but not distorted |
| Viewing angle | Slight downward tilt, ~5–10° |
| Format | Wide 16:9 |

### Target Framing Ratios

| Zone | Frame % |
|------|:-------:|
| Sky | ~25–30% |
| Flower carpet + hill (mid/background) | ~45–55% |
| Foreground (path + dense flowers) | ~20–25% |

This is the inverse of Cloud Hill's sky-dominant ratio — Flower Hill is flower-dominant.

---

## Hero View Composition

The primary Hero View identity is: flower carpet + five colours + S-curve stepping-stone path + soft rounded hill. Connected homes are optional and secondary.

- no characters
- no animals
- no butterflies
- wide 16:9 environment
- foreground: curved stepping-stone path and dense flowers
- midground: rolling Flower Hill with flower fields
- background: soft sky and distant gentle hills
- five colours clearly visible
- path clearly visible as S-curve
- warm morning daylight
- not cluttered
- default: omit Kiko's Home and Mimi's Burrow unless explicitly needed
- if shown, they must be tiny, soft, distant landmarks only, never redesigned

---

## Butterfly Rule

**Hero View:**
- no butterflies
- no animals
- pure environment only

**Story shots:**
- FH-BUTTERFLY-01 may appear optionally
- only when the story needs it
- never required in every Flower Hill frame
- butterfly should not distract from flower/path identity
- if present: single or at most 2–3, confined to a small area of frame, slow and gentle movement matching wind rhythm

---

## World Identity Lock

### Locked elements

| Element | Canonical Definition | Locked |
|---------|----------------------|:------:|
| Hill silhouette | Soft rounded slope, no peak, no jagged edge | 🔒 |
| Path shape | Clear S-curve through the flower field, never a straight line | 🔒 |
| Flower colour count | Exactly 5: red, yellow, pink, purple, orange, all readable in wide shots | 🔒 |
| Colour dominance cap | No single flower colour exceeds ~40% of frame | 🔒 |
| Path material | Smooth rounded stepping stones, soft matte grey #E0E0E0 | 🔒 |
| Grass colour | Soft green #C8E6C9 | 🔒 |
| Lighting default | Warm morning daylight — upper-left, warm | 🔒 |
| Framing ratio | ~25–30% sky / ~70–75% flower+hill+path in wide shots | 🔒 |

### Canonical Hero View Rule (applies once Hero View is approved)

Once the Hero View is approved, match it on these six points before accepting any new Flower Hill generation:

1. Hill silhouette — soft, rounded, same slope as Hero View
2. Path shape — same S-curve direction and proportion
3. Framing ratio — approximately 25–30% sky / 70–75% flower+hill+path
4. Five-colour distribution — balanced, no colour dominating
5. Colour palette — pastel tones within the defined range
6. Path material and colour — soft matte grey (#E0E0E0)

If a generated frame does not resemble the Hero View silhouette on first glance, reject without further evaluation.

### Acceptable Natural Variations

- Exact flower placement within clusters
- Exact flower count per cluster (within 8–15 range)
- Slight colour variation within the defined palette
- Path curve detail (as long as the overall S-shape is preserved)
- Wind direction
- Small decorative flower clusters

### What Must Never Change

- Flower Hill must never become a generic green hill
- Flower Hill must never become a forest
- Flower Hill must never become a realistic wild meadow
- Flower Hill must never lose its five-colour flower identity
- Flower Hill must never be dry, brown, sparse, or faded
- Path must never become concrete, asphalt, dirt road, or sharp stone

---

## Colour Palette

Vibrant pastel. Colourful but controlled.

White balance: warm morning daylight, approximately 5500K.
Exposure: gently bright, not overexposed (+0.2 to +0.4 stops).
Contrast: low.
Saturation: medium-high pastel, never neon.

### Flower colours:
- red #EF5350
- yellow #FFD54F
- pink #F48FB1
- purple #CE93D8
- orange #FF7043

### Grass:
- soft green #C8E6C9

### Path:
- soft grey #E0E0E0

### Highlight behaviour:
Highlights are soft and rolled — never clipped to pure white. The brightest point in any frame should be a flower petal highlight, never a hard glare.

### Shadow behaviour:
Shadows are lifted and warm — never cold, never black. The darkest value in a standard daytime frame is approximately a warm mid-grey (#9E9E9E) or lighter.

### Forbidden colour shifts:
- neon colour
- muddy colour
- grey desaturation
- orange sunset shift
- blue cold shift
- high contrast HDR
- realistic photography colour
- dark green forest palette
- brown dry field palette
- pure black anywhere
- pure white except soft flower highlights

---

## Lighting

Warm morning daylight — the permanent default lighting identity for Flower Hill.

### Light direction

| Time | Direction | Quality |
|------|-----------|---------|
| Morning (default) | Upper-left, warm | Softest — gentle, bright |
| Midday (special story use only) | Upper-centre, neutral | Bright — even, clean |
| Sunset (special variant only, never Hero View) | Upper-left, warm-orange | Long soft shadows |

Default light direction across all standard scenes is **upper-left, warm morning**. If a scene begins in this light, every shot in that scene keeps it.

### Softness

All light is soft. No hard shadows, no sharp shadow edges, no spotlight effects. Light should feel filtered through thin cloud — bright but never harsh.

### Ambient fill

A gentle ambient fill always lifts the shadow side of every object. Nothing falls into true darkness. The darkest shadow value is approximately 70% of the highlight value — never lower.

### Shadow density

| Shadow Type | Density | Notes |
|-------------|---------|-------|
| Character shadow on grass | Very soft, 20–30% opacity | Short — never longer than character height |
| Flower shadow | Slightly visible | Never suppresses flower colour |
| Path stone shadow | Visible but soft | Defines stone separation |

### Exposure behaviour

The world is always slightly bright — lifted, not overexposed. Midtones are open and readable. Nothing crushed in darks. Highlights soft, never blown.

Soft preschool light.
Low contrast.
No hard shadows.
No dramatic golden-hour look.
No sunset (default scenes).
No cinematic colour grading.
No HDR.
No orange shift.
No colourful reflection.
No rainbow glare.

### Continuity rules

- Light direction does not change between shots in the same scene.
- If a scene opens in morning light, it stays in morning light throughout.
- Character lighting must match environment lighting — no isolated character illumination.

Lighting should support colour clarity, not overpower it.

---

## Flower Density

Abundant but readable.
Dense clusters with clear walking space.
Path always visible.
Characters always readable.
Five colours visible in every wide shot.

| Metric | Value |
|--------|-------|
| Flowers per cluster | 8–15 |
| Space between clusters | Clear grass or path strip |
| Colours visible in wide shot | Minimum 5 (all) |
| Max frame coverage per single colour | ~40% |

---

## Spatial Layout

```
Central Square → Flower Hill girişi → Çimenlik → Çiçek tarlası → Patika → Kiko's Home / Mimi's Burrow
```

---

## Playable Areas

**Hilltop** — Purpose: en geniş manzara. Visual identity: çiçekler, açık gökyüzü, patika kesişimi. Typical use: varış, geniş bakış.

**Flower Fields** — Purpose: renk cümbüşü bölgesi. Visual identity: yoğun ama okunabilir çiçek kümeleri, beş renk. Typical use: renk öğrenme, çiçek sayma.

**Path** — Purpose: bağlantı yolu. Visual identity: kavisli taşlar, çiçekler arasında S-eğrisi. Typical use: yürüyüş, keşif.

---

## Materials

Grass: soft plush green. Flowers: round, soft petals in vibrant pastel colours, height ~0.25–0.40 m (child knee-to-waist height). Path stones: smooth, rounded stepping stones, soft matte grey (#E0E0E0), diameter ~0.35 m, child-safe. Not brown. Not dirt. Not concrete/asphalt. All surfaces read as soft, colourful, and child-safe.

---

## Scale

Everything sized for small preschool children. Hill is gentle, not steep. Path is wide enough for comfortable walking (~0.60–0.80 m). Flowers large enough to see colours clearly.

| Element | Measurement |
|---------|-------------|
| Stepping stone diameter | ~0.35 m |
| Flower height | ~0.25–0.40 m |
| Path width | ~0.60–0.80 m |
| Camera eye level range (project standard) | 0.70–1.10 m |
| Flower Hill wide establishing camera height | ~1.20 m |

---

## Camera Identity

### Default lens

24–35mm equivalent. Wide enough to reveal the flower field and path; not so wide it distorts form. Never wider than 20mm (hill distortion). Never tighter than 50mm (loses flower-carpet feel).

### Character eye level

| Height | Usage |
|--------|-------|
| 1.20 m | Wide establishing, full hill + path visible |
| 0.85 m | Medium, character + nearby flowers |
| 0.30 m | Close-up, flower detail or character bending to a flower |

### Movement philosophy

The camera moves slowly and gently, like wind through flowers. Nothing sudden, no hard cuts. The world is calm and the camera respects that calm.

### Allowed movements

| Movement | Speed | When |
|----------|-------|------|
| Slow pan | Very slow — 3–5 sec across frame | Establishing, flower field reveal |
| Slow track | Slow, matched to character pace | Path walking scenes |
| Slow push-in | Very slow — 4+ sec | Emotional moment, flower discovery |
| Static hold | — | Dialogue, observation, flower smelling |

### Forbidden movements

```
✗ Fast zoom
✗ Handheld shake
✗ Whip pan
✗ Dutch angle
✗ 360° rotation
✗ Drone-style fly-over
```

### Framing consistency

- Subject never dead-centre — slightly left or right.
- Path always visible in wide shots — never cropped out.
- Characters framed against the flower field, not bare grass.

### Transition rules

- Scene openings: always begin with environment wide shot before character.
- Scene closings: end wider than the previous shot — pull back to the flower field.
- Between shots: cut or slow dissolve only — no wipe, no flash.

---

## Environmental Sound Identity

> Aligned with AUDIO_GUIDE.md project standard.

### Wind

| Parameter | Value |
|-----------|-------|
| Intensity | Soft and constant — never gusting, never silent |
| Tone | Gentle, mixed with flower/leaf rustle |
| Variation | Slight — rises gently at emotional peaks |
| Forbidden | Howling, sharp gusts, threatening wind sound |

### Bird and bee frequency

| Parameter | Value |
|-----------|-------|
| Bird call | Always lightly present, distant |
| Bee hum | Very distant, sparse, never close or dominant |
| Call type | Single, melodic — never flocking or chattering |
| Frequency | One bird call every 8–12 seconds on average |
| Volume | Low — never louder than the wind layer |

### Ambience level

Total ambient sound sits at approximately -18 dB per AUDIO_GUIDE.md. Dialogue always sits clearly above ambience.

### Silence ratio

Silence, or near-silence with only faint wind, is valid during flower-smelling, colour-discovery, or calm walking moments.

### Forbidden sounds

```
✗ Traffic, machinery, modern sound
✗ Crowd noise
✗ Thunder or storm sounds
✗ Loud or swarming insect sound
✗ Sudden loud sounds
✗ Music not authored for the scene
```

---

## Consistency Rules

- At least 5 flower colours always visible
- No single flower colour exceeds ~40% of frame
- Grass always soft green (#C8E6C9)
- Path always round stones (#E0E0E0), forming an S-curve
- No barren ground
- No dark areas
- Flower carpet always dense but readable
- Light direction consistent within a scene

---

## Reusable Assets

| Asset ID | Description | Notes |
|----------|-------------|-------|
| FH-FLOWER-R | Round red flowers | 8–15 per cluster |
| FH-FLOWER-Y | Round yellow flowers | 8–15 per cluster |
| FH-FLOWER-P | Round pink flowers | 8–15 per cluster |
| FH-FLOWER-V | Round purple flowers | 8–15 per cluster |
| FH-FLOWER-O | Round orange flowers | 8–15 per cluster |
| FH-GRASS-01 | Soft green grass | Base for non-flower areas |
| FH-PATH-01 | Curved stepping stones | S-curve, ~0.35 m diameter stones |
| FH-BUTTERFLY-01 | Colourful butterflies | Optional, story shots only |

---

## World Navigation

> Canonical movement flow through Flower Hill.

### Entry point

Characters always enter from the Central Square direction. Arrival at the flower field edge is part of the world experience, not skipped.

### Canonical transition sequence

```
1. Entry — character appears at the foot of the hill, flower field beginning
       ↓
2. Path Walk — character follows the S-curve stepping-stone path
       ↓
3. Flower Field Exploration — main story content (colour learning, counting, smelling)
       ↓
4. Natural Exit — character continues along the path toward Kiko's Home or Mimi's Burrow
```

### Path Walk

The path traces a clear S-curve. Camera typically follows from the side or behind. The flower field reveals gradually, not all at once.

### Flower Field Exploration

This is the main story area. Characters stop, bend down, count, or smell among flower clusters. All five colours should be readable here.

### Natural Exit

Characters continue along the path and leave the scene — no abrupt cut. Closing is often a wide flower-field frame, possibly with the character as a small departing silhouette.

### Canonical vs. Optional transitions

| Transition | Status | Notes |
|-----------|--------|-------|
| Entry → Path → Field | Canonical | Use in every episode visiting Flower Hill |
| Field → Exit | Canonical | Standard story structure |
| Starting directly in the field | Optional | Only if entry was shown in a previous episode |
| Teleporting between worlds without a transition shot | Forbidden | Always show the approach |

---

## View Transition Rules

### Standard shot sequence

```
Environment wide (establish — no character)
    ↓
Approach shot (character on path, entering field)
    ↓
Field shot (main story content)
    ↓
Close shot (emotional peak — face, flower, hand)
    ↓
Closing wide (exit or field hold)
```

### When to use each shot type

| Shot Type | When | Notes |
|-----------|------|-------|
| Environment wide | Scene opening, before character | Always first |
| Approach shot | Character on path, entering field | Can be skipped when continuity permits |
| Field shot | Character in field — main story content | Always present |
| Close shot | Emotional peak | Optional but recommended |
| Closing wide | Scene end | Always wider than the previous shot |

---

## Generation Failures

| Failure | Fix |
|---------|-----|
| Generic meadow | Add curved path, dense five-colour flower carpet |
| Flowers too sparse | Increase flower density (8–15 per cluster) |
| Flowers too chaotic | Use clustered readable flower fields |
| Path missing | Add curved stepping-stone path |
| Path is a straight line | Re-curve into a clear S-shape |
| Too neon | Use vibrant pastel |
| Too muted | Restore five-colour pastel palette |
| Homes redesigned | Keep homes distant or omit |
| Forest look | Keep open hill, flowers and path |
| Sunset/orange light in Hero View | Revert to warm morning daylight |
| Butterfly present in Hero View | Remove butterfly, pure environment only |

---

## Video Rules

| Element | Rule |
|---------|------|
| Flower movement | Gentle sway, 20 sec cycle |
| Grass movement | Soft wave, 15 sec cycle |
| Camera speed | Max 3% frame/sec pan or track |
| Wind | Constant, gentle |

---

## Hero View Generation Prompt

Copy this prompt directly into OpenArt to generate the Canon Hero View.

```
Create the Canon Hero View for Flower Hill in Pompom Hills.

Flower Hill is the most colourful hill in Pompom Hills: a soft rounded green hillside covered with an abundant but readable carpet of colourful flowers.

The primary identity is: flower carpet + five colours + S-curve stepping-stone path + soft rounded hill. Connected homes are optional and secondary.

This is a pure environment reference image.
No characters.
No animals.
No butterflies.
No text.
No logo.

Composition:
Wide 16:9 establishing view.
Foreground: curved soft grey stepping-stone path forming a clear S-curve through the flowers.
Midground: soft rounded green Flower Hill covered with dense but readable flower clusters.
Background: soft pastel sky and distant gentle hills.

The flower carpet must clearly show five colours: red, yellow, pink, purple, orange.
Use vibrant pastel colours, never neon.
Grass is soft pastel green.
Path stones are smooth rounded matte grey.
Everything feels safe, rounded, preschool-friendly and handcrafted.

Lighting:
Warm morning daylight.
Soft preschool light.
Low contrast.
No hard shadows.
No sunset.
No orange grading.
No HDR.
No cinematic look.

Identity:
The image must immediately read as "the colourful flower hill of Pompom Hills."
Not a generic meadow.
Not a forest.
Not a realistic wild field.
Not a garden shop.
Not a dry field.

Connected locations:
Default Hero View should omit Kiko's Home and Mimi's Burrow unless they are explicitly needed. Flower Hill's Hero View should focus on the flower carpet, S-curve stepping-stone path, soft rounded hill, and five-colour identity. If Kiko's Home or Mimi's Burrow appear, they must be tiny, soft, distant landmarks only and must not be redesigned.

Avoid: photorealism, neon colours, brown dry grass, barren soil, sharp stones, dark mood, forest look, visual clutter, too many chaotic flowers, missing path, realistic meadow, modern objects.

The final image should be iconic, clean, colourful, warm, and reusable as the master visual reference for all future Flower Hill scenes.
```

---

## Hero View QA Checklist

- [ ] No characters.
- [ ] No animals or butterflies.
- [ ] Five flower colours visible: red, yellow, pink, purple, orange.
- [ ] Flower density abundant but readable.
- [ ] Curved stepping-stone path clearly visible.
- [ ] Path forms a readable S-curve.
- [ ] Grass is soft pastel green.
- [ ] Lighting is warm morning daylight.
- [ ] No orange sunset grading.
- [ ] No neon colours.
- [ ] No barren soil.
- [ ] No forest look.
- [ ] No redesigned Kiko's Home.
- [ ] No redesigned Mimi's Burrow.
- [ ] Image is iconic enough to define Flower Hill.

---

## Production QA

> Run before accepting any generated frame, shot, or scene for Flower Hill.

### World Identity
```
✓ Hill silhouette soft and rounded?
✓ Five flower colours visible and readable?
✓ Path forms a clear S-curve?
✓ Grass is soft green (#C8E6C9)?
✓ No sharp edges or sharp stones?
✓ No dark mood anywhere in frame?
```

### Camera Identity
```
✓ Camera height matches shot type (1.20 / 0.85 / 0.30 m)?
✓ Lens feels like 24–35mm — no distortion?
✓ Subject off-centre, not dead-centre?
✓ Path visible in wide shots?
✓ No forbidden camera movement (zoom, shake, dutch angle)?
```

### Lighting Identity
```
✓ Light from upper-left, warm morning?
✓ No hard shadow edges?
✓ Shadow side lifted — no true darkness?
✓ Highlights soft — not clipped to pure white?
✓ No golden-hour / sunset / orange shift in default scenes?
```

### Colour Identity
```
✓ Five flower colours match defined hex values?
✓ No neon anywhere?
✓ Overall warmth present — not cool-shifted?
✓ Low contrast — no HDR look?
```

### Scale Identity
```
✓ Characters correctly scaled against flowers?
✓ Path stones sized for comfortable child steps (~0.35 m)?
✓ Flowers at knee-to-waist height (~0.25–0.40 m)?
```

### Atmosphere Identity
```
✓ Scene feels colourful, beautiful, inviting?
✓ Wind implied through flower/grass movement?
✓ No modern objects anywhere in frame?
✓ Connected homes soft and distant if shown?
```

### World Recognition
```
✓ Would a viewer recognise this as Flower Hill from a previous episode?
✓ Do the five colours and S-curve path read immediately?
✓ Could this frame sit next to another Flower Hill frame without inconsistency?
```

---

## Production Summary

Flower Hill is Pompom Hills' flower-dominant world — the colourful counterpart to Cloud Hill's sky-dominant identity. Its one defining rule: five colours must always be readable, and the path must always be visible. Everything else — flower placement, butterfly presence, wind direction — can flex.

For production, Flower Hill is medium complexity: a small prop set (five flower colours, grass, path, optional butterfly), a locked colour palette, and a clear camera language. The most common failure is flower density being too sparse or too chaotic — both break preschool readability. The second most common failure is the path flattening into a straight line and losing its S-curve identity.

Every future episode using Flower Hill should load the Hero View as its master reference, verify Colour Identity before accepting any frame, and run the Production QA checklist before signing off on any shot. The world does not change. Only the story does.

---

## Changelog

| Version | Changes | Breaking |
|---------|---------|:--------:|
| 4.0 | Single Hero View + World Spec pipeline | ✅ Breaking |
| 4.1 | Fixed Mimi / Mimi's Burrow terminology. Removed OpenArt-unsafe local file references from World Spec header. Fixed S-curve typo. Clarified butterfly usage: not in Hero View, optional in story shots. Unified path material as soft matte grey #E0E0E0. Unified lighting as warm morning daylight. Added copy-ready Hero View Generation Prompt. Added Hero View QA Checklist. | — |
| 4.1 micro-polish | Unified Pompom Hills spelling. Unified default lighting as warm morning daylight. Marked sunset/snow/rain as special variants. Clarified that connected homes are optional and secondary in Hero View. | — |
| 4.2 | Production-depth pass: added Hero View Technical Setup and framing ratios, expanded World Identity Lock (locked element table + Canonical Hero View Rule), expanded Colour Palette (highlight/shadow behaviour), expanded Lighting (direction table, softness, ambient fill, shadow density, continuity), expanded Camera Identity (lens, movement philosophy, allowed/forbidden movements, framing/transition rules), new Environmental Sound Identity, new World Navigation, new View Transition Rules, categorized Production QA (World/Camera/Lighting/Colour/Scale/Atmosphere/World Recognition), new Scale table, new Production Summary. Five colours, pipeline, and Hero View QA Checklist unchanged. | — |

---

*This specification supports the current Pompom Hills production pipeline.*
*Flower Hill — World Specification v4.2*
*Last updated: 4 Temmuz 2026*
