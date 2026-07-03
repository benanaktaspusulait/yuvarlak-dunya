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
├── 02-WORLDS/                  ← Mekan bible dosyaları (27 mekan)
├── 03-PROPS/                   ← Prop kütüphanesi + prop görselleri
├── 04-SCENES/                  ← Sahne dosyaları + şablonlar
│   ├── season-01/              ← Sezon 1 sahneleri
│   └── _templates/             ← Şablonlar
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
| Mekan detayları | `02-WORLDS/{mekan}.md` |
| Üretim akışı | `00-CORE/PRODUCTION_PIPELINE.md` |
| Süreklilik kuralları | `00-CORE/CONTINUITY_RULES.md` |
| Prompt yazma | `05-AI-PROMPTS/` |
| YouTube yükleme | `07-BRANDING/YOUTUBE_WORKFLOW.md` |
| Bölüm detayları | `04-SCENES/season-01/{bolum}/` |
| Üretim takibi | `08-PRODUCTION/` |
| Mekan görselleri (PNG) | `environment/NN-slug.png` veya çok görünümlü `environment/NN-slug/hero-view.png` |
| Karakter görselleri (PNG) | `01-CHARACTERS/drawings/{karakter}.png` |
| Prop görselleri (PNG) | `03-PROPS/{kategori}/...` |
| Video çıktıları | `videos/` |

## İsimlendirme Standardı

- Numaralı mekan/dosya: `NN-slug` — **2 haneli sıfır dolgulu** numara + **küçük harf, tireli** slug (örn. `06-opas-tree`).
- Çok görünümlü mekan klasörlerinde görünüm dosyaları: `hero-view.png`, `left-view.png`, `right-view.png`, `top-view.png`.
- Mekan numaraları `02-WORLDS/` bible'ları ile `environment/` görselleri arasında **birebir** eşleşir (25=flower-hill, 26=tree-hill, 27=stone-hill).

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

## Channel Growth Decisions — Early Launch Phase

==================================================
1. EARLY DATA INTERPRETATION
==================================================

The channel is in its first launch period.

Early performance data should be treated as directional signal, not final proof.

Do not overreact to one high-performing or low-performing video.

Evaluate performance using 24-hour, 72-hour and weekly windows.

The first 30 days are considered the learning phase.

==================================================
2. BENCHMARK VIDEO
==================================================

Meet Kiko is the current early benchmark video.

Future character introductions should be compared against Meet Kiko for:

- opening hook
- character readability
- emotional clarity
- thumbnail strength
- first 3 seconds
- parent-friendly appeal

Do not copy Meet Kiko directly.
Use it as a performance reference.

==================================================
3. CORE CHARACTER ROLLOUT
==================================================

Do not introduce all 14 characters at once.

Launch with a core group of 6 characters.

After the core group is established, introduce new characters slowly.

New character cadence:

One new character every 2–3 months.

New characters should be treated as content events, with teaser Shorts before launch.

==================================================
4. WORLD ROLLOUT
==================================================

Do not introduce all 31 worlds early.

Worlds should be introduced gradually.

Each new world requires:

- clear production purpose
- Hero View
- World Spec
- repeatable visual identity
- at least one episode use case

Focus first on a small number of reusable worlds.

Recommended early worlds:

- Central Square
- Kiko’s Home
- Cloud Hill
- Flower Hill
- Opa’s Tree

==================================================
5. CONTENT PHASES
==================================================

Phase 1:
Character introductions.

Goal:
Help children and parents recognise the first core characters.

Phase 2:
Educational preschool stories with the core characters.

Themes:

- sharing
- taking turns
- colours
- counting
- weather
- feelings
- helping
- friendship
- gentle problem solving

Phase 3:
New character and new world expansion.

==================================================
6. VIDEO LENGTH STRATEGY
==================================================

Main production format:

60–90 second long videos.

120 second videos are allowed only after 60–90 second videos show strong retention.

Do not rush into longer videos before watch-time data supports it.

Longer videos must still keep:

- strong first 3 seconds
- clear preschool pacing
- visual micro-actions every few seconds
- warm ending
- reusable Shorts potential

==================================================
7. LONG VIDEO TO SHORTS SYSTEM
==================================================

Every long video should produce multiple Shorts.

Target:

1 long video
+
3–5 Shorts

Shorts are not random cuts.

Each Short must have its own mini-story:

- hook
- simple action
- emotional beat
- clear ending

Shorts are the discovery engine.
Long videos are the world-building and retention engine.

==================================================
8. PUBLISHING CADENCE
==================================================

Continue daily publishing.

Recommended rhythm:

Day A:
Publish one long video and optionally one supporting Short.

Day B:
Publish 3–4 Shorts derived from recent long videos.

Day C:
Publish next long video.

Day D:
Publish more Shorts.

Do not dump too many similar Shorts at the same time.

Spread Shorts across the day.

Avoid overloading the same character repeatedly unless the data clearly supports it.

==================================================
9. FORMAT PAIRING
==================================================

Track each content item across formats.

For every major video, track:

- Facebook video post
- Instagram post
- Reel
- YouTube long
- YouTube Short

Maintain a simple content matrix:

Content ID
Character
World
Long video status
Shorts status
Facebook status
Instagram status
YouTube status

This prevents missing post equivalents.

==================================================
10. ENGAGEMENT STYLE
==================================================

Use gentle parent-friendly questions in captions.

Examples:

- Who would you share the ball with?
- Which Pompom Hills friend should visit next?
- What colour should Kiko find next?

Avoid aggressive calls to action.

Do not add loud or intrusive engagement prompts inside preschool videos.

==================================================
11. PERFORMANCE TRACKING
==================================================

Create a weekly performance report.

Track:

- views after 3 hours
- views after 24 hours
- views after 72 hours
- reach
- non-follower percentage
- likes
- comments
- shares
- saves
- new followers
- average watch time
- completion rate if available

Do not judge a video only by total views.

Compare videos by format, character, world, hook and length.

==================================================
12. REALISTIC GROWTH EXPECTATIONS
==================================================

Do not treat optimistic growth projections as guaranteed.

The first month goal is not only high views.

The first month goal is to learn:

- which characters attract attention
- which worlds retain viewers
- which video lengths work best
- which formats convert to followers
- which Shorts drive discovery

Growth targets should be reviewed weekly.

==================================================
13. STRATEGIC SUMMARY
==================================================

Pompom Hills will grow through:

- consistent daily publishing
- strong character recognition
- gradual world rollout
- 60–90 second educational stories
- Shorts extracted from long videos
- slow introduction of new characters
- weekly data review

The strategy is not to flood the audience with all characters and worlds.

The strategy is to build recognition, trust and repeat viewing over time.

---

*Bu belge Pompom Hills projesinin ana giriş dosyasıdır.*
*Son güncelleme: 2 Temmuz 2026*
