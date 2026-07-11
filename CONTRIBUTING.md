# Contributing v3.1

Bu repo Pompom Hills / Yuvarlak Dunya prodüksiyon dosyasıdır. Katkılar; 3-4 yaş pedagojisi, görsel güvenlik ve üretim tutarlılığına göre değerlendirilir.

## Dizin Yapısı

```
yuvarlak-dunya/
├── 00-CORE/         ← Tek kaynak master dosyalar
├── 01-CHARACTERS/   ← Karakter bible dosyaları + drawings/
├── POMPOM_HILLS_PRODUCTION/ ← Dünya-bazlı üretim paketleri (tek kaynak)
│   ├── 00_GLOBAL_RULES/     ← Şablonlar + global environment/world standartları
│   ├── 02_WORLDS/           ← Her dünya: canon bible + world-spec + hero view +
│   │                          o dünyada geçen bölüm paketleri (shots/overview/metadata)
│   └── 03_EPISODES/         ← Seri-seviyesi dosyalar (Opa's Storytime bumper'ları vb.)
├── 03-PROPS/        ← Prop kütüphanesi
├── 05-AI-PROMPTS/   ← AI üretim promptları
├── 06-ASSETS/       ← Referans görseller
├── 07-BRANDING/     ← Marka dosyaları + metadata/
├── 08-PRODUCTION/   ← Üretim takibi
├── 09-ARCHIVE/      ← Eski dosyalar
├── 10-LICENSING/    ← Lisanslama stratejisi
├── scripts/         ← Otomasyon scriptleri
├── 14-SUBTITLES/    ← Altyazı dosyaları
└── .github/         ← GitHub Actions
```

## Tek Kaynak Prensibi

Her konu için tek yetkili dosya vardır. Bu dosyalar `00-CORE/` dizinindedir:

| Konu | Tek Kaynak Dosya |
|------|-----------------|
| Duygu ve felsefe | `CREATIVE_BIBLE.md` |
| Görsel stil | `VISUAL_STYLE_GUIDE.md` |
| Dünya tanımı | `WORLD_BIBLE.md` |
| Karakter tanımı | `CHARACTER_GUIDE.md` |
| Bölüm yapısı | `SERIES_STRUCTURE.md` |
| Üretim akışı | `PRODUCTION_PIPELINE.md` |
| Teknik standartlar | `TECH_SPECS.md` |
| Ses standartları | `AUDIO_GUIDE.md` |
| Prompt değişkenleri | `VARIABLES.md` |
| Yasak listeler | `NEGATIVE_PROMPTS.md` |
| Süreklilik kuralları | `CONTINUITY_RULES.md` |
| Opa's Storytime serisi (format, playlist, bölüm isimlendirme) | `31_OPA_INTERACTIVE_STORYTELLING_FORMAT.md` |
| Series bumper / world micro-opening ayrımı ve dosya organizasyonu | `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/MICRO_OPENING_AND_CLOSING_STANDARD.md` |
| Shot'lar arası continuity workflow (@image1 zinciri, transition QA) | `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/SHOT_CONTINUITY_WORKFLOW.md` |
| Standalone shot + dosya-içi post-production transition notu (çok-shot'lu / world geçişli videolar) | `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/STANDALONE_SHOT_AND_TRANSITION_STANDARD.md` |
| OpenArt prompt `## Sound` bölümü + doğal sakinleştirici ambient ses (shot-level, müzik yok) | `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/NATURAL_CALMING_AMBIENCE_SOUND_STANDARD.md` |
| Sosyal medya görsel formatı (Story/Feed/YouTube platform seti) | `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/SOCIAL_MEDIA_IMAGE_FORMAT_STANDARD.md` |
| Arda's Stories alt-serisi (format, duration architecture, episode naming) | `POMPOM_HILLS_PRODUCTION/07_ARDAS_STORIES/FORMAT_STANDARD.md` |

**Kural:** Bir kural bir kez yazılır. Bölüm dosyaları bu kurallara referans verir, tekrar etmez.

## Prompt Ekleme Kuralları

1. Prompt metni İngilizce yazılır.
2. Açıklama, kullanım notu ve onay süreci Türkçe kalabilir.
3. Her prompt `{style}`, `{camera}`, `{lighting}` değişkenlerini içermek zorundadır.
4. Her prompt karakter kilitlerini korur:
   - Kiko = 100 birim, coral shirt #F8BBD0, white shorts #FFFFFF.
   - Mimi = 80 birim, soft blue #90CAF9, yellow t-shirt #FFF59D.
   - Opa = 120 birim, low-staged, warm green #A5D6A7, gold glasses #FFD54F, brown shawl #A1887F.
5. Her prompt `NEGATIVE_PROMPTS.md` ile birlikte kullanılacak şekilde yazılır.
6. Görselde yazı sadece moodboard, poster veya palette card gibi özellikle belirtilen assetlerde kullanılabilir.

## Görsel Onay Süreci

| Aşama | Kontrol | Onay Kriteri |
| --- | --- | --- |
| 1. Prompt QA | Değişkenler var mı? | `{style}`, `{camera}`, `{lighting}` eksiksiz |
| 2. Pedagoji QA | 3-4 yaş için güvenli mi? | Korku, şiddet, utandırma, bağırma yok |
| 3. Tasarım QA | Form dili doğru mu? | Yuvarlak, pastel, oyuncak gibi |
| 4. Karakter QA | Ölçek ve kıyafet doğru mu? | Kiko/Mimi/Opa kilitleri bozulmamış |
| 5. Metadata QA | Tekrar üretilebilir mi? | Prompt, model, seed, negative prompt kayıtlı |

## Dosya İsimlendirme

Dosya adları küçük harf, tire ayracı ve sürüm bilgisiyle yazılır.

```text
01-CHARACTERS/01-kiko.md
POMPOM_HILLS_PRODUCTION/02_WORLDS/CENTRAL_SQUARE/00_CANON/01-central-square-bible.md
POMPOM_HILLS_PRODUCTION/02_WORLDS/CENTRAL_SQUARE/04_EPISODE_PACKAGES/S01E01_HELLO_POMPOM_HILLS/01_SHOTS/shot-01-kiko-discovery.md
```

## Yeni Dosya Ekleme

### Yeni Karakter
1. `01-CHARACTERS/` dizinine `[sıra]-[isim].md` formatında dosya ekle
2. `00-CORE/CHARACTER_GUIDE.md`'yi güncelle
3. `05-AI-PROMPTS/voice/` dizinine ses promptu ekle

### Yeni Mekan
1. `POMPOM_HILLS_PRODUCTION/02_WORLDS/<WORLD_NAME>/` altında dünya klasörünü aç
   (bkz. `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/EPISODE_TEMPLATES/WORLD_BIBLE_TEMPLATE.md`)
2. `00_CANON/[sıra]-[isim]-bible.md` formatında bible dosyasını ekle
3. `02_WORLD_SPEC/[sıra]-[isim]-world-spec.md` formatında world-spec dosyasını ekle
4. `00-CORE/WORLD_BIBLE.md`'yi güncelle
5. `01_HERO_VIEW/` dizinine referans görsel ekle

### Yeni Bölüm
1. İlgili dünyanın altında `POMPOM_HILLS_PRODUCTION/02_WORLDS/<WORLD_NAME>/04_EPISODE_PACKAGES/`
   dizininde `S01Exx_BOLUM_ADI/` klasörünü aç (bkz. mevcut paketler örnek olarak)
2. `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/EPISODE_TEMPLATES/EPISODE_TEMPLATE.md` şablonunu kullan
3. Her sahne için `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/EPISODE_TEMPLATES/SCENE_TEMPLATE.md` şablonunu kullan
4. Shot dosyalarını paketin `01_SHOTS/` alt klasörüne ekle

## Pull Request Checklist

- [ ] Yeni veya değişen promptlarda `{style}`, `{camera}`, `{lighting}` var.
- [ ] `NEGATIVE_PROMPTS.md` ile çelişen ifade yok.
- [ ] README dosya listesi güncel.
- [ ] Örnek görsel eklendiyse `.txt` metadata dosyası yanında.
- [ ] 3-4 yaş için korkutucu, hızlı, sert veya karmaşık sahne yok.
- [ ] Tek kaynak dosyalar (`00-CORE/`) güncellendi mi?
- [ ] Dosya isimlendirme standardına uygun mu?

---

## Otomasyon & Doğrulama

### Script'ler

`13-SCRIPTS/` klasöründe 3 doğrulama scripti bulunur:

| Script | Amaç |
|--------|------|
| `validate-naming.sh` | NN-slug isimlendirme doğrulaması |
| `validate-continuity.py` | Karakter ölçek ve renk paleti kontrolü |
| `lint-prompts.py` | Prompt değişken ve negatif liste uyumluluk |

### Çalıştırma

```bash
# Tüm scriptleri çalıştır
bash 13-SCRIPTS/validate-naming.sh
python3 13-SCRIPTS/validate-continuity.py
python3 13-SCRIPTS/lint-prompts.py

# veya tek seferde
./13-SCRIPTS/validate-naming.sh && python3 13-SCRIPTS/validate-continuity.py && python3 13-SCRIPTS/lint-prompts.py
```

### GitHub Actions

`.github/workflows/validate.yml` dosyası PR ve push'larda otomatik olarak çalışır.

---

*Bu belge katkıkılama kuralları için tek kaynaktır.*
*Son güncelleme: 2 Temmuz 2026*
*Versiyon: v3.1*
