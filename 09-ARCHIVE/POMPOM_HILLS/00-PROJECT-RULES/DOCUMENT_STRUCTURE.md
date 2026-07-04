# DOCUMENT STRUCTURE — PomPom Hills

---

## Amaç

Bu dosya, tüm dokümantasyonun nerede olduğunu ve her dosyanın ne işe yaradığını açıklar.

---

## Kural

Bir kural bir kez yazılır.

Bölüm dosyaları bu kurallara referans verir, tekrar etmez.

Master dosyalar standartları belirler.

Bölüm dosyaları yalnızca bölüme özgü veriyi içerir.

---

## Master Dosyalar (00-PROJECT-RULES/)

| Dosya | Sorumluluk | Soru |
|---|---|---|
| CREATIVE_BIBLE.md | PomPom Hills nasıl hissettirmeli? | Duygu, felsefe, çocuk gelişimi |
| VISUAL_STYLE_GUIDE.md | PomPom Hills nasıl görünmeli? | Renk, şekil, malzeme, kamera |
| PRODUCTION_PIPELINE.md | Bölümler nasıl üretilmeli? | Akış, shot, render, inceleme |
| CONTINUITY_RULES.md | Süreklilik nasıl korunmalı? | Karakter, mekan, ışık, kamera |
| PROMPT_RULES.md | AI promptları nasıl yazılmalı? | Visual Prompt, negatif, referans |
| YOUTUBE_WORKFLOW.md | YouTube'a nasıl yüklenmeli? | Başlık, thumbnail, açıklama |
| DOCUMENT_STRUCTURE.md | Bu dosya | Harita |

---

## Karakter Dosyaları (01-CHARACTERS/)

| Dosya | İçerik |
|---|---|
| kiko.md | Kiko karakter tanımı |
| mimi.md | Mimi karakter tanımı |
| opa.md | Opa karakter tanımı |
| arda.md | Arda karakter tanımı |
| noah.md | Noah karakter tanımı |
| luca.md | Luca karakter tanımı |

---

## Dünya Dosyaları (POMPOM_HILLS_PRODUCTION/02_WORLDS/)

| Dosya | İçerik |
|---|---|
| stone-hill.md | Stone Hill dünya tanımı |
| central-square.md | Central Square dünya tanımı |
| opas-tree.md | Opa's Tree dünya tanımı |

---

## Bölüm Dosyaları (03-EPISODES/)

Her bölüm klasörü aynı formata sahiptir:

```
S01E0X-bolum-adi/
├── 01-overview.md          ← Genel bakış
├── 02-beat-sheet.md        ← Beat sheet
├── 03-storyboard.md        ← Storyboard
├── 04-assets.md            ← Asset listesi
├── 05-camera.md            ← Kamera planı
├── 06-dialogues.md         ← Diyaloglar
├── 07-sfx.md               ← Ses efektleri
├── 08-animation-notes.md   ← Animasyon notları
├── 09-render-prompts.md    ← OpenArt promptları
├── EPISODE_SUMMARY_TR.md   ← Türkçe anlatım
├── shots/                  ← Shot dosyaları
├── references/             ← Referans görselleri
└── outputs/                ← Üretilen videolar
```

---

## Dosya Sorumluluk Haritası

| Konu | Hangi dosyada? |
|---|---|
| Renk paleti | VISUAL_STYLE_GUIDE.md |
| Karakter tanımı | 01-CHARACTERS/{karakter}.md |
| Dünya tanımı | POMPOM_HILLS_PRODUCTION/02_WORLDS/{mekan}.md |
| Üretim akışı | PRODUCTION_PIPELINE.md |
| Süreklilik kuralları | CONTINUITY_RULES.md |
| Prompt yazma | PROMPT_RULES.md |
| YouTube yükleme | YOUTUBE_WORKFLOW.md |
| Hikaye felsefesi | CREATIVE_BIBLE.md |
| Bölüm detayları | 03-EPISODES/{bolum}/ |

---

## Yeni Kural Ekleme

Yeni bir kural eklenecekse:

1. Hangi konuda? → İlgili master dosyayı bul
2. O dosyaya ekle
3. Diğer dosyalarda tekrar etme
4. Bölüm dosyaları bu kurala referans versin

---

*Bu dosya tüm dokümantasyonun haritasıdır.*
