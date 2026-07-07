# TODO.md — Pompom Hills Profesyonel Standartlar

> Bu dosya, projenin profesyonel production standardına ulaşması için gereken tüm görevleri listeler.
> Her madde öncelik sırasına göre sıralanmıştır.
> Tamamlanan maddeler ✅ ile işaretlenir.

---

## Öncelik 1: Üretim Altyapısı (Acil)

### 1.1 Shot Format Standardizasyonu
- [ ] Tüm shot dosyalarında tutarlı format sağlamak
- [ ] Her shot'ta zorunlu bölümler: Scene Context, Purpose, Visual Prompt, Dialogue, Negative Prompt, Camera, Sound, QA Checklist
- [ ] Eksik bölümleri olan shot dosyalarını tamamlamak
- [ ] Shot dosya adlandırma standardı: `shot-XX-slug.md`

### 1.2 OpenArt Prompt Standardı
- [ ] `00-CORE/OPENART_PROMPT_STANDARD.md` oluştur — tüm promptlar bu formata uymalı
- [ ] Shorts prompt'ları için özel standart: karakter her zaman frame'de görünmeli
- [ ] Her prompt'ta zorunlu: @image1 reference, karakter rengi, karakter pozisyonu, ölçek, negatif prompt
- [ ] Prompt değişkenleri: `{style}`, `{camera}`, `{lighting}` her yerde tutarlı

### 1.3 Shorts Üretim Standardı
- [ ] `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/SHORTS_PRODUCTION_STANDARD.md` oluştur
- [ ] Karakter çıkmama sorunu için: prompt'ta "character MUST be visible in centre of frame" ekle
- [ ] Kalite için: minimum çözünürlük, frame rate, encoding standardı tanımla
- [ ] Shorts prompt şablonu: hook (0-3sn), aksiyon (3-12sn), kapanış (12-15sn)

### 1.4 Character Reference Standardı
- [ ] Her karakter için onaylı hero view PNG'si oluştur
- [ ] `01-CHARACTERS/drawings/` klasörünü tamamla (tüm 23 karakter)
- [ ] Karakter ölçek tablosu: Kiko=100, Mimi=80, Opa=120 birim
- [ ] Karakter renk paleti: her karakter için hex kodları kilitle

---

## Öncelik 2: World Production (Kısa Vade)

### 2.1 Hero View Üretimi
- [ ] 36 world için OpenArt'ta hero view görseli üret
- [ ] Her hero view'ı bible ile karşılaştır, onayla
- [ ] Onaylanan hero view'ları `01_HERO_VIEW/` klasörüne yerleştir
- [ ] Hero view status tracker oluştur

### 2.2 World Spec Tamamlama
- [ ] Eksik world spec dosyalarını tamamla (8 world'de spec yok)
- [ ] World spec formatını standardize et
- [ ] Her world spec'de: purpose, identity, colour palette, lighting, spatial layout, props, consistency rules

### 2.3 World Navigation Haritaları
- [ ] Tüm world'ler arası yürüyüş sürelerini hesapla
- [ ] ASCII navigation haritası oluştur
- [ ] Hangi world komşu, hangisi uzak — netleştir

---

## Öncelik 3: Bölüm Production (Orta Vade)

### 3.1 Shot Dosyaları Kalite Kontrolü
- [ ] Tüm shot dosyalarını QA'dan geçir
- [ ] Eksik Visual Prompt olan shot'ları tamamla
- [ ] Tutarlı olmayan dialogue formatlarını düzelt
- [ ] Negative prompt eksik olan shot'ları tamamla

### 3.2 Episode Overview Tutarlılığı
- [ ] Tüm episode overview'ları aynı formata getir
- [ ] Eksik bilgi alanlarını doldur: duration, characters, location, theme, learning point
- [ ] Hook bölümünü her episode'da güçlendir (ilk 3-5 saniye)

### 3.3 Metadata Oluşturma
- [ ] Her bölüm için YouTube metadata (title, description, tags)
- [ ] Her bölüm için Facebook/Instagram metadata
- [ ] Her bölüm için TikTok metadata
- [ ] Metadata format standardı oluştur

### 3.4 Thumbnail Standardı
- [ ] Her bölüm için thumbnail prompt'u oluştur
- [ ] Thumbnail format: 1280×720, bir mutlu yüz, net aksiyon, sıcak renkler
- [ ] Thumbnail şablonu: `07-BRANDING/THUMBNAIL_TEMPLATE.md`

---

## Öncelik 4: Ses ve Altyazı (Orta Vade)

### 4.1 Ses/Voice Standardı
- [ ] Her karakter için onaylı ses reference'ı
- [ ] Voice continuity kurallarını netleştir
- [ ] ambient sound standardı: her world için tanımlı sesler
- [ ] Music/SFX lisans takibi

### 4.2 Altyazı Standardı
- [ ] EN altyazı: tüm bölümler için zorunlu
- [ ] TR altyazı: tüm bölümler için zorunlu
- [ ] SRT/VTT format standardı
- [ ] Altyazı timing standardı: max 2 satır, max 7 karakter/satır

---

## Öncelik 5: Yayın Altyapısı (Uzun Vade)

### 5.1 Video Export Standardı
- [ ] Master video format: ProRes 422 HQ veya H.264
- [ ] Çözünürlük: 1920×1080, 16:9
- [ ] FPS: 24
- [ ] Ses: Stereo, 48 kHz, 24-bit WAV

### 5.2 YouTube Yükleme Akışı
- [ ] `07-BRANDING/YOUTUBE_WORKFLOW.md` güncelle
- [ ] Otomatik yükleme script'i
- [ ] Playlist organizasyonu
- [ ] Shorts yükleme akışı

### 5.3 Performans Takibi
- [ ] Haftalık performans raporu şablonu
- [ ] İzlenme, beğeni, abone takibi
- [ ] Hangi karakter/world en iyi performans gösteriyor
- [ ] A/B test sistemi

---

## Öncelik 6: Kalite Güvence (Sürekli)

### 6.1 QA Checklist Standardı
- [ ] Shot öncesi QA: karakter, mekan, ışık, süre
- [ ] Shot sonrası QA: output kalitesi, süreklilik, renk
- [ ] Yayın öncesi QA: altyazı, metadata, thumbnail, ses

### 6.2 Red Rules Netleştirme
- [ ] Her red durumu için spesifik kural
- [ ] Red count tracker
- [ ] Yaygın hatalar ve düzeltme önerileri

### 6.3 Continuity Supervisor
- [ ] Shot'lar arası süreklilik kontrolü
- [ ] Karakter görünüm sürekliliği
- [ ] Mekan sürekliliği
- [ ] Işık/renk sürekliliği

---

## Öncelik 7: Organizasyon ve Dokümantasyon (Sürekli)

### 7.1 Dosya Yapısı Standardı
- [ ] Tüm season'lar için tutarlı dizin yapısı
- [ ] Dosya adlandırma standardı: `NN-slug` (2 haneli sıfır dolgulu)
- [ ] Eksik dizinleri oluştur
- [ ] Boş dizinleri temizle

### 7.2 README Güncelleme
- [ ] Ana README.md'yi güncelle (yeni seriler, sezonlar)
- [ ] Her alt dizin için README
- [ ] Contributing.md güncelle

### 7.3 Changelog Takibi
- [ ] Her önemli değişikliği CHANGELOG.md'ye ekle
- [ ] Versiyon numaralandırma sistemi

---

## Öncelik 8: Ölçeklenebilirlik (Uzun Vade)

### 8.1 Batch Üretim Sistemi
- [ ] Toplu shot üretim script'i
- [ ] Toplu metadata oluşturma
- [ ] Toplu altyazı oluşturma

### 8.2 Template Sistemi
- [ ] Yeni bölüm şablonu
- [ ] Yeni karakter şablonu
- [ ] Yeni dünya şablonu
- [ ] Yeni seri şablonu

### 8.3 Otomasyon
- [ ] QA otomasyonu
- [ ] Metadata otomasyonu
- [ ] Altyazı otomasyonu
- [ ] Yükleme otomasyonu

---

## Öncelik 9: Shorts Sorunu Çözümü (Acil — Detaylı)

### 9.1 Karakter Çıkmama Sorunu
**Neden oluyor:**
- Prompt'ta karakter pozisyonu belirsiz ("somewhere in the frame")
- @image1 reference kullanılmıyor
- Karakter scale çok küçük (%5'in altında)
- Negatif prompt'ta "no characters" var

**Çözüm:**
- [ ] Her shorts prompt'unda zorunlu: "Character is CENTRED in frame, 15-20% of frame size"
- [ ] Shorts prompt şablonu oluştur
- [ ] Negatif prompt'tan "no characters" kaldır
- [ ] Her shorts'ta karakter referansı ekle

### 9.2 Düşük Kalite Sorunu
**Neden oluyor:**
- Düşük çözünürlük
- Yanlış encoding
- Kötü frame seçimi
- Renk grading tutarsız

**Çözüm:**
- [ ] Minimum çözünürlük: 1080×1920 (9:16)
- [ ] Encoding standardı: H.264, high profile
- [ ] Frame seçim kriterleri tanımla
- [ ] Renk grading standardı

### 9.3 Shorts Prompt Şablonu

```text
[Hook - ilk 3 saniye]:
Karakter merkezde, direkt ekrana bakıyor. Net ifade. Sıcak ışık.

[Aksiyon - 3-12 saniye]:
Karakter belirli bir hareket yapıyor. Ortam net. Renkler canlı.

[Kapanış - 12-15 saniye]:
Karakter gülümseme veya tekrarlanan cümle. Sıcak bitiş.

Karakter scale: frame'in %15-20'si
Karakter pozisyonu: merkez veya merkez-üst
Işık: sıcak, yumuşak, diffusion
Renk: pastel, canlı, tutarlı
```

---

*Oluşturulma: 7 Temmuz 2026*
*Son güncelleme: 7 Temmuz 2026*
