# Environment / Hero View Assets

> *World image assets for Pompom Hills.*
> *Each world's visual references now live inside its own world package,
> under `POMPOM_HILLS_PRODUCTION/02_WORLDS/<WORLD_NAME>/01_HERO_VIEW/`.*
>
> This file used to describe the standalone `12-ENVIRONMENT/` directory.
> That directory has been merged into the world-based production packages
> so every world's canon, hero view, and episodes live in one place.

---

## Where to find a world's images now

```
POMPOM_HILLS_PRODUCTION/02_WORLDS/<WORLD_NAME>/01_HERO_VIEW/
├── hero-view.png     — Main establishing shot (primary AI generation reference)
├── left-view.png     — Left angle (where available)
├── right-view.png    — Right angle (where available)
└── top-view.png      — Overhead view (where available)
```

Example: Stone Hill's hero views are at
`POMPOM_HILLS_PRODUCTION/02_WORLDS/STONE_HILL/01_HERO_VIEW/`.

## Image Types

| File | Purpose |
|------|---------|
| `hero-view.png` | Main establishing shot — the primary reference for AI generation |
| `left-view.png` | Left angle |
| `right-view.png` | Right angle |
| `top-view.png` | Overhead view |

## Coverage Status (at time of migration)

- Hero + 3 views: CENTRAL_SQUARE, OPA_TREE, WISH_POND, FLOWER_HILL, TREE_HILL, STONE_HILL
- Hero view only: CLOUD_HILL, KIKOS_HOME, SUN_HILL, MIMIS_BURROW, TILLOS_GARDEN,
  LULUS_GREENHOUSE, POPPYS_BAKERY, BENNYS_PLAYGROUND, TILLOS_TREEHOUSE, MILOS_POND,
  ROSIES_ROSE_GARDEN, LILYS_LAVENDER_FARM, RAINBOW_BRIDGE, FRIENDSHIP_MEADOW,
  BUTTERFLY_MEADOW, LITTLE_FOREST, RAINBOW_CREEK, CAMPING_GROVE, STORY_CIRCLE,
  ART_CORNER, ADVENTURE_TRAIL
- No hero view yet (empty — planned/awaiting): PADDLE_COVE, PONY_MEADOW,
  HOBBY_HORSE_TRAIL, and Opa's Tree Night variant

## Related Documents

- `00-CORE/WORLD_BIBLE.md` — canonical world reference
- `11-DOCS/WORLD_CATALOG.md` — complete world inventory
- `POMPOM_HILLS_PRODUCTION/02_WORLDS/<WORLD_NAME>/00_CANON/` — world bible documents
- `08-PRODUCTION/ASSET_TRACKER.md` — asset production status

---

*Last updated: 4 Temmuz 2026 — merged into world-based production packages.*
