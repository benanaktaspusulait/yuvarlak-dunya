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
Match the episode's approved clean colour master and canonical World references.

Avoid any colour shift: no cool shift, warm shift, green tint, magenta tint, orange grading, HDR look or cinematic LUT.

Do not introduce cinematic grading.

The approved clean colour master is the colour reference. A generated video frame is not
a colour or production-anchor reference.

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

## 7. Clean Anchor and Editorial Continuity Rule

Her shot ayrı onaylanmış clean start-frame still ile başlamalıdır. Video çıktısından
çıkarılmış hiçbir frame production anchor olarak kullanılamaz. Ayrıntılı ve öncelikli kural
`00-CORE/17_VIDEO_GENERATION_STANDARD.md` içindeki **SHOT COMPLETION AND QUALITY RESET
RULE** bölümüdür.

### Kurallar

```
- Use the approved clean start-frame still created from canonical references
- Treat @image1 as the complete visual master reference
- The first visible frame must be visually indistinguishable from @image1
- Not similar. Not close. Identical.
- Treat @image1 as frame zero
- Only after the first frame matches perfectly may animation begin
- Do not reinterpret the starting frame
- Match: framing, camera distance, character positions, colour identity, lighting identity, exposure, white balance, atmosphere, world proportions, character proportions and character performance
- The viewer may perceive a clean editorial cut; story continuity is mandatory, pixel-level
  continuation is not
- Exact clean-anchor linkage is normally limited to 2 consecutive shots and exceptionally
  limited to 3; then perform a mandatory quality reset
- Never use a raw, corrected, normalized, graded or upscaled AI-video frame as @image1
```

### Master Reference Paragraph

Every shot prompt should include:

```text
Treat @image1 as the complete visual master reference.
@image1 is a separately approved clean production still, not a frame extracted from video.
Preserve not only framing, but also colour identity, lighting identity, exposure, white balance, atmosphere, environment identity, character proportions, and character performance.
Preserve story continuity through placement, screen direction, world identity and editing.

The first visible frame must be visually indistinguishable from @image1.
Not similar. Not close. Identical.

Only after the first frame matches perfectly may animation begin.
```

---

## 8. Global OpenArt Continuity Locks

Bu kilitler her video shot için geçerlidir. Bunlar yalnızca shot'lar arası değil, aynı
15 saniyelik klip içindeki sürekliliği de kontrol eder.

### Hard Background Lock

Environment sabit bir fiziksel set gibi davranmalıdır. İlk frame'de görünen ağaçlar,
trunk'lar, bench'ler, planter'lar, bush'lar, flowerbed'ler, path'ler, paving/stepping
stone'lar, grass patch'ler, bunting/flag'ler, house'lar, wall'lar, landmark'lar ve tüm
görünür objeler pozisyon, ölçek, kimlik ve layout korumalıdır.

Bench planter'a, bush tree'ye, flowerbed grass mound'a, path road'a, house shop'a
dönüşemez. Landmark shift, resize, duplicate veya disappear yapamaz.

### Interaction Object Usability Rule

Bir shot bir obje ile yalnızca obje `@image1` içinde görünür ve planlanan aksiyon için
mevcut boyutu, şekli, pozisyonu ve mesafesiyle kullanılabilir durumdaysa etkileşime
girebilir.

Visible is not enough.

Eğer obje çok küçük, çok uzak, kalabalık içinde, kısmen crop edilmiş veya aksiyon için
doğru formda değilse, karakter aksiyonu sadeleştirilir. Obje büyütülmez, çoğaltılmaz,
taşınmaz, yeniden şekillendirilmez, replace edilmez ve spawn edilmez.

Characters adapt to the environment.
The environment does not adapt to the characters.

### Environment Object Lock

`@image1` içinde görünen tüm environment objeleri yerinde kilitlidir.

Trees, flowers, grass patches, hills, stones, doorways, props, sky elements, furniture,
anchors ve landmarks move, grow, shrink, slide, drift, pop in, enter frame, leave frame
veya reposition yapamaz.

Yalnızca karakterler hareket edebilir; bunun istisnası yalnızca shot tarafından açıkça
izin verilen planlı lokasyon geçişleridir.

Kamera bir objeyi daha kullanılabilir yapmak için hareket edemez.
Obje karaktere yaklaşamaz.
Shot mevcut kompozisyonu aynen kullanmalıdır.

### Intra-Shot Character Continuity Lock

Karakter aynı shot içinde kesintisiz fiziksel varlık olarak kalmalıdır. Karakter
kaybolamaz, tekrar beliremez, occlusion sonrası regenerate olamaz, teleport yapamaz,
duplicate olamaz, ani side-switch yapamaz, scale/identity değiştiremez.

Karakter yolu frame-to-frame okunabilir olmalıdır.

### Single Visible Path Rule

Karakterler yalnızca görünür yürünebilir alanlarda hareket eder: clear path, paving
stones, stepping stones, clear open grass patch veya objelerin yanındaki açık alan.

Bush, flowerbed, planter, tree trunk, bench, house, wall, dense grass, foreground plant
veya fiziksel engel olması gereken dekoratif objelerin içinden/arkasından geçemez.

### Occlusion Is Not A Transition

Do not use occlusion as a transition.

Karakterler hareketi devam ettirmek veya resetlemek için bush, flower, bench, tree
trunk, planter, wall, house, flag veya foreground plant arkasında saklanamaz. Tiny
partial overlap yalnızca yarım saniyeden kısa, gövdeyi tamamen kapatmayan ve direction
of travel'ı saklamayan durumlarda kabul edilir.

### Camera Must Not Break Continuity

Kamera sürekliliği korumalıdır. Tiny push-in, tiny settle, very slow stable drift ve
nearly locked-off camera kabul edilir. Camera reset, fast pan, whip pan, orbit, fast
zoom, sudden angle jump, layout değiştiren tracking, background object shift, character
hiding, farklı location reveal veya regenerated environment hissi yasaktır.

### First Second Continuity Hold

Continuity-linked shot'larda ilk 1 saniye `@image1`'e çok yakın kalmalıdır. Camera
angle/height/lens feel, character position/scale, background objects, lighting ve colour
grading değişmemelidir. Yeni obje belirmemeli, obje kaybolmamalı, karakter teleport veya
side-switch yapmamalıdır.

### Character Action Reduction For Stability

Eğer shot background morphing, occlusion veya teleport riski taşıyorsa hareket azaltılır.
Pointing, looking, head turn, tiny step, smiling, gentle reaction, small body turn ve
shared still moment tercih edilir. Set içinde uzun yürüyüş, objelerin arkasından geçme,
enter/exit frame ve foreground object transition kullanılmaz.

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
- [ ] Hard Background Lock passed
- [ ] Intra-Shot Character Continuity Lock passed
- [ ] Single Visible Path Rule passed
- [ ] Occlusion Is Not A Transition passed
- [ ] Camera Must Not Break Continuity passed
- [ ] First Second Continuity Hold passed
- [ ] Object Identity Lock passed
- [ ] Interaction Object Usability Rule passed
- [ ] Environment Object Lock passed
- [ ] Current action object is visible and usable at its existing size/position
- [ ] Character action was simplified instead of moving/resizing/spawning an object
```

---

*Bu belge tüm görsel süreklilik kuralları için tek kaynaktır.*
*Her shot bu kurallara uymalıdır.*
*Son güncelleme: 5 Temmuz 2026*
