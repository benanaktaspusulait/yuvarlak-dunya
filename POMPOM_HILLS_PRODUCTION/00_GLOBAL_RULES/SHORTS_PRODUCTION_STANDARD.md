# Shorts Production Standard

> Bu dosya, Pompom Hills Shorts üretimindeki kalite ve karakter çıkmama sorunlarını çözer.

---

## Temel Kural

**Her Shorts'ta karakter MERKEZDE ve NET görünmeli.**

---

## Shorts Prompt Şablonu

### Zorunlu Bölümler

```text
## Character Position
Karakter merkezde, frame'in %15-20'si büyüklüğünde.
Karakter ekrana bakıyor veya belirli bir hareket yapıyor.

## Visual Hook (0-3 sn)
İlk 3 saniyede bir şey olmalı: renk, hareket, yüz ifadesi.

## Action (3-12 sn)
Karakter belirli bir şey yapıyor: zıplıyor, gülüyor, bir şey buluyor.

## Closing (12-15 sn)
Karakter gülümseme veya tekrarlanan cümle. Sıcak bitiş.
```

### Negatif Prompt (Shorts için)

```text
low quality, blurry, deformed, extra limbs, text, watermark, photorealistic, 
horror, scary, dark lighting, sharp objects, NO CHARACTERS, empty frame, 
character missing, character not visible, off-screen character, 
too small character, tiny character, character cut off, 
background music, loud sounds, fast camera movement
```

**ÖNEMLİ:** "NO CHARACTES" veya "empty frame" negatif prompt'ta OLMAZ — bunlar karakterin çıkmamasına neden olur!

### Olumlu Prompt Ekleri (Shorts için)

Her shorts prompt'una şunu ekle:

```text
Character is clearly visible in the centre of the frame.
Character occupies 15-20% of the frame.
Character is fully visible from head to toe (or waist up).
Character is NOT cropped by frame edges.
Character is NOT too small to see.
Character is NOT off-screen.
```

---

## Shorts Formatı

| Alan | Değer |
|------|-------|
| Çözünürlük | 1080×1920 (9:16) |
| Süre | 15-30 saniye |
| FPS | 24 |
| Encoding | H.264, high profile |
| Ses | Stereo, 48 kHz |

---

## Shorts İçerik Tipleri

| Tip | Açıklama | Örnek |
|-----|----------|-------|
| Character Intro | Karakter tanıtımı | "Meet Kiko!" |
| Key Moment | Önemli bir an | Kiko bir şey keşfediyor |
| Gentle Loop | Huzurlu döngü | Mimi zıplıyor, tekrar ediyor |
| Discovery Clip | Keşif anı | Bir çiçeğe bakıyor |
| Catchphrase | Tekrarlanan cümle | "Aaa, böyleymiş!" |

---

## Karakter Görünürsüzlüğü Kontrol Listesi

Her shorts üretilmeden önce:

- [ ] Karakter prompt'ta merkezde mi?
- [ ] Karakter scale %15-20 mi?
- [ ] Karakter crop edilmemiş mi?
- [ ] Negatif prompt'ta "no characters" yok mu?
- [ ] @image1 reference kullanıldı mı?
- [ ] Karakter rengi doğru mu?

---

## Red Rules (Shorts)

| Durum | Red | Çözüm |
|-------|-----|-------|
| Karakter görünmüyor | ✅ Red | Prompt'ta karakter pozisyonunu netleştir |
| Karakter çok küçük | ✅ Red | Scale'i %15-20'ye çıkar |
| Karakter crop edilmiş | ✅ Red | Karakteri merkeze al |
| Karakter yanlış renkte | ✅ Red | Renk kodunu kontrol et |
| Arka plan çok karmaşık | ✅ Red | Arka planı basitleştir |
| Işık çok karanlık | ✅ Red | Işığı sıcacık yap |

---

*Oluşturulma: 7 Temmuz 2026*
