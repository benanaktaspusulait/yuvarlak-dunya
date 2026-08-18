# Shorts Segment Crop Workflow

> Shot'lardan short üretimi için segment bazlı kaydırma (crop) workflow'u.
> Bu dosya, `SHORTS_PRODUCTION_STANDARD.md`'yi tamamlar.
> Bitmiş bir 16:9 master videonun tamamını story-aware biçimde 9:16'ya çevirmek için
> yetkili kaynak `SHORTS_SMART_REFRAME_STANDARD.md` dosyasıdır. Buradaki sabit X değerleri
> yalnızca karelerle doğrulanan shot-level uygulama örnekleridir.

---

## 1. Genel Akış

```
1. Shot dokümanını oku (konuşmacı, aksiyon ve zamanlamalar)
        ↓
2. Shot'ın ilk/temsilî karelerinde karakter taraflarını doğrula
        ↓
3. Zaman kodlu aktif konuşmacı ve aksiyon crop planı hazırla
        ↓
4. Ardışık aynı-karakter beat'lerini tek segmentte birleştir
        ↓
5. Tek ffmpeg render'ında zaman kodlu crop uygula
        ↓
6. Sesi koruyarak 1080x1920 MP4 üret
        ↓
7. Teknik ve görsel QA yap
```

### 1.1 Güncel shot-to-short uygulama kuralı

Bu bölüm, aşağıdaki eski örnek tabloların üstündeki güncel uygulama kuralıdır. Shot-to-short
çıktısı, onaylanmış bir shot'ın tamamından üretilir; içerik kesilmez, yeni görüntü veya ses
eklenmez.

1. Shot breakdown dosyasındaki gerçek zaman aralıklarını ve konuşmacıyı oku.
2. Kaynak shot'ın ilk karesinden karakterlerin ekran tarafını kare çıkararak doğrula.
3. Aktif konuşmacı, ana aksiyon ve kritik obje için zaman kodlu crop planı hazırla.
4. Aynı karakterin ardışık repliklerini tek crop segmentinde birleştir; gereksiz sağ-sol
   kamera avı oluşturma.
5. Her segmentte `scale=-2:1920` sonrası 1080x1920 crop uygula. X değeri episode'dan
   episode'a veya shot'tan shot'a sabit varsayılmaz.
6. Segmentleri ayrı dosyalara bölüp `-c copy` ile birleştirmek yerine, zaman kodlu crop
   ifadesini tek ffmpeg render'ında kullan. Böylece sınır kareleri ve audio sync korunur.
7. Orijinal shot'ı değiştirme; çıktıyı aynı episode içindeki `EXPORTS/shot-shorts/`
   klasörüne `shot-N-short.mp4` adıyla yaz.
8. Son olarak `ffprobe` ile 1080x1920, 24 fps, H.264, yuv420p, 48 kHz stereo AAC ve
   kaynakla aynı süreyi doğrula; başlangıç, crop geçişleri ve bitişi görsel olarak izle.

Konuşmacı crop'u için kaynakta Noah solda ve Kiko sağda ise örnek X değerleri:

```text
Sol karakter odak:  x=400
Sağ karakter odak:  x=1600
```

Bu değerler yalnızca aynı kaynak kadrajı karelerle doğrulandıktan sonra kullanılabilir.
Başka bir episode, karakter çifti veya kamera yerleşiminde yeniden ölçüm zorunludur.

### 1.2 Zaman kodlu plan dosyası

Yeniden kullanılabilir araç `TOOLS/make_shot_short_speaker_aware.sh` plan dosyasıyla
çalışır. Plan dosyasında her satır `segment_bitis_saniyesi crop_x` biçimindedir; son satır
`default crop_x` olur:

```text
# Shot-1 örneği: Noah solda, Kiko sağda
2.0 400
4.0 1600
6.2 400
8.4 1600
10.6 400
12.8 1600
default 400
```

İlk satır `t < 2.0` için, sonraki satırlar kendi bitişlerine kadar geçerlidir; `default`
son segmenti tanımlar. Komut:

```bash
./TOOLS/make_shot_short_speaker_aware.sh \
  input-shot_hd.mp4 \
  EXPORTS/shot-shorts/shot-1-short.mp4 \
  shot-1-crop-plan.txt
```

Araç aktif konuşmacıyı kadrajda tutar; sesi yeniden encode ederken senkronu korur. Bu,
`make_short_vertical.sh` içindeki sabit merkez crop'un yerine geçen genel araç değildir;
merkez crop yalnızca görsel QA ile tek crop'un yeterli olduğu shot'larda kullanılabilir.

---

## 2. Karakter Konumları (Tarihsel S01E08 örneği)

| Karakter | Konum | Tanımlayıcı |
|----------|-------|-------------|
| Arda (koyu saç, mavi gömlek) | Solda | Sol taraf |
| Noah (açık saç, çizgili gömlek) | Sağda | Sağ taraf |
| Bloklar / kule | Ortada | Merkez |

> Bu tablo yalnızca tarihsel S01E08 örneğidir; global varsayım değildir. Karakter isimlerini
> ve konumlarını HER shot için kare çıkararak doğrula.
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

Zaman kodlu speaker planı için doğrudan tek render tercih edilir:

```bash
ffmpeg -y -i shot_hd.mp4 \
  -vf "scale=-2:1920:flags=lanczos,crop=1080:1920:'if(lt(t,2),400,if(lt(t,4),1600,400))':0,setsar=1,format=yuv420p" \
  -c:v libx264 -preset slow -crf 18 -profile:v high -pix_fmt yuv420p -r 24 \
  -c:a aac -b:a 192k -ar 48000 -ac 2 -movflags +faststart shot-short.mp4
```

---

## 5. Eski parça-birleştirme yöntemi (yalnızca arşiv örneği)

Bu yöntem güncel shot-to-short üretiminde kullanılmaz; zaman kodlu tek render sınır karelerini
ve audio sync'i daha güvenilir korur. Aşağıdaki komutlar yalnızca eski işler için arşiv
referansıdır.

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
2. **Karakter isimlerini karıştırma:** Her episode'da ekran tarafını shot dokümanı ve karelerle doğrula.
3. **Kaydırma yönü:** Sol karakter için X küçült (sola), sağ karakter için X artır (sağa).
4. **Ortaya kaydırma:** Sol karakteri ortaya çekmek için X artır, sağ karakteri ortaya çekmek için X küçült.
5. **format=yuv420p zorunlu:** Yoksa ffmpeg sessizce başarısız olur ve 0 byte dosya üretir.
6. **Karakter odaklandığında:** Konuşmacı crop'unu zaman koduna bağla; kör bir `+350` kuralı uygulama.
7. **Süre kontrolü:** Tek render çıktısının süresi kaynak shot ile aynı olmalı.

---

## 8. İlgili Dosyalar

| Dosya | Amaç |
|-------|------|
| `SHORTS_PRODUCTION_STANDARD.md` | Shorts format, kalite ve karakter standartları |
| `SHORTS_SMART_REFRAME_STANDARD.md` | Finished master → 9:16 smart narrative reframe |
| `TOOLS/make_shot_short_speaker_aware.sh` | Zaman kodlu aktif konuşmacı crop planını tek render'da uygulayan araç |
| `00-CORE/17_VIDEO_GENERATION_STANDARD.md` | Ana video üretim standardı |
| `00-CORE/VISUAL_STYLE_GUIDE.md` | Görsel stil rehberi |

---

*Oluşturulma: 14 Temmuz 2026 — Güncelleme: 18 Ağustos 2026; speaker-aware tek-render shot-to-short workflow*
