# DON'T DROP IT! — Production Guide

> Bu belge, "DON'T DROP IT!" formatının üretim sürecini ve test metodolojisini açıklar.

---

## 1. Bu Test Neden Farklı?

Mevcut Pompom Shorts'ları:

```
Pompom markası → çocuk hikâyesi → İngilizce/eğitim → olay
```

Bu test:

```
OLAY → merak → komedi/payoff → Pompom
```

**Fark:** İzleyici önce "ne oluyor?" diyor, sonra karakterleri fark ediyor.
Sesi kapalı bile izlenebilir. Eğitim yok. Tek amaç: güldürmek / merak ettirmek.

---

## 2. Üretim Akışı

```
1. @image1 start-frame still üret
   → Kiko + dev dondurma, Central Square, 9:16 dikey
   → Onay al
        ↓
2. OpenArt'ta video üret (shot-01-openart-prompt.md)
   → 10 saniye, 9:16, frame-to-video
   → En yüksek kalite modu
        ↓
3. QA kontrolü
   → Karakterler görünür mü? (centre 60% safe zone)
   → Hikâye sesi kapalı okunur mu?
   → Loop noktası doğal mı?
   → Renk/Işık tutarlı mı?
        ↓
4. Brightness normalizasyonu
   → python3 POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/TOOLS/normalize-brightness.py . 109
        ↓
5. YouTube Shorts olarak yükle
   → 1080×1920 doğrudan (16:9'dan crop değil)
   → Metadata: title, description, tags
        ↓
6. Performans ölç (7 gün sonra)
   → Average view duration
   → View rate
   → Like rate
   → Share rate
   → Comment rate
```

---

## 3. @image1 Üretim Rehberi

### Kompozisyon

```
┌─────────────────────┐
│                     │
│   Sky / Tree (bg)   │
│                     │
│  ┌───────────────┐  │
│  │               │  │
│  │   DONDURMA    │  │  ← Top lavender scoop (tehlikeli eğik)
│  │   (3 top)     │  │  ← Middle yellow scoop
│  │               │  │  ← Bottom pink scoop
│  │   ┌───────┐   │  │
│  │   │ KIKO  │   │  │  ← Worried face, "uh-oh"
│  │   │       │   │  │
│  │   │       │   │  │
│  │   └───────┘   │  │
│  └───────────────┘  │
│                     │
│   Ground / Grass    │
│                     │
└─────────────────────┘
        9:16
```

### Karakter Pozisyonu
- Kiko: merkez, frame'in %25-30'u büyüklüğünde
- Dondurma: Kiko'nun ellerinde, başının üstüne kadar uzanıyor
- Opa: @image1'de YOK — video'da giriyor

### Dondurma Prop'u
- 3 top üst üste: pembe (#F8BBD0), sarı (#FFF9C4), lavanta (#CE93D8)
- Waffle cone: sıcak tan rengi, yuvarlak kenarlar
- Toplam boy: Kiko'nun boyu kadar (neredeyse 100 birim)
- Malzeme: yumuşak, mat, oyuncak dondurma hissi
- En üst top hafifçe yana yatmış (tehlike hissi)

### Onay Kriterleri
- [ ] Kiko tanınabilir (renk, kıyafet, pigtail)
- [ ] Dondurma komik derecede büyük
- [ ] "Bu düşecek" hissi oluşuyor
- [ ] Central Square arka planda tanınabilir
- [ ] 9:16 format, karakter safe zone'da
- [ ] Soft pastel preschool look

---

## 4. Video QA Kontrol Listesi

### Sesli İzleme
- [ ] "Uh-oh…" doğru zamanda, doğru tonda
- [ ] "For me?" doğru zamanda, doğru tonda
- [ ] Ambience rahatsız edici değil
- [ ] Ses seviyeleri dengeli

### Sessiz İzleme (Kritik Test)
- [ ] İlk kare: "Bu düşecek" okunabiliyor mu?
- [ ] Düşme anı: net, takip edilebilir mi?
- [ ] Opa'nın girişi: doğal mı, aniden belirme mi?
- [ ] Kafaya oturma: komik payoff okunuyor mu?
- [ ] Kiko'nun gülüşü: yüz ifadesi + vücut dili okunuyor mu?
- [ ] Loop: son kare başa dönmeye davet ediyor mu?

### Teknik QA
- [ ] Karakterler centre 60% safe zone'da mı?
- [ ] Arka plan sabit mi? (bench, tree, path hareket etmemiş)
- [ ] Dondurma prop'u tutarlı mı? (renk, boyut, şekil)
- [ ] Kiko ve Opa aynı shot içinde kaybolmamış/ışınlanmamış
- [ ] Parlaklık tutarlı (karanlıklaşma yok)
- [ ] HDR/gloss/oversharpening yok
- [ ] 9:16 format doğru

---

## 5. Yayın ve Ölçüm

### YouTube Shorts Metadata

```
Title: DON'T DROP IT! 😱 | Kiko & Opa | Pompom Hills
Description: Kiko has a VERY big ice cream... but can she hold it? 🍦
Watch more Pompom Hills: https://www.youtube.com/@PompomHills
#PompomHills #Shorts #IceCream #Comedy #Cute #Satisfying #Animation
Tags: pompom hills, funny animation, cute cartoon, ice cream,
physical comedy, satisfying, adorable, loop video, kiko, opa
```

### Performans Karşılaştırma

Bu videoyu mevcut eğitim Shorts'larıyla karşılaştır:

| Metrik | Eğitim Shorts (ortalama) | DON'T DROP IT! | Yorum |
|--------|--------------------------|----------------|-------|
| View rate | ? | ? | İlk kare çekiciliği |
| Avg view duration | ? | ? | Retention / loop |
| Like rate | ? | ? | Komedi payoff |
| Share rate | ? | ? | "Bunu görmelisin" |
| Comment rate | ? | ? | Genel kitle etkileşimi |

### 7 Günlük Değerlendirme

Yayından 7 gün sonra bu soruları yanıtla:

1. **View rate** mevcut Shorts'lardan yüksek mi?
   → Evet: İlk kare "preschool" etiketi yemiyor, genel kitleye ulaşıyor
   → Hayır: İlk kare hâlâ "çocuk içeriği" olarak filtrelenebilir

2. **Average view duration** yüksek mi?
   → Evet: Loop çalışıyor, izleyici sonuna kadar izliyor
   → Hayır: Hikâye yeterince okunabilir değil veya ilgi düşüyor

3. **Audience demographics** değişmiş mi?
   → 18-24, 25-34 yaş grubundan izleyici artışı var mı?
   → Coğrafi dağılım genişlemiş mi?

4. **Comment content** nasıl?
   → Genel kitle yorumları mı ("lol", "so cute") yoksa ebeveyn yorumları mı?

---

## 6. Format Varyasyonları (Eğer Test Başarılıysa)

Test başarılı olursa, aynı "micro-gag" mantığıyla:

| # | Konsept | Karakter | Gag |
|---|---------|----------|-----|
| 02 | Giant Balloon | Mimi + Kiko | Balon Mimi'yi yukarı kaldırır |
| 03 | Stack of Cups | Opa | Bardaklar devrilir, Opa'nın kafasına düşer |
| 04 | Bouncy Ball | Kiko | Top zıplar, Kiko yakalayamaz |
| 05 | Windy Day | Mimi | Şapka uçar, Mimi kovalar |

Her biri: 9-12 sn, minimal diyalog, sesi kapalı okunur, loop-friendly.

---

## 7. Risk ve Notlar

### Bu bir deney.
Mevcut Pompom canon'unu bozmuyoruz. Karakterler aynı, dünya aynı, renkler aynı.
Sadece **format** farklı: eğitim → komedi, uzun → kısa, hikâye → gag.

### Eğer çalışmazsa:
- "Preschool" etiketi video seviyesinde mi, kanal seviyesinde mi?
- Kanal seviyesindeyse: tek video ile test edilemez, farklı kanal/strateji gerekir
- Video seviyeseyse: ilk kare / başlık / thumbnail optimizasyonu denenebilir

### Eğer çalışırsa:
- İkinci test: 15-20 sn, daha hikâyeli, genel kitle
- Üçüncü test: Seri formatı (her hafta yeni gag)
- Uzun vade: Pompom Hills "cute funny clips" içerik hattı

---

*Oluşturulma: 9 Ağustos 2026*
*Test: Universal Audience Shorts Format — DON'T DROP IT!*
