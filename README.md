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
│   └── drawings/               ← Karakter referans çizimleri (PNG)
├── POMPOM_HILLS_PRODUCTION/     ← Dünya-bazlı üretim paketleri (tek kaynak)
│   ├── 00_GLOBAL_RULES/         ← Şablonlar + global environment/world standartları
│   ├── 02_WORLDS/               ← Her dünya: canon bible + world-spec + hero view +
│   │                              o dünyada geçen bölüm paketleri (31 mekan)
│   └── 03_EPISODES/             ← Seri-seviyesi dosyalar (Opa's Storytime bumper'ları vb.)
├── 03-PROPS/                   ← Prop kütüphanesi + prop görselleri
├── 05-AI-PROMPTS/              ← AI üretim promptları + ses dosyaları
├── 06-ASSETS/                  ← Genel referans görseller (world/karakter/prop hariç)
├── 07-BRANDING/                ← Marka, sosyal medya, kanal görselleri
│   └── channel-images/         ← YouTube/sosyal medya logo & kapak
├── 08-PRODUCTION/              ← Üretim takibi (TODO, takvim, tracker, QC, asset)
├── 09-ARCHIVE/                 ← Eski/arsiv dosyalar
├── 10-LICENSING/               ← Lisanslama stratejisi ve yol haritası
│
├── environment/                ← Mekan referans görselleri (world PNG'leri, kanonik)
├── videos/                     ← Render edilmiş video çıktıları
│
├── PROJECT_OVERVIEW.md         ← Kapsamlı proje çerçeve belgesi
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
| Mekan detayları | `POMPOM_HILLS_PRODUCTION/02_WORLDS/{MEKAN}/00_CANON/{mekan}-bible.md` |
| Üretim akışı | `00-CORE/PRODUCTION_PIPELINE.md` |
| Süreklilik kuralları | `00-CORE/CONTINUITY_RULES.md` |
| Prompt yazma | `05-AI-PROMPTS/` |
| YouTube yükleme | `07-BRANDING/YOUTUBE_WORKFLOW.md` |
| YouTube metadata (title/description/tags/Shorts) | `00-CORE/30_YOUTUBE_METADATA_STANDARD.md` |
| Video stili, pacing, hook, retention | `00-CORE/18_VIDEO_STYLE_AND_RETENTION_STANDARD.md` |
| Series bumper (Opa's Storytime vb.) ile world micro-opening ayrımı, dosya organizasyonu | `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/MICRO_OPENING_AND_CLOSING_STANDARD.md` |
| Shot'lar arası continuity workflow (@image1 zinciri, transition QA) | `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/SHOT_CONTINUITY_WORKFLOW.md` |
| Sosyal medya görsel formatı (Story/Feed/YouTube platform seti, safe margin) | `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/SOCIAL_MEDIA_IMAGE_FORMAT_STANDARD.md` |
| Opa's Storytime (interactive storytelling sub-series, format, playlist) | `00-CORE/31_OPA_INTERACTIVE_STORYTELLING_FORMAT.md` |
| Brave Little Days (life-skills / günlük hayat becerileri sub-series, format, playlist) | `00-CORE/32_BRAVE_LITTLE_DAYS_LIFE_SKILLS_FORMAT.md` |
| Bölüm detayları | `POMPOM_HILLS_PRODUCTION/02_WORLDS/{MEKAN}/04_EPISODE_PACKAGES/{bolum}/` |
| Üretim takibi | `08-PRODUCTION/` |
| Mekan görselleri (PNG) | `environment/NN-slug.png` veya çok görünümlü `environment/NN-slug/hero-view.png` |
| Karakter görselleri (PNG) | `01-CHARACTERS/drawings/{karakter}.png` |
| Prop görselleri (PNG) | `03-PROPS/{kategori}/...` |
| Video çıktıları | `videos/` |
| Facebook/Instagram event kampanya görselleri (poster/story/reel-cover promptları) | `07-BRANDING/campaigns/{kampanya-adı}/prompts.md` |

## İsimlendirme Standardı

- Numaralı mekan/dosya: `NN-slug` — **2 haneli sıfır dolgulu** numara + **küçük harf, tireli** slug (örn. `06-opas-tree`).
- Çok görünümlü mekan klasörlerinde görünüm dosyaları: `hero-view.png`, `left-view.png`, `right-view.png`, `top-view.png`.
- Mekan numaraları `POMPOM_HILLS_PRODUCTION/02_WORLDS/` bible'ları ile `environment/` görselleri arasında **birebir** eşleşir (25=flower-hill, 26=tree-hill, 27=stone-hill).

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
4. `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/EPISODE_TEMPLATES/SCENE_TEMPLATE.md` kullanarak yeni sahne yaz
5. `05-AI-PROMPTS/` ile OpenArt'ta üret

## Üretim Akışı

```
1. World Reference oluştur (bir kez)
   └── POMPOM_HILLS_PRODUCTION/02_WORLDS/ → Hero Pack PNG'leri
        ↓
2. Character Reference oluştur (bir kez)
   └── 01-CHARACTERS/ → Character PNG'leri
        ↓
3. Sahne yaz
   └── POMPOM_HILLS_PRODUCTION/02_WORLDS/{MEKAN}/04_EPISODE_PACKAGES/ → Scene MD dosyaları
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

## Channel Growth Decisions — Early Launch Phase

> Strategic publishing decisions (early data interpretation, benchmark video, character/world rollout pace, video length, Shorts system, publishing cadence, engagement style, performance tracking) live in `11-DOCS/09_YOUTUBE_STRATEGY.md`. Bu belge kanon üretim/karakter/dünya/senaryo dosyalarını değiştirmez — sadece yayın stratejisini tanımlar.

---

*Bu belge Pompom Hills projesinin ana giriş dosyasıdır.*
*Son güncelleme: 2 Temmuz 2026*
