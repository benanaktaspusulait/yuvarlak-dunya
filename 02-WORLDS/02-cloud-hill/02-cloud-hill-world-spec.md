# Cloud Hill — World Creation Specification

> Source of truth: `02-cloud-hill-bible.md` (canonical, creative). This document
> is a production-oriented extraction for AI-assisted world generation. It does
> not replace the Bible and does not duplicate its storytelling, emotional,
> character, or workflow content.

---

## Purpose

Cloud Hill is the highest point in Pompom Hills — a single smooth grass dome
where the sky feels close enough to touch. It is the world's primary location
for cloud-watching, wonder, and quiet discovery.

---

## Immutable Identity

The following elements define the canonical identity of Cloud Hill and must
never change across any generation:

- Single smooth dome hill — no peak, no jagged edges, no flat cliff
- Sky occupies 60–65% of every wide frame — sky dominates, always
- 2–3 large white rounded clouds — never 0, never more than 4
- Clouds are always white, always rounded cumulus — never grey, never storm
- Grass is short, even, open green (#A5D6A7) — never yellow, never tall
- Sun in upper right quadrant — always soft, never hard-edged
- Horizon sits at 35–40% from frame bottom in all wide shots
- No buildings, no fences, no modern objects — ever
- No thorns, no sharp stones, no dangerous elements — ever
- Warm pastel palette — soft, handcrafted, never photorealistic

---

## Visual Identity

A single wide grass dome against an open sky. The world is defined by what
is absent as much as what is present — no walls, no structures, no clutter.
The hill's silhouette is one continuous soft curve from edge to edge of the
frame. Two or three large white clouds float in the upper sky, spaced apart
and never touching. The sun sits softly in the upper right. A faint line of
pastel hills marks the horizon. Everything is open, calm, and sky-dominant.
The overall feeling is quiet freedom — a place to breathe, look up, and wonder.

---

## World Layout

The world reads as a simple vertical journey: you climb, and the sky gets
bigger. The hillside is an open grassy slope leading upward to the summit
plateau. The plateau is flat and wide enough to sit comfortably. No enclosure,
no boundary — the world opens in every direction at the top.

```
Hillside (çimenli yokuş — tırmanış)
    ↓
Summit Plateau (geniş düzlük — oturma, izleme)
    ↓ gökyüzü bağlantısı
Open Sky (bulutlar, güneş, ufuk)
```

---

## Spatial Relationships

- The hillside connects naturally to the summit — one continuous grassy surface
- The summit plateau is wide and open — no edge or drop visible from normal camera height
- The sitting stone is always at the summit, slightly right of centre
- Daisies are scattered loosely across both the hillside and summit — never clustered densely
- The horizon is always visible from the summit — distant pastel hill silhouettes only
- Cloud Hill is visually higher than all other hills — other hilltops appear below the horizon line when shooting from the summit
- Central Square is in the valley direction — implied, not visible

---

## Playable Areas

**Hillside** — Purpose: the journey up. Visual identity: open grassy slope, gentle incline, daisies scattered on slope. Important props: daisies. Typical use: arrival, trekking up together, first reveal of the sky opening up.

**Summit Plateau** — Purpose: the main play and observation space. Visual identity: flat open grass, sitting stone, wide sky view in all directions. Important props: sitting stone, daisy cluster. Typical use: cloud-watching, sitting together, quiet conversation, rain observation, rainbow spotting.

**Open Sky** — Purpose: the emotional destination — the reason the hill exists. Visual identity: pale blue sky, 2–3 large white clouds, soft sun upper right. Important props: none — sky only. Typical use: POV cloud shots, tilt-up reveals, wonder moments.

---

## Materials

Grass: soft plush texture, short and even, matte surface — never glossy, never
realistic. Sitting stone: smooth matte grey (#ECEFF1), gently rounded edges —
no sharp corners, no rough texture. Daisy petals: clean white, soft matte.
Daisy centre: warm soft yellow (#FFF59D). Soil: not visible — grass covers
all ground. Sky: flat soft gradient from pale blue-white at horizon (#E3F2FD)
to slightly deeper pale blue at zenith (#BBDEFB). Clouds: pure soft white
(#F5F5F5), matte cotton texture — no internal shadows, no dark undersides.
No glass, no metal, no realistic stone surfaces anywhere.

---

## Lighting

Primary light is warm soft daylight from the upper left. All shadows are soft
and short — never hard, never dark. The ambient fill lifts all shadow sides so
nothing falls into true darkness. Cloud shadows are never cast onto the ground.
The world is always slightly brighter than neutral — open, lifted, safe.

| Time of Day | Quality | Notes |
|-------------|---------|-------|
| Morning | Warm golden, softest | Recommended for story opening scenes |
| Midday | Bright and even, neutral | Clearest colours — best for colour-focused stories |
| Evening | Warm golden-orange | Long soft shadows — emotional closing scenes |
| Night | Soft moonlight, pale blue-white | Stars visible — rare, special scenes only |

---

## Colour Palette

| Element | Colour | Hex |
|---------|--------|-----|
| Grass | Soft open green | #A5D6A7 |
| Sky upper | Pale blue | #BBDEFB |
| Sky lower / horizon | Very pale blue-white | #E3F2FD |
| Clouds | Soft white | #F5F5F5 |
| Distant hills | Pale grey-green pastel | #C8E6C9 |
| Sitting stone | Smooth pale grey | #ECEFF1 |
| Daisy white | Clean white | #FFFFFF |
| Daisy centre | Soft warm yellow | #FFF59D |

White balance: warm daylight, ~5500K. Exposure: slightly lifted (+0.3 stops).
Contrast: low. Saturation: medium-low, pastel. No neon, no deep colours,
no pure black anywhere in the frame.

---

## Scale

Cloud Hill is sized so a small preschool character feels free, not dwarfed.
The hill is wide and gently sloping — never steep enough to feel dangerous.
The summit plateau is large enough for two characters to sit comfortably side
by side with space around them. The sitting stone is approximately 40 cm wide
and 15 cm tall — right for a small character to sit on easily. Clouds are
large and close-feeling — they should read as big and touchable, not tiny and
distant. The horizon hills are low, pastel, and non-dominant.

---

## Atmosphere

Open. Still. Quietly vast. Every frame should feel like a long slow breath.
There is always subtle movement — grass ripples gently, clouds drift very
slowly — but nothing is ever sudden or fast. The world belongs to the sky.
The dominant emotion is peaceful wonder: the soft wide-eyed feeling of being
somewhere high and open, looking at something large and gentle.

---

## Consistency Rules

- Hill silhouette is always a single smooth dome — never redesigned
- Sky-to-ground ratio never falls below 60/40 in wide shots
- Cloud count is always 2–3 — verified before accepting any generation
- Grass colour stays within the defined range — never yellow, never dark
- Sun always in upper right quadrant — never centred, never behind clouds
- No modern object, structure, road, or fence ever appears
- No sharp stones, no thorns, no dangerous elements ever appear
- Sitting stone is always present at the summit in summit scenes
- Colour palette stays within the pastel set — no shifts to vivid or cool

---

## Generation Considerations

The most common failure point is the sky ratio dropping below 60% — verify
this first on every generated frame. The second most common failure is clouds
becoming grey, dark-bottomed, or dramatically lit — reject these immediately,
clouds on Cloud Hill are always pure white and softly lit from above. Keep
the hill silhouette as a single smooth curve — any jagged, pointed, or
asymmetrical result should be rejected. Do not allow any structure, fence,
or modern element to appear even in the background. Keep grass strictly within
the defined colour range — yellow or olive grass breaks the world identity
immediately. When generating summit scenes, ensure the sitting stone is
present and correctly scaled.
