# Lulu's Greenhouse — World Creation Specification

> Source of truth: `08-lulus-greenhouse-bible.md` (canonical, creative). This document
> is a production-oriented extraction for AI-assisted world generation. It does
> not replace the Bible and does not duplicate its storytelling, educational,
> character, or workflow content.

---

## Purpose

Lulu's Greenhouse is a warm, humid indoor-outdoor space with rounded glass walls and lush green plants inside. It bridges indoor and outdoor worlds, teaching children about plant care in a controlled, cozy environment. The warm atmosphere and visible condensation create a unique sensory experience.

---

## Immutable Identity

The following elements define the canonical identity of Lulu's Greenhouse and must never change:

- Rounded glass panels with wooden frames
- Warm interior visible through transparent walls
- Lush green plants filling the interior
- Condensation droplets on glass
- Warm humid atmosphere
- Round pots on wooden shelves
- Natural wood materials throughout
- No broken glass, no wilting plants, no dark spaces
- Warm golden light from within

---

## Visual Identity

A warm greenhouse with rounded glass panels framed in natural wood. Inside, lush green plants fill every surface — on shelves, in pots, hanging from above. Condensation droplets cling to the glass, suggesting warmth and humidity. The interior glows with warm golden light. Everything reads as soft, rounded, and nurturing. The overall feeling is a "warm green sanctuary" — a place where plants thrive and children feel safe.

---

## World Layout

The world reads as one continuous greenhouse space. The exterior shows the rounded glass structure with green visible inside. Entering reveals one open interior with shelves, pots, and plants arranged naturally. There are no separate rooms — just one flowing green space from entrance to back wall.

---

## Spatial Relationships

- The exterior glass always reveals the green interior.
- The entrance connects directly to the main interior space.
- Shelves line the walls, holding pots and plants.
- The central area has larger plants and open space.
- The back wall has a window looking out to the garden.
- Condensation is always visible on glass panels.

---

## Playable Areas

**Exterior View** — Purpose: the greenhouse approach. Visual identity: rounded glass panels, green visible inside, wooden frame. Important props: glass, frame. Typical use: approaching, looking in.

**Entrance** — Purpose: threshold between garden and greenhouse. Visual identity: rounded wooden door frame, warm light inside. Important props: door frame. Typical use: entering, exiting.

**Interior Main** — Purpose: the heart of the greenhouse. Visual identity: shelves with plants, central open area, warm humid air. Important props: shelves, pots, plants. Typical use: plant care, observation, quiet activity.

**Glass Panel Area** — Purpose: condensation and humidity detail. Visual identity: glass with droplets, warm interior glow. Important props: glass, condensation. Typical use: looking through, discovering.

---

## Materials

Glass: rounded, soft reflections, condensation droplets. Wood: natural, warm, smooth matte. Pots: rounded, soft matte green. Plants: soft green leaves, round flowers. Floor: warm tile or stone. All surfaces read as warm, soft, and touchable. No sharp edges, no broken glass, no cold surfaces.

---

## Lighting

Primary light is warm golden sunlight filtering through glass panels. Interior has additional warm ambient light. The combination creates a soft, humid glow. Condensation on glass diffuses light gently. Shadows are very soft — never harsh, never dark.

---

## Colour Palette

Glass frame: natural wood (#A1887F). Plants: lush green (#66BB6A). Pots: soft green (#81C784). Interior warmth: golden (#FFF9C4). Condensation: clear with warm reflection. Floor: warm stone (#D7CCC8). The palette stays within this warm, green, golden set.

---

## Scale

Everything is sized for small children. Shelves are low and reachable. Pots are small and toy-sized. The greenhouse itself is modest — large enough for a few children to explore, small enough to feel cozy. The door is child-proportioned.

---

## Atmosphere

Warm. Humid. Green. Alive. Nurturing. Every surface reads as moist and vibrant. The mood is consistently warm and growing — a place where children feel "life is happening here."

---

## Consistency Rules

- Glass panels are always rounded — never rectangular, never sharp-edged.
- The interior is always warm and green — never dark, never cold.
- Condensation is always present on glass — never dry.
- Plants are always healthy and lush — never wilting, never dead.
- Wood is always natural and warm — never painted, never cold.
- No broken glass, no sharp edges, no dark corners.

---

## Generation Considerations

The greenhouse must be generated as a warm, humid space with rounded glass and lush plants — not as a cold conservatory or industrial structure. Keep all shapes rounded. Keep the colour palette warm and green. The greenhouse's identity — its warmth, its humidity, its nurturing quality — must be preserved exactly across every generation.

---

## Colour Palette (Detailed)

| Asset ID | Element | Hex |
|----------|---------|-----|
| LG-FRAME-01 | Glass frame | #A1887F |
| LG-PLANTS-01 | Plants | #66BB6A |
| LG-POT-01 | Pots | #81C784 |
| LG-FLOOR-01 | Floor | #D7CCC8 |
| Interior warmth | Golden light | #FFF9C4 |

White balance: 4500K warm. Exposure: normal. Contrast: low. Saturation: medium.
No neon. No pure black. No cool shift.

---

## Reusable Assets

| Asset ID | Description |
|----------|-------------|
| LG-GLASS-01 | Rounded glass panel |
| LG-FRAME-01 | Natural wooden frame |
| LG-POT-01 | Rounded green pot |
| LG-SHELF-01 | Wooden shelf for plants |
| LG-CAN-01 | Small watering can |
| LG-PLANTS-01 | Lush green plants |
| LG-FLOWERS-01 | Greenhouse flowers |
| LG-CONDENSATION-01 | Glass condensation droplets |
| LG-DOOR-01 | Rounded wooden door frame |
| LG-FLOOR-01 | Warm stone floor |

---

## Framing

Glass always visible in exterior shots — it is the primary visual anchor. Interior shots show plants as central element.

| Shot | Max Character % | Glass Visible |
|------|:---------------:|:-------------:|
| Wide establishing | 15–20% | Always |
| Medium single | 30–35% | Yes |
| Medium two characters | 40–45% | Yes |
| Interior wide | 40–50% | From inside |
| Close-up | 65–75% | Partial |

Emotional peak = interior shot showing warm green abundance.

---

## Navigation

Default flow: Exterior (approach) → Entrance (threshold) → Interior (living) → Glass Detail (discovery) → Exit.
The journey from outside to inside — the temperature and humidity change — should feel natural and welcoming.
**Alternative openings are permitted when story continuity requires them.**

---

## Generation Failures — Quick Reference

| Failure | Fix |
|---------|-----|
| Rectangular glass panels | Reject — rounded only |
| Broken or cracked glass | Reject — never broken |
| Dark or cold interior | Add warm light, recheck palette |
| Wilting or dead plants | Replace with healthy plants |
| No condensation on glass | Add condensation droplets |
| Sharp edges anywhere | Smooth all forms |
| Cold colour temperature | Warm to 4500K, recheck palette |
| Dry atmosphere | Add humidity effects |

---

## Video Rules

| Element | Rule |
|---------|------|
| LG-PLANTS-01 movement | Gentle sway, 20 sec cycle |
| LG-CONDENSATION-01 | Slow droplet formation, 25 sec |
| Water drip | Soft, 15 sec cycle |
| Camera speed | Max 3% frame/sec pan or push |
| Environmental rhythm | All movement on the same warm, humid breath |

Every animated frame passes the same QA as a still image.

---

## Visual Richness Layer

> See `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/WORLD_STANDARDS/GLOBAL_ENVIRONMENT_STANDARD.md` § Visual Richness Principle.
> Lulu's Greenhouse must never be reduced to "a glass building with plants."

This layer protects Lulu's Greenhouse from becoming too plain. Keep the
rounded glass silhouette clear and add only the canon-approved charm details
below. Do not add random objects. Do not remove the warm, humid, nurturing
emotional identity.

**Allowed charm details:** the LG-GLASS-01 rounded glass panels in their
LG-FRAME-01 wooden frame stay the iconic landmark, always revealing the green
interior. Surface charm comes from LG-CONDENSATION-01 droplets on the glass
and the warm golden interior glow (#FFF9C4). Small prop charm comes from
LG-POT-01 round pots lined up on LG-SHELF-01 shelves and the LG-CAN-01
watering can. Motion charm comes from the gentle sway of LG-PLANTS-01 leaves.

**Forbidden clutter:** broken or cracked glass, wilting or dead plants, a
dark unlit interior, sharp corners or edges, a cold blue colour cast, a dry
atmosphere with no condensation, a generic industrial greenhouse or cold
conservatory look, and any text, logos, or modern signage.

### Art Direction Layer (use together with Technical Canon above)

```text
premium preschool animation, handcrafted toy-set feeling, warm humid
glasshouse atmosphere with glowing condensation, storybook beauty,
thumbnail-appeal composition, makes a child want to press their nose
against the glass and peek at the green world inside
```

### Hero View Quality Tests

Before accepting a Hero View, it must pass:

1. **Silhouette Test** — recognisable as Lulu's Greenhouse from the rounded glass-and-frame shape alone?
2. **Colour Test** — recognisable from the warm golden-and-green palette alone?
3. **Charm Test** — does it make a child want to peek through the glass at the plants?

If any test fails, reject.

---

*Lulu's Greenhouse — World Specification, aligned with Bible v3.1.*
*Visual Richness Layer added 4 Temmuz 2026.*
