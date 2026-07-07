# World Bible Template — Pompom Hills

> Bu dosya, yeni bir dünya/mekan bible'ı oluştururken kullanılacak şablondur.
> Her world bible bu template'e uymak zorundadır.
> Bu template, Little Forest düzeltmelerinden çıkarılan dersleri içerir.

---

## Kullanım

1. Bu dosyayı kopyala
2. `[WORLD_NAME]` kısımlarını gerçek dünya adıyla değiştir
3. Her bölümü doldur — boş bırakma
4. Tüm bölümlerin detaylı olduğundan emin ol (1-2 cümle yeterli değil)
5. Oluşturduktan sonra `validate-worlds.sh` ile doğrula

---

## Template

```markdown
# Environment Bible — [WORLD_NAME]

> **Version 4.0** — Current pipeline format.

---

\`\`\`
Environment ID: ENV-[XX]
File: POMPOM_HILLS_PRODUCTION/02_WORLDS/[WORLD_NAME]/
Version: 4.0
Location: [Pompom Hills konumu]
Type: [Exterior/Interior/Living World]
Bible: ✅
Hero View: ❌ — Pending
\`\`\`

---

## Overview

[2-3 cümlelik dünya tanımı. Bu, world'ün ne olduğunu anlatan ilk bölüm. Detaylı ol.]

---

## Purpose

[Bu dünya neden var? Ne amaçla kullanılıyor? 2-3 cümle.]

---

## Why This World Exists ⭐

[Bu dünya duygusal olarak neyi temsil ediyor? Çocuklar için ne anlama geliyor? 3-4 cümle.]

---

## Emotional Purpose

### How do children feel when they arrive?
[3-4 duygu]

### What stories naturally belong here?
[3-4 hikaye türü]

### What emotional experiences does this world support?
[3-4 deneyim]

---

## Play Philosophy

### Play style

| Feature | Description |
|---------|-------------|
| Open-ended | [Açık uçlu oyun] |
| Imagination | [Hayal gücü] |
| Cooperation | [İşbirliği] |
| Observation | [Gözlem] |
| Gentle movement | [Yumuşak hareket] |

### No rule-based games

- Yarış yok
- Puan yok
- Rekabet yok

### Natural interactions

- [3-4 doğal etkileşim]

---

## World Position

| Feature | Detail |
|---------|--------|
| Coğrafya | [Konum tanımı] |
| Komşu world'ler | [Komşu mekanlar] |
| Ulaşım | [Nasıl gidilir] |
| Rakım | [Yükseklik/düz] |

```
[ASCII harita]
```

---

## Visual Identity

### Primary Visual Anchor

**[ANA LANDMARK TANIMI] — bu world'ün tanınmasını sağlayan ana öğe.**

[Landmark'ın ne olduğu, neden önemli olduğu, nasıl tanımlandığı]

### Visual Identity

[World'ün görsel kimliği — 6-8 maddelik liste. HER madde somut ve spesifik olmalı.]

Example:
```text
[World Name] is not just [generic description].
Its visual identity is:
- [landmark 1]
- [landmark 2]
- [detail 3]
- [detail 4]
- [detail 5]
```

### Silhouette

[Kısa tanım — uzaktan nasıl görünür]

### Character

[Nesnelerin nasıl göründüğü — yumuşak, yuvarlak, vb.]

### Mood

[Atmosfer — sıcak, davetkar, vb.]

---

## Spatial Layout

```
[Detaylı ASCII harita — tüm zone'ları gösterir]
```

### Key landmarks

| Landmark | Position | Description |
|----------|----------|-------------|
| [Landmark 1] | [Pozisyon] | [Açıklama] |
| [Landmark 2] | [Pozisyon] | [Açıklama] |
| [Landmark 3] | [Pozisyon] | [Açıklama] |

---

## Props

| Prop ID | Description | Reusable? | Notes |
|---------|-------------|-----------|-------|
| [PROP-01] | [Açıklama] | ✅ | [Not] |
| [PROP-02] | [Açıklama] | ✅ | [Not] |

---

## Camera Rules

| Rule | Standard |
|------|----------|
| Default lens | [mm] |
| Camera height | [m] (child eye-level) |
| Establishing shot | [Tanım] |
| Medium shot | [Tanım] |
| Close-up | [Tanım] |
| Movement | [Hareket türü] |
| Yasak | [Yasaklanan hareketler] |

---

## Generation Workflow

```
1. Load Hero View reference (when available)
        ↓
2. Apply World Specification
        ↓
3. Insert characters (10–12% of frame)
        ↓
4. Apply scene-specific prompt
        ↓
5. Generate shot
        ↓
6. Check reject rules
        ↓
7. Accept or regenerate
```

---

## Soundscape

### Primary sounds

| Sound | Source | When |
|-------|--------|------|
| [Ses 1] | [Kaynak] | [Ne zaman] |
| [Ses 2] | [Kaynak] | [Ne zaman] |

### Sound identity

```
[2-3 cümlelik ses kimliği]
```

### Forbidden sounds

- [Yasak ses 1]
- [Yasak ses 2]

---

## Forbidden

### Visual

- [Görsel yasak 1]
- [Görsel yasak 2]

### Behavioural

- [Davranış yasağı 1]
- [Davranış yasağı 2]

---

## Story Opportunities

| Theme | Story idea |
|-------|------------|
| [Tema 1] | [Hikaye fikri] |
| [Tema 2] | [Hikaye fikri] |

---

## Emotional Tone

| Emotion | Intensity | When |
|---------|-----------|------|
| [Duygu 1] | [Yoğunluk] | [Ne zaman] |
| [Duygu 2] | [Yoğunluk] | [Ne zaman] |

---

## Production Notes

- [Üretim notu 1]
- [Üretim notu 2]
- Hero View henüz oluşturulmamıştır — production öncesi oluşturulmalıdır.

---

## Visual Richness & World Charm

### Richness layers

| Layer | Element | Purpose |
|-------|---------|---------|
| Foreground | [Öğe] | [Amaç] |
| Mid-ground | [Öğe] | [Amaç] |
| Background | [Öğe] | [Amaç] |

### World charm

[3-4 cümlelik world charm tanımı]

### Forbidden Clutter

```
✗ [Yasak 1]
✗ [Yasak 2]
✗ [Yasak 3]
```

---

## World Identity Lock

**Primary visual anchor:** [ANA LANDMARK] must be visible in the main [WORLD] Hero View. It is the main landmark that makes the world recognisable.

**[WORLD NAME] is recognised by:**
- [Tanım 1]
- [Tanım 2]
- [Tanım 3]
- [Tanım 4]

**Reject if:**
- [Ret kriteri 1]
- [Ret kriteri 2]
- [Ret kriteri 3]

**[WORLD NAME] is not "[generic description]." [WORLD NAME] is [specific identity with primary landmark].**

---

## Hero View Technical Specification

| Field | Value |
|-------|-------|
| Resolution | 1920×1080, 16:9 |
| Format | PNG, 16-bit |
| Naming | `01-hero-view.png` |
| Content | [İçerik tanımı] |
| Characters | None (environment only) |
| Status | ❌ Pending |

---

## Camera Identity

| Rule | Standard |
|------|----------|
| Default lens | [mm] |
| Camera height | [m] (child eye-level) |
| Establishing | [Tanım] |
| Characters | Small (10–12% of frame) |
| Movement | [Hareket türü] |
| Yasak | [Yasaklar] |

---

## Lighting Identity

| Condition | Standard |
|-----------|----------|
| Daylight | [Tanım] |
| Golden hour | [Tanım] |
| Overcast | [Tanım] |
| Night | [Tanım] |

**Kural:** [Aydınlatma kuralı]

---

## Colour Identity

### Primary palette

| Element | Colour | Hex |
|---------|--------|-----|
| [Öğe 1] | [Renk] | [Hex] |
| [Öğe 2] | [Renk] | [Hex] |
| [Öğe 3] | [Renk] | [Hex] |

### Atmosphere

```
[2-3 cümlelik renk atmosferi]
```

---

## Environmental Sound Identity

| Element | Sound | Volume |
|---------|-------|--------|
| [Öğe 1] | [Ses] | [Ses seviyesi] |
| [Öğe 2] | [Ses] | [Ses seviyesi] |

---

## Continuity Rules

Across all [WORLD] shots:
- [Süreklilik kuralı 1]
- [Süreklilik kuralı 2]
- [Süreklilik kuralı 3]
- [Süreklilik kuralı 4]

---

## Production QA

### Before generation

- [ ] [QA kontrol 1]
- [ ] [QA kontrol 2]

### After generation

- [ ] [QA kontrol 3]
- [ ] [QA kontrol 4]

---

## Canonical Reusable Assets

| Asset ID | Description | Reusable across |
|----------|-------------|-----------------|
| [ASSET-01] | [Açıklama] | All [WORLD] episodes |

---

## World Navigation

```
[Komşu world'ler arası harita]
```

### Entry points

| From | To | Path |
|------|----|------|
| [World A] | [WORLD] | [Yol] |

---

## View Transition Rules

| From | To | Method |
|------|----|--------|
| Hero View | Character medium | Gentle push-in |
| Wide establishing | Medium on characters | Slow pan |
| Character medium | Close-up | Gentle push-in |
| Any view | Hero View | Slow pull-back |

---

## Character Occupancy

| Character | Role | Frequency |
|-----------|------|-----------|
| [Karakter 1] | [Rol] | [Sıklık] |

---

## Typical Episode Usage

| Episode | Characters | Story | Duration |
|---------|------------|-------|----------|
| [Bölüm] | [Karakterler] | [Hikaye] | [Süre] |

---

## Common Generation Failures

| # | Failure | Prevention |
|---|---------|------------|
| 1 | [Hata 1] | [Önlem 1] |
| 2 | [Hata 2] | [Önlem 2] |

---

## Video Generation Rules

| Rule | Standard |
|------|----------|
| Camera | [mm], child eye-level |
| Movement | [Hareket türü] |
| Lighting | [Aydınlatma türü] |
| Characters | 10–12% of frame, never larger |
| Sound | Natural ambience only, no music tracks |
| Yasak | [Yasaklar] |

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 4.0 | [Tarih] | Initial canon bible created |
```

---

## Kontrol Listesi

Her world bible oluşturulduktan sonra bu listeyi kontrol et:

### Zorunlu Bölümler (boş bırakılamaz)

- [ ] Overview (2+ cümle)
- [ ] Purpose (2+ cümle)
- [ ] Why This World Exists ⭐ (3+ cümle)
- [ ] Emotional Purpose (4 alt bölüm)
- [ ] Play Philosophy (tablo + etkileşimler)
- [ ] World Position (tablo + ASCII harita)
- [ ] Visual Identity (6+ maddelik liste + primary anchor)
- [ ] Spatial Layout (ASCII harita + landmark tablosu)
- [ ] Props (tablo)
- [ ] Camera Rules (tablo)
- [ ] Soundscape (ses tablosu + kimlik)
- [ ] Forbidden (görsel + davranış)
- [ ] Story Opportunities (tablo)
- [ ] Emotional Tone (tablo)
- [ ] Production Notes (detaylı)
- [ ] Visual Richness & World Charm (katmanlar +charm + forbidden clutter)
- [ ] World Identity Lock (primary anchor + ret kriterleri)
- [ ] Hero View Technical Specification (tablo)
- [ ] Camera Identity (tablo)
- [ ] Lighting Identity (tablo + kural)
- [ ] Colour Identity (palet tablosu + atmosfer)
- [ ] Environmental Sound Identity (tablo)
- [ ] Continuity Rules (madde listesi)
- [ ] Production QA (kontrol listesi)
- [ ] Canonical Reusable Assets (tablo)
- [ ] World Navigation (harita + giriş noktaları)
- [ ] View Transition Rules (tablo)
- [ ] Character Occupancy (tablo)
- [ ] Typical Episode Usage (tablo)
- [ ] Common Generation Failures (tablo)
- [ ] Video Generation Rules (tablo)
- [ ] Changelog (tablo)

### Nitelik Kontrolleri

- [ ] Hiçbir bölüm 1-2 cümle değil (detaylı)
- [ ] Primary visual anchor net ve spesifik
- [ ] Ret kriterleri açık
- [ ] Colour palette hex kodları ile
- [ ] Continuity rules güçlü ve spesifik
- [ "Generic" tanım yok (örn. "yuvarlak ağaçlar, yeşil" gibi)

---

*Template: 7 Temmuz 2026*
*Kullanım: Yeni world bible oluştururken bu dosyayı şablon olarak kullan*
