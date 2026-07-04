# Pompom Hills Negative Prompts v2.2

Bu dosya Midjourney, SDXL ve Flux üretimlerinde ortak yasak listesidir. Pozitif prompt ne kadar iyi olursa olsun, bu liste her üretimde kullanılmalıdır.

## Negative Prompt Philosophy ⭐

> Added by the Visual Richness and World Charm decision (4 Temmuz 2026).
> See `POMPOM_HILLS_PRODUCTION/02_WORLDS/GLOBAL_ENVIRONMENT_STANDARD.md` § Negative Prompt Philosophy.

Negative prompts must prevent drift, not remove charm. Avoid generic
"no detail" language that accidentally strips out a world's Allowed Charm
Details along with the clutter you actually meant to block.

```
Bad:  no objects, no props, no houses, no details, no decorations, no texture
Good: no random clutter, no non-canon objects, no sharp edges, no photorealism,
      no dark mood, no modern objects, no readable text
```

The lists below already follow this philosophy (they target specific unsafe
or off-canon elements, not "detail" in general) — keep any future additions
consistent with it.

## Common Negative Prompt

```text
sharp edges, angular shapes, realistic skin texture, realistic pores, realistic fur, horror, violence, weapons, blood, injury, crying meltdown, screaming, angry adult face, punishment, bullying, sarcasm, dark shadows, black background, harsh rim light, high contrast, neon colors, dirty grunge texture, photorealism, text, watermark, logo, extra fingers, visible fingernails, sharp teeth, sharp beak, claws, city street, cars, traffic, cliff, deep tunnel, scary forest, lightning, fire, smoke, handheld camera, Dutch angle, fisheye, cluttered background, unsafe height, adult proportions
```

## Midjourney v6 Negative

```text
--no sharp edges, angular shapes, realistic skin texture, realistic pores, realistic fur, horror, violence, weapons, blood, injury, crying meltdown, screaming, punishment, bullying, dark shadows, black background, harsh rim light, high contrast, neon colors, dirty grunge texture, photorealism, watermark, logo, extra fingers, fingernails, sharp teeth, sharp beak, claws, cars, city street, cliff, deep tunnel, scary forest, lightning, fire, smoke, handheld camera, Dutch angle, fisheye, clutter
```

## SDXL Negative

```text
sharp edges, angular shapes, realistic skin texture, pores, realistic fur strands, horror lighting, violence, weapon, blood, bruises, injury, crying meltdown, screaming mouth, angry eyebrows, punishment scene, bully, dark shadows, black night, harsh rim light, neon, grunge, dirty texture, photorealistic, text, watermark, logo, extra fingers, fingernails, sharp teeth, sharp beak, claws, car, city, cliff, tunnel, scary forest, lightning, fire, smoke, shaky camera, Dutch angle, fisheye, cluttered background, unsafe height, adult body proportions, low quality, noisy, over-detailed
```

## Flux Negative Guidance

Flux modellerinde negatif prompt desteği araca göre değişir. Destek varsa aşağıdaki listeyi negative alanına koy. Destek yoksa pozitif prompt sonuna "avoid..." cümlesi olarak ekle.

```text
avoid sharp edges, realistic skin texture, horror, violence, text, watermark, dark shadows, photorealism, extra fingers, sharp teeth, claws, city streets, cars, cliffs, scary forest, lightning, cluttered background, adult proportions
```

## 3D Production Avoid List

```text
razor bevels, real fur particles, hair strand simulation, pore displacement, fabric weave close-up, metallic glasses glare, hard ray-traced face shadows, black unlit background, high-frequency grass, tiny unreadable props, sharp branch silhouettes, unsafe staircases, steep cliffs, fast slapstick crash, aggressive camera shake
```

## OpenArt Production Failure Modes

OpenArt testleriyle doğrulanmış hata modlarına karşı koruma. Sahne (Director) promptlarında,
karakter var olan LOCKED dünyaya yerleştirilirken bu bloğu negative alanına ekle
(bkz. `PRODUCTION_PIPELINE.md` "Known OpenArt Failure Modes" bölümü).

```text
oversized character, giant character, character too large, character filling the frame, tiny environment, shrunken world, regenerated architecture, redesigned buildings, different house style, different trees, altered tree shape, brown pompom tree, reshaped Giant Pompom Tree, moved landmark, different flower layout, rearranged flowers, changed world layout, different paths, different lighting, environment sheet in scene, reference sheet visible, labels, arrows, layout diagram, frame border, random text, random signs, sign artifacts, watermark, extra characters
```

### Locked-World Positive Reinforcement (negatif ile birlikte kullan)

```text
environment is LOCKED and identical to the world reference, do not redesign architecture trees flowers paths benches lamp posts or landmarks, keep Giant Pompom Tree identical in shape position scale and color #81C784, insert character only, environment is the visual hero, character occupies about 10-12 percent of the frame, 35mm eye level, generous negative space
```
