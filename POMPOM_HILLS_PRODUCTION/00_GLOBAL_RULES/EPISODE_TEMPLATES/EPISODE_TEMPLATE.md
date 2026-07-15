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
| Series (varsa) | [Sub-series adı, örn. Opa's Storytime — yoksa "—"] |
| Playlist (varsa) | [Playlist adı, örn. Opa's Storytime \| Gentle Preschool Stories — yoksa "—"] |
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

## Opening Bumper

Reference: `00-CORE/18_VIDEO_STYLE_AND_RETENTION_STANDARD.md` §4a (and `00-CORE/31_OPA_INTERACTIVE_STORYTELLING_FORMAT.md` §4 for Opa's Storytime episodes).

- Duration: [3–5 sn max, veya "None"]
- Visual: [Görsel]
- Sound: [Ses]
- Dialogue: [Diyalog, varsa]
- Purpose: [Amaç]
- Retention risk: [Risk notu]

Bumper kullanılmayan bölümler için:

```text
Opening Bumper: None. Episode begins directly with in-story hook.
```

---

## Episode Body

[Ana bölüm — Scene Order tablosuna bakınız]

---

## Closing Bumper

Reference: `00-CORE/18_VIDEO_STYLE_AND_RETENTION_STANDARD.md` §9a (ve §9b End Screen Policy).

- Duration: [3–6 sn max]
- Visual: [Görsel]
- Sound: [Ses]
- Dialogue: [Diyalog, varsa]
- End-screen-safe frame: [Açıklama]
- Purpose: [Amaç]

Bumper kullanılmayan bölümler için:

```text
Closing Bumper: Warm final hold only.
```

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

## Continuity and Quality-Reset Schedule

Decide this table before any video generation:

| Shot | Production Mode | Linked chain count | Main action complete? | Stable final 1–2s | Next-shot dependency |
|---:|---|---:|---|---|---|
| 01 | FRESH QUALITY-RESET SHOT | 0 | [Yes/No] | [State] | [NONE/LIMITED/EXACT] |
| 02 | [Mode] | [0–3] | [Yes/No] | [State] | [NONE/LIMITED/EXACT] |
| 03 | [Mode] | [0–3] | [Yes/No] | [State] | [NONE/LIMITED/EXACT] |
| 04 | [Mode] | [0–3] | [Yes/No] | [State] | [NONE/LIMITED/EXACT] |
| 05 | [Mode] | [0–3] | [Yes/No] | [State] | [NONE/LIMITED/EXACT] |
| 06 | [Mode] | [0–3] | [Yes/No] | [State] | [NONE/LIMITED/EXACT] |

`EXACT FRAME CONTINUITY REQUIRED` is rare and must be justified. A shot after Linked
Continuity Shot 3 is always fresh. A shot after Linked Continuity Shot 2 should normally be
fresh. Reject the plan if a simple physical action or camera move is split across shots.

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
Clean shot boundaries must remain visually cohesive; exact seamlessness is required only for
pre-planned linked shots.
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
| `10-continuity-reset-plan.md` | ✅ | Pre-planned Production Mode, chain count ve reset schedule |
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

Reference: `11-DOCS/16_VIDEO_QA_SPEC.md`
Standards: `00-CORE/17_VIDEO_GENERATION_STANDARD.md`,
`00-CORE/SHOT_PRODUCTION_STANDARD.md`

Required episode-level checks:

- [ ] Every shot includes the Required Global QA Locks section.
- [ ] Voice continuity checked first.
- [ ] Colour continuity checked second.
- [ ] Lighting continuity checked third.
- [ ] Intra-shot character continuity checked after voice/colour/lighting.
- [ ] Hard background and object identity continuity checked after character continuity.
- [ ] World continuity checked after background/object continuity.
- [ ] Story and tempo checked last.
- [ ] Voice identity, pitch, timbre, speaking speed, pronunciation, accent, emotional tone and recording quality remain consistent across speaking shots.
- [ ] White balance, exposure, colour temperature, saturation, contrast, brightness and pastel palette remain consistent across all shots.
- [ ] Light direction, light intensity, shadow softness, ambient lighting and highlight behaviour remain consistent across all shots.
- [ ] Full video watched once for character continuity and once for background/object stability.
- [ ] No character disappears, teleports, regenerates after occlusion or becomes fully hidden inside any shot.
- [ ] No background object moves, morphs, duplicates, disappears or changes identity.
- [ ] Episode feels visually cohesive even when clean editorial cuts are used.
- [ ] Every shot completes its own main action and camera move.
- [ ] Every shot has a stable, grounded final 1–2 seconds.
- [ ] Production Mode and linked-chain count are approved before generation.
- [ ] No linked chain exceeds two normally or three exceptionally.
- [ ] Mandatory quality resets return to canonical World and character references.
- [ ] If an opening bumper is used, it is 3–5 seconds maximum and does not delay the story (`00-CORE/18_VIDEO_STYLE_AND_RETENTION_STANDARD.md` §4a).
- [ ] If a closing bumper is used, it is 3–6 seconds maximum and gives a warm resolution (`00-CORE/18_VIDEO_STYLE_AND_RETENTION_STANDARD.md` §9a).

---

*Bu belge tüm yeni bölümler için standart şablondur.*
