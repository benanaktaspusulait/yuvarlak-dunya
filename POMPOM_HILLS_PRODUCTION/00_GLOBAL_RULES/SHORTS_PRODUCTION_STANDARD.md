# Shorts Production Standard

> Bu dosya, Pompom Hills Shorts üretimindeki kalite ve karakter çıkmama sorunlarını çözer.
> Tüm Shorts üretimi bu standarda uymak zorundadır.

---

## 1. Temel Kural

**Her Shorts'ta karakter MERKEZDE ve NET görünmeli.**

Bu kural tartışmaya kapalıdır. Karakter görünmeyen Shorts yayınlanamaz.

---

## 2. Shorts Formatı

| Alan | Değer |
|------|-------|
| Çözünürlük | 1080×1920 (9:16 dikey) |
| Süre | 15-30 saniye |
| FPS | 24 |
| Encoding | H.264, high profile, CRF 18 |
| Ses | Stereo, 48 kHz, 24-bit |
| Minimum bitrate | 8 Mbps |
| Maksimum dosya boyutu | 28 MB |

---

## 3. Shorts İçerik Tipleri

| Tip | Açıklama | Süre | Örnek |
|-----|----------|------|-------|
| Character Intro | Karakter tanıtımı | 15 sn | "Meet Kiko!" |
| Key Moment | Önemli bir an | 15-20 sn | Kiko bir şey keşfediyor |
| Gentle Loop | Huzurlu döngü | 15 sn | Mimi zıplıyor, tekrar ediyor |
| Discovery Clip | Keşif anı | 15-20 sn | Bir çiçeğe bakıyor |
| Catchphrase | Tekrarlanan cümle | 10-15 sn | "Aaa, böyleymiş!" |
| Emotion Moment | Duygu anı | 15 sn | Mimi heyecanlanıyor |
| Nature Discovery | Doğa keşfi | 15-20 sn | Yaprak düşüyor |

---

## 4. Shorts Prompt Şablonu

### 4.1 Zorunlu Bölüm Yapısı

Her shorts prompt'u şu bölümleri içermelidir:

```text
## Character Position (EN BAŞTA)
Karakter merkezde, frame'in %15-20'si büyüklüğünde.
Karakter ekrana bakıyor veya belirli bir hareket yapıyor.
Karakter tam görünür, crop edilmemiş.

## Visual Hook (0-3 sn)
İlk 3 saniyede bir şey olmalı:
- Renk patlaması
- Hareket
- Yüz ifadesi
- Merak uyandıran bir nesne

## Action (3-12 sn)
Karakter belirli bir şey yapıyor:
- Zıplıyor
- Gülüyor
- Bir şey buluyor
- Bir şeyi keşfediyor
- BirArkadaşıyla etkileşime giriyor

## Closing (12-15 sn)
- Karakter gülümseme
- Tekrarlanan cümle
- Sıcak bitiş
- Kalp atışı gibi ritmik kapanış
```

### 4.2 Örnek: Character Intro Shorts

```text
Character Position:
Kiko is centred in the frame, occupying 15-20% of the vertical frame.
She faces the camera directly with a warm, inviting smile.
Full body visible from head to toe. Not cropped. Not too small.

Visual Hook (0-3 sec):
Kiko waves at the camera with both hands. Her coral pink shirt #F8BBD0 
brightens in warm sunlight. A soft sparkle appears near her face.

Action (3-12 sec):
Kiko points at herself: "I'm Kiko!" She then hops once, pigtails bouncing.
She points at the camera: "And you're my friend!" She claps her hands together.

Closing (12-15 sec):
Kiko smiles warmly at the camera. She waves goodbye. Soft fade to warm light.
Text overlay: "Kiko | Pompom Hills" (optional, 2 seconds max).
```

### 4.3 Örnek: Discovery Clip Shorts

```text
Character Position:
Kiko is centred, kneeling on soft grass, occupying 15-20% of frame.
She looks down at something with wide curious eyes.

Visual Hook (0-3 sec):
A single bright red flower blooms in fast-forward right in front of Kiko.
Her eyes go wide with amazement.

Action (3-12 sec):
Kiko gently touches the flower petals. She looks up at the camera and smiles.
She says: "So pretty!" Mimi hops into frame from the right.

Closing (12-15 sec):
Kiko and Mimi look at the flower together. Both smile. Warm sunlight.
Kiko: "Aaa, böyleymiş!" Gentle fade.
```

---

## 5. Negatif Prompt Kuralları

### 5.1 ASLA Kullanılmayacak Kelimeler

Bu kelimeler negatif prompt'ta OLMAZ — çünkü karakterin çıkmamasına neden olurlar:

```
❌ NO CHARACTERS
❌ empty frame
❌ character missing
❌ character not visible
❌ off-screen character
❌ too small character
❌ tiny character
❌ character cut off
❌ no people
❌ nobody
❌ void
```

### 5.2 Kısa Shorts Negatif Prompt

```text
low quality, blurry, deformed, extra limbs, text, watermark, photorealistic, 
horror, scary, dark lighting, sharp objects, background music, loud sounds, 
fast camera movement, shaky camera, dramatic lighting, cold tones
```

### 5.3 Detaylı Shorts Negatif Prompt

```text
low quality, blurry, deformed, extra limbs, extra fingers, missing limbs, 
text, watermark, photorealistic, horror, scary, dark lighting, sharp objects, 
sharp edges, harsh shadows, cold tones, blue tint, green tint, orange shift, 
HDR look, cinematic LUT, fast camera movement, shaky camera, dramatic lighting, 
dramatic shadows, background music, loud sounds, electronic sounds, 
fast cuts, jump cuts, zoom cuts, static talking pose, frozen character, 
characters frozen, no movement, long empty pause, silent staring, 
awkward pause, dead air, characters staring silently, random filler motion
```

---

## 6. Olumlu Prompt Ekleri

Her shorts prompt'una şunu ekle (Character Position bölümünde):

### 6.1 Zorunlu Cümleler

```text
Character is clearly visible in the centre of the frame.
Character occupies 15-20% of the frame.
Character is fully visible from head to toe (or waist up for close-up).
Character is NOT cropped by frame edges.
Character is NOT too small to see.
Character is NOT off-screen.
Character is facing the camera or slightly angled toward it.
```

### 6.2 Karakter-Spesifik Ekler

**Kiko için:**
```text
Kiko wears coral pink #F8BBD0 shirt, white shorts, brown pigtails.
Her expression is warm, curious, and inviting.
She is the focal point of the frame.
```

**Mimi için:**
```text
Mimi wears soft blue #90CAF9 body with round ears.
She is cute, small, and clearly visible.
Her ears are perked up and expressive.
```

**Opa için:**
```text
Opa wears warm green #A5D6A7 feathers with golden glasses #FFD54F.
He is wise, calm, and gently smiling.
His round shape is clearly defined against the background.
```

---

## 7. Karakter Görünürsüzlüğü Kontrol Listesi

Her shorts üretilmeden önce bu listeyi kontrol et:

### 7.1 Prompt Kontrolü

- [ ] Karakter prompt'ta merkezde mi?
- [ ] Karakter scale %15-20 mi?
- [ ] Karakter crop edilmemiş mi?
- [ ] Karakter tam görünür mü (head to toe)?
- [ ] Karakter ekrana bakıyor veya yüzü görünüyor mu?

### 7.2 Negatif Prompt Kontrolü

- [ ] "NO CHARACTERS" yok mu?
- [ ] "empty frame" yok mu?
- [ ] "character missing" yok mu?
- [ ] "too small character" yok mu?

### 7.3 Referans Kontrolü

- [ ] @image1 reference kullanıldı mı?
- [ ] Karakter rengi doğru mu?
- [ ] Karakter costume doğru mu?
- [ ] Karakter scale doğru mu?

### 7.4 Ortam Kontrolü

- [ ] Arka plan çok karmaşık mı?
- [ ] Işık yeterli mi?
- [ ] Renkler canlı mı?
- [ ] Karakter arka plandan ayrışıyor mu?

---

## 8. Red Rules (Shorts)

### 8.1 Kesin Red

| Durum | Neden | Çözüm |
|-------|-------|-------|
| Karakter görünmüyor | İzleyici ne izlediğini anlayamaz | Prompt'ta karakter pozisyonunu netleştir |
| Karakter çok küçük | Karakter tanınamaz | Scale'i %15-20'ye çıkar |
| Karakter crop edilmiş | Kısmi görünüm kafa karıştırıcı | Karakteri merkeze al |
| Karakter yanlış renkte | Tanınmaz hale gelir | Renk kodunu kontrol et |
| Karakter eksik uzuv | Deforme görünüm | Prompt'u temizle |
| Karanlık aydınlatma | Çocuklar karanlık sevmez | Işığı sıcacık yap |

### 8.2 Uyarı ile Geçiş

| Durum | Uyarı | Aksiyon |
|-------|-------|---------|
| Arka plan çok karmaşık | Karakter kaybolabilir | Arka planı basitleştir |
- Karakter çok hızlı hareket ediyor | Bulanık çıkabilir | Hareketi yavaşlat
- Işık çok parlak | Göz kamaştırabilir | Işığı yumuşat

---

## 9. Shorts Üretim Akışı

```
1. Bölüm seç (hangi sahne Shorts olacak?)
        ↓
2. Karakter Reference yükle
        ↓
3. Shorts Prompt oluştur (şablona göre)
        ↓
4. Negatif prompt ekle (shorts standardına göre)
        ↓
5. Karakter pozisyonunu kontrol et (merkez, %15-20)
        ↓
6. OpenArt'ta üret
        ↓
7. QA kontrolü (karakter görünüyor mu?)
        ↓
8. Red ise düzelt ve yeniden üret
        ↓
9. Geçerse: 1080×1920'e crop et
        ↓
10. Metadata ekle (başlık, açıklama, etiket)
        ↓
11. Yükle
```

---

## 10. Shorts Metadata Standardı

### 10.1 Başlık Formatı

```
[Karakter] [Aksiyon] | Pompom Hills Shorts
```

Örnekler:
- "Kiko Waves Hello | Pompom Hills Shorts"
- "Mimi Hops and Bounces | Pompom Hills Shorts"
- "Kiko Finds a Flower | Pompom Hills Shorts"

### 10.2 Açıklama Formatı

```
[Karakter] [ne yapıyor] bu tatlı Pompom Hills Short'ta.

#PompomHills #Shorts #PreschoolAnimation #[tema]
```

### 10.3 Etiketler

```
Pompom Hills, preschool animation, kids animation, toddler cartoon, 
kids cartoon, gentle kids video, calm kids cartoon, safe cartoon for kids, 
animated preschool story, educational cartoon, [karakter adı], [mekan], [tema]
```

---

## 11. Kalite Kontrol Sonrası

### 11.1 İzleme Kontrolü

Her üretilen Shorts'u izle ve kontrol et:

- [ ] İlk 3 saniyede dikkat çekiyor mu?
- [ ] Karakter net görünüyor mu?
- [ ] Karakter merkezde mi?
- [ ] Renkler canlı mı?
- [ ] Ses net mi?
- [ ] Kapanış sıcak mı?

### 11.2 Parental Kontrol

- [ ] Korkutucu bir şey var mı? → Yok olmalı
- [ ] Çocuğu rahatsız edecek bir şey var mı? → Yok olmalı
- [ ] Yetişkin için de izlenebilir mi? → Evet olmalı
- [ ] Tekrar izlenir mi? → Evet olmalı

---

## 12. Bilinen Sorunlar ve Çözümleri

### 12.1 Karakter Çıkmama Sorunu

**Belirtiler:**
- Sadece arka plan görünüyor
- Karakter çok küçük, tanınamıyor
- Karakter frame dışında

**Nedenleri:**
1. Prompt'ta karakter pozisyonu belirsiz
2. @image1 reference kullanılmıyor
3. Negatif prompt'ta "no characters" var
4. Karakter scale çok küçük

**Çözümler:**
1. Her prompt'ta zorunlu: "Character is CENTRED in frame, 15-20% of frame"
2. Her zaman @image1 kullan
3. Negatif prompt'tan character-related negatifleri kaldır
4. Karakteri merkeze ve büyüt

### 12.2 Düşük Kalite Sorunu

**Belirtiler:**
- Bulanık görüntü
- Düşük çözünürlük
- Renk solukluğu
- Kötü encoding

**Nedenleri:**
1. Düşük çözünürlük seçimi
2. Yanlış encoding ayarları
3. Kötü frame seçimi
4. Renk grading tutarsız

**Çözümler:**
1. Minimum çözünürlük: 1080×1920
2. Encoding: H.264 high profile, CRF 18
3. En iyi frame'i seç (en net, en renkli)
4. Renk grading standardı uygula

### 12.3 Tutarsızlık Sorunu

**Belirtiler:**
- Farklı Shorts'larda farklı görünüm
- Karakter rengi değişiyor
- Mekan değişiyor

**Nedenleri:**
1. Farklı prompt'lar kullanılıyor
2. @image1 reference farklı
3. Renk kodları tutarsız

**Çözümler:**
1. Her zaman aynı prompt şablonunu kullan
2. Her zaman aynı @image1 reference'ı kullan
3. Karakter renk kodlarını kilitle

---

## 13. Shorts Örnek Kütüphanesi

### 13.1 Character Intro Örnekleri

| Karakter | Hook | Aksiyon | Kapanış |
|----------|------|---------|---------|
| Kiko | El sallama | "I'm Kiko!" + zıplama | Gülümseme + el sallama |
| Mimi | Kulak sallama | Hop hop! + kuyruk sallama | Mırıltı + gülümseme |
| Opa | Kanat açma | "Shhh..." + parmak işareti | Bilge gülümseme |
| Luca | Koşarak gelme | "Let's explore!" + parmakla gösterme | Heyecanlı gülümseme |
| Noah | Ritmik el çırpma | "Let's make it fun!" + dans | Müzikal kapanış |
| Arda | Zıplayarak gelme | "Hadi gidelim!" + koşma | Enerjik gülümseme |

### 13.2 Discovery Clip Örnekleri

| Keşif | Hook | Aksiyon | Kapanış |
|-------|------|---------|---------|
| Çiçek | Çiçeğin açılması | Dokunma + hayranlık | "So pretty!" |
| Yaprak | Yaprak düşmesi | Yakalama + inceleme | "Yummy leaf!" (Mimi) |
| Yıldız | Yıldız parlaması | Yukarı bakma | "Wow!" |
| Kelebek | Kelebek konması | İzleme | "Hello butterfly!" |
| Taş | Taşın parlaklığını | Alma + inceleme | "Shiny!" |

---

## 14. YouTube Thumbnail (Önizleme Resmi)

Her Shorts ve ana video için YouTube thumbnail/resim çıkarılmalıdır.

### 14.1 Thumbnail Formatı

| Alan | Değer |
|------|-------|
| Çözünürlük | 1280×720 (16:9 yatay) |
| Format | JPG |
| Kalite | q=2 (yüksek kalite) |
| Minimum dosya boyutu | 100 KB |
| Maksimum dosya boyutu | 2 MB |

### 14.2 Thumbnail Çıkarma Akışı

```
1. Ana videoyu bul
        ↓
2. Farklı anlardan 6 frame çıkar (2sn, 8sn, 15sn, 45sn, 90sn, 110sn)
        ↓
3. Her frame'i 1280×720 JPG olarak kaydet
        ↓
4. Kullanıcıya sun, en iyisini seç
        ↓
5. Seçileni "thumbnail.jpg" olarak kaydet
```

### 14.3 ffmpeg Komutu

```bash
# Tek frame çıkarma
ffmpeg -ss [SN] -i [ANA_VIDEO] -vframes 1 -q:v 2 [ÇIKIŞ_DOSYASI].jpg

# 6 frame çıkarma (farklı anlar)
for t in 2 8 15 45 90 110; do
  ffmpeg -y -ss $t -i [ANA_VIDEO] -vframes 1 -q:v 2 "thumb_${t}s.jpg"
done
```

### 14.4 Thumbnail Seçim Kriterleri

| Kriter | Açıklama |
|--------|----------|
| Karakter görünür mü? | En az 1 karakter net görünmeli |
| Renkler canlı mı? | Sıcak, çocuk dostu renkler |
| Duygu var mı? | Heyecan, merak, mutluluk |
| Arka plan temiz mi? | Karakter arka plandan ayrışmalı |
| Metin okunabilir mi? | Varsa overlay text net olmalı |

### 14.5 Thumbnail Dosya Yapısı

```
03_VIDEO_EXPORTS/shorts/
├── thumb_02s.jpg
├── thumb_08s.jpg
├── thumb_15s.jpg
├── thumb_45s.jpg
├── thumb_90s.jpg
├── thumb_110s.jpg
└── thumbnail.jpg  (seçilen)
```

---

## 15. İlgili Dosyalar

| Dosya | Amaç |
|-------|------|
| `00-CORE/17_VIDEO_GENERATION_STANDARD.md` | Ana video üretim standardı |
| `00-CORE/18_VIDEO_STYLE_AND_RETENTION_STANDARD.md` | Video stili ve retention |
| `00-CORE/VISUAL_STYLE_GUIDE.md` | Görsel stil rehberi |
| `00-CORE/VISUAL_CONTINUITY_RULES.md` | Görsel süreklilik kuralları |
| `00-CORE/NEGATIVE_PROMPTS.md` | Negatif prompt listeleri |
| `00-CORE/VARIABLES.md` | Prompt değişkenleri |
| `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/SHOT_CONTINUITY_WORKFLOW.md` | Shot süreklilik akışı |

---

*Oluşturulma: 7 Temmuz 2026*
*Son güncelleme: 10 Temmuz 2026*
