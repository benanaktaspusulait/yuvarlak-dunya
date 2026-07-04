# Tree Hill — World Creation Specification

> Source of truth: `26-tree-hill-bible.md` (canonical, creative). This document
> is a production-oriented extraction for AI-assisted world generation. It does
> not replace the Bible and does not duplicate its storytelling, educational,
> character, or workflow content.

---

## Purpose

Tree Hill is a large, round, ancient forest hill that functions as the
spiritual heart of Pompom Hills. It is where stillness, wisdom, and nature
come alive through the simple beauty of old trees and quiet campfires.

---

## Immutable Identity

The following elements define the canonical identity of Tree Hill and must never change:

- Large, round hill with ancient round-crowned trees
- Deep green canopy (#66BB6A)
- Thick, old tree trunks
- Soft moss ground cover
- Safe campfire in clearing
- Wisdom stump for storytelling
- Open sky view point
- No sharp corners anywhere

---

## Visual Identity

A large, fully round hill with no rectangles, no straight edges, no sharp
corners anywhere. Soft matte surfaces give every element a natural,
handcrafted quality. The palette is deep and natural, centred on dark green
canopy with warm brown trunks and soft green moss. The overall feeling is a
"living toy forest" — approachable, wise, and visually simple enough for a
preschool audience to read instantly.

---

## World Layout

The world reads as one continuous ancient space rather than a set of separate
areas. The ancient gate leads through cathedral canopy to moss garden to camp
clearing to wisdom stump to sky view point. All zones are open and connected
without barriers between them.

---

## Spatial Relationships

- The ancient gate is always visible from the path.
- The cathedral canopy can be seen from the entrance.
- The moss garden is visible from the canopy.
- The camp clearing is visible from the moss garden.
- The wisdom stump is visible from the camp clearing.
- The sky view point provides a view of the entire hill.

---

## Playable Areas

**Ancient Gate** — Purpose: welcoming approach to the hill. Visual identity: largest ancient tree as gateway, round shapes dominant. Important props: ancient tree. Typical use: arrival, respect.

**Cathedral Canopy** — Purpose: towering tree ceiling zone. Visual identity: multiple round crowns creating natural cathedral, dappled light. Important props: tree canopies. Typical use: wonder, protection.

**Moss Garden** — Purpose: soft moss ground zone. Visual identity: thick green moss, smooth stones, gentle light. Important props: moss, stones. Typical use: resting, touching.

**Camp Clearing** — Purpose: campfire and gathering zone. Visual identity: round stone fire pit, safe contained fire, seating stones. Important props: fire pit, stones. Typical use: warmth, togetherness.

**Wisdom Stump** — Purpose: storytelling and contemplation zone. Visual identity: large round tree stump, natural seat. Important props: stump. Typical use: listening, learning.

**Sky View Point** — Purpose: viewing the sky. Visual identity: open canopy, stars visible, wide view. Important props: sky, stars. Typical use: imagination, wonder.

---

## Materials

Trees: ancient, round-crowned, thick trunks. Moss: soft, green, carpet-like.
Stones: smooth, round, warm grey. Fire: contained, safe, warm orange glow.
Stump: old, round, wise. No hard surfaces, no sharp edges, no artificial
materials anywhere. Everything reads as natural and safe.

---

## Lighting

Primary light filters through ancient canopy. Morning brings dappled golden
light; midday is shaded and cool; evening turns warm golden with long
shadows; night is firelight and starlight. Hill lighting is always natural,
filtering through leaves. Shadows are always soft — never hard, never dark.

---

## Colour Palette

Trees: deep green canopy (#66BB6A), warm brown trunks. Moss: soft green.
Stones: warm grey. Fire: warm orange. Stump: dark brown. The palette stays
within this deep, natural set across every zone.

---

## Scale

Everything is sized for a small preschool child. Trees are towering but
gentle — their round canopies create protective shelter. The hill is
intimate, not vast. The camp clearing is cozy. The hill never feels
overwhelming.

---

## Atmosphere

Wise. Soft. Safe. Ancient. Every surface reads as natural and gentle.
The mood is always calm and contemplative — full of stillness and gentle
light. The hill never feels dark or threatening.

---

## Consistency Rules

- The hill is always round, ancient, and wise — never dark, never young.
- Trees stay round-crowned and ancient across every generation.
- Moss stays soft and green.
- Fire stays contained and safe.
- No sharp corners, no dead trees, no scary elements.
- No dark or high-contrast lighting.
- The hill's core shape, colours, and proportions are never redesigned or reinterpreted.

---

## Generation Considerations

The hill must be generated as a single ancient, wise space with natural
elements, not as a dark or threatening forest — this is the defining trait
of this world and the most common failure point to watch for. Keep all shapes
rounded with no sharp corners anywhere. Keep the colour palette limited to
the deep natural set defined above. Favor a soft, matte, natural material
language over any glossy, metallic, or realistic rendering. Treat the
hill's shape, colours, and proportions as a fixed identity to preserve
exactly, not to reinterpret, across every generation.

---

## Visual Richness Layer

> See `02-WORLDS/GLOBAL_ENVIRONMENT_STANDARD.md` § Visual Richness Principle.
> Tree Hill must never be reduced to "an old forest with trees."

This layer protects Tree Hill from becoming too plain. Keep the world
readable and the ancient, round-crowned silhouette clear — add only the
canon-approved charm details below. Do not add random objects. Do not remove
the wise, still, protective emotional identity.

**Allowed charm details (use, do not omit):**
- TH-TREE-01, the largest ancient gateway tree at the Ancient Gate — primary landmark, always present in entrance shots
- the Wisdom Stump — large, round, old storytelling seat
- soft green moss carpet on the ground and stones in the Moss Garden
- dappled light filtering through the canopy onto the mossy floor
- round, warm-grey seating stones around the safe campfire
- scattered fallen leaves (TH-LEAVES-01) drifting onto the moss
- slow, gentle swaying of the ancient canopies overhead

**Forbidden clutter:** dark or threatening forest atmosphere, scary or sudden sounds, maze-like layout, sharp branches or thorny undergrowth, sharp corners or jagged rock edges, fast or chaotic movement, large crowds cluttering the clearing, unsafe or uncontained fire, metal or artificial surfaces, generic artificial-looking woodland.

### Art Direction Layer (use together with Technical Canon above)

```text
premium preschool animation, handcrafted toy-set feeling, ancient wise
forest atmosphere with dappled golden light, storybook beauty, thumbnail-
appeal composition, makes a child want to sit on the wisdom stump and
listen to a story by the fire
```

### Hero View Quality Tests

1. **Silhouette Test** — is the ancient gateway tree and cathedral canopy recognisable as Tree Hill from shape alone?
2. **Colour Test** — does the deep green canopy and warm brown trunk palette read as Tree Hill without any other detail?
3. **Charm Test** — does it make a child want to walk through the gateway tree and sit by the campfire with Tillo?

If any test fails, reject — see Generation Failures table above and
`26-tree-hill-bible.md` § Forbidden Over-Simplification.
