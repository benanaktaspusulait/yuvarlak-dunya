# ONB-E04 — Welcome to Crystal Cave v1.0

---

## Onboarding Gate

| Kontrol | Durum |
|---|---|
| World bible (`02-WORLDS/32-crystal-cave/`) | ❌ Eksik — sadece `SEASON_2_ONBOARDING/worlds/crystal-cave.md` onboarding taslağı var |
| World Spec | ❌ Eksik |
| Canon Hero View | ❌ Eksik |
| Onboarding policy uygunluğu | ✅ Format + "no complex plot, one character maximum" kuralına uygun tasarlandı |

**Bu bölüm en kısıtlı (bloklu) bölümdür.** Policy §5, madde 1-2: bir dünyanın tanıtım videosu üretilmeden önce Canon Hero View ve production-ready World Spec zorunludur. Bu ikisi de yok. Render'a girmeden önce:

1. `02-WORLDS/32-crystal-cave/32-crystal-cave-bible.md` yazılmalı (bkz. Stone Hill / Rainbow Creek formatı örnek alınabilir)
2. `02-WORLDS/32-crystal-cave/32-crystal-cave-world-spec.md` yazılmalı
3. Hero View görseli üretilip onaylanmalı
4. Bu shot dosyaları Hero View'e göre güncellenmeli

Bu klasördeki shot dosyaları **görsel taslak** (concept placeholder) olarak yazılmıştır — gerçek render promptları değildir.

---

## Episode Lock

| Alan | Değer |
|---|---|
| Tür | World Introduction Video |
| Başlık | "Welcome to Crystal Cave" |
| Süre | 45 saniye (3 shot × 15 sn) |
| Hedef yaş | 3-4 |
| Ana duygu | Merak + hafif büyü (korku değil) |
| Ana tema | Gizli, parlayan bir mağaranın tanıtımı — dünya kendisi kahraman |
| Mekan | Stone Hill (giriş) → Crystal Cave (iç) |
| Karakterler | Luca (mevcut karakter, tek karakter — Policy §5 format kuralı: "one character maximum, or no character") |
| Görsel yoğunluk | Düşük-orta |
| Çatışma | Yok |
| Complex plot | Yok — Policy §5 format kuralı |

---

## Story Summary

Stone Hill'de çiçeklerin arasında gizli bir mağara girişi görünür. Kamera içeri süzülür — yumuşak pastel kristaller (pembe, mavi, lavanta) duvarlarda parlar. Luca girer, yukarı bakar, hayranlıkla durur. Bir kristale dokunur — kristal daha parlak parlar. Title card belirir: "Crystal Cave".

---

## World Introduction Purpose (Policy §6 kontrolü)

| Soru | Cevap |
|---|---|
| Bu mekan nedir? | Stone Hill içinde gizli, kristallerle parlayan küçük bir mağara |
| Hangi hissi yaratır? | Merak, hafif büyü, güvenli gizem |
| Çocuklar burada ne yapabilir? | Kristallere dokunup parlamalarını izleyebilir, sessizce hayran olabilir |
| Diğer dünyalardan farkı ne? | Yer altı, kapalı bir alan olması ama korkutucu değil — yumuşak ışıkla dolu |
| Hatırlanacak görsel öğe | Luca bir kristale dokunduğunda parlaması |

---

## Micro-Moment (Key Discovery)

Luca'nın kristale dokunduğunda kristalin parlaklaşması — bu mağaranın imza anı olur.

---

## Scene Order

| Sıra | Dosya | Süre | Karakter | Amaç |
|---|---|---:|---|---|
| 01 | `shots/shot-01-hidden-entrance.md` | 15 sn | — (dünya kahraman) | Gizli girişin keşfi, Stone Hill'den geçiş |
| 02 | `shots/shot-02-crystal-glow.md` | 15 sn | — (dünya kahraman) | Kristal duvarların gösterimi, pastel parıltı |
| 03 | `shots/shot-03-luca-discovers.md` | 15 sn | Luca | Luca'nın girişi, dokunuş, title card |

---

## Learning Point

Çocuk izleyici Crystal Cave'in adını, mağaranın korkutucu değil büyülü olduğunu ve kristallere nazikçe dokunulabileceğini öğrenir.

---

## Repeated Phrase

```text
(Bu bir dünya tanıtımıdır — tekrarlanan repnik yok, sadece Luca'nın hayranlık ünlemi: "Wow...")
```

---

## Voice Notes

Luca'nın sesi mevcut Voice ID / approved voice reference ile aynı kalmalıdır (`00-CORE/SHOT_PRODUCTION_STANDARD.md`). Shot 01-02'de karakter yoktur, sadece ortam sesi.

---

## Colour Notes

```text
The full episode must appear colour graded as one continuous film.
Maintain identical white balance, exposure, colour temperature, saturation, contrast, brightness and pastel palette across all shots.
No cool shift. No warm shift. No green tint. No magenta tint. No orange grading. No HDR look. No cinematic LUT.
The viewer must not perceive a shot boundary.
```

---

## Lighting Notes

```text
The lighting must continue across shots without reinterpretation.
Maintain identical light direction, light intensity, shadow softness, ambient lighting and highlight behaviour.
Crystal glow is the primary light source inside the cave — soft pastel pink, blue and lavender. No harsh shadows, no darkness that could feel frightening.
```

---

## Negative Prompt

```text
sharp edges, angular rock formations, realistic cave texture, horror, violence, weapons, blood, injury, crying meltdown, screaming, dark shadows, black background, harsh rim light, high contrast, neon colors, dirty grunge texture, photorealism, text, watermark, logo, extra fingers, sharp teeth, claws, deep tunnel, scary cave, bats, spiders, lightning, fire, smoke, handheld camera, Dutch angle, fisheye, cluttered background, unsafe height, adult proportions, oversized character, giant character, environment regenerated, redesigned crystal colours, jagged rock edges, complete darkness, echo horror sound
```

---

## QA Status

| Shot | QA Score | Production Ready |
|------|:--------:|:----------------:|
| 01 | /10 | ⬜ |
| 02 | /10 | ⬜ |
| 03 | /10 | ⬜ |

Reference: `16_VIDEO_QA_SPEC.md`

Required episode-level checks (before render):

- [ ] World bible tamamlandı mı?
- [ ] World Spec tamamlandı mı?
- [ ] Canon Hero View onaylandı mı?
- [ ] Voice continuity checked (Luca).
- [ ] Colour continuity checked.
- [ ] Lighting continuity checked (crystal glow as primary light).
- [ ] World continuity checked (Stone Hill entrance LOCKED, once canon).
- [ ] Story and tempo checked last — mystery without fear (Policy: "no complex plot").

---

*Bu belge ONB-E04 için tek kaynaktır.*
*Referans: `SEASON_2_ONBOARDING/worlds/crystal-cave.md`, `11-DOCS/02_SEASON_STRATEGY.md`*
