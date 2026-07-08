# Shot 02 — OpenArt Prompt

> Bu dosya sadece OpenArt'a verilecek prompt bloklarını içerir.
> Shot 01 approved final frame: Kiko red/pink stepping stone üzerinde, medium-close framing.

---

## Visual Prompt

```text
Duration: 15 seconds.

Use @image1 as the exact first frame and only visual continuity source.

Do not reinterpret @image1.
Do not use memory of any previous video.
Only preserve what is visible in @image1.

The clean blue sky from @image1 has absolute priority.
Use only the same sky, lighting, colour grading, exposure and contrast from @image1.
Do not warm up the lighting.
Do not create sunset, golden hour, orange sky, dramatic clouds, grey sky, or painterly sky.

0-1 second:
Hold @image1 almost exactly.
Kiko remains visible in the same position, scale and general direction from @image1, with only tiny natural idle motion such as blinking, breathing, a small smile, or a very slight hand movement.
Kiko does not step away, change side, change scale, or leave the red/pink stepping stone.
Mimi is not visible.
No new character appears.
No camera pull-back.
No wider frame.
No new side objects.
No lighting change.
No colour grading change.

1-3 seconds:
Mimi becomes visible inside the existing @image1 composition, in the existing right-side or right-midground area.
Mimi makes one or two small soft hops or steps toward Kiko.
Mimi is readable enough to greet Kiko.
Mimi is not close to the camera, oversized, cropped, or foreground close-up.
Mimi is not a tiny distant background character.

3-5 seconds:
Mimi waves gently and says: "Hi Kiko!"

5-7 seconds:
Kiko turns naturally toward Mimi, smiles, and says: "Hi Mimi!"

7-10 seconds:
Mimi looks at the red/pink stepping stone and asks: "What did you find?"

10-13 seconds:
Kiko gestures gently toward the red/pink stepping stone and says: "Red! I'm finding colours!"

13-15 seconds:
Both characters smile and look at the red/pink stepping stone together with tiny natural idle motion.

Kiko keeps the exact @image1 scale and remains on the red/pink stepping stone.
Mimi remains toddler-like and in correct perspective scale for her position.
Both characters remain preschool-safe, soft, expressive and alive.

Do not leave long empty pauses.
Do not make the shot a static talking pose.
Do not make the characters stare silently for several seconds.
Every 2-3 seconds there should be a small clear action or dialogue beat.

The camera must preserve the @image1 composition.
Do not pull back to show more of Central Square.
Do not create a new establishing shot.
Do not push in to a close-up.
Do not zoom in for dialogue.
Do not track Mimi.
Do not track Kiko.
Do not reframe the scene.

Kiko must remain a single solid character.
No ghost Kiko.
No transparent duplicate Kiko.
No double exposure.
No motion smear.
No character trail.

Mimi must remain a single solid character.
No ghost Mimi.
No transparent duplicate Mimi.
No double exposure.
No motion smear.
No character trail.

No other characters.
No text.
No captions.
No subtitles.
No speech bubbles.

Natural ambience only:
soft breeze, distant birds, gentle footsteps or tiny hop sounds.
No music.
No background music.
No melody.
No song.
No soundtrack.

Dialogue:
Mimi: Hi Kiko!
Kiko: Hi Mimi!
Mimi: What did you find?
Kiko: Red! I'm finding colours!
```

---

## Voice Lock

Each character must use their registered locked voice from VOICE_TRACKER.md.
Do not let OpenArt choose or generate voices.
Do not change voice between shots.
Same pitch, same timbre, same age, same speed, same warmth.

## Negative Prompt

```text
camera pull-back, wider first frame, recomposed scene, new establishing shot, camera reset, changed camera angle, changed Kiko position, changed Kiko scale, changed lighting, changed colour grading, sky colour shift, sunset sky, orange sky, golden sky, grey sky, dramatic sky, Mimi visible in first frame, new character in first 1 second, Mimi too large, oversized Mimi, giant foreground Mimi, cropped Mimi, Mimi too close to camera, Mimi dominating frame, Kiko too large, Kiko changed position, extra characters, text, captions, subtitles, speech bubbles, tiny distant Mimi, background-only Mimi, unreadable Mimi, Mimi hidden behind tree, Mimi hidden behind flowers, Mimi appearing behind objects, Mimi wrong perspective scale, Mimi too far away, Kiko frozen unnaturally, frozen Kiko pose, static talking pose, characters frozen, no movement, ghost Kiko, duplicate Kiko, transparent Kiko, double exposure Kiko, motion smear Kiko, character trail, ghost Mimi, duplicate Mimi, transparent Mimi, double exposure Mimi, motion smear Mimi, music, background music, melody, song, soundtrack, musical bed, long empty pause, silent staring, awkward pause, static waiting, dead air, characters staring silently, frozen dialogue, inactive characters, random filler motion
```

---, high contrast, contrast increase, overly saturated, saturation increase, HDR, HDR look, glossy plastic, glossy CGI, harsh highlights, harsh shadows, blown highlights, oversharpened, extra sharp, over-polished CGI, colour drift, exposure drift, saturation drift, contrast drift, dark areas growing darker, highlights growing brighter, lighting becoming harsher


## OpenArt Ayarları

- Duration: 15 seconds
- @image1: Shot 01 approved final frame (Kiko red stepping stone üzerinde, medium-close)
- Prompt enhancer: Kapalı
- Cinematic/auto camera: Kapalı

---

## Reject Kontrolü

```
0-1 sn:
- Kiko aynı pozisyon/ölçekte mi?
- Mimi yok mu?
- Kamera aynı mı?
- Gökyüzü aynı temiz mavi mi?

1-3 sn:
- Mimi görünür mü?
- Mimi küçük hop/step yapıyor mu?

3-5 sn:
- Mimi el sallıyor mu?
- "Hi Kiko!" diyor mu?

5-7 sn:
- Kiko doğal şekilde dönüyor mu?
- "Hi Mimi!" diyor mu?

7-10 sn:
- Mimi taşa bakıyor mu?
- "What did you find?" diyor mu?

10-13 sn:
- Kiko taşa işaret ediyor mu?
- "Red! I'm finding colours!" diyor mu?

13-15 sn:
- İkisi birlikte taşa bakıyor mu?
- Küçük doğal hareket var mı?

Genel:
- Ghosting / duplicate var mı?
- Kamera geri çekilmedi mi?
- Wide establishing frame'e dönüldü mü?
- Kiko red stone üzerinde mi kaldı?
- Müzik var mı? (olmamalı)
- Uzun boş bekleme var mı?
- Karakterler sessizce uzun süre bakışıyor mu?
- Her 2-3 saniyede küçük aksiyon veya konuşma beat'i var mı?
- Diyalog doğal akıyor mu?
```
