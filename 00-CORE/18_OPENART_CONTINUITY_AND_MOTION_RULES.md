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

**Ölçülebilir zaman kuralı (zorunlu):** "No long pause" tek başına yeterli DEĞİLDİR. Her
OpenArt-facing prompt, hareketin ve diyalogun ne zaman başladığını sayısal olarak belirtmelidir.
Bu, §4A No Idle Opening / Immediate Life Rule tarafından zorunlu kılınır: frame-one motion,
ilk 1 saniye içinde ilk jest, ilk 1–2 saniye içinde diyalog. Bu zamanlama satırları yoksa
prompt NOT READY'dir.

Natural Character Motion Rule bölümünde her prompt şu yapıyı içermelidir:

```text
Calm but alive from the first frame: subtle breathing, blinking, warm expression, and the first approved gesture begins within the first 1 second. Dialogue begins within the first 1–2 seconds. No freeze, no long pause, no silent idle hold, no delayed wave, no delayed nod, no delayed reaction, no delayed dialogue, no waiting before action, no empty opening seconds.
```

---

## 4A. No Idle Opening / Immediate Life Rule

> **Kısa ad: NO IDLE OPENING / IMMEDIATE LIFE RULE.**
> Bu kural zorunludur ve her OpenArt-facing prompt'a uygulanır.
>
> **Neden:** Önceki "No long pause" kuralı yeterince güçlü değildi. OpenArt karakteri yine de
> birkaç saniye hareketsiz tutup el sallamayı veya konuşmayı ancak 5. saniye civarında
> başlatabiliyordu. Bu, boş ve sıkıcı preschool shot'ları yaratır ve üretim kredisini boşa
> harcar. Kural açık, ölçülebilir ve her OpenArt prompt'unun İÇİNDE uygulanır — sadece negative
> prompt'ta değil.

### Kural

Her OpenArt video shot'ı hemen canlı başlamalıdır.

- İlk frame zaten aktif, sıcak ve amaçlı hissetmelidir.
- Karakterler daha ilk frame'den itibaren subtle doğal hareket göstermelidir.
- İlk onaylı görünür jest ilk 1 saniye içinde başlamalıdır.
- Diyalog, shot açıkça sessiz olarak tasarlanmadıkça ilk 1–2 saniye içinde başlamalıdır.
- Hiçbir shot uzun sessiz hold, donmuş poz, boş establishing duraklama, gecikmiş el sallama,
  gecikmiş baş sallama, gecikmiş tepki veya gecikmiş diyalogla başlayamaz.

### Required wording — Visual Prompt

Visual Prompt bölümüne, shot'a uyarlanmış bir zamanlama paragrafı eklenir:

```text
The shot begins immediately with life and motion from frame one. The character(s) are already subtly alive at the first frame with gentle breathing, blinking, warm expression, and the first approved small gesture beginning within the first 1 second. Dialogue begins early, within the first 1–2 seconds of the shot. Do not hold a silent idle pose. Do not wait before action. Do not delay the dialogue.
```

### Required wording — Natural Character Motion Rule

```text
Calm but alive from the first frame: subtle breathing, blinking, warm expression, and the first approved gesture begins within the first 1 second. Dialogue begins within the first 1–2 seconds. No freeze, no long pause, no silent idle hold, no delayed wave, no delayed nod, no delayed reaction, no delayed dialogue, no waiting before action, no empty opening seconds.
```

### Required wording — Negative Prompt

```text
long silent pause, delayed dialogue, delayed speech, delayed gesture, delayed wave, delayed nod, waiting before action, idle pose, frozen opening, no movement at start, silent hold, empty opening seconds, late speech, late gesture, long establishing hold, motion starts late, dialogue starts late
```

### Uygulama kapsamı

Bu kural gelecekteki TÜM OpenArt video prompt'larına uygulanır: karakter tanıtımları, dünya
sahneleri, bölüm shot'ları, sezon açılışları, full-cast shot'ları ve sosyal video klipleri.

Özellikle 10–15 saniyelik OpenArt shot'ları için kritiktir. OpenArt'ın ilk 4–5 saniyeyi
sessizce sahneyi kurarak harcamasına izin verme. Bir preschool video shot'ı hemen canlı
hissetmelidir.

### İlk continuity saniyesiyle uyum

Bu kural §2 First-Second Continuity Hold Rule ile çelişmez. İlk 1 saniye continuity hold'dür,
donma değildir: mevcut karakterler `@image1` pozisyon/scale'ini korurken küçük idle motion
(blink, breathe, warm expression, tiny head/hand motion) yapar ve ilk onaylı jest bu birinci
saniye içinde başlar. "Hemen canlı" demek "kompozisyonu resetle" demek değildir — hareket
küçük karakter hareketinden ve erken diyalogdan gelir, kamera hareketinden değil.

### Kontrol kriteri (NOT READY testi)

Prompt'lar incelenirken, sadece "No long pause" yazan hiçbir OpenArt prompt'u kabul etme.

Bir prompt şunları belirtmiyorsa **NOT READY**'dir:
- motion from frame one
- first gesture within 1 second
- dialogue within 1–2 seconds (veya açıkça "silent shot")
- no silent idle opening
- no delayed dialogue

### Bu kural neyi değiştirmez

Mevcut hareket güvenlik kurallarını kaldırmaz. Şu kurallarla birlikte çalışır:
- Camera Lock / Stable Composition (§3)
- Natural Character Motion Rule (§4)
- Surprise element / late object kuralları (§11, §14)
- Character Count / entrance kuralları (§5)

Zamanlamayı çözmek için kamera hareketi ekleme. Aktivite yaratmak için prop ekleme. Ekstra
karakter ekleme. Çözüm sadece hemen başlayan küçük karakter hareketinden ve erken diyalogdan
gelmelidir.

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

## 14. Early Object Seeding / No Surprise Discovery Objects Rule

Her multi-shot Pompom Hills sequence'inde, sonraki bir shot'ta keşfedilecek, adlandırılacak, işaret edilecek veya etkileşime girilecek her hikaye objesi, sequence'in en kurulum shot'ında (tercihen Shot 01'de) zaten mevcut olmalıdır.

Bu şunları kapsar:
- Renk keşif objeleri
- Bench, badge, stepping stone, çiçek, oyuncak, tabela, ev, ağaç, aksesuar
- Arka plan objeleri ki sonradan hikaye beat'inin parçası olsun

Temel prensip:
Sonraki shot'lar zaten var olan bir objeyi keşfetmelidir. Objeyi ilk kez oluşturmalıdır.

Doğru:
- Shot 01 zaten mavi badge'i ortamda görünür bir yerde içerir.
- Shot 03 aynı mavi badge'e dikkat çeker.
- Nesne diyalogdan ÖNCE dünyanın fiziksel parçasıdır.
- Sonraki shot dikkat değiştirir, dünya içeriğini değil.

Yanlış:
- Nesne Shot 01 ve Shot 02'de eksiktir, Shot 03'te diyalog ihtiyacı olduğunda belirir.
- Bir bench, badge, çiçek, aksesuar veya renk objesi adlandırılmadan hemen önce arka planda pop-in yapar.
- Sahne script'i karşılamak için yeni bir nesne üretir.
- Nesne keşif anında önceden tohumlanmadan görünür hale gelir.

Planning kuralı:
Bir shot sequence'i yazmadan veya üretmeden önce, sequence için tüm gelecek discovery objelerini listele.
Onları en erken kurulum shot'ında (tercihen Shot 01'de) görsel olarak tohumla.
Eğer bir nesne Shot 01'de gösterilemiyorsa, keşif shot'ından ÖNCE özel bir kurulum shot'ında tanıtılmalı.

Tohum kuralı:
Tohumlanmış bir nesne Shot 01'de görsel odak olmak zorunda değildir.
Arka planda subtle ve okunabilir kalabilir.
Ama fiziksel olarak mevcut, okunabilir ve sonraki sürekliliği destekleyecek kadar stabil olmalıdır.

Süreklilik kuralı:
Tohumlandıktan sonra nesne şu açıdan aynı kalmalıdır:
- Kimlik
- Renk
- Genel pozisyon
- Ölçek
- İşlev

Nesnenin yapmaması gerekenler:
- Spawn olmak
- Pop-in yapmak
- Fade in yapmak
- Var olmak için morph olmak
- Çoğalmak
- Motive edilmeden farklı bir yere taşınmak
- Shot'lar arasında kimlik değiştirmek

Keşif kuralı:
Sonraki keşif shot'ında karakter şunları yapabilir:
- Nesneyi fark edebilir
- Ona bakabilir
- Ona işaret edebilir
- Ona gülümseyebilir
- Onu adlandırabilir
- Onun hakkında sorabilir
- Ona tepki verebilir

Ama sahne şunları yapamaz:
- Nesneyi üretmek
- Yeni oluşturulmuş bir versiyonunu göstermek
- Yerine başka bir nesne koymak
- Daha önce tohumlanmamış bir sürpriz nesne yaratmak

Shot 01 kurulum kuralı:
Bir sequence'in ilk shot'ı sadece karakter ve lokasyon tanıtmamalıdır.
Gelecekteki önemli hikaye objelerini de tohumlamalıdır.

Yani Shot 01 şunları kurmalıdır:
- Kullanılabilir ortam
- Oynanabilir alan
- Önemli görünür aksesuarlar
- Gelecekteki discovery objeleri
- Sequence'in görsel mantığı

OpenArt-facing wording (kurulum shot'ları için):
```
Seed all story-relevant future discovery objects in the environment 
from the beginning.
Objects that will be named, discovered, pointed at, or interacted 
with in later shots must already be visible in this setup shot.
Do not leave important future objects absent if they will be 
needed later.
```

OpenArt-facing wording (sonraki continuity shot'ları için):
```
Use @image1 as the exact first frame and only visual continuity source.
Any discovery object in this shot must already be visible in @image1 
or already established earlier in the sequence.
Do not create, reveal, spawn, fade in, pop in, morph, duplicate, 
move, resize, repaint, or replace the discovery object.
The character may discover the object, but the scene must not 
generate it.
```

Negative prompt additions:
```
late object appearance, surprise object, object pop-in, object spawning, 
object appearing from nowhere, discovery object appearing late, 
prop spawning, background object appearing late, object fade-in, 
object morphing into existence, newly generated discovery object, 
object created to satisfy dialogue, object not present before discovery, 
surprise prop reveal, bench appearing late, badge appearing late, 
colour object appearing late
```

QA kuralı:
Her sonraki keşif shot'ında kontrol et:
- Bu nesne daha önceki bir shot'ta zaten tohumlanmış mıydı?
- Shot 01'de veya başka bir önceki kurulum shot'ında görünür müydü?
- Sonraki shot aynı nesneyi mi keşfediyor, yoksa yenisini mi oluşturuyor?
- Nesne kimlik ve yerleşme açısından stabil kaldı mı?
- Dünya yeni bir aksesuar icat etmek yerine tutarlı kaldı mı?

---

## 15. Multi-Image Reference Planning / Each Image Must Have a Role

Bir shot birden fazla görsel referans gerektirdiğinde, tüm gerekli referans görselleri üretimden ÖNCE hazırlanmalı ve her referans görseli OpenArt-facing prompt içinde belirli bir role sahip olmalıdır.

Bu kural neden var:
OpenArt proje hafızası anlamaz. Sadece yüklenen referans görselleri ve prompt'u görür. Açıkça tanımlanmamış rollerle birden fazla görsel yüklenirse OpenArt bunları karıştırabilir, sürekliliği göz ardı edebilir, yanlış image'i kopyalayabilir, eksik nesneleri icat edebilir veya object reference'ı first frame olarak kullanabilir.

Tek image yeterli olduğunda:
- First frame continuity zaten tüm gerekli karakterleri içeriyor
- Gerekli hikaye objesi zaten görünür
- Lokasyon, ışık, ölçek ve kamera doğru
- Ekstra object/detail referansına ihtiyaç yok

Birden fazla image gerektiğinde:
- Continuity frame gelecek bir hikaye objesini net göstermiyor
- Bir prop, badge, bench, çiçek, oyuncak veya landmark ayrı bir görsel referans gerektiriyor
- Bir karakter detayı veya kostüm detayı korunmalı
- Shot, model tarafından icat edilmemesi gereken bir objeye bağlı
- Bir ortam detayı canon olmalı ama @image1'de okunabilir değil

Her yüklenen image'ın net bir rolü olmalıdır.

Örnek:
```
@image1 = exact first frame continuity source
@image2 = blue badge object reference only
@image3 = Central Square layout reference only
```

OpenArt-facing prompt her image'ın rolünü açıkça belirtmelidir.

Doğru wording:
```
Use @image1 as the exact first frame and only continuity source.
Do not reinterpret @image1.
The shot must begin from @image1.

Use @image2 only as the visual reference for the blue badge design.
Do not use @image2 as the first frame.
Do not copy @image2 camera, background, lighting, scale, or composition.
Only use @image2 to preserve the badge's shape, colour, texture and identity.

Use @image3 only as the environment layout reference.
Do not replace @image1 with @image3.
Do not reset the camera to match @image3.
Only use @image3 to preserve the canon layout if already compatible 
with @image1.
```

Yanlış:
- Birden fazla image yüklemek ama amacını açıklamamak.
- OpenArt'ın hangi image'ın first frame olduğuna karar vermesine izin vermek.
- Bir prop reference image'ını object-only olarak tanımlamamak.
- Bir karakter image'ını kullanıp yanlışlıkla shot kompozisyonunu resetletmek.
- Bir ortam reference'ı kullanıp kamerayı farklı bir açıya atlatmak.
- "Bu referansları kullan" demek ama image rollerini atamamak.

Hard kural:
`@image1` continuity-linked shot'larda her zaman önceliklidir.
`@image1` şunları tanımlar:
- First frame
- Camera angle
- Character position
- Character scale
- Lighting
- Colour grading
- Visible environment
- Composition

Diğer image'lar `@image1`'i override etmemelidir (prompt açıkça söylemediği sürece).

Object reference kuralı:
Eğer `@image2` object reference olarak kullanılıyorsa, nesne sadece `@image1` dünyasında mantıklı olduğu yere yerleştirilmelidir.
`@image2`'nin yeni bir sahne yaratmasına izin verme.
`@image2`'nin kamerayı değiştirmesine izin verme.
`@image2`'nin farklı bir lighting stili getirmesine izin verme.
`@image2`'nin ilgisiz arka plan detayları eklemesine izin verme.

Planning kuralı:
Eğer sonraki bir shot `@image1`'de görünmeyen bir objeye ihtiyaç duyuyorsa, surprise generation'a güvenme.
Ya:
1. Daha önceki bir kurulum shot'ını revize et ki nesne zaten orada tohumlanmış olsun, veya
2. Ayrı bir object reference image sağla ve onu object-only olarak tanımla.

Ama `@image2` ile bile, nesne kontrollü bir şekilde tanıtılmalıdır.
Diyalog sırasında late object spawning'a izin verme.

OpenArt-facing wording (multi-image shot'lar için):
```
Reference setup:
@image1 = exact first frame continuity source.
@image2 = [object / character / prop / environment] reference only.

Use @image1 as the exact first frame and main visual continuity source.
@image1 has priority over all other images for camera, lighting, 
composition, character scale and environment.

Use @image2 only to preserve the design of [specific object].
Do not use @image2 as the first frame.
Do not copy @image2 background, camera angle, lighting or composition.
Do not let @image2 override @image1.
```

Negative prompt additions:
```
wrong reference priority, image2 overriding image1, 
prop reference changing camera, object reference becoming new scene, 
environment reference replacing continuity frame, reference image mix-up, 
wrong first frame, copied reference background, 
copied object-reference composition, camera reset from reference image, 
lighting copied from wrong reference, scale copied from wrong reference
```

QA kuralı:
Üretimden önce kontrol et:
- `@image1` first frame continuity source olarak net mi?
- Her yüklenen image'ın tanımlı bir rolü var mı?
- İkincil image `@image1`'i yanlışlıkla override edebilir mi?
- Object reference sadece object identity için mi kullanılıyor?
- Prompt, secondary image'lardan NEYİ kopyalamayacağını söylüyor mu?
- Daha önce tohumlanması gereken eksik bir gelecek hikaye objesi var mı?

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

### Camera Stability (§18 — Global Camera Stability Rule):
- [ ] Locked camera ise prompt açıkça "Locked camera only. No pan. No zoom. No push-in. No pull-back. No camera movement. No reframing. No angle change. No reveal." içeriyor.
- [ ] Prompt'ta "or minimal soft follow", "if needed", "gentle follow", "slight camera adjustment", "small cinematic movement" gibi belirsiz kamera dili YOK.
- [ ] Kamera hareketi varsa tek, adı net verilmiş, basit ve yavaş bir hareket (ör. "Slow left-to-right pan only.") ve §18'in 5 koşulunun tümü sağlanıyor.
- [ ] Kamera hareketli bir objeyi (yaprak, kelebek, rüzgârla hareket eden prop) takip etmiyor; hareketli objeler mevcut kompozisyon içinde kalıyor.
- [ ] Kamera shot boyunca ilk frame açısına/yüksekliğine/mesafesine/framing'ine kilitli kalıyor; sonradan yeni bir açıya kaymıyor.

### Character Motion:
- [ ] Karakterler doğal preschool-safe hareketle canlı görünüyor.
- [ ] Diyalog görsel aksiyonla destekleniyor.
- [ ] Static talking pose yok.
- [ ] Frozen character performance yok.

### No Idle Opening / Immediate Life (§4A):
- [ ] Shot ilk frame'den canlı başlıyor (frame-one motion belirtilmiş).
- [ ] İlk onaylı jest ilk 1 saniye içinde başlıyor (prompt'ta yazılı).
- [ ] Diyalog ilk 1–2 saniye içinde başlıyor (veya shot açıkça "silent" olarak işaretli).
- [ ] Silent idle opening / frozen opening / empty opening seconds yok.
- [ ] Delayed dialogue / delayed gesture / delayed wave / delayed nod yok.
- [ ] Prompt sadece "No long pause" yazmıyor; ölçülebilir zamanlama satırlarını içeriyor.

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
From frame one (No Idle Opening / Immediate Life Rule, §4A):
- motion from frame one (subtle breathing, blinking, warm expression)
- first approved gesture begins within the first 1 second
- dialogue begins within the first 1–2 seconds (unless explicitly a silent shot)
- no silent idle opening, no frozen opening, no delayed dialogue

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

### Camera Stability (§18 — Global Camera Stability Rule)
```
- locked camera by default; camera locked to the approved first frame (angle, height, distance, framing, composition)
- if the shot is locked, the OpenArt-facing prompt must state:
  "Locked camera only. No pan. No zoom. No push-in. No pull-back. No camera movement. No reframing. No angle change. No reveal."
- no vague camera language ("or minimal soft follow", "if needed", "gentle follow", "small cinematic movement")
- camera does not follow leaves, butterflies, wind-driven props or any moving object
- camera movement allowed ONLY if it is part of the story beat, explicitly written here, named clearly, simple/slow/readable, and does not create an unintended reveal
- if a move is required, replace the locked-camera line with a single named move only (e.g. "Slow left-to-right pan only.")
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
camera pull-back, wider first frame, recomposed scene, new establishing shot, camera reset, changed camera angle, changed lens, camera tracking, pan, tilt, zoom, push-in, pull-back, reframing, dolly, soft follow, gentle follow, camera chase, camera following object, camera inventing movement, sudden camera angle change, surprise reframing, unscripted reveal move, widening reset, wide shot turning into close-up, cinematic camera improvisation, camera reacting to moving object
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

### Idle Opening / Timing (§4A):
```
long silent pause, delayed dialogue, delayed speech, delayed gesture, delayed wave, delayed nod, waiting before action, idle pose, frozen opening, no movement at start, silent hold, empty opening seconds, late speech, late gesture, long establishing hold, motion starts late, dialogue starts late
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

---

## 16. Video Production Preflight System

Her OpenArt video üretiminden ÖNCE preflight check yapılmalıdır.

Detaylar için: `00-CORE/19_VIDEO_PRODUCTION_PREFLIGHT_SYSTEM.md`

Ana kural:
Bir shot prompt'u sadece `@image1` görsel olarak destekliyorsa geçerlidir.
OpenArt'tan onaylı frame'in desteklemediği hiçbir şeyi keşfetmesini isteme.

Her shot için Shot Contract yazılmalı ve Preflight Checklist'ten geçirilmelidir.

Preflight Checklist'in 20 maddesi:
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
12A. Shot frame-one motion, ilk 1 sn içinde ilk jest ve ilk 1–2 sn içinde diyalog belirtiyor mu (No Idle Opening / Immediate Life Rule §4A)? Prompt sadece "No long pause" yazıyorsa NOT READY.
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

## 17. Pointing and Gaze Target Lock

> **Sorun türü: direction / target ambiguity.**
> Model karakterin bir şeyi işaret ettiğini anlıyor ama neyi işaret ettiğini net
> bağlamıyor; diğer karakterin nereye bakacağını da serbest yorumluyor. Sonuç:
> boşluğa işaret etme, uyumsuz bakış yönleri, okunamayan hikaye beat'i.
>
> Bu sorun tek başına "gesture" sorunu değil, üç şeyin birleşimidir:
> **gesture direction + eye-line direction + target visibility.** Biri eksik
> olduğunda model boşluğu kendi kafasına göre doldurur.

### Required Target Definition

Bir karakter bir şeyi işaret ettiğinde, sunduğunda, fark ettiğinde veya dikkat
yönlendirdiğinde, hedef açıkça kilitlenmelidir. Her pointing / showing / looking
beat'i için shot prompt'u şunları tanımlamalıdır:

1. **Who initiates** — hangi karakter işaret ediyor / bakıyor / sunuyor
2. **What the target is** — tam obje, yer, kapı, yatak, ağaç, burrow entrance vb.
3. **Where the target is in the frame** — screen-left / screen-right / center / behind character / foreground / background
4. **Whether the target is visible on screen** — görünürse net okunabilir olmalı; görünmüyorsa prompt bunun kasıtlı olarak off-screen olduğunu açıkça söylemeli

### Alignment Requirement

Bir karakter bir hedefe işaret ediyorsa, şunların hepsi aynı hedefe hizalanmalıdır:
- pointing hand / finger direction
- head direction
- eye line
- shoulder direction
- torso / upper body orientation

İkinci bir karakter bu işarete tepki veriyorsa, o karakter de aynı hedefe bakmalıdır
(script açıkça aksini söylemedikçe).

### Full-Body Orientation Toward the Target

> **Sadece "points" demek yetmez; sadece gaze de yetmez.** Karakterin hedefe
> nasıl yeniden yöneldiği (reorient) açıkça yazılmalıdır. Model niyeti anlar ama
> blocking / staging / orientation'ı biz kilitlemezsek kolaya kaçar.

Bir karakter bir hedefe işaret ettiğinde / fark ettiğinde / sunduğunda,
orientation açık olmalıdır. Sadece gaze'e güvenme; şunları ayrı ayrı belirt:
- torso direction
- shoulder direction
- head direction
- eye line
- arm / finger direction

Hedef Mimi'nin evi / burrow entrance / doorway ise:
- işaret eden karakter **gövdesini** eve döndürmeli
- kafası ve gözleri de eve bakmalı
- işaret eden kolu net şekilde evi göstermeli
- tepki veren karakter de aynı eve dönmeli
- her iki karakter de görünür şekilde **eve dönük** okunmalı, rastgele boşluğa değil

**Example (orientation):**
"Kiko turns her body toward Mimi's burrow entrance and points directly at it. Her
eyes, head, shoulders, and arm all align toward the burrow entrance. Mimi also turns
her body and head toward the burrow entrance, following Kiko's indication. Both
characters visibly read as oriented toward the home."

### Direction + Orientation Lock (kısa versiyon)

```text
Whenever a character points toward a target, the prompt must explicitly state that:
- the target is named
- the target is visible in frame whenever possible
- the pointing character turns toward the target
- the reacting character also turns toward the same target
- hand, head, eyes, shoulders, and torso all align toward that target

Do not allow mismatched orientation. Do not allow characters to point one way while
looking another way. Do not allow the reacting character to keep facing an unrelated
direction.
```

### No Ambiguous Pointing

"Generic pointing" yasak. Karakter boşluğa, rastgele çimene, kamera yönüne veya
alakasız background'a işaret edemez.

### Visible Target Preference

Mümkün olduğunda işaret edilen obje aynı frame içinde görünür kalmalı. Beat
tanıma (recognition) üzerine kuruluysa, hedef görünür ve kompozisyon olarak net olmalı.

### End-of-Shot Lock

Shot bir pointing beat'i üzerinde bitiyorsa, son 1–2 saniye okunabilir yönü korumalıdır:
- pointer hâlâ hedefe yönelik
- hedef hâlâ net konumda
- tepki veren karakter hâlâ hedefe bakıyor

### Example

**Bad:** "Kiko points toward the burrow."

**Good:** "Kiko stands screen-right under the tree and points diagonally screen-left
toward Mimi's glowing burrow entrance, which remains clearly visible in frame.
Kiko's eyes, face, and arm all align toward the burrow entrance. Mimi turns her
head and eyes toward the same burrow entrance."

### Directional Action Rule (shot'lara koymalık kısa versiyon)

```text
Any time a character points, looks, or presents something, the exact target must be
named and visually anchored in the frame. The prompt must explicitly state:
- who is pointing
- what the target is
- where the target is on screen
- that the pointer's hand, eyes, face, and torso all orient toward that target
- that any reacting character also looks toward that same target

Never allow vague or generic pointing. Never let characters point toward empty space
or look in mismatched directions. Prefer keeping the target visible in the same frame.
```

### Micro-sentence pattern (prompt içine)

```text
At the end of the shot, [Character A] notices [named target] and turns toward it,
then points directly at it. [Character A]'s arm, head, eyes, shoulders, and torso
all align toward the [target]. The [target] remains visible in frame. [Character B]
follows the cue and also turns toward the same [target]; [Character B]'s head, eyes,
and body reorient toward the [target] as well. Both characters clearly read as facing
the [target]. Do not let either character point or look toward empty space or an
unrelated off-screen direction.
```

> Bkz. QA: `00-CORE/MASTER_QA_CHECKLIST.md` ve `00-CORE/SCENE_QA_CHECKLIST.md`
> "Pointing / Gaze Direction" kontrolü.

---

## 18. Global Camera Stability Rule (No Surprise Camera Change Rule)

> **Kısa ad: GLOBAL CAMERA STABILITY RULE / NO SURPRISE CAMERA CHANGE RULE.**
> Bu kural zorunludur ve gelecekteki TÜM Pompom Hills shot dokümanlarına ve OpenArt-facing
> prompt'larına uygulanır. Bu tek seferlik bir Shot 03 düzeltmesi değildir; kalıcı bir global
> production kuralıdır.
>
> **Neden:** OpenArt, prompt açıkça kamera hareketi istemese bile kendi kafasına göre kamera
> hareketi, ani açı değişimi, sürpriz reframing veya hareketli bir objeyi takip (camera-follow)
> uydurabiliyor. Bu, preschool storytelling için okunabilir, sakin ve stabil kompozisyonu bozar.
> Bu kural bunu prompt tasarımıyla kalıcı olarak engeller.

### The Rule

For all Pompom Hills shots, the camera must stay locked unless a camera move is explicitly
required by the story beat and explicitly written in the shot document.

OpenArt must never invent camera movement on its own.

The approved first frame defines the camera angle, camera height, camera distance, framing, and
composition lock for the shot. The video must not drift into a new angle later in the shot.

Characters may move inside the frame, but the camera must not react unless the shot explicitly
says so.

### What "Locked Camera" Means

If a shot is written as **locked camera**, that means:

- no pan
- no tilt
- no zoom
- no push-in
- no pull-back
- no dolly
- no tracking
- no soft follow
- no camera chase
- no reframing
- no angle change
- no widening reset
- no reveal move
- no sudden composition change

The camera angle, camera height, camera distance, framing, and composition are all locked to the
approved first frame for the entire duration of the shot.

### Moving Objects Do Not Move the Camera

Objects such as leaves, butterflies, wind-driven props, or small moving elements must stay inside
the existing composition. The camera must not follow them.

If an object or character would require the camera to move in order to stay visible, then the shot
must be redesigned so the action fits inside the existing frame. The environment and staging adapt
to the locked camera — the camera does not adapt to the action.

### Preschool Storytelling Preference

For preschool storytelling, prefer:

- locked camera
- simple readable staging
- motion inside frame
- no dramatic camera invention
- no cinematic improvisation by OpenArt

### When Camera Movement Is Allowed

Camera movement is allowed only if ALL of the following are true:

1. the movement is part of the story beat
2. the movement is explicitly written in the shot document
3. the movement type is named clearly
4. the movement is simple, slow, and readable
5. the movement does not create a reveal that changes story meaning unintentionally

If any one of these five is not satisfied, the shot is locked camera by default.

### Prompt Wording Rule

Shot prompts must never use vague camera language such as:

- "or minimal soft follow"
- "if needed"
- "unless necessary"
- "gentle follow"
- "slight camera adjustment"
- "small cinematic movement"

Instead, prompts must be explicit:

- "Locked camera only."

or, if a camera move is truly required by the story beat and written in the shot document:

- "Slow left-to-right pan only."
- "Very slow push-in only."

etc. The named movement must be the only movement allowed, and every other movement type stays
forbidden.

### Failure Pattern (Recurring Issue To Prevent)

Without this rule, OpenArt may otherwise:

- suddenly change camera angle
- move closer to the character
- start following a moving object
- turn a wide shot into a close-up
- reframe toward a tree/object
- create a reveal that was never scripted

These are production errors and must be prevented by prompt design, not fixed after the fact.

### Implementation Instruction

This new rule must be reflected in all future OpenArt shot prompts.

Whenever a shot is intended to stay visually stable, the OpenArt-facing prompt should explicitly
say:

```text
Locked camera only. No pan. No zoom. No push-in. No pull-back. No camera movement. No reframing. No angle change. No reveal.
```

If the story beat genuinely requires movement, replace this line with a single named, simple, slow
move (e.g. "Slow left-to-right pan only." or "Very slow push-in only.") and keep every other
camera movement type forbidden.

### Negative Prompt Additions (Camera Stability)

```text
sudden camera angle change, surprise reframing, unintended camera movement, camera inventing movement, camera following object, camera chasing character, soft follow, gentle follow, camera drift to new angle, unscripted push-in, unscripted pull-back, unscripted zoom, unscripted pan, unscripted tilt, unscripted dolly, unscripted tracking, wide shot turning into close-up, close-up turning into wide shot, reframe toward tree, reframe toward object, unscripted reveal move, widening reset, cinematic camera improvisation, camera reacting to moving object
```

### Relationship To Other Camera Rules

This rule builds on and does not replace: §2 First-Second Continuity Hold Rule, §3 Stable
Composition vs Frozen Scene Rule, and the Camera Rules / Global OpenArt Continuity Locks in
`00-CORE/17_VIDEO_GENERATION_STANDARD.md`. A locked camera still allows natural character motion
inside the frame (§4, §4A). "Locked camera" locks the camera, not the characters.
