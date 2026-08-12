# Shorts Smart Reframe Standard

> **Tek yetkili kapsam:** Bitmiş bir 16:9 master videonun, içeriği yeniden üretmeden
> 1080x1920 (9:16) dikey videoya dönüştürülmesi.
>
> **Ana karar kuralı:** **Static when readable, adaptive when necessary.**

---

## 1. Kapsam

Bu standart, mevcut ve onaylanmış bir 16:9 videonun 9:16 dikey sürümünü üretirken
uygulanır. Kör merkez crop yasaktır. Kadraj, her hikâye beat'inin anlamına göre analiz
edilir; yalnızca gerekli olduğunda yumuşak biçimde yeniden konumlandırılır.

Bu işlem:

- yeni sahne veya yeni görüntü üretmez,
- diyaloğu, kurgu zamanlamasını ve ses senkronunu değiştirmez,
- müzik veya yeni ses eklemez,
- kaynak videodaki aksiyonu yeniden sıralamaz,
- yalnızca crop, reframe ve gerektiğinde çok hafif sanal pan/zoom uygular.

Klip seçimi, hook seçimi veya uzun master'dan 30–60 saniyelik bölüm çıkarma bu
standardın kapsamında değildir. Bunlar ayrı bir editoryal seçim workflow'u gerektirir.

---

## 2. Zorunlu Çıktı

| Alan | Kural |
|---|---|
| En-boy oranı | 9:16 dikey |
| Çözünürlük | 1080x1920 |
| Görsel kaynak | Yalnızca onaylanmış 16:9 master |
| Ses | Orijinal ses ve senkron korunur |
| Diyalog | Metin, sıra ve zamanlama değişmez |
| Yeni içerik | Yasak |
| Hareket | Yalnızca anlatı için gerekli, yumuşak crop/pan/zoom |

Orijinal master değiştirilmez. Dikey çıktı ayrı dosya olarak üretilir.

---

## 3. Karar Hiyerarşisi

Her anda aşağıdaki sıra kullanılır:

1. O an önemli olan her şey 9:16 içinde rahatça okunuyorsa crop sabit tutulur.
2. Konuşmacı ana odaksa aktif konuşmacı tercih edilir.
3. Fiziksel aksiyon anlamı taşıyorsa aksiyon konuşmacıdan önce gelir.
4. Dinleyicinin tepkisi eşit derecede önemliyse iki karakter birlikte korunur.
5. Kitap, pebble, petal, flower, river veya stepping stones gibi kritik hikâye nesnesi
   beat'i taşıyorsa nesne korunur.
6. Birden fazla unsur eşit derecede önemliyse agresif takip yerine dengeli grup kadrajı
   tercih edilir.
7. Her şeyi göstermek mümkün değilse geometrik merkeze değil, en açık hikâye anlamına
   öncelik verilir.

Odak önceliği:

1. aktif konuşmacı,
2. ana fiziksel aksiyon,
3. ana tepki karakteri,
4. kritik hikâye nesnesi,
5. dengeli grup kompozisyonu.

Bu sıra mekanik değildir. Örneğin konuşma sırasında kitabın sayfasında gerçekleşen reveal
hikâyeyi taşıyorsa kadraj konuşan yüz yerine reveal'i koruyabilir.

---

## 4. Hareket Dili

- Mümkün olan en uzun süre crop'u sabit tut.
- Yalnızca anlam veya okunabilirlik kaybolacaksa hareket et.
- Hareketler yavaş, yumuşak, ease-in/ease-out ve kasıtlı olmalı.
- Konuşmacılar arasında sürekli ileri-geri gidilmez.
- Birkaç karede bir mikro düzeltme yapılmaz.
- Jitter, hunting, snap-pan ve salınım yasaktır.
- Gereksiz zoom yapılmaz; bağlamı kaybettirecek ölçüde yaklaşılmaz.
- Okunabilirliği crop kaydırmasıyla korumak mümkünse zoom yerine reframe kullanılır.
- Kaynakta blur, defocus, dissolve veya başka bir transition varsa bu sırada crop sabit
  veya neredeyse sabit tutulur. Kaynak transition'a ek dikkat dağıtıcı hareket eklenmez.

---

## 5. Korunacak Görsel Bilgi

Anlatı açısından önemli oldukları sürece şunlar crop dışında bırakılamaz:

- yüzler ve gözler,
- aktif konuşmacının ağzı,
- anlamlı el, kanat veya beden jestleri,
- ana tepki karakteri,
- açık kitap ve ilgili sayfa içeriği,
- hikâyeyi taşıyan pebble, petal, flower, river, stepping stones veya başka nesne,
- aksiyonun başlangıç ve sonuç ilişkisini anlatan çevresel bağlam.

Doğal headroom korunur. Önemli yüz, çene, alın, el veya nesneler rahatsız edici bir
noktadan kesilmez. Crop, shot'ın duygusal anlamını yok edemez.

---

## 6. Uygulama Workflow'u

1. Master videonun çözünürlük, FPS, süre, ses kanalı ve codec bilgisini doğrula.
2. Shot sınırlarını ve mevcut transition aralıklarını çıkar.
3. Her shot içinde konuşma, aksiyon, tepki ve kritik nesne beat'lerini zaman kodlarıyla
   işaretle.
4. Her beat için en az başlangıç, orta ve bitiş karesini görsel olarak kontrol et.
5. Önce tek bir sabit crop'un beat'i okuyup okumadığını test et.
6. Okuyorsa crop'u sabit tut; okumuyorsa en az sayıda keyframe ile yeni crop merkezi belirle.
7. Hareket gereken komşu keyframe'ler arasında yumuşak easing kullan.
8. Transition aralıklarında crop hareketini dondur veya minimuma indir.
9. 1080x1920 çıktıyı üret; orijinal sesi değişmeden veya senkronu bozmayan yeniden encode
   ile taşı.
10. Tam videoyu baştan sona izleyerek QA yap. Otomatik subject tracking tek başına onay
    sayılmaz.

Crop merkezi hiçbir zaman kaynak görüntünün dışına çıkamaz. X koordinatı kaynak ve hedef
ölçeğine göre hesaplanır; episode'a özgü sabit X değerleri global varsayım olarak kullanılmaz.

---

## 7. QA ve Red Kuralları

### Zorunlu QA

- [ ] Çıktı 1080x1920 ve 9:16 mı?
- [ ] Master video değişmeden duruyor mu?
- [ ] Orijinal audio sync korunuyor mu?
- [ ] Her konuşmacının ağzı gerektiği anda görünür mü?
- [ ] Ana aksiyon ve kritik nesneler anlaşılır mı?
- [ ] Tepki beat'leri duygusal anlamını koruyor mu?
- [ ] Grup kadrajlarında gereksiz speaker hunting yok mu?
- [ ] Transition sırasında ek reframe dikkat dağıtmıyor mu?
- [ ] Pan/zoom sayısı mümkün olan minimumda mı?
- [ ] Baştan sona jitter, snap veya mikro düzeltme yok mu?

### Kesin Red

- Tüm videoya uygulanan kör merkez crop,
- aktif konuşmacının ağzının kesilmesi,
- hikâyeyi taşıyan nesnenin crop dışında kalması,
- sürekli sağ-sol speaker takibi,
- ani snap-pan veya hızlı punch-in,
- kaynak transition sırasında ek kamera hareketi,
- yeni görüntü, yeni sahne, yeni müzik veya değiştirilmiş diyalog,
- duygusal tepkiyi veya aksiyon-sonuç ilişkisini kaybettiren crop.

---

## 8. Codex İçin Paste-Ready Görev Prompt'u

```text
TASK:
Convert the provided approved 16:9 finished master video into a 1080x1920 9:16
vertical version using intelligent, story-aware reframing.

SOURCE AUTHORITY:
The approved finished master is the only visual and audio source. Do not alter the
master file. Create a separate vertical output.

PRESERVE:
- original edit and full source timing
- original dialogue, ambience and audio sync
- story continuity and emotional intent
- existing transitions exactly as they occur

DO NOT:
- blindly center-crop the entire video
- invent, generate or reorder shots
- add music, dialogue, sound effects, overlays or new visual content
- use fake camera shake, snap-pans, fast punch-ins or constant reframing
- crop away the active speaker's mouth, meaningful reactions or critical story objects

DECISION RULE:
Static when readable, adaptive when necessary.

For every story beat, first test whether all important content fits comfortably in a
stable 9:16 crop. If it does, hold that crop. If meaning or readability would be lost,
reframe smoothly toward the most important subject in this order: active speaker, main
physical action, main reaction character, critical story object, balanced group
composition. This hierarchy is story-aware: if an action or reveal carries more meaning
than the speaker, preserve the action or reveal.

Prefer a stable two-shot or group frame when multiple subjects are equally important.
Do not hunt back and forth between speakers. Use the fewest crop keyframes necessary.
All movement must be slow, eased and intentional, with no jitter, oscillation or
micro-corrections. Avoid zoom unless a very gentle zoom is necessary for readability;
prefer lateral reframing over digital zoom.

During blur, defocus, dissolve or other transitions already present in the master, keep
the crop stable or nearly stable. Do not compete with the source transition.

Protect faces, eyes, the active speaker's mouth, meaningful hands or wing gestures,
important reactions, book contents and active narrative objects such as the pebble,
petal, flower, river or stepping stones. Maintain natural headroom and avoid awkward
cuts through important faces, hands or props.

WORKFLOW:
Analyze shot boundaries and story beats; inspect representative frames; prepare a
time-coded crop plan; render a separate 1080x1920 output; preserve audio sync; then watch
the complete result and verify every movement and hold. Automatic subject tracking alone
is not final approval.

QUALITY TARGET:
The final vertical version must feel smooth, readable, calm but responsive, cinematic on
mobile, visually intentional and faithful to the approved master.
```

---

## 9. İlgili Dosyalar

| Dosya | Rol |
|---|---|
| `SHORTS_PRODUCTION_STANDARD.md` | Genel Shorts format ve kalite şartları |
| `SHORTS_SEGMENT_CROP_WORKFLOW.md` | Shot-level segment crop tekniği ve uygulanmış örnekler |
| `TOOLS/make_short_vertical.sh` | Yalnızca sabit merkez crop'un önceden doğrulandığı basit sahneler için araç |
| `../07_ARDAS_STORIES/00_GLOBAL_RULES/SHORTS_CROP_AND_SEGMENT_WORKFLOW.md` | Arda's Stories uygulama notları |

---

*Oluşturulma: 12 Ağustos 2026 — finished-master smart narrative reframing kuralı kilitlendi.*
