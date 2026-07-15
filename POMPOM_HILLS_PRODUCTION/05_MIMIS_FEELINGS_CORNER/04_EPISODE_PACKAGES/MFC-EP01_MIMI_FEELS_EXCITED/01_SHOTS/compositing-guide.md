# Shot 5 & Shot 6 — Compositing Kılavuzu

> Bu dosya, After Effects veya DaVinci Resolve'ta yapılacak compositing işlemleri için adım adım rehberdir.

---

## Gerekli Araçlar

- **After Effects** veya **DaVinci Resolve** ( Fusion veya Edit + Color)
- **Topaz Video AI** veya **Real-ESRGAN** (AI restoration için)
- FFmpeg (referans kare çıkarma için — tamamlandı)

---

## Hazırlanan Dosyalar

```
01_SHOTS/
├── shot-5.mp4                    # Orijinal (sorunlu)
├── shot-5-backup.mp4             # Yedek
├── shot-5-ref/
│   ├── frame-0s.jpg
│   ├── frame-3s.jpg
│   ├── frame-7s.jpg
│   ├── frame-10s.jpg
│   └── frame-14s.jpg
├── shot-6.mp4                    # Orijinal (sorunlu)
├── shot-6-backup.mp4             # Yedek
├── shot-6-ref/
│   ├── frame-0s.jpg
│   ├── frame-3s.jpg
│   ├── frame-7s.jpg
│   ├── frame-10s.jpg
│   └── frame-14s.jpg
├── shot-1.mp4                    # Referans (temiz)
└── shot-4.mp4                    # Referans (temiz)
```

---

## Shot 5 — Adım Adım Compositing

### Adım 1: Proje Oluştur
- Yeni After Effects / DaVinci projesi oluştur
- Timeline: 15 saniye, 24fps
- Composition: 1280×720 (orijinal çözünürlük)

### Adım 2: Katmanları Yükle
```
Katman 1: shot-5.mp4 (orijinal video)
Katman 2: shot-5-ref/frame-0s.jpg (temiz arka plan referansı)
Katman 3: Doğru Kiko görüntüsü (ayrı prepare edilecek)
```

### Adım 3: Yanlış Kiko'yu Maskelenir
1. Katman 1'i seç
2. Sol taraftaki insan görünümlü karakterin etrafına mask çiz
3. Mask'ı keyframe ile hareketlendir (karakter hareket ediyorsa)
4. Mask feather: 5-10px (yumuşak geçiş için)
5. Mask expansion: -2px (kenar temizliği için)

### Adım 4: Temiz Background Plate Oluştur
1. shot-5-ref/frame-0s.jpg'ı katman 2 olarak yerleştir
2. Katman 1'deki maskeyi kullanarak yanlış karakteri kaldır
3. Geride kalan boşluğu katman 2 ile doldur
4. Bu işlem tüm 15 saniye için yapılması gerekiyor

**Alternatif (daha hızlı):**
1. Shot-5'in ilk karesinde yanlızca arka planı (Mimi ve Kiko olmadan) temizle
2. Bu temiz kareyi 15 saniye boyunca statik arka plan olarak kullan
3. Mimi'yi orijinal videodan koru (maske ile)

### Adım 5: Doğru Kiko Katmanı Ekle
1. Onaylı Kiko görüntüsünü veya PNG'sini katman 3 olarak yükle
2. Kiko'yu sol tarafa yerleştir (shot-4'teki pozisyona benzer)
3. Kiko'ya küçük hareketler ekle:
   - Hafif nefes alma (scale 100% ↔ 101%)
   - Göz kırpma (2-3 frame'de gözleri kapat)
   - Tek el hareketi (rotation -5° ↔ 5°)
4. Shadow ekle (drop shadow, opacity %20, distance 3px)

### Adım 6: Colour Match
1. Shot-1'den referans kare seç (frame-10s.jpg)
2. Shot-5'e colour match uygula:
   - Siyah seviyesi
   - Orta tonlar
   - Highlight seviyesi
   - White balance
   - Saturation

### Adım 7: Export
- Format: H.264, high profile
- Bitrate: 8 Mbps minimum
- Çözünürlük: 1280×720
- FPS: 24

---

## Shot 6 — Adım Adım Compositing

### Adım 1: Yedekleme (Tamamlandı)
```
shot-6-backup.mp4 mevcut
```

### Adım 2: Sorunlu Bölgeyi Belirle
Shot 6'da yanlış karakter hangi saniyelerde görünüyor?
- frame-0s.jpg → kontrol et
- frame-3s.jpg → kontrol et
- frame-7s.jpg → kontrol et

### Adım 3: Lokal Değişim
Eğer yanlış karakter yalnızca belirli bir bölgedeyse:
1. O bölgeyi maskeyle
2. Temiz arka plan ile değiştir
3. Doğru Kiko katmanını ekle

Eğer zıplama bölgesinde ise:
1. Zıplama bölgesini kes (1-1.5 saniye)
2. Temiz geniş kareden yeniden oluştur
3. Geri kalanını koru

### Adım 4: AI Restoration
Shot 6 için sharpness sorunu yok (7.6, Shot 1 ile uyumlu). Sadece character fix gerekli.

### Adım 5: Colour Match
Aynı işlem — Shot 1 referans ile eşleştir.

---

## AI Restoration Adımı (Shot 5 İçin)

```
1. shot-5.mp4'yü Topaz Video AI'ye yükle
2. Model: Proteus (Fine Tune) veya Artemis (Low Quality)
3. Settings:
   - Recover Detail: 30-40
   - Sharpen: 20-30
   - Reduce Noise: 10-20
   - Dehalo: 10
4. Export: 1280×720, H.264
5. Elde edilen: shot-5-restored.mp4
```

> Not: Restoration sonrası character fix hâlâ gerekli. Restoration yalnızca görüntü kalitesini artırır, yanlış karakteri değiştirmez.

---

## Final Kontrol Listesi

- [ ] Shot 5: Yanlış karakter kaldırıldı mı?
- [ ] Shot 5: Doğru Kiko eklendi mi?
- [ ] Shot 5: AI restoration uygulandı mı?
- [ ] Shot 5: Shot 1 ile colour match uyumlu mu?
- [ ] Shot 6: Yanlış karakter kaldırıldı mı?
- [ ] Shot 6: Doğru Kiko eklendi mi?
- [ ] Shot 6: Colour match uyumlu mu?
- [ ] Tüm shot'lar arasında geçiş sorunsuz mu?
- [ ] Toplam süre 90 saniye mi?

---

*Bu dosya compositing işlemi için tek kaynaktır.*
