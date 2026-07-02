# Changelog

Bu dosya Pompom Hills repo sürüm geçmişini tutar.

## v3.0 - Büyük Yeniden Yapılandırma

### Added

- `00-CORE/` dizini: Tek kaynak master dosyalar (CREATIVE_BIBLE, VISUAL_STYLE_GUIDE, WORLD_BIBLE, CHARACTER_GUIDE, SERIES_STRUCTURE, PRODUCTION_PIPELINE, TECH_SPECS, AUDIO_GUIDE, VARIABLES, NEGATIVE_PROMPTS, CONTINUITY_RULES, BATCH_WORKFLOW)
- `01-CHARACTERS/` dizini: 13 karakter bible dosyası (tek kaynak)
- `02-WORLDS/` dizini: 27 mekan bible dosyası (tek kaynak)
- `03-PROPS/` dizini: Prop kütüphanesi
- `04-SCENES/_templates/` dizini: SCENE_TEMPLATE.md ve EPISODE_TEMPLATE.md
- `05-AI-PROMPTS/` dizini: Tüm AI prompt dosyaları ve ses dosyaları
- `06-ASSETS/` dizini: Referans görseller
- `07-BRANDING/` dizini: Marka ve sosyal medya dosyaları
- `08-PRODUCTION/` dizini: TODO.md, EPISODE_TRACKER.md, PRODUCTION_SCHEDULE.md, QC_CHECKLIST.md, ASSET_TRACKER.md, LOCATION_ANALYSIS.md, CHARACTER_ANALYSIS.md, SEASON_2_PLAN.md
- `10-LICENSING/` dizini: LICENSING_STRATEGY.md (UK merkezli lisanslama stratejisi), UK_TRADEMARK_GUIDE.md (trademark başvuru rehberi), LICENSING_PITCH_DECK.md (lisanslama sunumu), PRODUCT_SPECIFICATIONS.md (ürün kategorisi spesifikasyonları), LICENSE_AGREEMENT_TEMPLATE.md (lisans anlaşması şablonu)
- `PROJECT_OVERVIEW.md` — Kapsamlı proje çerçeve belgesi
- `09-ARCHIVE/` dizini: Eski/arsiv dosyalar

### Changed

- `README.md`: Yeni dizin yapısına göre tamamen yeniden yazıldı
- `CHANGELOG.md`: v3.0 girişi eklendi
- İçerik birleştirme: Çakışan dosyalar tek kaynakta birleştirildi
  - VISUAL_STYLE_GUIDE: Root + POMPOM_HILLS birleştirildi
  - PRODUCTION_PIPELINE: Root + PRODUCTION_RULES birleştirildi
  - WORLD_BIBLE: Root + WORLD_BUILD_DESCRIPTION birleştirildi
  - CHARACTER_GUIDE: CHARACTER_REFERENCE_GUIDE + CHARACTER_DESIGN_GUIDE birleştirildi
  - CONTINUITY_RULES: 3 farklı süreklilik dosyası birleştirildi

### Removed (09-ARCHIVE/ taşındı)

- `WORLD_BUILD_DESCRIPTION.md` → WORLD_BIBLE.md'ye birleştirildi
- `CHARACTER_DESIGN_GUIDE.md` → CHARACTER_GUIDE.md'ye birleştirildi
- `NAMING_REFINEMENT.md` → SERIES_STRUCTURE.md'ye taşındı
- `OPENART_WORLD_PROMPT_PACK.md` → 05-AI-PROMPTS/ taşındı
- `OPENART_WORLD_DISCOVERY.md` → PRODUCTION_PIPELINE.md'ye taşındı
- `OPENART_COMPACT_PROMPT_TEMPLATE.md` → 04-SCENES/_templates/ taşındı
- `VIDEO_CONTINUATION_RULES.md` → CONTINUITY_RULES.md'ye birleştirildi
- `SCENE_CONTINUATION_TEMPLATE.md` → CONTINUITY_RULES.md'ye birleştirildi
- `REUSABLE_EPISODE_FORMAT.md` → SERIES_STRUCTURE.md'ye taşındı
- `MASTER_PROMPTS.md` → 05-AI-PROMPTS/ taşındı
- `PRODUCTION_RULES.md` → PRODUCTION_PIPELINE.md'ye birleştirildi
- `POMPOM_HILLS/` dizini → 09-ARCHIVE/ taşındı (içerik yeni yapıya taşındı)
- `characters/` dizini → 09-ARCHIVE/ taşındı (içerik 01-CHARACTERS/ taşındı)
- `02-WORLDS/` dizini → 09-ARCHIVE/ taşındı (içerik 02-WORLDS/ taşındı)
- `03-PROPS/` dizini → 09-ARCHIVE/ taşındı (içerik 03-PROPS/ taşındı)
- `ai-prompts/` dizini → 09-ARCHIVE/ taşındı (içerik 05-AI-PROMPTS/ taşındı)
- `Color/` dizini → 09-ARCHIVE/ taşındı (içerik 07-BRANDING/ taşındı)
- `scenes/` dizini → 09-ARCHIVE/ taşındı (içerik 04-SCENES/ taşındı)

### Philosophy

- Tek kaynak prensibi: Her konu için tek yetkili dosya
- Sıfır içerik tekrarı: Çakışan dosya kalmadı
- Tutarlı organizasyon: Tek dizin yapısı
- 1000+ video ölçeklenebilirliği: Şablon sistemi ile hızlı bölüm üretimi

## v2.1 - OpenArt Production Pipeline Pass

### Added

- `PRODUCTION_RULES.md` oluşturuldu (daha önce `README.md`'de listeliydi ama dosya yoktu):
  production pipeline felsefesi, LOCKED kuralları, OpenArt World & Hero Pack kuralları,
  camera & scale, known failure modes, süreklilik ve etkileşim kuralları.
- `WORLD_BUILD_DESCRIPTION.md`: OpenArt World master prompt (§0) ve Production Pipeline & LOCKED
  kuralları (§0.1) bölümleri eklendi.
- `MASTER_PROMPTS.md`: Production Pipeline, World Reference & Hero Pack ve OpenArt Failure Modes
  hızlı koruma bölümleri eklendi.
- `OPENART_WORLD_PROMPT_PACK.md`: Production pipeline notu, Hero Pack view cümleleri ve LOCKED
  environment cümlesi eklendi.
- `02-WORLDS/ENVIRONMENT_IMAGE_PROMPTS.md`: World reference & Hero Pack production notu eklendi.
- `NEGATIVE_PROMPTS.md`: "OpenArt Production Failure Modes" negatif bloğu ve locked-world pozitif
  pekiştirme cümlesi eklendi.

### Changed

- `README.md`: `PRODUCTION_RULES.md` açıklaması genişletilerek production pipeline kapsamı yansıtıldı.
- `WORLD_BUILD_DESCRIPTION.md`: coğrafya/karakter tutarlılık düzeltmeleri (büyük ponpon ağaç
  Central Square'da, Kiko'nun evi Flower Hill'de) ve yazım düzeltmeleri yapıldı.

### Fixed — Environment ID & Hero Image Reconciliation

- `ENVIRONMENT_BIBLE_GENERATOR.md` mekan tablosu canonical hâle getirildi: 1–24 render plate
  mekanları gerçek `environment/*.png` dosyalarıyla ve ENV-001…024 ID'leriyle birebir eşleşiyor;
  Flower/Tree/Stone Hill artık 25–27 (background, render plate yok) olarak listeleniyor. Yanlış
  Butterfly Meadow örneği ENV-020 → ENV-017 düzeltildi.
- Üç tepe bible'ındaki çift (duplicate) ENV ID'leri düzeltildi: Flower Hill ENV-003 → ENV-025,
  Tree Hill ENV-005 → ENV-026, Stone Hill ENV-006 → ENV-027. Artık 27 mekan da benzersiz ID taşıyor.
- 11 bible'daki kırık `File:` referansları gerçek dosya adlarına düzeltildi (apostrof/boşluk/büyük
  harf temizlendi; ör. `9-poppy's-bakery.png` → `9-poppys-bakery.png`, `20-Wish-Pond.png` →
  `20-wish-pond.png`). Central Square gerçek konumu olan `1-central-square/1-central-square.png`'e işaret ediyor.

### Production Philosophy

- OpenArt bir image generator değil, **production engine**'dir.
- Consistency > beauty. Production quality > speed.
- Environment / Character / Giant Pompom Tree LOCKED.

## v2.1 - Production Readiness Pass

### Added

- `CHANGELOG.md`
- `CONTRIBUTING.md`
- `NEGATIVE_PROMPTS.md`
- `LICENSE`
- `examples/` klasörü için PNG preview ve metadata standardı
- Tüm AI prompt packlerinde `{style}`, `{camera}`, `{lighting}` değişkenleri
- `scenes/` klasörü, sahne yazım standardı ve S01E01 Kiko/Mimi tanıtım sahneleri

### Changed

- `README.md` v2.1 prodüksiyon giriş dosyası olarak yeniden düzenlendi.
- `WORLD_BIBLE_v2.1.md` ve `CHARACTER_REFERENCE_GUIDE_v2.1.md` ana kaynak dosyaları olarak korundu.
- `SERIES_STRUCTURE_v2.1.md` adıyla seri stratejisi v2.1 sürümüne taşındı.
- AI prompt dosyaları daha kısa, ekip tarafından değişkenle yönetilebilir v2.1 template formatına alındı.
- Eski v1/v2.0 dosya referansları kaldırıldı.

### Production Rules

- Hedef yaş: 3-4.
- Format: 7 dakika x 26 bölüm, 3D.
- Ölçek: Kiko = 100 birim, Mimi = 80 birim, Opa = 120 birim.
- Görsel güvenlik: keskin köşe, sert gölge, gerçekçi doku, korku, şiddet, metin/watermark yasak.

## v2.0 - Studio Bible Draft

- 3D stüdyo standardında world bible ve character reference guide oluşturuldu.
- Ölçek, shader, hareket, ses ve DO/DONT listeleri eklendi.

## v1.0 - Initial Concept Pack

- İlk dünya, karakter, stil ve OpenArt prompt dokümanları oluşturuldu.
