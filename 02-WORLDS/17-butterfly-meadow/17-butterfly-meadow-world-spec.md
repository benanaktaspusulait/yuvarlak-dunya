# Butterfly Meadow — World Creation Specification

> Source of truth: `17-butterfly-meadow-bible.md` (canonical, creative). This document
> is a production-oriented extraction for AI-assisted world generation. It does
> not replace the Bible and does not duplicate its storytelling, educational,
> character, or workflow content.

---

## Purpose

Butterfly Meadow is a wide, round green meadow filled with colourful flowers
and dancing butterflies. It is where wonder, nature, and gentle discovery
come alive through the simple beauty of butterflies and blossoms.

---

## Immutable Identity

The following elements define the canonical identity of Butterfly Meadow and must never change:

- Wide, round green meadow
- Colourful round flowers (red, yellow, pink, purple)
- Dancing butterflies (pink, purple, yellow)
- Soft, waving grass
- Round trees at edges
- Soft rounded hills
- Warm golden sunlight
- No sharp corners anywhere

---

## Visual Identity

A wide, fully open meadow with no rectangles, no straight edges, no sharp
corners anywhere. Soft matte surfaces give every element a natural,
handcrafted quality. The palette is warm and pastel, centred on green grass
with colourful flowers and soft butterflies. The overall feeling is a
"living toy meadow" — approachable, magical, and visually simple enough for
a preschool audience to read instantly.

---

## World Layout

The world reads as one continuous natural space rather than a set of separate
areas. The entrance leads into the meadow, which flows naturally from
butterfly dance zone to flower garden to wind path to observation hill to
quiet rest spot. All zones are open and connected without barriers between
them.

---

## Spatial Relationships

- The meadow entrance is visible from the path.
- The butterfly dance zone can be seen from the observation hill.
- The flower garden is visible from the butterfly zone.
- The wind path connects all areas naturally.
- The observation hill provides a view of the entire meadow.
- The quiet rest spot is visible from the hill but feels separate.

---

## Playable Areas

**Meadow Entrance** — Purpose: welcoming approach to the meadow. Visual identity: colourful flowers, soft path. Important props: flowers, path. Typical use: arrival, first butterfly sighting.

**Butterfly Dance Zone** — Purpose: where butterflies dance and fly. Visual identity: butterflies in soft pastel colours, warm sunlight. Important props: butterflies. Typical use: observation, wonder.

**Flower Garden** — Purpose: colourful flower discovery zone. Visual identity: round flowers in red, yellow, pink, purple. Important props: flowers. Typical use: colour exploration, scent.

**Wind Path** — Purpose: natural wind corridor. Visual identity: waving grass, floating leaves, gentle breeze. Important props: grass, leaves. Typical use: movement, freedom.

**Observation Hill** — Purpose: viewing the entire meadow. Visual identity: soft rounded hill, panoramic view. Important props: hill, view. Typical use: perspective, calm.

**Quiet Rest Spot** — Purpose: rest and quiet observation. Visual identity: smooth stones under tree shade. Important props: stones, tree. Typical use: resting, butterfly watching.

---

## Materials

Grass: soft, waving, green. Flowers: round, soft, colourful. Butterflies:
thin, delicate, pastel. Trees: round, wide, providing shade. Stones: smooth,
round, grey. No hard surfaces, no sharp edges, no artificial materials
anywhere. Everything reads as natural and safe.

---

## Lighting

Primary light is warm golden sunlight. Morning brings soft golden light;
midday is bright and even; evening turns golden-orange with longer soft
shadows; night is soft moonlight with butterflies sleeping. Outdoor lighting
is always natural daylight. Shadows are always soft — never hard, never dark.

---

## Colour Palette

Grass: soft green. Flowers: red, yellow, pink, purple. Butterflies: pink,
purple, yellow. Trees: green with brown trunks. Stones: warm grey. The
palette stays within this soft, pastel set across every zone.

---

## Scale

Everything is sized for a small preschool child. The meadow is wide but
intimate — open enough to walk and explore, but contained enough to feel
safe. Flowers are child-height. Butterflies fly at eye level. Hills are
gentle and climbable.

---

## Atmosphere

Warm. Soft. Safe. Magical. Every surface reads as natural and gentle.
The mood is always wondrous and inviting — full of gentle movement and
quiet beauty. The meadow never feels threatening or overwhelming.

---

## Consistency Rules

- The meadow is always wide, round, and green — never narrow, never brown.
- Flowers stay round and colourful (red, yellow, pink, purple).
- Butterflies stay pastel (pink, purple, yellow) and fly slowly.
- Grass stays soft and waving.
- No sharp corners, no dark colours, no threatening insects.
- No dark or high-contrast lighting.
- The meadow's core shape, colours, and proportions are never redesigned or reinterpreted.

---

## Generation Considerations

The meadow must be generated as a single wide natural space with magical
elements, not as a confined or threatening landscape — this is the defining
trait of this world and the most common failure point to watch for. Keep all
shapes rounded with no sharp corners anywhere. Keep the colour palette
limited to the soft pastel set defined above. Favor a soft, matte, natural
material language over any glossy, metallic, or realistic rendering. Treat
the meadow's shape, colours, and proportions as a fixed identity to preserve
exactly, not to reinterpret, across every generation.

---

## Visual Richness Layer

> See `02-WORLDS/GLOBAL_ENVIRONMENT_STANDARD.md` § Visual Richness Principle.
> Butterfly Meadow must never be reduced to "a flower field." Its identity is
> the butterflies themselves, not the flowers.

This layer protects Butterfly Meadow from becoming too plain. Keep the wide,
round meadow silhouette readable and the pastel flower carpet clear — add
only the canon-approved charm details below. Do not add random objects. Do
not remove the wonder-and-magic emotional identity, and never let the
butterflies become incidental to the flowers.

**Allowed charm details:** BM-BUTTERFLY-01, a drifting cloud of at least 5-6
pastel butterflies (pink, purple, yellow) dancing in slow curved paths just
above the flowers, is the primary landmark and must be visible in every wide
shot. BM-FLOWERS-01, the pastel flower carpet the butterflies dance above,
and the soft rolling meadow silhouette with low hills at the edges add
landmark and surface charm, along with gentle grass-wave patterns rippling
beneath the butterfly flight paths. A soft round stepping-stone path winding
through the flowers and one or two low shade trees at the meadow's edge are
the central reusable small props. Gentle motion — the slow, curved, looping
butterfly flight paths and the gentle sway of BM-FLOWERS-01 in the breeze —
keeps the world feeling alive without adding clutter.

**Forbidden clutter:** a meadow with too few or no visible butterflies, fast
or jittery butterfly movement, dark, black, or harsh-coloured butterflies,
scary insects, dense or cluttered flower coverage that hides the
butterflies, sharp corners anywhere, and a dull or desaturated palette.

### Art Direction Layer (use together with Immutable Identity above)

```text
premium preschool animation, handcrafted toy-set feeling, enchanted
butterfly-dance meadow atmosphere, storybook beauty, thumbnail-appeal
composition, makes a child want to stand very still and watch the
butterflies dance
```

### Hero View Quality Tests

Before accepting a Hero View, it must pass:

1. **Silhouette Test** — recognisable as Butterfly Meadow from the wide rolling meadow shape alone?
2. **Colour Test** — recognisable from the pastel flower carpet and pastel butterfly colours alone?
3. **Charm Test** — does it make a child want to stand very still and watch the butterflies dance?

If any test fails, reject.
