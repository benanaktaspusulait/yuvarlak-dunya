# Mimi's Burrow — World Creation Specification

> Source of truth: `05-mimis-burrow-bible.md` (canonical, creative). This document
> is a production-oriented extraction for AI-assisted world generation. It does
> not replace the Bible and does not duplicate its storytelling, educational,
> character, or workflow content.

---

## Purpose

Mimi's Burrow is an underground retreat — a cozy hidden world beneath the grass where Mimi lives. It is a warm, safe, intimate space designed for quiet moments, sleep scenes, friend visits, and cozy indoor activities. The underground layout reinforces Mimi's gentle, introverted personality.

---

## Immutable Identity

The following elements define the canonical identity of Mimi's Burrow and must never change:

- Round underground entrance with blue frame (#90CAF9)
- Flowers on top of the entrance
- Warm interior light visible from outside
- Round stepping-stone path (#E0E0E0) to entrance
- Soft green grass (#C8E6C9) above
- Warm blue interior walls (#90CAF9)
- Round soft pillow (#90CAF9)
- Small round window
- Mini white shelf with books
- Round orange carrot box (#FF7043)
- No door — open entrance
- Small, child-proportioned scale throughout

---

## Visual Identity

A round underground burrow entrance framed in soft blue, nestled beneath green grass with flowers on top. Inside, warm blue walls create a cozy intimate space. Everything is rounded, small, and soft — designed for a small character like Mimi. The entrance is always open, always inviting, with warm light spilling out. The overall feeling is a "secret cozy hideaway" — hidden but safe, small but warm.

---

## World Layout

The world reads as one continuous journey from outside to inside. The exterior shows the grass hill with the round blue entrance, flowers on top, and a stepping-stone path. Entering the burrow reveals one small continuous underground room containing a pillow, window, shelf, and carrot box. There are no separate rooms — just one cozy connected space.

---

## Spatial Relationships

- The exterior flowers are always visible above the entrance.
- The stepping-stone path always leads directly to the entrance.
- The interior is always visible through the round entrance when looking in.
- The window maintains a visual relationship with the outside world.
- The pillow is always the central interior element.
- The shelf and carrot box are always within reach of the pillow.

---

## Playable Areas

**Exterior Approach** — Purpose: welcoming approach to the burrow. Visual identity: green grass, flowers on top, round blue entrance below, stepping-stone path. Important props: flowers, grass, path. Typical use: arrival, waiting, approach.

**Entrance** — Purpose: threshold between outside and underground. Visual identity: round blue frame (#90CAF9), warm light inside, no door. Important props: entrance frame. Typical use: entering, exiting, greetings.

**Interior Room** — Purpose: the heart of the burrow, one continuous underground space. Visual identity: warm blue walls, soft green carpet, round pillow, small window, mini shelf, carrot box. Important props: pillow, window, shelf, carrot box. Typical use: sleeping, reading, eating, resting, quiet play.

---

## Materials

Entrance frame: soft matte blue. Interior walls: soft matte warm blue. Floor: soft plush green carpet. Pillow: soft plush blue. Shelf: smooth matte white. Carrot box: smooth matte orange. All surfaces read as touchable, soft, and child-safe. No glass, no metal, no plastic, no hard edges anywhere.

---

## Lighting

Interior light is always warm and soft — never cold, never harsh. The entrance provides a warm glow visible from outside. The window lets in gentle exterior light. The overall interior feeling is warm blue with golden undertones — cozy, safe, never dark or spooky.

---

## Colour Palette

Entrance frame: soft blue (#90CAF9). Interior walls: soft blue (#90CAF9). Pillow: soft blue (#90CAF9). Grass: soft green (#C8E6C9). Carrot box: warm orange (#FF7043). Stones: light grey (#E0E0E0). Shelf: white. Interior light: warm golden. The palette stays within this small, consistent warm-blue set.

---

## Scale

Everything is sized for a small character. The entrance is low (0.80m), child-proportioned. The interior is intimate, not spacious. The pillow is large relative to the room. The shelf is low and reachable. The carrot box is small and toy-sized. The overall feeling is cozy and enclosed, not grand.

---

## Atmosphere

Safe. Warm. Cozy. Hidden. Intimate. Every surface reads as soft and touchable. The mood is consistently calm and reassuring — a place where children feel "this is my secret safe place."

---

## Consistency Rules

- The entrance is always round and blue — never rectangular, never other colours.
- The interior is always warm and softly lit — never dark, never cold.
- Flowers are always present on top of the entrance.
- The stepping-stone path always has 3 stones.
- No sharp edges anywhere, inside or outside.
- No large furniture, no modern objects, no scary elements.
- The burrow's core shape, entrance colour, and interior palette are never redesigned.

---

## Generation Considerations

The entrance must be generated as a round blue-framed opening — not a door, not a tunnel, not a cave. The interior must feel warm and cozy, not dark or cavernous. Keep all shapes rounded with no sharp corners. Keep the colour palette limited to warm blues, greens, and orange accents. The burrow's identity — its warmth, its smallness, its hidden quality — must be preserved exactly across every generation.

---

## Colour Palette (Detailed)

| Asset ID | Element | Hex |
|----------|---------|-----|
| MB-DOOR-01 | Entrance frame | #90CAF9 |
| MB-GRASS-01 | Grass above | #C8E6C9 |
| MB-STONES-01 | Stepping stones | #E0E0E0 |
| MB-CARROT-BOX-01 | Carrot box | #FF7043 |
| MB-PILLOW-01 | Interior pillow | #90CAF9 |
| MB-SHELF-01 | Mini shelf | #FFFFFF |

White balance: 5000K warm. Exposure: normal. Contrast: low. Saturation: medium.
No neon. No pure black. No cool shift.

---

## Reusable Assets

| Asset ID | Description |
|----------|-------------|
| MB-DOOR-01 | Round blue entrance frame |
| MB-PILLOW-01 | Round blue plush pillow |
| MB-WINDOW-01 | Small round window with white frame |
| MB-SHELF-01 | Mini round white shelf with books |
| MB-CARROT-BOX-01 | Round orange carrot box |
| MB-CARROTS-01 | 2–3 orange carrots |
| MB-FLOWERS-01 | Small round flowers above entrance |
| MB-STONES-01 | Round grey stepping stones |
| MB-GRASS-01 | Soft green grass above burrow |
| MB-BUSH-01 | Small green pompom bush |

---

## Framing

Entrance always visible in exterior shots — it is the primary visual anchor. Interior shots show the pillow as central element.

| Shot | Max Character % | Entrance Visible |
|------|:---------------:|:----------------:|
| Wide establishing | 15–20% | Always |
| Medium single | 30–35% | Yes |
| Medium two characters | 40–45% | Yes |
| Interior wide | 40–50% | From inside |
| Close-up | 65–75% | Partial |

Emotional peak = interior shot showing warmth and coziness.

---

## Navigation

Default flow: Exterior (approach) → Entrance (threshold) → Interior (living) → Exit.
Entrance crossing — the transition from outside to underground — must not be skipped.
**Alternative openings are permitted when story continuity requires them.**

---

## Generation Failures — Quick Reference

| Failure | Fix |
|---------|-----|
| Entrance not round or not blue | Reject — round blue frame is identity |
| Interior dark or cold | Add warm light, recheck palette |
| Sharp edges anywhere | Smooth all forms |
| Large furniture present | Scale down to child-size |
| Flowers missing from entrance top | Add flowers |
| Stepping stones missing | Add 3 round stones |
| No warm interior glow visible | Add warm light from inside |
| Cool colour temperature | Warm to 5000K, recheck palette |

---

## Video Rules

| Element | Rule |
|---------|------|
| MB-PILLOW-01 movement | Gentle settle, very slow |
| MB-FLOWERS-01 movement | Slight sway, 5 sec cycle |
| Interior light | Constant warm glow, no flicker |
| Camera speed | Max 3% frame/sec pan or push |
| Environmental rhythm | All movement on the same slow breath |

Every animated frame passes the same QA as a still image.

---

## Visual Richness Layer

> See `02-WORLDS/GLOBAL_ENVIRONMENT_STANDARD.md` § Visual Richness Principle.
> Mimi's Burrow must never be reduced to "a hole in the ground."

This layer protects Mimi's Burrow from becoming too plain. Keep the round
blue entrance readable and the cozy underground silhouette clear — add only
the canon-approved charm details below. Do not add random objects. Do not
remove the hidden, safe, cozy-hideaway emotional identity.

**Allowed charm details:** MB-DOOR-01, the round blue entrance frame with
warm interior light always spilling out, is the primary landmark and must be
visible in every exterior shot. MB-FLOWERS-01 growing on top of the entrance
mound and MB-STONES-01, the three round grey stepping stones, plus
MB-GRASS-01 above the burrow, add surface and landmark charm. Inside,
MB-PILLOW-01 (the round blue plush pillow) and MB-CARROT-BOX-01 (the round
orange carrot box) are the central reusable small props. Gentle motion —
MB-FLOWERS-01 swaying above the entrance and Mimi's soft ear-flop/hop at the
threshold — keeps the world feeling alive without adding clutter.

**Forbidden clutter:** a dark or cold interior, sharp edges anywhere, large
or oversized furniture, frightening elements or creatures, an entrance that
is not round or not blue, metal or plastic materials, and any loud sounds or
sudden fast motion.

### Art Direction Layer (use together with Immutable Identity above)

```text
premium preschool animation, handcrafted toy-set feeling, cozy hidden
underground atmosphere, storybook secret-hideaway beauty, thumbnail-appeal
composition, makes a child want to peek inside the little blue doorway
```

### Hero View Quality Tests

Before accepting a Hero View, it must pass:

1. **Silhouette Test** — recognisable as Mimi's Burrow from the round blue entrance beneath the grass alone?
2. **Colour Test** — recognisable from the soft blue frame, green grass, and warm interior glow alone?
3. **Charm Test** — does it make a child want to peek inside the cozy blue doorway?

If any test fails, reject.

---

*Mimi's Burrow — World Specification, aligned with Bible v3.1.*
*Visual Richness Layer added 4 Temmuz 2026.*
