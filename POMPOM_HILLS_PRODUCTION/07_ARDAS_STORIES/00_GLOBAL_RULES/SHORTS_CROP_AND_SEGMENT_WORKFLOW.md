# Shorts Crop and Segment Workflow

> Bu dosya, shot'lardan short üretimi, segment bazlı crop, konuşmacı takibi ve birleştirme
> workflow'unu tanımlar. Bu session'da (17 Temmuz 2026) test edilmiş ve onaylanmış çözümlerdir.

---

## 1. Shot → Short Dönüşümü

### 1.1 Temel Kural

Orijinal shot video (16:9) asla değiştirilmez. Short'lar ayrı dosya olarak üretilir.

### 1.2 Crop Formülü

1280×720 kaynaktan 9:16 dikey (1080×1920):

```bash
ffmpeg -y -i shot-X.mp4 \
  -vf "scale=-2:1920,crop=1080:1920:XXXX:0,format=yuv420p" \
  -c:v libx264 -crf 18 -profile:v high \
  -c:a aac -ar 48000 -ac 2 \
  shot-X-short.mp4
```

### 1.3 Merkez Crop Değeri

| Kaynak | Genişlik (scale sonrası) | Merkez Crop X |
|--------|--------------------------|---------------|
| 1280×720 → scale=-2:1920 | ~3413px | 1166 |

### 1.4 Karakter Konumu Kontrolü

Crop uygulamadan önce frame çıkararak karakterin konumunu doğrula:

```bash
ffmpeg -y -ss 7 -i shot-X.mp4 -vframes 1 -q:v 2 frame-check.jpg
```

Karakter merkeze yakınsa X=1166, sola yakınsa X=1066, sağa yakınsa X=1266 kullan.

---

## 2. Segment Bazlı Crop (Konuşmacı Takibi)

### 2.1 Ne Zaman Kullanılır

İki veya daha fazla karakter aynı frame'de konuşuyorsa ve 9:16 crop'a sığmıyorsa.

### 2.2 Workflow

```
1. Orijinal 16:9 shot'ı oku
2. Her karakter için farklı crop X değeri belirle
3. Konuşma zamanlamasına göre segmentlere böl
4. Her segment'i ayrı dosya olarak kaydet
5. Kullanıcı onayını bekle
6. Onay sonrası birleştir
```

### 2.3 ffmpeg Segment Komutu

```bash
# Parça 1: 0-2sn Arda (X=1066)
ffmpeg -y -ss 0 -t 2 -i shot-8.mp4 \
  -vf "scale=-2:1920,crop=1080:1920:1066:0,format=yuv420p" \
  -c:v libx264 -crf 18 -profile:v high \
  -c:a aac -ar 48000 -ac 2 \
  seg1-arda-0-2s.mp4

# Parça 2: 2-7.5sn Kiko (X=1900)
ffmpeg -y -ss 2 -t 5.5 -i shot-8.mp4 \
  -vf "scale=-2:1920,crop=1080:1920:1900:0,format=yuv420p" \
  -c:v libx264 -crf 18 -profile:v high \
  -c:a aac -ar 48000 -ac 2 \
  seg2-kiko-2-7.5s.mp4
```

### 2.4 Önemli Kurallar

- **`-ss` ve `-t` kullan** (`-vf` içindeki `trim` filter'ı güvenilir çalışmaz)
- **Her parça ayrı dosya** olarak kaydedilir
- **Birleştirme yapılmaz** — kullanıcı onay verene kadar beklenir
- **Orijinal shot'a dokunulmaz**

### 2.5 Birleştirme (Onay Sonrası)

```bash
cat > concat.txt << EOF
file 'seg1-arda-0-2s.mp4'
file 'seg2-kiko-2-7.5s.mp4'
file 'seg3-arda-7.5-12s.mp4'
file 'seg4-kiko-12-15s.mp4'
EOF

ffmpeg -y -f concat -safe 0 -i concat.txt \
  -c:v libx264 -crf 18 -profile:v high \
  -c:a aac -ar 48000 -ac 2 \
  AS-EP0X-shot-X-short.mp4
```

---

## 3. Pan ve Kaydırma Teknikleri

### 3.1 Yavaş Pan (Takip)

Arda gibi bir karakter yürüyorken kamera onu takip eder:

```bash
# 4sn sonra başlayıp 10sn'de duran, sağa 40px/s pan
ffmpeg -y -i shot-X.mp4 \
  -vf "scale=-2:1920,crop=1080:1920:1166+40*max(0,min(t-4,10)):0,format=yuv420p" \
  ...
```

### 3.2 Pan Sınırı

Pan, karakterin yürüme süresiyle sınırlı olmalı:

```bash
# Pan 10sn'de durur (t>10 sonrası hareket yok)
1166+40*min(t,10)
```

### 3.3 Hızlı Geçiş (Kamera Değişimi)

Konuşmacı değişirken segment approach kullanılır — tek frame'de kesim.

---

## 4. Tam Episode Birleştirme

### 4.1 Short Versiyon (9:16)

```bash
cat > concat-full.txt << EOF
file 'AS-EP0X-shot-1-short.mp4'
file 'AS-EP0X-shot-2-short.mp4'
...
file 'AS-EP0X-shot-8-short.mp4'
EOF

ffmpeg -y -f concat -safe 0 -i concat-full.txt \
  -c:v libx264 -crf 18 -profile:v high \
  -c:a aac -ar 48000 -ac 2 \
  AS-EP0X-FULL_NAME-full.mp4
```

### 4.2 Orijinal Versiyon (16:9)

```bash
cat > concat-original.txt << EOF
file 'shot-1.mp4'
file 'shot-2.mp4'
...
file 'shot-8.mp4'
EOF

ffmpeg -y -f concat -safe 0 -i concat-original.txt \
  -c:v libx264 -crf 18 -profile:v high \
  -c:a aac -ar 48000 -ac 2 \
  01_SHOTS/AS-EP0X-FULL_NAME-full.mp4
```

---

## 5. Social Media Metadata

### 5.1 Dosya Yapısı

Her video için ayrı metadata dosyası:

```
05_METADATA/
├── AS-EP0X-youtube.md
├── AS-EP0X-instagram.md
├── AS-EP0X-tiktok.md
└── AS-EP0X-facebook.md
```

### 5.2 Short'lar için Metadata

Short'lar kendi klasöründe metadata dosyasına sahip:

```
04_SHORTS/
├── AS-EP0X-shot-1-short.mp4
├── AS-EP0X-shot-1-metadata.md
├── AS-EP0X-shot-2-short.mp4
├── AS-EP0X-shot-2-metadata.md
...
```

---

## 6. OpenArt Prompt Kuralları

### 6.1 İki Farklı Shot Tipi

| Tip | @image1 Kaynağı | Ne Zaman |
|-----|-----------------|----------|
| **Fresh Quality-Reset** | Canonical character/world reference | Kalite düştüğünde, yeni chain başlarken |
| **Frame-to-Video Continuity** | Önceki shot'un son karesi | Kaliteli olduğu sürece zincir devam eder |

### 6.2 Canonical Reference Tag Sistemi

Fresh quality-reset shot'larda:

- `@image1` = Approved canonical Arda reference
- `@image2` = Approved canonical Pompom Ball reference
- `@image3` = Approved canonical environment reference
- `@image4` = Episode colour / lighting master reference

### 6.3 Continuity Shot'ta

- `@image1` = Önceki shot'un onaylanmış son karesi
- `@image2` = Varsa ikinci karakter reference (örn. Kiko)

### 6.4 Chain Kuralı

- Zincir en fazla 4 shot sürebilir (EP01: Shot 04'te chain bitti)
- Chain bittiğinde: `Next-Shot Dependency: NONE — CHAIN ENDS HERE`
- Yeni chain: Fresh Take Shot ile başlar

### 6.5 Take Shot Workflow

```
1. Fresh Arda's Home world'den temiz kompozisyon oluştur (still image)
2. Take Shot'u onayla
3. Onaylı Take Shot'ı OpenArt'a yükle → @image1 olarak seç
4. Video'yu frame-to-video moduyla üret
```

### 6.6 lip-synchronised speech Çelişkisi

"visibly mouths" kullanırken negatif prompt'tan kaldır:

```text
Do not generate audible spoken dialogue or voices. Arda must still perform the clearly
scripted visible mouth movements at the specified times.
```

---

## 7. Dosya Yapısı Standartı

```
AS-EP0X_EPISODE_NAME/
├── 00_EPISODE_OVERVIEW/
│   ├── 01-overview.md
│   ├── 02-beat-sheet.md
│   └── 03-screenplay.md
├── 01_SHOTS/
│   ├── shot-01-*.md
│   ├── shot-02-*.md
│   └── AS-EP0X-FULL_NAME-full.mp4  (16:9 tam episode)
├── 03_VIDEO_EXPORTS/
│   ├── shot-1.mp4  (orijinal 16:9)
│   ├── shot-2.mp4
│   ├── ...
│   └── openart/
│       ├── shot-01-openart-prompt.md
│       └── shot-01-openart-take-shot-prompt.md  (varsa)
├── 04_SHORTS/
│   ├── 00-shorts-plan.md
│   ├── AS-EP0X-shot-1-short.mp4
│   ├── AS-EP0X-shot-1-metadata.md
│   ├── ...
│   └── AS-EP0X-FULL_NAME-full.mp4  (9:16 tam episode)
└── 05_METADATA/
    ├── AS-EP0X-youtube.md
    ├── AS-EP0X-instagram.md
    ├── AS-EP0X-tiktok.md
    └── AS-EP0X-facebook.md
```

---

## 8. Bilinen Sorunlar

### 8.1 16:9 → 9:16 İki Karakter Sığmama

Orijinal 16:9 frame'de iki karakter uzaktaysa (örn. Arda solda, Kiko sağda), 9:16 crop'a ikisi de sığmaz. Çözüm: segment bazlı crop ile konuşmacıyı takip et.

### 8.2 `trim` Filter'ı Güvenilir Değil

`-vf` içindeki `trim=start=X:end=Y` her zaman doğru çalışmaz. Bunun yerine `-ss` ve `-t` flag'ları kullan.

### 8.3 `crop` Filter'ı `enable` Desteklemiyor

Zaman bazlı crop değişimi için `enable` kullanılamaz. Bunun yerine segment approach veya ffmpeg expression (`if(gte(t,...))`) kullanılır.

### 8.4 ffmpeg Expression Nested Function Escaping

İç içe `if(gte(...))` ifadelerinde virgül escaping karmaşık hale gelir. Mümkünse basit ifadeler veya segment approach tercih edilir.

---

*Bu dosya, 17 Temmuz 2026 session'ında test edilmiş çözümleri içerir.*
*İlgili dosyalar: SHORTS_PRODUCTION_STANDARD.md, SHORTS_SEGMENT_CROP_WORKFLOW.md*
