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

## 2. Episode Object / Colour / Prop Map

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

## 3. Shot 01 as Master Setup / Visual Contract

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

---

## 4. Early Object Seeding / No Surprise Discovery Objects

Herhangi bir object, prop, landmark, renk ipucu veya discovery item, sonraki bir shot'ta önemli hale gelecekse, daha önceki bir kurulum shot'ında kasıtlı olarak tohumlanmalıdır.

Sonraki shot'lar zaten tohumlanmış bir objeyi keşfeder, fark eder, işaret eder, adlandırır veya etkileşime girer.

Onu ilk kez oluşturmaz veya göstermez.

Discovery karakterin dikkatinden gelir, dünya yaratılmasından değil.

---

## 5. Discovery Object Must Be Localised

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

## 6. Multi-Image Reference Planning / Each Image Must Have A Role

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

## 7. Shot Contract Before OpenArt Prompt

OpenArt-facing prompt'u yazmadan önce, her shot için kısa bir Shot Contract olmalıdır.

Gerekli format:

```
## Shot Contract

Shot:
@image1 source:
Characters visible in @image1:
Discovery object:
Is discovery object visible in @image1:
Discovery object location:
Must preserve:
Camera:
Allowed movement:
Forbidden:
Dialogue:
Beat structure:
Sound:
Final frame requirement:
Risk verdict:
- safe / risky / not ready
```

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

## 8. OpenArt Prompt Structure

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

## 9. Calm But Alive / No Empty Pauses

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

## 10. Sound Must Be Explicit

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

## 11. Final Frame as Next @image1

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
20. Shot safe / risky / not ready mu?

Herhangi bir cevap güvensizse, henüz shot'ı üretme.

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
