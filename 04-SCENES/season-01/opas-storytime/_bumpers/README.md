# Opa's Storytime — Shared Bumpers

---

## Amaç

Bu klasör, **tüm Opa's Storytime bölümlerinde ortak** kullanılan açılış ve kapanış
bumper spesifikasyonlarını içerir. Bir kez üretilir, her bölümün başına/sonuna eklenir.
Böylece "bir kural bir kez yazılır" prensibi korunur — bölümler bu dosyalara referans
verir, içeriğini tekrar etmez.

| Dosya | İçerik | Süre |
|---|---|---|
| `opening-bumper.md` | Ortak açılış bumper (kitap açılır) | 3–4 sn (max 5) |
| `closing-bumper.md` | Ortak kapanış bumper (kitap kapanır + end-screen-safe kare) | 4–5 sn (max 6) |
| `render-prompts.md` | Her iki bumper için OpenArt still + video render prompt'ları + negative prompt | — |

---

## Süre Kararı (Series)

- **Bölüm gövdesi: 120 saniye (8 sahne × 15 sn).** 5 bölümün tamamı bu sürede kilitlidir.
- 180 sn kullanılmaz — mevcut standart (`00-CORE/18_VIDEO_STYLE_AND_RETENTION_STANDARD.md`
  §13) long-form tavanını 120 sn kabul eder; 3–4 yaş için 120 sn zaten üst sınırdır.
- Daha uzun süre (150–180 sn) ancak retention datası güçlü çıkarsa, tek pilot bölümle
  ve önce §13 standardı güncellenerek test edilir.

## Toplam Video Süresi

```
Ortak açılış bumper (~3–4 sn)
  + Bölüm gövdesi (120 sn)
  + Ortak kapanış bumper (~4–5 sn)
  ≈ ~128 saniye final video
```

Bumper'lar hikayenin ÜSTÜNE eklenir; 120 sn hikaye beat'lerinden çalınmaz.

---

## Kullanım Kuralı

1. Açılış bumper bölümün EN başına eklenir → ardından bölümün kendi mekan içi açılış
   beat'ine kesme (`00-CORE/31_OPA_INTERACTIVE_STORYTELLING_FORMAT.md` §4). İki açılış
   üst üste bindirilmez.
2. Kapanış bumper bölümün warm final hold'undan SONRA eklenir (§4a).
3. Playlist CTA / end-screen öğeleri video içine değil, açıklama metadata'ya girer
   (`00-CORE/30_YOUTUBE_METADATA_STANDARD.md` §16–§17).

---

*Referans: `00-CORE/18_VIDEO_STYLE_AND_RETENTION_STANDARD.md` §4a/§9a/§9b,*
*`00-CORE/31_OPA_INTERACTIVE_STORYTELLING_FORMAT.md` §4/§4a/§5.*
*Oluşturulma: 4 Temmuz 2026*
