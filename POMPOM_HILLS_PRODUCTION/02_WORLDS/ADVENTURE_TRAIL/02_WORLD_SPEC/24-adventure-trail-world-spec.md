# Adventure Trail — World Creation Specification

> Source of truth: `24-adventure-trail-bible.md` (canonical, creative). This document
> is a production-oriented extraction for AI-assisted world generation. It does
> not replace the Bible and does not duplicate its storytelling, educational,
> character, or workflow content.

---

## Purpose

Adventure Trail is a long, winding, round-stoned path that functions as the
connective heart of Pompom Hills. It is where journeys, transitions, and
discovery come alive through the simple joy of walking and exploring.

---

## Immutable Identity

The following elements define the canonical identity of Adventure Trail and must never change:

- Long, winding path with round stones
- Diverse terrain (forest, meadow, hill, creek)
- Warm natural sunlight
- Soft, natural surroundings
- Safe, well-marked pathway
- Round marker stones along edges
- Gentle curves inviting exploration
- No sharp corners anywhere

---

## Visual Identity

A long, fully winding trail with no rectangles, no straight edges, no sharp
corners anywhere. Soft matte surfaces give every element a natural,
handcrafted quality. The palette is warm and earthy, centred on grey stones
with green nature and warm sunlight. The overall feeling is a "living toy
trail" — approachable, adventurous, and visually simple enough for a preschool
audience to read instantly.

---

## World Layout

The world reads as one continuous journey rather than a set of separate
areas. The trail head leads through forest, meadow, hill, and creek to the
destination view. All zones are open and connected as one winding path.

---

## Spatial Relationships

- The trail head is visible from the starting point.
- The forest section can be seen from the trail head.
- The meadow crossing is visible from the forest edge.
- The hill climb provides a view of the entire trail.
- The creek bridge connects to the destination view.
- The destination view provides a panoramic view of all connected worlds.

---

## Playable Areas

**Trail Head** — Purpose: starting point of the journey. Visual identity: round welcome stone, first bend visible. Important props: welcome stone. Typical use: arrival, beginning.

**Forest Section** — Purpose: path through trees. Visual identity: round trees, dappled light, soft shadows. Important props: trees, stones. Typical use: discovery, shade.

**Meadow Crossing** — Purpose: open grassland crossing. Visual identity: green grass, colourful flowers, wide sky. Important props: grass, flowers. Typical use: freedom, running.

**Hill Climb** — Purpose: ascending to higher ground. Visual identity: rounded hill, stone steps, panoramic view. Important props: hill, steps. Typical use: climbing, achievement.

**Creek Bridge** — Purpose: crossing over water. Visual identity: round stone bridge, clear water below. Important props: bridge, water. Typical use: crossing, pausing.

**Destination View** — Purpose: panoramic viewpoint. Visual identity: wide view of all connected worlds. Important props: viewpoint, panorama. Typical use: achievement, perspective.

---

## Materials

Stones: smooth, round, warm grey. Soil: soft, natural brown. Grass: soft,
green. Trees: round, leafy. Water: clear, flowing. Bridge: smooth stone.
No hard surfaces, no sharp edges, no artificial materials anywhere.
Everything reads as natural and safe.

---

## Lighting

Primary light is warm natural sunlight. Morning brings soft golden light;
midday is bright and even; evening turns golden-orange with longer soft
shadows; night the trail rests in moonlight. Trail lighting is always
natural daylight. Shadows are always soft — never hard, never dark.

---

## Colour Palette

Stones: warm grey. Grass: green. Trees: various greens. Water: clear blue.
Sky: blue. Soil: warm brown. The palette stays within this warm, natural
set across every zone.

---

## Scale

Everything is sized for a small preschool child. The trail is narrow enough
to feel intimate but wide enough to walk comfortably. Stones are child-sized.
Hills are gentle and climbable. The trail never feels overwhelming.

---

## Atmosphere

Warm. Soft. Safe. Adventurous. Every surface reads as natural and gentle.
The mood is always inviting and curious — full of discovery and gentle
movement. The trail never feels dark or threatening.

---

## Consistency Rules

- The trail is always winding, round-stoned, and safe — never straight, never sharp.
- Stones stay smooth and round across every generation.
- Trees stay round and welcoming.
- Water stays clear and gentle.
- No sharp corners, no dangerous terrain, no getting lost.
- No dark or high-contrast lighting.
- The trail's core shape, colours, and proportions are never redesigned or reinterpreted.

---

## Generation Considerations

The trail must be generated as a single winding natural path with safe
elements, not as a straight or dangerous road — this is the defining trait
of this world and the most common failure point to watch for. Keep all shapes
rounded with no sharp corners anywhere. Keep the colour palette limited to
the warm natural set defined above. Favor a soft, matte, natural material
language over any glossy, metallic, or realistic rendering. Treat the
trail's shape, colours, and proportions as a fixed identity to preserve
exactly, not to reinterpret, across every generation.

---

## Visual Richness Layer

> See `POMPOM_HILLS_PRODUCTION/02_WORLDS/GLOBAL_ENVIRONMENT_STANDARD.md` § Visual Richness Principle.
> Adventure Trail must never be reduced to "a dirt path."

This layer protects Adventure Trail from becoming too plain. Keep the
winding, round-stone-marked silhouette readable and add only the
canon-approved charm details below. Do not add random objects. Do not
flatten the trail into a straight, generic road — its charm must come from
the path itself, not from the worlds it connects.

**Allowed charm details:** AT-PATH-01, the round, smooth waypoint stones
marking the trail's curves, is the primary landmark and must be visible
along the trail in every establishing shot, together with the gentle rises
and dips in the terrain. AT-FLOWERS-01, the small clusters of colourful
flowers along the trail edges, and the varied ground textures (grass,
packed earth, mossy patches) marking different trail sections, add surface
charm. Small round pebbles scattered near the waypoint stones and an
occasional low, friendly signpost-shaped stone (no readable text) at major
bends are the central reusable small props. Gentle motion — grass swaying
along the trail edges and soft dappled shade shifting overhead in wooded
sections — keeps the world feeling alive without adding clutter.

**Forbidden clutter:** a straight or generic road shape, no visible
waypoint stones or markers, sharp gravel or dangerous terrain, modern
signage with readable text, a paved or asphalt surface, sharp corners
anywhere, and a dull, monotone colour palette.

### Art Direction Layer (use together with Immutable Identity above)

```text
premium preschool animation, handcrafted toy-set feeling, winding
discovery-path atmosphere, storybook adventure-trail beauty,
thumbnail-appeal composition, makes a child wonder what's around the
next bend
```

### Hero View Quality Tests

Before accepting a Hero View, it must pass:

1. **Silhouette Test** — recognisable as Adventure Trail from the winding, round-stone-marked path alone?
2. **Colour Test** — recognisable from the warm grey stones, green nature, and warm sunlight alone?
3. **Charm Test** — does it make a child wonder what's around the next bend?

If any test fails, reject.
