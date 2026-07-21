# Shot 01 — OpenArt Prompt

## Production Metadata

| Field | Value |
|-------|-------|
| Shot | 01 |
| Title | A Coat on the Chair |
| Spine Step | PROBLEM |
| Duration | 15 seconds |
| Characters | Kiko, Mimi |
| Location | Kiko's Home — Entryway |
| Coat State | Hanging on rack |

## Reference Upload Map

| Ref # | Image | Description | Usage |
|-------|-------|-------------|-------|
| @image1 | Kiko character model | Full-body, coral-pink top, white shorts, brown pigtails | Character consistency |
| @image2 | Mimi character model | Full-body, soft-blue rabbit, yellow top | Character consistency |
| @image3 | Entryway environment | Warm cream walls, honey wood floor, coat rack, door | Environment consistency |

## Hard Gate Before Generation

- [ ] @image1 loaded: Kiko visible, correct outfit, screen-left ready
- [ ] @image2 loaded: Mimi visible, correct outfit, screen-right ready
- [ ] @image3 loaded: Entryway, warm palette, coat rack visible
- [ ] All references match episode style
- [ ] No conflicting references
- [ ] Warm colour palette confirmed
- [ ] Coat prop ready on rack

## Take Shot Prompt

```
@image1 @image2 @image3 CONTINUOUS UNBROKEN 15-SECOND SINGLE TAKE: 3D animated children's show, warm and cozy, soft textures, child-friendly. Entryway of cozy home, warm cream walls, honey wood floor. Terracotta coat hanging on wooden coat rack, screen-left. Kiko, 3-4 year old girl, coral-pink top, white shorts, brown pigtails, screen-left, looking at coat with excited expression, eyes open. Mimi, soft-blue rabbit, yellow top, screen-right, standing near front door with glass panels, warm smile. Warm daytime, soft golden light through door. Low visual density, simple uncluttered space. Eyes open in first frame. 28-35mm lens, child eye level 0.75m, static camera. No camera movement. Warm golden daytime lighting, soft diffused light from screen-right, no harsh shadows.
```

## Video Prompt (MANDATORY SPOKEN DIALOGUE)

```
@image1 @image2 @image3 CONTINUOUS UNBROKEN 15-SECOND SINGLE TAKE: 3D animated children's show, warm and cozy, soft textures, child-friendly. Entryway of cozy home, warm cream walls, honey wood floor. Terracotta coat hanging on wooden coat rack, screen-left. Kiko, 3-4 year old girl, coral-pink top, white shorts, brown pigtails, screen-left, looking at coat with excited expression, eyes open. Mimi, soft-blue rabbit, yellow top, screen-right, standing near front door with glass panels, warm smile, speaking: "Your coat is ready!" Warm daytime, soft golden light through door. Low visual density, simple uncluttered space. Eyes open in first frame. 28-35mm lens, child eye level 0.75m, static camera. No camera movement. Warm golden daytime lighting, soft diffused light from screen-right, no harsh shadows.
```

## Dialogue Timing Table

| Timestamp | Character | Line | Duration | Notes |
|-----------|-----------|------|----------|-------|
| 0.4–1.8s | Mimi | "Your coat is ready!" | 1.4s | Warm, inviting tone |

## Prop/Continuity Lock

| Prop | State | Position | Notes |
|------|-------|----------|-------|
| Coat | Hanging on rack | Screen-left, 25% | Terracotta/rust |
| Coat rack | Standing | Screen-left, 20% | Wooden |
| Door | Closed | Screen-right | Glass panels |
| Potted plant | Static | Screen-left corner | Green |

## Audio/Voice Lock

| Element | Description | Level | Timing |
|---------|-------------|-------|--------|
| Ambience | Quiet home, distant birds | -18dB | Continuous |
| SFX | Soft fabric rustle | -12dB | 0.0-2.0s |
| Dialogue | Mimi: "Your coat is ready!" | 0dB | 0.4-1.8s |

## Negative Prompt

No crying, no tears, no tantrum, no yelling, no anger, no fear, no sadness. No dark shadows, no cold lighting, no dramatic lighting, no HDR, no cinematic LUT. No fast camera movements, no zooms, no Dutch angles, no shaky cam. No background music, no instruments, no singing, no humming. No on-screen text, no subtitles, no logos, no watermarks. No other characters, no background people, no pets. No complex backgrounds, no clutter, no mess. No modern technology, no screens, no phones. No food, no eating, no drinking. No sleeping, no yawning. No wet conditions, no rain, no snow. No sharp objects, no dangerous items.

## Final QA Checklist

- [ ] All 3 reference images loaded correctly
- [ ] Kiko matches @image1 exactly
- [ ] Mimi matches @image2 exactly
- [ ] Environment matches @image3 exactly
- [ ] Coat is on rack (hanging)
- [ ] Kiko screen-left, excited expression
- [ ] Mimi screen-right, warm smile
- [ ] Mimi dialogue included: "Your coat is ready!"
- [ ] Eyes open in first frame
- [ ] Warm palette throughout
- [ ] Camera static at child eye level
- [ ] No on-screen text
- [ ] No background music
- [ ] 15-second duration
- [ ] Safe-exposure compliant
