# Video Production Preflight System

> Her OpenArt video üretiminden ÖNCE bu kontrol sisteminden geçilmelidir.
> Amaç: Üretime geçmeden önce sorunları yakalamak.

---

## Purpose

OpenArt video üretiminden önce her shot bir preflight check'ten geçmelidir.

Amaç, büyük sorunların üretim başladıktan sonra değil, ÖNCE yakalanmasını sağlamaktır.

Çoğu OpenArt hatası eksik kurulumdan gelir:
- Discovery object erken tohumlanmamış
- `@image1` planlanan aksiyonu desteklemiyor
- Kamera bir objeyi aramak zorunda kalıyor
- Prompt frame'de görünmeyen bir şeyi istiyor
- İkincil reference image continuity'yi override ediyor
- Shot sakin ama boş ve static olmuş
- Music/chime istemsiz üretilmiş
- Final frame bir sonraki shot için kullanılamıyor

Bu sistem bu sorunları üretimden önce engeller.

---

## 0. HARD PREFLIGHT GATE: FRAME-SUPPORTED ACTION ONLY

> **Bu bir zorunlu geçittir. Kurallar metin olarak yeterli değildir.**
> Bir shot sadece "doğru kelimeler içeriyor" diye geçemez.
> @image1 frame'i gerçekten aksiyonu desteklemelidir.

### Temel Kural

Bir shot preflight'tan geçemez sadece şunları içeriyor diye:
- "background lock" metni
- "no new objects" metni
- "no object spawning" metni
- "continuity hold" metni

Bu kurallar SADECE @image1 gerçekten aksiyonu destekliyorsa geçerlidir.

### Doğrulama Süreci

Her shot için şu adımlar ZORUNLUDUR:

**1. Gerekli Objeleri Listele**
Her shot'ta kullanılan tüm story-relevant objeleri, prop'ları, landmark'ları, location feature'ları ve action target'ları listele.

Örnekler:
- bench (Mimi tries to lie on it)
- flower patch (Mimi lies on flowers)
- stream (they walk toward a stream)
- big tree (they find a big tree)
- leaf blanket (Kiko picks a large leaf)
- stars (soft stars appear in final beat)
- pillow, carrot box, stepping stones, doorway, path, sleeping spot

**2. Her Obje İçin Cevapla**
Her obje için şu soruları cevapla:

| Soru | Gereken Cevap |
|------|---------------|
| @image1'de görünür mü? | EVET veya daha önce tohumlanmış |
| Net şekilde lokalize edilmiş mi? | EVET |
| Karakter etkileşime geçebilir mi? | EVET, kamera araması olmadan |
| Model bunu icat etmek zorunda mı? | HAYIR |

**3. Sonuç**

Herhangi bir gerekli obje için:
- @image1'de görünür DEĞİLSE
- VE daha önce onaylı bir setup shot'tunda tohumlanmamışsa

**SHOT OTOMATİK OLARAK PREFLIGHT'TA BAŞARISIZ OLUR.**

### Başarısızlık Durumunda Yapılacaklar

Bu durumu düzeltmek için:
1. Shot'ı yeniden yaz - sadece görünen objeleri kullan
2. VEYA daha önceki setup shot'ını revize et - objeyi tohumla
3. VEYA Shot 01 master setup frame'e objeyi ekle

Yapılmaması gerekenler:
- ❌ Sadece negative prompt ekle
- ❌ OpenArt'ın doğru icat edeceğini um
- ❌ Objenin dialogue sırasında görünmesine izin ver
- ❌ "Model muhtemelen doğru yapar" diye düşün

### Örnekler

**GEÇERSİZ:**
```
@image1 shows Mimi and Kiko in a grassy area.
Shot asks them to walk to a stream.
The stream is not visible or seeded.
→ FAIL PREFLIGHT
```

**GEÇERSİZ:**
```
@image1 shows a path and flowers.
Shot asks Kiko to pick a large leaf blanket.
The large leaf is not visible.
→ FAIL PREFLIGHT
```

**GEÇERSİZ:**
```
@image1 shows dusk sky with no stars.
Shot asks soft stars to appear in the final beat.
Stars were not seeded.
→ FAIL PREFLIGHT (unless explicit planned gradual sky transition)
```

**GEÇERLİ:**
```
@image1 shows Mimi, Kiko, burrow entrance, flowers, path stones,
and a visible soft leaf near the grass.
Shot asks Kiko to use the visible leaf as a blanket.
→ PASS if camera does not move to search for it.
```

---

## 0.1 HARD GATE: MASTER FRAME ACTION LAYOUT (STAGED, NOT JUST VISIBLE)

> **§0 objenin GÖRÜNÜR olup olmadığını sorar. Bu gate objenin AKSİYON İÇİN
> DOĞRU YERLEŞTİRİLİP yerleştirilmediğini sorar.**
> Bir obje frame'de "var" diye onaylamak yetmez. Sonraki shot'ların aksiyon
> objesi, karakterin doğal olarak ulaşıp etkileşebileceği bir interaction zone
> olarak sahnelenmelidir.

### Neden Bu Gate Var (Öğrenilen Ders)

S01E04'te ağaç ve büyük çiçek çalısı Shot 01 master frame'de **vardı** — ama ikisi
de karakter aksiyonları için yanlış mesafede / yanlış pozisyondaydı:
- Flower patch entrance'ın solunda ama Mimi'nin oturup yaslanacağı kadar sahne içinde net değildi.
- Tree/grass alanı sağ arkada, dekor gibi, Mimi'nin doğal olarak gidip yatacağı kadar yakın değildi.

Sonuç: OpenArt sonraki shot'larda "yanlış" objeyi kendi açısından çözdü —
aksiyon objesini karaktere uygun hale getirmek için **büyüttü / yaklaştırdı /
sahneye çekti**. Bu bizim için continuity break oldu.

**Kök neden:** Pipeline'da object *presence check* vardı ama object *staging
check* yoktu. Bu gate o eksikliği kapatır.

### Temel Kural

```
Visible is not enough. The object must be placed for action.
Görünür olması yetmez. Obje aksiyon için yerleştirilmiş olmalı.
```

Bir shot, sonraki aksiyonlar için master setup görevi görüyorsa (ör. Shot 01),
frame sadece gerekli objeleri **içermekle** kalmamalı — her gerekli aksiyon
objesini **kullanılabilir bir interaction zone** olarak konumlandırmalıdır.

### Doğrulama Süreci (Master Setup Frame İçin)

Bir master setup frame'ini onaylamadan ÖNCE, sonraki shot'larda kullanılacak her
gelecek aksiyon objesini belirle. Her aksiyon objesi için doğrula:

| Kontrol | Gereken |
|---------|---------|
| Master frame'de görünür mü? | EVET |
| Cropped mı? | HAYIR |
| Sadece dekoratif mi? | HAYIR — aksiyon için kullanılabilir olmalı |
| Karakterin doğal ulaşabileceği mesafede mi? | EVET (2–3 küçük adım) |
| Planlanan etkileşim için yeterince büyük mü? | EVET |
| Kamera hareketi olmadan etkileşilebilir mi? | EVET |
| Sonradan hareket/büyüme/çoğalma/spawn gerektirmeyecek şekilde mi konumlanmış? | EVET |
| Gerektiğinde ana landmark / transition objesiyle birlikte görünüyor mu? | EVET |

### Sonuç

Bir gelecek aksiyon objesi:
- çok uzaktaysa,
- çok küçükse,
- sadece dekoratifse,
- karakterlerin arkasında gizliyse,
- veya yalnızca background'daysa,

**MASTER FRAME NOT READY.**

→ Master frame'i video üretimi için onaylama. First-frame still'i yeniden üret;
kredi harcamadan önce staging'i düzelt.

### Pompom Hills Kısa Versiyon (OpenArt-facing)

```text
Every master setup must stage the next actions, not just show the world.

If a flower patch will be used, it must be usable as a flower patch.
If a tree/grass area will be used, it must be reachable and usable.
If an entrance will be used, it must remain open, visible, and reachable.

Do not approve decorative-only objects as action-ready objects.
```

### Master Frame Action Layout Checklist (S01E04 türü dış mekân örneği)

```
[ ] Flower patch visible mı?
[ ] Flower patch Mimi'nin oturabileceği / yaslanabileceği kadar usable mı?
[ ] Flower patch entrance'tan doğal yürüme mesafesinde mi?

[ ] Tree visible mı?
[ ] Tree/grass area Mimi'nin 2–3 küçük adımda ulaşabileceği yerde mi?
[ ] Tree/grass area sahnenin aşırı arkasında / kenarında / dekor gibi mi kalıyor? (öyleyse REJECT)

[ ] Entrance visible mı?
[ ] Entrance taşlarla birlikte Shot 04–05 transition için açık mı?

[ ] Bu üç aksiyon alanı aynı wide frame içinde birlikte çalışıyor mu?
```

> Doğru onay kriteri: **var + yakın + usable + aksiyona uygun.**
> Sadece "var" demek yetmez.

---

## 1. Prompt + Frame Must Be Checked Together

Bir shot prompt'u sadece metinle onaylanamaz.

Her OpenArt shot'ı gerçek `@image1` frame'iyle birlikte kontrol edilmelidir.

Prompt sadece `@image1` görsel olarak planlanan aksiyonu destekliyorsa geçerlidir.

Yanlış:
- Prompt "yellow flowers" diyor ama `@image1` sadece belirsiz mixed flowers gösteriyor.
- Prompt "blue bench" diyor ama `@image1` bench'i göstermiyor.
- Prompt "character points to object" diyor ama obje görünür değil.
- Prompt daha geniş bir view gerektiriyor ama `@image1` medium-close.
- Prompt daha önce tohumlanmamış yeni bir prop gerektiriyor.

Doğru:
- `@image1` zaten gerekli karakterleri içeriyor.
- `@image1` zaten discovery objesini içeriyor veya net şekilde destekliyor.
- Shot aksiyonu mevcut frame içinde gerçekleşebilir.
- Kamera araması, reseti, genişlemesi, pan'i veya yeni nesne üretimine ihtiyaç yok.

Hard kural:
OpenArt'tan onaylı frame'in desteklemediği hiçbir şeyi keşfetmesini isteme.

---

## 2. RULE LANGUAGE IS NOT COMPLIANCE

> **Bir shot dosyası sadece doğru kural metni içeriyor diye "safe" olarak işaretlenemez.**

### Sorun

Bir shot dosyası şu metinleri içerebilir:
```text
Background locked.
No new environment elements.
No object spawning.
Camera locked.
Lighting locked.
```

AMA aynı dosya şunu da istiyor olabilir:
```text
They walk toward a stream.
Kiko picks a large leaf.
Mimi lies on a flower patch.
Stars appear in the sky.
```

Eğer stream / leaf / flower patch / stars @image1'de görünmüyorsa, kural metni anlamsızdır.

Story isteği kuralı ezer. Model mecburen yeni obje üretir.

### Çelişki Kontrolü

Validator şu üç şeyi karşılaştırmalıdır:

1. **Prompt neyi yasaklıyor?**
   - "no new environment"
   - "no object spawning"
   - "background locked"

2. **Shot aksiyonu ne gerektiriyor?**
   - walk to stream
   - pick a leaf
   - lie on flower patch
   - stars appear

3. **@image1 ne gösteriyor?**
   - grassy area (no stream visible)
   - path and flowers (no large leaf visible)
   - dusk sky (no stars visible)

**Çelişki varsa: SHOT BAŞARISIZ.**

### Yasaklanan Durumlar

| Kural Metni | Aksiyon İsteği | @image1 Göstermiyor | Sonuç |
|-------------|----------------|---------------------|-------|
| "no new environment" | walk to stream | stream yok | FAIL |
| "no object spawning" | pick a leaf | leaf yok | FAIL |
| "camera locked" | walk to new location | location yok | FAIL |
| "lighting locked" | dusk → night with stars | stars yok | FAIL* |

*Yalnızca açıkça planlanmış gradual transition varsa geçerli.

### Örnek Çelişki

**SHOT DOSYASI:**
```markdown
## Background Object Lock
The background is locked from the first frame.
Do not create new objects.

## Visual Prompt
Kiko leads Mimi toward a small rounded bench.
Mimi tries to lie on it.
```

**@image1:**
```
Shows Mimi, Kiko, and grassy area.
No bench visible.
```

**SONUÇ:**
```
Shot contains "background lock" and "no new objects" text.
BUT shot action requires a bench that is not in @image1.
This is a CONTRADICTION.
→ FAIL PREFLIGHT
```

Doğrusu ya:
1. Shot'ı yeniden yaz: "Kiko leads Mimi toward [visible object]"
2. VEYA Shot 01'e bench ekle: "Kiko leads Mimi toward the already-visible bench"

---

## 3. Episode Object / Colour / Prop Map

Bir episode için shot prompt'ları yazmadan önce bir object map oluştur.

Object map, her shot'ta kullanılacak tüm hikaye objelerini, renk ipuçlarını, prop'ları, landmark'ları ve discovery item'ları listeler.

Gerekli format:

```
Shot 01:
- visible characters:
- visible environment anchors:
- seeded future objects:
- discovery object if any:

Shot 02:
- @image1 source:
- discovery object:
- must already be visible from earlier:
- new objects allowed: no, unless explicitly planned

Shot 03:
- @image1 source:
- discovery object:
- must already be visible from earlier:
- new objects allowed: no, unless explicitly planned
```

Tüm shot'lar için devam et.

Object map şunları cevaplamalıdır:
- Bu shot'ta hangi obje keşfediliyor?
- Daha önce tohumlanmış mıydı?
- `@image1`'de görünür mü?
- Net şekilde lokalize edilmiş mi?
- Shot'ın bulmak için kamera hareketine ihtiyacı var mı?
- İkincil bir reference image gerektiriyor mu?
- OpenArt onu yanlışlıkla spawn edebilir mi?

Cevap güvensizse, üretimden önce daha önceki bir kurulum shot'ını revize et.

---

## 4. Shot 01 as Master Setup / Visual Contract

Bir sequence'in Shot 01'i sadece bir açılış shot'ı değildir.

Shot 01, episode veya sahne için master kurulum frame'i olarak hareket etmelidir.

Shot 01 şunları tohumlamalıdır:
- Ana oynanabilir alan
- Önemli environment anchor'ları
- Gelecekteki discovery objeleri
- Gelecekteki renk objeleri
- Önemli prop'lar
- Önemli bench / flower / stone / sign / toy'lar
- Karakter scale
- Sky ve lighting
- Camera language

Eğer sonraki bir shot bir objeye ihtiyaç duyuyorsa, o obje ideal olarak Shot 01'de görünür olmalı veya discovery shot'ından ÖNCE özel bir kurulum shot'ında tanıtılmalı.

> **Kritik:** Objeyi Shot 01'e koymak yetmez — objeyi aksiyon için DOĞRU
> sahnelemek gerekir. Her gelecek aksiyon objesi kullanılabilir bir interaction
> zone olarak konumlanmalıdır (yakın + usable + aksiyona uygun). Bkz. §0.1 HARD
> GATE: MASTER FRAME ACTION LAYOUT. Sadece "görünür" olan ama uzak/küçük/dekoratif
> kalan objeler master frame'i NOT READY yapar.

---

## 5. Early Object Seeding / No Surprise Discovery Objects

Herhangi bir object, prop, landmark, renk ipucu veya discovery item, sonraki bir shot'ta önemli hale gelecekse, daha önceki bir kurulum shot'ında kasıtlı olarak tohumlanmalıdır.

Sonraki shot'lar zaten tohumlanmış bir objeyi keşfeder, fark eder, işaret eder, adlandırır veya etkileşime girer.

Onu ilk kez oluşturmaz veya göstermez.

Discovery karakterin dikkatinden gelir, dünya yaratılmasından değil.

---

## 6. Discovery Object Must Be Localised

Bir discovery objesinin sadece dünyada belirsiz bir yerde olması yetmez.

Üretimden önce discovery objesi net şekilde lokalize edilmelidir.

Shot contract'ı şunları belirtmelidir:
- Objenin `@image1`'de nerede olduğu
- Foreground, midground veya background olup olmadığı
- Frame'in hangi tarafında olduğu
- Onu tanımlayan yakınlardaki anchor
- Karakterin fark edecek kadar okunabilir olup olmadığı

Örnek:
Güvensiz:
"yellow flowers in the set"

Güvenli:
"already-visible yellow flowers inside the mixed flowerbed area behind the blue bench, left/right of the characters, part of the existing @image1 background"

Eğer obje çok belirsiz veya okunabilir değilse, discovery shot'ını zorlama.
Daha önceki kurulum shot'ını revize et veya özel bir reference sağla.

---

## 7. Multi-Image Reference Planning / Each Image Must Have A Role

Üretimden önce bir image'ın yeterli olup olmadığına karar ver.

Tek image yeterli olduğunda:
- `@image1` zaten tüm gerekli karakterleri içeriyor
- `@image1` zaten discovery objesini içeriyor
- Kamera, ışık, ölçek ve ortam doğru
- Ekstra object veya character referansına ihtiyaç yok

Birden fazla image gerektiğinde:
- Bir prop, badge, bench, çiçek, oyuncak veya landmark ayrı bir design referansı gerektiriyor
- Bir karakter detayı korunmalı
- Bir ortam detayı canon olmalı ama `@image1`'de okunabilir değil

Her yüklenen image'ın net bir rolü olmalıdır.

Standart rol sistemi:
```
@image1 = exact first frame continuity source
@image2 = object design only
@image3 = character design only
@image4 = environment canon only
```

Hard kural:
`@image1` her zaman önceliklidir:
- First frame
- Camera angle
- Composition
- Character position
- Character scale
- Lighting
- Colour grading
- Visible environment

İkincil image'lar `@image1`'i override etmemelidir (açıkça belirtilmedikçe).

---

## 8. Shot Contract Before OpenArt Prompt

OpenArt-facing prompt'u yazmadan önce, her shot için kısa bir Shot Contract olmalıdır.

Gerekli format:

```
## Shot Contract

Shot:
@image1 source:
Characters visible in @image1:
Required story objects/props/targets (all of them):
  - [object]: visible in @image1? / seeded earlier? / localised?
Discovery object:
Is discovery object visible in @image1:
Discovery object location:
Rule text vs action contradiction check:
  - Forbids: [no new objects / background lock / ...]
  - Action needs: [walk to X / pick Y / ...]
  - @image1 shows: [...]
  - Contradiction? yes/no
Must preserve:
Camera:
Allowed movement:
Forbidden:
Dialogue:
Beat structure:
Sound:
Final frame requirement:
Risk verdict:
- SAFE / RISKY / NOT READY
```

> Not: Eğer "Required story objects" listesinde `@image1`'de görünmeyen VE tohumlanmamış bir obje varsa, verdict otomatik olarak **NOT READY** olur. Kural metni bunu değiştirmez (bkz. §0, §2).

Örnek:

```
Shot:
04 — Yellow Flowers

@image1 source:
Shot 03 approved final frame.

Characters visible in @image1:
Kiko and Mimi.

Discovery object:
Yellow flowers.

Is discovery object visible in @image1:
Yes, inside existing mixed flowerbed / planter area.

Discovery object location:
Background flowerbed area behind / around the blue bench, 
already part of @image1.

Must preserve:
Kiko, Mimi, blue bench, Big Pompom Tree, stepping stones, 
paths, flowerbeds, sky, lighting.

Camera:
Preserve @image1 composition.

Allowed movement:
Only character eye/head/hand gestures, tiny idle motion.

Forbidden:
New planter, new flower cluster, new garden, Flower Hill, 
camera search, music, chime, ghosting.

Dialogue:
Kiko: Yellow flowers!
Mimi: So bright!

Beat structure:
Every 2-3 seconds has action, reaction, look, point, 
smile, nod, or dialogue.

Sound:
Natural ambience only. No music. No chime.

Final frame requirement:
Usable as @image1 for next shot. No crop, no close-up, 
no lighting change, no new object.

Risk verdict:
Safe only if yellow flowers are visible enough in @image1.
```

OpenArt prompt'u bu contract'a dayanmalıdır.
Eğer contract risky veya not ready ise henüz prompt yazma.

---

## 9. OpenArt Prompt Structure

OpenArt-facing prompt dosyaları kısa, direkt ve operasyonel olmalıdır.

Sadece şunları içermelidir:
- Visual Prompt
- Negative Prompt
- OpenArt Settings
- Reject Checklist

Uzun production notları, teori, QA dokümantasyonu veya iç mantık OpenArt-facing prompt'un içine konmamalıdır.

Önerilen Visual Prompt sırası:
1. Duration
2. `@image1` continuity rule
3. Lighting / sky lock
4. Discovery object lock
5. Timed beat structure
6. Calm but alive rule
7. Character scale / identity rule
8. Camera lock
9. Ghosting prevention
10. Text / character / sound restrictions
11. Dialogue

---

## 10. Calm But Alive / No Empty Pauses

Pompom Hills sakin, yumuşak ve preschool-safe olmalıdır ama asla görsel olarak ölü olmamalıdır.

Her 10-15 saniyelik shot'ta 2-3 saniyede bir net bir beat olmalıdır.

İzin verilen beat'ler:
- Blink
- Breathe
- Smile
- Turn head
- Look at object
- Look at another character
- Point gently
- Tiny nod
- Tiny hand gesture
- Bir veya iki küçük adım/hop (güvenliyse)
- Shared reaction
- Kısa dialogue satırı

Yasak:
- Uzun boş bekleme
- Birkaç saniye sessiz bakışma
- Static talking pose
- Frozen characters
- Dead air
- Random filler motion
- Anlamsız dolaşma
- Hikaye beat'ini desteklemeyen hareket

---

## 11. Sound Must Be Explicit

Müzik istenmiyorsa, açıkça yasaklanmalıdır.

OpenArt-facing wording:
```
Natural ambience only:
soft breeze, distant birds, gentle tiny foot sounds, 
soft fabric-like character movement.
No music.
No background music.
No melody.
No song.
No soundtrack.
No musical bed.
No chime.
```

"Tiny discovery chime" kullanma (müzik veya chime kasıtlı olarak istenmedikçe).

---

## 12. Final Frame as Next @image1

Her shot'ın final frame'i bir sonraki shot'ın `@image1`'i olabilir.

Bu yüzden final frame onaylanmadan önce kontrol edilmelidir.

Final frame şunları içermemelidir:
- İstenmeyen close-up
- Crop
- Ghosting
- Duplicate character
- Lighting change
- Sky shift
- Object pop-in
- Yeni planlanmamış nesne
- Camera reset
- Character scale change
- Kullanılamayan kompozisyon
- Music-driven veya random action

Final frame şunları korumalıdır:
- Kullanılabilir karakter pozisyonları
- Stabil kamera
- Okunabilir ortam
- Continuity object pozisyonları
- Aynı lighting
- Aynı scale
- Sürpriz prop'lar yok

---

## Global Preflight Checklist

Üretimden önce her shot şunları cevaplamalıdır:

**HARD GATE (§0 ve §2 — önce bunlar geçmeli):**

0a. Shot'taki tüm story-relevant obje/prop/landmark/action target listelendi mi?
0b. Her gerekli obje `@image1`'de görünür VEYA daha önce tohumlanmış mı?
0c. Prompt'un yasakları (no new objects, background lock) ile aksiyon istekleri (walk to X, pick Y) arasında çelişki var mı?
0d. Herhangi bir gerekli obje görünmüyorsa → shot NOT READY, üretme.

**MASTER FRAME ACTION LAYOUT GATE (§0.1 — master setup shot'ları için):**

0e. Bu shot sonraki aksiyonlar için master setup mı? (Shot 01 vb.)
0f. Öyleyse: her gelecek aksiyon objesi sadece görünür değil, aynı zamanda usable interaction zone olarak mı sahnelenmiş?
0g. Her aksiyon objesi karakterin doğal ulaşabileceği mesafede + yeterince büyük + kamera hareketi gerektirmeden etkileşilebilir mi?
0h. Herhangi bir aksiyon objesi uzak / küçük / sadece dekoratif / karakter arkasında / sadece background ise → master frame NOT READY, first-frame still'i yeniden üret.

**Standart kontroller:**

1. `@image1` seçilmiş ve onaylanmış mı?
2. `@image1` görsel olarak bu shot'ı destekliyor mu?
3. Gerekli tüm karakterler `@image1`'de görünür mü?
4. Discovery objesi `@image1`'de görünür mü veya daha önce tohumlanmış mı?
5. Discovery objesi net şekilde lokalize edilmiş mi?
6. Shot'ın bir şeyi bulmak için kamera hareketine ihtiyacı var mı?
7. Evetse, shot kamera hareketini önleyecek şekilde yeniden yazılabilir mi?
8. İkincil reference image'lara ihtiyaç var mı?
9. Her image'ın net bir rolü var mı?
10. `@image1` diğer tüm image'lara öncelikli mi?
11. İlk 1 saniye continuity hold tanımlı mı?
12. Her 2-3 saniyede net bir action/reaction/dialogue beat var mı?
13. Sound doğal ambience only mi?
14. Music, melody, soundtrack ve chime kasıtlı olmadıkça yasak mı?
15. Ghosting ve duplicate characters yasak mı?
16. Final frame bir sonraki `@image1` olarak güvenli mi?
17. Sadece dialogue ihtiyaç duyduğunda görünen bir nesne var mı?
18. Kamera reset, widen, pan, zoom, search veya reframe'e neden olabilecek prompt wording var mı?
19. Orange/golden lighting drift'e neden olabilecek "warm morning" wording var mı?
20. Shot SAFE / RISKY / NOT READY mu?

Herhangi bir cevap güvensizse, henüz shot'ı üretme.

---

## Shot Status: SAFE / RISKY / NOT READY

Her shot üretimden önce şu üç statüden birini almalıdır. Bu statü, kural metnine göre değil, `@image1`'in aksiyonu gerçekten destekleyip desteklemediğine göre verilir.

### SAFE
`@image1` aksiyonu destekliyor ve tüm gerekli objeler görünür veya tohumlanmış.
- Tüm karakterler `@image1`'de görünür.
- Tüm story objeleri `@image1`'de görünür veya onaylı bir setup frame'de tohumlanmış.
- Kamera araması, reseti, genişlemesi yok.
- Lighting/sky jump yok.
- Yeni environment üretimi yok.

→ **Sadece SAFE shot'lar OpenArt üretimine geçebilir.**

### RISKY
Çoğu element destekleniyor, ama bir obje belirsiz, küçük veya kötü lokalize.
- Obje `@image1`'de var ama okunabilir değil.
- Obje çok küçük veya belirsiz konumda.
- Karakter etkileşimi kamera araması gerektirebilir.

→ **Rewrite veya daha iyi setup gerekir. RISKY shot üretime geçemez.**

### NOT READY
Shot görünmeyen obje, tohumlanmamış location değişikliği, kamera araması, lighting jump veya yeni environment üretimi gerektiriyor.
- Gerekli obje `@image1`'de yok ve tohumlanmamış.
- Yeni location'a yürüme (location görünmüyor).
- Stars/night gibi lighting değişikliği (planlanmamış).
- Model bir şeyi icat etmek zorunda.

→ **NOT READY shot ÜRETİLMEZ. Setup shot'ı revize et veya shot'ı yeniden yaz.**

### Statü Kuralı

```
Frame support yok = NOT READY = üretim yok.
```

Kural metni (background lock, no new objects) bir shot'ı SAFE yapmaz. Sadece `@image1`'in gerçek görsel desteği SAFE yapar.

---

## Required Workflow for Future Episodes

Bu sırayı kullan:

1. Episode beat list
2. Object / colour / prop map
3. Shot 01 master setup requirements
4. Shot 01 üret ve onayla
5. Her shot için:
   a. `@image1` frame'ini incele
   b. Shot Contract yaz
   c. Object visibility ve localisation kontrol et
   d. Reference image rollerine karar ver
   e. OpenArt prompt'u yaz
   f. Test üret
   g. Onayla / reject et
   h. Hata tekrar edilebilir bir ders öğretiyorsa, global kuralı ekle veya güncelle

Shot Contract ve Preflight Checklist'i atlama.
