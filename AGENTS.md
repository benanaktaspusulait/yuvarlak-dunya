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
- Episode script'leri (`POMPOM_HILLS_PRODUCTION/02_WORLDS/*/04_EPISODE_PACKAGES/*`)
- Production/teknik standartlar (`00-CORE/TECH_SPECS.md`, `00-CORE/17_VIDEO_GENERATION_STANDARD.md`,
  `00-CORE/VISUAL_STYLE_GUIDE.md`, `00-CORE/CONTINUITY_RULES.md`)

Bu dosyalar sadece kullanıcı açıkça "karakteri değiştir", "dünyayı güncelle", "senaryoyu
yeniden yaz" gibi bir talimat verdiğinde değiştirilir. Stratejik/yayın/metadata güncellemeleri
bu dosyalara dokunmaz.

---

## 1. Görev Türüne Göre Routing Tablosu

| Yapılacak iş | Önce oku |
|---|---|
| Yeni karakter ekleme/değiştirme | `00-CORE/CHARACTER_GUIDE.md`, `01-CHARACTERS/`, `CONTRIBUTING.md` §"Yeni Karakter" |
| Yeni dünya/mekan ekleme/değiştirme | `00-CORE/WORLD_BIBLE.md`, `POMPOM_HILLS_PRODUCTION/02_WORLDS/`, `CONTRIBUTING.md` §"Yeni Mekan" |
| Yeni bölüm/sahne yazımı | `00-CORE/SERIES_STRUCTURE.md`, `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/EPISODE_TEMPLATES/`, `00-CORE/CONTINUITY_RULES.md` |
| Opa's Storytime bölümü (interactive storytelling sub-series) | `00-CORE/31_OPA_INTERACTIVE_STORYTELLING_FORMAT.md`, ardından ilgili mekan (`POMPOM_HILLS_PRODUCTION/02_WORLDS/`) ve karakter (`01-CHARACTERS/`) dosyaları |
| Shot/video üretimi (kamera, renk, süreklilik, teknik) | `00-CORE/17_VIDEO_GENERATION_STANDARD.md`, `00-CORE/VISUAL_STYLE_GUIDE.md`, `00-CORE/VISUAL_CONTINUITY_RULES.md` |
| Video pacing / hook / retention stili, micro-opening & warm-closing / bumper (dış feedback dahil) | `00-CORE/18_VIDEO_STYLE_AND_RETENTION_STANDARD.md` |
| YouTube title / description / tags / Shorts metadata | `00-CORE/30_YOUTUBE_METADATA_STANDARD.md` |
| Yayın stratejisi, kanal büyümesi, publishing cadence, karakter/dünya rollout hızı | `11-DOCS/09_YOUTUBE_STRATEGY.md` (Channel Growth Decisions bölümü) |
| Ses / voice / seslendirme | `00-CORE/AUDIO_GUIDE.md`, `00-CORE/EPISODE_AUDIO_WORKFLOW.md`, `05-AI-PROMPTS/voice/` |
| Çocuk güvenliği / COPPA | `00-CORE/CHILD_SAFETY_RULES.md`, `10-LICENSING/COPPA_MADE_FOR_KIDS_CHECKLIST.md` |
| Yasak/negatif prompt listeleri | `00-CORE/NEGATIVE_PROMPTS.md` |
| Prompt değişkenleri (`{style}` `{camera}` `{lighting}`) | `00-CORE/VARIABLES.md` |
| Yayın öncesi kalite kontrol | `00-CORE/MASTER_QA_CHECKLIST.md`, `00-CORE/SCENE_QA_CHECKLIST.md`, `00-CORE/PRE_RENDER_CHECKLIST.md` |
| Altyazı (SRT/VTT) | `14-SUBTITLES/SRT_TEMPLATE.md`, `11-DOCS/12_SUBTITLE_STYLE_GUIDE.md`, `11-DOCS/15_SUBTITLE_WORKFLOW.md` |
| Üretim takibi (asset/tracker/takvim/bütçe) | `08-PRODUCTION/` (ör. `ASSET_TRACKER.md`, `EPISODE_TRACKER.md`, `PRODUCTION_CALENDAR.md`) |
| İçerik/format eşleştirme (long video ↔ Shorts ↔ sosyal medya) | `08-PRODUCTION/CONTENT_MATRIX.md` |
| Haftalık performans raporu | `08-PRODUCTION/WEEKLY_PERFORMANCE_REPORT.md` |
| Lisanslama / marka / hukuki | `10-LICENSING/` |
| Branding, thumbnail, renk paleti | `07-BRANDING/` |
| Dosya isimlendirme, PR kuralları, doğrulama script'leri | `CONTRIBUTING.md` |

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
anlatısal bağlam, strateji ve narrative derinlik için kullanılır (örn. karakterin "neden var
olduğu" gibi). İki kaynak doğrudan çelişiyorsa (örn. bölüm süresi 60s vs 60-90s):

1. Sessizce birini seçip devam etme.
2. Çelişkiyi kullanıcıya bildir, hangisinin geçerli olacağını sor.
3. Kullanıcı onaylayınca hangi dosyanın güncelleneceğine karar ver (mümkünse eski dosyaya
   "superseded by X" notu ekle, silme).

Bilinen açık çelişki örneği: `00-CORE/TECH_SPECS.md` / `SERIES_STRUCTURE.md` / `PRODUCTION_PIPELINE.md`
hâlâ "60 saniye" bölüm süresini teknik standart olarak tanımlıyor, ancak
`11-DOCS/09_YOUTUBE_STRATEGY.md` → Channel Growth Decisions §6 artık 60–90 saniyeyi ana
format yapıyor. Bu henüz çözülmedi — production canon dosyalarına dokunulmadan bekletiliyor.

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
*Versiyon: 1.0*
