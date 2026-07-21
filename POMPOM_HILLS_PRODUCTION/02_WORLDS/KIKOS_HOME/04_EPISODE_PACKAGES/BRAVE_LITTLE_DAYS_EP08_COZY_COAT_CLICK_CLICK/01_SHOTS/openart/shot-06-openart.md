# Shot 06 — OpenArt Prompt

## Production Metadata

| Field | Value |
|-------|-------|
| Shot | 06 |
| Title | Click Click |
| Spine Step | RELIEF |
| Duration | 15 seconds |
| Characters | Kiko, Mimi |
| Location | Kiko's Home — Entryway |
| Coat State | Being snapped → snapped |

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
- [ ] Close-up framing ready

## Take Shot Prompt

```
@image1 @image2 @image3 CONTINUOUS UNBROKEN 15-SECOND SINGLE TAKE: 3D animated children's show, warm and cozy, soft textures, child-friendly. Entryway, warm setting. Close-up on terracotta coat front. Kiko's small hands and Mimi's soft-blue paw together at coat snap. Snap closing with satisfying click. Both characters' faces partially visible, smiling. Warm golden light focused on snap detail. Close-up, slightly lower angle. Eyes open in first frame. 28-35mm lens, child eye level 0.65m, static camera. Warm golden daytime lighting, soft diffused light from screen-right, no harsh shadows.
```

## Video Prompt (MANDATORY SPOKEN DIALOGUE)

```
@image1 @image2 @image3 CONTINUOUS UNBROKEN 15-SECOND SINGLE TAKE: 3D animated children's show, warm and cozy, soft textures, child-friendly. Entryway, warm setting. Close-up on terracotta coat front. Kiko's small hands and Mimi's soft-blue paw together at coat snap. Snap closing with satisfying click. Both characters' faces partially visible, smiling, Mimi speaking: "Click click!" Warm golden light focused on snap detail. Close-up, slightly lower angle. Eyes open in first frame. 28-35mm lens, child eye level 0.65m, static camera. Warm golden daytime lighting, soft diffused light from screen-right, no harsh shadows.
```

## Dialogue Timing Table

| Timestamp | Character | Line | Duration | Notes |
|-----------|-----------|------|----------|-------|
| 0.8–1.8s | Mimi | "Click click!" | 1.0s | Playful onomatopoeia |

## Prop/Continuity Lock

| Prop | State | Position | Notes |
|------|-------|----------|-------|
| Coat | Being snapped → snapped | On Kiko's body | Front closure |
| Snap mechanism | Open → closed | Center of coat | The click-click! |
| Coat rack | Standing | Screen-left, 20% | Empty |

## Audio/Voice Lock

| Element | Description | Level | Timing |
|---------|-------------|-------|--------|
| Ambience | Quiet home, distant birds | -18dB | Continuous |
| SFX | **CLICK-CLICK** (snap) | -6dB | 1.8-3.0s |
| SFX | Kiko's giggle | -10dB | 3.0-6.0s |
| Dialogue | Mimi: "Click click!" | 0dB | 0.8-1.8s |

## Negative Prompt

No crying, no tears, no tantrum, no yelling, no anger, no fear, no sadness. No dark shadows, no cold lighting, no dramatic lighting, no HDR, no cinematic LUT. No fast camera movements, no zooms, no Dutch angles, no shaky cam. No background music, no instruments, no singing, no humming. No on-screen text, no subtitles, no logos, no watermarks. No other characters, no background people, no pets. No complex backgrounds, no clutter, no mess. No modern technology, no screens, no phones. No food, no eating, no drinking. No sleeping, no yawning. No wet conditions, no rain, no snow. No sharp objects, no dangerous items.

## Final QA Checklist

- [ ] All 3 reference images loaded correctly
- [ ] Kiko matches @image1 exactly
- [ ] Mimi matches @image2 exactly
- [ ] Environment matches @image3 exactly
- [ ] Close-up on coat snap
- [ ] Click-click sound clear and satisfying
- [ ] Mimi dialogue included: "Click click!"
- [ ] Kiko giggles after snap
- [ ] Eyes open in first frame
- [ ] Warm palette throughout
- [ ] Camera slightly lower (0.65m)
- [ ] No on-screen text
- [ ] No background music
- [ ] 15-second duration
- [ ] Safe-exposure compliant
