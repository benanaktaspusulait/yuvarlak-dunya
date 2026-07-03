# 17 — Video Generation Standard

> Tüm shot dosyaları bu standarttan üretir.
> Her shot bu dosyaya atıfta bulunur, aynı kuralları tekrar etmez.

---

## First Frame Lock

Shot 02+ için:

Treat @image1 as the complete visual master reference.

The first visible frame must be visually indistinguishable from @image1.

Only after the first frame matches perfectly may animation begin.

Do not reinterpret @image1.
Do not reposition the camera.
Do not recompose the scene.
Do not adjust framing before movement begins.

---

## Voice Continuity

The speaking voices MUST remain identical across the whole episode.

Maintain:
- same voice identity per character
- same pitch
- same timbre
- same speaking speed
- same warmth
- same preschool naturalness

Do not generate a narrator.
Do not generate alternate voices.

---

## Colour Continuity

Match the colour grading of the previous shot exactly.

Treat the previous shot as the colour master reference. Never rebalance colours between shots.

Maintain:
- identical white balance
- identical warmth
- identical exposure
- identical saturation
- identical pastel palette
- identical contrast

Avoid:
- blue tint
- green tint
- orange shift
- HDR look
- cinematic LUT

The entire episode must appear colour graded as one continuous film.

---

## Lighting Continuity

Preserve the lighting from the previous shot exactly.

Maintain:
- identical light direction
- identical light intensity
- identical shadow softness
- identical ambient lighting
- identical highlight behaviour

Do not reinterpret the lighting. Continue it.

---

## Camera Rules

- Child eye level throughout
- Gentle 35mm framing
- Slow stable movement
- No zoom
- No handheld motion
- No sudden camera reset
- No tight framing

---

## Text Safety

Do not display dialogue as on-screen text.

No speech bubbles.
No captions.
No subtitles.
No text.

---

## Ball Continuity

The same round yellow ball must persist through the entire episode.

The ball must not change colour, size, texture, or shape.

---

## World Continuity

Central Square must remain visually consistent.

- Big Pompom Tree in background whenever composition allows
- Warm morning light throughout
- Soft pastel colours
- Safe open play space
- No new environment
- No extra characters
- No redesign

---

## Scale

Characters should feel small and childlike within Central Square, but must remain readable for facial expression and action.

Use wide framing for environment identity and medium framing for emotional beats.

---

## Animation Quality

- All movements slow and natural
- No sudden gestures
- No fast cuts
- Characters never fully frozen — idle animations present
- Grass moves gently in wind
- Environmental rhythm consistent

---

## Child Safety

- No sharp edges or dark shadows
- No threatening imagery
- All characters express only positive or gently curious emotions
- No violence, conflict, or distressing content
- Soft and safe throughout

---

## How to Use This Standard

In each shot file, replace the repeated sections with:

```text
Use the production generation standard (17_VIDEO_GENERATION_STANDARD.md).

First frame: Continue from @image1.
Location: Central Square.
Lighting: Warm morning light.
Ball: Same round yellow ball.
```

This keeps shot files short and maintainable.

---

*Bu belge tüm shot'lar için tek kaynaktır.*
*Versiyon: 1.0*
