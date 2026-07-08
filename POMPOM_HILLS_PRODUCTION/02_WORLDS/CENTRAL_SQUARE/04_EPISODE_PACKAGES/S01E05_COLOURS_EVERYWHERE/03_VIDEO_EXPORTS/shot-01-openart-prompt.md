# Shot 01 — OpenArt Prompt

> Bu dosya sadece OpenArt'a verilecek prompt bloklarını içerir.
> Production dokümanı shot-01-kiko-sees-red.md içindeki tam dosya değil.

---

## Visual Prompt

```text
Duration: 15 seconds.

Use @image1 as the exact locked first frame and only visual continuity source.

Do not reinterpret @image1.
Do not use memory of any previous video.
Do not recreate the scene from description.
Only preserve what is visible in @image1.

The clean blue sky from @image1 has absolute priority.
Do not change the sky colour.
Do not warm up the lighting.
Do not create sunset, golden hour, orange sky, dramatic clouds, grey sky, or painterly sky.
Use only the same sky, lighting, colour grading, exposure and contrast from @image1.

0-1 second:
Hold @image1 almost exactly.
No Kiko visible.
No character visible.
No camera movement.
No pull-back.
No push-in.
No zoom.
No pan.
No tilt.
No wider frame.
No new side objects.
No lighting change.
No colour grading change.
Preserve the clean bright blue morning sky from @image1.

After 1 second:
Kiko is visible on the lower-left path inside the same locked @image1 frame, already near the left side but fully or mostly visible.
Kiko is not cropped by the frame edge.
Kiko is not close to the camera.
Kiko is not a foreground close-up.
Kiko remains in correct world scale, about 6-8% of the wide frame.

Do not show a full walking entrance.
Do not move the camera to introduce Kiko.
Do not widen the shot.
Do not recompose the scene.

Kiko remains toddler-like, preschool-safe, soft toy-like, and small within Central Square.
Kiko notices an existing red/pink stepping stone already visible in @image1.
Do not create any new red object.
Do not create a red pot, red bucket, red planter, red vase, or large foreground red prop.

Preserve exactly from @image1:
Big Pompom Tree position, tree size in frame, rounded paths, coloured stepping-stone ring, benches, planters, yellow flowers, purple bunting, distant houses, clean blue sky, cloud shapes, sky proportion, same clean blue morning daylight from @image1, colour grading, exposure and contrast.

No other characters.
No Mimi.
No text.
No captions.
No subtitles.
No speech bubbles.

Dialogue:
Kiko: Red! I found red!
```

---

## Voice Lock

Each character must use their registered locked voice from VOICE_TRACKER.md.
Do not let OpenArt choose or generate voices.
Do not change voice between shots.
Same pitch, same timbre, same age, same speed, same warmth.

## Negative Prompt

```text
camera pull-back, wider first frame, recomposed scene, new establishing shot, camera reset, changed camera angle, changed lighting, changed colour grading, sky colour shift, sunset sky, orange sky, golden sky, grey sky, dramatic sky, Kiko visible in first frame, new character in first 1 second, oversized Kiko, giant foreground character, cropped Kiko, Kiko too close to camera, Kiko dominating frame, new red pot, new red bucket, new red planter, new red vase, large foreground red object, extra characters, Mimi, text, captions, subtitles, speech bubbles
```

---, high contrast, contrast increase, overly saturated, saturation increase, HDR, HDR look, glossy plastic, glossy CGI, harsh highlights, harsh shadows, blown highlights, oversharpened, extra sharp, over-polished CGI, colour drift, exposure drift, saturation drift, contrast drift, dark areas growing darker, highlights growing brighter, lighting becoming harsher


## OpenArt Ayarları

- Duration: 15 seconds
- @image1: Approved Central Square Friends Micro-Opening final frame (temiz mavi gökyüzü)
- Prompt enhancer: Kapalı
- Cinematic/auto camera: Kapalı

---

## Reject Kontrolü

```
0-1 sn:
- Kiko yok mu?
- Kamera aynı mı?
- Ağaç boyutu aynı mı?
- Gökyüzü aynı temiz mavi mi?

1 sn sonrası:
- Kiko küçük mü?
- Kiko lower-left path üzerinde mi?
- Kiko crop değil mi?
- Kiko foreground dev değil mi?
- Kamera geri çekilmedi mi?
- Yeni kırmızı obje çıkmadı mı?
```
