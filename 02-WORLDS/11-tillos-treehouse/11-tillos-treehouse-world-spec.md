# Tillo's Treehouse — World Creation Specification

> Source of truth: `11-tillos-treehouse-bible.md` (canonical, creative). This document
> is a production-oriented extraction for AI-assisted world generation. It does
> not replace the Bible and does not duplicate its storytelling, educational,
> character, or workflow content.

---

## Purpose

Tillo's Treehouse is a warm wooden treehouse nestled in a large tree, connected to the Little Forest by a low wooden bridge. It provides verticality and perspective contrast to ground-level worlds, teaching children about heights safely through warm wooden textures and secure structures.

---

## Immutable Identity

The following elements define the canonical identity of Tillo's Treehouse and must never change:

- Round wooden treehouse in a large tree
- Warm honey-toned wood (#FFCC80)
- Round windows with warm interior light
- Low wooden bridge connecting to forest
- Secure railings on bridge and treehouse
- Large tree trunk supporting structure
- Green leaves framing the scene
- No dangerous heights without protection
- No broken or unstable structures
- No sharp nails or splinters

---

## Visual Identity

A warm round wooden treehouse nestled in the branches of a large tree. The honey-toned wood glows in natural sunlight filtering through leaves. A low wooden bridge with secure railings connects the treehouse to the forest floor. Round windows emit warm interior light. Everything reads as safe, sturdy, and inviting — a place where heights feel like adventure, not danger. The overall feeling is a "safe elevated retreat" — high enough to see the world, secure enough to feel at home.

---

## World Layout

The world reads as one continuous upward journey. The forest floor leads to the ladder, which leads to the bridge, which leads to the treehouse. From the treehouse, windows provide panoramic views. There are no separate structures — just one flowing vertical space from ground to canopy.

---

## Spatial Relationships

- The ladder connects the forest floor to the bridge level.
- The bridge connects the treehouse to the surrounding forest.
- The treehouse interior is visible through round windows.
- The windows maintain visual relationships with the forest, sky, and ground below.
- The tree trunk supports the entire structure visibly.
- Leaves frame every exterior view.

---

## Playable Areas

**Forest Floor** — Purpose: the base of the tree, where the journey begins. Visual identity: large tree trunk, ladder base, green leaves. Important props: trunk, ladder. Typical use: arrival, looking up, beginning ascent.

**Bridge** — Purpose: the transition between forest and treehouse. Visual identity: low wooden bridge with secure railings, leaves on sides. Important props: bridge, railings. Typical use: crossing, looking down, transition.

**Treehouse Interior** — Purpose: the heart of the treehouse, one continuous room. Visual identity: warm honey wood, round windows, soft cushions. Important props: windows, cushions, small shelf. Typical use: resting, reading, looking out.

**Window View** — Purpose: the panoramic observation point. Visual identity: round window framing forest and sky. Important props: window, view. Typical use: observing, discovering, quiet contemplation.

---

## Materials

Treehouse: warm honey-toned wood, smooth and rounded. Bridge: natural wood with secure railings. Ladder: sturdy wood with rounded rungs. Windows: round with warm frames. All surfaces read as natural, warm, and safe. No metal, no sharp edges, no splinters, no nails visible.

---

## Lighting

Primary light is natural sunlight filtering through leaves, creating dappled patterns on the treehouse and bridge. Interior light is warm and golden. Shadows are soft and green-tinted from the leaf canopy. The overall feeling is natural, warm, and forest-filtered.

---

## Colour Palette

| Asset ID | Element | Hex |
|----------|---------|-----|
| TT-HOUSE-01 | Treehouse wood | #FFCC80 |
| TT-TRUNK-01 | Tree trunk | #795548 |
| TT-LEAVES-01 | Leaves | #66BB6A |
| TT-BRIDGE-01 | Bridge wood | #A1887F |
| Interior light | Warm glow | #FFF9C4 |
| Sky | Open sky | #E3F2FD |

White balance: 5000K natural. Exposure: normal. Contrast: low. Saturation: medium.
No neon. No pure black. No cool shift.

---

## Scale

Everything is sized for small preschool children. The treehouse is modest — large enough for a few children, small enough to feel cozy. The bridge is low with secure railings. The ladder has rounded rungs at child-friendly intervals. The windows are at child eye level. Heights feel elevated but never dangerous.

---

## Atmosphere

Safe. Elevated. Natural. Adventurous. Warm. Every surface reads as sturdy and secure. The mood is consistently adventurous but reassuring — a place where children feel "I'm high up but I'm safe."

---

## Consistency Rules

- The treehouse is always round and wooden — never rectangular, never metal.
- The bridge is always low with secure railings — never high without protection.
- The wood is always warm honey-toned — never painted, never cold.
- Leaves are always present, framing the scene — never bare.
- No sharp edges, no visible nails, no broken structures.
- Heights always feel secure with visible safety features.

---

## Generation Considerations

The treehouse must be generated as a warm, sturdy wooden structure in a large tree — not as a fragile platform or dangerous perch. Keep all shapes rounded. Keep the wood warm and natural. The treehouse's identity — its safety, its warmth, its elevated perspective — must be preserved exactly across every generation.

---

## Colour Palette (Detailed)

| Asset ID | Element | Hex |
|----------|---------|-----|
| TT-HOUSE-01 | Treehouse | #FFCC80 |
| TT-TRUNK-01 | Trunk | #795548 |
| TT-LEAVES-01 | Leaves | #66BB6A |
| TT-BRIDGE-01 | Bridge | #A1887F |
| TT-WINDOW-01 | Window frame | #FFCC80 |
| Interior | Warm light | #FFF9C4 |

White balance: 5000K natural. Exposure: normal. Contrast: low. Saturation: medium.
No neon. No pure black. No cool shift.

---

## Reusable Assets

| Asset ID | Description |
|----------|-------------|
| TT-HOUSE-01 | Round wooden treehouse |
| TT-BRIDGE-01 | Low wooden bridge |
| TT-LADDER-01 | Sturdy wooden ladder |
| TT-WINDOW-01 | Round window |
| TT-DOOR-01 | Round wooden door |
| TT-RAILING-01 | Secure wooden railing |
| TT-CUSHION-01 | Interior cushion |
| TT-SHELF-01 | Small wooden shelf |
| TT-TRUNK-01 | Large tree trunk |
| TT-LEAVES-01 | Green leaves |

---

## Framing

Treehouse always visible in wide shots — it is the primary visual anchor. Bridge visible in transition shots.

| Shot | Max Character % | Treehouse Visible |
|------|:---------------:|:-----------------:|
| Wide establishing | 15–20% | Always |
| Medium single | 30–35% | Yes |
| Medium two characters | 40–45% | Yes |
| Bridge crossing | 40–50% | Yes |
| Close-up | 65–75% | Partial |

Emotional peak = wide shot showing treehouse in tree with forest backdrop.

---

## Navigation

Default flow: Forest Floor (base) → Ladder (ascent) → Bridge (crossing) → Treehouse (arrival) → Window (observation) → Exit.
The upward journey — the change in perspective — should feel natural and exciting.
**Alternative openings are permitted when story continuity requires them.**

---

## Generation Failures — Quick Reference

| Failure | Fix |
|---------|-----|
| Dangerous height without protection | Add railings, secure structure |
| Broken or unstable structure | Repair or regenerate |
| Sharp nails or splinters | Smooth all wood surfaces |
| Dark or scary interior | Add warm light |
| Cold colour temperature | Warm to 5000K, recheck palette |
| No leaves present | Add leaf canopy |
| Metal structures present | Replace with wood |
| Sharp edges anywhere | Smooth all forms |

---

## Video Rules

| Element | Rule |
|---------|------|
| TT-LEAVES-01 movement | Gentle sway, 20 sec cycle |
| TT-BRIDGE-01 movement | Very slight sway, 15 sec |
| Wind through leaves | Constant, soft |
| Camera speed | Max 3% frame/sec pan or tilt |
| Environmental rhythm | All movement on the same natural breath |

Every animated frame passes the same QA as a still image.

---

## Visual Richness Layer

> See `02-WORLDS/GLOBAL_ENVIRONMENT_STANDARD.md` § Visual Richness Principle.
> Tillo's Treehouse must never be reduced to "a house in a tree."

This layer protects Tillo's Treehouse from becoming too plain. Keep the
round honey-wood treehouse readable and the height/bridge silhouette clear —
add only the canon-approved charm details below. Do not add random objects.
Do not remove the safe-adventure, elevated-retreat emotional identity.

**Allowed charm details:** TT-HOUSE-01, the round honey-wood treehouse with
its round window glowing warm from inside, is the primary landmark and must
be visible in every exterior wide shot. TT-BRIDGE-01, the low wooden bridge
with safe railings connecting to Little Forest, is the secondary landmark
that gives the world its height and crossing feeling. TT-LEAVES-01
surrounding and partially framing the treehouse, plus dappled sunlight
patterns filtering through the canopy onto the treehouse walls, add surface
charm. TT-LADDER-01 leading up to the bridge, and TT-CUSHION-01 /
TT-SHELF-01 glimpsed through the round window, are the reusable small
props. Gentle motion — TT-LEAVES-01 swaying in the breeze and the light
creak and soft bounce of TT-BRIDGE-01 as it's crossed — keeps the world
feeling alive without adding clutter.

**Forbidden clutter:** a treehouse shown with no visible bridge or height
context, an unsafe-looking drop or missing railings, a broken or
unstable-looking structure, sharp nails or splinters, a dark or scary
interior, sharp corners anywhere, and modern building materials.

### Art Direction Layer (use together with Immutable Identity above)

```text
premium preschool animation, handcrafted toy-set feeling, cozy elevated
adventure atmosphere, storybook safe-treehouse beauty, thumbnail-appeal
composition, makes a child want to cross the little bridge and climb up
```

### Hero View Quality Tests

Before accepting a Hero View, it must pass:

1. **Silhouette Test** — recognisable as Tillo's Treehouse from the round treehouse in the tree with its connecting bridge alone?
2. **Colour Test** — recognisable from the honey-wood tones, green leaves, and warm interior glow alone?
3. **Charm Test** — does it make a child want to cross the bridge and climb up into the trees?

If any test fails, reject.
