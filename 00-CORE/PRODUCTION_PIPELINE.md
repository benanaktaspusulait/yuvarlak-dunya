# Pompom Hills — Production Pipeline (Gold Master)

> **⚠️ DEPRECATED** — This file is a legacy reference. The canonical production pipeline is now:
> `11-DOCS/07_PRODUCTION_PIPELINE.md`
> Only use this file for detailed prompt templates and OpenArt workflow specifics not covered in the canonical bible.

Bu dosya, tüm sahnelerin uyması gereken **tek kaynak** production pipeline'ıdır.
OpenArt bir görsel üretici değil, **prodüksiyon motorudur**. Her sahne yalnızca mevcut,
onaylı dünyaya karakter/prop yerleştirir.

> **Sahne dosyaları için kural:** Her sahne markdown'u en üstte `Follow PRODUCTION_PIPELINE.md`
> yazar ve yalnızca **sahneye özgü** veriyi (Production Lock, koordinatlar, beat, shot plan,
> diyalog, kısa Visual Prompt, continuity) içerir. Ortak kurallar burada tutulur; sahnelerde
> tekrar edilmez.

İlişkili dosyalar: `CONTINUITY_RULES.md` (süreklilik kuralları),
`VISUAL_CONTINUITY_RULES.md` ve `WORLD_IDENTITY_RULES.md` (görsel/world identity kuralları),
`AUDIO_GUIDE.md` ve `EPISODE_AUDIO_WORKFLOW.md` (voice/audio identity kuralları),
`NEGATIVE_PROMPTS.md` (araç bazlı negative listeleri), `VARIABLES.md` (prompt değişkenleri),
`CHARACTER_GUIDE.md` ve `WORLD_BIBLE.md` (kilit referanslar).

---

# Production Philosophy

Pompom Hills is being developed as a long-term animation series.

The goal of the first production phase is NOT to create long episodes.

The goal is to build a professional, repeatable and reliable production pipeline.

Every 1-minute episode is considered a production experiment.

Each episode should help validate or improve one or more production rules.

Examples include:

- character consistency
- world consistency
- shot-to-shot continuity
- camera language
- prompt structure
- production documentation
- pacing
- sound design
- editing workflow
- YouTube publishing workflow

Do not introduce major workflow changes during an active episode.

Finish the episode first.

Review the completed episode.

Only then update the production pipeline.

A production rule is considered stable only after it has been successfully validated across multiple completed episodes.

---

# Phase 1 — Production Lab

Goal:

Create multiple 1-minute episodes.

The objective is to strengthen the production system rather than increase story complexity.

Keep stories intentionally simple.

Use:

- one world whenever possible
- two or three characters maximum
- one emotional idea
- one simple lesson
- four connected shots

Focus on learning every detail of the production process.

Do not rush into longer stories.

---

# Phase 2 — Stable Production

Begin only after the production pipeline has proven to be reliable.

Continue using the same production rules.

Increase production speed while maintaining quality.

---

# Phase 3 — Story Expansion

Only after the production pipeline has matured.

Expand naturally into longer stories.

Begin producing approximately 2-minute episodes.

The workflow should remain the same.

Only the storytelling becomes more complex.

Do not redesign the pipeline.

Scale the existing pipeline.

---

# Core Principle

Never scale complexity before scaling reliability.

A strong production pipeline is more valuable than a long episode.

Every improvement should make future episodes easier to produce.

The production system itself is the first product.

The animated episodes are built on top of that system.

---

## 1. Reference Priority

```
Character Reference
        ↓
World Reference
        ↓
Director Prompt
```

If any conflict exists, **Character Reference and World Reference always override the Director
Prompt**. OpenArt must preserve the approved production assets above any textual interpretation.

---

## 2. Character Rules

**Character Reference is ABSOLUTE. It overrides every prompt.**
If the prompt and the character reference conflict, **follow the character reference.**

Locked and identical across every scene (no redesign allowed):

- Hair
- Eyes
- Face
- Body
- Clothes
- Colors
- Scale

Character sheets live in `01-CHARACTERS/` and `01-CHARACTERS/drawings/`.

---

## 3. World Rules / Environment Lock

**World Reference is ABSOLUTE. The prompt can never modify the world.**

- The environment is **LOCKED**. Never regenerate. Never redesign. Scenes only insert
  characters and scene props into the existing world.
- Use a **CLEAN world render only** — no titles, labels, arrows, frames or layouts.
- Never use an **Environment Sheet** as a world reference. OpenArt interprets sheets as
  physical objects and will place them inside the scene.
- Each World has its own **Hero Pack**: **Hero View · Right View · Back View · Top View**.
- Maintain identical: **layout, architecture, trees, flowers, paths, benches, lamp posts,
  lighting, landmark positions.**
- The **Giant Pompom Tree** keeps its designed pompom colors and shape — never brown, never
  redesigned.

Explicit OpenArt directives:

```
DO NOT redesign environment.
DO NOT regenerate environment.
Maintain identical layout, architecture, trees, flowers, paths, benches, lamp posts, lighting, landmark positions.
```

---

## 4. Scale Rules

- The character occupies approximately **10–12%** of the final frame.
- The environment occupies approximately **85–90%** of the composition.
- The audience should notice the **world first**, then naturally discover the character.
- Preserve realistic scale between the character and: benches, stepping stones, flowers,
  houses, lamp posts, and the Giant Pompom Tree.
- Never generate an oversized character.

---

## 5. Camera Rules

- Environment first, character second.
- Wide compositions.
- **35mm default lens.**
- Eye level.
- Large negative space.
- The world should always feel large and explorable.

---

## 6. OpenArt Rules

- OpenArt is our **production engine**, not an image generator.
- **Consistency > beauty. Production quality > speed.**
- Use the existing World. Do NOT regenerate the world. Do NOT redesign the environment.
- Only insert the scene's character(s) and the scene's props.
- Negatives: apply `NEGATIVE_PROMPTS.md`; do not duplicate its entries inside scene prompts.

---

## 7. Reject & Regenerate Rules

- If the character appears larger than **~12% of the frame** → reject and regenerate with
  stronger scale instruction (target 10–12%; environment 85–90%).
- If the **Giant Pompom Tree** changes in any way (color, shape, becomes brown) → reject.
- If **architecture** changes → reject.
- If **flowers, paths or benches** (or lamp posts, stepping stones) change → reject.
- If the **world layout** changes or the environment is regenerated → reject.
- If an **Environment Sheet appears inside the scene** → reject.
- If **random unreadable text or signs** appear → reject (accept only if tiny and unreadable
  in video).
- If the **lighting** differs from the locked warm daylight → reject.

---

## 8. Production Order

```
1. Load Character Reference
        ↓
2. Load World Reference
        ↓
3. Open Director
        ↓
4. Insert Character
        ↓
5. Generate Shot
        ↓
6. Check Reject Rules
        ↓
7. Accept
        ↓
8. Proceed to next shot
```

Artık prompt yazmıyoruz; **pipeline çalıştırıyoruz.**

---

## 9. Director Workflow (per scene)

1. Open the scene markdown; read its **Production Lock** (scene-specific character, location,
   scale, weather, frame ratio).
2. Load the locked **Character Reference** and **World Reference (Hero Pack)** for that scene.
3. Use the scene's short **Visual Prompt** only to describe the action, mood and framing.
4. Insert the character and scene props into the existing world.
5. Generate the shot, then run the **Reject & Regenerate Rules** (Section 7).
6. Accept only when scale, world, tree, architecture and lighting are preserved.
7. Proceed to the next shot / next scene.

---

## 10. How Scene Files Reference This

Every scene file:

- States `Follow PRODUCTION_PIPELINE.md` at the top.
- Contains only scene-specific data + a short scene-description Visual Prompt.
- Does **not** repeat Environment Lock, Reference Priority, Scale, Camera, OpenArt or Reject
  rules — those live here, in one authoritative place.

Change a rule once here → the whole project (all scenes, all environments, all characters)
updates consistently.

---

# Episode 1 Production Lessons

Bu bölümler, "Goodnight, Tree" (E11) bölümünün üretim sürecinde edinilen dersleri içerir.

---

## Story Structure

- Start with 1-minute episodes.
- Each episode consists of 4 shots.
- Each shot is approximately 15 seconds.
- Use only one world whenever possible.
- Prefer only 2-3 characters per episode.
- Each episode should communicate one simple emotional idea or lesson.

---

## Shot Workflow

Shot 01 is the only shot that starts from a newly created Take Shot.

Every following shot continues from the previous shot.

Never create a new Take Shot for Shot 02, Shot 03 or Shot 04.

---

## Reference Frame Rule

Do not automatically use the final frame of the previous video.

Instead, choose the frame that creates the smoothest visual continuity for the next shot.

The best continuity frame may occur before the last frame.

Always prioritize continuity over choosing the most beautiful frame.

---

## Reference Images

Each new shot uses:

- Previous shot continuity frame
- Required character references
- Existing world

Never recreate the world from scratch.

---

## Prompt Rules

Production documents are written for humans.

Visual Prompts are written for AI.

Visual Prompts should describe only visible actions.

Do not describe spoken dialogue inside the Visual Prompt.

Dialogue belongs only inside the Dialogue section.

---

## Camera Rules

Shot 01 establishes the camera.

Subsequent shots continue naturally from the previous framing.

Avoid dramatic camera changes.

Camera movement should remain slow, calm and cinematic.

---

## Continuity Rules

Maintain:

- character appearance
- environment
- lighting
- proportions
- camera composition

Never redesign existing environments.

---

## Production Philosophy

Complete the episode before improving the pipeline.

Do not redesign the production system during an active episode.

Review the finished episode first.

Improve the pipeline only after the episode is complete.

---

## Long-term Roadmap

**Phase 1**

Create several 1-minute episodes.

Focus on production quality and workflow consistency.

**Phase 2**

Move to approximately 2-minute episodes using the same production pipeline.

Expand storytelling without changing the core workflow.

The pipeline should scale naturally from 1-minute episodes to longer stories.

---

## Cinematic Language

Pompom Hills'in sinema dili. Her sahne, her shot, her hareket bu kurallara uyar.

### Core Principles

```
Every scene should breathe.

Motion is meaningful.

Stillness is meaningful.

Silence is meaningful.

Camera follows emotion.

Never move the camera simply because movement is possible.

Characters should appear alive even when not speaking.

The audience should feel invited into the world rather than entertained by constant stimulation.
```

### Visual Rhythm Rule

Her shot aynı uzunlukta (15 saniye) olabilir, ama hareket miktarı değişir:

```
Shot 1: Çok az hareket (sahneyi keşfet)
    ↓
Shot 2: Biraz daha hareket (etkileşim başlar)
    ↓
Shot 3: En fazla hareket (ana an)
    ↓
Shot 4: Tekrar sakinleşir (kapanış)
```

**Örnek (S01E14):**
- Shot 01: Yıldızlar parlar, yapraklar sallanır, Luca sessizce bakar — çok az hareket
- Shot 02: Luca sorar, Opa düşünür — biraz daha hareket
- Shot 03: Opa anlatır, Luca'nın gözleri kapanır — en fazla hareket (duygusal doruk)
- Shot 04: Luca uykuya dalar, her şey sakinleşir — tekrar sakin

### Eye Line Rule

Karakterlerin bakış yönü shot'lar arasında mantıklı devam etmeli:

```
Shot 1: Luca yukarı bakıyor (yıldızlara)
    ↓
Shot 2: Luca Opa'ya bakıyor (soru soruyor)
    ↓
Shot 3: Luca yukarı bakıyor (cevabı dinliyor)
    ↓
Shot 4: Luca aşağı bakıyor (gözleri kapanıyor)
```

**Kural:** Her shot'ta bakış yönü bir sonraki shot'la tutarlı olmalı. OpenArt bazen bakışları değiştirir — bu yüzden her shot'ta bakış yönü açıkça tanımlanmalı.

### Breathing Rule

Karakterler "yaşıyor" olmalı — sadece aksiyon yaparken değil, beklerken de:

```
Opa konuşmadan önce: küçük nefes
Luca cevap vermeden önce: küçük blink
Soru sormadan önce: hafif baş eğme
Cevap aldıktan sonra: hafif gülümseme
```

**Kural:** Her diyalog öncesi ve sonrasında doğal "nefes" anları olmalı. Bu, karakterleri canlı hissettirir.

### Idle Animation Rule

Karakterler hiçbir zaman tamamen hareketsiz olmamalı:

```
Stars twinkle (sürekli)
Leaves move (sürekli)
Tüyler/kıllar çok hafif hareket eder
Kıyafet çok hafif sallanır
Göz kırpma doğal olur (3-5 sn aralıkla)
Nefes alma görünür (göğüs/hareket)
```

**Kural:** "Idle" durumunda bile character'laralive olmalı. Hareket minimal ama sürekli olmalı.

---

## Lighting Continuity

Lighting Identity, sahne sürekliliğinin bir parçasıdır.

Continuity reference image kullanırken, AI aydınlatmayı aynen korumalıdır.

### Lighting Identity

```
- Warm morning sunlight
- Soft ambient preschool lighting
- Gentle shadows
- Natural bounce lighting
- No dramatic contrast
```

### Kurallar

```
Do not reinterpret the lighting.

Do not brighten the scene.

Do not darken the scene.

The continuity reference image is also the lighting reference.
```

### Production Rule

Her shot'ta aydınlatma bir önceki shot'ın reference frame'iyle birebir aynı olmalıdır. Farklı aydınlatma = red.

---

## Colour Continuity

Colour Identity, Lighting Identity kadar kritik bir production lock'tur.

Continuity frame'den establish edilen renk paletini ve grading'i koru.

### Match

```
- identical white balance
- identical warmth
- identical exposure
- identical saturation
- identical pastel palette
- identical contrast
```

### Avoid

```
- blue tint
- green tint
- orange tint
- HDR look
- cinematic LUT
- warmer or cooler reinterpretation
```

### Kurallar

```
Match the colour grading of the previous shot.

Avoid any colour shift.

Do not introduce cinematic grading.

The continuity reference image is also the colour reference.

The entire episode must appear colour graded as one continuous film.
```

### Production Rule

Ardışık shot'lar arasında renk tonu değişmemelidir. Farklı renk grading'i = red.

---

## Voice Continuity

Karakter sesi her speaking shot'ta aynı kalmalıdır.

Her Shot Specification'da diyalog varsa ayrı bir Voice Continuity bölümü olmalıdır:

```
## Voice Continuity

For Shot 01, match the approved character Voice ID or voice reference.

For Shot 02+, match the previous speaking shot.

The speaking voice MUST remain identical to the previous shot.

Maintain:

- same voice identity
- same pitch
- same timbre
- same speaking speed
- same emotional warmth
- same preschool narration style

Do not generate a different narrator or alternate voice.
```

Eğer kullanılan sistem Voice Reference veya Voice ID destekliyorsa, aynı karakter için her sahnede aynı Voice ID kullanılmalıdır. Desteklemiyorsa, ses değişimi model sınırlaması olarak QA'da işaretlenmelidir.

### Production Rule

Aynı karakterin sesi shot'lar arasında değişmemelidir. Farklı ses kimliği = red.

---

## Dialogue Continuity

Shot dokümanları içindeki diyalog çelişkilerini önler.

### Core Rule

Bir shot dokümanı asla çelişkili diyalog talimatları içermemelidir.

Eğer bir shot diyalog içeriyorsa, doküman şu bilgileri net bir şekilde tanımlamalıdır:

- Kesin diyalog cümlesi
- Kim söylüyor
- Ne zaman söyleniyor
- Ne önce olur
- Ne sonra olur

Eğer bir shot sessizse, doküman şu ifadeyi eklemelidir:

```
This shot has no dialogue.
```

Ancak shot'ın başka bir yerinde diyalog satırları içermemelidir.

### Kurallar

```
Bir shot dokümanı asla çelişkili diyalog talimatları içermemelidir.

Eğer shot diyalog içeriyorsa:
- Kesin diyalog cümlesi tanımlanmalı
- Kim söylüyor belirtilmeli
- Ne zaman söyleniyor belirtilmeli
- Ne önce olur belirtilmeli
- Ne sonra olur belirtilmeli

Eğer shot sessizse:
- "This shot has no dialogue." ifadesi eklenmeli
- Shot'ın başka yerinde diyalog satırı olmamalı
```

### Yanlış Örnek

```
Önceki shot:
"Come on! Let me show you inside!"

Sonraki shot:
"Come on! Let me show you inside!"
```

### Doğru Örnek

```
Önceki shot:
"See you soon!"

Sonraki shot:
"Oh! I almost forgot! Come on... let me show you inside!"
```

---

## Continuation Dialogue Rule

Devam shot'larında diyalog sürekliliği.

### Kurallar

```
Bir shot önceki shot'tan devam ediyorsa:

- Daha önce olan diyalogu tekrarlama
- Önceki shot'ın son satırını tekrarlama (kasıtlı olarak senaryolaştırılmadıkça)
- Yalnızca net bir duygusal veya hikaye beat'i oluşturuyorsa yeni diyalog kullan
- Devam diyalogu neden sahnenin devam ettiğini açıklamalı
```

### Yanlış Örnek

```
Önceki shot:
"Come on! Let me show you inside!"

Sonraki shot:
"Come on! Let me show you inside!"
```

### Doğru Örnek

```
Önceki shot:
"See you soon!"

Sonraki shot:
"Oh! I almost forgot! Come on... let me show you inside!"
```

---

## Shot Duration Feasibility Rule

Shot dokümanlarının çok az sürede çok fazla aksiyon, diyalog, kamera hareketi ve dünya geçişi istemesini önler.

### Core Rule

Her shot süresi, içerdiği aksiyon miktarı için gerçekçi olmalıdır.

Onaylamadan önce, istenen süre içinde şunların sığabileceğini değerlendirin:

- Diyalog satırları
- Karakter duraklaması
- Yüz ifadesi
- Hareket
- Yürüyüş
- Kapı açma
- Girme veya çıkma
- Kamera hareketi
- Dünya geçişi
- Duygusal an

### Minimum Süre Rehberi

| Aksiyon Tipi | Minimum Süre |
|--------------|--------------|
| Basit tepke veya hareket | 2-4 saniye |
| Kısa diyalog + basit aksiyon | 4-6 saniye |
| İki diyalog satırı + tepki | 6-8 saniye |
| Diyalog + yürüyüş + nesne etkileşimi | 8-10 saniye |
| Kapı açma / girme / çıkma geçişi | minimum 8 saniye |
| Diyalog + kapı açma + yeni alana girme | minimum 10 saniye |
| Dışarıdan içeriye geçiş | minimum 10-12 saniye |

### Kurallar

```
Eğer bir shot hem diyalog hem gezinme içeriyorsa, 8 saniyeden kısa olmamalıdır.

Eğer bir shot diyalog, kapı etkileşimi ve yeni alana girme içeriyorsa, 10 saniyeden kısa olmamalıdır.

Eğer bir shot aşırı yüklü hissediliyorsa, iki shot'a bölün.
```

### Shot Document Checklist

Her shot dokümanına şu maddeyi ekleyin:

```
- [ ] Shot süresi, diyalog, aksiyon, kamera hareketi ve geçiş için gerçekçi mi?
```

### Neden Önemli

AI video üretimi, aşırı yüklü shot'larda:
- Aksiyonları atlayabilir
- Diyalogları görmezden gelebilir
- Geçişleri aceleye getirebilir
- Sahneyi yeniden başlatabilir

Bu kural, shot'ların gerçekçi olmasını sağlar.

---

## Reference Frame Selection

Bir shot'ın son karesi otomatik olarak bir sonraki shot için en iyi referans karesi **değildir**.

### Core Rule

```
The final frame of a rendered shot is NOT automatically the best reference frame for the next shot.

The production workflow should always choose the frame that best supports:
- character continuity
- pose continuity
- eye direction continuity
- camera continuity
- composition continuity
- emotional continuity

The selected frame may occur before the final frame.
```

### Production Workflow

```
1. Shot'ı render et
2. Tüm kareleri incele
3. En iyi continuity referans karesini seç (son kare OLMAYABİLİR)
4. Seçilen kareyi bir sonraki shot'ın başlangıç karesi olarak kullan
5. Sürekliliği doğrula
```

### Selection Criteria

| Kriter | Açıklama |
|--------|----------|
| **Character continuity** | Karakter pozisyonu bir sonraki shot'la uyumlu mu? |
| **Pose continuity** | Karakter pozu doğal bir geçiş sağlıyor mu? |
| **Eye direction continuity** | Bakış yönü mantıklı mı? |
| **Camera continuity** | Kamera açısı uyumlu mu? |
| **Composition continuity** | Kompozisyon dengeli mi? |
| **Emotional continuity** | Duygu tonu korunuyor mu? |

### Production Lesson (Episode 1)

Episode 1, son kareyi otomatik kullanmanın zaman zaman görsel sıçramalara yol açtığını göstermiştir.

**Ders:** Kasıtlı continuity frame seçimi, otomatik son kare kullanımından çok daha akıcı geçişler üretir.

Bu artık tüm gelecek bölümler için üretim standardıdır.

### Example

```
Shot 01: Luca yukarı bakıyor, yıldızlar parlıyor
    ↓
Son kare: Luca gözlerini kapatıyor (uyukluyor)
    ↓
AMA en iyi continuity karesi: 3. saniye — Luca henüz yukarı bakıyor
    ↓
Shot 02: Luca yukarı bakarak devam ediyor (akıcı geçiş)
```

---

## Known OpenArt Failure Modes

Aşağıdaki yaygın hatalara karşı korun. İlgili her yerde prompt'ları bu hataları açıkça
önleyecek şekilde güçlendir.

| # | Failure Mode | Koruma |
|---|---|---|
| 1 | Oversized characters | Ölçeği kilitle, %10–12 frame oranını belirt |
| 2 | Tiny environments | Environment = visual hero, wide shot |
| 3 | Regenerated architecture | "DO NOT redesign", environment LOCKED |
| 4 | Different trees | Ağaç şekli/rengi kilitli, redesign yasak |
| 5 | Different flower layouts | Çiçek yerleşimi kilitli, insert-only |
| 6 | Different lighting | `{lighting}` sabit, warm diffused daylight |
| 7 | Brown or reshaped Giant Pompom Tree | Landmark LOCKED: #81C784 taç, şekil sabit |
| 8 | Environment Sheet appearing inside the scene | World reference = clean render only |
| 9 | Random text or sign artifacts | Negative: text, watermark, random signs |
| 10 | Changed world layout | Layout/paths/object placement LOCKED |

Negative prompt blokları için `NEGATIVE_PROMPTS.md` dosyasına bakınız.

---

## Production Document Discipline

- Markdown'lar **production-ready** tutulur.
- Dokümantasyon asla basitleştirilmez (never simplify).
- Bölümler asla birleştirilmez (never merge sections).
- Tablolar asla kaldırılmaz (never remove tables).
- Teknik bilgi asla kaldırılmaz (never remove technical information).
- Version-control dostu formatlama korunur.
- Yalnızca istenen alanlar güncellenir (only update requested fields).

---

## Goal

Nihai doküman, jenerik bir AI prompt gibi değil,
profesyonel bir animasyon stüdyosu production dokümanı gibi okunmalıdır.

---

*Bu belge Pompom Hills production pipeline'ının tek kaynaktır.*
*Son güncelleme: 2 Temmuz 2026*
