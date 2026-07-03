# Cloud Hill — World Specification

> Aligned with Bible v5.2.
> Source of truth: `01-world-bible.md`. Primary visual reference: `00-hero-view.png`.
> This document is a dense generation instruction set — not a summary of the Bible.
> **Whenever text and image appear to disagree, the Hero View takes precedence.**

---

## Canonical Reference

```
Primary Reference : 00-hero-view.png — Cloud Hill Hero View v1
Status            : Canon — accepted 3 July 2026
Overrides         : All previous text-only descriptions of hill shape,
                    cloud layout, stone position, and sky ratio
```

This image is the visual definition of Cloud Hill. Every future generation
must match the silhouette, sky composition, stone position, and colour
register of this image. If a generated hill does not immediately resemble
the Hero View silhouette on first glance, reject it.

---

## Identity

- **The Canon Hero View is the visual source of truth.** Text descriptions
  below are secondary to the image.
- One perfectly smooth grass dome with a broad rounded summit — silhouette
  must match the Canon Hero View exactly.
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

The Canon Hero View defines the canonical composition. All wide shots derive from it.

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
| CH-GRASS-01 | Grass | #A5D6A7 — note: Hero View reads slightly brighter; both acceptable |
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
| CH-HILL-DOME | Full-width smooth grass dome — silhouette must match Canon Hero View |
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
| Hill silhouette does not match Hero View | Reject — regenerate referencing Canon Hero View |
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
