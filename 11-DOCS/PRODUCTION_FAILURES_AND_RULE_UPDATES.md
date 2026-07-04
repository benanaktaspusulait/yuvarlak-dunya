# Production Failures and Rule Updates

> Bu dosya üretim hatalarını ve bunlardan çıkarılan global kuralları kaydeder.
> Her yeni hata buraya eklenmeli ve çözümü global kurallara işlenmelidir.

---

## E05 Shot 01 — Kiko Sees Red

### Failure: Opening-to-shot mismatch
**Tarih:** 2026-07-04
**Gözlem:** Kiko ilk frame'de ortaya çıktı, kamera geri çekildi, wider establishing frame oluştu.
**Sebep:** Yeni karakterin ilk frame'de görünmesi camera pull-back / wider reset'e neden oldu.
**Çözüm:** `@image1` exact first frame, ilk 1 saniye continuity hold, ertelenmiş character introduction.
**Global kural:** First-Second Continuity Hold Rule, Character Entrance Without Recomposition Rule.

### Failure: Sky became orange/sunset
**Tarih:** 2026-07-04
**Gözlem:** Temiz mavi gökyüzü turuncu/sunset gibi oldu.
**Sebep:** Warm/generic lighting dili `@image1`'i override etti.
**Çözüm:** Sky/lighting absolute lock from `@image1`; warm lighting dilinden kaçınılması.
**Global kural:** Sky, Lighting and Colour Continuity Rule.

### Failure: Kiko became giant foreground edge character
**Tarih:** 2026-07-04
**Gözlem:** Kiko çok büyük, close-up, crop edilmiş olarak geldi.
**Sebep:** "Partial edge reveal" wording.
**Çözüm:** Karakter mevcut visible path / safe existing area'da görünür olmalı, fully or mostly visible, correct world scale, cropped/foreground değil.
**Global kural:** Character Scale Rule, Character Entrance Without Recomposition Rule.

### Failure: Late push-in
**Tarih:** 2026-07-04
**Gözlem:** Discovery/dialogue sırasında kamera yaklaştı.
**Sebep:** Story beat'ler camera push-in'i tetikledi.
**Çözüm:** Final frame continuity rule; istenmeyen push-in yok.
**Global kural:** Final Frame Continuity Rule.

---

## E05 Shot 02 — Mimi Joins

### Failure: Frozen/static dialogue scene
**Tarih:** 2026-07-04
**Gözlem:** Shot çok donmuş, sadece dialogue, hareket yok.
**Sebep:** Full-shot hard camera lock ve çok az aksiyon.
**Çözüm:** Stable composition vs frozen scene rule; natural character motion rule; her 3-5 saniyede aksiyon beats.
**Global kural:** Stable Composition vs Frozen Scene Rule, Natural Character Motion Rule, Dialogue Action Rule.

### Failure: Kiko ghost/double exposure
**Tarih:** 2026-07-04
**Gözlem:** Kiko'nun arkasında yarı saydam ikinci Kiko oluştu.
**Sebep:** Çok sert lock altında character turn motion smear/duplicate'e neden oldu.
**Çözüm:** Ghosting prevention rule.
**Global kural:** Ghosting / Duplicate Character Prevention Rule.

### Failure: Unwanted background music
**Tarih:** 2026-07-04
**Gözlem:** Arka planda müzik oluştu.
**Sebep:** Açık no-music rule yoktu.
**Çözüm:** Natural ambience only / no music rule.
**Global kural:** Natural Ambience / No Music Rule.

### Failure: Shot 03 object late spawning
**Tarih:** 2026-07-04
**Gözlem:** Blue bench/badge diyalog sırasında veya hemen öncesinde sahneye sonradan eklendi.
**Sebep:** Model "blue object discovery" ihtiyacını karşılamak için objeyi baştan korumak yerine sonradan spawn etti.
**Çözüm:** Object Must Exist Before Discovery Rule — discovery objesi ilk frame'de zaten görünür olmalı veya discovery beat'inden önce net şekilde mevcut olmalı.
**Global kural:** No Late Object Spawning / Object Must Exist Before Discovery Rule.

---

## Global Kural Güncellemeleri

| Tarih | Güncelleme | Dosya |
|---|---|---|
| 2026-07-04 | @image1 Reference Language Rule eklendi | 18_OPENART_CONTINUITY_AND_MOTION_RULES.md |
| 2026-07-04 | First-Second Continuity Hold Rule eklendi | 18_OPENART_CONTINUITY_AND_MOTION_RULES.md |
| 2026-07-04 | Stable Composition vs Frozen Scene Rule eklendi | 18_OPENART_CONTINUITY_AND_MOTION_RULES.md |
| 2026-07-04 | Natural Character Motion Rule eklendi | 18_OPENART_CONTINUITY_AND_MOTION_RULES.md |
| 2026-07-04 | Character Entrance Without Recomposition Rule eklendi | 18_OPENART_CONTINUITY_AND_MOTION_RULES.md |
| 2026-07-04 | Character Scale Rule eklendi | 18_OPENART_CONTINUITY_AND_MOTION_RULES.md |
| 2026-07-04 | Sky, Lighting and Colour Continuity Rule eklendi | 18_OPENART_CONTINUITY_AND_MOTION_RULES.md |
| 2026-07-04 | Ghosting / Duplicate Character Prevention Rule eklendi | 18_OPENART_CONTINUITY_AND_MOTION_RULES.md |
| 2026-07-04 | Natural Ambience / No Music Rule eklendi | 18_OPENART_CONTINUITY_AND_MOTION_RULES.md |
| 2026-07-04 | Dialogue Action Rule eklendi | 18_OPENART_CONTINUITY_AND_MOTION_RULES.md |
| 2026-07-04 | No Late Object Spawning / Object Must Exist Before Discovery Rule eklendi | 18_OPENART_CONTINUITY_AND_MOTION_RULES.md |
| 2026-07-04 | Final Frame Continuity Rule eklendi | 18_OPENART_CONTINUITY_AND_MOTION_RULES.md |
| 2026-07-04 | Prompt Length Rule eklendi | 18_OPENART_CONTINUITY_AND_MOTION_RULES.md |
| 2026-07-04 | Global QA Checklist eklendi | 18_OPENART_CONTINUITY_AND_MOTION_RULES.md |
| 2026-07-04 | Negative Prompt Modular Bank eklendi | 18_OPENART_CONTINUITY_AND_MOTION_RULES.md |
| 2026-07-04 | Shot Template Requirements eklendi | 18_OPENART_CONTINUITY_AND_MOTION_RULES.md |
