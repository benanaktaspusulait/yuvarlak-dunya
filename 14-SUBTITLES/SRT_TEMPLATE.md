# Altyazı Şablonu — PomPom Hills

> *Source of truth for: subtitle format, rules, file structure.*

---

## Dosya Yapısı

```
14-SUBTITLES/
├── s01e01/
│   ├── srt/
│   │   ├── s01e01-EN.srt
│   │   ├── s01e01-TR.srt
│   │   └── s01e01-ES.srt
│   └── vtt/
│       ├── s01e01-EN.vtt
│       ├── s01e01-TR.vtt
│       └── s01e01-ES.vtt
├── s01e02/
│   ├── srt/
│   └── vtt/
├── s01e26/
│   ├── srt/
│   └── vtt/
├── intros/
│   ├── kiko/
│   │   ├── srt/ (3 dosya)
│   │   └── vtt/ (3 dosya)
│   ├── mimi/
│   │   ├── srt/
│   │   └── vtt/
│   ├── opa/
│   ├── arda/
│   ├── noah/
│   └── luca/
└── SRT_TEMPLATE.md
```

---

## Format: SRT

```srt
1
00:00:01,000 --> 00:00:04,000
[İlk cümle]

2
00:00:04,500 --> 00:00:07,000
[İkinci cümle]

3
00:00:07,500 --> 00:00:10,000
[Üçüncü cümle]
```

---

## Format: WebVTT

```vtt
WEBVTT

1
00:00:01.000 --> 00:00:04.000
[İlk cümle]

2
00:00:04.500 --> 00:00:07.000
[İkinci cümle]

3
00:00:07.500 --> 00:00:10.000
[Üçüncü cümle]
```

---

## Farklar

| Özellik | SRT | VTT |
|---------|-----|-----|
| Header | Yok | `WEBVTT` |
| Time separator | Virgül (`,`) | Nokta (`.`) |
| Encoding | UTF-8 | UTF-8 |
| YouTube uyumu | İyi | Daha iyi |
| Tarayıcı desteği | Sınırlı | Tam |

---

## Kurallar

- Maks. 2 satır altyazı
- Maks. 42 karakter/satır
- Minimum 1 saniye, maksimum 7 saniye
- Her entry arasında boş satır olmalı
- Dosya tek satır newline ile bitmeli
- Encoding: UTF-8

---

## Dil Sürümü

Her bölüm ve intro için 6 dosya (3 dil × 2 format):

| Dil | SRT | VTT |
|-----|-----|-----|
| Türkçe | `s01eXX-TR.srt` | `s01eXX-TR.vtt` |
| İngilizce | `s01eXX-EN.srt` | `s01eXX-EN.vtt` |
| İspanyolca | `s01eXX-ES.srt` | `s01eXX-ES.vtt` |

---

## Intro Dosyaları

| Intro | Dosya adı |
|-------|-----------|
| Kiko | `intros/kiko-intro-{LANG}.{ext}` |
| Mimi | `intros/mimi-intro-{LANG}.{ext}` |
| Opa | `intros/opa-intro-{LANG}.{ext}` |
| Arda | `intros/arda-intro-{LANG}.{ext}` |
| Noah | `intros/noah-intro-{LANG}.{ext}` |
| Luca | `intros/luca-intro-{LANG}.{ext}` |

---

*Bu belge altyabı şablonu için tek kaynaktır.*
*Son güncelleme: 2 Temmuz 2026*
