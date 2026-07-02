# Contributing v3.0

Bu repo Pompom Hills / Yuvarlak Dunya prodüksiyon dosyasıdır. Katkılar; 3-4 yaş pedagojisi, görsel güvenlik ve üretim tutarlılığına göre değerlendirilir.

## Dizin Yapısı

```
yuvarlak-dunya/
├── 00-CORE/         ← Tek kaynak master dosyalar (sadece bu dosyalar güncellenir)
├── 01-CHARACTERS/   ← Karakter bible dosyaları
├── 02-WORLDS/       ← Mekan bible dosyaları
├── 03-PROPS/        ← Prop kütüphanesi
├── 04-SCENES/       ← Sahne dosyaları + şablonlar
├── 05-AI-PROMPTS/   ← AI üretim promptları
├── 06-ASSETS/       ← Referans görseller
├── 07-BRANDING/     ← Marka dosyaları
├── 08-PRODUCTION/   ← Üretim takibi
└── 09-ARCHIVE/      ← Eski dosyalar
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
02-WORLDS/01-central-square.md
04-SCENES/season-01/s01e01-hello-pompom-hills/01-kiko-intro.md
```

## Yeni Dosya Ekleme

### Yeni Karakter
1. `01-CHARACTERS/` dizinine `[sıra]-[isim].md` formatında dosya ekle
2. `00-CORE/CHARACTER_GUIDE.md`'yi güncelle
3. `05-AI-PROMPTS/voice/` dizinine ses promptu ekle

### Yeni Mekan
1. `02-WORLDS/` dizinine `[sıra]-[isim]-bible.md` formatında dosya ekle
2. `00-CORE/WORLD_BIBLE.md`'yi güncelle
3. `environment/` dizinine referans görsel ekle

### Yeni Bölüm
1. `04-SCENES/season-01/` dizininde `s01e[XX]-[bolum-adi]/` klasörü aç
2. `04-SCENES/_templates/EPISODE_TEMPLATE.md` şablonunu kullan
3. Her sahne için `04-SCENES/_templates/SCENE_TEMPLATE.md` şablonunu kullan

## Pull Request Checklist

- [ ] Yeni veya değişen promptlarda `{style}`, `{camera}`, `{lighting}` var.
- [ ] `NEGATIVE_PROMPTS.md` ile çelişen ifade yok.
- [ ] README dosya listesi güncel.
- [ ] Örnek görsel eklendiyse `.txt` metadata dosyası yanında.
- [ ] 3-4 yaş için korkutucu, hızlı, sert veya karmaşık sahne yok.
- [ ] Tek kaynak dosyalar (`00-CORE/`) güncellendi mi?
- [ ] Dosya isimlendirme standardına uygun mu?

---

*Bu belge katkıkılama kuralları için tek kaynaktır.*
*Son güncelleme: 2 Temmuz 2026*
