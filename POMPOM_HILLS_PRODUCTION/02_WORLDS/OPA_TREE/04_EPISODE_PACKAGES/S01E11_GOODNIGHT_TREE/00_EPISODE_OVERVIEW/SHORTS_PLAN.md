# S01E11 — Goodnight Tree | Shorts Plan

---

## Overview

| Alan | Değer |
|---|---|
| Episode | S01E11 — Goodnight Tree |
| Karakterler | Arda, Opa |
| Lokasyon | Opa's Tree (Night) |
| Shorts Sayısı | 2 |
| Platform | YouTube Shorts / Facebook / Instagram |

---

## Revizyon Notu (9 Temmuz 2026)

Önceki plan 4 Short içeriyordu ve 60 saniyelik kaynak video için bu sayı fazlaydı:
zaman aralıkları birbiriyle çakışıyordu (#1↔#2, #2↔#3, #3↔#4), yani aynı sahneler
birden fazla Short'ta tekrar ediyordu. 60 sn'lik bir kaynaktan 4 yerine, her biri
kendi başına tam bir mini-hikaye olan (hook → aksiyon → duygu), çakışmasız ve
tekrarsız **2 Short**'a düşürüldü.

> Not: Ana video dosyasının adı yanlış ("What Do Stars Say...") olarak kaydedilmişti;
> içerik doğru (Arda + Opa, "ağaçlar uyur mu"). Dosya
> `03_VIDEO_EXPORTS/Goodnight, Tree! 🌳 _ Arda & Opa _ Pompom Hills Preschool Animation.mp4`
> olarak yeniden adlandırıldı.

---

## Short Schedule

| Short | Yayın Tarihi | Başlık | Timing | Süre |
|---|---|---|---|---|
| #1 — Hook | TBD | Is the Tree Sleepy? 🌳 | 00:02 – 00:16 | 14 sn |
| #2 — Answer + Goodnight | TBD | Even Trees Need Sleep 🍃💛 | 00:28 – 01:00 | 32 sn |

> Short #1 crop notu: Bu bölümün açılış wide shot'ında Arda ağacın karşı kenarından
> geliyor ve merkez-crop'ta kadraj dışında kalıyor. Bu yüzden Short #1 merkez değil,
> **sola kaymış (left-of-center) kenar-crop** ile üretildi (ffmpeg `crop=1080:1920:583:0`,
> 3413px genişliğe scale sonrası). `make_short_vertical.sh` yalnızca merkez-crop yapar;
> bu offset manuel uygulandı.

---

## Short #1 — The Hook

**Başlık:** Is the Tree Sleepy? 🌳
**Timing:** 00:03 – 00:18 (15 sn)

### İçerik
Arda akşam vakti Opa'nın ağacına geliyor.
"Opa? I'm sleepy."
Ağaca bakıyor — acaba ağaç da yorgun mu?
Merak uyandırıyor.

### YouTube Metadata

**Title:** Is the Tree Sleepy? 🌳 | Arda & Opa | Pompom Hills Shorts

**Description:**
🌳 Arda visits Opa's tree at bedtime and wonders... is the tree sleepy too?
A gentle Pompom Hills bedtime moment.
#PompomHills #Shorts #KidsAnimation

**Tags:** Pompom Hills, Arda, Opa, tree, bedtime, wonder, preschool animation, kids animation, shorts

### Video Dosyası
`03_VIDEO_EXPORTS/shorts/s01e11-short-1-is-the-tree-sleepy.mp4`

---

## Short #2 — The Answer + Goodnight

**Başlık:** Even Trees Need Sleep 🍃💛
**Timing:** 00:28 – 01:00 (32 sn)

### İçerik
"Is the tree sleepy too?" — "Even trees need sleep."
Yapraklar hafifçe sallanıyor.
"Goodnight, tree." — "The tree says goodnight too."
Arda ağacın altında huzurla uykuya dalıyor.
Bölümün en güçlü sahnesinden huzurlu iyi geceler kapanışına kesintisiz geçiş.

### YouTube Metadata

**Title:** Even Trees Need Sleep 🍃💛 | Pompom Hills Shorts

**Description:**
🍃 Arda asks a gentle bedtime question — and the tree has a beautiful goodnight for everyone. 💛
A warm Pompom Hills bedtime moment.
#PompomHills #BedtimeStory #Shorts

**Tags:** Pompom Hills, Arda, Opa, tree, goodnight, bedtime story, nature, preschool animation, kids animation, shorts

### Video Dosyası
`03_VIDEO_EXPORTS/shorts/s01e11-short-2-goodnight-tree.mp4`

---

## Neden 2 (ve neden bu iki aralık)

- **Çakışma yok:** Short #1 (00:03–00:18) ve Short #2 (00:28–01:00) arasında 10 saniyelik
  boşluk var — aynı sahne iki klipte de görünmüyor.
- **Her Short kendi başına tam bir mini-hikaye:** Short #1 = hook + soru (merak
  uyandırır). Short #2 = cevap + duygu + iyi geceler kapanışı (sıcak, güven veren son).
- **Başlangıç etkisi korunur:** Her iki Short da kendi güçlü açılış anıyla başlıyor
  (Arda'nın gelip ağaca bakması / "even trees need sleep" cevabı).

---

## Eski 4'lü Plan (Superseded — artık kullanılmıyor)

> Bu bölüm sadece geçmiş referans için tutulur. Aşağıdaki 4 Short çakışmalı 4'lü planın
> parçasıydı ve yukarıdaki 2'li plan tarafından supersede edildi.

| Short | Başlık | Timing |
|---|---|---|
| #1 | Is the Tree Sleepy? 🌳 | 00:03 – 00:18 |
| #2 | Opa Tells a Story 🦉 | 00:12 – 00:30 |
| #3 | Even Trees Need Sleep 🍃 | 00:28 – 00:45 |
| #4 | Goodnight, Little Friend 💛 | 00:45 – 01:00 |
