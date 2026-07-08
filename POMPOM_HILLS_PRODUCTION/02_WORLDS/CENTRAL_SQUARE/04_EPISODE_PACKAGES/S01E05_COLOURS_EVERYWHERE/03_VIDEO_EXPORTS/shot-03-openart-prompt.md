# Shot 03 — OpenArt Prompt

> Bu dosya sadece OpenArt'a verilecek prompt bloklarını içerir.
> Shot 02 approved final frame: Kiko ve Mimi birlikte, Kiko red/pink stepping stone üzerinde.

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

0-1 second:
Hold @image1 almost exactly.
Kiko and Mimi remain visible in the same positions, scale and general direction from @image1.
Only tiny natural idle motion is allowed: blinking, breathing, tiny smile, slight head movement.
No camera movement.
No bench movement.
No lighting change.

1-3 seconds:
Mimi notices the already-visible pastel blue bench.
Mimi turns her head and eyes toward the bench.
Kiko glances toward Mimi.
Both remain in place.

3-5 seconds:
Mimi gently points toward the already-visible blue bench and says: "I see blue!"

5-7 seconds:
Kiko follows Mimi's point, looks at the bench, smiles, and takes a tiny natural reaction beat without stepping away.

7-10 seconds:
Kiko gently points or gestures toward the bench and says: "A blue bench!"

10-13 seconds:
Mimi nods or smiles softly.
Kiko and Mimi both look from the bench back to each other with small natural preschool-safe movement.

13-15 seconds:
Both characters look back at the blue bench together, smiling.
Final frame remains usable for the next shot: no close-up, no crop, no lighting change, no new object, no camera reset.

Kiko and Mimi keep the exact @image1 scale, position relationship and toddler-like proportions.
Do not make either character older, taller, realistic, school-age, oversized, cropped, or foreground-dominant.
Both characters remain small, rounded, soft toy-like and preschool-safe.

The pastel blue bench must already be visible in @image1.
Do not create, reveal, move, resize, duplicate, repaint, or replace the bench.
Do not use camera movement to find the bench.
If the bench is not visible in @image1, do not invent a new blue bench or new blue object.

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
Mimi: I see blue!
Kiko: A blue bench!
```

---

## Voice Lock

Each character must use their registered locked voice from VOICE_TRACKER.md.
Do not let OpenArt choose or generate voices.
Do not change voice between shots.
Same pitch, same timbre, same age, same speed, same warmth.

## Negative Prompt

```text
camera pull-back, wider first frame, recomposed scene, new establishing shot, camera reset, changed camera angle, changed lens, camera tracking, pan, tilt, zoom, push-in, pull-back, reframing, camera settle, camera drift, camera searching for bench, changed character position, changed character scale, changed lighting, changed colour grading, sky colour shift, sunset sky, orange sky, golden sky, grey sky, dramatic sky, painterly sky, lighting reinterpretation, new blue bench, new blue object, large foreground blue bench, blue bench appearing from nowhere, bench spawning, duplicated bench, resized bench, moved bench, repainted bench, bench identity change, oversized Kiko, oversized Mimi, Kiko too large, Mimi too large, cropped character, character too close to camera, character dominating frame, older child, school-age child, teenager, adult proportions, realistic child, tall child, wrong scale, ghost Kiko, duplicate Kiko, transparent Kiko, double exposure Kiko, motion smear Kiko, character trail Kiko, ghost Mimi, duplicate Mimi, transparent Mimi, double exposure Mimi, motion smear Mimi, character trail Mimi, extra characters, non-canon characters, disappearing character, teleporting character, character side-switching, character hidden behind objects, character occluded by bench, character occluded by flowers, character occluded by planters, character clipping through bench, character clipping through bushes, character clipping through plants, background morphing, disappearing objects, moving trees, moving planters, moving bench, changing path, new path, new landmarks, new buildings, roads, cars, traffic, shops, readable signs, fountain, water feature, bridge, river, pond, crowd, static talking pose, characters frozen, no movement, long empty pause, silent staring, awkward pause, static waiting, dead air, frozen dialogue, inactive characters, random filler motion, meaningless movement, music, background music, melody, song, soundtrack, musical bed, chime, text, readable text, captions, subtitles, speech bubbles, logo, watermark, title card, subscribe button, like button
```

---, high contrast, contrast increase, overly saturated, saturation increase, HDR, HDR look, glossy plastic, glossy CGI, harsh highlights, harsh shadows, blown highlights, oversharpened, extra sharp, over-polished CGI, colour drift, exposure drift, saturation drift, contrast drift, dark areas growing darker, highlights growing brighter, lighting becoming harsher


## OpenArt Ayarları

- Duration: 15 seconds
- @image1: Shot 02 approved final frame (Kiko ve Mimi birlikte)
- Prompt enhancer: Kapalı
- Cinematic/auto camera: Kapalı

---

## Reject Kontrolü

```
0-1 sn:
- Kiko ve Mimi aynı pozisyon/ölçekte mi?
- Kamera aynı mı?
- Gökyüzü ve lighting @image1 ile aynı mı?
- Blue bench @image1 içinde zaten görünür mü?

1-3 sn:
- Mimi blue bench'e bakıyor mu?
- Kiko Mimi'ye veya Mimi'nin baktığı yöne bakıyor mu?

3-5 sn:
- Mimi blue bench'e nazikçe işaret ediyor mu?
- "I see blue!" diyor mu?

5-7 sn:
- Kiko blue bench'e bakıyor mu?
- Gülümsüyor mu?

7-10 sn:
- Kiko blue bench'e nazikçe işaret ediyor mu?
- "A blue bench!" diyor mu?

10-13 sn:
- Mimi baş sallıyor veya gülümsüyor mu?
- İkisi kısa şekilde birbirine tepki veriyor mu?

13-15 sn:
- İkisi birlikte blue bench'e bakıyor mu?
- Final frame bir sonraki shot için uygun mu?

Genel:
- Ghosting / duplicate var mı?
- Kamera geri çekildi mi, genişledi mi, reset attı mı?
- Yeni bench oluştu mu? (olmamalı)
- Bench hareket etti, büyüdü, çoğaldı veya repaint oldu mu? (olmamalı)
- Müzik / chime / melody var mı? (olmamalı)
- Uzun boş bekleme var mı?
- Her 2-3 saniyede küçük aksiyon var mı?
```
