# Instagram Reels Format Standard — Pompom Hills

> Instagram'a özel, mevcut uzun bölümlerden bağımsız mini formatlar.
> Bu formatlar Instagram trendlerine uygun: tek fikir, düşük prodüksiyon hissi,
> ilk 1-2 saniyede merak, izleyici katılımı, tekrar izleme motivasyonu.
>
> **Bu dosya Instagram Reels içerik üretimi için tek kaynaktır.**

---

## 1. Genel Kurallar

| Alan | Değer |
|------|-------|
| Format | 9:16 dikey, 1080×1920 |
| Süre | 7–15 saniye (formatına göre) |
| FPS | 24 |
| Mod | Frame-to-video, tek continuous shot |
| Üretim | OpenArt (aynı Shorts pipeline) |
| Dil | İngilizce (eğitim içeriği) |
| Karakter | Her format kendi karakter setini tanımlar |

### 1.1 Instagram Reels vs Shorts Farkı

| Özellik | Shorts (YouTube) | Instagram Reels |
|---------|-----------------|-----------------|
| Süre | 15-30 sn | 7-15 sn |
| Yapı | Discovery/hook | Tek fikir, anında kavranır |
| Hedef | İzlenme, abone | Kaydetme, paylaşma, yorum |
| Karakter görünümü | Tam body, merkez | Close-up serbest, reveal formatı |
| Kamera | Statik, child-eye | Değişken: close-up → reveal serbest |
| Metin overlay | Yasak | Instagram'da ayrı eklenir |

### 1.2 Ortak Prompt Yapısı

Her Instagram Reels prompt'u şu bölümleri içerir:

```text
## Shot Info
Format, süre, karakter(ler), lokasyon

## Visual Prompt
Sahne tanımı, karakter pozisyonu, zaman bazlı aksiyon

## Dialogue
İngilizce replikler (eğitim hedefiyle)

## Negative Prompt
Format-spesifik yasaklar

## OpenArt Settings
Süre, @image1 referansı, ayarlar
```

### 1.3 Karakter Referans Kullanımı

Her Reel için:
- `@image1`: Onaylanmış temiz start-frame still (canonical karakter referansı + dünya)
- Karakter rengi/kıyafeti `01-CHARACTERS/` dosyalarından birebir alınır
- Karakter pozisyonu: çerçevenin ortasındaki %60 güvenli bölge

### 1.4 Negatif Prompt (Tüm Formatlar İçin Ortak)

```
frozen staring, abrupt movement, pose snapping, teleporting, extra limbs,
duplicate characters, camera movement (unless specified), environment redesign,
harsh contrast, oversaturation, HDR, glossy surfaces, text, captions, subtitles,
background music, low quality, blur, facial distortion, dark lighting,
sharp edges, scary elements
```

---

## 2. Format Kataloğu

### FORMAT #1: "DON'T SAY IT, OPA!" (10-15 sn)

**Tür:** Kelime oyunu + karakter komedisi
**Eğitim hedefi:** Vocabulary (nesne adları)
**Karakterler:** Opa + Arda (+ opsiyonel Kiko)
**Lokasyon:** Central Square veya Opa's Garden
**İzleyici katılımı:** "Did YOU guess it?" → yorum

**Yapı:**
1. (0-2 sn) Ekranda bir nesne, Opa bakar
2. (2-4 sn) Arda: "Don't say [WORD]!"
3. (4-10 sn) Opa ipuçları verir (renk, şekil, kullanım)
4. (10-12 sn) Başka bir karakter dayanamaz, söyler
5. (12-15 sn) "Did YOU guess it?" → bitiş

**Seri potansiyeli:** Her nesne için yeni Reel (apple, ball, flower, star, tree, sun, bird, fish...)

---

### FORMAT #2: "WHAT DID [KARAKTER] SEE?" (7-10 sn)

**Tür:** Close-up → reveal, merak gizemi
**Eğitim hedefi:** "What is that?" / naming objects
**Karakterler:** Tek karakter (Kiko, Mimi, Opa, Arda, Luca...)
**Lokasyon:** Herhangi bir mekan
**İzleyici katılımı:** "What is it?" → yorum

**Yapı:**
1. (0-1 sn) Aşırı yakın plan: karakterin şaşkın yüzü
2. (1-3 sn) "Oh! What is THAT?"
3. (3-6 sn) Kamera yavaşça geri çekilir → reveal
4. (6-8 sn) Nesne/hayvan/durum ortaya çıkar
5. (8-10 sn) "A [OBJECT]!" → karakter tepkisi

**Teknik not:** Close-up'tan wide'e geçiş tek shot içinde olmalı (OpenArt frame-to-video).

**Seri potansiyeli:** Her karakter + her nesne kombinasyonu.

---

### FORMAT #3: "PICK ONE!" (8-12 sn)

**Tür:** İnteraktif seçim oyunu
**Eğitim hedefi:** Kelime dağarcığı + kavram eşleştirme
**Karakterler:** Opa (sunucu) + 1-2 karakter
**Lokasyon:** Central Square
**İzleyici katılımı:** Çocuğun ekrana cevap vermesi (yorum değil, etkileşim)

**Yapı:**
1. (0-2 sn) Opa: "Quick! Pick one!"
2. (2-4 sn) İki seçenek gösterilir (görsel olarak)
3. (4-6 sn) 2 saniyelik geri sayım hissi
4. (6-10 sn) Karakter seçer → komik sonuç
5. (10-12 sn) Tepki/kapanış

**Seri varyasyonları:**
- Apple / Banana
- Big / Small
- Red / Blue
- Happy / Sad
- Cat / Dog
- Up / Down
- Fast / Slow

---

### FORMAT #4: "OPA SAYS IT WRONG" (8-12 sn)

**Tür:** Düzeltme oyunu + dil eğitimi
**Eğitim hedefi:** Grammar correction (tenses, articles, plurals)
**Karakterler:** Opa + Arda (veya Kiko)
**Lokasyon:** Herhangi
**İzleyici katılımı:** "Can you fix it?" → yorum

**Yapı:**
1. (0-2 sn) Opa yanlış İngilizce söyler: "I am eat apple."
2. (2-4 sn) Karakter kameraya bakar: şaşkın ifade
3. (4-7 sn) "Opaaa… I am EATING an apple!"
4. (7-9 sn) Opa: "Ohhh!" + doğru cümle ekranda belirir
5. (9-12 sn) Opa gülümseme, bitiş

---

### FORMAT #5: "WHO SAID IT?" (8-10 sn)

**Tür:** Ses tahmin oyunu
**Eğitim hedefi:** Karakter tanıma + dinleme
**Karakterler:** 3+ karakter
**Lokasyon:** Herhangi
**İzleyici katılımı:** Kim söyledi → yorum

**Yapı:**
1. (0-2 sn) Karakter görünmez. Ses: "I LOVE CARROTS!"
2. (2-4 sn) Ekranda: WHO SAID IT? + 3 seçenek
3. (4-7 sn) Beklenti → kamera açılır
4. (7-10 sn) Beklenmedik karakter: "ME!" + komik tepki

---

### FORMAT #6: "TINY PROBLEMS" (12-15 sn)

**Tür:** Mini sitcom
**Eğitim hedefi:** "Can you help me?" / "I can help" / "Thank you!"
**Karakterler:** 2-3 karakter
**Lokasyon:** Herhangi
**İzleyici katılımı:** Empati + dil tekrarı

**Yapı:**
1. (0-3 sn) Karakter bir sorun yaşar
2. (3-6 sn) İkinci karakter yardım etmeye çalışır
3. (6-9 sn) Komik çözüm
4. (9-12 sn) "Thank you!" / "I can help!"
5. (12-15 sn) Sıcak kapanış

---

### FORMAT #7: "BEFORE / AFTER OPA" (6-9 sn)

** Tür:** Dramatik reveal
**Eğitim hedefi:** Vocabulary (yemek/nesne adları)
**Karakterler:** Opa + 1-2 karakter
**Lokasyon:** Herhangi
**İzleyici katılımı:** Görsel memnuniyet → kaydetme

**Yapı:**
1. (0-2 sn) Üzgün/boş sahne
2. (2-4 sn) Opa bir hareket yapar (kanat şaklatma, zıplama)
3. (4-7 sn) Renkli/dolu sahne ortaya çıkar
4. (7-9 sn) Eğitim kelimeleri tek tek belirir

---

### FORMAT #8: "POV: OPA IS YOUR ENGLISH TEACHER" (10-15 sn)

**Tür:** Komik eğitim skeci
**Eğitim hedefi:** Sayılar, renkler, nesneler
**Karakterler:** Opa + 1 karakter
**Lokasyon:** Herhangi
**İzleyici katılımı:** Güldürme → paylaşma

**Yapı:**
1. (0-3 sn) Opa öğretmen gibi başlar
2. (3-8 sn) Saçma bir şey olur (düşürür, kaybeder, karıştırır)
3. (8-12 sn) Doğru cevap ortaya çıkar
4. (12-15 sn) Gülümseme, bitiş

---

## 3. Üretim Akışı

```
1. Format seç (hangi Reel?)
        ↓
2. Varyasyonu belirle (hangi nesne/karakter/kavram?)
        ↓
3. @image1 start-frame still üret (canonical referanslarla)
        ↓
4. OpenArt prompt yaz (bu standarda göre)
        ↓
5. Negatif prompt ekle
        ↓
6. OpenArt'ta üret
        ↓
7. QA kontrolü (karakter görünüyor mu? mesaj anlaşılıyor mu?)
        ↓
8. Instagram'a özel metadata ekle (başlık, hashtag, CTA)
        ↓
9. Yükle
```

---

## 4. Instagram Metadata Standardı

### 4.1 Başlık Formatı

```
[Emoji] [Format adı] — [Varyasyon] | Pompom Hills
```

Örnek:
- "DON'T SAY APPLE! | Pompom Hills"
- "What Did Kiko See? | Pompom Hills"
- "Pick One: Apple or Banana? | Pompom Hills"

### 4.2 Açıklama Formatı

```
[1-2 cümlelik açıklama]
Did you guess it? Tell us in the comments!

#PompomHills #LearnEnglish #KidsEnglish #Preschool #ToddlerLearning
#EnglishForKids #Reels #KidsReels #[format-specific-hashtag]
```

### 4.3 Format-Spesifik Hashtag'ler

| Format | Hashtag |
|--------|---------|
| DON'T SAY IT | #DontSayIt #GuessTheWord #VocabularyGame |
| WHAT DID THEY SEE | #WhatDidYouSee #GuessWhat #DiscoveryReel |
| PICK ONE | #PickOne #WhichOne #KidsChoice |
| OPA SAYS WRONG | #FixIt #GrammarGame #EnglishCorrection |
| WHO SAID IT | #WhoSaidIt #GuessWho #CharacterQuiz |
| TINY PROBLEMS | #TinyProblem #CanYouHelp #HelpingHands |
| BEFORE/AFTER | #BeforeAfter #MagicReveal #Transformation |
| POV OPA TEACHER | #OpaTeacher #FunnyTeacher #LearnWithOpa |

---

## 5. Seri Yönetimi

Her format için bir klasör yapısı:

```
09_SOCIAL_REELS/
├── INSTAGRAM_REELS_FORMAT_STANDARD.md  (bu dosya)
├── DONT_SAY_IT/
│   ├── EP01_APPLE/
│   │   ├── shot-01-openart-prompt.md
│   │   └── metadata.md
│   ├── EP02_BALL/
│   └── EP03_FLOWER/
├── WHAT_DID_KIKO_SEE/
│   ├── EP01_GIANT_STRAWBERRY/
│   └── EP02_TINY_FROG/
├── PICK_ONE/
│   ├── EP01_APPLE_BANANA/
│   └── EP02_BIG_SMALL/
└── ...
```

---

## 6. İlgili Dosyalar

| Dosya | Amaç |
|-------|------|
| `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/SHORTS_PRODUCTION_STANDARD.md` | Teknik Shorts standartları |
| `00-CORE/CHARACTER_GUIDE.md` | Karakter canon |
| `01-CHARACTERS/` | Bireysel karakter dosyaları |
| `00-CORE/VARIABLES.md` | Prompt değişkenleri |
| `00-CORE/NEGATIVE_PROMPTS.md` | Negatif prompt listeleri |
| `00-CORE/30_YOUTUBE_METADATA_STANDARD.md` | YouTube metadata (Instagram'dan farklı) |

---

*Oluşturulma: 8 Ağustos 2026*
*Instagram Reels strateji dokümanından türetilmiştir.*
