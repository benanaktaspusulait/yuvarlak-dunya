# Mimi's Burrow — Interior Hero View Production Prompt

> **Purpose:** Canonical INTERIOR reference for Mimi's Burrow. Companion to
> `mimis-burrow-exterior-openart-prompt.md`.
> **World Spec:** `02_WORLD_SPEC/05-mimis-burrow-world-spec.md` (§ Interior Room, § Materials, § Colour Palette, § Reusable Assets)
> **Primary use:** `@image2` interior canon reference for **S01E04 — Mimi's Big Yawn, Shot 05 (Stepping Inside)** and any future interior shot.
> **Status:** Reference prompt — generate and approve BEFORE producing S01E04 Shot 05 (Gate C).

---

## Why This Exists

S01E04 Shot 05 crosses from the exterior into the interior and seeds ALL interior objects in one shot. Generating that crossing with only the exterior `@image1` is the single highest object-spawning / cave-morphing risk in the episode. This interior reference gives Shot 05 a canonical `@image2` so the model preserves interior design instead of inventing it.

**Reference role (hard rule for Shot 05):**
```
@image1 = exact exterior first frame continuity source from Shot 04 (priority).
@image2 = this Mimi's Burrow interior canon reference — interior design only.

Do not use @image2 as the first frame.
Do not copy @image2 camera before the threshold crossing.
Do not let @image2 override @image1's exterior start, characters, or lighting.
Use @image2 only AFTER the crossing, to keep interior design on-canon.
```

---

## Interior Canon Notes (must match world spec)

- Warm blue interior walls (#90CAF9)
- Soft green plush carpet (#C8E6C9)
- Round blue plush pillow (#90CAF9) — central interior element / sleeping spot
- Small round window with white frame (gentle exterior light)
- Mini white shelf with a few books (low, reachable)
- Round orange carrot box (#FF7043)
- Warm golden interior glow — cozy, never dark or cold
- ONE small continuous underground room — no separate rooms, no chamber
- Everything rounded, soft, touchable, Mimi-sized — no sharp edges, no adult furniture

---

## Ready-to-Use Interior Hero View Prompt

```text
Create the canonical Interior Hero View for Mimi's Burrow.

The cozy inside of a small hidden underground burrow, designed as a preschool-safe toy-set world. One small continuous underground room — warm and intimate, not a cave, not a large chamber, no separate rooms.

Warm blue walls (#90CAF9) curve softly around the space. A soft green plush carpet (#C8E6C9) covers the floor. A large round blue plush pillow (#90CAF9) rests as the central, cozy element — clearly the comfiest sleeping spot. A small round window with a white frame lets in a gentle hint of soft evening light. A mini white shelf with a few small books sits low and reachable. A round orange carrot box (#FF7043) sits nearby. Warm golden light fills the room with a soft, safe, cozy glow.

Everything is Mimi-sized: child-proportioned, rounded, soft and touchable. No adult furniture, no oversized room, no sharp edges. The mood is warm, safe, hidden, and reassuring — "my secret cozy home."

Interior establishing view from a gentle eye-level inside the room, showing the pillow as the central element with the window, shelf and carrot box as supporting anchors around it.

{style} = Pompom Hills v2.1, rounded preschool toy world, pastel colors, matte clay-plush surfaces, toddler-safe emotional clarity
{camera} = stable 50mm preschool camera, interior eye-level, gentle framing, no distortion, no Dutch angle
{lighting} = warm golden interior glow, soft warm-blue undertones, cozy, never dark or cold, no harsh shadows
```

---

## Interior Negative Prompt

```text
door, closed door, wooden door, rectangular door, cave, cave mouth, dark hole, tunnel, mine shaft, scary underground, spooky, dark interior, cold interior, blue light only, harsh shadows, black interior, night, huge room, large underground chamber, oversized room, separate rooms, multiple rooms, house interior, adult furniture, large furniture, sharp edges, sharp corners, cracked walls, realistic dirt walls, missing pillow, missing window, missing shelf, missing carrot box, pillow not round, pillow not blue, clutter, random props, metal, plastic, glass, modern objects, city objects, signs, text, logo, watermark, photorealistic, exterior view, outside, grass field, sky, characters (unless intentionally added later)
```

---

## Interior Hero View QA Checklist

**APPROVE if ALL are YES:**

- [ ] **Room:** One small continuous cozy room? Not a cave/tunnel/large chamber?
- [ ] **Walls:** Warm blue (#90CAF9 or close)?
- [ ] **Carpet:** Soft green (#C8E6C9)?
- [ ] **Pillow:** Round, blue, and the clear central element?
- [ ] **Window:** Small round white-framed window visible?
- [ ] **Shelf:** Mini white shelf with books, low and reachable?
- [ ] **Carrot box:** Round orange carrot box visible?
- [ ] **Glow:** Warm golden interior glow, cozy, not dark?
- [ ] **Scale:** Mimi-sized, intimate, no adult/oversized furniture?
- [ ] **Shapes:** All rounded and soft, no sharp edges?

**REJECT if ANY are YES:**

- [ ] Room looks like a cave, tunnel, or large chamber
- [ ] Dark, cold, or scary atmosphere
- [ ] Pillow missing or not round/blue (pillow is the must-have anchor)
- [ ] Adult-sized or oversized furniture
- [ ] Separate/multiple rooms
- [ ] Sharp edges or hard modern materials

---

## Production Notes

- **Minimum acceptable for Shot 05 use:** the four must-haves from Shot 05 (round blue pillow, warm blue walls, green carpet, warm glow) plus at least one anchor (window, shelf, or carrot box). Ideally all three anchors are visible.
- **Save the approved still** and reference it as `@image2` when generating S01E04 Shot 05.
- **Do not copy this camera** for the exterior part of Shot 05 — the crossing must start from the exterior `@image1` and only settle into this interior look after the threshold.

---

*Companion to the exterior hero prompt. For full world specification, see*
*`02_WORLD_SPEC/05-mimis-burrow-world-spec.md`.*
