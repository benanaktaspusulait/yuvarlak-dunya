# Pompom Hills Scenes v3.0

Bu klasör, 7 dakikalık bölümleri sahne sahne üretmek için kullanılır.

## Folder Convention

```text
scenes/
  season-01/
    s01e01-hello-pompom-hills/
      README.md
      01-kiko-intro.md          # EN (kaynak)
      01-kiko-intro-TR.md       # TR (senkronize)
      02-mimi-intro.md
      02-mimi-intro-TR.md
      ...
      COORDINATE_MAP.md         # Bölüm koordinat haritası
      archive/                  # Kullanılmayan sahneler
```

## Kaynak Dil Kuralı

**EN dosyaları tek kaynaktır.** TR dosyaları EN'den türetilir ve senkronize tutulur.

- Tüm prodüksiyon kararları EN dosyasında yapılır.
- TR dosyası, EN'nin çevirisidir; yapısal olarak aynı olmalıdır.
- Güncelleme gerektiğinde önce EN, sonra TR güncellenir.

## Scene File Standard

Her sahne dosyası şu bölümleri içermelidir:

| Bölüm | Amaç |
| --- | --- |
| Scene ID | Bölüm, sahne no, versiyon, toplam süre |
| Previous Scene End State | Önceki sahnedeki son durum |
| Start State | Bu sahnenin ilk karesindeki durum |
| Environment Plate | Kullanılan kesin dosya yolu |
| Coordinate Map | Karakter/prop/kamera konumları (100 birim) |
| Character Positions | Her karakterin başlangıç ve bitiş konumu |
| Prop Positions | Her propun başlangıç ve bitiş konumu |
| Weather Lock | Saat, ışık, bulut, rüzgar |
| Action Beats | 3-5 basit beat |
| Dialogue | İngilizce replikler, 2-4 kelime |
| End State | Son karede herkesin durumu |
| Continuity Handoff | Sonraki sahne için devredilen bilgi |
| Existing Assets | Kullanılan dosya yolları |
| Missing Assets | Eksik görseller |
| QA | Yaş uygunluğu, tekrar, continuity kontrolü |

## Production Rules

- Her sahne tek ana fikir taşır.
- Her sahnede en fazla 2 aktif karakter (1.5+ yaş hedefi).
- Diyalog cümleleri 2-4 kelimeyi geçmez.
- Kamera sabit veya yavaş hareket eder.
- Her prompt `{style}`, `{camera}`, `{lighting}` değişkenlerini içerir.
- Negative prompt için `NEGATIVE_PROMPTS.md` kullanılır.
- Her sahne önceki sahnenin bittiği fiziksel durumdan başlar.

## First Intro Arc (v3.0)

Bu bölüm ana trioyu tanıtır, ardından Pompom Hills komşularını kısa "merhaba"
cameo'larıyla gösterir ve güvenli bir veda ile kapanır. Trio (Kiko, Mimi, Opa)
duygusal çıpadır; 05-14 arası karakterler kısa tanıtım sahneleridir.

| Scene | Character | Purpose |
| --- | --- | --- |
| `01-kiko-intro.md` | Kiko | Ana karakter tanıtılır; merak ve keşif |
| `02-mimi-intro.md` | Mimi | Duygusal destek arkadaşı; Kiko continuity'da |
| `03-opa-intro.md` | Opa | Bilge rehber; Kiko ve Mimi continuity'da |
| `04-trio-hello.md` | Üçlü | Birlikte neşe; trio pozu |
| `05-arda-intro.md` | Arda | Enerjik futbol sever komşu |
| `06-noah-intro.md` | Noah | Yaratıcı yapı-bozar oyuncu |
| `07-aiko-intro.md` | Aiko | Sakin, düşünceli gözlemci |
| `08-amara-intro.md` | Amara | Yardımsever şarkıcı arkadaş |
| `09-sofia-intro.md` | Sofia | Renk seven yaratıcı sanatçı |
| `10-luca-intro.md` | Luca | Meraklı kaşif |
| `11-freya-intro.md` | Freya | Doğa seven bahçıvan |
| `12-tillo-intro.md` | Tillo | Bahçe/ağaç ev komşusu |
| `13-mirnik-intro.md` | Mirnik | Oyuncu saklambaç kedisi |
| `14-mimo-intro.md` | Mimo | Rainbow Creek komşusu |
| `15-goodbye-handoff.md` | Üçlü | Güvenli veda; bir sonraki bölüme devir |

> Not: EN dosyaları tek kaynaktır (structured). Karakter intro TR dosyaları anlatım
> (narrative) formatındadır; `04-trio-hello` ve `15-goodbye-handoff` TR dosyaları structured tutulur.
