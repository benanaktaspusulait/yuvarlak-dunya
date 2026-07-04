# Opa's Storytime — Scene Klasörü

---

## Amaç

Bu klasör, **Opa's Storytime** sub-series'ine ait bölümlerin shot seviyesindeki
production dosyalarını içerir.

Format standardı: `00-CORE/31_OPA_INTERACTIVE_STORYTELLING_FORMAT.md` (tek kaynak).
Sub-series tanımı: `11-DOCS/02_SEASON_STRATEGY.md` § Recurring Sub-Series.

Bu klasör, Sezon 1'in normal `s01eNN-slug/` numaralandırmasından **kasıtlı olarak
ayrıdır**. Opa's Storytime bölümleri düzenli bölüm sırasına girmez; kendi playlist'i
(`Opa's Storytime | Gentle Preschool Stories`) ve kendi tekrarlayan formatıyla
takip edilir. Bölümler yine Sezon 1 üretim takvimine ve karakter/dünya onboarding
politikasına dahildir — sadece dosya organizasyonu ayrıdır.

---

## Format Kuralları (özet)

- Opa + en az 2 çocuk karakter zorunlu, önerilen maksimum Opa + 2-3 çocuk.
- Opa 10-15 saniyeden uzun tek başına konuşmaz; her zaman bir çocuk tepkisi gelir.
- Mekan hikaye moduna göre seçilir — Opa's Tree zorunlu değildir.
- Her bölüm tek bir duygusal tema işler, ders anlatılmaz, hikaye içinde hissettirilir.
- Açılış beat'i 3-6 saniye, sabit ("Come close, little friends." / "Shall we begin?" tarzı).

---

## Bölüm Listesi

Bölüm paketleri artık world-based üretim yapısında, kendi dünya klasörlerinin
`04_EPISODE_PACKAGES/` altında yaşıyor (bkz. `POMPOM_HILLS_PRODUCTION/02_WORLDS/`).
Bu klasör (`03_EPISODES/OPAS_STORYTIME_SERIES/`) sadece **seri-seviyesi** ortak
dosyaları (bumper'lar, bu README) tutar — bölüm shot/overview dosyalarını değil.

| # | Bölüm Paketi Yolu | Başlık | Mekan | Karakterler | Tema | Süre |
|---|--------|--------|-------|-------------|------|------|
| 01 | `02_WORLDS/LEARNING_ROOM/04_EPISODE_PACKAGES/OPA_STORYTIME_EP01_THE_LITTLE_CLOUD_THAT_WAITED/` | The Little Cloud That Waited | Learning Room — Reading Corner (indoor) | Opa, Luca, Mimi | Sabır | 120 sn (8×15) |
| 02 | `02_WORLDS/KIKOS_HOME/04_EPISODE_PACKAGES/OPA_STORYTIME_EP02_THE_LITTLE_SEED_THAT_LISTENED/` | The Little Seed That Listened | Kiko's Home — Reading Corner | Opa, Kiko, Mimi | Dinleme / yavaş büyüme | 120 sn (8×15) |
| 03 | `02_WORLDS/OPA_TREE/04_EPISODE_PACKAGES/OPA_STORYTIME_EP03_THE_STAR_THAT_SHARED_ITS_LIGHT/` | The Star That Shared Its Light | Opa's Tree (gece) | Opa, Luca, Noah | Paylaşma / iyilik | 120 sn (8×15) |
| 04 | `02_WORLDS/CENTRAL_SQUARE/04_EPISODE_PACKAGES/OPA_STORYTIME_EP04_THE_SLEEPY_LEAF/` | The Sleepy Leaf | Central Square — Outdoor Story Blanket (gün batımı) | Opa, Kiko, Noah | Dinlenme / uyku vakti sakinliği | 120 sn (8×15) |
| 05 | `02_WORLDS/LEARNING_ROOM/04_EPISODE_PACKAGES/OPA_STORYTIME_EP05_THE_QUIET_BIRD/` | The Quiet Bird | Learning Room — Reading Corner (yağmurlu gün) | Opa, Luca, Mimi | Dinleme / fark etme | 120 sn (8×15) |

(Yollar `POMPOM_HILLS_PRODUCTION/` kök dizinine göredir.)

Konum çeşitliliği kasıtlıdır: aynı format 4 farklı dünyada (Learning Room, Kiko's
Home, Opa's Tree, Central Square) ve 2 farklı hava/mood'da (güneşli, yağmurlu,
gece, gün batımı) çalışıyor — format dosyasının "Opa's Tree zorunlu değil" kuralını
kanıtlar.

**Süre:** Tüm bölümler 120 sn (8×15) gövdede kilitlidir. 180 sn kullanılmaz — gerekçe
için bkz. `OPENING_BUMPER/README.md` (aşağıdaki) § Süre Kararı.

---

## Ortak Bumper'lar — Ayrı Klasörler

Açılış ve kapanış bumper'ı **kasıtlı olarak ayrı klasörlerdedir** — bunlar farklı
üretim varlıkları (farklı süre, farklı yerleşim, farklı render zamanlaması), tek bir
`_bumpers/` klasöründe birleştirmek onları tek bir şeymiş gibi gösterip karıştırıyordu.
Bu, repo'nun dünya klasörlerinde zaten kullandığı ayrık `03_OPENINGS/` deseniyle de
tutarlıdır.

| Klasör | İçerik |
|---|---|
| `OPENING_BUMPER/opening-bumper.md` | Ortak açılış spesifikasyonu (3–4 sn, kitap açılır) |
| `OPENING_BUMPER/render-prompts.md` | Açılış için OpenArt still + video prompt'ları |
| `CLOSING_BUMPER/closing-bumper.md` | Ortak kapanış spesifikasyonu (4–5 sn, kitap kapanır + end-screen-safe kare) |
| `CLOSING_BUMPER/render-prompts.md` | Kapanış için OpenArt still + video prompt'ları |

**Süre Kararı (Series):**

- Bölüm gövdesi: 120 saniye (8 sahne × 15 sn). 5 bölümün tamamı bu sürede kilitlidir.
- 180 sn kullanılmaz — mevcut standart (`00-CORE/18_VIDEO_STYLE_AND_RETENTION_STANDARD.md`
  §13) long-form tavanını 120 sn kabul eder; 3–4 yaş için 120 sn zaten üst sınırdır.
- Daha uzun süre (150–180 sn) ancak retention datası güçlü çıkarsa, tek pilot bölümle
  ve önce §13 standardı güncellenerek test edilir.

**Toplam Video Süresi:**

```
Ortak açılış bumper (~3–4 sn)
  + Bölüm gövdesi (120 sn)
  + Ortak kapanış bumper (~4–5 sn)
  ≈ ~128 saniye final video
```

Bumper'lar hikayenin ÜSTÜNE eklenir; 120 sn hikaye beat'lerinden çalınmaz.

**Kullanım Kuralı:**

1. Açılış bumper bölümün EN başına eklenir → ardından bölümün kendi mekan içi açılış
   beat'ine kesme (`00-CORE/31_OPA_INTERACTIVE_STORYTELLING_FORMAT.md` §4). İki açılış
   üst üste bindirilmez.
2. Kapanış bumper bölümün warm final hold'undan SONRA eklenir (§4a).
3. Playlist CTA / end-screen öğeleri video içine değil, açıklama metadata'ya girer
   (`00-CORE/30_YOUTUBE_METADATA_STANDARD.md` §16–§17).

**Yol Kuralı:** Bölüm paketleri artık her biri farklı bir dünya klasöründe yaşadığı için
(`02_WORLDS/{MEKAN}/04_EPISODE_PACKAGES/{bölüm}/`), bölüm dosyalarından bumper'lara
göreli yol (`../_bumpers/...`) ile referans VERİLMEZ — dünya taşındığında kırılır.
Bunun yerine repo köküne göre **mutlak yol** kullanılır:

```text
POMPOM_HILLS_PRODUCTION/03_EPISODES/OPAS_STORYTIME_SERIES/OPENING_BUMPER/opening-bumper.md
POMPOM_HILLS_PRODUCTION/03_EPISODES/OPAS_STORYTIME_SERIES/CLOSING_BUMPER/closing-bumper.md
```

Her bölümün `00_EPISODE_OVERVIEW/01-overview.md` (Opening/Closing Bumper bölümleri) ve
`01_SHOTS/shot-01-*.md` / `shot-08-*.md` dosyaları bu mutlak yollara referans verir.

---

## Bölüm Paketi Klasör Yapısı

Her bölüm paketi (`02_WORLDS/{MEKAN}/04_EPISODE_PACKAGES/{BÖLÜM}/`)
`POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/EPISODE_TEMPLATES/EPISODE_TEMPLATE.md`'ye uygundur:

| Alt Klasör / Dosya | İçerik |
|---|---|
| `00_EPISODE_OVERVIEW/01-overview.md` | Episode lock (Series/Playlist dahil), story summary, scene order, Opening/Closing Bumper, QA Status |
| `00_EPISODE_OVERVIEW/02-beat-sheet.md` | 8 shot'lık story rhythm |
| `00_EPISODE_OVERVIEW/03-storyboard.md` | Shot-by-shot storyboard |
| `00_EPISODE_OVERVIEW/04-assets.md` | Gerekli world/character referansları |
| `00_EPISODE_OVERVIEW/05-camera.md` | Lens/yükseklik/hareket tablosu |
| `00_EPISODE_OVERVIEW/06-dialogues.md` | Tüm replikler |
| `00_EPISODE_OVERVIEW/07-sfx.md` | Ses tasarımı |
| `00_EPISODE_OVERVIEW/08-animation-notes.md` | Animasyon notları |
| `00_EPISODE_OVERVIEW/09-render-prompts.md` | OpenArt compact prompt'lar + negative prompt |
| `00_EPISODE_OVERVIEW/COORDINATE_MAP.md` | Karakter pozisyonları |
| `00_EPISODE_OVERVIEW/EPISODE_SUMMARY.md` | İngilizce özet |
| `00_EPISODE_OVERVIEW/EPISODE_SUMMARY_TR.md` | Türkçe özet |
| `01_SHOTS/` | 8 shot dosyası (`shot-01-...md` … `shot-08-...md`), Scene QA'dan geçti |
| `02_CONTINUITY_FRAMES/` | Continuity frame görselleri (render sonrası) |
| `03_VIDEO_EXPORTS/` | Render edilmiş shot/episode videoları |
| `04_SHORTS/` | Shorts kırpımları |
| `05_METADATA/youtube-metadata.md` | `00-CORE/30_YOUTUBE_METADATA_STANDARD.md` §16 şablonuna göre title/description/tags/hashtag/Shorts |
| `06_ARCHIVE/` | Eski versiyonlar |

---

*Bu klasör Opa's Storytime seri-seviyesi (bumper) dosyaları için tek kaynaktır.*
*Bölüm shot/overview dosyaları için ilgili dünya klasörüne bakın (`02_WORLDS/{MEKAN}/04_EPISODE_PACKAGES/`).*
*Referans: `00-CORE/31_OPA_INTERACTIVE_STORYTELLING_FORMAT.md`, `11-DOCS/02_SEASON_STRATEGY.md`*
*Oluşturulma: 4 Temmuz 2026 · Güncelleme: opening/closing bumper ayrı klasörlere taşındı, mutlak yol referansına geçildi.*
