# Global Environment Standard — Pompom Hills

> This document defines the mandatory structure every Environment Bible and
> World Specification must follow. Cloud Hill (ENV-002) is the reference
> implementation at v5.1.

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
| Bible | `02-WORLDS/02-cloud-hill/02-cloud-hill-bible.md` |
| World Spec | `02-WORLDS/02-cloud-hill/02-cloud-hill-world-spec.md` |

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
✓ World folder created at 02-WORLDS/NN-slug/?
```

---

*Bu belge tüm Pompom Hills mekanları için üretim standardını tanımlar.*
*Versiyon: 1.0*
*Son güncelleme: 3 Temmuz 2026*

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
