# Sun Hill — World Creation Specification

> Source of truth: `04-sun-hill-bible.md` (canonical, creative). This document
> is a production-oriented extraction for AI-assisted world generation. It does
> not replace the Bible and does not duplicate its storytelling, educational,
> character, or workflow content.

---

## Purpose

Sun Hill is the warmest hill in Pompom Hills — the first to receive sunlight every morning. It is a wide, soft, open grass hill with an expansive valley view, designed for sunrise scenes, breakfast moments, energy-filled adventures, and warm emotional peaks.

---

## Immutable Identity

The following elements define the canonical identity of Sun Hill and must never change:

- Warm open grass hill with gentle slope
- First sunlight of the day hits here
- Wide panoramic valley view from summit
- Short bright green grass (#C8E6C9)
- Warm golden sunlight dominant
- Open sky — sun always visible
- Pastel distant hill silhouettes on horizon
- No structures, no fences, no modern objects
- Warm pastel colour palette throughout

---

## Visual Identity

A wide, gently sloping open hill covered in short bright green grass. The sun dominates the composition — always visible, always warm, always casting golden light. The hill crest provides a broad panoramic view of the entire valley below. Distant hills appear as soft pastel silhouettes. The overall feeling is warmth, energy, and optimism — a place where every day begins.

---

## World Layout

The world reads as one continuous upward journey. The lower slope begins the climb, the mid-slope builds energy, the hill crest opens into a wide flat area, and the summit point provides the panoramic view. There are no separate structures or zones — just one flowing hill from base to peak.

---

## Spatial Relationships

- The lower slope connects naturally to the mid-slope climb.
- The mid-slope opens into the wide hill crest.
- The hill crest leads to the summit observation point.
- The valley view is visible from every point on the upper hill.
- The sun is always overhead or upper-right in every composition.
- Distant hills are always visible on the horizon.

---

## Playable Areas

**Lower Slope** — Purpose: the beginning of the climb, where the journey starts. Visual identity: gentle grass slope, warm sunlight. Important props: grass, slope. Typical use: arrival, approach, first steps upward.

**Mid-Slope** — Purpose: the climbing experience. Visual identity: ascending grass with expanding view. Important props: grass, distant view. Typical use: walking, climbing, looking up.

**Hill Crest** — Purpose: the heart of the hill, wide flat sitting area. Visual identity: broad flat grass plateau, warm sun overhead. Important props: flat grass area. Typical use: sitting, resting, group moments.

**Summit Point** — Purpose: the panoramic observation spot. Visual identity: highest point, full valley view. Important props: open view. Typical use: looking down, discovery, emotional peaks.

**Valley View** — Purpose: the reward for climbing — the entire world visible below. Visual identity: wide valley with distant pastel hills. Important props: distant hills, valley floor. Typical use: wonder, connection, overview.

---

## Materials

Ground: short bright green grass, plush and warm to the touch. No rocks, no hard surfaces, no sharp edges. Every surface reads as soft, warm, and sun-drenched. The grass has a gentle plush texture — like a soft carpet warmed by sunlight. Distant hills are soft matte pastel shapes. The sky is warm and clear.

---

## Lighting

Primary light is warm golden sunlight from above. The hill receives the strongest, warmest light in all of Pompom Hills. Shadows are very soft and short — the hill is mostly lit evenly. Morning brings the warmest golden tones; midday is bright and even; evening turns deeper gold with longer soft shadows. The sun is always the dominant light source — never overcast, never dim.

---

## Colour Palette

Grass: bright warm green (#C8E6C9). Sky: warm blue (#BBDEFB). Sun: golden (#FFF9C4). Horizon hills: soft pastel green (#E8F5E9). Flowers: warm yellow (#FFD54F) and orange (#FFAB91). The palette stays within this warm, bright, sun-drenched set across every zone.

---

## Scale

The hill is wide and open — large enough to feel expansive, small enough to feel approachable. The climb is gentle, not steep. The summit provides a wide view without being dizzying. Everything is sized for small preschool children to climb comfortably and safely.

---

## Atmosphere

Warm. Bright. Energetic. Optimistic. Every surface reads as sun-drenched and inviting. The mood is consistently warm and hopeful — a place where children feel "today is going to be a great day."

---

## Consistency Rules

- The hill is always warm and sunlit — never overcast, never cold.
- The grass is always bright green — never dark, never brown.
- The sun is always visible in wide shots — never hidden.
- The valley view is always present from the summit.
- No structures, no fences, no modern objects anywhere.
- No cool colour shifts, no dark shadows, no rain, no fog.
- The hill's gentle slope and wide crest are preserved across every generation.

---

## Generation Considerations

The hill must be generated as one continuous warm grass slope with a wide crest and panoramic view — not as a steep cliff or narrow ridge. Keep the sun dominant in every composition. Keep the colour palette warm and bright. The hill's identity — its warmth, its openness, its sun-drenched quality — must be preserved exactly across every generation.

---

## Colour Palette (Detailed)

| Asset ID | Element | Hex |
|----------|---------|-----|
| SH-GRASS-01 | Grass | #C8E6C9 |
| SH-SKY-01 | Sky | #BBDEFB |
| SH-SUN-01 | Sun glow | #FFF9C4 |
| SH-HORIZON-01 | Distant hills | #E8F5E9 |
| SH-FLOWER-01 | Yellow flowers | #FFD54F |
| SH-FLOWER-02 | Orange flowers | #FFAB91 |

White balance: 5500K warm. Exposure: +0.3 lifted. Contrast: low. Saturation: medium.
No neon. No pure black. No cool shift in daytime.

---

## Reusable Assets

| Asset ID | Description |
|----------|-------------|
| SH-GRASS-01 | Short bright warm green grass, plush surface |
| SH-PLATEAU-01 | Wide flat grass crest area |
| SH-STONE-01 | Round warm stone (optional sitting spot) |
| SH-FLOWER-01 | Warm yellow flower clusters |
| SH-FLOWER-02 | Warm orange flower clusters |
| SH-HORIZON-01 | Low pastel hill silhouettes on horizon |
| SH-SUN-01 | Dominant warm golden sun |

---

## Framing

Sun always visible in every wide shot — never hidden. Valley view present in summit shots.

| Shot | Max Character % | Sun Visible |
|------|:---------------:|:-----------:|
| Wide establishing | 15–20% | Always |
| Medium single | 30–35% | Always |
| Medium two characters | 40–45% | Always |
| Close-up | 65–75% | 50%+ |

Emotional peak = wide shot showing full valley, not close-up.

---

## Navigation

Default flow: Entry (lower slope) → Climb (mid-slope) → Crest (flat area) → Summit (observation) → Exit.
Summit arrival — valley opening moment — must not be skipped.
**Alternative openings are permitted when story continuity requires them.**

---

## Generation Failures — Quick Reference

| Failure | Fix |
|---------|-----|
| Cool colour temperature | Warm to 5500K, recheck palette |
| Sun not visible in wide shot | Add sun or regenerate |
| Dark or heavy shadows | Reduce shadow density |
| Rain or fog present | Reject — Sun Hill is always clear |
| Grass too dark | Brighten to #C8E6C9 range |
| Valley view missing from summit | Add panoramic view or regenerate |
| Sharp edges anywhere | Smooth all forms |
| Modern objects present | Reject — no structures |

---

## Video Rules

| Element | Rule |
|---------|------|
| SH-SUN-01 movement | Gentle pulse, very slow, 8–10 sec cycle |
| SH-GRASS-01 movement | Warm breeze wave, 4–5 sec cycle, tips only |
| Wind | Constant, warm, soft — no gusts |
| Camera speed | Max 5% frame/sec pan or tilt |
| Environmental rhythm | Sun, grass, camera all move on the same warm breath |

Every animated frame passes the same QA as a still image.

---

## Visual Richness Layer

> See `02-WORLDS/GLOBAL_ENVIRONMENT_STANDARD.md` § Visual Richness Principle.
> Sun Hill must never be reduced to "a hill with sun."

This layer protects Sun Hill from becoming too plain. Keep the wide warm
slope and panoramic crest readable — add only the canon-approved charm
details below. Do not add random objects. Do not remove the warm,
energetic, sunrise emotional identity.

**Allowed charm details:** SH-STONE-01, the round sun-warmed sitting stone
at the Güneş Noktası, is the primary landmark and should be present at the
hill's brightest point. SH-PLATEAU-01, the wide flat hill crest, opens into
the panoramic valley view that defines the summit experience. Warm sunlit
sparkle across the short bright-green grass (SH-GRASS-01) and soft pastel
horizon hills (SH-HORIZON-01) add surface charm. SH-FLOWERS-01 scattered
yellow and orange wildflower clusters bring small reusable prop charm.
Gentle motion — a warm breeze wave across the grass tips and the sun's soft
golden pulse at the Güneş Noktası — keeps the world feeling alive.

**Forbidden clutter:** an empty plain hill with no landmark, cold or dim
lighting, rain or fog, sharp corners or jagged terrain, modern structures,
characters or logos in the Hero View, dark or desaturated grass, and any
noise or fast motion.

### Art Direction Layer (use together with Immutable Identity above)

```text
premium preschool animation, handcrafted toy-set feeling, warm golden
sunrise atmosphere, storybook energy and hope, thumbnail-appeal
composition, makes a child want to climb up and greet the first light
```

### Hero View Quality Tests

Before accepting a Hero View, it must pass:

1. **Silhouette Test** — recognisable as Sun Hill from the wide warm slope and open crest alone?
2. **Colour Test** — recognisable from the bright green grass, warm gold sun, and pastel sky alone?
3. **Charm Test** — does it make a child want to climb up and sit on the warm stone in the sunlight?

If any test fails, reject.

---

*Sun Hill — World Specification, aligned with Bible v3.1.*
*Visual Richness Layer added 4 Temmuz 2026.*
