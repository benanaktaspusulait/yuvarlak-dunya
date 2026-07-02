# Batch Production Workflow — PomPom Hills

---

## Amaç

Bu dosya, 1000+ video üretimi için toplu (batch) üretim iş akışını tanımlar.

Tek tek bölüm üretmek yerine, aynı mekanda veya aynı karakterle birden fazla sahne/bölüm üretmek için optimize edilmiş süreçleri içerir.

---

## 1. Batch Production Stratejisi

### Mekan Bazlı Batch

Aynı mekanda geçen birden fazla bölümü sırayla üret:

```
Central Square batch:
├── S01E01 (15 sahne) — Central Square
├── S01E05 (4 sahne) — Central Square
├── S01E08 (4 sahne) — Central Square
├── S01E10 (4 sahne) — Central Square
└── Toplam: 27 sahne, tek mekan
```

**Avantaj:** World reference bir kez yüklenir, tüm sahneler için kullanılır.

### Karakter Bazlı Batch

Aynı karakteri içeren birden fazla bölümü sırayla üret:

```
Kiko batch:
├── S01E01 (15 sahne) — Kiko
├── S01E02 (4 sahne) — Kiko
├── S01E03 (4 sahne) — Kiko
├── S01E05 (4 sahne) — Kiko
├── S01E06 (4 sahne) — Kiko
├── S01E07 (4 sahne) — Kiko
├── S01E09 (4 sahne) — Kiko
└── Toplam: 39 sahne, tek karakter
```

**Avantaj:** Character reference bir kez yüklenir, tüm sahneler için kullanılır.

### Shot Bazlı Batch

Aynı shot tipini içeren birden fazla sahneyi sırayla üret:

```
Walking shot batch:
├── S01E01 Shot 01 — Kiko yürür
├── S01E02 Shot 01 — Kiko yürür
├── S01E03 Shot 01 — Kiko yürür
└── ...
```

**Avantaj:** Kamera ayarları ve animasyon notları benzer, hız kazanılır.

---

## 2. Production Pipeline (Adım Adım)

### Adım 1: Hazırlık (10 dakika)

```
□ World reference'ı yükle
□ Character reference'ı yükle
□ Compact prompt'u hazırla
□ Previous frame reference'ı yükle (devam sahneleri için)
```

### Adım 2: Üretim (5-10 dakika/sahne)

```
□ Compact prompt'u OpenArt'a yapıştır
□ 4-6 varyasyon üret
□ En iyi varyasyonu seç
□ Reject kurallarını uygula
□ Kabul et veya yeniden üret
```

### Adım 3: Kalite Kontrol (2 dakika/sahne)

```
□ Karakter ölçeği doğru mu? (%10-12 frame)
□ Mekan değişmiş mi? (LOCKED olmalı)
□ Işık tutarlı mı?
□ Renkler pastel mi?
□ Sivri köşe var mı?
□ Text/watermark var mı?
```

### Adım 4: Devam Sahneleri (3-5 dakika/sahne)

```
□ Önceki sahnenin son karesini seç
□ Continuity frame olarak yükle
□ Devam prompt'unu yaz
□ Üret
□ Sürekliliği kontrol et
```

### Adım 5: Birleştirme (5 dakika/bölüm)

```
□ Tüm shot'ları sırayla birleştir
□ Ses ekle (diyalog + SFX + müzik)
□ Süre kontrolü (60 saniye veya 7 dakika)
□ Final kalite kontrol
```

---

## 3. Optimize Edilmiş Compact Prompt Formatı

Her sahne için 600-800 karakterlik optimize prompt:

```text
Use [WORLD] (@image1) as FINAL background. Insert [CHARACTER] (@image2) into existing world.

[CHARACTER] [ACTION]. Natural gentle movement.

World LOCKED: Do not repaint/regenerate/redesign/replace. Background pixels unchanged.

Character LOCKED: Use @image2 exactly. No costume/hairstyle/facial changes.

[CHARACTER] is SMALL preschool child (~[X]% frame). Environment hero (~[Y]%).

Keep original camera. No zoom/crop.

[CHARACTER]: "[DIALOGUE]". Voice: [VOICE DESCRIPTION].

Reject if [CHARACTER] too large, environment changes, wrong world, camera moves.
```

---

## 4. Hızlı Üretim İpuçları

### 1. Referans Yükleme Optimizasyonu

- World reference'ı bir kez yükle, tüm sahnelerde kullan
- Character reference'ı bir kez yükle, tüm sahnelerde kullan
- Previous frame'i sadece devam sahnelerinde yükle

### 2. Prompt Yeniden Kullanımı

- Benzer sahneler için aynı prompt şablonunu kullan
- Sadece aksiyon ve diyalog 부분ını değiştir
- Camera ve lighting ayarlarını koru

### 3. Reddy Tekrar Kullanımı

- Başarılı bir sahneyi referans olarak kullan
- Benzer sahnelerde aynı ayarları kullan
- Reject pattern'ı kaydet, tekrar uygula

### 4. Ses Toplu Üretimi

- Tüm diyalogları tek seferde kaydet
- SFX'leri kütüphane olarak organize et
- Müzik parçalarını yeniden kullan

---

## 5. Batch Production Takvimi

### Haftalık Üretim Hedefi

| Gün | Hedef | Süre |
|-----|-------|------|
| Pazartesi | 4 sahne üret (2 bölüm) | 2-3 saat |
| Salı | 4 sahne üret (2 bölüm) | 2-3 saat |
| Çarşamba | 4 sahne üret (2 bölüm) | 2-3 saat |
| Perşembe | 4 sahne üret (2 bölüm) | 2-3 saat |
| Cuma | 4 sahne üret (2 bölüm) | 2-3 saat |
| Cumartesi | Ses ve montaj | 3-4 saat |
| Pazar | Dinlenme / Planlama | — |

**Toplam:** Haftada 20 sahne = 5 bölüm

### Aylık Hedef

| Ay | Hedef |
|----|-------|
| 1. Ay | 20 bölüm (80 sahne) |
| 2. Ay | 6 bölüm (24 sahne) — Sezon 1 tamamlanır |

---

## 6. Otomasyon Fırsatları

### Prompt Şablonu Otomasyonu

```python
# Örnek: Otomatik prompt oluşturma
def create_prompt(world, character, action, dialogue):
    return f"""
    Use {world} (@image1) as FINAL background.
    Insert {character} (@image2) into existing world.
    {character} {action}. Natural gentle movement.
    World LOCKED: Do not repaint/regenerate/redesign/replace.
    Character LOCKED: Use @image2 exactly.
    {character} is SMALL preschool child (~6-8% frame).
    Environment hero (~92-94%).
    {character}: "{dialogue}".
    Reject if {character} too large, environment changes.
    """
```

### Kontrol Listesi Otomasyonu

```bash
# Otomatik kalite kontrol
for scene in scenes/*.md; do
    check_scale "$scene"
    check_world_lock "$scene"
    check_character_lock "$scene"
    check_negative "$scene"
done
```

### Ses Sentez Otomasyonu

- AI voice ile toplu ses üretimi
- SFX kütüphanesinden otomatik seçim
- Müzik parçalarını otomatik eşleştirme

---

## 7. Batch Production Kontrol Listesi

### Bölüm Başlangıcında

```
□ World reference hazır mı?
□ Character reference hazır mı?
□ Compact prompt şablonu hazır mı?
□ Previous frame reference hazır mı? (devam sahneleri için)
□ Ses dosyaları hazır mı?
```

### Her Sahne Sonunda

```
□ Karakter ölçeği doğru mu?
□ Mekan değişmiş mi?
□ Işık tutarlı mı?
□ Renkler pastel mi?
□ Sivri köşe var mı?
□ Text/watermark var mı?
□ Süre doğru mu?
```

### Bölüm Sonunda

```
□ Tüm sahneler birleştirildi mi?
□ Ses eklendi mi?
□ Süre kontrol edildi mi?
□ Final kalite kontrol yapıldı mı?
□ YouTube formatına uygun mu?
```

---

## 8. Performans Metrikleri

### Üretim Hızı

| Metrik | Hedef | Mevcut |
|--------|-------|--------|
| Sahne/saat | 4-6 | — |
| Bölüm/gün | 1-2 | — |
| Bölüm/hafta | 5-7 | — |

### Kalite Metrikleri

| Metrik | Hedef | Mevcut |
|--------|-------|--------|
| İlk üretim kabul oranı | %60+ | — |
| Revizyon ihtiyacı | < %30 | — |
| Character tutarlılığı | %95+ | — |
| World tutarlılığı | %95+ | — |

---

*Bu belge toplu üretim iş akışı için tek kaynaktır.*
*Son güncelleme: 2 Temmuz 2026*
