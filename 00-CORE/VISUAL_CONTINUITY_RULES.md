# Visual Continuity Rules

---

> *Bu belge tüm görsel süreklilik kurallarını tek çatıda toplar.*
> *Her shot artık "Apply all Pompom Hills Visual Continuity Rules" diyebilir.*

---

## Usage

Her shot dokümanında şu ifadeyi kullanın:

```
Apply all Pompom Hills Visual Continuity Rules.
```

Bu, tüm alt kuralları otomatik olarak uygular.

---

## 1. Colour Identity Rule

Her shot, aynı renk kimliğini korumalıdır.

Colour Identity, World Identity kadar önemlidir.

Amaç yalnızca benzer görünmek değildir. Amaç, tüm bölümün tek bir sürekli film gibi aynı colour grade ile görünmesidir.

### Default Colour Profile

```
- Warm morning lighting
- Soft pastel colour palette
- Gentle golden sunlight
- Medium-low contrast
- Slightly warm white balance
- Soft shadows
- Matte handcrafted materials
- Natural colour saturation
- Calm preschool atmosphere
```

### Continuity Requirements

```
Her shot korumalıdır:
- identical white balance
- identical exposure
- identical colour temperature
- identical saturation
- identical contrast
- identical brightness
- identical pastel palette
- matte handcrafted finish
```

### Avoid

```
- cool shift
- warm shift
- green tint
- magenta tint
- orange grading
- HDR look
- cinematic LUT
```

### Production Rules

```
Match the colour grading of the previous shot.

Avoid any colour shift: no cool shift, warm shift, green tint, magenta tint, orange grading, HDR look or cinematic LUT.

Do not introduce cinematic grading.

The continuity reference image is also the colour reference.

The entire episode must appear colour graded as one continuous film.
```

### Exceptions

Renk değişikliğine yalnızca hikaye tarafından açıkça gerek duyulduğunda izin verilir:

- Gün batımı
- Akşam
- Yağmurlu gün
- Karlı gün
- Rüya sırası
- Büyüsel an
- Mevsimsel değişiklik

Aksi takdirde, belirlenmiş renk profili değişmeden kalır.

---

## 2. Lighting Identity Rule

Her shot, önceki shot'ın aydınlatmasını birebir korumalıdır.

Lighting Identity ve Colour Identity ayrı kilitlerdir. Lighting ışığın davranışını korur; Colour Identity grade, palette ve white balance'ı korur.

### Default Lighting Identity

```
- identical light direction
- identical light intensity
- identical shadow softness
- identical ambient lighting
- identical highlight behaviour
- identical cloud brightness
- identical grass brightness
```

### Match

```
- light direction
- light intensity
- shadow softness
- ambient lighting
- highlight behaviour
- cloud brightness
- grass brightness
- exposure
- brightness
- colour temperature
- lantern brightness
- night sky colour
- contrast
```

### Kurallar

```
Do not reinterpret the lighting.

Do not brighten the scene.

Do not darken the scene.

The continuity reference image is also the lighting reference.
```

---

## 3. Camera Continuity Rule

Kamera mesafesi, açısı ve hareketi shot'lar arasında tutarlı olmalıdır.

### Kurallar

```
- Camera distance must be preserved
- No close-ups unless absolutely required
- No dramatic push-in or pull-back
- Pull-back must stay inside the existing scene
- No new establishing shots
- Camera movement must remain slow and natural
```

---

## 4. Scale Continuity Rule

Karakter ve nesne ölçekleri shot'lar arasında tutarlı olmalıdır.

### Kurallar

```
- Characters occupy 6-8% of the frame
- Environment occupies 92-94% of the frame
- No oversized characters
- Proportions must match previous shot
- Reference scale: Kiko = 100 units
```

---

## 5. Character Continuity Rule

Karakter görünümü ve davranışı shot'lar arasında tutarlı olmalıdır.

### Kurallar

```
- Character appearance never changes
- Character position continues naturally
- Characters already present are NOT reintroduced
- Character scale remains consistent
- Character personality remains consistent
```

---

## 6. World Continuity Rule

Mekan shot'lar arasında tutarlı olmalıdır.

### Kurallar

```
- World is LOCKED — never regenerate or redesign
- Preserve proportions, silhouettes, landmarks
- No new establishing shots
- Environment feels like the same place
- Do not reveal new parts of the world unexpectedly
- If the world has sub-zones (e.g. Flower Hill — Nature Field Zone / Home
  Cluster Zone), the zone stays fixed for the duration of a scene unless a
  transition shot explicitly moves between zones
```

---

## 7. Frame Continuity Rule

Her continuation shot, bir önceki shot'ın reference frame'inden devam etmelidir.

### Kurallar

```
- Use the approved continuity reference frame
- Treat @image1 as the complete visual master reference
- The first visible frame must be visually indistinguishable from @image1
- Not similar. Not close. Identical.
- Treat @image1 as frame zero
- Only after the first frame matches perfectly may animation begin
- Do not reinterpret the starting frame
- Match: framing, camera distance, character positions, colour identity, lighting identity, exposure, white balance, atmosphere, world proportions, character proportions and character performance
- The viewer must not perceive a shot boundary
```

### Master Reference Paragraph

Every continuation shot prompt should include:

```text
Treat @image1 as the complete visual master reference.
Preserve not only framing, but also colour identity, lighting identity, exposure, white balance, atmosphere, environment identity, character proportions, and character performance.
The viewer must not perceive a shot boundary.

The first visible frame must be visually indistinguishable from @image1.
Not similar. Not close. Identical.

Only after the first frame matches perfectly may animation begin.
```

---

## QA Checklist

Her shot için:

```
- [ ] First visible frame is visually indistinguishable from @image1
- [ ] Colour grading matches the previous shot
- [ ] White balance remains consistent
- [ ] Warmth remains consistent
- [ ] Colour temperature remains consistent
- [ ] Brightness remains consistent
- [ ] Lighting mood remains consistent
- [ ] Light direction remains consistent
- [ ] Light intensity remains consistent
- [ ] Shadow softness remains consistent
- [ ] Ambient lighting remains consistent
- [ ] Highlight behaviour remains consistent
- [ ] Exposure matches neighbouring shots
- [ ] Saturation remains consistent
- [ ] Contrast remains consistent
- [ ] No unexpected colour shift
- [ ] No cool shift, warm shift, green tint, magenta tint, orange grading, HDR look or cinematic LUT
- [ ] Camera distance preserved
- [ ] No close-ups unless necessary
- [ ] Character scale correct (6-8% frame)
- [ ] World proportions preserved
- [ ] No environment redesign
- [ ] Continuity frame used correctly
- [ ] Environment feels like the same place
```

---

*Bu belge tüm görsel süreklilik kuralları için tek kaynaktır.*
*Her shot bu kurallara uymalıdır.*
*Son güncelleme: 3 Temmuz 2026*
