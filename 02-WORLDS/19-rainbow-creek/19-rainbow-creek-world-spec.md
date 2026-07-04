# Rainbow Creek — World Creation Specification

> Source of truth: `19-rainbow-creek-bible.md` (canonical, creative). This document
> is a production-oriented extraction for AI-assisted world generation. It does
> not replace the Bible and does not duplicate its storytelling, educational,
> character, or workflow content.

---

## Purpose

Rainbow Creek is a natural waterway flowing between Stone Hill and Flower Hill — a clear, shallow stream with smooth colourful stones, a small wooden bridge, and gentle fish families. It teaches children about nature's peaceful rhythm through water, stone, and quiet observation.

---

## Immutable Identity

The following elements define the canonical identity of Rainbow Creek and must never change:

- Clear shallow flowing water
- Smooth round colourful stones (pink, yellow, blue, green)
- Small low wooden bridge
- Fish families swimming in the water
- Green plants along the banks
- No deep water, no fast currents, no dark atmosphere
- Warm natural sunlight
- Peaceful, meditative mood

---

## Visual Identity

A clear, shallow stream flowing gently between green banks. Smooth round stones in pastel colours line the edges — pink, yellow, blue, green. A small low wooden bridge crosses the water. Fish families glide through the clear water below. Green plants and flowers frame the banks. The overall feeling is peaceful and natural — a place where time slows down and every detail invites quiet observation.

---

## World Layout

The world reads as one continuous flowing stream. Stone Hill on one end provides the water source, which flows down through the stone-lined banks, under the wooden bridge, and continues toward Flower Hill. There are no separate structures — just one flowing waterway from source to destination.

---

## Spatial Relationships

- The creek flows continuously from Stone Hill to Flower Hill.
- The stones are always visible along both banks.
- The bridge always spans the creek at the midpoint.
- Fish are always visible in the clear water.
- Plants frame the banks on both sides.
- The water surface reflects sunlight constantly.

---

## Playable Areas

**Creek Source (Stone Hill side)** — Purpose: where the water begins. Visual identity: small spring, first stones, water emerging. Important props: source, stones. Typical use: discovery, looking up.

**Creek Middle** — Purpose: the heart of the stream. Visual identity: flowing water, colourful stones, fish visible below. Important props: water, stones, fish. Typical use: observation, stone collecting, fish watching.

**Bridge** — Purpose: crossing point over the water. Visual identity: low wooden bridge with railings, water flowing beneath. Important props: bridge, water. Typical use: crossing, looking down, transition.

**Creek End (Flower Hill side)** — Purpose: where the creek meets the meadow. Visual identity: water widening, flowers on banks, calm pool. Important props: flowers, calm water. Typical use: resting, reflecting.

---

## Materials

Water: clear, gentle flow, sun-reflective surface. Stones: smooth, round, pastel-coloured. Bridge: natural wood, low and sturdy. Plants: soft green leaves, round flowers. All surfaces read as natural, soft, and safe. No sharp edges, no rough surfaces, no dangerous elements.

---

## Lighting

Primary light is warm natural sunlight reflecting off the water surface. Stones catch and reflect light creating gentle sparkle. Shadows are soft and green-tinted from surrounding plants. The overall feeling is bright, natural, and peaceful.

---

## Colour Palette

| Asset ID | Element | Hex |
|----------|---------|-----|
| RC-CREEK-01 | Water | #E3F2FD |
| RC-STONES-P | Pink stones | #F48FB1 |
| RC-STONES-Y | Yellow stones | #FFD54F |
| RC-STONES-B | Blue stones | #42A5F5 |
| RC-STONES-G | Green stones | #66BB6A |
| RC-BRIDGE-01 | Bridge | #A1887F |
| RC-PLANTS-01 | Plants | #66BB6A |
| RC-FLOWERS-01 | Flowers | #F48FB1, #FFD54F |

White balance: 5000K natural. Exposure: normal. Contrast: low. Saturation: medium.
No neon. No pure black. No dark or cold tones.

---

## Scale

Everything is sized for small preschool children. The creek is shallow and safe. The stones are small and easy to pick up. The bridge is low with secure railings. The fish are small and friendly-looking. The overall feeling is intimate and accessible — nature at child scale.

---

## Atmosphere

Peaceful. Natural. Clean. Calm. Gentle. Every surface reads as smooth and inviting. The mood is consistently serene — a place where children feel "nature is beautiful here."

---

## Consistency Rules

- The water is always clear and shallow — never deep, never murky.
- The stones are always smooth and round — never sharp, never rough.
- The bridge is always low and wooden — never high, never metal.
- Fish are always visible in the water — never hidden, never scary.
- No fast currents, no dark water, no dangerous elements.
- The colour palette stays natural and pastel throughout.

---

## Generation Considerations

The creek must be generated as a gentle, shallow stream — not as a deep river or rushing waterfall. Keep all shapes rounded. Keep colours natural and pastel. The creek's identity — its peace, its clarity, its gentle rhythm — must be preserved exactly across every generation.

---

## Colour Palette (Detailed)

| Asset ID | Element | Hex |
|----------|---------|-----|
| RC-CREEK-01 | Water | #E3F2FD |
| RC-STONES-01 | Stones (mixed) | #F48FB1, #FFD54F, #42A5F5, #66BB6A |
| RC-BRIDGE-01 | Bridge | #A1887F |
| RC-PLANTS-01 | Plants | #66BB6A |

White balance: 5000K. Exposure: normal. Contrast: low. Saturation: medium.

---

## Reusable Assets

| Asset ID | Description |
|----------|-------------|
| RC-CREEK-01 | Clear flowing water |
| RC-STONES-01 | Smooth round colourful stones |
| RC-BRIDGE-01 | Low wooden bridge |
| RC-FISH-01 | Small friendly fish |
| RC-PLANTS-01 | Green bank plants |
| RC-FLOWERS-01 | Colourful bank flowers |
| RC-LEAVES-01 | Floating leaves |

---

## Framing

Water always visible in every wide shot — it is the primary visual anchor. Stones visible along banks.

| Shot | Max Character % | Water Visible |
|------|:---------------:|:-------------:|
| Wide establishing | 15–20% | Always |
| Medium single | 30–35% | Yes |
| Medium two characters | 40–45% | Yes |
| Close-up | 65–75% | Partial |

Emotional peak = wide shot showing full creek with stones and bridge.

---

## Navigation

Default flow: Stone Hill (source) → Creek flow → Stones → Bridge → Flower Hill (destination).
The journey along the waterway — the stone discovery, the bridge crossing — should feel natural and unhurried.
**Alternative openings are permitted when story continuity requires them.**

---

## Generation Failures — Quick Reference

| Failure | Fix |
|---------|-----|
| Deep water | Shallow only — children must feel safe |
| Fast currents | Gentle flow only |
| Sharp stones | Smooth all stones |
| Dark or murky water | Clear and clean |
| High or metal bridge | Low wooden bridge only |
| No fish visible | Add small friendly fish |
| Cold colour temperature | Warm to 5000K |
| Sharp edges anywhere | Smooth all forms |

---

## Video Rules

| Element | Rule |
|---------|------|
| RC-CREEK-01 flow | Gentle, continuous, slow |
| RC-FISH-01 movement | Slow, round, peaceful |
| RC-LEAVES-01 | Gentle float, 5 sec cycle |
| Camera speed | Max 3% frame/sec pan or track |
| Environmental rhythm | Water, fish, camera all move on the same gentle breath |

Every animated frame passes the same QA as a still image.

---

## Visual Richness Layer

> See `02-WORLDS/GLOBAL_ENVIRONMENT_STANDARD.md` § Visual Richness Principle.
> Rainbow Creek must never be reduced to "a stream and some rocks."

This layer protects Rainbow Creek from becoming too plain. Keep the world
readable and the flowing-water silhouette clear — add only the
canon-approved charm details below. Do not add random objects. Do not remove
the peaceful, meditative emotional identity.

**Allowed charm details:** RC-BRIDGE-01, the low round wooden bridge crossing the creek at its midpoint — primary landmark, always present in mid-creek shots; RC-STONES-01 smooth round rainbow-coloured stones (pink, yellow, blue, green) lining both banks; sunlight sparkle drifting across the moving water surface; RC-FISH-01 small friendly fish families gliding beneath the surface; RC-FLOWERS-01 colourful flowers scattered along the banks; a few RC-LEAVES-01 floating gently on the water.

**Forbidden clutter:** empty plain stream with no bridge or stones, deep or murky water, fast rushing rapids or waterfalls, generic drainage-ditch look, cold blue-grey water tone, dark overhanging vegetation, thorny plants or scary creatures, sharp rocky edges.

### Art Direction Layer (use together with Technical Canon above)

```text
premium preschool animation, handcrafted toy-set feeling, sun-dappled
sparkling creek atmosphere, storybook beauty, thumbnail-appeal composition,
makes a child want to sit on a colourful stone and watch the fish glide by
```

### Hero View Quality Tests

1. **Silhouette Test** — recognisable as Rainbow Creek from the winding water shape and bridge alone?
2. **Colour Test** — recognisable from the pastel rainbow-stone and clear-water palette alone?
3. **Charm Test** — does it make a child want to sit by the water and watch the fish?

If any test fails, reject — see Generation Failures table above and
`19-rainbow-creek-bible.md` § Forbidden Over-Simplification.

---

*Rainbow Creek — World Specification, aligned with Bible v3.1.*
*Visual Richness Layer added 4 Temmuz 2026.*
