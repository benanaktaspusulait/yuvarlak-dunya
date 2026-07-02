# Yuvarlak Dunya - Pompom Hills v3.0

3-4 yaş için 7 dakika × 26 bölümlük 3D preschool seri dosyası. Pompom Hills; yuvarlak tepeler, ponpon ağaçlar, kıvrımlı yollar, küre evler ve güvenli duygusal keşif üzerine kurulu pastel bir oyuncak dünyasıdır.

## Production Status

| Alan | Durum |
| --- | --- |
| Version | v3.0 |
| Audience | 3-4 yaş |
| Format | 3D animation, 7 dakika × 26 bölüm |
| License | CC-BY-NC 4.0 |
| Scale | Kiko = 100 birim, Mimi = 80 birim, Opa = 120 birim |
| Prompt variables | `{style}`, `{camera}`, `{lighting}` |

## Core Rule

Her görsel ve sahne şu cümleyi geçmelidir: "3-4 yaş çocuk bunu 2 saniyede okuyabilir, korkmaz, kimin ne hissettigini anlar."

## Dizin Yapısı

```
yuvarlak-dunya/
├── 00-CORE/                    ← Tek kaynak master dosyalar
│   ├── CREATIVE_BIBLE.md       ← Duygu, felsefe, çocuk gelişimi
│   ├── VISUAL_STYLE_GUIDE.md   ← Renk, şekil, malzeme, kamera
│   ├── WORLD_BIBLE.md          ← Dünya tanımı (tek kaynak)
│   ├── CHARACTER_GUIDE.md      ← Karakter tanımları (tek kaynak)
│   ├── SERIES_STRUCTURE.md     ← Bölüm yapısı, karakter stratejisi
│   ├── PRODUCTION_PIPELINE.md  ← Üretim akışı (tek kaynak)
│   ├── TECH_SPECS.md           ← 3D teknik standartlar
│   ├── AUDIO_GUIDE.md          ← Ses felsefesi ve standartları
│   ├── VARIABLES.md            ← Prompt değişkenleri
│   └── NEGATIVE_PROMPTS.md     ← Yasak listeleri
│
├── 01-CHARACTERS/              ← Karakter bible dosyaları (13 karakter)
├── 02-WORLDS/                  ← Mekan bible dosyaları (27 mekan)
├── 03-PROPS/                   ← Prop kütüphanesi
├── 04-SCENES/                  ← Sahne dosyaları + şablonlar
│   ├── season-01/              ← Sezon 1 sahneleri
│   └── _templates/             ← Şablonlar
├── 05-AI-PROMPTS/              ← AI üretim promptları + ses dosyaları
├── 06-ASSETS/                  ← Referans görseller
├── 07-BRANDING/                ← Marka ve sosyal medya
├── 08-PRODUCTION/              ← Üretim takibi (TODO, takvim, tracker)
├── 09-ARCHIVE/                 ← Eski/arsiv dosyalar
│
├── README.md                   ← Bu dosya
├── LICENSE
├── CHANGELOG.md
└── CONTRIBUTING.md
```

## Dosya Sorumluluk Haritası

| Konu | Hangi dosyada? |
|------|---------------|
| Duygu ve felsefe | `00-CORE/CREATIVE_BIBLE.md` |
| Görsel stil | `00-CORE/VISUAL_STYLE_GUIDE.md` |
| Dünya tanımı | `00-CORE/WORLD_BIBLE.md` |
| Karakter tanımı | `00-CORE/CHARACTER_GUIDE.md` |
| Karakter detayları | `01-CHARACTERS/{karakter}.md` |
| Mekan detayları | `02-WORLDS/{mekan}.md` |
| Üretim akışı | `00-CORE/PRODUCTION_PIPELINE.md` |
| Süreklilik kuralları | `00-CORE/CONTINUITY_RULES.md` |
| Prompt yazma | `05-AI-PROMPTS/` |
| YouTube yükleme | `07-BRANDING/YOUTUBE_WORKFLOW.md` |
| Bölüm detayları | `04-SCENES/season-01/{bolum}/` |
| Üretim takibi | `08-PRODUCTION/` |

## Prompt Variable System

Tüm promptlar bu üç değişkenle başlar veya biter:

```text
{style} {camera} {lighting}
```

| Variable | Default |
| --- | --- |
| `{style}` | `Pompom Hills v2.1, rounded preschool toy world, pastel colors, matte clay-plush surfaces, toddler-safe emotional clarity` |
| `{camera}` | `stable 50mm preschool camera, eye-level or gentle wide shot, clear readable staging, no Dutch angle, no fisheye, no shaky movement` |
| `{lighting}` | `warm diffused daylight or cozy soft-blue night, soft contact shadows under 25 percent opacity, no hard rim light, no black night values` |

## Quick Start

1. `00-CORE/CREATIVE_BIBLE.md` oku — projenin ruhunu anla
2. `00-CORE/WORLD_BIBLE.md` oku — dünyayı tanı
3. `00-CORE/CHARACTER_GUIDE.md` oku — karakterleri tanı
4. `04-SCENES/_templates/SCENE_TEMPLATE.md` kullanarak yeni sahne yaz
5. `05-AI-PROMPTS/` ile OpenArt'ta üret

## Üretim Akışı

```
1. World Reference oluştur (bir kez)
   └── 02-WORLDS/ → Hero Pack PNG'leri
        ↓
2. Character Reference oluştur (bir kez)
   └── 01-CHARACTERS/ → Character PNG'leri
        ↓
3. Sahne yaz
   └── 04-SCENES/season-01/ → Scene MD dosyaları
        ↓
4. Compact Prompt oluştur
   └── 600-800 karakter OpenArt optimized
        ↓
5. OpenArt'ta üret
   └── World PNG + Character PNG + Compact Prompt → Video
        ↓
6. Kontrol et
   └── Reject kurallarını uygula
        ↓
7. Yayınla
   └── YouTube'a yükle
```

---

*Bu belge Pompom Hills projesinin ana giriş dosyasıdır.*
*Son güncelleme: 2 Temmuz 2026*
