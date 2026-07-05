# Season Begins — Shorts Plan

## Hangi sahneler Shorts olabilir?

| Short | Kaynak Shot | İçerik | Süre |
|-------|-------------|--------|------|
| 1 | Shot 01 | Kiko kendi evinde hoş geldin | 12s |
| 2 | Shot 02 | Mimi'nin kovanında cozy hello | 12s |
| 3 | Shot 03 | Noah + Arda little sound | 15s |
| 4 | Shot 04 | Luca + Opa wonder/wisdom | 15s |
| 5 | Shot 05 | Kiko + Noah + Arda trio | 15s |
| 6 | Shot 06 | Full cast final | 15s |

---

## Kısa yol: Shot'lardan direkt Short

Her shot zaten 12-15 saniye — YouTube Shorts için ideal.

Tek yapman gereken:
1. `ffmpeg` ile her shot'u 9:16 (dikey) formatına kırp
2. Ya da mevcut 16:9 shot'u olduğu gibi kullan (YouTube Shorts 16:9'i de kabul eder)

---

## Alternatif: Tam videodan clips

`pompom-hills-season-begins-all-shots.mp4` dosyasından zaman damgaları ile clips kesilir:

| Short | Başlangıç | Bitiş | İçerik |
|-------|-----------|-------|--------|
| 1 | 0:00 | 0:12 | Kiko welcome |
| 2 | 0:12.2 | 0:24.2 | Mimi cozy hello |
| 3 | 0:24.4 | 0:39.4 | Noah + Arda |
| 4 | 0:39.6 | 0:54.6 | Luca + Opa |
| 5 | 0:54.8 | 1:09.8 | Trio |
| 6 | 1:10 | 1:25 | Full cast |

---

## FFmpeg ile Short oluşturma

Tek shot'tan Short:
```bash
ffmpeg -i shot-1.mp4 -vf "crop=ih*9/16:ih" -t 12 short-kiko-welcome.mp4
```

Tam videodan clip:
```bash
ffmpeg -i pompom-hills-season-begins-all-shots.mp4 -ss 0 -t 12 short-01-kiko.mp4
```

---

## Her Short için Metadata

### Short 1 — Kiko Welcome

**Title:**
```
Hello from Kiko's Home! | Pompom Hills Shorts
```

**Description:**
```
Kiko welcomes you from her cozy home in Pompom Hills! 🌈
A warm hello to start the day.

Watch more: https://www.youtube.com/@PompomHills
#PompomHills #Shorts #PreschoolAnimation #Welcome
```

**Tags:**
```
Pompom Hills, Shorts, preschool animation, kids animation, Kiko, welcome, hello, toddler cartoon, gentle kids video, safe cartoon for kids
```

---

### Short 2 — Mimi Cozy

**Title:**
```
Come In, It's Cozy Here! | Mimi | Pompom Hills Shorts
```

**Description:**
```
Mimi peeks out from her cozy burrow in Pompom Hills. 💛
A gentle, sleepy hello.

Watch more: https://www.youtube.com/@PompomHills
#PompomHills #Shorts #PreschoolAnimation #Cozy
```

**Tags:**
```
Pompom Hills, Shorts, preschool animation, Mimi, cozy, hello, toddler cartoon, gentle kids video, calm kids cartoon, safe cartoon for kids
```

---

### Short 3 — Noah + Arda

**Title:**
```
Did You Feel That? | Noah & Arda | Pompom Hills Shorts
```

**Description:**
```
Noah and Arda notice something special at Stone Hill. ✨
A tiny happy feeling in Pompom Hills.

Watch more: https://www.youtube.com/@PompomHills
#PompomHills #Shorts #PreschoolAnimation #Curiosity
```

**Tags:**
```
Pompom Hills, Shorts, preschool animation, Noah, Arda, curiosity, Stone Hill, kids animation, toddler cartoon, gentle kids video
```

---

### Short 4 — Luca + Opa

**Title:**
```
So Much to Discover! | Luca & Opa | Pompom Hills Shorts
```

**Description:**
```
Luca and Opa explore Opa's Tree together. 🌳
A warm moment of wonder and wisdom.

Watch more: https://www.youtube.com/@PompomHills
#PompomHills #Shorts #PreschoolAnimation #Wonder
```

**Tags:**
```
Pompom Hills, Shorts, preschool animation, Luca, Opa, wonder, wisdom, Opa's Tree, kids animation, toddler cartoon
```

---

### Short 5 — Trio

**Title:**
```
Come Play With Us! | Kiko, Noah & Arda | Pompom Hills Shorts
```

**Description:**
```
Three friends invite you to play in Pompom Hills! 🎈
A playful trio moment before the big welcome.

Watch more: https://www.youtube.com/@PompomHills
#PompomHills #Shorts #PreschoolAnimation #Friends
```

**Tags:**
```
Pompom Hills, Shorts, preschool animation, Kiko, Noah, Arda, friends, play, trio, kids animation, toddler cartoon
```

---

### Short 6 — Full Cast

**Title:**
```
Welcome to Pompom Hills! | All Friends | Pompom Hills Shorts
```

**Description:**
```
All six friends welcome you to Pompom Hills! 🌈
The full cast says hello together.

Watch more: https://www.youtube.com/@PompomHills
#PompomHills #Shorts #PreschoolAnimation #Welcome
```

**Tags:**
```
Pompom Hills, Shorts, preschool animation, welcome, full cast, all friends, Kiko, Mimi, Noah, Arda, Luca, Opa, kids animation, toddler cartoon
```
