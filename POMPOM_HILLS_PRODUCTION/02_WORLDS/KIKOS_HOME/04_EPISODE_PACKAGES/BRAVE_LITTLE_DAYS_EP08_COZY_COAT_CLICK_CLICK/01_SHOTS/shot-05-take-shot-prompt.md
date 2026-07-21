# Shot 05 — Take Shot Prompt (Chain B Quality Reset)

## Purpose

This is the Chain B quality reset anchor. Shot 05 marks the beginning of the second chain (Shots 05-08) and serves as a fresh quality checkpoint to ensure visual consistency for the second half of the episode.

## Reference Upload Map

| Ref # | Image | Description | Usage |
|-------|-------|-------------|-------|
| @image1 | Kiko with coat (both arms in) | Coral-pink top, white shorts, brown pigtails, terracotta coat with both arms in | Character + coat state |
| @image2 | Mimi character model | Soft-blue rabbit, yellow top | Character consistency |
| @image3 | Entryway environment | Warm cream walls, honey wood floor, coat rack, door | Environment consistency |

## Hard Gate Before Generation

- [ ] @image1 loaded: Kiko with coat, both arms in sleeves
- [ ] @image2 loaded: Mimi character visible, correct outfit
- [ ] @image3 loaded: Entryway environment, warm palette
- [ ] Coat state matches Shot 04 ending (both arms in, unsnapped)
- [ ] All three references match episode style
- [ ] No conflicting references
- [ ] Warm colour palette confirmed

## Take Shot Prompt

### Primary Prompt

```
@image1 @image2 @image3 CONTINUOUS UNBROKEN 15-SECOND SINGLE TAKE: 3D animated children's show, warm and cozy, soft textures, child-friendly. Entryway, warm setting. Kiko, 3-4 year old girl, coral-pink top, white shorts, brown pigtails, screen-left, both arms now in terracotta coat sleeves, looking down at herself with amazed expression, eyes open. Mimi, soft-blue rabbit, yellow top, screen-right, beaming with pride. Coat on but unsnapped. Warm golden light. Medium shot, child eye level. Eyes open in first frame. 28-35mm lens, child eye level 0.75m, static camera. Warm golden daytime lighting, soft diffused light from screen-right, no harsh shadows.
```

### Compact Version

```
@image1 @image2 @image3 {style}, {camera}, {lighting}. Kiko screen-left, both arms in coat, amazed. Mimi screen-right, proud. Coat unsnapped. Eyes open. Static.
```

## Dialogue Timing

| Timestamp | Character | Line | Duration |
|-----------|-----------|------|----------|
| 0.6–1.6s | Kiko | "Both arms!" | 1.0s |
| 1.8–3.0s | Mimi | "You're doing it!" | 1.2s |

## Visual Targets

| Element | Target | Tolerance |
|---------|--------|-----------|
| Kiko position | Screen-left, 45% | ±5% |
| Mimi position | Screen-right, 55% | ±5% |
| Coat state | Both arms in, unsnapped | Exact |
| Lighting | Warm golden from right | ±10% warmth |
| Camera height | 0.75m | ±0.05m |

## Quality Benchmarks

- **Resolution**: 1920×1080 minimum
- **Frame rate**: 24fps
- **Style match**: Must match @image1, @image2, @image3
- **Colour palette**: Warm cream, honey wood, terracotta
- **Coat state accuracy**: Both arms clearly in sleeves
- **No artifacts**: Clean, smooth animation
- **No text**: No on-screen文字

## Chain B Reset Checklist

- [ ] Visual quality matches Chain A (Shots 01-04)
- [ ] Character models consistent
- [ ] Environment consistent
- [ ] Coat state tracks correctly from Shot 04
- [ ] Lighting consistent
- [ ] Camera consistent
- [ ] No quality degradation
- [ ] No style drift

## Validation Checklist

- [ ] All 3 reference images loaded
- [ ] Kiko matches @image1 exactly
- [ ] Mimi matches @image2 exactly
- [ ] Environment matches @image3 exactly
- [ ] Coat: both arms in, unsnapped
- [ ] Warm palette throughout
- [ ] Camera at child eye level
- [ ] Eyes open in first frame
- [ ] No on-screen text
- [ ] Dialogue timing correct
- [ ] 15-second duration
- [ ] No background music
- [ ] Safe-exposure compliant
- [ ] Chain B quality reset confirmed
