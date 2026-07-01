# MASTER PROMPTS — PomPom Hills v2.1

---

## Production Pipeline (OKU — Zorunlu)

Pompom Hills bir **production pipeline** olarak inşa edilmiştir. OpenArt bir image generator
değil, bizim **production engine**'imizdir. İzole prompt yazılmaz; her prompt bu pipeline'ı
takip eder. **Consistency > beauty. Production quality > speed.**

Tam kural seti: `PRODUCTION_RULES.md`. Bu doküman o kuralların prompt-uygulama katmanıdır.

**Pipeline özeti:**

```
1. World Build      → WORLD_BUILD_DESCRIPTION.md (dünya kanonik tanımı)
2. World Reference  → Her mekan için bağımsız World + Hero Pack (clean render)
3. IMAGE PROMPT     → Environment görselini üret (yalnızca ilk kez)
4. DIRECTOR PROMPT  → LOCKED dünyanın içine yalnızca karakter yerleştir
5. Scene Visual     → OpenArt'a doğrudan yapıştır
```

**Kilit kurallar (LOCKED):**
- Environment LOCKED — asla yeniden üretme/yeniden tasarlama; yalnızca karakter yerleştir.
- Character appearance LOCKED — saç, göz, yüz, vücut, kıyafet, renk, ölçek her sahnede aynı.
- Giant Pompom Tree LOCKED — şekil, konum (Central Square merkezi), ölçek, renk (#81C784) sabit.

---

## World Reference & Hero Pack Kuralları

- **Environment Sheet'leri asla World reference olarak kullanma.**
- World reference **yalnızca temiz render** içerir: başlık yok, etiket yok, ok yok, layout yok, çerçeve yok.
- **Her mekanın kendi bağımsız World'ü vardır.**
- Her World'ün bir **Hero Pack**'i vardır:

| View | Kullanım |
|---|---|
| Hero View | İkonik ana kompozisyon (reference plate) |
| Right View | Sağ profil tutarlılığı |
| Back View | Arka görünüm tutarlılığı |
| Top View | Layout/konum doğrulaması |

- Sahne üretiminde world'ler **asla yeniden üretilmez** — yalnızca karakter insert edilir.
- Prompt'ta environment'ın LOCKED olduğunu açıkça belirt; mimari, ağaç, çiçek, yol, bank,
  lamba direği ve landmark yeniden tasarımını açıkça yasakla.

---

## Workflow

```
1. IMAGE PROMPT → Dünya (environment) görseli üret
2. DIRECTOR PROMPT → O dünyanın içinde sahneleri çek
3. Scene dosyasındaki Visual Prompt → OpenArt'a doğrudan yapıştır
```

---

## 1. IMAGE PROMPT (Hero / Reference Image)

**Kullanım:** OpenArt'ta Image üretirken.

**Şablon:**

```text
{LOCATION}, Pompom Hills, magical preschool village, {KEY_FEATURE}, {DETAILS}, {BACKGROUND_ELEMENTS}, {SKY}, {LIGHTING}, {ATMOSPHERE}, cinematic composition, environment is the hero, extremely detailed stylized 3D animation, Pixar-quality, clean composition, highly consistent world design, vibrant preschool colors, rounded friendly shapes, 16:9
```

---

## 2. DIRECTOR / SHOT PROMPT (Sahne Üretimi — Yeni Standart)

**Kullanım:** Runway Director'da "Describe your scene..." kısmına yapıştır.

**Bu format tüm sahneler için kalıcı standarttır.**

```text
{CHARACTER}, {CHARACTER_DESCRIPTION}, is introducing himself/herself in {ENVIRONMENT}, Pompom Hills.

STYLE
High-end stylized 3D preschool animation, Pixar-quality, soft rounded shapes, colorful magical village, cinematic composition, ultra clean render, consistent production design, realistic scale, child-friendly, highly detailed but simple enough for preschool audiences.

CHARACTER
{CHARACTER} is exactly the same as the reference character sheet.
- {KEY_FEATURE_1}
- {KEY_FEATURE_2}
- {KEY_FEATURE_3}
- {OUTFIT}
- {EXPRESSION}
- Age {AGE}.
- Small preschool proportions.

ACTION
{DETAILED_ACTION_DESCRIPTION}

ENVIRONMENT
Use the existing {ENVIRONMENT} Pompom Hills world exactly as provided in the world reference.
DO NOT redesign the environment.

The environment is the visual hero.

Include:
• {WORLD_ELEMENT_1}
• {WORLD_ELEMENT_2}
• {WORLD_ELEMENT_3}
• {WORLD_ELEMENT_4}
• {WORLD_ELEMENT_5}

Maintain exactly the same layout, paths, object placement and proportions from the world reference.

SCALE
This is extremely important.

{CHARACTER} must look like a normal preschool child inside a large magical village.

{CHARACTER} occupies approximately {PERCENTAGE}% of the frame.

Objects must all appear correctly scaled relative to {CHARACTER}.

The world should feel large and explorable.

Never make {CHARACTER} oversized.

CAMERA

{CAMERA_SHOT}

{LENS}

Eye level

Camera height {HEIGHT}

Leave generous negative space around {CHARACTER}.

Show a large portion of {ENVIRONMENT}.

The viewer should immediately understand the world before focusing on {CHARACTER}.

LIGHTING

{LIGHTING_DESCRIPTION}

ATMOSPHERE

{EMOTION_1}

{EMOTION_2}

{EMOTION_3}

ANIMATION

{ANIMATION_RULES}

CONSISTENCY

Keep {CHARACTER} identical to the reference character.

Keep {ENVIRONMENT} identical to the world reference.

Do not change architecture.

Do not invent new landmarks.

Do not replace signs.

Do not change house styles.

Maintain production consistency with previous scenes.

NEGATIVE

{NEGATIVE_LIST}

16:9
```

---

## 3. Örnek: Noah — Central Square

```text
Noah, a cheerful and creative 4-year-old preschool boy, is introducing himself in Central Square, Pompom Hills.

STYLE
High-end stylized 3D preschool animation, Pixar-quality, soft rounded shapes, colorful magical village, cinematic composition, ultra clean render, consistent production design, realistic scale, child-friendly, highly detailed but simple enough for preschool audiences.

CHARACTER
Noah is exactly the same as the reference character sheet.
- Curly light brown hair (#C48A5A)
- Big warm brown eyes (#7A4A2A)
- Soft freckles across his nose (#E7869A)
- Blue striped t-shirt (#8EC5F0) with denim pocket (#4C7DBA)
- Khaki shorts (#D2B48C)
- Blue sneakers (#3D7DBB)
- Happy, creative expression.
- Age 4.
- Small preschool proportions.

ACTION
Noah sits naturally on the colorful stepping stones in the middle of Central Square.
He is happily stacking rounded colorful wooden building blocks.
Some blocks gently fall over.
He smiles, laughs softly, then continues building with excitement.
His body language feels playful, curious and creative.

ENVIRONMENT
Use the existing Central Square Pompom Hills world exactly as provided in the world reference.
DO NOT redesign the environment.

The environment is the visual hero.

Include:
• Giant pompom tree in the center
• Circular flower bed
• Colorful stepping stones
• Wooden benches
• Warm street lamps
• Rolling green hills
• Pastel dome houses
• Flower gardens
• Soft rainbow in the distance
• Blue sky with soft white clouds

Maintain exactly the same layout, paths, object placement and proportions from the world reference.

SCALE
This is extremely important.

Noah must look like a normal preschool child inside a large magical village.

Noah occupies approximately 18–20% of the frame.

Benches, lamp posts, flowers, stepping stones, houses and the giant tree must all appear correctly scaled relative to Noah.

The world should feel large and explorable.

Never make Noah oversized.

CAMERA

Wide medium shot

35mm lens

Eye level

Camera height 0.8 meters

Leave generous negative space around Noah.

Show a large portion of Central Square.

The viewer should immediately understand the world before focusing on Noah.

LIGHTING

Warm morning sunlight

Soft cinematic shadows

Bright saturated preschool colors

Soft global illumination

Natural sky light

ATMOSPHERE

Joyful

Creative

Safe

Magical

Peaceful

Wonder-filled

ANIMATION

Gentle idle movement

Small head movement

Natural blinking

Soft breathing

Hair lightly bounces

Blocks move with soft rounded physics

No sudden movement

No exaggerated squash/stretch

CONSISTENCY

Keep Noah identical to the reference character.

Keep Central Square identical to the world reference.

Do not change architecture.

Do not invent new landmarks.

Do not replace signs.

Do not change house styles.

Maintain production consistency with previous scenes.

NEGATIVE

Oversized child

Tiny environment

Different hairstyle

Different clothes

Different colors

Different architecture

Different village layout

Extra characters

Photorealism

Dark lighting

Scary atmosphere

Sharp edges

Realistic human anatomy

Text artifacts

Random signs

Watermarks

16:9
```

---

## 4. Hızlı Referans

### Camera Shot Seçenekleri

| Shot | Kullanım |
|---|---|
| Wide shot | Mekan tanıtımı |
| Medium wide shot | Karakter + mekan |
| Medium shot | Karakter etkileşimi |
| Medium close-up | Yüz ifadesi |
| Close-up | Detay |
| Low angle | Güçlü his |
| High angle | Genel görünüm |
| Eye level | Normal (en sık) |

### Camera Height Seçenekleri

| Yükseklik | Kullanım |
|---|---|
| 0.60 m | Küçük karakter |
| 0.70 m | Mimi seviyesi |
| 0.80 m | Kiko/Noah seviyesi (default) |
| 0.90 m | Opa seviyesi |
| 1.00 m | Yüksek açı |

### Character Percentage Seçenekleri

| Karakter | Frame Oranı |
|---|---|
| Kiko | 20-25% |
| Mimi | 15-20% |
| Opa | 18-22% |
| Noah | 18-20% |
| Arda | 18-20% |

> **Production scale kuralı:** Standart production sahnelerinde environment visual hero'dur ve
> karakter yaklaşık **%10–12** yer kaplar (bkz. `PRODUCTION_RULES.md` §4). Yukarıdaki %15–25
> aralığı yalnızca bilinçli **karakter tanıtım (intro)** sahneleri içindir. Asla oversized
> karakter üretme.

### OpenArt Failure Modes — Hızlı Koruma

Her Director prompt'unda aşağıdaki hatalara karşı NEGATIVE bloğunu güçlendir (detay: `PRODUCTION_RULES.md` §5):

| Failure | Prompt'ta önle |
|---|---|
| Oversized character | Ölçeği kilitle, %10–12 belirt |
| Tiny environment | Environment = hero, wide shot |
| Regenerated architecture / different trees | "DO NOT redesign", environment LOCKED |
| Different flower layout / world layout | Layout + object placement LOCKED |
| Brown or reshaped Giant Pompom Tree | Landmark LOCKED, taç #81C784 |
| Environment Sheet in scene | World reference = clean render only |
| Random text / sign artifacts | Negative: text, watermark, random signs |

---

## 5. Kullanım Sırası

### Adım 1: Image Prompt ile environment üret

```
[IMAGE_PROMPT şablonunu doldur]
→ OpenArt'a ver
→ Görsel üret
→ environment/ klasörüne kaydet
```

### Adım 2: Director Prompt ile sahne çek

```
[DIRECTOR_PROMPT şablonunu doldur]
→ Runway Director'a ver
→ Üretilen environment görselini reference olarak ekle
→ Sahneyi çek
→ videos/ klasörüne kaydet
```

### Adım 3: Tekrarla

Her karakter ve mekan için aynı işlemi tekrarla.

---

## 6. Kalıcı Standart

Bundan sonra her sahne dosyasında **Visual Prompt** bölümü bu formatta olmalıdır:

```
STYLE → CHARACTER → ACTION → ENVIRONMENT → SCALE → CAMERA → LIGHTING → ATMOSPHERE → ANIMATION → CONSISTENCY → NEGATIVE
```

Bu, PomPom Hills'in görsel tutarlılığının garantisidir.

---

*Bu belge PomPom Hills görsel üretim workflow'unun temelidir.*
*Son güncelleme: 2026-07-01*
