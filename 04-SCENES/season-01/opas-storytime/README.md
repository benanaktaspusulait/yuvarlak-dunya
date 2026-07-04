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

| # | Klasör | Başlık | Mekan | Karakterler | Tema | Süre |
|---|--------|--------|-------|-------------|------|------|
| 01 | `ep01-the-little-cloud-that-waited/` | The Little Cloud That Waited | Learning Room — Reading Corner (indoor) | Opa, Luca, Mimi | Sabır | 120 sn (8×15) |
| 02 | `ep02-the-little-seed-that-listened/` | The Little Seed That Listened | Kiko's Home — Reading Corner | Opa, Kiko, Mimi | Dinleme / yavaş büyüme | 120 sn (8×15) |
| 03 | `ep03-the-star-that-shared-its-light/` | The Star That Shared Its Light | Opa's Tree (gece) | Opa, Luca, Noah | Paylaşma / iyilik | 120 sn (8×15) |
| 04 | `ep04-the-sleepy-leaf/` | The Sleepy Leaf | Central Square — Outdoor Story Blanket (gün batımı) | Opa, Kiko, Noah | Dinlenme / uyku vakti sakinliği | 120 sn (8×15) |
| 05 | `ep05-the-quiet-bird/` | The Quiet Bird | Learning Room — Reading Corner (yağmurlu gün) | Opa, Luca, Mimi | Dinleme / fark etme | 120 sn (8×15) |

Konum çeşitliliği kasıtlıdır: aynı format 4 farklı dünyada (Learning Room, Kiko's
Home, Opa's Tree, Central Square) ve 2 farklı hava/mood'da (güneşli, yağmurlu,
gece, gün batımı) çalışıyor — format dosyasının "Opa's Tree zorunlu değil" kuralını
kanıtlar.

**Süre:** Tüm bölümler 120 sn (8×15) gövdede kilitlidir. 180 sn kullanılmaz — gerekçe
için bkz. `_bumpers/README.md` § Süre Kararı.

---

## Ortak Bumper'lar

Tüm bölümler ortak bir açılış ve kapanış bumper'ı kullanır (bir kez üretilir, her bölüme
eklenir). Spesifikasyon `_bumpers/` klasöründedir:

- `_bumpers/opening-bumper.md` — ortak açılış (3–4 sn, kitap açılır)
- `_bumpers/closing-bumper.md` — ortak kapanış (4–5 sn, kitap kapanır + end-screen-safe kare)
- `_bumpers/README.md` — kullanım kuralı, süre kararı, toplam video süresi

Her bölümün `01-overview.md` dosyası bu bumper'lara referans verir (Opening Bumper /
Closing Bumper bölümleri).

---

## Klasör Yapısı (her bölüm)

`04-SCENES/_templates/EPISODE_TEMPLATE.md` § Kanonik Bölüm Klasör Yapısı'na uygun:

| Dosya | İçerik |
|---|---|
| `01-overview.md` | Episode lock (Series/Playlist dahil), story summary, scene order |
| `02-beat-sheet.md` | 8 shot'lık story rhythm |
| `03-storyboard.md` | Shot-by-shot storyboard |
| `04-assets.md` | Gerekli world/character referansları |
| `05-camera.md` | Lens/yükseklik/hareket tablosu |
| `06-dialogues.md` | Tüm replikler |
| `07-sfx.md` | Ses tasarımı |
| `08-animation-notes.md` | Animasyon notları |
| `09-render-prompts.md` | OpenArt compact prompt'lar + negative prompt |
| `COORDINATE_MAP.md` | Karakter pozisyonları |
| `EPISODE_SUMMARY.md` | İngilizce özet |
| `EPISODE_SUMMARY_TR.md` | Türkçe özet |

---

*Bu klasör Opa's Storytime shot üretimi için tek kaynaktır.*
*Referans: `00-CORE/31_OPA_INTERACTIVE_STORYTELLING_FORMAT.md`, `11-DOCS/02_SEASON_STRATEGY.md`*
*Oluşturulma: 4 Temmuz 2026*
