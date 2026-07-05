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

### Failure: No multi-image reference planning
**Tarih:** 2026-07-04
**Gözlem:** Birden fazla referans image yüklendiğinde OpenArt hangisinin first frame, hangisinin object reference olduğunu karıştırdı.
**Sebep:** Her image'ın net bir role sahip olması gerektiği belirtilmemişti.
**Çözüm:** Multi-Image Reference Planning Rule — her image'ın rolü açıkça tanımlanmalı, @image1 her zaman öncelikli olmalı.
**Global kural:** Multi-Image Reference Planning / Each Image Must Have a Role.

### Failure: No preflight validation system
**Tarih:** 2026-07-04
**Gözlem:** Üretime geçmeden önce sorunlar yakalanamadı. Çoğu hata üretim sırasında keşfedildi.
**Sebep:** Pre-production validation sistemi yoktu. Prompt ve frame birlikte kontrol edilmiyordu.
**Çözüm:** Video Production Preflight System — her shot için Shot Contract ve Preflight Checklist.
**Global kural:** Video Production Preflight System.

---

## S01E04 Shot 01 — Mimi Yawns (First-Frame Still)

### Failure: Stepping stone count wrong / cropped in master still
**Tarih:** 2026-07-05
**Gözlem:** Shot 01 first-frame still'de kanonik "exactly 3 stepping stones" yerine 2 taş net görünüyordu; 3. taş frame kenarından kesilmişti.
**Sebep:** Prompt "exactly three stepping stones" diyordu ama taşların frame içinde tam görünür ve kesilmemiş olması gerektiği belirtilmemişti. Model taşı kadraj kenarına yerleştirip kırptı.
**Çözüm:** Shot 01'de "all three stones fully inside the frame, not near the edge, not cropped, clearly countable as three" ifadesi eklendi; negative prompt'a "missing third stone, two stepping stones, four stepping stones, cropped stones, stones cut off by frame edge" eklendi; reject kriterine "not exactly 3 fully visible = reject" eklendi.
**Global kural:** Master Setup Frame — Countable Object Visibility Rule: kanonik sabit sayıdaki objeler (ör. tam 3 taş) master still'de tamamen görünür ve kesilmemiş olmalı, aksi halde reject.

### Failure: Character blocking the entrance in master still
**Tarih:** 2026-07-05
**Gözlem:** Mimi burrow entrance'ın tam ağzında/önünde duruyordu; entrance okunuyordu ama geçiş yolu ve kompozisyon riskliydi (Shot 05 crossing bu yolu kullanacak).
**Sebep:** Karakter pozisyonu "near the entrance" diye belirsizdi; "beside, not blocking" netliği yoktu.
**Çözüm:** Mimi pozisyonu "beside the entrance (to one side, not inside the doorway), must not block the entrance opening or the stepping-stone path" olarak netleştirildi; reject kriterine "Mimi blocking entrance / inside doorway / blocking path = reject" eklendi.
**Global kural:** Master Setup Frame — Landmark & Path Unblocked Rule: master still'de ana landmark (entrance) ve gelecekte kullanılacak yol (stepping-stone path) karakter tarafından bloklanmamalı.

### Failure: Action objects present but not staged for action (object staging gap)
**Tarih:** 2026-07-05
**Gözlem:** S01E04 Shot 01 master frame'de ağaç ve büyük çiçek çalısı **vardı**, ama ikisi de karakter aksiyonları için yanlış mesafede / yanlış pozisyondaydı. Flower patch entrance solunda ama Mimi'nin oturup yaslanamayacağı kadar sahne içinde belirsizdi; tree/grass alanı sağ arkada dekor gibiydi. Sonraki shot'larda OpenArt aksiyon objesini karaktere uydurmak için flower patch'i büyüttü (Shot 02) ve ağaç/grass alanını yaklaştırdı/büyüttü (Shot 03) — continuity break.
**Sebep:** Pipeline'da object **presence check** vardı (§0), ama object **staging check** yoktu. "Obje görünür mü?" soruluyordu ama "obje aksiyon için doğru mesafede/büyüklükte/kullanılabilir konumda mı?" sorulmuyordu. Hata Shot 03'te görünse de aslında Shot 01 master setup'ta başlamıştı.
**Çözüm:** Yeni hard gate eklendi — master setup frame'de her gelecek aksiyon objesi sadece görünür değil, kullanılabilir bir interaction zone olarak sahnelenmeli (yakın + usable + aksiyona uygun). Uzak/küçük/dekoratif/ulaşılamaz obje = master frame NOT READY, first-frame still yeniden üretilir.
**Global kural:** Master Frame Action Layout Gate — "Visible is not enough. The object must be placed for action."

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
| 2026-07-04 | Early Object Seeding / No Surprise Discovery Objects Rule eklendi | 18_OPENART_CONTINUITY_AND_MOTION_RULES.md |
| 2026-07-04 | Multi-Image Reference Planning / Each Image Must Have a Role eklendi | 18_OPENART_CONTINUITY_AND_MOTION_RULES.md |
| 2026-07-04 | Video Production Preflight System eklendi | 19_VIDEO_PRODUCTION_PREFLIGHT_SYSTEM.md |
| 2026-07-04 | Final Frame Continuity Rule eklendi | 18_OPENART_CONTINUITY_AND_MOTION_RULES.md |
| 2026-07-04 | Prompt Length Rule eklendi | 18_OPENART_CONTINUITY_AND_MOTION_RULES.md |
| 2026-07-04 | Global QA Checklist eklendi | 18_OPENART_CONTINUITY_AND_MOTION_RULES.md |
| 2026-07-04 | Negative Prompt Modular Bank eklendi | 18_OPENART_CONTINUITY_AND_MOTION_RULES.md |
| 2026-07-04 | Shot Template Requirements eklendi | 18_OPENART_CONTINUITY_AND_MOTION_RULES.md |
| 2026-07-05 | Master Setup Frame — Countable Object Visibility Rule (3 taş tam görünür/kesilmemiş) | S01E04 shot-01-mimi-yawns.md |
| 2026-07-05 | Master Setup Frame — Landmark & Path Unblocked Rule (Mimi entrance/yol bloklamıyor) | S01E04 shot-01-mimi-yawns.md |
| 2026-07-05 | Master Frame Action Layout Gate (§0.1) — obje presence değil staging kontrolü | 19_VIDEO_PRODUCTION_PREFLIGHT_SYSTEM.md, SCENE_QA_CHECKLIST.md |


## S01E04 Production — Rule Language vs Action Contradiction

### Failure: Shot passes "rules compliance" but fails "production logic"
**Tarih:** 2026-07-05
**Gözlem:** Shot dosyaları doğru kural metni içeriyor ("no new objects", "background locked") ama production'da başarısız oluyor çünkü @image1 frame'i aksiyonu desteklemiyor.
**Örnek:** Shot "no new objects" diyor ama "walk to a stream" istiyor; stream @image1'de görünmüyor. 
**Örnek:** Shot "background locked" diyor ama "pick a large leaf" istiyor; leaf @image1'de yok.
**Sebep:** Validator sadece kural metnini kontrol ediyordu — prompt'ta "no new objects" yazması yeterli sayılıyordu. Validator, kural metni ile aksiyon ihtiyacı arasındaki çelişkiyi ve @image1'in gerçekte ne gösterdiğini kontrol etmiyordu.
**Çözüm:** Yeni hard gate eklendi — kural metni compliance değildir. Validator üç şeyi karşılaştırmalı:
1. Prompt neyi yasaklıyor? (no new objects, background lock)
2. Shot aksiyonu ne gerektiriyor? (walk to stream, pick leaf) 
3. @image1 ne gösteriyor? (stream yok, leaf yok)
Çelişki varsa → shot FAIL PREFLIGHT.
**Global kural:** Rule Language Is Not Compliance (§2) — kural metni değil, @image1'in gerçek görsel desteği önemlidir.

### Failure: Frame not supporting action despite "rule exists"
**Tarih:** 2026-07-05
**Gözlem:** Shot geçiyor çünkü doğru kural kelimeleri var, ama sonraki shot'ta obje görünmüyor çünkü aslında @image1'de yok veya kullanılamaz.
**Sebep:** Object presence check var ama object usability / staging check yok. 
**Çözüm:** Yeni hard gate — FRAME-SUPPORTED ACTION ONLY (§0). Her gerekli obje için: @image1'de görünür mü? Net şekilde lokalize edilmiş mi? Karakter etkileşime geçebilir mi? Model icat etmek zorunda mı? Hayır ise → shot NOT READY.
**Global kural:** HARD PREFLIGHT GATE: FRAME-SUPPORTED ACTION ONLY (§0) — shot sadece @image1 gerçekten aksiyonu destekliyorsa preflight'tan geçebilir.

---

## Global Kural Güncellemeleri (devam)

| Tarih | Güncelleme | Dosya |
|---|---|---|
| 2026-07-05 | **§0 HARD PREFLIGHT GATE: FRAME-SUPPORTED ACTION ONLY** — kural metni compliance değil; @image1'in gerçek görsel desteği önemli | 19_VIDEO_PRODUCTION_PREFLIGHT_SYSTEM.md |
| 2026-07-05 | **§2 RULE LANGUAGE IS NOT COMPLIANCE** — validator kural metni, aksiyon ihtiyacı ve @image1'i karşılaştırmalı; çelişki varsa FAIL | 19_VIDEO_PRODUCTION_PREFLIGHT_SYSTEM.md |
| 2026-07-05 | **SAFE/RISKY/NOT READY status definitions** — sadece SAFE shot'lar üretime geçebilir; kural metni status'u değiştirmez | 19_VIDEO_PRODUCTION_PREFLIGHT_SYSTEM.md |
| 2026-07-05 | **Global Preflight Checklist** güncellendi — §0 ve §2 hard gate'ler eklendi | 19_VIDEO_PRODUCTION_PREFLIGHT_SYSTEM.md |
| 2026-07-05 | **Shot Contract format** güncellendi — contradiction check, required objects list eklendi | 19_VIDEO_PRODUCTION_PREFLIGHT_SYSTEM.md |