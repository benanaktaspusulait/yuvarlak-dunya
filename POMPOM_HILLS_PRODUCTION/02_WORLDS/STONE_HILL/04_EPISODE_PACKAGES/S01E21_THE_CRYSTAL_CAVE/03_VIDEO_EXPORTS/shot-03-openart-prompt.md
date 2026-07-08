# Shot 03 — OpenArt Prompt

## Visual Prompt

```text
Duration: 15 seconds.

Use @image1 as the exact locked first frame and only visual continuity source.
Do not reinterpret @image1.

Continue directly from the previous shot video reference.
The opening frame must continue seamlessly from the previous shot reference.

Crystal Cave interior background is locked from the first frame.
Warm pastel colors, round soft shapes, crystals on walls and ceiling.

Wide view of cave interior, crystals catching light and casting soft sparkles on walls.
Luca steps forward, eyes wide, light reflecting on face.
Luca is light blue (#81D4FA), toddler-like, preschool-safe, soft toy-like.
Kiko reaches toward a crystal cluster, fingers almost touching, light shimmers across hand.
Kiko is coral pink (#F8BBD0), toddler-like, preschool-safe, soft toy-like.
Luca turns slowly, scanning the ceiling crystals, mouth slightly open in wonder.
Both stand together gazing upward, subtle body sway reflecting the crystal light patterns.
Kiko gently points at a particular crystal, Luca follows the gesture, both smiling softly.

Preserve exactly from @image1:
All visible crystals, cave walls, light patterns, warm pastel colour grading, exposure and contrast.

No other characters.
No text.
No captions.

Dialogue:
Luca: The crystals are shining!
```

## Voice Lock

Each character must use their registered locked voice from VOICE_TRACKER.md.
Do not let OpenArt choose or generate voices.
Do not change voice between shots.
Same pitch, same timbre, same age, same speed, same warmth.

## Negative Prompt

```text
camera pull-back, wider first frame, recomposed scene, changed camera angle, changed lighting, changed colour grading, extra characters, text, captions, subtitles, speech bubbles, background music, music, melody, song, soundtrack, static talking pose, characters frozen
```, high contrast, contrast increase, overly saturated, saturation increase, HDR, HDR look, glossy plastic, glossy CGI, harsh highlights, harsh shadows, blown highlights, oversharpened, extra sharp, over-polished CGI, colour drift, exposure drift, saturation drift, contrast drift, dark areas growing darker, highlights growing brighter, lighting becoming harsher


## OpenArt Ayarları

- Duration: 15 seconds
- @image1: Previous shot video reference (shot-02 final frame)
- Prompt enhancer: Kapalı
- Cinematic/auto camera: Kapalı
