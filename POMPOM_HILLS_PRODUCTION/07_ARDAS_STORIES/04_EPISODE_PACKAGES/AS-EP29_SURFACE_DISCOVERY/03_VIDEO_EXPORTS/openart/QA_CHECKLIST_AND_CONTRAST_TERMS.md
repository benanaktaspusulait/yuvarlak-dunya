# QA Checklist and Contrast Terms — AS-EP29 Surface Discovery

## Per-Shot QA Checklist (apply to every shot)

- [ ] Character identity preserved (Arda / Luca / Noah)
- [ ] Acorn prop consistent (warm brown, round, 3 cm, child-safe)
- [ ] No camera movement (locked camera)
- [ ] No dialogue as on-screen text
- [ ] No music, no background music
- [ ] No new characters or objects appearing unexpectedly
- [ ] Soft pastel preschool look maintained
- [ ] No contrast increase, no saturation drift
- [ ] No HDR, no glossy look, no oversharpening
- [ ] Warm natural lighting preserved
- [ ] First 0.5s is stable and edit-safe
- [ ] Final 0.5s is calm and transition-safe
- [ ] No background object morphing or shifting
- [ ] Characters do not freeze or become static

## Transition QA (Shot-to-Shot)

- [ ] Previous shot final frame matches next shot first frame
- [ ] No camera reset between shots
- [ ] No environment shift between shots
- [ ] Character scale stays consistent
- [ ] Background/world-locked elements stay in same layout
- [ ] Acorn prop stays consistent between shots
- [ ] Colour does not fade or shift
- [ ] Transition feels like continuation, not new setup

## Colour / Contrast Stability Terms (add to every OpenArt prompt)

```
Colour / Contrast Stability:
Use @image1 for continuity, first-frame composition, character positions, object layout and
action placement.
Use the Episode Colour Master for colour, brightness, contrast, saturation, shadow softness
and matte material feel.
If the production tool supports multiple image references, upload the Episode Colour Master
as @image2.
@image2 = Episode Colour Master only. Do not copy @image2 camera, framing, character
position, background layout, or action.
If @image1 has accumulated video-generation drift and is darker, harsher, sharper, glossier,
more saturated, or more contrasty than @image2, keep @image1 composition but correct colour
back toward @image2.
Preserve the soft pastel preschool look.
Preserve medium-low contrast.
Preserve warm morning dappled sunlight.
Preserve gentle golden warmth.
Preserve soft shadows.
Preserve matte handcrafted toy-set materials.
Do not increase contrast.
Do not increase saturation.
Do not add HDR effect.
Do not add extra sharpening.
Do not add glossy plastic highlights.
Do not create harsher shadows.
Do not brighten highlights into a blown-out look.
Do not make dark areas deeper or more cave-like.
Do not make the scene look more intense than @image1.
If any adjustment happens, it should be slightly softer and calmer, never stronger,
sharper, glossier, darker, or more contrasty.
```

## OpenArt Contrast Terms (add to every negative prompt)

```
high contrast, contrast increase, overly saturated, saturation increase, HDR, HDR look,
glossy plastic, glossy CGI, harsh highlights, harsh shadows, blown highlights,
oversharpened, extra sharp, over-polished CGI, colour drift, exposure drift, saturation
drift, contrast drift, dark areas growing darker, highlights growing brighter, lighting
becoming harsher
```

## Voice Lock Terms (add to every prompt with dialogue)

```
Voice Lock:
Each character must use their registered locked voice from VOICE_TRACKER.md.
Do not let OpenArt choose or generate voices.
Do not change voice between shots.
Same pitch, same timbre, same age, same speed, same warmth.
```

## Pompom Item Checklist

- [ ] At least 1 Pompom item included in the episode (background detail acceptable)
- [ ] Pompom items are round, fluffy, and soft-looking
- [ ] No sharp edges or hard textures on Pompom items

## Episode-Level Verification

- [ ] All 8 shots follow the @image1 continuity chain
- [ ] Episode Colour Master established from Shot 01
- [ ] Repeated rhyme appears at least twice (Shots 08, 16, 23)
- [ ] Arda resolves the central problem through his own observation
- [ ] Supporting characters do not solve Arda's problem for him
- [ ] No burned-in titles, numbers, arrows, captions, or lesson cards
- [ ] Master video contains no burned-in text
