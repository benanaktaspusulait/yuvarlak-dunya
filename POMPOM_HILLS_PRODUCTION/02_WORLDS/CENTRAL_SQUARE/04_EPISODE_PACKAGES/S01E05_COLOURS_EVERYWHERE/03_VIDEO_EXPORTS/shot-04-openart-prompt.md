# Shot 04 — OpenArt Prompt

> Bu dosya sadece OpenArt'a verilecek prompt bloklarını içerir.
> Shot 03 approved final frame: Kiko ve Mimi birlikte, blue bench görünür.

---

## Visual Prompt

```text
Duration: 15 seconds.

Use @image1 as the exact first frame and only visual continuity source.

Do not reinterpret @image1.
Do not use memory of any previous video or previous shot.
Do not recreate the scene from description.
Only preserve what is visible in @image1.

The clean sky and lighting from @image1 have absolute priority.
Use only the same sky, lighting, colour grading, exposure, contrast and colour temperature from @image1.
Do not warm up the lighting.
Do not create sunset, golden hour, orange sky, grey sky, dramatic clouds, painterly sky, or lighting reinterpretation.

The yellow flowers must already be visible inside the existing mixed flowerbed / planter area in @image1.
Do not create a new yellow flower planter.
Do not create a new flower cluster.
Do not create a new garden, meadow, Flower Hill, flower field, or alternate location.
Do not use camera movement to search for flowers.
The characters simply notice the already-visible yellow flowers that are part of the existing @image1 background.

The blue bench, Big Pompom Tree, stepping stones, paths, flowerbeds, distant houses and all visible background objects remain stable.
Do not move, duplicate, repaint, resize, replace, reveal, or newly generate any background object.

0-1 second:
Hold @image1 almost exactly.
Kiko and Mimi remain visible in the same positions, scale and general direction from @image1.
Only tiny natural idle motion is allowed: blinking, breathing, tiny smile, slight head movement.
No camera movement.
No lighting change.
No new flowers.
No new planter.
No object pop-in.

1-2.5 seconds:
Kiko notices already-visible yellow flowers in the existing flowerbed / planter area.
Kiko turns his eyes and head gently toward the flowers.
Mimi notices Kiko looking and turns slightly toward him.
Both characters remain in place.

2.5-4.5 seconds:
Kiko gently points toward the already-visible yellow flowers and says: "Yellow flowers!"

4.5-6.5 seconds:
Mimi follows Kiko's point and looks at the same yellow flowers.
Mimi smiles and makes a tiny delighted bounce or hand gesture.
No walking into the flowers.
No stepping behind the bench or planter.

6.5-8.5 seconds:
Mimi says: "So bright!"
Kiko smiles back at Mimi and nods gently.

8.5-10.5 seconds:
Kiko and Mimi both look back at the yellow flowers together.
They share a small happy reaction: blinking, smiling, tiny hand movement, or gentle nod.
No silent staring.
No frozen pose.

10.5-12.5 seconds:
Mimi points softly once more toward the yellow flowers.
Kiko follows the gesture with his eyes.
Both remain readable and preschool-safe.
The shot stays calm but alive.

12.5-15 seconds:
Both characters look from the yellow flowers back to each other, smiling.
Then they look back at the flowers together for the final beat.
Final frame remains usable for the next shot: no close-up, no crop, no lighting change, no new object, no camera reset.

Do not leave long empty pauses.
Do not make the shot a static talking pose.
Do not make the characters stare silently for several seconds.
Every 2-3 seconds must have a clear action, reaction, look, point, smile, nod, or dialogue beat.
Every movement must support the story beat.
Do not use random filler motion.

Kiko and Mimi keep the exact @image1 scale, position relationship and toddler-like proportions.
Do not make either character older, taller, realistic, school-age, oversized, cropped, or foreground-dominant.
Both characters remain small, rounded, soft toy-like and preschool-safe.

The camera preserves the @image1 composition.
Do not pull back, widen, reset, push in, pan, tilt, zoom, track, settle, drift, or reframe.
Characters may move naturally inside the stable composition.
Stable composition does not mean frozen characters.

Kiko must remain a single solid character at all times.
No ghost Kiko.
No transparent duplicate Kiko.
No double exposure Kiko.
No motion smear Kiko.
No character trail Kiko.
No overlapping duplicate face or body.

Mimi must remain a single solid character at all times.
No ghost Mimi.
No transparent duplicate Mimi.
No double exposure Mimi.
No motion smear Mimi.
No character trail Mimi.
No overlapping duplicate face or body.

No other characters.
No text.
No captions.
No subtitles.
No speech bubbles.

Natural ambience only:
soft breeze, distant birds, gentle tiny foot sounds, soft fabric-like character movement.
No music.
No background music.
No melody.
No song.
No soundtrack.
No musical bed.
No chime.

Dialogue:
Kiko: Yellow flowers!
Mimi: So bright!
```

---

## Negative Prompt

```text
camera pull-back, wider first frame, recomposed scene, new establishing shot, camera reset, changed camera angle, changed lens, camera tracking, pan, tilt, zoom, push-in, pull-back, reframing, camera settle, camera drift, camera searching for flowers, camera searching for planter, changed character position, changed character scale, changed lighting, changed colour grading, sky colour shift, sunset sky, orange sky, golden sky, grey sky, dramatic sky, painterly sky, lighting reinterpretation, new yellow flowers, new yellow flower planter, new flower cluster, new garden, new meadow, Flower Hill, flower field, yellow flowers appearing from nowhere, flower spawning, planter spawning, flowers appearing right before dialogue, discovery object appearing late, late object appearance, object pop-in, object spawning, object appearing from nowhere, object fade-in, object morphing into discovery object, newly generated discovery object, object created to match dialogue, flowerbed changing, duplicated flowers, resized flowers, moved flowers, repainted flowers, oversized Kiko, oversized Mimi, Kiko too large, Mimi too large, cropped character, character too close to camera, character dominating frame, older child, school-age child, teenager, adult proportions, realistic child, tall child, wrong scale, ghost Kiko, duplicate Kiko, transparent Kiko, double exposure Kiko, motion smear Kiko, character trail Kiko, ghost Mimi, duplicate Mimi, transparent Mimi, double exposure Mimi, motion smear Mimi, character trail Mimi, extra characters, non-canon characters, disappearing character, teleporting character, character side-switching, character hidden behind objects, character occluded by bench, character occluded by flowers, character occluded by planters, character clipping through bench, character clipping through bushes, character clipping through plants, character walking behind flowers, character walking into planter, character walking through flowerbed, background morphing, disappearing objects, moving trees, moving planters, moving bench, changing path, new path, new landmarks, new buildings, roads, cars, traffic, shops, readable signs, fountain, water feature, bridge, river, pond, crowd, static talking pose, characters frozen, no movement, long empty pause, silent staring, awkward pause, static waiting, dead air, frozen dialogue, inactive characters, random filler motion, meaningless movement, music, background music, melody, song, soundtrack, musical bed, chime, text, readable text, captions, subtitles, speech bubbles, logo, watermark, title card, subscribe button, like button
```

---

## OpenArt Ayarları

- Duration: 15 seconds
- @image1: Shot 03 approved final frame
- Prompt enhancer: Kapalı
- Cinematic/auto camera: Kapalı

---

## Reject Kontrolü

```
0-1 sn:
- İlk frame @image1 ile aynı mı?
- Kiko ve Mimi aynı pozisyon/ölçekte mi?
- Kamera aynı mı?
- Gökyüzü ve lighting @image1 ile aynı mı?
- Yeni çiçek / yeni planter / yeni obje belirmiyor mu?

1-2.5 sn:
- Kiko zaten görünen yellow flowers alanına bakıyor mu?
- Mimi Kiko'nun reaksiyonunu fark ediyor mu?
- Kamera çiçek aramak için hareket etmiyor mu?

2.5-4.5 sn:
- Kiko yellow flowers'a nazikçe işaret ediyor mu?
- "Yellow flowers!" diyor mu?

4.5-6.5 sn:
- Mimi Kiko'nun işaret ettiği yere bakıyor mu?
- Mimi küçük, canlı ama abartısız bir tepki veriyor mu?

6.5-8.5 sn:
- Mimi "So bright!" diyor mu?
- Kiko Mimi'ye gülümseyip küçük tepki veriyor mu?

8.5-10.5 sn:
- İkisi birlikte yellow flowers'a bakıyor mu?
- Sahne sessiz ve donuk kalmıyor mu?

10.5-12.5 sn:
- Mimi veya Kiko küçük bir ikinci reaction beat veriyor mu?
- Random filler motion yok mu?

12.5-15 sn:
- Final frame bir sonraki shot için uygun mu?
- Close-up, crop, lighting change veya camera reset yok mu?

Genel:
- Yellow flowers baştan beri @image1 içindeki mevcut flowerbed / planter area içinde mi?
- Yeni yellow planter oluştu mu? (olmamalı)
- Yeni flower field / garden / Flower Hill oluştu mu? (olmamalı)
- Ghosting / duplicate var mı?
- Kamera geri çekildi mi, genişledi mi, reset attı mı?
- Müzik / chime / melody var mı? (olmamalı)
- Uzun boş bekleme var mı?
- Karakterler sessizce donup bakıyor mu? (olmamalı)
- Her 2-3 saniyede küçük action / reaction / dialogue beat var mı?
```
