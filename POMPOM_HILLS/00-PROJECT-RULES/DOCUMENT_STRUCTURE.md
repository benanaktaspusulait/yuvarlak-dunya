# DOCUMENT STRUCTURE — PomPom Hills

---

## Folder Layout

```
POMPOM_HILLS/
│
├── 00-PROJECT-RULES/
│   ├── PRODUCTION_PIPELINE.md      ← Production akışı ve felsefesi
│   ├── DOCUMENT_STRUCTURE.md       ← Bu dosya
│   ├── PROMPT_RULES.md             ← Prompt yazma kuralları
│   ├── CONTINUITY_RULES.md         ← Süreklilik kuralları
│   └── YOUTUBE_WORKFLOW.md         ← YouTube yükleme süreci
│
├── 01-CHARACTERS/
│   ├── kiko.md                     ← Kiko karakter tanımı
│   ├── mimi.md                     ← Mimi karakter tanımı
│   ├── opa.md                      ← Opa karakter tanımı
│   ├── arda.md                     ← Arda karakter tanımı
│   ├── noah.md                     ← Noah karakter tanımı
│   ├── luca.md                     ← Luca karakter tanımı
│   └── ...
│
├── 02-WORLDS/
│   ├── stone-hill.md               ← Stone Hill dünya tanımı
│   ├── central-square.md           ← Central Square dünya tanımı
│   ├── opas-tree.md                ← Opa's Tree dünya tanımı
│   └── ...
│
└── 03-EPISODES/
    └── S01E01-goodnight-tree/
        ├── README.md               ← Bölüm özeti
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

## Dosya Türleri

### Global Kurallar (00-PROJECT-RULES/)

| Dosya | Amaç | Kim kullanır |
|---|---|---|
| PRODUCTION_PIPELINE.md | Tüm production akışı | Herkes |
| DOCUMENT_STRUCTURE.md | Dosya yapısı | Herkes |
| PROMPT_RULES.md | Prompt yazma kuralları | Prompt yazan |
| CONTINUITY_RULES.md | Süreklilik kuralları | Prompt yazan |
| YOUTUBE_WORKFLOW.md | YouTube yükleme | Yükleme yapan |

### Karakterler (01-CHARACTERS/)

| Dosya | Amaç |
|---|---|
| {character}.md | Karakter tanımı, renk, tasarım, ses |

### Dünyalar (02-WORLDS/)

| Dosya | Amaç |
|---|---|
| {world}.md | Dünya tanımı, mekan kuralları, camera rules |

### Bölümler (03-EPISODES/)

| Dosya | Amaç |
|---|---|
| README.md | Bölüm özeti |
| 01-overview.md | Genel bakış |
| 02-beat-sheet.md | Beat sheet |
| 03-storyboard.md | Storyboard |
| 04-assets.md | Asset listesi |
| 05-camera.md | Kamera planı |
| 06-dialogues.md | Diyaloglar |
| 07-sfx.md | Ses efektleri |
| 08-animation-notes.md | Animasyon notları |
| 09-render-prompts.md | OpenArt promptları |
| EPISODE_SUMMARY_TR.md | Türkçe anlatım |
| shots/ | Shot dosyaları |
| references/ | Referans görselleri |
| outputs/ | Üretilen videolar |

---

## Kural

Kurallar bir kez yazılır, global dosyalarda tutulur.

Bölüm dosyaları bu kurallara referans verir, tekrar etmez.

Karakter ve dünya dosyaları sadece kendi klasörlerinde bulunur.

Hiçbir dosya başka bir dosyanın içeriğini kopyalamaz.
