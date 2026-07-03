# Episode Template — PomPom Hills

---

## Kullanım

Bu şablonu kullanarak yeni bölüm dosyası oluşturun.

---

## Template

```markdown
# S[SEZON]E[BÖLÜM] — [BÖLÜM ADI] v3.0

---

## Episode Lock

| Alan | Değer |
| --- | --- |
| Süre | 90 saniye (6 sahne × 15 sn) |
| Hedef yaş | 3-4 |
| Ana duygu | [Duygu] |
| Ana tema | [Tema] |
| Mekan | [Mekan adı] |
| Karakterler | [Karakter listesi] |
| Voice Identity | [Voice ID / approved voice reference per speaking character] |
| Colour Identity | [Warm white balance / pastel palette / soft saturation / low contrast] |
| Lighting Identity | [Warm morning sunlight / soft ambient preschool lighting] |
| Görsel yoğunluk | [Düşük/Orta] |
| Çatışma | Yok; sadece [açıklama] |

---

## Story Summary

[Bölümün kısa özeti]

---

## Micro-Moment (Key Discovery)

[Çocuğun hatırlayacağı küçük ama unutulmaz an]

---

## Scene Order

| Sıra | Dosya | Süre | Karakter | Amaç |
| --- | --- | ---: | --- | --- |
| 01 | `01-[sahne-adı].md` | 15 sn | [Karakter] | [Amaç] |
| 02 | `02-[sahne-adı].md` | 15 sn | [Karakter] | [Amaç] |
| 03 | `03-[sahne-adı].md` | 15 sn | [Karakter] | [Amaç] |
| 04 | `04-[sahne-adı].md` | 15 sn | [Karakter] | [Amaç] |
| 05 | `05-[sahne-adı].md` | 15 sn | [Karakter] | [Amaç] |
| 06 | `06-[sahne-adı].md` | 15 sn | [Karakter] | [Amaç] |

---

## Repeated Phrase

```text
[Tekrarlanan cümle]
```

---

## Learning Point

[Çocuğun öğreneceği şey]

---

## Voice Notes

| Karakter | Ses |
| --- | --- |
| [Karakter] | [Voice ID or approved voice reference + ses notları] |

Reference: `00-CORE/SHOT_PRODUCTION_STANDARD.md`

Voice continuity rule:

```text
The speaking voice MUST remain identical throughout the entire episode.
Use the same Voice ID or approved voice reference for the same character.
Maintain the same voice identity, timbre, pitch, speaking speed, warmth, preschool energy, pronunciation, accent, age impression, emotional tone and recording quality.
All speaking shots must sound as if they were recorded during the same recording session.
Never replace the voice with a narrator or alternate performer.
```

---

## Colour Notes

```text
The full episode must appear colour graded as one continuous film.
Maintain identical white balance, exposure, colour temperature, saturation, contrast, brightness and pastel palette across all shots.
No cool shift. No warm shift. No green tint. No magenta tint. No orange grading. No HDR look. No cinematic LUT.
The viewer must not perceive a shot boundary.
```

---

## Lighting Notes

```text
The lighting must continue across shots without reinterpretation.
Maintain identical light direction, light intensity, shadow softness, ambient lighting, highlight behaviour, cloud brightness and grass brightness.
Do not allow the episode to become brighter, darker, warmer, cooler, harsher or more cinematic between shots.
```

---

## Negative Prompt

[Toplu negative prompt]
```

---

## Kanonik Bölüm Klasör Yapısı (Standart)

Her bölüm klasörü (`04-SCENES/season-NN/sNNeNN-slug/`) şu dosyaları içermelidir:

| Dosya | Zorunlu | İçerik |
| --- | --- | --- |
| `01-overview.md` | ✅ | Bölüm özeti, lock tablosu |
| `02-beat-sheet.md` | ✅ | Beat/zaman akışı |
| `03-storyboard.md` | ✅ | Sahne sahne storyboard (BÜYÜK harfli `STORYBOARD.md` KULLANILMAZ) |
| `04-assets.md` | ✅ | Karakter/mekan/prop dosya listesi |
| `05-camera.md` | ✅ | Kamera planı |
| `06-dialogues.md` | ✅ | Diyaloglar |
| `07-sfx.md` | ✅ | Ses efektleri |
| `08-animation-notes.md` | ✅ | Animasyon notları |
| `09-render-prompts.md` | ✅ | OpenArt render promptları |
| `COORDINATE_MAP.md` | ✅ | Koordinat haritası (Kiko=100 birim) |
| `EPISODE_SUMMARY.md` | ✅ | İngilizce bölüm özeti |
| `EPISODE_SUMMARY_TR.md` | ✅ | Türkçe bölüm özeti |
| `shots/` | Opsiyonel | Shot bazında ayrıntı (`shot-NN-aciklama.md`) |
| `README.md` | Opsiyonel | Bölüm giriş/gezinme notu |

**İstisna — S01E01 (Hello Pompom Hills):** Bu bölüm bir "karakter tanıtım" montajıdır; numaralı aspect dosyaları yerine karakter başına sahne dosyaları kullanır (`01-kiko-intro.md` … `15-goodbye-handoff.md`). Bu bilinçli bir istisnadır.

---


- Her bölüm 6 sahne × 15 saniye = 90 saniye.
- Maksimum 3 karakter.
- Tek mekan tercih edilir.
- Tek duygusal hedef.
- Sıcak kapanış.

---

## QA Status

| Shot | QA Score | Production Ready |
|------|:--------:|:----------------:|
| 01 | /10 | ⬜ |
| 02 | /10 | ⬜ |
| 03 | /10 | ⬜ |
| 04 | /10 | ⬜ |
| 05 | /10 | ⬜ |
| 06 | /10 | ⬜ |

Reference: `16_VIDEO_QA_SPEC.md`

Required episode-level checks:

- [ ] Voice continuity checked first.
- [ ] Colour continuity checked second.
- [ ] Lighting continuity checked third.
- [ ] Character continuity checked after voice/colour/lighting.
- [ ] World continuity checked after character continuity.
- [ ] Story and tempo checked last.
- [ ] Voice identity, pitch, timbre, speaking speed, pronunciation, accent, emotional tone and recording quality remain consistent across speaking shots.
- [ ] White balance, exposure, colour temperature, saturation, contrast, brightness and pastel palette remain consistent across all shots.
- [ ] Light direction, light intensity, shadow softness, ambient lighting and highlight behaviour remain consistent across all shots.
- [ ] Episode feels like one uninterrupted animated film.
- [ ] The viewer cannot perceive where one shot ends and the next begins.

---

*Bu belge tüm yeni bölümler için standart şablondur.*
