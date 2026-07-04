# Opa's Storytime: The Little Seed That Listened v1.0

---

## Episode Lock

| Alan | Değer |
| --- | --- |
| Süre | 120 saniye (8 sahne × 15 sn) |
| Hedef yaş | 3-4 |
| Series | Opa's Storytime |
| Playlist | Opa's Storytime \| Gentle Preschool Stories |
| Ana duygu | Sıcaklık, ev hissi, sakin merak |
| Ana tema | Dinleme / yavaş büyümek |
| Mekan | Kiko's Home — Reading Corner |
| Karakterler | Opa, Kiko, Mimi |
| Voice Identity | Approved voice reference per speaking character (Opa, Kiko, Mimi) |
| Colour Identity | Warm coral-pink pastel palette, soft saturation, low contrast |
| Lighting Identity | Warm morning light through round window, cosy interior glow |
| Görsel yoğunluk | Düşük |
| Çatışma | Yok; sadece küçük tohumun sabırla dinleyip yavaşça büyümeyi öğrenmesi |

---

## Story Summary

Kiko, Opa'yı kendi evine davet eder. Mimi de oradadır. Üçü, Kiko'nun evindeki okuma
köşesinde toplanır. Opa küçük bir tohum hakkında bir masal anlatır — tohum toprağın
altında pek çok ses işitir ama acele etmeden dinlemeyi ve doğru zamanı beklemeyi
öğrenir. Kiko ve Mimi hikaye boyunca sorular sorar.

---

## Opening Bumper

Ortak açılış bumper kullanılır — bkz. `../_bumpers/opening-bumper.md`.

- Duration: 3–4 sn (ortak klip, her bölümde aynı)
- Visual: Yuvarlak kitap yumuşakça açılır (yer-nötr)
- Sound: Tek yumuşak chime
- Dialogue: Yok — bumper'dan sonra bölümün kendi açılış beat'ine kesme (Shot 01)
- Purpose: Seri kimliği + playlist tanınırlığı
- Retention risk: Düşük (max 5 sn, hikayeyi geciktirmez)

---

## Closing Bumper

Ortak kapanış bumper kullanılır — bkz. `../_bumpers/closing-bumper.md`.

- Duration: 4–5 sn (ortak klip, her bölümde aynı)
- Visual: Kitap yumuşakça kapanır + end-screen-safe kare
- Sound: Soft müzik kuyruğu
- Dialogue: Yok — Opa'nın son repliği Shot 08 warm final hold'da kalır
- End-screen-safe frame: Sakin, boşluklu, playlist öğesi için yer
- Purpose: Sıcak kapanış + repeat/playlist viewing

---

## Micro-Moment (Key Discovery)

Kiko'nun son sözü: "I listen with my ears and my heart." — dinlemenin sadece kulaklarla
değil, kalple de olduğunu keşfetme anı.

---

## Scene Order

| Sıra | Dosya | Süre | Karakter | Amaç |
| --- | --- | ---: | --- | --- |
| 01 | `shots/shot-01-welcome-home.md` | 15 sn | Kiko, Opa, Mimi | Ev sahipliği açılışı, seri açılış beat'i |
| 02 | `shots/shot-02-the-little-seed.md` | 15 sn | Opa, Kiko | Masalın başlaması |
| 03 | `shots/shot-03-so-many-sounds.md` | 15 sn | Opa, Mimi | Tohumun işittiği sesler |
| 04 | `shots/shot-04-which-sound-to-follow.md` | 15 sn | Opa, Kiko, Mimi | Duygusal soru, karar anı |
| 05 | `shots/shot-05-the-seed-waits.md` | 15 sn | Opa, Kiko | Sabırla dinleme |
| 06 | `shots/shot-06-a-small-green-shoot.md` | 15 sn | Opa, Mimi | Ders hikaye üzerinden gösterilir |
| 07 | `shots/shot-07-i-listen-with-my-heart.md` | 15 sn | Opa, Kiko | Micro-moment, kişisel bağlantı |
| 08 | `shots/shot-08-cosy-home-hold.md` | 15 sn | Opa, Kiko, Mimi | Sessiz sıcak kapanış |

---

## Repeated Phrase

```text
Come close, little friends.
```

---

## Learning Point

Dinlemek zaman alır; doğru anı beklemek büyümeye yardım eder.

---

## Voice Notes

| Karakter | Ses |
| --- | --- |
| Opa | Approved Opa voice reference — warm, calm, wise |
| Kiko | Approved Kiko voice reference — curious, gentle, welcoming (home setting) |
| Mimi | Approved Mimi voice reference — soft, quiet, observant |

Reference: `00-CORE/SHOT_PRODUCTION_STANDARD.md`

Voice continuity rule:

```text
The speaking voice MUST remain identical throughout the entire episode.
Use the same Voice ID or approved voice reference for the same character.
Maintain the same voice identity, timbre, pitch, speaking speed, warmth, preschool energy, pronunciation, accent, age impression, emotional tone and recording quality.
All speaking shots must sound as if they were recorded during the same recording session.
Never replace the voice with a narrator or alternate performer.
```

---

## Colour Notes

```text
The full episode must appear colour graded as one continuous film.
Maintain identical white balance, exposure, colour temperature, saturation, contrast, brightness and pastel palette across all shots.
No cool shift. No warm shift. No green tint. No magenta tint. No orange grading. No HDR look. No cinematic LUT.
The viewer must not perceive a shot boundary.
```

---

## Lighting Notes

```text
The lighting must continue across shots without reinterpretation.
Maintain identical light direction, light intensity, shadow softness, ambient lighting, highlight behaviour, cloud brightness and grass brightness.
Do not allow the episode to become brighter, darker, warmer, cooler, harsher or more cinematic between shots.
```

---

## Negative Prompt

low quality, blurry, deformed, extra limbs, text, watermark, readable text on book pages, photorealistic, horror, scary, dark lighting, violence, weapons, sharp objects, extra characters, redesigned environment, modern furniture, harsh lighting, scary shadows, adult lecture feeling

---

## QA Status

Scene QA (document-level, per `00-CORE/SCENE_QA_CHECKLIST.md`) passed on 4 Temmuz 2026: all 8 shot files contain the required sections — Frame Lock (shots 02–08), Background Object Lock, Visual Prompt, Camera Direction, Dialogue, Shot Breakdown, Sound, Lighting, Reference Usage, Text Safety, Negative Prompt, QA Checklist and Scale. Shot 01 carries the Opening Hook and series opening beat; shot 08 carries the warm-hold + closing-bumper note.

Render QA (`16_VIDEO_QA_SPEC.md`, scored /10) runs after each shot is generated — pending.

| Shot | Scene QA (doc) | Render QA /10 | Ready to Render |
|------|:--------------:|:-------------:|:---------------:|
| 01 | ✅ | — | ✅ |
| 02 | ✅ | — | ✅ |
| 03 | ✅ | — | ✅ |
| 04 | ✅ | — | ✅ |
| 05 | ✅ | — | ✅ |
| 06 | ✅ | — | ✅ |
| 07 | ✅ | — | ✅ |
| 08 | ✅ | — | ✅ |
