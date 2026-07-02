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
| Süre | 60 saniye (4 sahne × 15 sn) |
| Hedef yaş | 3-4 |
| Ana duygu | [Duygu] |
| Ana tema | [Tema] |
| Mekan | [Mekan adı] |
| Karakterler | [Karakter listesi] |
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
| [Karakter] | [Ses notları] |

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


- Her bölüm 4 sahne × 15 saniye = 60 saniye.
- Maksimum 3 karakter.
- Tek mekan tercih edilir.
- Tek duygusal hedef.
- Sıcak kapanış.

---

*Bu belge tüm yeni bölümler için standart şablondur.*
