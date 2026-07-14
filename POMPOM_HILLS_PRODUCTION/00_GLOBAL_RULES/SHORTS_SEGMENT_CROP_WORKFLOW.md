# Shorts Segment Crop Workflow

> Shot'lardan short üretimi için segment bazlı kaydırma (crop) workflow'u.
> Bu dosya, `SHORTS_PRODUCTION_STANDARD.md`'yi tamamlar.

---

## 1. Genel Akış

```
1. Shot dokümanını oku (shot breakdown, aksiyon zamanlaması)
        ↓
2. Shot mp4'ünü 15 parçaya böl (her parça ~1 sn, -c copy)
        ↓
3. Kare çıkararak karakter konumlarını doğrula
        ↓
4. Her parça için hangi karakter odakta belirle
        ↓
5. Her parçaya uygun crop X değeri uygula
        ↓
6. Tüm parçaları birleştir (-c copy concat)
        ↓
7. Süreyi ve kaliteyi doğrula
```

---

## 2. Karakter Konumları (S01E08 — Building Together)

| Karakter | Konum | Tanımlayıcı |
|----------|-------|-------------|
| Arda (koyu saç, mavi gömlek) | Solda | Sol taraf |
| Noah (açık saç, çizgili gömlek) | Sağda | Sağ taraf |
| Bloklar / kule | Ortada | Merkez |

> **ÖNEMLİ:** Karakter isimlerini ve konumlarını HER shot için kare çıkararak doğrula.
> Tüm shot'larda aynı konum garantisi yoktur.

---

## 3. Crop X Değerleri

1280×720 kaynaktan `scale=-2:1920` → genişlik ~3413px.

| Amaç | Crop X | Açıklama |
|------|:------:|----------|
| Sol karakter (Arda) | 1066 | 500px ortaya kaydırılmış |
| Sağ karakter (Noah) | 1216 | 400px ortaya kaydırılmış |
| Merkez (ikisi birlikte / kule) | 1166 | Standart merkez crop |
| Sol karakter (max) | 566 | Maksimum sol kaydırma |
| Sağ karakter (max) | 1616 | Maksimum sağ kaydırma |

---

## 4. ffmpeg Komut Kalıbı

```bash
ffmpeg -y -i part-XX.mp4 \
  -vf "scale=-2:1920,crop=1080:1920:XXXX:0,format=yuv420p" \
  -c:v libx264 -crf 18 -profile:v high \
  -c:a aac -ar 48000 -ac 2 \
  part-XX-short.mp4
```

> **NOT:** `format=yuv420p` ZORUNLU. Bazı kaynak dosyalar yuv444p ile gelir, libx264 bunu kabul etmez.

---

## 5. Birleştirme (Concat)

```bash
# 1. Concat listesi oluştur
rm -f /tmp/concat.txt
for i in $(seq 1 15); do
  part=$(printf '%02d' $i)
  echo "file 'part-${part}-short.mp4'" >> /tmp/concat.txt
done

# 2. Birleştir
ffmpeg -y -f concat -safe 0 -i /tmp/concat.txt -c copy shot-XX-final.mp4
```

---

## 6. Shot Bazlı Kaydırma Tablosu (S01E08)

Her shot için hangi parçada hangi kaydırmanın uygulandığı:

### Shot 01 — Blocks Are Found
| Part | Süre | Aksiyon | Kaydırma |
|------|------|---------|----------|
| 1 | 0-1sn | Continuity hold | Orta (1166) |
| 2-3 | 1-3sn | Noah curious | Sol (566) |
| 4 | 3-4sn | Noah curious | Sol (566) |
| 5 | 4-5sn | Arda giriyor | Sol (566) |
| 6-7 | 5-7sn | Arda geliyor | Sol (566) |
| 8 | 7-8sn | Noah gösteriyor | Sol (566) |
| 9 | 8-9sn | Arda bakıyor | Sağ (1626) |
| 10 | 9-10sn | Arda anlıyor | Sağ (1626) |
| 11-13 | 10-13sn | Noah gesture | Sağ (1366) |
| 14-15 | 13-15sn | Birlikte | Orta (1166) |

### Shot 02 — Choosing Shapes
| Part | Süre | Aksiyon | Kaydırma |
|------|------|---------|----------|
| 1-3 | 0-3sn | Continuity + Arda round block | Sağ (1591) |
| 4-5 | 3-5sn | Noah flat block | Sol (566) |
| 6-8 | 5-8sn | Noah gösteriyor | Sol (566) |
| 9-11 | 8-11sn | Arda bakıyor, anlıyor | Sağ (1626) |
| 12-15 | 11-15sn | Base yerleştirme | Orta (1166) |

### Shot 03 — First Tower Attempt
| Part | Süre | Aksiyon | Kaydırma |
|------|------|---------|----------|
| 1 | 0-1sn | Continuity | Orta (1166) |
| 2-4 | 1-4sn | Noah ikinci blok | Sol (566) |
| 5-7 | 4-7sn | Arda üçüncü blok | Orta (1166) |
| 8-10 | 7-10sn | Arda dördüncü blok | Sağ (1626) |
| 11-15 | 10-15sn | Kule sallanıyor | Orta (1166) |

### Shot 04 — Tower Falls
| Part | Süre | Aksiyon | Kaydırma |
|------|------|---------|----------|
| 1-6 | 0-6sn | Kule devriliyor | Orta (1166) |
| 7-9 | 6-9sn | Arda "oh no" | Sol (566) |
| 10-11 | 9-11sn | Noah konuşuyor | Sağ (1366) |
| 12-13 | 11-13sn | Noah konuşuyor | Sağ (1366) |
| 14-15 | 13-15sn | Arda'ya bakış | Sol (566) |

### Shot 05 — Small Feeling Beat
| Part | Süre | Aksiyon | Kaydırma |
|------|------|---------|----------|
| 1-3 | 0-3sn | Arda üzgün | Sol (566) |
| 4-7 | 3-7sn | Noah teselli | Sağ (1366) |
| 8-11 | 7-11sn | Arda konuşuyor | Sol (566) |
| 12-15 | 11-15sn | Noah konuşuyor | Sağ (1616) |

### Shot 06 — New Plan
| Part | Süre | Aksiyon | Kaydırma |
|------|------|---------|----------|
| 1 | 0-1sn | Continuity | Orta (1166) |
| 2-10 | 1-10sn | Noah planı açıklıyor | Sağ (1216) |
| 11-15 | 10-15sn | Arda anlıyor | Sol (1066) |

### Shot 07 — Careful Together Build
| Part | Süre | Aksiyon | Kaydırma |
|------|------|---------|----------|
| 1 | 0-1sn | Continuity | Orta (1166) |
| 2-4 | 1-4sn | Arda base'ı sabitliyor | Sol (1066) |
| 5-7 | 4-7sn | Noah blok yerleştiriyor | Sağ (1216) |
| 8-15 | 7-15sn | Birlikte inşa | Orta (1166) |

### Shot 08 — Tower Stands
| Part | Süre | Aksiyon | Kaydırma |
|------|------|---------|----------|
| 1 | 0-1sn | Continuity | Orta (1166) |
| 2-4 | 1-4sn | Noah gururla bakıyor | Sağ (1566) |
| 5-7 | 4-7sn | Arda gülüyor | Sol (716) |
| 8-15 | 7-15sn | Kutlama, gülümseme | Orta (1166) |

---

## 7. Dikkat Edilecekler

1. **Kare çıkararak doğrula:** Her shot için en az 3-4 frame çıkararak karakter konumunu kontrol et.
2. **Karakter isimlerini karıştırma:** Arda (koyu saç, mavi) solda, Noah (açık saç, çizgili) sağda.
3. **Kaydırma yönü:** Sol karakter için X küçült (sola), sağ karakter için X artır (sağa).
4. **Ortaya kaydırma:** Sol karakteri ortaya çekmek için X artır, sağ karakteri ortaya çekmek için X küçült.
5. **format=yuv420p zorunlu:** Yoksa ffmpeg sessizce başarısız olur ve 0 byte dosya üretir.
6. **Karakter odaklandığında +350 birim:** Arda veya Noah konuşurken/odakta iken, temel kaydırma değerine 350 birim daha ekle (Arda için sola, Noah için sağa doğru).
6. **Süre kontrolü:** `-c copy` ile kesimde keyframe hizalaması nedeniyle süren hafif sapabilir.

---

## 8. İlgili Dosyalar

| Dosya | Amaç |
|-------|------|
| `SHORTS_PRODUCTION_STANDARD.md` | Shorts format, kalite ve karakter standartları |
| `00-CORE/17_VIDEO_GENERATION_STANDARD.md` | Ana video üretim standardı |
| `00-CORE/VISUAL_STYLE_GUIDE.md` | Görsel stil rehberi |

---

*Oluşturulma: 14 Temmuz 2026 — S01E08 Building Together shorts üretiminden çıkarılan workflow*
