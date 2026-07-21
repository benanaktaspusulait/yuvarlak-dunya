# Shot 04 — OpenArt Prompt

## Production Metadata

| Field | Value |
|-------|-------|
| Shot | 04 |
| Title | One Arm In |
| Spine Step | ACTION |
| Duration | 15 seconds |
| Characters | Kiko, Mimi |
| Location | Kiko's Home — Entryway |
| Coat State | One arm in |

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
- [ ] Coat one arm in state ready

## Take Shot Prompt

```
@image1 @image2 @image3 CONTINUOUS UNBROKEN 15-SECOND SINGLE TAKE: 3D animated children's show, warm and cozy, soft textures, child-friendly. Entryway, warm setting. Kiko, 3-4 year old girl, coral-pink top, white shorts, brown pigtails, screen-left, one arm successfully in terracotta coat sleeve, amazed happy expression, eyes open. Mimi, soft-blue rabbit, yellow top, screen-right, guiding Kiko's arm, encouraging smile. One arm in coat, other sleeve hanging. Warm golden light. Medium shot, child eye level. Eyes open in first frame. 28-35mm lens, child eye level 0.75m, static camera. Warm golden daytime lighting, soft diffused light from screen-right, no harsh shadows.
```

## Video Prompt (MANDATORY SPOKEN DIALOGUE)

```
@image1 @image2 @image3 CONTINUOUS UNBROKEN 15-SECOND SINGLE TAKE: 3D animated children's show, warm and cozy, soft textures, child-friendly. Entryway, warm setting. Kiko, 3-4 year old girl, coral-pink top, white shorts, brown pigtails, screen-left, one arm successfully in terracotta coat sleeve, amazed happy expression, eyes open, speaking: "One arm is in!" Mimi, soft-blue rabbit, yellow top, screen-right, guiding Kiko's arm, encouraging smile, speaking: "Now the other one." One arm in coat, other sleeve hanging. Warm golden light. Medium shot, child eye level. Eyes open in first frame. 28-35mm lens, child eye level 0.75m, static camera. Warm golden daytime lighting, soft diffused light from screen-right, no harsh shadows.
```

## Dialogue Timing Table

| Timestamp | Character | Line | Duration | Notes |
|-----------|-----------|------|----------|-------|
| 0.8–2.2s | Kiko | "One arm is in!" | 1.4s | Excited discovery |
| 2.4–3.8s | Mimi | "Now the other one." | 1.4s | Encouraging guidance |

## Prop/Continuity Lock

| Prop | State | Position | Notes |
|------|-------|----------|-------|
| Coat | One arm in | On Kiko's body | One sleeve on, one hanging |
| Coat rack | Standing | Screen-left, 20% | Empty |
| Door | Closed | Screen-right | Glass panels |

## Audio/Voice Lock

| Element | Description | Level | Timing |
|---------|-------------|-------|--------|
| Ambience | Quiet home, distant birds | -18dB | Continuous |
| SFX | Fabric slide | -12dB | 0.0-3.0s |
| Dialogue | Kiko: "One arm is in!" | 0dB | 0.8-2.2s |
| Dialogue | Mimi: "Now the other one." | 0dB | 2.4-3.8s |

## Negative Prompt

No crying, no tears, no tantrum, no yelling, no anger, no fear, no sadness. No dark shadows, no cold lighting, no dramatic lighting, no HDR, no cinematic LUT. No fast camera movements, no zooms, no Dutch angles, no shaky cam. No background music, no instruments, no singing, no humming. No on-screen text, no subtitles, no logos, no watermarks. No other characters, no background people, no pets. No complex backgrounds, no clutter, no mess. No modern technology, no screens, no phones. No food, no eating, no drinking. No sleeping, no yawning. No wet conditions, no rain, no snow. No sharp objects, no dangerous items.

## Final QA Checklist

- [ ] All 3 reference images loaded correctly
- [ ] Kiko matches @image1 exactly
- [ ] Mimi matches @image2 exactly
- [ ] Environment matches @image3 exactly
- [ ] Coat: one arm in, one sleeve hanging
- [ ] Kiko screen-left, amazed expression
- [ ] Mimi screen-right, encouraging smile
- [ ] Kiko dialogue included: "One arm is in!"
- [ ] Mimi dialogue included: "Now the other one."
- [ ] Eyes open in first frame
- [ ] Warm palette throughout
- [ ] Camera static at child eye level
- [ ] No on-screen text
- [ ] No background music
- [ ] 15-second duration
- [ ] Safe-exposure compliant
