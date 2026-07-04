# Opa's Storytime — Shared Closing Bumper v1.1

> Bu, **tüm Opa's Storytime bölümlerinde birebir aynı** kullanılan ortak kapanış klibidir.
> Bölümün kendi sıcak son shot'undan (warm final hold) SONRA gelir. Bölümün duygusal
> kapanışını kesmez; üstüne yumuşak bir seri kimliği ve playlist/end-screen alanı ekler.
>
> Kural kaynağı: `00-CORE/18_VIDEO_STYLE_AND_RETENTION_STANDARD.md` §9a Closing Bumper Rule,
> §9b YouTube End Screen Policy.
> Açılış çifti: `POMPOM_HILLS_PRODUCTION/03_EPISODES/OPAS_STORYTIME_SERIES/OPENING_BUMPER/opening-bumper.md`
> (opening ve closing kasıtlı olarak ayrı klasörlerde tutulur — bkz. seri `README.md`).

---

## Lock

| Alan | Değer |
| --- | --- |
| Tür | Shared series closing bumper (reusable) |
| Süre | 4–5 saniye (hard max 6 sn) |
| Yerleşim | Bölümün warm final hold'undan SONRA |
| Mekan | Yer-nötr (açılış bumper'ıyla aynı kitap motifi) |
| Karakter | Yok (kitap motifi) |
| Ses | Yumuşak müzik kuyruğu (soft tail); loud CTA / abartılı müzik YOK |
| End-screen | Son 3–5 sn end-screen-safe kare (sakin, boşluklu, playlist öğeleri için yer) |

---

## Visual

```text
The same rounded storybook from the opening gently closes.
Warm pastel light settles. A calm, uncluttered final frame holds — visually warm,
with open space for a YouTube suggested-video / playlist element to appear on top.
No important action happens in this frame.
```

- Açılıştaki kitap motifi yumuşakça kapanır.
- Sıcak pastel ışık dinginleşir.
- Son kare sakin ve boşluklu → end-screen öğeleri için uygun (`18` §9b).

## Sound

- Yumuşak müzik kuyruğu (soft tail), yavaşça sönümlenir.
- Loud subscribe/like sesi, stinger YOK.

## Dialogue

- Yok. (Opa'nın son repliği bölümün kendi kapanış beat'inde kalır, ör. "Until next time, little friends.")

## Forbidden (per `18` §9a)

- Loud subscribe request, "smash like" dili.
- Flashing text, uzun credits, abrupt cut to black.
- Alakasız branding ekranı, hikaye render'ı içinde dikkat dağıtan end card.
- Bölümün duygusal kapanışını kesmek.

---

## Production Notes

- Tek sefer render edilir, açılış bumper'ıyla aynı asset seti içinde saklanır (aynı kitap, aynı yüzey, aynı sıcak palet).
- Playlist CTA ve end-screen öğeleri VİDEONUN İÇİNE değil, açıklama/upload metadata'ya
  (`00-CORE/30_YOUTUBE_METADATA_STANDARD.md` §16 Playlist CTA, §17 Public Link Rule) girer.
- 120 sn hikayenin ÜSTÜNE eklenir.
- Render prompt'ları: `POMPOM_HILLS_PRODUCTION/03_EPISODES/OPAS_STORYTIME_SERIES/CLOSING_BUMPER/render-prompts.md`

---

## Bölümlerden Referans Verme

Her bölümün `00_EPISODE_OVERVIEW/01-overview.md` ve `01_SHOTS/shot-08-*.md` dosyaları
bu dosyaya şu mutlak yolla referans verir:

```text
POMPOM_HILLS_PRODUCTION/03_EPISODES/OPAS_STORYTIME_SERIES/CLOSING_BUMPER/closing-bumper.md
```

Göreli yol (`../_bumpers/...`) kullanılmaz — bölüm paketleri farklı dünya klasörlerinde
yaşadığı için göreli yollar dünya taşındığında kırılır (bkz. seri `README.md` § Yol Kuralı).

---

*Referans: `00-CORE/18_VIDEO_STYLE_AND_RETENTION_STANDARD.md` §9a–§9b, `00-CORE/31_OPA_INTERACTIVE_STORYTELLING_FORMAT.md` §4a.*
*Versiyon: 1.1 — Ayrı klasöre taşındı (opening/closing split), mutlak yol referansına geçildi. 4 Temmuz 2026*
