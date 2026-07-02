# VARIABLES — Pompom Hills v2.1

---

## Prompt Değişkenleri

Tüm prompt'larda şu değişkenler kullanılır:

```text
{style} = Pompom Hills v2.1, rounded preschool toy world, pastel colors, matte clay-plush surfaces, toddler-safe emotional clarity
{camera} = stable 50mm preschool camera, eye-level or gentle wide shot, clear readable staging, no Dutch angle, no fisheye, no shaky movement
{lighting} = warm diffused daylight or cozy soft-blue night, soft contact shadows under 25 percent opacity, no hard rim light, no black night values
{background} = transparent PNG or soft pastel gradient #F5F0EB (optional; isolated prop/character assetlerinde kullanılır)
```

> **Tek kaynak:** Yukarıdaki tanımlar kanoniktir ve `README.md` ile birebir aynıdır. Sahne/dünya
> prompt packleri (`05-AI-PROMPTS/ENVIRONMENT_PROMPTS.md`, `05-AI-PROMPTS/SCENE_PROMPTS.md`,
> `05-AI-PROMPTS/ADVANCED_PRODUCTION_PROMPTS.md`) bu tanımları kullanır.
> **Bilinçli istisnalar:** `05-AI-PROMPTS/TECHNICAL_SHEETS.md` (orthographic studio kamera + even studio
> lighting), `03-PROPS/PROP_ASSETS.md` (isolated-object framing) ve `05-AI-PROMPTS/VISUAL_REFERENCES.md`
> (clean reference framing) amaçları gereği farklı `{camera}`/`{lighting}` kullanır.

---

## Renk Paleti

### Gökyüzü

| Durum | Renk | Hex |
|---|---|---|
| Gündüz | Açık Mavi | #BBDEFB |
| Gün batımı | Yumuşak Turuncu | #FFCC80 |
| Gece | Yumuşak Koyu Mavi | #5C6BC0 |

### Doğa

| Öğe | Renk | Hex |
|---|---|---|
| Çimen | Yumuşak Yeşil | #C8E6C9 |
| Ağaç taçı | Sıcak Yeşil | #81C784 |
| Ağaç gövdesi | Sıcak Kahverengi | #A1887F |
| Yol taşları | Yumuşak Gri | #E0E0E0 |

### Gökyüzü Öğeleri

| Öğe | Renk | Hex |
|---|---|---|
| Bulutlar | Beyaz | #FFFFFF |
| Güneş | Sıcak Sarı | #FFF9C4 |
| Ay | Sıcak Krem | #FFF9C4 |

### Karakter Renkleri

| Karakter | Ana Renk | Hex |
|---|---|---|
| Kiko | Mercan Pembe | #F8BBD0 |
| Mimi | Yumuşak Mavi | #90CAF9 |
| Opa | Sıcak Yeşil | #A5D6A7 |

### Ev Renkleri

| Ev | Renk | Hex |
|---|---|---|
| Kiko'nun evi | Mercan Pembe | #F8BBD0 |
| 2. Ev | Yumuşak Mavi | #90CAF9 |
| 3. Ev | Yumuşak Sarı | #FFF59D |
| 4. Ev | Yumuşak Yeşil | #A5D6A7 |
| 5. Ev | Yumuşak Mor | #CE93D8 |
| 6. Ev | Yumuşak Turuncu | #FFCC80 |

---

## Boyut Standartları

| Öğe | Boyut | Not |
|---|---|---|
| Kiko | 1.00 m | Ana ölçek referansı (100 birim) |
| Mimi | 0.80 m | Kiko'nun %80'i (80 birim) |
| Opa | 1.20 m | En uzun karakter; alçak sahnelenir, göz çizgisi 0.82-0.92 m (120 birim) |
| Kapı | 1.35 m | Tüm kapılar |
| Tavan | 2.20 m | İç mekanlar |
| Stepping stone | 0.35 m çap | Tüm taşlar |
| Big Pompom Tree | 5.00-6.00 m | Merkez ağaç |
| Kamera göz seviyesi | 0.70-1.10 m | Karakter göz hizası |

---

## Prompt Şablonları

### Karakter Promptu

```text
[Character name] from Pompom Hills v2.1, [yaş/tip], [renk kodları], [kıyafet], [özelliği], {style}, {camera}, {lighting}, 16:9
```

### Mekan Promptu

```text
[Location name] in Pompom Hills, [detay], [renk kodları], [hava], {style}, {camera}, {lighting}, 16:9
```

### Prop Promptu

```text
[Prop name], [renk] #[hex], [şekil], [malzeme], Pixar-quality stylized 3D preschool illustration, Pompom Hills art style, centered composition, isolated object, transparent background, {style}, {lighting}, 1:1
```

---

## Versiyon Kontrolü

| Değişken | Mevcut Versiyon | Not |
|---|---|---|
| {style} | v2.1 | Stil tanımı |
| {camera} | v2.1 | Kamera kuralları |
| {lighting} | v2.1 | Işık kuralları |
| {background} | v2.1 | Arka plan |

**Versiyon güncellendiğinde bu dosya güncellenmeli ve tüm prompt'lar kontrol edilmelidir.**

---

## Negatif Promptlar

```text
no sharp edges, no dark shadows, no realistic textures, no complex backgrounds, no scary elements, no harsh lighting, no neon colors, no busy compositions, no characters (unless specified), no text, no watermarks
```

---

*Bu belge tüm prompt değişkenleri için merkezi referanstır.*
