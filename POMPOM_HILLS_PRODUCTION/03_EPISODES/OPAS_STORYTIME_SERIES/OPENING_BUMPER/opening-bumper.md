# Opa's Storytime — Shared Opening Bumper v1.1

> Bu, **tüm Opa's Storytime bölümlerinde birebir aynı** kullanılan ortak açılış klibidir.
> Bir kez üretilir, her bölümün başına eklenir. Bölümlerin kendi mekan içi açılış beat'inin
> (`00-CORE/31_OPA_INTERACTIVE_STORYTELLING_FORMAT.md` §4) YERİNE değil, ONDAN ÖNCE gelir ve
> çok kısadır — iki açılışı üst üste bindirme (bkz. §4 "do not stack both").
>
> Kural kaynağı: `00-CORE/18_VIDEO_STYLE_AND_RETENTION_STANDARD.md` §4a Opening Bumper Rule.
> Kapanış çifti: `POMPOM_HILLS_PRODUCTION/03_EPISODES/OPAS_STORYTIME_SERIES/CLOSING_BUMPER/closing-bumper.md`
> (opening ve closing kasıtlı olarak ayrı klasörlerde tutulur — bkz. seri `README.md`).

---

## Lock

| Alan | Değer |
| --- | --- |
| Tür | Shared series opening bumper (reusable) |
| Süre | 3–4 saniye (hard max 5 sn) |
| Yerleşim | Bölümün EN başı; ardından mekan içi açılış beat'ine kesme |
| Mekan | Yer-nötr (nötr sıcak arka plan; belirli bir dünyayı göstermez) |
| Karakter | Yok (sadece kitap motifi) — opsiyonel olarak Opa'nın eli |
| Ses | Tek yumuşak chime + hafif sıcak ambiyans; loud müzik YOK |
| Yazı | Varsayılan: yazısız görsel ritüel. Opsiyonel 1–2 sn "Opa's Storytime" title (bkz. `31` §5, sadece onaylıysa) |

---

## Visual

```text
A rounded, handcrafted storybook rests on a soft neutral warm surface.
The book gently glows and opens a little. Warm pastel light spills from the pages
(no readable text on the pages). A single soft sparkle drifts up.
Cut into the episode's own cozy opening beat.
```

- Yuvarlak, el yapımı hisli resimli kitap.
- Yumuşak açılış hareketi, sayfalardan sıcak pastel ışık.
- Sayfalarda okunabilir yazı YOK.
- 3–4 saniye sonra bölümün kendi açılış shot'una kesme.

## Sound

- Tek, yumuşak chime (kitap açılırken).
- Altında çok hafif sıcak ambiyans.
- Loud müzik, stinger, whoosh YOK (`18` §11).

## Dialogue

- Yok. (Diyalog bölümün kendi açılış beat'inde başlar: "Come close, little friends." / "Shall we begin?")

## Forbidden

- Uzun logo animasyonu, loud müzik, hızlı montaj, flashy title sequence.
- Belirli bir dünyayı gösterme (yer-nötr kalmalı ki her bölümde tekrar kullanılabilsin).
- Sayfalarda okunabilir yazı (`00-CORE/17_VIDEO_GENERATION_STANDARD.md` §Text Safety).
- Hikayeyi geciktiren cold open.

---

## Production Notes

- Tek sefer render edilir, `assets/` veya branding altında saklanır ve her bölüm montajında başa eklenir.
- 120 sn hikayenin ÜSTÜNE eklenir (hikaye beat'lerinden çalmaz).
- İlk 3–5 saniye kuralı: bumper dahil ilk saniyeler yine merak yaratmalı (`18` §4a).
- Render prompt'ları: `POMPOM_HILLS_PRODUCTION/03_EPISODES/OPAS_STORYTIME_SERIES/OPENING_BUMPER/render-prompts.md`

---

## Bölümlerden Referans Verme

Her bölümün `00_EPISODE_OVERVIEW/01-overview.md` ve `01_SHOTS/shot-01-*.md` dosyaları
bu dosyaya şu mutlak yolla referans verir:

```text
POMPOM_HILLS_PRODUCTION/03_EPISODES/OPAS_STORYTIME_SERIES/OPENING_BUMPER/opening-bumper.md
```

Göreli yol (`../_bumpers/...`) kullanılmaz — bölüm paketleri farklı dünya klasörlerinde
yaşadığı için göreli yollar dünya taşındığında kırılır (bkz. seri `README.md` § Yol Kuralı).

---

*Referans: `00-CORE/18_VIDEO_STYLE_AND_RETENTION_STANDARD.md` §4a, `00-CORE/31_OPA_INTERACTIVE_STORYTELLING_FORMAT.md` §4–§5.*
*Versiyon: 1.1 — Ayrı klasöre taşındı (opening/closing split), mutlak yol referansına geçildi. 4 Temmuz 2026*
