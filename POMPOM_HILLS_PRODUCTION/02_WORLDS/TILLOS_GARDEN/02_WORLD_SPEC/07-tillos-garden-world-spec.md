# Tillo's Garden — World Creation Specification

> Source of truth: `07-tillos-garden-bible.md` (canonical, creative). This document
> is a production-oriented extraction for AI-assisted world generation. It does
> not replace the Bible and does not duplicate its storytelling, educational,
> character, or workflow content.

---

## Purpose

Tillo's Garden is a warm, earthy outdoor space where gardening, growth, and nurturing happen. It features round flower beds, soft brown soil, green plants, and natural wooden tools. It teaches children the beauty of patience and care through hands-on gardening experiences.

---

## Immutable Identity

The following elements define the canonical identity of Tillo's Garden and must never change:

- Round flower beds (low, earth-toned)
- Soft brown soil (#8D6E63)
- Green plants and flowers
- Natural wooden tools (shovel, watering can)
- Straw hat on fence or shelf
- Warm golden sunlight
- No thorns, no sharp tools, no dangerous equipment
- Round shapes throughout
- Warm earth-tone colour palette

---

## Visual Identity

A warm outdoor garden with round flower beds, soft brown earth, and green plants growing gently. Natural wooden tools — a straw hat, blue watering can, small shovel, seed box — sit ready for use. The sun casts warm golden light across the soil. Everything reads as soft, natural, and hand-tended. The overall feeling is a "loving garden" — a place where good things grow with patience.

---

## World Layout

The world reads as one continuous garden space. Round flower beds surround a central grassy area. Tillo's tool corner sits at one side, the watering point at another. A stone path leads in from the entrance. There are no walls or barriers — just one flowing garden from path to far bed.

---

## Spatial Relationships

- The flower beds are always visible from the central grass area.
- Tillo's tool corner is always within sight of the beds.
- The watering point connects naturally to the nearest beds.
- The entrance path leads directly to the garden center.
- Trees provide shade at the garden edges.
- The soil is always visible between and around beds.

---

## Playable Areas

**Entrance Path** — Purpose: the garden approach. Visual identity: round stepping stones, green grass on sides. Important props: stones, grass. Typical use: arrival, first steps.

**Flower Beds** — Purpose: the heart of the garden — where planting happens. Visual identity: round low beds with soil and growing plants. Important props: beds, soil, plants, seeds. Typical use: planting, watering, observing growth.

**Central Grass** — Purpose: resting and observation area. Visual identity: soft green grass, open space. Important props: grass, shade from trees. Typical use: sitting, resting, watching.

**Tillo's Corner** — Purpose: tools and supplies. Visual identity: straw hat, watering can, shovel, seed box on wooden shelf. Important props: all tools. Typical use: tool selection, preparation.

**Watering Point** — Purpose: water source for the garden. Visual identity: near water source, damp soil. Important props: watering can, water. Typical use: watering, nurturing.

---

## Materials

Soil: soft matte brown, warm and touchable. Plants: soft green leaves, round flowers. Tools: natural wood, soft matte finish. Hat: soft straw texture. Watering can: smooth matte blue. All surfaces read as natural, soft, and child-safe. No metal sharpness, no glass, no hard edges anywhere.

---

## Lighting

Primary light is warm golden sunlight. The garden receives soft, even light with gentle shadows from trees. Morning brings warm golden tones; midday is bright; evening turns deeper gold. Shadows are soft and dappled through leaves — never hard, never dark.

---

## Colour Palette

Soil: warm brown (#8D6E63). Grass: soft green (#C8E6C9). Flowers: warm yellow (#FFD54F), red (#EF5350), pink (#F48FB1). Tools: natural wood (#A1887F). Hat: straw (#FFF9C4). Watering can: soft blue (#90CAF9). The palette stays within this warm, earthy, natural set.

---

## Scale

Everything is sized for small preschool children. The flower beds are low and accessible. The tools are small and toy-proportioned. The watering can is easy to hold. The shovel is tiny. The garden feels intimate, not sprawling — a few beds and a short path, not a large farm.

---

## Atmosphere

Warm. Natural. Patient. Nurturing. Calm. Every surface reads as soft and touchable. The mood is consistently warm and grounded — a place where children feel "good things grow here."

---

## Consistency Rules

- Flower beds are always round and low — never rectangular, never raised high.
- Soil is always soft and brown — never dark, never muddy.
- Tools are always round and wooden — never metal, never sharp.
- No thorns, no insects that could frighten, no dark weather.
- The garden is always clean and tended — never messy or overgrown.
- The colour palette stays warm and earthy across every generation.

---

## Generation Considerations

The garden must be generated as a warm, earthy space with round flower beds and soft soil — not as a wild jungle or formal park. Keep all shapes rounded. Keep the colour palette warm and earthy. The garden's identity — its patience, its warmth, its nurturing quality — must be preserved exactly across every generation.

---

## Colour Palette (Detailed)

| Asset ID | Element | Hex |
|----------|---------|-----|
| TG-SOFT-01 | Soil | #8D6E63 |
| TG-GRASS-01 | Grass | #C8E6C9 |
| TG-FLOWERS-01 | Yellow flowers | #FFD54F |
| TG-FLOWERS-02 | Red flowers | #EF5350 |
| TG-FLOWERS-03 | Pink flowers | #F48FB1 |
| TG-HAT-01 | Straw hat | #FFF9C4 |
| TG-CAN-01 | Watering can | #90CAF9 |

White balance: 5000K warm. Exposure: normal. Contrast: low. Saturation: medium.
No neon. No pure black. No cool shift.

---

## Reusable Assets

| Asset ID | Description |
|----------|-------------|
| TG-BED-01 | Round low flower bed with soil |
| TG-SOFT-01 | Soft brown garden soil |
| TG-HAT-01 | Straw hat (round, natural) |
| TG-CAN-01 | Blue round watering can |
| TG-SHOVEL-01 | Small wooden shovel |
| TG-SEED-BOX-01 | Wooden seed box |
| TG-FLOWERS-01 | Round yellow flowers |
| TG-FLOWERS-02 | Round red flowers |
| TG-FLOWERS-03 | Round pink flowers |
| TG-VEGGIES-01 | Vegetables (carrot, lettuce, tomato) |
| TG-PATH-01 | Round stepping stones |
| TG-GRASS-01 | Soft green grass |

---

## Framing

Flower beds always visible in every wide shot — they are the primary visual anchor.

| Shot | Max Character % | Beds Visible |
|------|:---------------:|:------------:|
| Wide establishing | 15–20% | Always |
| Medium single | 30–35% | Yes |
| Medium two characters | 40–45% | Yes |
| Close-up | 65–75% | Partial |

Emotional peak = wide shot showing full garden with growing plants.

---

## Navigation

Default flow: Entrance (path) → Central (grass) → Beds (planting) → Tools (preparation) → Watering (nurturing) → Exit.
The journey through the garden — from entry to planting to growth — should feel natural and unhurried.
**Alternative openings are permitted when story continuity requires them.**

---

## Generation Failures — Quick Reference

| Failure | Fix |
|---------|-----|
| Rectangular flower beds | Reject — round only |
| Sharp metal tools | Replace with wooden round tools |
| Thorns present | Reject — no thorns ever |
| Dark or muddy soil | Lighten to #8D6E63 range |
| Cold colour temperature | Warm to 5000K, recheck palette |
| Messy or overgrown garden | Clean and tend the garden |
| Sharp edges anywhere | Smooth all forms |
| Frightening insects | Remove or replace with friendly ones |

---

## Video Rules

| Element | Rule |
|---------|------|
| Plant growth | Very slow, 30 frame cycle |
| Water flow | Soft arc, 15 frame cycle |
| Wind | Gentle, constant, leaves sway |
| Camera speed | Max 3% frame/sec pan or tilt |
| Environmental rhythm | All movement on the same slow, patient breath |

Every animated frame passes the same QA as a still image.

---

## Visual Richness Layer

> See `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/WORLD_STANDARDS/GLOBAL_ENVIRONMENT_STANDARD.md` § Visual Richness Principle.
> Tillo's Garden must never be reduced to "a garden with plants."

This layer protects Tillo's Garden from becoming too plain. Keep the round
flower beds and earthy soil readable — add only the canon-approved charm
details below. Do not add random objects. Do not remove the patient,
nurturing, growing emotional identity.

**Allowed charm details:** TG-BED-01, the round low flower beds with visible
soft brown soil and healthy growing plants, is the primary landmark and
should anchor every wide shot. Tillo'nun köşesi — the tool corner where
TG-HAT-01 (straw hat), TG-CAN-01 (blue watering can), and TG-SEED-BOX-01
(wooden seed box) sit together — adds landmark and small prop charm.
TG-SOFT-01, the warm brown soil visible between beds, and TG-PATH-01, the
round stepping-stone entrance path, add surface charm. Gentle motion — the
slow patient growth-sway of plants and the soft arc of water from the
watering can — keeps the world feeling alive without adding clutter.

**Forbidden clutter:** thorny plants, sharp or metal tools, fast or hurried
movement, large or unsafe holes, mess or overgrowth, frightening insects,
sharp corners anywhere, and a cold or dim colour palette.

### Art Direction Layer (use together with Immutable Identity above)

```text
premium preschool animation, handcrafted toy-set feeling, warm earthy
nurturing atmosphere, storybook growth and patience beauty,
thumbnail-appeal composition, makes a child want to kneel down and plant
a seed
```

### Hero View Quality Tests

Before accepting a Hero View, it must pass:

1. **Silhouette Test** — recognisable as Tillo's Garden from the round flower beds and soil alone?
2. **Colour Test** — recognisable from the warm brown soil, green plants, and colourful flowers alone?
3. **Charm Test** — does it make a child want to kneel down and plant something here?

If any test fails, reject.

---

*Tillo's Garden — World Specification, aligned with Bible v3.1.*
*Visual Richness Layer added 4 Temmuz 2026.*
