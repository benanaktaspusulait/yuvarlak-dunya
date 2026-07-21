# Shot 05 — OpenArt Prompt

## Production Metadata

| Field | Value |
|-------|-------|
| Shot | 05 |
| Title | The Other Arm |
| Spine Step | ACTION |
| Duration | 15 seconds |
| Characters | Kiko, Mimi |
| Location | Kiko's Home — Entryway |
| Coat State | Both arms in (unsnapped) |

## Reference Upload Map

| Ref # | Image | Description | Usage |
|-------|-------|-------------|-------|
| @image1 | Kiko with coat (both arms in) | Coral-pink top, white shorts, brown pigtails, terracotta coat | Character + coat state |
| @image2 | Mimi character model | Soft-blue rabbit, yellow top | Character consistency |
| @image3 | Entryway environment | Warm cream walls, honey wood floor, coat rack, door | Environment consistency |

## Hard Gate Before Generation

- [ ] @image1 loaded: Kiko with coat, both arms in sleeves
- [ ] @image2 loaded: Mimi visible, correct outfit
- [ ] @image3 loaded: Entryway, warm palette
- [ ] Coat state matches Shot 04 ending
- [ ] All references match episode style
- [ ] No conflicting references
- [ ] Warm colour palette confirmed

## Take Shot Prompt

```
@image1 @image2 @image3 CONTINUOUS UNBROKEN 15-SECOND SINGLE TAKE: 3D animated children's show, warm and cozy, soft textures, child-friendly. Entryway, warm setting. Kiko, 3-4 year old girl, coral-pink top, white shorts, brown pigtails, screen-left, both arms now in terracotta coat sleeves, looking down at herself with amazed expression, eyes open. Mimi, soft-blue rabbit, yellow top, screen-right, beaming with pride. Coat on but unsnapped. Warm golden light. Medium shot, child eye level. Eyes open in first frame. 28-35mm lens, child eye level 0.75m, static camera. Warm golden daytime lighting, soft diffused light from screen-right, no harsh shadows.
```

## Video Prompt (MANDATORY SPOKEN DIALOGUE)

```
@image1 @image2 @image3 CONTINUOUS UNBROKEN 15-SECOND SINGLE TAKE: 3D animated children's show, warm and cozy, soft textures, child-friendly. Entryway, warm setting. Kiko, 3-4 year old girl, coral-pink top, white shorts, brown pigtails, screen-left, both arms now in terracotta coat sleeves, looking down at herself with amazed expression, eyes open, speaking: "Both arms!" Mimi, soft-blue rabbit, yellow top, screen-right, beaming with pride, speaking: "You're doing it!" Coat on but unsnapped. Warm golden light. Medium shot, child eye level. Eyes open in first frame. 28-35mm lens, child eye level 0.75m, static camera. Warm golden daytime lighting, soft diffused light from screen-right, no harsh shadows.
```

## Dialogue Timing Table

| Timestamp | Character | Line | Duration | Notes |
|-----------|-----------|------|----------|-------|
| 0.6–1.6s | Kiko | "Both arms!" | 1.0s | Proud exclamation |
| 1.8–3.0s | Mimi | "You're doing it!" | 1.2s | Warm praise |

## Prop/Continuity Lock

| Prop | State | Position | Notes |
|------|-------|----------|-------|
| Coat | Both arms in, unsnapped | On Kiko's body | Sleeves on, front open |
| Coat rack | Standing | Screen-left, 20% | Empty |
| Door | Closed | Screen-right | Glass panels |

## Audio/Voice Lock

| Element | Description | Level | Timing |
|---------|-------------|-------|--------|
| Ambience | Quiet home, distant birds | -18dB | Continuous |
| SFX | Fabric slide | -12dB | 0.0-2.0s |
| Dialogue | Kiko: "Both arms!" | 0dB | 0.6-1.6s |
| Dialogue | Mimi: "You're doing it!" | 0dB | 1.8-3.0s |

## Negative Prompt

No crying, no tears, no tantrum, no yelling, no anger, no fear, no sadness. No dark shadows, no cold lighting, no dramatic lighting, no HDR, no cinematic LUT. No fast camera movements, no zooms, no Dutch angles, no shaky cam. No background music, no instruments, no singing, no humming. No on-screen text, no subtitles, no logos, no watermarks. No other characters, no background people, no pets. No complex backgrounds, no clutter, no mess. No modern technology, no screens, no phones. No food, no eating, no drinking. No sleeping, no yawning. No wet conditions, no rain, no snow. No sharp objects, no dangerous items.

## Final QA Checklist

- [ ] All 3 reference images loaded correctly
- [ ] Kiko matches @image1 exactly
- [ ] Mimi matches @image2 exactly
- [ ] Environment matches @image3 exactly
- [ ] Coat: both arms in, unsnapped
- [ ] Kiko screen-left, amazed expression
- [ ] Mimi screen-right, proud expression
- [ ] Kiko dialogue included: "Both arms!"
- [ ] Mimi dialogue included: "You're doing it!"
- [ ] Eyes open in first frame
- [ ] Warm palette throughout
- [ ] Camera static at child eye level
- [ ] No on-screen text
- [ ] No background music
- [ ] 15-second duration
- [ ] Safe-exposure compliant
- [ ] Chain B quality reset confirmed
