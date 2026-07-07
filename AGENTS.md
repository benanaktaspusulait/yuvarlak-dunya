# AGENTS.md — Pompom Hills / Yuvarlak Dunya

> **Bu repoda çalışan her AI agent/tool (Kiro, Codex, Claude, ChatGPT, vb.), bir prompt'u
> işlemeden veya herhangi bir dosyayı değiştirmeden önce BU DOSYAYI okumalı ve aşağıdaki
> routing tablosuna göre ilgili kaynak dosyayı bulup okumalıdır.**
>
> Varsayımla, hafızadan veya "muhtemelen böyledir" diyerek iş yapma. İlgili dosyayı oku,
> sonra uygula. Bir konuda hangi dosyaya bakman gerektiği belirsizse, kullanıcıya sor —
> tahmin etme.

---

## 0. Altın Kural

**Bir kural bir kez yazılır.** Aşağıdaki tabloda listelenen dosyalar her konu için TEK
yetkili kaynaktır. Yeni bir prompt/görev geldiğinde önce ilgili satırı bul, o dosyayı/dosyaları
oku, sonra işe başla.

Varsayılan olarak DEĞİŞTİRME (aksi açıkça istenmedikçe):

- Character canon (`00-CORE/CHARACTER_GUIDE.md`, `01-CHARACTERS/*`)
- World canon (`00-CORE/WORLD_BIBLE.md`, `POMPOM_HILLS_PRODUCTION/02_WORLDS/*`)
- Episode script'leri (`POMPOM_HILLS_PRODUCTION/02_WORLDS/*/04_EPISODE_PACKAGES/*`, `02_SEASON_2/*`, `03_SEASON_3/*`)
- Sub-series script'leri (`04_KIKOS_DISCOVERY_DAYS/*`, `05_MIMIS_FEELINGS_CORNER/*`, `06_MUSIC_RHYTHM_TIME/*`)
- Production/teknik standartlar (`00-CORE/TECH_SPECS.md`, `00-CORE/17_VIDEO_GENERATION_STANDARD.md`,
  `00-CORE/VISUAL_STYLE_GUIDE.md`, `00-CORE/CONTINUITY_RULES.md`)

Bu dosyalar sadece kullanıcı açıkça "karakteri değiştir", "dünyayı güncelle", "senaryoyu
yeniden yaz" gibi bir talimat verdiğinde değiştirilir. Stratejik/yayın/metadata güncellemeleri
bu dosyalara dokunmaz.

---

## 1. Görev Türüne Göre Routing Tablosu

| Yapılacak iş | Önce oku |
|---|---|
| **Sezon yapısı** | `08-PRODUCTION/EPISODE_TRACKER_S01.md`, `EPISODE_TRACKER_S02.md`, `EPISODE_TRACKER_S03.md` |
| Sezon 1 bölüm/şena yazımı | `00-CORE/SERIES_STRUCTURE.md`, `POMPOM_HILLS_PRODUCTION/02_WORLDS/*/04_EPISODE_PACKAGES/` |
| Sezon 2 bölüm/şena yazımı | `POMPOM_HILLS_PRODUCTION/02_SEASON_2/04_EPISODE_PACKAGES/` |
| Sezon 3 bölüm/şena yazımı | `POMPOM_HILLS_PRODUCTION/03_SEASON_3/04_EPISODE_PACKAGES/` |
| Yeni karakter ekleme/değiştirme | `00-CORE/CHARACTER_GUIDE.md`, `01-CHARACTERS/`, `CONTRIBUTING.md` §"Yeni Karakter" |
| Yeni dünya/mekan ekleme/değiştirme | `00-CORE/WORLD_BIBLE.md`, `POMPOM_HILLS_PRODUCTION/02_WORLDS/`, `CONTRIBUTING.md` §"Yeni Mekan" |
| Opa's Storytime (masal anlatımı sub-series) | `00-CORE/31_OPA_INTERACTIVE_STORYTELLING_FORMAT.md`, `POMPOM_HILLS_PRODUCTION/02_WORLDS/*/04_EPISODE_PACKAGES/OPA_STORYTIME_*` |
| Brave Little Days (yaşam becerisi sub-series) | `00-CORE/32_BRAVE_LITTLE_DAYS_LIFE_SKILLS_FORMAT.md`, `POMPOM_HILLS_PRODUCTION/03_EPISODES/BRAVE_LITTLE_DAYS_SERIES/` |
| **Kiko's Discovery Days** (keşif/merak sub-series) | `POMPOM_HILLS_PRODUCTION/04_KIKOS_DISCOVERY_DAYS/FORMAT_STANDARD.md`, `04_EPISODE_PACKAGES/` |
| **Mimi's Feelings Corner** (duygu okuryazarlığı sub-series) | `POMPOM_HILLS_PRODUCTION/05_MIMIS_FEELINGS_CORNER/FORMAT_STANDARD.md`, `04_EPISODE_PACKAGES/` |
| **Music & Rhythm Time** (müzik/ritim sub-series) | `POMPOM_HILLS_PRODUCTION/06_MUSIC_RHYTHM_TIME/FORMAT_STANDARD.md`, `04_EPISODE_PACKAGES/` |
| Shot/video üretimi (kamera, renk, süreklilik, teknik) | `00-CORE/17_VIDEO_GENERATION_STANDARD.md`, `00-CORE/VISUAL_STYLE_GUIDE.md`, `00-CORE/VISUAL_CONTINUITY_RULES.md` |
| Video pacing / hook / retention stili | `00-CORE/18_VIDEO_STYLE_AND_RETENTION_STANDARD.md` |
| **Shorts üretim standardı (karakter görünürsüzlüğü, kalite)** | `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/SHORTS_PRODUCTION_STANDARD.md` |
| Series bumper ile world micro-opening ayrımı | `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/MICRO_OPENING_AND_CLOSING_STANDARD.md` |
| Shot'lar arası continuity workflow | `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/SHOT_CONTINUITY_WORKFLOW.md` |
| Standalone shot üretimi | `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/STANDALONE_SHOT_AND_TRANSITION_STANDARD.md` |
| Sosyal medya görsel formatı | `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/SOCIAL_MEDIA_IMAGE_FORMAT_STANDARD.md` |
| YouTube title / description / tags / Shorts metadata | `00-CORE/30_YOUTUBE_METADATA_STANDARD.md` |
| Yayın stratejisi | `11-DOCS/09_YOUTUBE_STRATEGY.md` |
| Ses / voice / seslendirme | `00-CORE/AUDIO_GUIDE.md`, `00-CORE/EPISODE_AUDIO_WORKFLOW.md` |
| OpenArt prompt Sound bölümü | `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/NATURAL_CALMING_AMBIENCE_SOUND_STANDARD.md` |
| Çocuk güvenliği / COPPA | `00-CORE/CHILD_SAFETY_RULES.md`, `10-LICENSING/COPPA_MADE_FOR_KIDS_CHECKLIST.md` |
| Yasak/negatif prompt listeleri | `00-CORE/NEGATIVE_PROMPTS.md` |
| Prompt değişkenleri | `00-CORE/VARIABLES.md` |
| Yayın öncesi kalite kontrol | `00-CORE/MASTER_QA_CHECKLIST.md`, `00-CORE/SCENE_QA_CHECKLIST.md` |
| Altyazı (SRT/VTT) | `14-SUBTITLES/SRT_TEMPLATE.md`, `11-DOCS/12_SUBTITLE_STYLE_GUIDE.md` |
| Üretim takibi | `08-PRODUCTION/EPISODE_TRACKER_S01.md`, `EPISODE_TRACKER_S02.md`, `EPISODE_TRACKER_S03.md` |
| **Profesyonel standartlar / TODO** | `08-PRODUCTION/TODO.md` |
| İçerik/format eşleştirme | `08-PRODUCTION/CONTENT_MATRIX.md` |
| Lisanslama / marka / hukuki | `10-LICENSING/` |
| Branding, thumbnail, renk paleti | `07-BRANDING/` |
| Dosya isimlendirme, PR kuralları | `CONTRIBUTING.md` |

Bir görev birden fazla satıra giriyorsa (örn. "yeni karakter tanıtım videosu için başlık
yaz") ilgili tüm dosyaları oku, sadece birini değil.

---

## 2. Bilinen Çelişki: `00-CORE/` vs `11-DOCS/`

Repoda iki paralel doküman seti var:

- **`00-CORE/`** — orijinal, teknik, üretimde gerçekten kullanılan canon (karakter ölçüleri,
  renk kodları, kamera kuralları, süreklilik kuralları). `CONTRIBUTING.md`'deki "Tek Kaynak
  Prensibi" tablosu bu klasörü referans alır.
- **`11-DOCS/`** — sonradan eklenmiş "v3.0 bible" seti (ör. `04_CHARACTER_BIBLE.md`,
  `05_WORLD_BIBLE.md`, `09_YOUTUBE_STRATEGY.md`). Bazı dosyalar kendini de "source of truth"
  ilan ediyor ama `00-CORE` ile aynı ayrıntı seviyesinde değil ve bazı noktalarda (örn. bölüm
  süresi, karakter sayısı) farklı sayılar içerebilir.

**Kural:** Teknik/görsel/karakter/dünya canon için **`00-CORE/` kazanır**. `11-DOCS/`
anlatısal bağlam, strateji ve narrative derinlik için kullanılır. İki kaynak doğrudan çelişiyorsa:

1. Sessizce birini seçip devam etme.
2. Çelişkiyi kullanıcıya bildir, hangisinin geçerli olacağını sor.
3. Kullanıcı onaylayınca hangi dosyanın güncelleneceğine karar ver.

> **Çözülen çelişkiler:**
> - Bölüm süresi: **120 sn** (8 shot × 15 sn) — sıkı, uzatma yok.
> - YouTube birleştirme: **3 × 120 sn = ~6 dk** — tema bazlı birleştirme.
> - Opa's Storytime: 300 sn (5 dakika) olarak kilitlenmiştir.
> - Sezon yapısı: S1 (6 karakter), S2 (4 yeni karakter), S3 (4 yeni karakter) olarak ayrılmıştır.
> - Platform stratejisi: Tek ana içerik (YouTube) → Diğer platformlar için dönüşüm.
> - Shorts kalitesi: 16:9 üretirken karakteri ortadaki %60 güvenli bölge içinde tut.
> - **ALTIN KURAL: Kalite > Süre. Uzatma yok.**

---

## 3. Yeni Bir Strateji/Standart Dosyası Eklerken

1. Önce bu tabloda (§1) veya `CONTRIBUTING.md`'de aynı konuyu kapsayan bir dosya var mı kontrol et.
2. Varsa, üstüne yazma / tekrar etme. Yeni dosyadan eskiye, eskiden yeniye kısa bir
   cross-reference notu ekle (bkz. `00-CORE/17_VIDEO_GENERATION_STANDARD.md` ↔
   `00-CORE/18_VIDEO_STYLE_AND_RETENTION_STANDARD.md` örneği).
3. Yeni dosyayı bu AGENTS.md'deki routing tablosuna (§1) ekle.
4. `00-CORE/` içine bir teknik standart ekliyorsan `CONTRIBUTING.md`'deki "Tek Kaynak
   Prensibi" tablosuna da ekle.
5. `README.md`'deki "Dosya Sorumluluk Haritası" tablosuna da bir satır ekle.

---

## 4. Prompt Verirken Kullanılacak Şablon

Belirli bir standarda göre içerik üretilmesi istendiğinde şu formatı kullan:

```text
Use [ilgili dosya yolu].

[Görev tanımı — episode/karakter/dünya/tema/uzunluk gibi somut detaylarla]
```

Örnek:

```text
Use 00-CORE/30_YOUTUBE_METADATA_STANDARD.md.

Create YouTube title, description, tags, hashtags and Shorts metadata for this episode:
Episode: S01E10 — My Turn, Your Turn
Characters: Luca, Noah
Location: Central Square
Theme: Sharing, taking turns, teamwork
Length: 90 seconds
```

---

## 5. Belirsizlik Durumunda

Eğer:

- görev iki kaynak dosyayla çelişiyorsa,
- görev canon (karakter/dünya/senaryo) değiştirmeyi gerektiriyor görünüyorsa ama kullanıcı
  bunu açıkça istemediyse,
- ilgili konuda hiçbir dosya yoksa,

**dur ve kullanıcıya sor.** Tahmin ederek ilerleme.

---

*Bu dosya, repodaki tüm agent/tool etkileşimleri için giriş noktasıdır.*
*Diğer tüm kaynak dosyalar bu dosyadan yönlendirilir, bu dosya onların içeriğini tekrar etmez.*
*Versiyon: 1.2 — Shorts Production Standard, TODO.md, yeni seriler eklendi*
