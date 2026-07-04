# Global Environment Standard — Pompom Hills

> This document defines the mandatory structure every Environment Bible and
> World Specification must follow. Cloud Hill (ENV-002) is the reference
> implementation at v5.1.

---

## Visual Richness Principle ⭐

> Added by the Visual Richness and World Charm decision (4 Temmuz 2026).
> This principle governs every world in Pompom Hills and overrides any
> reading of this standard that treats "production-safe" as "visually empty."

**Production-safe does NOT mean visually empty.**
**Simple does NOT mean boring.**
**Preschool-readable does NOT mean plain.**
**Canon-safe worlds must still be visually rich, iconic and memorable.**

The single Hero View + World Spec + Shot Continuity pipeline (see below) stays
exactly as it is. This principle does not reopen the old multi-reference-pack
workflow, and it does not license chaotic or over-detailed worlds. It corrects
a different failure: recent world documentation had become so focused on
production safety that some worlds were reduced to their most basic object —
Cloud Hill as "a hill and some clouds," Flower Hill as "a field with flowers."
If a world can be fully described as one generic noun, it has lost its
identity, because any generic version of that noun could then pass for canon.

Every Pompom Hills world must have:

- a clear silhouette
- a distinct colour identity
- at least one iconic landmark
- 3–7 allowed charm details
- a repeatable world texture
- a unique emotional atmosphere
- a thumbnail-readable visual hook
- a reason children would remember it

A world must never be reduced to its most basic object.

```
Bad:  Cloud Hill = hill + clouds
Good: Cloud Hill = smooth cloud-watching hill + soft sky dome + wind path
      + sitting stone + cloud-shadow patterns + gentle summit charm

Bad:  Flower Hill = flowers + path
Good: Flower Hill = colourful flower-home hill + five-colour flower carpet
      + S-curve path + rounded garden homes + small fences + soft stairs
      + flower pots + warm home feeling
```

Every world must answer: **"What makes this place recognisable even without
characters?"**

If the answer is only the world's category name (a hill, a field, a tree, a
plaza), the world documentation is not finished.

---

## Why This Standard Exists

As the world library grows, consistency between bibles breaks down without
a shared structure. This standard ensures that every world:

- Can be read and used by any team member without orientation
- Can be consumed by AI generation tools in a predictable way
- Can be compared, audited, and versioned across the full library
- Produces visually consistent output across all episodes

---

## Two-Document Architecture

Every world requires exactly two documents:

| Document | Audience | Length | Purpose |
|----------|----------|--------|---------|
| `NN-slug-bible.md` | Humans + creative team | Long | Full creative definition, lore, production rules |
| `NN-slug-world-spec.md` | AI generation tools | 600–900 words | Dense extraction for generation prompts |

The Bible is the source of truth. The Spec is a translation layer.
The Spec never replaces or contradicts the Bible.

---

## Bible — Required Sections

Every Environment Bible MUST contain the following sections, in this order:

```
1.  Overview               — 1–2 sentences. What is this place?
2.  Purpose                — Why does it exist in the world?
3.  Why This World Exists  — Design rationale ⭐
4.  Emotional Purpose      — 4 sub-questions (why / feel / stories / experiences)
5.  Play Philosophy        — Play style table + no-rules list + natural interactions
6.  World Position         — ASCII map showing neighbours
7.  Visual Identity        — Subsections per major element (hill, sky, flora, etc.)
8.  Spatial Layout         — ASCII flow from entry to exit
9.  Props                  — Table with Asset IDs, description, reusable flag
10. Camera Rules           — Angle table
11. Canonical Prompt Reference Pack — 4 views (Hero, Entrance/Climb, Mid, Detail)
12. Prompt Generation Rules — Table + Reject Rules
13. Soundscape             — Table
14. Forbidden              — Code block list
15. Story Opportunities    — Numbered list
16. Emotional Tone         — Bullet list
17. Production Notes       — Best characters, avoid, themes, opening/closing shots,
                             camera recommendations table, continuity notes
18. Consistency Checklist  — Code block ✓ list
18a. Visual Richness & World Charm ⭐ — Iconic Landmark, Allowed Charm Details
                             (by category), Forbidden Clutter, Thumbnail Hook,
                             Child Recognition Test. See §Visual Richness Principle.
19. World Identity Lock    — Locked elements table + acceptable variations
20. Hero View Technical Specification — Camera setup, framing percentages, composition rules
21. Camera Identity        — Default lens, height table, movement philosophy,
                             allowed/forbidden movements, framing consistency
22. Lighting Identity      — Direction table, softness, ambient fill, shadow density,
                             exposure, continuity rules
23. Colour Identity        — White balance, exposure, contrast, saturation, palette table,
                             highlight/shadow behaviour, forbidden colour shifts
24. Environmental Sound Identity — Wind, birds, ambience level, silence ratio, forbidden sounds
25. Continuity Rules       — Full table of everything that must stay consistent
26. Production QA          — Checklist: World Identity / Camera / Lighting / Colour /
                             Scale / Atmosphere / World Recognition
27. Canonical Reusable Assets — Table with Asset IDs
28. World Navigation       — Entry, climb/approach, main area, exit. Default + alternatives.
29. View Transition Rules  — Default sequence + when-to-use table + transitions to avoid
30. Character Occupancy    — Ratio table per shot type
31. Typical Episode Usage  — 30s / 60s / 90s structures + story types that fit / don't fit
32. Common Generation Failures — Per failure: recognition / why it matters / fix
33. Video Generation Rules — Movement speeds, camera speed, pacing, rhythm
34. Production Summary     — 1–2 paragraphs. How this world behaves as a reusable asset.
35. Changelog              — Version table with breaking changes
```

**Sections 1–18** are the creative foundation. Every bible must have them.
**Sections 19–35** are the production layer. Add them when the world moves into active production.

---

## World Spec — Required Sections

Every World Spec MUST contain the following sections. Each section is dense and brief.

```
1. Identity           — 5–8 locked bullet points. What defines this world, always.
2. Colour Palette     — Table with Asset IDs and hex values. White balance + exposure note.
3. Reusable Assets    — Table with Asset IDs and descriptions.
4. Framing            — Zone percentage table for wide shots. Horizon rule.
5. Character Occupancy — Ratio table. Emotional peak rule.
6. Navigation         — Default flow + explicit note that alternatives are permitted.
7. Generation Failures — Quick-reference table: failure / fix.
8. Video Rules        — Compact table: element / rule.
```

Total target length: 600–900 words. If the spec exceeds 900 words, trim.
The spec is not a summary of the bible — it is a generation instruction set.

---

## Visual Richness & World Charm — Bible Section ⭐

Every world Bible must contain a `## Visual Richness & World Charm` section
(inserted after Consistency Checklist, before World Identity Lock — see
section order above, §18a). This section defines the allowed details that
make the world feel alive, memorable and premium without causing production
drift.

It must include:

### Iconic Landmark

The one visual element that makes the world immediately recognisable.

### Allowed Charm Details

A controlled list of reusable small details that may appear in shots,
organised into the four charm categories below.

### Forbidden Clutter

Details that would make the world messy, generic or hard to keep consistent.

### Thumbnail Hook

What makes this world visually attractive in a YouTube thumbnail.

### Child Recognition Test

A child should be able to describe the world in one simple phrase. Example
phrases:

- "the hill where clouds come close"
- "the colourful flower home hill"
- "the big tree where Opa tells stories"
- "the square where friends meet and play"

---

## Visual Richness Layer — World Spec Section ⭐

Every World Spec must contain a `## Visual Richness Layer` section. This
layer protects the world from becoming too plain.

Rules:

- Keep the world readable.
- Keep the main silhouette clear.
- Add only canon-approved charm details.
- Do not add random objects.
- Do not make the scene empty.
- Do not remove the world's emotional identity.
- Do not flatten the world into a generic background.

Use visual richness through:

- rounded shapes
- repeated motif patterns
- soft handcrafted textures
- small reusable props
- gentle environmental motion
- landmark objects
- clear colour accents
- preschool-safe decorative details

---

## World Charm Categories ⭐

For every world, define charm details in these four categories. A world
should have 3–7 Allowed Charm Details total, drawn from across these
categories (not necessarily one per category).

### Landmark Charm

Large or medium elements that define the place.

Examples: special tree, summit stone, curved bridge, home cluster, fountain,
lantern path, cloud arch.

### Surface Charm

Textures and patterns that make the world recognisable.

Examples: flower carpets, cloud shadows, pebble paths, mossy stones, soft
grass tufts, star-shaped leaves, rounded wood grain.

### Small Prop Charm

Small reusable props that add life without causing chaos.

Examples: flower pots, tiny flags without text, mailboxes, small benches,
soft fences, lanterns, stepping stones, little baskets.

### Motion Charm

Gentle environmental movements.

Examples: clouds drifting, flowers swaying, leaves moving, water trickling,
soft wind ribbons, shadows passing slowly.

---

## Forbidden Over-Simplification Rule ⭐

Reject any world generation if the image technically follows the description
but loses the world's unique charm.

```
Reject Cloud Hill if:
- it is only a plain green hill with clouds
- the summit has no memorable detail
- there is no cloud-watching feeling
- it could belong to any generic meadow

Reject Flower Hill if:
- it is only a generic flower field
- it has no S-curve path
- it has no five-colour identity
- it has no home/beauty feeling when used as Home Cluster

Reject Central Square if:
- it is only an empty plaza
- the Big Pompom Tree is missing
- there is no community/play feeling

Reject Opa's Tree if:
- it is only a random tree
- it has no storytelling/shelter feeling
- the tree is not iconic
```

A world should be simple enough to read, but rich enough to remember.

This rule applies to every world in the library, not only the four examples
above — apply the same test (does the image lose the world's unique charm
even while technically matching the description?) to any world.

---

## Hero View Quality Target ⭐

Hero View should not be empty.

A Canon Hero View must include:

- the world's main silhouette
- the main landmark
- controlled charm details
- clear colour identity
- atmosphere
- depth
- preschool-safe visual richness

Hero View should feel like a premium preschool animation environment, not a
technical asset preview.

Hero View must pass three tests:

1. **Silhouette Test** — Can the world be recognised from shape alone?
2. **Colour Test** — Can the world be recognised from palette alone?
3. **Charm Test** — Does the image make a child want to enter the world?

If any test fails, reject the Hero View.

---

## Art Direction Prompt Layer ⭐

World Specs should include two prompt layers when writing a Hero View
generation prompt:

### Technical Canon Layer

Defines what must stay consistent:

- geometry
- landmarks
- colours
- scale
- lighting
- forbidden elements

### Art Direction Layer

Defines quality and emotional richness:

- premium preschool animation
- handcrafted toy-set feeling
- soft rounded details
- warm atmosphere
- visual charm
- storybook beauty
- thumbnail appeal
- child curiosity

Do not use only the Technical Canon Layer for generation. Technical-only
prompts often create safe but boring worlds. Use both layers together in
every Hero View generation prompt.

---

## Visual Quality Anchor Policy ⭐

When strong previous images exist for a world (older references, earlier
Hero View attempts, concept art), use them as **Visual Quality Anchors**.

A Visual Quality Anchor is an approved image used to preserve:

- charm
- richness
- style quality
- toy-set feeling
- colour appeal
- premium preschool look

It is **not** a command to copy every object exactly.

Rules:

- Use strong previous images to preserve world charm.
- Use the World Spec to decide which objects are canon.
- Do not blindly copy text signs, animals, water features, extra houses or
  random props from an anchor image.
- If an image is beautiful but too complex, extract its style and charm into
  Allowed Charm Details rather than discarding it.
- Do not discard strong older images just because the new spec is cleaner —
  mine them for charm first.

---

## Image vs Text vs Hybrid Generation ⭐

World creation should use a **hybrid system** when possible:

```
Approved reference image
    +
World Spec
    +
Allowed Charm Details
    +
Shot Continuity
```

Text-only generation is allowed for first exploration, but it often produces
safe and generic results. Image-only generation is not enough on its own
because it may copy unwanted details from the reference.

Hybrid generation is preferred because:

- image preserves visual richness
- spec preserves canon
- allowed charm controls detail
- shot continuity protects video production

---

## Negative Prompt Philosophy ⭐

Negative prompts must prevent drift, not remove charm.

Avoid overusing negative prompts in a way that makes worlds empty.

```
Bad:  No objects, no props, no houses, no details, no decorations, no texture.
Good: No random clutter, no non-canon objects, no sharp edges, no photorealism,
      no dark mood, no modern objects, no readable text.
```

Allowed charm details should never be accidentally removed by generic
"no clutter" language.

Use: **"No random clutter."**
Do not use: **"No detail."**

See `00-CORE/NEGATIVE_PROMPTS.md` for the project-wide negative prompt lists —
this philosophy applies whenever a world-specific negative block is written.

---

## Asset ID Convention

Every reusable environmental asset must have a stable ID.

**Format:** `[WORLD-PREFIX]-[TYPE]-[INDEX]`

| Component | Rule | Example |
|-----------|------|---------|
| World prefix | 2–3 uppercase letters from world name | CH (Cloud Hill), KH (Kiko's Home), CS (Central Square) |
| Type | Descriptive uppercase tag | GRASS, CLOUD, STONE, TREE, FENCE, AMB, BIRD |
| Index | 01, 02, A, B — for variants | 01, A |

**Examples:**
```
CH-GRASS-01     Cloud Hill canonical grass
CH-CLOUD-A      Cloud Hill large cloud (left)
CH-CLOUD-B      Cloud Hill medium cloud (right)
CH-STONE-01     Cloud Hill sitting stone
KH-DOOR-01      Kiko's Home front door
KH-BED-01       Kiko's Home round bed
CS-TREE-01      Central Square big pompom tree
```

Asset IDs are referenced in:
- Bible → Canonical Reusable Assets table
- Spec → Colour Palette table + Reusable Assets table
- Shot files → "Use CH-STONE-01" instead of describing the stone each time

---

## Versioning Rules

Every bible uses semantic versioning: `MAJOR.MINOR`

| Change Type | Version Bump | Examples |
|-------------|:------------:|---------|
| New section added, identity rules changed, production layer added | MAJOR (x.0) | v3.0, v4.0, v5.0 |
| Corrections, clarifications, small additions | MINOR (x.1, x.2) | v3.1, v4.1 |

Every version bump requires a Changelog entry with:
- Version number
- List of changes
- Note of any breaking changes (marked **Breaking**)

---

## Status Flags

Use these flags in the metadata block at the top of each bible:

| Flag | Meaning |
|------|---------|
| `Bible: ✅` | Bible document exists |
| `Hero View: ✅ / ❌` | Hero view prompt/image exists |
| `World Spec: ✅ / ❌` | World Spec document exists |
| `Status: Design` | Creative definition only — not yet production-ready |
| `Status: Production Ready` | Full bible + spec + production layer complete |
| `Status: In Use` | World has appeared in at least one produced episode |
| `Status: Locked` | Produced world — no changes without creative director approval |

---

## Reference Implementation

Cloud Hill (ENV-002) is the reference implementation of this standard.

| Document | Path |
|----------|------|
| Bible | `POMPOM_HILLS_PRODUCTION/02_WORLDS/CLOUD_HILL/00_CANON/02-cloud-hill-bible.md` |
| World Spec | `POMPOM_HILLS_PRODUCTION/02_WORLDS/CLOUD_HILL/02_WORLD_SPEC/02-cloud-hill-world-spec.md` |

When in doubt about structure, formatting, or depth — consult Cloud Hill.

---

## Compliance Checklist

Before marking any world as Production Ready, verify:

```
✓ Bible exists and follows the required section order?
✓ World Spec exists and is 600–900 words?
✓ All Asset IDs defined and consistent between Bible and Spec?
✓ Hero View technically specified (framing %, camera height)?
✓ Colour palette has hex values for all primary elements?
✓ Common Generation Failures documented (minimum 3)?
✓ Video Generation Rules defined?
✓ Changelog present with all version entries?
✓ Status flag set correctly in metadata block?
✓ World folder created at POMPOM_HILLS_PRODUCTION/02_WORLDS/NN-slug/?
```

### Visual Richness & World Charm QA ⭐

Add these checks to every world QA checklist (Bible Consistency Checklist or
Production QA section):

```
✓ Does the world have a clear iconic landmark?
✓ Does the world feel visually rich but readable?
✓ Are allowed charm details present?
✓ Is the world recognisable without characters?
✓ Is the world more specific than a generic landscape?
✓ Does the image have thumbnail appeal?
✓ Is the world production-safe without being empty?
✓ Are details canon-approved rather than random?
✓ Would a child remember this place?
✓ Would a parent perceive this as premium preschool animation?
```

### Hero View Prompt Template Addition ⭐

Add this to the global Hero View prompt template used when generating or
regenerating any world's Canon Hero View:

```text
Create a premium preschool animation Hero View for [World Name].

This world must feel visually rich, charming and iconic while remaining
clean and readable. Do not make the world empty or generic.

The image should include:
- the main world silhouette
- the primary landmark
- approved charm details
- clear colour identity
- soft handcrafted textures
- warm preschool atmosphere
- thumbnail-readable composition

Use the Technical Canon Layer for consistency.
Use the Art Direction Layer for visual quality.

Reject any result that looks like a generic version of the world.
```

---

## Changelog

| Version | Changes | Breaking |
|---------|---------|:--------:|
| 1.0 | Initial standard | — |
| 2.0 | **Visual Richness Update:** Added Visual Richness Principle (global). Added Visual Richness & World Charm Bible section (§18a) and Visual Richness Layer World Spec section. Added World Charm Categories (Landmark / Surface / Small Prop / Motion). Added Forbidden Over-Simplification rule. Added Hero View Quality Target (Silhouette/Colour/Charm tests). Added Art Direction Prompt Layer (Technical Canon + Art Direction). Added Visual Quality Anchor policy for reusing strong prior reference images. Added Image vs Text vs Hybrid generation preference (hybrid preferred). Added Negative Prompt Philosophy ("no random clutter" not "no detail"). Added Visual Richness & World Charm QA checks and updated Hero View prompt template. Does not remove or replace the single Hero View + World Spec + Shot Continuity pipeline. | ✅ Breaking (adds mandatory section) |

---

*Bu belge tüm Pompom Hills mekanları için üretim standardını tanımlar.*
*Versiyon: 2.0*
*Son güncelleme: 4 Temmuz 2026*

---

## Related Documents

These documents form the complete production system alongside this standard.
Do not duplicate their content in world bibles — reference them instead.

| Document | Path | What It Covers |
|----------|------|----------------|
| Asset Registry | `00-CORE/ASSET_REGISTRY.md` | All env asset IDs, world prefixes, registered assets |
| Master QA Checklist | `00-CORE/MASTER_QA_CHECKLIST.md` | Full episode QA before publish — 12 layers |
| Scene QA Checklist | `00-CORE/SCENE_QA_CHECKLIST.md` | Per-shot QA during production |
| Visual Style Guide | `00-CORE/VISUAL_STYLE_GUIDE.md` | Global shape language, colour philosophy, rendering rules |
| Continuity Rules | `00-CORE/CONTINUITY_RULES.md` | Character, world, camera, lighting, sound continuity |
| Child Safety Rules | `00-CORE/CHILD_SAFETY_RULES.md` | Safety standards for all content |
| Audio Guide | `00-CORE/AUDIO_GUIDE.md` | Voice, music, ambience standards |
| Tech Specs | `00-CORE/TECH_SPECS.md` | 3D pipeline, naming convention, render specs |
