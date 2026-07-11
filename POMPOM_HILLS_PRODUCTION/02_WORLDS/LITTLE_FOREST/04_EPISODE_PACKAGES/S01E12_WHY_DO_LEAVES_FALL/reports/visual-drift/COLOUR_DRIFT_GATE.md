# Colour Drift Gate and Anchor Pipeline

> Pompom Hills kalıcı renk drift çözümü.
> OpenArt video modelleri her shot'ta karanleştirme, contrast artırma, keskinleştirme ve doygunluk düşürme yapar.
> Bu, prompt talimatlarıyla çözülemez. Tek çözüm: sabit anchor + ölçülü normalizasyon + Drift Gate.

---

## Kök Neden

OpenArt frame-to-frame video üretiminde her shot, önceki shot'un final frame'ini yeni doğru kabul eder. Birikimsel hata:

```
Shot 01 final frame (temiz)
→ Shot 02 @image1 olarak kullanılır
→ Shot 02 final frame (hafif bozuk)
→ Shot 03 @image1 olarak kullanılır
→ Shot 03 final frame (daha bozuk)
→ ...ve así devam
```

**Ölçülen drift (S01E12):**
- Ortalama parlaklık: -%8
- Yerel kontrast: +%51
- Kenar keskinliği: +%75
- Laplacian sharpness: +%266
- Ortalama doygunluk: -%42

---

## Onaylı Workflow

```
Generate shot → Calibrate against @image1 → Fixed whole-clip correction → Drift Gate → Export normalized final frame → Use as next @image1
```

**ASLA:** Ham üretilmiş final frame'i @image1 olarak kullanma.

---

## Gerekli Dosyalar

### 1. EPISODE_COLOR_MASTER.png

- Bölümün başından onaylanmış sabit görsel
- Sonradan üretilmiş video frame'inden ALINMAZ
- Tüm bölüm boyunca DEĞİŞTİRİLMEZ
- Tüm shot'lar bu master'a göre kalibre edilir

### 2. analyze_visual_drift.py

```bash
python3 TOOLS/analyze_visual_drift.py \
  --refs shot-01-final.png shot-02-final.png ... \
  --master EPISODE_COLOR_MASTER.png \
  --output-dir reports/visual-drift/
```

Çıktılar:
- `visual-drift-report.json` — Tüm metrikler
- Konsol: parlaklık, kontrast, sharpness, saturation, progressive drift

### 3. normalize_continuity_video.py

```bash
python3 TOOLS/normalize_continuity_video.py \
  --input-video shot-XX.mp4 \
  --input-anchor shot-XX-1-final-frame-normalized.png \
  --episode-master EPISODE_COLOR_MASTER.png \
  --output-video shot-XX-normalized.mp4 \
  --output-final-frame shot-XX-final-frame-normalized.png \
  --report shot-XX-drift-report.json
```

---

## Drift Gate Eşikleri

### Opening-Frame Calibration (Anchor'a göre)

| Metrik | Eşik | Açıklama |
|--------|:----:|----------|
| Ortalama parlaklık | ±2% | Anchor'dan sapma |
| Medyan parlaklık | ±2% | Anchor'dan sapma |
| 10. percentile | ±3% | Anchor'dan sapma |
| 90. percentile | ±3% | Anchor'dan sapma |
| Yerel kontrast | ≤+5% | Anchor'dan fazla olamaz |
| Kenar keskinliği | ≤+10% | Anchor'dan fazla olamaz |
| Doygunluk | ±5% | Anchor'dan sapma |
| Black clipping | ≤+1% | Artamaz |
| White clipping | ≤+1% | Artamaz |

### Whole-Video Stability

- Final parlaklık, düzeltilmiş opening'den %3'ten fazla karanlık olamaz
- Final kontrast %5'ten fazla artamaz
- Final keskinlik %10'dan fazla artamaz
- Gölgeler kademeli derinleşemez
- Highlight'lar sertleşemez
- Frame-to-frame düzeltme titremesi olamaz

### Episode Master Limitleri

- Düzeltilmiş kontrast, episode master'dan %10'dan fazla fazla olamaz
- Düzeltilmiş keskinlik, episode master'dan %15'ten fazla fazla olamaz
- Karanlık alanlar master'dan daha derin olamaz
- Materyal görünümü matte, yumuşak ve preschool-safe kalmalı

---

## Kalibrasyon Yöntemi

1. Anchor (@image1) ve video opening frame karşılaştırılır
2. Sadece görsel drift hesaplanır:
   - Luminance shift
   - Gamma shift
   - Black-point shift
   - Highlight shift
   - Local contrast growth
   - Saturation loss/gain
   - Edge sharpness growth
3. Tek düzeltilmiş profil hesaplanır
4. Bu profil tüm klibe uygulanır

**Önemli:**
- Frame-by-frame değişen düzeltme YAPILMAZ (titreme yaratır)
- Generative editing KULLANILMAZ
- Karakter kimliği, geometri, ifadeler, nesneler, kompozisyon DEĞİŞTİRİLMEZ

---

## Renk Yönetimi

- Üretim çalışma alanı: Rec.709
- continuity PNG: sRGB
- Doğru transfer karakteristikleri ve metadata korunur
- Full-range / limited-range dönüşümü açıkça yönetilir
- Continuity frame'leri asla screenshot ile çıkarılmaz
- Tek tutarlı FFmpeg extraction yöntemi kullanılır

---

## Continuity Rule

```
ASLA ham üretilmiş final frame'i @image1 olarak kullanma.
SADECE kullan: shot-XX-final-frame-normalized.png
```

---

## Kalite Hedefi

Shot 08, Shot 01'in yumuşaklığını korumalı:
- Yüz gradientleri yumuşak
- Saç kenarları yumuşak
- Göz highlight'ları yumuşak
- Matte felt ve plush materyaller
- Yumuşak gölgeler
- Orta-düşük yerel kontrast
- Sert çizgi yok
- Kabalaşmış doku yok
- Kirli yüzey gürültüsü yok
- Aşırı keskinleştirilmiş kumaş yok

---

*Oluşturulma: 11 Temmuz 2026*
