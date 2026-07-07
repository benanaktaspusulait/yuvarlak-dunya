# 24 — Shorts Üretim Kalite Kontrolü

---

## Problem Tanımı

16:9 (yatay) formatta üretilmiş bir videodan 9:16 (dikey) shorts kırpmaya çalıştığımızda:

| Sorun | Açıklama | Sonuç |
|-------|----------|-------|
| **Karakter çerçeve dışı** | Karakter kenara kayar, görünmez | İzleyici ne olduğunu anlayamaz |
| **Kırpılma** | Karakterin yarısı görünür | Profesyonel görünmez |
| **Kalite düşüşü** | Büyütme (zoom) yapılır | Pikselleşme, bulanıklık |
| **Kompozisyon bozulması** | Arka plan dengesi kaybolur | Görsel kirlilik |
| **Metin/altyazı kaybı** | Kenar kısımlardaki metin görünmez | Bilgi eksikliği |

---

## Kök Neden Analizi

### Neden Oluyor?

```
16:9 Yatay Video (1920×1080)
    │
    └──→ 9:16 Dikey Kırpma (1080×1920)
         │
         └── Sadece orta kısım alınır
              │
              └── Kenarlardaki karakterler DÜŞÜRÜLÜR
```

**Temel sorun:** 16:9 formatında karakterler genellikle ortada değil, kenarlarda durur. 9:16'ya kırptığında kenarlar gider, karakter kaybolur.

---

## Çözüm Stratejileri

### Strateji 1: Shot Bazlı Üretim (En İyi Çözüm)

**Yaklaşım:** Her sahneyi hem 16:9 hem 9:16 için ayrı ayrı üret.

**Avantajlar:**
- Her formatta mükemmel kompozisyon
- Karakter her zaman çerçevede
- Kalite düşüşü yok
- Profesyonel görünüm

**Dezavantajları:**
- İki kat üretim süresi
- İki kat kaynak kullanımı

**Uygulama:**
```
Shot 01 — 16:9 (YouTube için)
Shot 01 — 9:16 (Shorts/TikTok/Instagram için)
Shot 02 — 16:9 (YouTube için)
Shot 02 — 9:16 (Shorts/TikTok/Instagram için)
...
```

### Strateji 2: Akıllı Kırpma (Orta Çözüm)

**Yaklaşım:** 16:9 videodan kırperken karakter takibi yap.

**Kurallar:**
1. **Karakter merkezde olmalı** — 16:9 üretirken karakteri ortada tut
2. **Güvenli bölge tanımla** — 16:9'un ortasındaki %60'lık kısım 9:16'ya sığar
3. **Dinamik kırpma** — Karakter hareket ettikçe kırpma alanı değişsin

**Güvenli Bölge Haritası:**
```
16:9 Video (1920×1080)
┌─────────────────────────────────────┐
│  Tehlikeli  │  GÜVENLİ  │ Tehlikeli │
│   Bölge    │   BÖLGE   │  Bölge   │
│  (kayıp)   │  (kalır)  │ (kayıp)  │
└─────────────────────────────────────┘
         ↓ Kırpma
    9:16 Video (1080×1920)
    ┌───────────┐
    │ GÜVENLİ   │
    │  BÖLGE    │
    │ (tamamı)  │
    └───────────┘
```

### Strateji 3: Özel Shorts Üretimi (Pratik Çözüm)

**Yaklaşım:** Bazı sahneleri sadece shorts için üret.

**Hangi sahneler?**
- Hook sahneleri (ilk 3-5 sn)
- En duygusal anlar
- En eğlenceli hareketler
- Döngüye uygun sahneler

**Örnek:**
```
YouTube için: Tam hikaye (120 sn, 16:9)
Shorts için: Sadece hook sahnesi (15 sn, 9:16)
```

---

## Üretim Kuralları

### Kural 1: Karakter Pozisyonu

| Durum | 16:9 Üretim | 9:16 Üretim |
|-------|-------------|-------------|
| Tek karakter | Ortada, %60 genişlik | Tam ortada |
| İki karakter | Birbirine yakın, orta %70 | Üst-alt veya yan yana |
| Grup | Ortada toplu | Üst-alt sıralama |

### Kural 2: Kompozisyon

| Öğe | 16:9 | 9:16 |
|-----|------|------|
| **Karakter boyutu** | Frame'in %30-40'ı | Frame'in %40-50'i |
| **Boş alan** | Yanlarda eşit | Üst-altta eşit |
| **Arka plan** | Geniş manzara | Dikey manzara |
| **Metin** | Alt %20 | Üst veya alt %15 |

### Kural 3: Geçişler

| Geçiş | 16:9 | 9:16 |
|-------|------|------|
| **Kamera hareketi** | Yatay pan | Dikey tilt |
| **Karakter girişi** | Yanlardan | Üstten/alttan |
| **Nesne hareketi** | Yatay | Dikey |

---

## Shorts Üretim Kontrol Listesi

### Üretim Öncesi

- [ ] Hangi sahneler shorts için uygun? (Hook, duygusal, eğlenceli)
- [ ] Karakter pozisyonları 9:16'ya uygun mu?
- [ ] Kompozisyon dikey formata uygun mu?
- [ ] Metin/altyazı 9:16'da görünür mü?

### Üretim Sırasında

- [ ] Karakter her zaman çerçevede mi?
- [ ] Arka plan dikey formata uygun mu?
- [ ] Geçişler doğal mı?
- [ ] Ses kalitesi korunuyor mu?

### Üretim Sonrası

- [ ] Karakter tam görünüyor mu?
- [ ] Kalite düşüşü var mı?
- [ ] Metin/altyazı okunabilir mi?
- [ ] İlk 3 saniye dikkat çekici mi?

---

## Dönüştürme Matrisi

### 16:9 → 9:16 Dönüştürme

| Adım | İşlem | Dikkat |
|------|-------|--------|
| 1 | Karakter takibi yap | Karakter her zaman ortada olmalı |
| 2 | Kırpma alanını belirle | Güvenli bölge %60 |
| 3 | Kırp | Sadece güvenli bölgeyi al |
| 4 | Yeniden boyutlandır | 1080×1920 |
| 5 | Metin/altyazı ekle | Üst veya alt %15 |
| 6 | Kalite kontrolü | Karakter görünüyor mu? |

### Örnek: S01E05'ten Shorts Üretimi

**Orijinal 16:9 Sahne:**
```
┌─────────────────────────────────┐
│   Arka plan (gökyüzü)           │
│         ┌─────┐                 │
│         │Kiko │                 │
│         └─────┘                 │
│   Mimi ┌─────┐                  │
│        └─────┘                  │
│   (kenarda)                     │
└─────────────────────────────────┘
```

**Yanlış 9:16 Kırpma:**
```
┌───────────┐
│ Gökyüzü   │
│  ┌─────┐  │
│  │Kiko │  │
│  └─────┘  │
│           │
│ (Mimi     │
│  kayıp!)  │
└───────────┘
```

**Doğru 9:16 Kırpma:**
```
┌───────────┐
│ Gökyüzü   │
│  ┌─────┐  │
│  │Kiko │  │
│  └─────┘  │
│ ┌─────┐   │
│ │Mimi │   │
│ └─────┘   │
│ (ikisi de │
│  görünür) │
└───────────┘
```

---

## Platform Bazlı Shorts Kuralı

| Platform | En-boy | Süre | Karakter Kuralı | Metin Kuralı |
|----------|--------|------|-----------------|--------------|
| YouTube Shorts | 9:16 | 15-30 sn | Her zaman çerçevede | Alt %15 |
| TikTok | 9:16 | 15-30 sn | Her zaman çerçevede | Üst veya alt |
| Instagram Reels | 9:16 | 15-30 sn | Her zaman çerçevede | Üst %15 |
| Facebook Story | 9:16 | 15 sn | Her zaman çerçevede | Alt %15 |

---

## Hata Önleme Stratejileri

### Strateji A: Planlı Üretim (Önerilen)

1. **Shot listesi oluştur** — Hangi sahneler shorts için uygun?
2. **Kompozisyon planı** — Her sahne için karakter pozisyonu
3. **Çift üretim** — Hem 16:9 hem 9:16 için üret
4. **Kalite kontrolü** — Her formatta karakter görünür mü?

### Strateji B: Sonradan Düzeltme (Acil Durum)

1. **Karakter takibi yap** — En iyi kareyi bul
2. **Akıllı kırpma** — Dinamik kırpma alanı
3. **Metin ekleme** — Kaybolan bilgileri metin olarak ekle
4. **Kalite artırma** — Upscale araçları kullan

---

## Örnek: S01E05 "Renkler ve Rüzgar" İçin Shorts Planı

### YouTube Shorts #1 (15 sn — Hook)
```
Sahne: E05, Shot 01-02
İçerik: Kiko uyanır, renkleri görür
Format: 9:16
Karakter: Kiko ortada
Metin: "Bugün ne renkler göreceğiz? 🌈"
```

### YouTube Shorts #2 (20 sn — Keşif)
```
Sahne: E05, Shot 03-05
İçerik: Kırmızı çiçek, mavi gökyüzü
Format: 9:16
Karakter: Kiko merkezde
Metin: "Kırmızı 🌺 Mavi 💙"
```

### YouTube Shorts #3 (15 sn — Döngü)
```
Sahne: E06, Shot 03-04
İçerik: Yapraklar havada dönüyor
Format: 9:16
Karakter: Kiko ve Mimi birlikte
Metin: "Yapraklar dans ediyor! 🍃"
```

---

*Bu dosya shorts üretim kalite kontrolü için tek kaynaktır.*
*Oluşturma tarihi: 7 Temmuz 2026*
