# Assets — EP08 "Cozy Coat, Click Click"

## Characters

| Character | Description | Ref File | Position | Notes |
|-----------|-------------|----------|----------|-------|
| Kiko | Coral-pink top, white shorts, brown pigtails | `01_CHARACTERS/kiko.md` | Screen-left | Main character, learning to put on coat |
| Mimi | Soft-blue rabbit, yellow top | `01_CHARACTERS/mimi.md` | Screen-right | Supportive friend, patient guide |

### Kiko Character Notes
- **Age appearance**: 3-4 years old
- **Hair**: Brown pigtails, neat but slightly tousled
- **Expression range**: Excited → frustrated → hopeful → proud
- **Movement style**: Childlike, slightly clumsy, enthusiastic
- **Voice**: Bright, childlike, higher pitch

### Mimi Character Notes
- **Species**: Soft-blue rabbit
- **Clothing**: Yellow top
- **Expression range**: Warm smile → gentle concern → encouraging → proud
- **Movement style**: Gentle, patient, deliberate
- **Voice**: Soft, warm, reassuring, mid-range pitch

## World

### Kiko's Home — Entryway

**Ref**: `02_WORLDS/KIKOS_HOME/world_entryway.md`

| Element | Description | Screen Position | Notes |
|---------|-------------|-----------------|-------|
| Front door | Wooden door with glass panels | Screen-right | Primary light source |
| Coat rack | Wooden stand with hooks | Center-left | Holds Kiko's coat |
| Small bench | Wooden bench with cushion | Near coat rack | Optional sitting spot |
| Potted plant | Green plant in terracotta pot | Screen-left corner | Adds life to scene |
| Walls | Warm cream colour | Background | No decorations |
| Floor | Honey-toned wood | Bottom | Clean, simple |

### Environment Notes
- **Atmosphere**: Warm, safe, familiar
- **Lighting**: Soft golden daylight through door glass
- **Clutter level**: Very low — only essential props
- **Sound**: Quiet home ambience, no TV, no music

## Props

| Prop | Description | State Changes | Reusable |
|------|-------------|---------------|----------|
| Coat | Terracotta/rust coloured, child-sized | On rack → half-on → one arm → both arms → snapped → worn | ✅ Yes |
| Snap/Button | Coat fastening mechanism | Open → closed (click-click) | ✅ Yes |
| Coat rack | Wooden stand | Static throughout | ✅ Yes |
| Potted plant | Green plant | Static throughout | ✅ Yes |

### Coat Prop Details
- **Colour**: Warm terracotta/rust
- **Size**: Child-sized (fits Kiko)
- **Fastening**: Snap buttons (not zipper) — for the "click-click" sound
- **Sleeves**: Long enough for Kiko's arms
- **Fit**: Slightly oversized for cute, cozy look

### Prop State Tracking

```yaml
coat_state:
  shot_01: "hanging_on_rack"
  shot_02: "half_on_attempting"
  shot_03: "half_on_mimi_approaches"
  shot_04: "one_arm_in"
  shot_05: "both_arms_in_unsnapped"
  shot_06: "snapped"
  shot_07: "fully_worn_cozy"
  shot_08: "fully_worn_standing_proud"
```

## Shared Assets

### Bumpers

| Asset | File | Duration | Usage |
|-------|------|----------|-------|
| Opening bumper | `SHARED_ASSETS/BUMPERS/brave_little_days_opening.mp4` | 3s | Before Shot 01 |
| Closing bumper | `SHARED_ASSETS/BUMPERS/brave_little_days_closing.mp4` | 3s | After Shot 08 |

### Bumper Notes
- Opening: Series logo with warm chime sound
- Closing: "See you next time!" with series logo
- No dialogue in bumpers
- Warm colour palette matching episode

## Asset Loading Order

1. **Character models**: Load Kiko and Mimi from character refs
2. **Environment**: Load entryway world
3. **Props**: Load coat, snap mechanism
4. **Bumpers**: Load opening and closing bumpers
5. **Audio**: Load SFX (click-click, door sounds)

## Asset Dependencies

```
EP08
├── 01_CHARACTERS/
│   ├── kiko.md
│   └── mimi.md
├── 02_WORLDS/
│   └── KIKOS_HOME/
│       └── world_entryway.md
├── SHARED_ASSETS/
│   └── BUMPERS/
│       ├── brave_little_days_opening.mp4
│       └── brave_little_days_closing.mp4
└── EP08_COZY_COAT_CLICK_CLICK/
    └── (this package)
```

## Asset Validation Checklist

- [ ] Kiko character model loads correctly
- [ ] Mimi character model loads correctly
- [ ] Entryway environment renders properly
- [ ] Coat prop appears in correct position on rack
- [ ] Coat state changes track correctly across shots
- [ ] Snap mechanism is visible and functional
- [ ] Opening bumper plays before Shot 01
- [ ] Closing bumper plays after Shot 08
- [ ] No missing assets or broken references
- [ ] All assets maintain warm colour palette
