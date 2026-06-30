# Pompom Hills Negative Prompts v2.1

Bu dosya Midjourney, SDXL ve Flux üretimlerinde ortak yasak listesidir. Pozitif prompt ne kadar iyi olursa olsun, bu liste her üretimde kullanılmalıdır.

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
