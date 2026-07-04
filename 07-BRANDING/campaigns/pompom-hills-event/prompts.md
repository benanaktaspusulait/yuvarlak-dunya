# Pompom Hills Family Fun — Event Campaign Prompts

> Facebook/Instagram için "Event / Weekend Fun" tarzı kampanya görselleri.
> Bu dosya bir pazarlama/kampanya asset paketidir — production canon (karakter, dünya, senaryo) değildir.
> Karakter ve dünya kilitleri için tek kaynak: `01-CHARACTERS/`, `00-CORE/WORLD_BIBLE.md`, `07-BRANDING/COLOR_PALETTE_LOCK.md`.
> Prompt kuralları için tek kaynak: `CONTRIBUTING.md` § Prompt Ekleme Kuralları.

---

## Text Safety İstisnası — Neden Bu Görsellerde Yazı Var

`00-CORE/17_VIDEO_GENERATION_STANDARD.md` § Text Safety kuralı **video master render'ları** için
"no on-screen text" der. Bu kampanya görselleri video değil, statik Facebook/Instagram
poster/story/reel-cover asseti olduğu için `CONTRIBUTING.md` § Prompt Ekleme Kuralları madde 6'daki
istisna geçerlidir:

> "Görselde yazı sadece moodboard, poster veya palette card gibi özellikle belirtilen assetlerde kullanılabilir."

Yani bu 5 sahnede okunabilir metin (başlık, CTA) **kasıtlı ve onaylı** bir kullanımdır. Bölüm
video'larına veya karakter intro'larına bu kural uygulanmaz — oralarda text safety kuralı
değişmeden geçerlidir.

---

## Ortak Taban Prompt (Base Prompt)

Her 5 sahne bu taban üzerine kurulur. Sahneye özel kısım her scene bloğunda ayrıca verilir.

```text
Create a cheerful 3D cartoon-style promotional scene for a children's family event at Pompom Hills.
Soft pastel colours, rounded shapes, warm lighting, playful magical hills, pompom trees, little
forest elements, friendly child characters, safe and happy atmosphere. The image should feel like
an invitation for families and children to visit. Facebook/Instagram friendly composition, bright
but not too busy, clear space reserved for text, high-quality children's animation style, no
realistic textures, no dark shadows. {style} {camera} {lighting}
```

Değişkenler (`00-CORE/VARIABLES.md` ile birebir aynı):

```text
{style} = Pompom Hills v2.1, rounded preschool toy world, pastel colors, matte clay-plush surfaces, toddler-safe emotional clarity
{camera} = stable 50mm preschool camera, eye-level or gentle wide shot, clear readable staging, no Dutch angle, no fisheye, no shaky movement
{lighting} = warm diffused daylight, soft contact shadows under 25 percent opacity, no hard rim light, no black night values
```

**World reference:** Her sahnede Central Square hero view'ı arka plan referansı olarak kullan
(`POMPOM_HILLS_PRODUCTION/02_WORLDS/CENTRAL_SQUARE/01_HERO_VIEW/` veya `environment/01-central-square/hero-view.png`).
Dünyayı yeniden tasarlama — bkz. `00-CORE/NEGATIVE_PROMPTS.md` § OpenArt Production Failure Modes.

**Negative prompt:** Her üretimde `00-CORE/NEGATIVE_PROMPTS.md` § Common Negative Prompt kullan.
Ek olarak bu kampanya için:

```text
no scary characters, no crowded chaotic composition, no unreadable text, no low-contrast text,
no text overlapping character faces, no more than 2 lines of headline text, no generic stock-photo
style, no photorealistic children, no logos other than Pompom Hills
```

---

## Karakter Kilitleri (Bu Kampanyada Kullanılan)

| Karakter | Ölçek | Ana Renkler | Kaynak |
|---|---|---|---|
| Kiko | 100 birim | Coral pink shirt #F8BBD0, white shorts, brown pigtails #8D6E63 | `01-CHARACTERS/01-kiko.md` |
| Mimi | 80 birim | Soft blue fur #90CAF9, yellow shirt #FFF59D, green eyes #66BB6A | `01-CHARACTERS/02-mimi.md` |
| Opa | 120 birim, alçak sahnelenir | Warm green #A5D6A7, gold glasses #FFD54F, brown shawl #A1887F, orange beak #FF7043 | `01-CHARACTERS/03-opa.md` |
| Noah | 100 birim | Blue striped shirt #8EC5F0, curly light brown hair #C48A5A | `01-CHARACTERS/05-noah.md` |

Karakter tasarımı hiçbir sahnede değiştirilmez, yalnızca poz/mesafe/ifade değişir.

---

## Scene 01 — Hero Event Poster

**Klasör:** `01-hero-event-poster/`
**Amaç:** Ana kampanya görseli, Facebook event kapak fotoğrafı / ana Instagram post.
**Format:** 1:1 (Instagram feed) veya 4:5 (Facebook event cover) — ikisi de üretilebilir.

```text
[BASE PROMPT] Wide establishing view of Pompom Hills Central Square, with the Giant Pompom Tree
and colourful dome houses in the background. A small welcoming archway or entrance path in the
foreground. Kiko, Mimi, Noah and Opa stand at a friendly distance, waving toward the camera with
big happy smiles. Characters occupy roughly 15-20% of the frame; the village is the visual hero.
Clear open sky area in the upper third reserved for headline text. 4:5 aspect ratio.
```

**Metin (görsele eklenecek):**

```text
Pompom Hills Family Fun
Come and Play This Weekend!
```

**Negative ek:** `characters too large, characters blocking the village, cluttered sky area`

**Çıktı dosyası:** `01-hero-event-poster/hero-event-poster.png`

---

## Scene 02 — Character Invite

**Klasör:** `02-character-invite/`
**Amaç:** Karakter odaklı davet görseli — Opa veya Kiko doğrudan izleyiciye "davet" eder.
**Format:** 1:1 (Instagram feed post).

```text
[BASE PROMPT] Medium close-up of Opa the owl, warm and welcoming expression, one wing gently
raised as if inviting the viewer, standing in front of a soft-focus Pompom Hills Central Square
background (Giant Pompom Tree visible but blurred). Opa fills about 40% of the frame, matching
thumbnail composition rules. Warm golden-hour-safe daylight, no harsh shadows. Clear space to the
right of Opa for short text.
```

**Alternatif karakter versiyonu (Kiko):** Aynı prompt, Opa yerine Kiko — "curious happy expression,
one hand waving" ile değiştir. İki versiyon da üretilip A/B test edilebilir.

**Metin (görsele eklenecek):**

```text
Come and Play!
```

**Negative ek:** `character face not centered, character too small, busy background competing with face`

**Çıktı dosyası:** `02-character-invite/opa-invite.png` ve/veya `02-character-invite/kiko-invite.png`

---

## Scene 03 — Activity Scene

**Klasör:** `03-activity-scene/`
**Amaç:** Etkinlik/aile atmosferini gösteren aksiyon sahnesi.
**Format:** 1:1 veya 4:5 (Instagram/Facebook feed post).

```text
[BASE PROMPT] Children playing joyfully among the pompom trees at Central Square. Kiko and Noah
play near a small decorated table with a soft picnic cloth, Mimi bounces nearby, a few round
pastel balloons (yellow, coral, soft blue) float gently near the tree. Warm family/community
atmosphere, soft midday light, no crowd — maximum 3-4 characters visible. Balanced composition
with open lower-third space for a caption line.
```

**Metin (görsele eklenecek, opsiyonel — bu sahnede metin az/yok tercih edilir):**

```text
(Bu sahnede metin opsiyoneldir — aksiyon/atmosfer öne çıkmalı. Gerekirse alt köşeye kısa bir
tarih/saat bandı eklenebilir, örn. "Saturday · Central Square".)
```

**Negative ek:** `more than 4 characters, cluttered balloons, table blocking character faces, unsafe balloon strings`

**Çıktı dosyası:** `03-activity-scene/activity-scene.png`

---

## Scene 04 — Story Version

**Klasör:** `04-story-version/`
**Amaç:** Instagram Story için dikey, sade, büyük başlıklı versiyon.
**Format:** 9:16 (Instagram Story / Facebook Story).

```text
[BASE PROMPT] Simplified vertical composition. A single warm view of the Pompom Hills entrance
path with the Giant Pompom Tree in the distance. Kiko waves from the middle-ground. Minimal
background detail compared to other scenes — fewer houses, fewer props — so the large headline
text remains fully readable. Top third and bottom third of the frame kept visually calm for text
safe zones (Instagram Story UI overlaps top ~250px and bottom ~250px). 9:16 aspect ratio.
```

**Metin (görsele eklenecek, büyük puntolu):**

```text
Pompom Hills
Family Fun Day!
Swipe Up / Link in Bio
```

**Negative ek:** `text near top or bottom edge, small unreadable text, busy background behind text, more than 1 character`

**Çıktı dosyası:** `04-story-version/story-version.png`

---

## Scene 05 — Reel Cover

**Klasör:** `05-reel-cover/`
**Amaç:** Instagram Reel kapak görseli — güçlü, tek bakışta anlaşılır.
**Format:** 9:16 (Reel cover, video ile aynı oran).

```text
[BASE PROMPT] Bold vertical cover composition. Kiko's face large and expressive (happy, inviting)
fills the left 55% of the frame, close enough to read clearly as a small thumbnail. Right 45% of
the frame shows a soft-focus colourful glimpse of the Pompom Hills world (tree, houses, sky) — not
sharp detail, just warm colour and shape. Strong contrast between character and background so the
cover reads instantly even at small size. 9:16 aspect ratio.
```

**Metin (görsele eklenecek, kısa ve kalın):**

```text
Family Fun Day!
```

**Negative ek:** `face too small, face off-center, background too sharp and competing with face, more than 3 words of text`

**Çıktı dosyası:** `05-reel-cover/reel-cover.png`

---

## Üretim Sırası Önerisi

1. Scene 01 (Hero) önce üretilir — dünya/kompozisyon onayı burada alınır.
2. Scene 01 onaylandıktan sonra aynı world reference ile Scene 02-05 üretilir (tutarlılık için).
3. Her görsel `07-BRANDING` görsel onay sürecinden geçer (bkz. `CONTRIBUTING.md` § Görsel Onay Süreci):
   Prompt QA → Pedagoji QA → Tasarım QA → Karakter QA → Metadata QA.
4. Onaylanan her görsel prompt + model + seed + negative prompt bilgisiyle birlikte ilgili
   `NN-slug/` klasörüne kaydedilir (örnek: bir `.txt` metadata dosyası görselin yanında).

---

## Metadata / Caption

Bu görseller için Facebook/Instagram caption'ları `00-CORE/30_YOUTUBE_METADATA_STANDARD.md` § 15
(Facebook / Instagram Cross-Promotion) formatına uyar — aynı sıcak, abartısız, "smash like" içermeyen ton.
CTA kuralları için `00-CORE/30_YOUTUBE_METADATA_STANDARD.md` § 14'e bakılır.

---

*Bu dosya Pompom Hills Family Fun event kampanyası görsel promptları için tek kaynaktır.*
*Karakter/dünya canon'una dokunmaz — sadece mevcut kilitli assetleri referans alır.*
