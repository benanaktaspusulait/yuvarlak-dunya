# CONTINUITY RULES — PomPom Hills v2.1

---

## Amaç

Bu dosya süreklilik ile ilgili tüm kuralları içerir. Karakter, mekan, kamera, ışık, ses ve devam sahneleri kuralları burada tanımlıdır.

---

## 1. Character Continuity

Karakter görünümü her shot'ta aynı kalır.

| Alan | Kural |
|---|---|
| Saç | Değişmez |
| Gözler | Değişmez |
| Yüz | Değişmez |
| Vücut | Değişmez |
| Kıyafet | Değişmez |
| Renkler | Değişmez |
| Ölçek | Değişmez |

Karakter asla yeniden tasarlanmaz.

Referans: `11-DOCS/04_CHARACTER_BIBLE.md`

---

## 2. World Continuity

Mekan her shot'ta aynı kalır.

- Mimari
- Ağaçlar
- Çiçekler
- Yollar
- Banklar
- Lamba direkleri
- Işık

Mekan asla yeniden tasarlanmaz.

Referans: `11-DOCS/05_WORLD_BIBLE.md`, `POMPOM_HILLS_PRODUCTION/02_WORLDS/`

---

## 3. Camera Continuity

Episode planı onaylı kamera dilini belirler.

Fresh shot'lar temiz edit içinde yeni ve yüksek kaliteli kompozisyon kullanabilir. Linked
shot'lar yalnızca önceden planlandığında önceki final frame'in kamerasını birebir sürdürür.

Ani kamera değişiklikleri yapılmaz.

| Kural | Değer |
|---|---|
| Lens sıçraması | Yasak |
| Varsayılan lens | 35-50mm |
| Kamera yüksekliği | 0.70-1.10 m |
| Dutch angle | Yasak |
| Fisheye | Yasak |
| Shaky cam | Yasak |

---

## 4. Lighting Continuity

Işık her shot'ta aynı kalır.

| Alan | Kural |
|---|---|
| Yön | Değişmez |
| Renk | Değişmez |
| Yoğunluk | Değişmez |
| Gölge yönü | Değişmez |
| Gölge opaklığı | %25 altında |
| Gece değerleri | Asla siyah değil |

Zaman dilimi (sabah/öğle/akşam/gece) sahne boyunca tutarlıdır.

---

## 5. Sound Continuity

Ambiyans döngüleri mekanla eşleşir.

Karakter sesi tüm speaking shot'larda aynı kalır.

Voice continuity için:

- aynı voice identity
- aynı pitch
- aynı timbre
- aynı speaking speed
- aynı pronunciation
- aynı accent
- aynı recording quality
- aynı emotional warmth

Önceki shot mevcutsa, önceki shot sesi voice reference olarak kullanılır.

Yasak sesler hiçbir sahnede kullanılmaz:
- Bağırma
- Çığlık
- Patlama
- Motor
- Siren
- Agresif müzik

Referans: `AUDIO_GUIDE.md`

---

## 6. Time Continuity

Günlük akış: Sabah → Öğle → Akşam → Gece

Bir bölüm içinde zaman geriye akmaz.

Geçişler yumuşak ve okunabilirdir.

---

## 7. Character Interaction

- Aynı anda kadrajda en fazla 3-4 karakter
- Karakterler arası 18-24 birim boşluk
- Etkileşim bölgeleri mekanın bible'ından alınır

---

## 8. Character Entrance Continuity

Karakterler aniden belirmez.

Doğal yollarla tanıtılır:
- Küçük silüet
- Parçalı görünüm
- Yumuşak ses
- Doğal kamera hareketi

---

## 9. Reference Frame and Quality-Reset Workflow

Her shot üretimden önce şu modlardan biriyle etiketlenir:

- `FRESH QUALITY-RESET SHOT`
- `LINKED CONTINUITY SHOT 1`
- `LINKED CONTINUITY SHOT 2`
- `LINKED CONTINUITY SHOT 3 — EXCEPTIONAL MAXIMUM`

Fresh shot canonical World ve karakter referanslarından, shot'a özel temiz bir başlangıç
kompozisyonuyla üretilir. Bu varsayılan moddur.

Exact generated final-frame linkage yalnızca fiziksel/uzamsal devamlılık gerçekten gerekliyse
planlanır. Linked kaynak, önceki shot'ın özgün generated final frame'i olmalı ve identity,
world, colour, contrast, sharpness, scale ve prop QA'dan geçmelidir. Normal zincir en fazla iki,
istisnai zincir en fazla üç shot'tır; ardından canonical referanslardan zorunlu fresh reset gelir.

Her shot kendi ana aksiyonunu tamamlar ve son 1–2 saniyeyi stabil, grounded bir final anchor ile
bitirir. Bir clean cut, progressive kalite kaybı taşıyan seamless devamlılıktan üstündür.

### 9.1 First Frame Master Lock

Yalnızca linked shot'larda ilk görünen frame, onaylı continuity reference frame'den ayırt
edilemez olmalıdır.

Benzer değil.
Yakın değil.
Aynı.

Required wording:

```text
Treat @image1 as the complete visual master reference.
Preserve not only framing, but also colour identity, lighting identity, exposure, white balance, atmosphere, environment identity, character proportions, and character performance.
For this explicitly linked shot, the viewer must not perceive a shot boundary.

The first visible frame must be visually indistinguishable from @image1.
Not similar. Not close. Identical.

Only after the first frame matches perfectly may animation begin.
```

---

## 10. Camera Scale Continuity

Kamera hareket edebilir.

Dünya değişmez.

Pull-back ≠ yeni establish shot.

Kamera yalnızca mevcut alanın içinde hareket eder.

Yeni manzara oluşturulmaz.

Yeni ağaç oluşturulmaz.

---

## 11. World Identity Lock

Her önemli mekan kalıcı bir görsel varlıktır.

| Mekan | Kural |
|---|---|
| Opa's Tree | Her zaman aynı ağaç |
| Stone Hill | Her zaman aynı tepe |
| Central Square | Her zaman aynı meydan |
| Kiko's Home | Her zaman aynı ev |
| Mimi's Burrow | Her zaman aynı yuva |

**Kural:** Mekanlar film seti gibidir.

### 11.1 No Generic Worlds Rule

Tekrar eden bir mekan asla genel (generic) ifadelerle tanımlanmaz.

Şunları YAZMA:
- "a big tree" / "büyük ağaç"
- "a tree" / "ağaç"
- "a hill" / "tepe"
- "a village" / "köy"

Bunun yerine **kurulu (established) mekanın adını** kullan ve AI'a kimliğini
korumasını söyle (örn. "Opa's Tree" ve korunacak öğeler listesi).

Tekrar eden mekanlar, her seferinde yeniden üretilen ortamlar değil,
**kalıcı film setleri** gibi ele alınır.

Her Opa's Tree shot'ı şunları korur:
- gövde şekli (trunk shape)
- taç silüeti (canopy silhouette)
- okuma platformları (platforms)
- ağaç ev açıklığı (tree house opening)
- fener yerleşim stili (lantern placement)
- çevredeki tepe (surrounding hill)
- kurulu gece atmosferi (established night atmosphere)

---

## 12. Scene Continuation Template

Önceki sahnenin son karesinden devam eden sahneler için bu şablon kullanılır:

```text
## Scene Continuity

This shot takes place immediately after the previous shot.

Remain inside the exact same [LOCATION].

Remain inside the exact same room.

Do NOT generate a new interior.

Do NOT redesign the room.

Keep the room layout exactly the same.

Keep all walls, windows, doors, furniture, decorations, shelves, fireplace, floor, ceiling, rugs and props in exactly the same positions.

Maintain identical architecture, colors, lighting, atmosphere and scale.

Maintain the same time of day.

Maintain the same weather.

Maintain the same visual style.

The only changes allowed are:
- camera position
- camera angle
- framing
- [CHARACTER]'s pose
- [CHARACTER]'s facial expression
- [CHARACTER]'s animation
```

---

## 13. Video Continuation Rules

Devam referansı sağlandığında (örn. @image2), bu görsel bir önceki videonun SON KARESİdir.

İlham görseli değildir.

Stil referansı değildir.

Mood board değildir.

Frame 0 olarak davranılır.

### Camera Continuity

Yeni videonun ilk saniyesi aynen şu unsurlarla başlamalıdır:
- Camera angle
- Focal length
- Framing
- Composition
- Environment
- Lighting
- Character pose

Hiçbir zaman sahneyi yeniden başlatma.

Hiçbir zaman yeni establish shot oluşturma.

### Character Continuity

Karakter hareketini doğal olarak devam ettir.

İlk hareket, bir sonraki animasyon karesi gibi hissettirmelidir.

Aynen korunacaklar:
- Karakter pozisyonu
- Karakter pozu
- Karakter ifadesi
- Karakter ölçeği
- Karakter kıyafeti
- Karakter renkleri

### Environment Continuity

Mekanı yeniden tasarlama.

Objeleri taşıma.

Dünyayı yeniden oluşturma.

Işığı değiştirme.

Gölgeyi değiştirme.

Havayı değiştirme.

### Dialogue Continuity

Devam sahneleri, bir önceki videoda zaten söylenen diyalogları tekrar etmemeli.

Önceki sahne diyaloglarını ve son söylenen repliği kontrol et.

Önceki video zaten "Merhaba" gibi bir selamlama içeriyorsa, devam bir selamlama ile başlamamalı.

Örnek:
- Yanlış: Önceki: "Merhaba!" → Devam: "Merhaba! Ben Noah."
- Doğru: Önceki: "Merhaba!" → Devam: "Ben Noah. Yeni şeyler yapmayı seviyorum."

---

## 14. Yasak Olanlar

```
✗ Karakter yeniden tasarımı
✗ Mekan yeniden tasarımı
✗ Işık yönü değişimi
✗ Ani kamera hareketi
✗ Dünyayı yeniden oluşturma
✗ Yeni manzara ekleme
✗ Yeni obje ekleme
✗ Mevcut objeleri silme
✗ Dialogue tekrarı
✗ Platform-specific tag'ler reusable bible/core dosyalarında hardcode edilmemeli
✗ Dosya adları ("3.png")
```

Not: Shot promptlarında production tool'un verdiği continuity image tag'i (`@image1`, `@image2` gibi) Frame Lock için kullanılabilir. Yasak olan, bu tag'leri world/character bible veya reusable core asset tanımlarına sabitlemektir.

---

*Bu belge tüm süreklilik kuralları için tek kaynaktır.*
*Son güncelleme: 2 Temmuz 2026*
