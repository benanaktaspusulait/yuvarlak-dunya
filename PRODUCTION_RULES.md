# PRODUCTION RULES — Pompom Hills v2.1

Bu belge Pompom Hills'in **production pipeline** kurallarını tanımlar. Kamera, mekan, ışık,
ses, zaman sürekliliği ve karakter etkileşimi standartlarının yanı sıra, OpenArt üzerinde
yapılan kapsamlı testlerle doğrulanmış **production pipeline** kurallarını içerir.

> Bu bir prompt koleksiyonu değildir. Bu, bir animasyon stüdyosu production dokümanıdır.
> Tüm sahneler bu pipeline'ı paylaşır. Tutarlılık, güzellikten **her zaman** daha önemlidir.

İlgili dosyalar: `MASTER_PROMPTS.md`, `OPENART_WORLD_PROMPT_PACK.md`, `WORLD_BUILD_DESCRIPTION.md`,
`Environments/ENVIRONMENT_IMAGE_PROMPTS.md`, `NEGATIVE_PROMPTS.md`, `VARIABLES.md`.

---

## 1. GLOBAL PRODUCTION PHILOSOPHY

- Pompom Hills artık bir **production pipeline** olarak inşa edilmiştir.
- OpenArt bir görsel üretici (image generator) DEĞİLDİR. OpenArt bizim **production engine**'imizdir.
- Artık izole/tek seferlik prompt yazmıyoruz. Her prompt production pipeline'ı takip eder.
- **Consistency is ALWAYS more important than beauty.** (Tutarlılık her zaman güzellikten önemlidir.)
- **Production quality is ALWAYS more important than speed.** (Production kalitesi her zaman hızdan önemlidir.)

---

## 2. LOCKED PRODUCTION RULES

### 2.1 Environment LOCKED

- Environment **kilitlidir (LOCKED)**.
- Environment asla yeniden üretilmez (never regenerate).
- Environment asla yeniden tasarlanmaz (never redesign).
- Sahneler yalnızca **var olan dünyaların içine karakter yerleştirir** (insert characters only).

### 2.2 Character Appearance LOCKED

Karakter görünümü kilitlidir. Aşağıdakiler her sahnede **birebir aynı** kalmalıdır:

| Alan | Kural |
|---|---|
| Hair (saç) | Değişmez |
| Eyes (göz) | Değişmez |
| Face (yüz) | Değişmez |
| Body (vücut) | Değişmez |
| Clothes (kıyafet) | Değişmez |
| Colors (renkler) | Değişmez |
| Scale (ölçek) | Değişmez |

Referans: `CHARACTER_REFERENCE_GUIDE_v2.1.md`, `Color/COLOR_PALETTE_LOCK.md`, `VARIABLES.md`.

### 2.3 Giant Pompom Tree — Iconic Landmark LOCKED

Büyük Ponpon Ağaç (Giant Pompom Tree) ikonik bir landmark'tır. Aşağıdakiler **asla değişmez**:

| Alan | Kural |
|---|---|
| Shape (şekil) | Yuvarlak, kabarık taç — değişmez |
| Position (konum) | Central Square merkezinde — değişmez |
| Scale (ölçek) | 5-6 m, Opa'nın dalı 1.20 m — değişmez |
| Colors (renkler) | Taç #81C784, gövde #A1887F — değişmez |

> Ağaç asla kahverengi olmaz, asla yeniden şekillenmez, asla başka bir tepeye taşınmaz.

---

## 3. OPENART PRODUCTION RULES

OpenArt testleriyle doğrulanmış kurallar. İlgili her yerde uygulanır.

- **Environment Sheet'leri asla World reference olarak kullanma.**
- **World reference'lar yalnızca temiz render (clean render) içermelidir:**
  - Başlık yok (no titles)
  - Etiket yok (no labels)
  - Ok yok (no arrows)
  - Layout/şema yok (no layouts)
  - Çerçeve yok (no frames)
- **Her mekanın kendi bağımsız World'ü vardır** (each location = its own independent World).
- **Her World'ün kendi Hero Pack'i vardır:**

  | View | Açıklama |
  |---|---|
  | Hero View | Mekanın ikonik ana kompozisyonu |
  | Right View | Sağ profil |
  | Back View | Arka görünüm |
  | Top View | Kuş bakışı / üstten |

- **Sahne üretimi sırasında world'ler asla yeniden üretilmez.** Yalnızca karakter yerleştirilir.
- **OpenArt'a environment'ın LOCKED olduğunu açıkça söyle.**
- **Şunların yeniden tasarlanmasını açıkça yasakla:** mimari (architecture), ağaçlar (trees),
  çiçekler (flowers), yollar (paths), banklar (benches), lamba direkleri (lamp posts) ve
  landmark'lar (landmarks).

---

## 4. CAMERA & SCALE

- Environment **her zaman görsel kahramandır** (the visual hero). Karakterler ikincildir.
- Wide (geniş) kompozisyonlar tercih edilir.
- Sahne aksini gerektirmedikçe **varsayılan lens 35mm**'dir.
- **Eye-level** (göz hizası) kamera.
- Geniş **negative space** (boşluk) bırakılır.
- Karakterler kare içinde yaklaşık **%10–12** yer kaplar.
- İzleyici önce dünyayı, sonra karakteri fark etmelidir.
- Asla oversized (büyütülmüş) karakter üretme.

> Not: `MASTER_PROMPTS.md` bazı tanıtım (intro) sahnelerinde %18–20 kullanır. Standart
> production kuralı %10–12'dir; daha yüksek oran yalnızca bilinçli karakter tanıtımı içindir.

Kamera shot, yükseklik ve karakter oranı seçenekleri için `MASTER_PROMPTS.md` §4'e bakınız.

---

## 5. KNOWN OPENART FAILURE MODES

Aşağıdaki yaygın hatalara karşı korun. İlgili her yerde prompt'ları bu hataları açıkça
önleyecek şekilde güçlendir.

| # | Failure Mode | Koruma |
|---|---|---|
| 1 | Oversized characters | Ölçeği kilitle, %10–12 frame oranını belirt |
| 2 | Tiny environments | Environment = visual hero, wide shot |
| 3 | Regenerated architecture | "DO NOT redesign", environment LOCKED |
| 4 | Different trees | Ağaç şekli/rengi kilitli, redesign yasak |
| 5 | Different flower layouts | Çiçek yerleşimi kilitli, insert-only |
| 6 | Different lighting | `{lighting}` sabit, warm diffused daylight |
| 7 | Brown or reshaped Giant Pompom Tree | Landmark LOCKED: #81C784 taç, şekil sabit |
| 8 | Environment Sheet appearing inside the scene | World reference = clean render only |
| 9 | Random text or sign artifacts | Negative: text, watermark, random signs |
| 10 | Changed world layout | Layout/paths/object placement LOCKED |

Negative prompt blokları için `NEGATIVE_PROMPTS.md` → "OpenArt Production Failure Modes".

---

## 6. CONTINUITY & INTERACTION RULES

### 6.1 Camera Continuity

- Aynı mekanda ardışık sahnelerde kamera yüksekliği tutarlı tutulur (0.70–1.10 m).
- Lens sıçraması yapılmaz; varsayılan 35–50mm aralığında kalınır.
- Dutch angle, fisheye, shaky cam yasaktır.

### 6.2 Environment Continuity

- Bir mekanın layout'u, yol yerleşimi ve obje sayıları bölümler arasında değişmez.
- Object Inventory (obje sayıları) mekanın Environment Bible'ından alınır ve korunur.

### 6.3 Lighting Continuity

- Zaman dilimi (sabah/öğle/akşam/gece) sahne boyunca tutarlıdır.
- Gölge opaklığı %25 altında; gece değerleri asla siyah değildir.

### 6.4 Sound Continuity

- Ambiyans döngüleri mekanla eşleşir (bkz. ilgili Environment Bible → Soundscape).
- Yasak sesler (bağırma, çığlık, patlama, motor, siren) hiçbir sahnede kullanılmaz.

### 6.5 Time Continuity

- Günlük akış: Sabah → Öğle → Akşam → Gece (bkz. `WORLD_BUILD_DESCRIPTION.md` §8).
- Bir bölüm içinde zaman geriye akmaz; geçişler yumuşak ve okunabilirdir.

### 6.6 Character Interaction

- Aynı anda kadrajda en fazla 3-4 karakter.
- Karakterler arası 18-24 birim boşluk (trio kuralı).
- Etkileşim bölgeleri ve güvenli alanlar mekanın Environment Bible'ından alınır.

---

## 7. PRODUCTION DOCUMENT DISCIPLINE

- Markdown'lar **production-ready** tutulur.
- Dokümantasyon asla basitleştirilmez (never simplify).
- Bölümler asla birleştirilmez (never merge sections).
- Tablolar asla kaldırılmaz (never remove tables).
- Teknik bilgi asla kaldırılmaz (never remove technical information).
- Version-control dostu formatlama korunur.
- Yalnızca istenen alanlar güncellenir (only update requested fields).

---

## 8. GOAL

Mevcut production dokümanı korunur ve OpenArt testleriyle doğrulanmış en güncel production
pipeline'ı yansıtacak şekilde yükseltilir. Nihai doküman, jenerik bir AI prompt gibi değil,
profesyonel bir animasyon stüdyosu production dokümanı gibi okunmalıdır.

---

*Bu belge Pompom Hills production pipeline'ının kilit referansıdır.*
*Son güncelleme: 2026-07-01*
