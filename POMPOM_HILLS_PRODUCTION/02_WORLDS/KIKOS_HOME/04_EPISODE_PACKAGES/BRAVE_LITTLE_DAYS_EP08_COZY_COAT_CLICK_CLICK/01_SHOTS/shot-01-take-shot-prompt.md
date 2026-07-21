# Shot 01 — Take Shot Prompt (Fresh Anchor Setup)

## Purpose

This is the fresh anchor setup for Shot 01. It establishes the visual baseline for the entire episode, providing 3 reference images that define the look, feel, and style for all subsequent shots.

## Reference Upload Map

| Ref # | Image | Description | Usage |
|-------|-------|-------------|-------|
| @image1 | Kiko character model | Full-body, coral-pink top, white shorts, brown pigtails | Character consistency |
| @image2 | Mimi character model | Full-body, soft-blue rabbit, yellow top | Character consistency |
| @image3 | Entryway environment | Warm cream walls, honey wood floor, coat rack, door | Environment consistency |

## Hard Gate Before Generation

- [ ] @image1 loaded: Kiko character visible, correct outfit
- [ ] @image2 loaded: Mimi character visible, correct outfit
- [ ] @image3 loaded: Entryway environment, warm palette
- [ ] All three references match episode style
- [ ] No conflicting references
- [ ] Warm colour palette confirmed

## Take Shot Prompt

### Primary Prompt

```
@image1 @image2 @image3 CONTINUOUS UNBROKEN 15-SECOND SINGLE TAKE: 3D animated children's show, warm and cozy, soft textures, child-friendly. Entryway of cozy home, warm cream walls, honey wood floor. Terracotta coat hanging on wooden coat rack, screen-left. Kiko, 3-4 year old girl, coral-pink top, white shorts, brown pigtails, screen-left, looking at coat with excited expression, eyes open. Mimi, soft-blue rabbit, yellow top, screen-right, standing near front door with glass panels, warm smile. Warm daytime, soft golden light through door. Low visual density, simple uncluttered space. Eyes open in first frame. 28-35mm lens, child eye level 0.75m, static camera. No camera movement. Warm golden daytime lighting, soft diffused light from screen-right, no harsh shadows.
```

### Compact Version

```
@image1 @image2 @image3 {style}, {camera}, {lighting}. Entryway, coat on rack. Kiko screen-left excited, Mimi screen-right warm smile. Eyes open. Static.
```

## Dialogue Timing

| Timestamp | Character | Line | Duration |
|-----------|-----------|------|----------|
| 0.4–1.8s | Mimi | "Your coat is ready!" | 1.4s |

## Visual Targets

| Element | Target | Tolerance |
|---------|--------|-----------|
| Kiko position | Screen-left, 30% | ±5% |
| Mimi position | Screen-right, 70% | ±5% |
| Coat state | Hanging on rack | Exact |
| Lighting | Warm golden from right | ±10% warmth |
| Camera height | 0.75m | ±0.05m |

## Quality Benchmarks

- **Resolution**: 1920×1080 minimum
- **Frame rate**: 24fps
- **Style match**: Must match @image1, @image2, @image3
- **Colour palette**: Warm cream, honey wood, terracotta
- **No artifacts**: Clean, smooth animation
- **No text**: No on-screen文字

## Validation Checklist

- [ ] All 3 reference images loaded
- [ ] Kiko matches @image1 exactly
- [ ] Mimi matches @image2 exactly
- [ ] Environment matches @image3 exactly
- [ ] Coat is on rack (hanging)
- [ ] Warm palette throughout
- [ ] Camera at child eye level
- [ ] Eyes open in first frame
- [ ] No on-screen text
- [ ] Dialogue timing correct
- [ ] 15-second duration
- [ ] No background music
- [ ] Safe-exposure compliant
