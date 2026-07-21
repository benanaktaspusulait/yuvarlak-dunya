# Shot 02 — OpenArt Prompt

## Production Metadata

| Field | Value |
|-------|-------|
| Shot | 02 |
| Title | I Can't Do It |
| Spine Step | FEELING |
| Duration | 15 seconds |
| Characters | Kiko, Mimi |
| Location | Kiko's Home — Entryway |
| Coat State | Half-on (attempting) |

## Reference Upload Map

| Ref # | Image | Description | Usage |
|-------|-------|-------------|-------|
| @image1 | Kiko character model | Full-body, coral-pink top, white shorts, brown pigtails | Character consistency |
| @image2 | Mimi character model | Full-body, soft-blue rabbit, yellow top | Character consistency |
| @image3 | Entryway environment | Warm cream walls, honey wood floor, coat rack, door | Environment consistency |

## Hard Gate Before Generation

- [ ] @image1 loaded: Kiko visible, correct outfit
- [ ] @image2 loaded: Mimi visible, correct outfit
- [ ] @image3 loaded: Entryway, warm palette
- [ ] All references match episode style
- [ ] No conflicting references
- [ ] Warm colour palette confirmed
- [ ] Coat prop ready for half-on state

## Take Shot Prompt

```
@image1 @image2 @image3 CONTINUOUS UNBROKEN 15-SECOND SINGLE TAKE: 3D animated children's show, warm and cozy, soft textures, child-friendly. Entryway, same warm setting. Kiko, 3-4 year old girl, coral-pink top, white shorts, brown pigtails, screen-left, trying to put on terracotta coat, arms slightly tangled, mild frustrated expression, eyes open. Coat half-on, one sleeve dangling. Mimi, soft-blue rabbit, yellow top, screen-right background, watching with gentle concern. Warm golden light, soft shadows. Child eye level, medium shot. Eyes open in first frame. 28-35mm lens, child eye level 0.75m, slow subtle push-in. Warm golden daytime lighting, soft diffused light from screen-right, no harsh shadows.
```

## Video Prompt (MANDATORY SPOKEN DIALOGUE)

```
@image1 @image2 @image3 CONTINUOUS UNBROKEN 15-SECOND SINGLE TAKE: 3D animated children's show, warm and cozy, soft textures, child-friendly. Entryway, same warm setting. Kiko, 3-4 year old girl, coral-pink top, white shorts, brown pigtails, screen-left, trying to put on terracotta coat, arms slightly tangled, mild frustrated expression, eyes open, speaking: "I can't do it..." Coat half-on, one sleeve dangling. Mimi, soft-blue rabbit, yellow top, screen-right background, watching with gentle concern, speaking: "It's tricky." Warm golden light, soft shadows. Child eye level, medium shot. Eyes open in first frame. 28-35mm lens, child eye level 0.75m, slow subtle push-in. Warm golden daytime lighting, soft diffused light from screen-right, no harsh shadows.
```

## Dialogue Timing Table

| Timestamp | Character | Line | Duration | Notes |
|-----------|-----------|------|----------|-------|
| 0.6–2.0s | Kiko | "I can't do it..." | 1.4s | Mild frustration |
| 2.2–3.4s | Mimi | "It's tricky." | 1.2s | Gentle acknowledgment |

## Prop/Continuity Lock

| Prop | State | Position | Notes |
|------|-------|----------|-------|
| Coat | Half-on, tangled | On Kiko's body | One sleeve dangling |
| Coat rack | Standing | Screen-left, 20% | Empty |
| Door | Closed | Screen-right | Glass panels |

## Audio/Voice Lock

| Element | Description | Level | Timing |
|---------|-------------|-------|--------|
| Ambience | Quiet home, distant birds | -18dB | Continuous |
| SFX | Fabric rustling | -12dB | 0.0-15.0s |
| Dialogue | Kiko: "I can't do it..." | 0dB | 0.6-2.0s |
| Dialogue | Mimi: "It's tricky." | 0dB | 2.2-3.4s |

## Negative Prompt

No crying, no tears, no tantrum, no yelling, no anger, no fear, no sadness. No dark shadows, no cold lighting, no dramatic lighting, no HDR, no cinematic LUT. No fast camera movements, no zooms, no Dutch angles, no shaky cam. No background music, no instruments, no singing, no humming. No on-screen text, no subtitles, no logos, no watermarks. No other characters, no background people, no pets. No complex backgrounds, no clutter, no mess. No modern technology, no screens, no phones. No food, no eating, no drinking. No sleeping, no yawning. No wet conditions, no rain, no snow. No sharp objects, no dangerous items.

## Final QA Checklist

- [ ] All 3 reference images loaded correctly
- [ ] Kiko matches @image1 exactly
- [ ] Mimi matches @image2 exactly
- [ ] Environment matches @image3 exactly
- [ ] Coat: half-on, one sleeve dangling
- [ ] Kiko screen-left, frustrated expression
- [ ] Mimi screen-right, concerned expression
- [ ] Kiko dialogue included: "I can't do it..."
- [ ] Mimi dialogue included: "It's tricky."
- [ ] Eyes open in first frame
- [ ] Warm palette throughout
- [ ] Camera at child eye level with subtle push-in
- [ ] No on-screen text
- [ ] No background music
- [ ] 15-second duration
- [ ] Safe-exposure compliant (mild frustration only)
