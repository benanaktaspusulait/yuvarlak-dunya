# Yuvarlak Dunya - Pompom Hills v2.1

3-4 yas icin 7 dakika x 26 bolumluk 3D preschool seri dosyasi. Pompom Hills; yuvarlak tepeler, ponpon agaclar, kivrimli yollar, kure evler ve guvenli duygusal kesif uzerine kurulu pastel bir oyuncak dunyasidir.

## Production Status

| Alan | Durum |
| --- | --- |
| Version | v2.1 |
| Audience | 3-4 yas |
| Format | 3D animation, 7 dakika x 26 bolum |
| License | CC-BY-NC 4.0 |
| Scale | Kiko = 100 birim, Mimi = 80 birim, Opa = 120 birim |
| Prompt variables | `{style}`, `{camera}`, `{lighting}` |

## Core Rule

Her gorsel ve sahne su cumleyi gecmelidir: "3-4 yas cocuk bunu 2 saniyede okuyabilir, korkmaz, kimin ne hissettigini anlar."

## Production Files

| File | Purpose |
| --- | --- |
| `WORLD_BIBLE_v2.1.md` | 3D stüdyo standardı dünya incili: felsefe, fizik, coğrafya, renk, materyal, hikaye kuralları |
| `CHARACTER_REFERENCE_GUIDE_v2.1.md` | Kiko, Mimi, Opa için kilit karakter, ölçek, hareket, ses ve yasak davranış referansı |
| `SERIES_STRUCTURE_v2.1.md` | Bölüm yapısı, karakter stratejisi, sezon planı |
| `TECH_SPECS.md` | 3D pipeline, model, rig, render ve teslim standartları |
| `WORLD.md` | Kısa dünya özeti |
| `WORLD_DETAILED.md` | Mekanlar, nesneler, sezonlar, sınırlar |
| `VISUAL_STYLE_GUIDE.md` | Şekil dili, renk, ışık, kompozisyon kuralları |
| `CHARACTER_DESIGN_GUIDE.md` | Karakter form, oran ve ifade prensipleri |
| `NAMING_REFINEMENT.md` | İsimlendirme ve seri dili kararları |
| `OPENART_WORLD_PROMPT_PACK.md` | OpenArt dünya promptları |
| `NEGATIVE_PROMPTS.md` | Midjourney, SDXL, Flux için ortak ve araç özel negative prompt listeleri |
| `CONTRIBUTING.md` | Prompt ekleme, görsel onay ve dosya isimlendirme kuralları |
| `CHANGELOG.md` | Sürüm geçmişi |
| `LICENSE` | CC-BY-NC 4.0 lisansı ve ticari kullanım iletişimi |
| `ai-prompts/VISUAL_REFERENCES.md` | Karakter, trio ve ana görsel referans promptları |
| `ai-prompts/VOICE_PROMPTS.md` | Her karakter için AI voice creator ses promptları |
| `ai-prompts/ENVIRONMENT_PROMPTS.md` | Mekan, arka plan, hava ve dünya plate promptları |
| `ai-prompts/TECHNICAL_SHEETS.md` | Master character sheet, turnaround, expression, scale, prop ve storyboard sheet promptları |
| `ai-prompts/ADVANCED_PRODUCTION_PROMPTS.md` | Aksiyon, kamera, gece, renk paleti ve motion test promptları |
| `ai-prompts/SCENE_PROMPTS.md` | Moodboard, lineup, interaction, loopable BG ve poster promptları |
| `examples/` | Örnek PNG çıktıları ve prompt/seed/model metadata dosyaları |
| `scenes/` | Bölüm ve sahne yazımı: beat sheet, shot plan, diyalog, prompt, animation notes |

## Prompt Variable System

Tüm promptlar bu üç değişkenle başlar veya biter:

```text
{style} {camera} {lighting}
```

Önerilen v2.1 değerleri:

| Variable | Default |
| --- | --- |
| `{style}` | `Pompom Hills v2.1, rounded preschool toy world, pastel colors, matte clay-plush surfaces, toddler-safe emotional clarity` |
| `{camera}` | `stable 50mm preschool camera, eye-level or gentle wide shot, no Dutch angle, no fisheye, no shaky movement` |
| `{lighting}` | `warm diffused daylight, soft contact shadows under 25 percent opacity, no hard rim light, no black night values` |

## AI Workflow

1. `ai-prompts/VISUAL_REFERENCES.md` ile Kiko, Mimi, Opa ve trio scale referanslarını üret.
2. `ai-prompts/TECHNICAL_SHEETS.md` ile master character sheet, turnaround, expression, prop ve storyboard sheetlerini kilitle.
3. `ai-prompts/VOICE_PROMPTS.md` ile her karakter için ses promptlarını üretim aracına ver.
4. `ai-prompts/ENVIRONMENT_PROMPTS.md` ile master valley, home, playhouse ve night/day plate üret.
5. `ai-prompts/SCENE_PROMPTS.md` ile poster, moodboard, lineup ve interaction sahneleri üret.
6. `NEGATIVE_PROMPTS.md` içinden kullanılan araca uygun negative prompt'u ekle.

## Scene Writing Workflow

1. Yeni sahne klasörü `scenes/season-01/s01e01-episode-name/` formatıyla açılır.
2. Her sahne dosyası `01-kiko-intro.md` gibi sıra numarası ve kısa amaçla adlandırılır.
3. Dosya içinde Production Lock, Beat Sheet, Shot Plan, Diyalog, Visual Prompt ve Safety Check bulunur.
4. İlk intro sahneleri: `scenes/season-01/s01e01-hello-pompom-hills/`.

## Midjourney / SDXL / Flux Usage

| Tool | Positive Prompt | Negative Prompt |
| --- | --- | --- |
| Midjourney v6 | Prompt + `{style}` + `{camera}` + `{lighting}` + `--style raw --s 250 --v 6.0` | `NEGATIVE_PROMPTS.md` Midjourney satırı |
| SDXL | Prompt + `{style}` + `{camera}` + `{lighting}` | `NEGATIVE_PROMPTS.md` SDXL satırı |
| Flux | Prompt + `{style}` + `{camera}` + `{lighting}` | `NEGATIVE_PROMPTS.md` Flux satırı |

## Example Assets

`examples/` klasörü prodüksiyon referansı değildir; repo içinde placeholder preview ve metadata standardını gösterir. Final görseller, aynı isimlendirme ve `.txt` metadata formatı korunarak onaylı AI çıktılarıyla değiştirilmelidir.

## Visual Approval Gate

Bir görsel ancak şu üç şartı geçerse ana referans olabilir:

1. Karakter ölçeği doğru: Kiko 100, Mimi 80, Opa 120 ama alçak sahnelenmiş.
2. Görsel korku, sert gölge, keskin köşe, gerçekçi doku veya yoğun detay taşımıyor.
3. Prompt dosyasında kullanılan seed, model, variable değerleri ve onay tarihi metadata olarak kayıtlı.
