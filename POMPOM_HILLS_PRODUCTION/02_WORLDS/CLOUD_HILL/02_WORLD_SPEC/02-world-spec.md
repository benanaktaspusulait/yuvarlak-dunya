# Cloud Hill — World Specification

> This specification defines the canonical Cloud Hill world.
> Primary visual reference: the uploaded reference image.
> This document is a dense generation instruction set.
> **If this specification and the uploaded reference image disagree, follow the uploaded reference image.**

---

## Canonical Reference

```
Primary Reference : The uploaded reference image supplied with this specification
Status            : Canon — accepted 3 July 2026
Overrides         : All previous text-only descriptions of hill shape,
                    cloud layout, stone position, and sky ratio
```

This image is the visual definition of Cloud Hill. Every future generation
must match the silhouette, sky composition, stone position, and colour
register of this image. If a generated hill does not immediately resemble
the uploaded reference image on first glance, reject it.

---

## Identity

- **The uploaded reference image is the visual source of truth.** Text descriptions
  below are secondary to the image.
- One perfectly smooth grass dome with a broad rounded summit — silhouette
  must match the uploaded reference image exactly.
- CH-STONE-01 visible at the summit, slightly right of centre — this stone
  is the primary visual anchor of the summit. When the summit is visible,
  the stone should normally be visible unless deliberately hidden by framing.
- Sky dominates every wide composition — approximately 62%.
- Three rounded white clouds define the sky: large upper-left, small centre,
  medium upper-right near the sun.
- Sun in upper-right, soft — not a hard disc.
- Pastel hill silhouettes on the horizon — low, not dominant.
- No structures, no fences, no modern objects. No thorns, no sharp stones.
- Warm pastel palette. Handcrafted, soft, never photorealistic.

---

## Hero View Composition

The uploaded reference image defines the canonical composition. All wide shots derive from it.

| Zone | Frame % |
|------|:-------:|
| Sky | 62% |
| Horizon band (CH-HILL-BG) | 8% |
| Ground (CH-GRASS-01) | 30% |

- Hill fills the entire width of the frame — dome visible edge to edge
- Summit centred horizontally
- CH-STONE-01 positioned slightly right of centre on the summit
- Three clouds visually balanced: large upper-left / small centre / medium upper-right
- Sun upper-right, soft glow — not clipping
- Horizon at 35–40% from frame bottom

---

## Colour Palette

| Asset ID | Element | Hex |
|----------|---------|-----|
| CH-GRASS-01 | Grass | #A5D6A7 — note: uploaded reference image reads slightly brighter; both acceptable |
| CH-SKY-LOW | Sky at horizon | #E3F2FD |
| CH-SKY-HIGH | Sky at zenith | #BBDEFB |
| CH-CLOUD-A | Large cloud (upper left) | #F5F5F5 |
| CH-CLOUD-B | Medium cloud (upper right) | #F5F5F5 |
| CH-CLOUD-C | Small cloud (centre) | #F5F5F5 |
| CH-STONE-01 | Sitting stone | #ECEFF1 |
| CH-DAISY-01 | Daisy petals | #FFFFFF, centre #FFF59D |
| CH-HILL-BG | Distant horizon hills | #C8E6C9 |

White balance: 5500K warm. Exposure: +0.3 lifted. Contrast: low. Saturation: medium-low.
No neon. No pure black. No cool shift in daytime.

---

## Reusable Assets

| Asset ID | Description |
|----------|-------------|
| CH-HILL-DOME | Full-width smooth grass dome — silhouette must match the uploaded reference image |
| CH-SUMMIT | Broad rounded plateau at top |
| CH-STONE-01 | Flat round grey stone, 40 cm × 15 cm, summit right-of-centre — **primary visual anchor** |
| CH-CLOUD-A | Large rounded cumulus, upper left |
| CH-CLOUD-B | Medium cumulus, upper right near sun |
| CH-CLOUD-C | Small cumulus, centre sky |
| CH-DAISY-01 | Sparse daisy clusters on hillside, 3–5 per group |
| CH-GRASS-01 | Short even plush grass, matte surface |
| CH-HILL-BG | Low pastel hill silhouettes on horizon |
| CH-WIND-AMB | Soft continuous wind audio, low breathy tone |
| CH-BIRD-01 | Single distant melodic bird call |

---

## Framing

Sky behind character in every shot — never ground as background.
Horizon always visible in wide shots — never cut off.

| Shot | Max Character % | Sky Visible |
|------|:---------------:|:-----------:|
| Wide establishing | 15–20% | 60%+ |
| Medium single | 30–35% | 40%+ |
| Medium two characters | 40–45% | 35%+ |
| Close-up | 65–75% | 20%+ (sky as bg, never bokeh) |

Emotional peak = pull back, not push in.

---

## Navigation

Default flow: Entry (lower hillside) → Climb → Summit Arrival → Observation → Exit.
Summit arrival — sky opening moment — must not be skipped.
**Alternative openings are permitted when story continuity requires them.**

---

## Generation Failures — Quick Reference

| Failure | Fix |
|---------|-----|
| Hill silhouette does not match uploaded reference image | Reject — regenerate referencing the uploaded reference image |
| Sky < 60% of frame | Reframe upward or regenerate |
| Grey or dark clouds | Reject — CH-CLOUD must be fully white |
| Jagged hill silhouette | Reject — smooth dome only |
| Modern object anywhere in frame | Reject — no structures |
| Grass not within acceptable range of #A5D6A7 | Correct colour or regenerate |
| Cloud count ≠ 3 | Regenerate — exactly 3 clouds matching CH-CLOUD-A/B/C layout |
| CH-STONE-01 missing from summit shot | Add stone or regenerate |
| Cool colour temperature | Warm to 5500K, recheck palette |

---

## Video Rules

| Element | Rule |
|---------|------|
| CH-CLOUD movement | Left → right, ~5% frame width/sec, continuous |
| CH-GRASS-01 movement | Gentle wave, 3–4 sec cycle, tips only |
| Wind | Constant, soft — no gusts, no direction change mid-scene |
| Camera speed | Max 5% frame/sec pan or tilt |
| Environmental rhythm | Clouds, grass, camera all move on the same slow breath |

Every animated frame passes the same QA as a still image.

---

## Visual Richness Layer

> See `POMPOM_HILLS_PRODUCTION/02_WORLDS/GLOBAL_ENVIRONMENT_STANDARD.md` § Visual Richness Principle.
> Cloud Hill must never be reduced to "a hill and some clouds."

This layer protects Cloud Hill from becoming too plain. Keep the world
readable and the dome silhouette clear — add only the canon-approved charm
details below. Do not add random objects. Do not remove the sky-dominant,
cloud-watching emotional identity.

**Allowed charm details (use, do not omit):**
- CH-STONE-01, the summit sitting/viewing stone — primary landmark, always present in summit shots
- gentle curved climb path on the hillside
- soft cloud-shadow patches on the grass
- CH-DAISY-01 sparse wildflower clusters
- tiny rounded pebbles along the path
- soft hazy horizon hills in the background

**Forbidden clutter:** empty plain hill with no landmark, generic meadow, harsh mountain, cliffs, dense flower fields (that is Flower Hill), houses or village elements on the summit, dark storm clouds, realistic landscape textures.

### Art Direction Layer (use together with Technical Canon above)

Technical Canon = geometry, landmarks, colours, scale, lighting, forbidden
elements (defined above in this spec). Add this Art Direction Layer whenever
writing or regenerating a Hero View prompt — technical-only prompts tend to
produce safe but boring hills:

```text
premium preschool animation, handcrafted toy-set feeling, soft rounded
summit stone with visible texture, warm inviting atmosphere, storybook
sky-watching beauty, thumbnail-appeal composition, makes a child want to
climb up and sit on the stone
```

### Hero View Quality Tests

Before accepting a Hero View, it must pass:

1. **Silhouette Test** — recognisable as Cloud Hill from the dome shape alone?
2. **Colour Test** — recognisable from the pastel sky/grass palette alone?
3. **Charm Test** — does it make a child want to climb up and look at the sky?

If any test fails, reject — see Generation Failures table above and
`01-world-bible.md` § Forbidden Over-Simplification.

---

*Cloud Hill — World Specification, aligned with Bible v5.3.*
*Visual Richness Layer added 4 Temmuz 2026.*
