# OpenArt Continuity and Motion Rules

> Bu dosya tüm Pompom Hills video üretiminde geçerli global kuralları içerir.
> E05 Shot 01 ve Shot 02 üretim hatalarından çıkarılan kalıcı production standartları.

---

## 1. @image1 Is The Only Visual Continuity Source

OpenArt sadece ekteki referans görselleri bilir (örn. `@image1`). Önceki videoyu, önceki shot'ı veya final frame geçmişini bilmez.

Kurallar:
- `@image1` tam görsel kaynak olarak kullanılmalıdır.
- OpenArt-facing prompt'lar önceki video hafızasına güvenmemelidir.
- İnsan dokümantasyonu önceki shot'lardan bahsedebilir, ama OpenArt'a verilen Visual Prompt `@image1` dili kullanmalıdır.

Doğru OpenArt wording:
```
Use @image1 as the exact first frame and only visual continuity source.
Preserve exactly what is visible in @image1.
Do not reinterpret @image1.
Do not recreate the scene from description.
Only preserve what is visible in @image1.
```

Yanlış OpenArt wording:
```
continue from previous video
match previous shot
opening final frame
Shot 01 final frame
```
...eğer hemen `@image1` olarak tanımlanmıyorsa.

---

## 2. First-Second Continuity Hold Rule

Continuity-linked shot'larda ilk 1 saniye `@image1`'i korumalıdır.

Kurallar:
- Mevcut karakterler küçük idle motion yapabilir (blink, breathe, tiny smile, very slight head/hand motion).
- Yeni karakterler ilk frame'de görünmemelidir (eğer `@image1`'de zaten yoksa).
- Yeni karakterler sadece 1. saniyeden sonra görünür.
- İlk 1 saniye continuity hold'dür, donma (freeze) değildir.

İzin verilen (ilk 1 saniye):
- Blink
- Breathing
- Tiny smile
- Very slight head/hand motion

Yasak (ilk 1 saniye):
- Camera pull-back
- Camera reset
- Wider frame
- New side objects
- Lighting/sky change
- New character appearing
- Existing character stepping away
- Existing character scale/position change

---

## 3. Stable Composition vs Frozen Scene Rule

Tanımlar:
- "Stable composition" = camera ve background continuity korunur.
- Bu, karakterlerin donduğu anlamına GELMEZ.
- İlk 1 saniyeden sonra karakterler doğal şekilde hareket etmelidir.

Kurallar:
- Full-shot hard lock wording kaçınılmalıdır (gerekmedikçe).
- Tercih edilen:
```
Camera preserves the @image1 composition.
Do not pull back, widen, reset, push in, pan, tilt, zoom, track or reframe.
```
- Kaçınılması gereken:
```
Everything locked for entire shot
Static locked camera for every beat
```
...eğer bu hareketi öldürüyorsa.

---

## 4. Natural Character Motion Rule

Her preschool video shot'ı canlı hissettirmelidir.

Gerekli micro-actions:
- Blinking
- Breathing
- Small smiles
- Head turns
- Hand gestures
- Small steps/hops
- Looking at object
- Looking at another character
- Pointing gently
- Shared reaction

Diyalog sahneleri sadece talking pose olmamalıdır.

Her 3-5 saniyede küçük bir görsel aksiyon olmalıdır (eğer shot kasıtlı olarak duragan değilse).

---

## 5. Character Entrance Without Recomposition Rule

Kurallar:
- Yeni karakter girişi `@image1`'e adapte olmalıdır.
- Karakteri göstermek için frame genişletilmemeli/recompose edilmemelidir.
- `@image1` zaten desteklemiyorsa tam visible entrance path istenmemelidir.
- Tam path görünmüyorsa, karakter ertelenmiş hold之后 mevcut güvenli görünür alanda zaten görünür olarak yerleştirilmelidir.
- Karakter okunabilir olmalıdır.
- Karakter tiny distant background olmamalıdır.
- Karakter close-up/foreground olmamalıdır (kasıtlı olmadıkça).
- Karakter crop edilmemeli veya gizlenmemelidir.

Güvenli wording:
```
After 1 second, [character] becomes visible inside the existing @image1 composition.
[Character] appears in the existing right-side/right-midground area if visible.
Do not widen the camera to show the entrance.
Do not create a new path.
```

Riskli wording:
```
Use a wide enough frame to show the full entrance path.
Full entrance path must be visible.
Character enters from far right path.
```
...eğer shot zaten wide değilse ve path `@image1`'de görünmüyorsa.

---

## 6. Character Scale Rule

Kurallar:
- Mevcut karakterler tam `@image1` scale'ini korur.
- Yeni karakterler pozisyonlarına göre doğru perspective scale kullanır.
- Wide-shot percentage scale'i medium-close frame'lere uygulanmaz.
- `@image1` medium-close ise "6-8% of frame" dayatılmaz.
- Karakter shot boyunca oversized olmamalıdır.
- Karakter tiny/unreadable olmamalıdır (kasıtlı background olmadıkça).

---

## 7. Sky, Lighting and Colour Continuity Rule

Kurallar:
- Sky, lighting, colour grading, exposure ve contrast `@image1`'den miras alınır.
- `@image1`, mood/style/lighting/atmosphere metnini override eder.
- OpenArt-facing prompt'larda "warm morning daylight" kaçınılmalıdır (turuncu/sunset riski).
- Kullanılacak:
```
same clean blue morning daylight from @image1
same sky, lighting, colour grading, exposure and contrast from @image1
```

Yasak drift:
- Sunset sky
- Orange sky
- Golden sky
- Grey sky
- Dramatic clouds
- Painterly sky change
- Lighting reinterpretation
- Colour temperature shift

---

## 8. Ghosting / Duplicate Character Prevention Rule

Tüm karakter hareketi tek bir solid karakter kimliği korumalıdır.

Yasak:
- Ghost character
- Transparent duplicate
- Double exposure
- Motion smear
- Character trail
- Overlapping duplicate face
- Overlapping duplicate body
- Semi-transparent copy during movement
- Duplicate head during turn
- Duplicated character after motion

Güvenli wording:
```
[Character] remains a single solid character at all times.
[Character] may turn naturally but must not duplicate, smear, or leave a ghost image.
```

---

## 9. Natural Ambience / No Music Rule

Eğer shot'ta müzik olmamalıysa, bu açıkça belirtilmelidir.

Sound section şunu söylemelidir:
```
Natural ambience only.
No music.
No background music.
No melody.
No song.
No soundtrack.
No musical bed.
```

Negative prompt şunları içermelidir:
```
music, background music, melody, song, soundtrack, musical bed
```

---

## 10. Dialogue Action Rule

Diyalog fiziksel aksiyonla desteklenmelidir.

Örnek:
- Karakter A nazikçe el sallar ve repliği söyler.
- Karakter B A'ya döner.
- Karakter B nesneye işaret eder.
- Her iki karakter de gülümser veya birlikte bakar.

Kaçınılması gereken:
- Her iki karakterin 15 saniye boyunca dimdik durması
- Static talking pose
- Frozen dialogue scene
- Ağız dışında hareket yokluğu

---

## 11. No Late Object Spawning / Object Must Exist Before Discovery Rule

Pompom Hills continuity shot'larında, hikaye beat'inin parçası olan herhangi bir nesne, karakter fark etmeden, işaret etmeden, adını vermeden veya keşfetmeden ÖNCE sahnede fiziksel olarak görünür olmalıdır.

Bir hikaye nesnesi sadece diyalogun ihtiyacı olduğu anda görünmemelidir.

Bu kural şunlara uygulanır: bench, çiçek, taş, oyuncak, tabela, ev, ağaç, aksesuar, renk objeleri, arka plan objeleri ve discovery objeleri.

Yanlış:
- Karakter "I see blue!" der ve arkasında aniden mavi bir obje belirir.
- Bir bench, badge, çiçek, taş veya aksesuar arka planda adlandırılmadan hemen önce pop-in yapar.
- Kamera veya sahne diyalogu karşılamak için sessizce yeni bir nesne üretir.
- Bir discovery objesi geç ortaya çıkar, fade in yapar, spawn olur, başka bir objeden morph olur veya daha önce mevcut olmadan görünür hale gelir.

Doğru:
- Nesne ilk frame'de zaten görünürdür veya discovery beat'inden ÖNCE net şekilde mevcuttur.
- Karakter kilitli sahnede zaten var olan bir nesneyi fark eder.
- Nesne boyunca aynı pozisyon, boyut, renk ve kimliği korur.
- Discovery karakterin dikkatinden gelir, nesne yaratılmasından değil.

OpenArt-facing wording:
```
The discovery object must already be visible in @image1 or clearly present before the character notices it.
Do not create, reveal, spawn, fade in, pop in, morph, move, resize, repaint, duplicate, or replace the discovery object.
The object must not appear for the first time right before or during the dialogue.
The character may notice the object, but the scene must not generate the object.
```

Negative prompt additions:
```
late object appearance, object pop-in, object spawning, object appearing from nowhere, object appearing right before dialogue, discovery object appearing late, prop spawning, prop pop-in, background object appearing late, object fade-in, object morphing into discovery object, newly generated discovery object, object created to match dialogue, object not present before discovery
```

Shot 04 ve sonrası için renk keşiflerinde:
```
The colour object must already be visible before the discovery beat begins. 
The character discovers it by looking, pointing, reacting or naming it. 
Do not make the object appear, spawn, fade in, or become newly visible 
at the moment of discovery.
```

---

## 12. Final Frame Continuity Rule

Bir shot'ın final frame'i, bir sonraki continuity-linked shot için `@image1` olarak kullanılabilir olmalıdır.

Final frame kazara şunları yapmamalıdır:
- İstenmeyen close-up'a dönüşmek
- Önemli karakterleri crop etmek
- Işığı değiştirmek
- Karakter scale'ini değiştirmek
- Ghosting oluşturmak
- Bir karakteri gizlemek
- Farklı bir kompozisyona kaymak
- İstenmeyen yeni nesneler eklemek

Ama:
Eğer hikaye kasıtlı olarak medium-close bitiyorsa, sonraki shot o medium-close `@image1`'den devam etmelidir, zorla wide'e dönmemelidir.

---

## 13. Prompt Length and OpenArt-Facing Prompt Rule

Production dokümanları detaylı olabilir.
OpenArt prompt'ları kısa, direkt ve çelişkisiz olmalıdır.

Kural:
- Üretim markdown'ını OpenArt'a yapıştırma.
- Ayrı bir OpenArt prompt dosyası/bölümü oluştur.
- Sadece şunları dahil et:
  - Visual Prompt
  - Negative Prompt
  - Sound instruction (gerekirse)
  - Duration ve reference setup
- OpenArt prompt'una QA checklist, analiz, insan bağlamı veya tam dokümantasyon ekleme.

---

## Global QA Checklist

### @image1 / Continuity:
- [ ] OpenArt-facing prompt `@image1`'i tek visual continuity source olarak kullanıyor.
- [ ] İlk 1 saniye `@image1`'e neredeyse birebir uyuyor.
- [ ] Mevcut karakterler `@image1` pozisyonunu, scale'ini ve genel yönünü koruyor.
- [ ] Mevcut karakterler küçük doğal idle motion yapabiliyor; donmuyorlar.
- [ ] Yeni karakterler ilk frame'de görünmüyor (`@image1`'de zaten yoksa).
- [ ] Yeni karakterler ertelenmiş entrance kullandığında sadece 1. saniyeden sonra görünüyor.

### Camera:
- [ ] Camera pull-back, widen, reset, pan, tilt, zoom, track veya reframe yapmıyor.
- [ ] Stable composition shot'ı donmuş hissettirmiyor.
- [ ] Shot istenmeyen wide establishing frame'e dönmüyor.
- [ ] Shot istenmeyen close-up'a push-in yapmıyor.

### Character Motion:
- [ ] Karakterler doğal preschool-safe hareketle canlı görünüyor.
- [ ] Diyalog görsel aksiyonla destekleniyor.
- [ ] Static talking pose yok.
- [ ] Frozen character performance yok.

### Character Entrance:
- [ ] Yeni karakter girişi camera recomposition zorlamıyor.
- [ ] Yeni karakter okunabilir, tiny distant background değil.
- [ ] Yeni karakter crop edilmemiş, gizlenmemiş, oversized veya close-up değil (kasıtlı olmadıkça).
- [ ] Tam entrance path sadece `@image1`'de zaten görünür olduğunda isteniyor.

### Ghosting:
- [ ] Ghost character yok.
- [ ] Transparent duplicate yok.
- [ ] Double exposure yok.
- [ ] Motion smear yok.
- [ ] Character trail yok.
- [ ] Overlapping duplicate face/body yok.

### Lighting:
- [ ] Sky, lighting, colour grading, exposure ve contrast `@image1`'e uyuyor.
- [ ] Sunset/orange/golden/grey/dramatic sky drift yok.
- [ ] Lighting reinterpretation yok.

### Sound:
- [ ] Doğal ambience only isteniyorsa, music/background music/melody/song/soundtrack/musical bed yok.
- [ ] Sound shot talimatlarıyla uyumlu.

### Final Frame:
- [ ] Final frame bir sonraki shot için `@image1` olarak kullanılabilir.
- [ ] Final frame kazara scale, lighting, composition veya character identity değiştirmiyor.
- [ ] Final frame medium-close ise, sonraki shot medium-close'dan devam etmeli, wide reset zorlamamalı.

---

## Solved Production Failures Log

### Failure: Shot 01 opening-to-shot mismatch
**Cause:** Yeni karakterin ilk frame'de görünmesi camera pull-back / wider reset'e neden oldu.
**Fix:** `@image1` exact first frame, ilk 1 saniye continuity hold, ertelenmiş character introduction.

### Failure: Shot 01 sky became orange/sunset
**Cause:** Warm/generic lighting dili `@image1`'i override etti.
**Fix:** Sky/lighting absolute lock from `@image1`; warm lighting dilinden kaçınılması.

### Failure: Shot 01 Kiko became giant foreground edge character
**Cause:** "Partial edge reveal" wording.
**Fix:** Karakter mevcut visible path / safe existing area'da görünür olmalı, fully or mostly visible, correct world scale, cropped/foreground değil.

### Failure: Shot 01 late push-in
**Cause:** Discovery/dialogue camera push-in'i tetikledi.
**Fix:** Final frame continuity rule; istenmeyen push-in yok; hikaye kasıtlı olarak medium-close bitiyorsa sonraki shot o frame'den devam etmeli.

### Failure: Shot 02 became frozen/static dialogue scene
**Cause:** Full-shot hard camera lock ve çok az aksiyon.
**Fix:** Stable composition vs frozen scene rule; natural character motion rule; her 3-5 saniyede aksiyon beats.

### Failure: Shot 02 Kiko ghost/double exposure
**Cause:** Çok sert lock altında character turn motion smear/duplicate'e neden oldu.
**Fix:** Ghosting prevention rule.

### Failure: Shot 02 unwanted background music
**Cause:** Açık no-music rule yoktu.
**Fix:** Natural ambience only / no music rule.

---

## Shot Template Requirements

Her gelecek shot dosyası OpenArt üretiminden önce şu bölümleri içermelidir:

### OpenArt Reference Setup
```
@image1 = [attached reference image, exact source]
@image1 is the only visual continuity source.
```

### Continuity Hold
```
First 1 second:
- preserve @image1
- existing characters may idle
- no new character
- no camera reset
```

### Character Motion
```
After continuity hold:
- define specific small actions every 3-5 seconds
- avoid static talking pose
```

### Camera Continuity
```
- stable composition
- no pull-back/widen/reset
- no unwanted push-in
- no tracking/reframing
```

### Scale Continuity
```
- existing character keeps @image1 scale
- new character uses perspective scale
```

### Sound
```
- natural ambience only / or music allowed
- if no music, state explicit no music rules
```

### Ghosting Prevention
```
- all characters remain single solid forms
```

---

## Negative Prompt Modular Bank

Her kategoriden uygun terimler seçilmelidir:

### Camera:
```
camera pull-back, wider first frame, recomposed scene, new establishing shot, camera reset, changed camera angle, changed lens, camera tracking, pan, tilt, zoom, push-in, pull-back, reframing
```

### Lighting:
```
changed lighting, changed colour grading, sky colour shift, sunset sky, orange sky, golden sky, grey sky, dramatic sky, painterly sky change, lighting reinterpretation
```

### Characters:
```
oversized character, cropped character, character too close to camera, character dominating frame, tiny distant character, unreadable character, character hidden behind objects, wrong perspective scale
```

### Continuity:
```
changed character position, changed character scale, character teleporting, character appearing from nowhere, character pop-in, character disappearing, character side-switching
```

### Ghosting:
```
ghost character, duplicate character, transparent character, double exposure, motion smear, character trail, overlapping duplicate face, overlapping duplicate body
```

### Sound:
```
music, background music, melody, song, soundtrack, musical bed
```

### Text:
```
text, captions, subtitles, speech bubbles, logo, watermark
```
