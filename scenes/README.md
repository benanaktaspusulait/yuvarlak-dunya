# Pompom Hills Scenes v2.1

Bu klasör, 7 dakikalık bölümleri sahne sahne üretmek için kullanılır.

## Folder Convention

```text
scenes/
  season-01/
    s01e01-hello-pompom-hills/
      README.md
      01-kiko-intro.md
      02-mimi-intro.md
```

## Scene File Standard

Her sahne dosyası şu bölümleri içermelidir:

| Bölüm | Amaç |
| --- | --- |
| Production Lock | Süre, karakter, mekan, duygu, hedef yaş |
| Pedagojik Amaç | 3-4 yaş çocuğun sahneden ne alacağı |
| Beat Sheet | Basit olay akışı |
| Shot Plan | Kamera, süre, aksiyon, ses |
| Diyalog | Kısa, tekrar edilebilir replikler |
| Visual Prompt | İngilizce AI görsel prompt |
| Animation Notes | 3D staging, rig, timing, hareket |
| Safety Check | Korku, hız, karmaşa, çatışma kontrolü |

## Production Rules

- Her sahne tek ana fikir taşır.
- Her sahnede en fazla 1 yeni karakter kendini tanıtır.
- Diyalog cümleleri 3-6 kelimeyi geçmez.
- Karakter kendini doğrudan tanıtır: ad, sevdiği şey, bir duygu.
- Kamera sabit veya yavaş hareket eder.
- Her prompt `{style}`, `{camera}`, `{lighting}` değişkenlerini içerir.
- Negative prompt için `NEGATIVE_PROMPTS.md` kullanılır.

## First Intro Arc

| Scene | Character | Purpose |
| --- | --- | --- |
| `season-01/s01e01-hello-pompom-hills/01-kiko-intro.md` | Kiko | Ana karakter ve izleyici gözü tanıtılır |
| `season-01/s01e01-hello-pompom-hills/02-mimi-intro.md` | Mimi | Duygusal destek arkadaşı tanıtılır |

Opa üçüncü sahnede tanıtılabilir: alçak hikaye dalı, "Yavaşça bakalım" ritüeli, güvenli rehber rolü.
