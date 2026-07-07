# Environment Bible — Music Hill

> **Version 4.0** — Full canon definition, current pipeline format.

---

```
Environment ID: ENV-028
File: POMPOM_HILLS_PRODUCTION/02_WORLDS/MUSIC_HILL/01_HERO_VIEW/
Version: 4.0
Location: World map position 28 — Pompom Hills doğu kenarı
Bible: ✅
Hero View: ❌ — Pending
```

> The canonical creative definition is contained within this document.
> **The Canon Hero View (`01-hero-view.png`) is the primary visual reference.**
> Whenever text descriptions and the Hero View appear to disagree,
> the Hero View takes precedence.
> A dense generation instruction set is maintained in `02-world-spec.md`.

---

## Overview

Music Hill, Pompom Hills'in müziğin yaşadığı tepesi. Rüzgarın ağaçlardan geçerken çıkardığı seslerin bir orkestraya dönüştüğü, her yaprağın bir enstrüman gibi titreştiği yumuşak bir tepe.

---

## Purpose

Müzik keşfi ve yaratıcılık mekanı. Çocuklar burada doğanın seslerini dinler, ritim hisseder, birlikte şarkı söyler ve müziğin her yerde olduğunu keşfeder.

---

## Why This World Exists ⭐

Music Hill, çocuklar için "dinleme" anının somut karşılığıdır. Rüzgar, yapraklar, kuşlar — hepsi birer sestir. Bu mekan çocukların kulaklarını açar ve "sessizlik bile bir sestir" düşüncesini güvenle keşfetmelerini sağlar.

---

## Emotional Purpose

### Why does this place exist emotionally?

Music Hill, neşe ve yaratıcılığı temsil eder. Sesler dünyası çocuklara rhythm ve melody hissini öğretir; birlikte müzik yapmak bağlılık duygusunu güçlendirir.

### How do children feel when they arrive?

Meraklı, neşeli, ritmik. Seslerin büyüsüne kapılmış, kulaklarını dikip dinleyen çocuklar.

### What stories naturally belong here?

Rüzgarla şarkı söyleme, ağaç tınılarını keşfetme, birlikte ritim tutma, kuş seslerini taklit etme, yaprakları çalıp müzik yapma.

### What emotional experiences does this world support?

Neşe · Yaratıcılık · Keşif · Birlikte müzik · Ritim hissi

---

## Play Philosophy

### Play style

| Feature | Description |
|---------|-------------|
| Open-ended | Sesleri dinle, ritim bul, şarkı kur |
| Imagination | Ağaçlardan enstrüman yapma, rüzgarla beste |
| Cooperation | Birlikte ritim tutma, birlikte şarkı söyleme |
| Observation | Farklı sesleri tanıma ve adlandırma |
| Gentle movement | Ritimle sallanma, yumuşak dans |

### No rule-based games

- Yarış yok
- Puan yok
- Rekabet yok

### Natural interactions

- Rüzgar estiğinde ağaçları dinleme
- Kuş seslerini taklit etme
- Yaprakları sallayarak ritim oluşturma
- Birlikte basit şarkılar söyleme
- Sessiz anlarda bile sesleri fark etme

---

## World Position

| Feature | Detail |
|---------|--------|
| Coğrafya | Pompom Hills'in doğu kenarında yumuşak bir tepe |
| Komşu world'ler | Little Forest (batı), Rainbow Creek (güney) |
| Ulaşım | Little Forest'ten patika ile |
| Rakım | Orta yükseklikte — Cloud Hill'den alçak, Flower Hill'den yüksek |

---

## Visual Identity

### Silhouette

- Yumuşak yuvarlak tepe — yumuşak eğimli, keskin köşe yok
- Tepenin üzerinde 3–5 müzik ağacı — yuvarlak yaprak kümeleri
- Ağaçlar farklı yüksekliklerde — en uzun olan tepeye yakın
- Patika tepenin sol altından zirveye doğru kıvrımlı

### Character

- Her ağaç bir "enstrüman" — yaprak kümeleri tını veren çanlar gibi
- Ağaç gövdeleri yumuşak kahverengi #A1887F
- Yaprak kümeleri müzik yeşili #66BB6A — yuvarlak, dolgun
- Çiçekler melodi pembesi #F48FB1 — ağaç diplerinde doğal dağılım

### Mood

- Sıcak, davetkar, ritmik
- Her ağaç şarkı söylüyormuş gibi görünür
- Hava canlı ama sakin

---

## Spatial Layout

```
                    [Zirve - 3 ağaç]
                   /                \
    [Sol ağaç]   /   [Patika]       [Sağ ağaç]
               /                     /
    [Çiçekler] /    [Taşlar]        / [Çiçekler]
             /                     /
    [Giriş - alt sol]           [Giriş - alt sağ]
```

### Key landmarks

| Landmark | Position | Description |
|----------|----------|-------------|
| Music Tree Cluster | Zirve | 3 ağaç birlikte — ana landmark |
| Single Music Tree | Sol | Yalnız ağaç — keşif noktası |
| Single Music Tree | Sağ | Yalnız ağaç — dinlenme noktası |
| Winding Path | Sol alt → Zirve | Kıvrımlı patika |
| Stepping Stones | Patika üzerinde | Yuvarlak, düz taşlar |
| Flower Clusters | Ağaç diplerinde | Melodi pembesi çiçekler |

---

## Props

| Prop ID | Description | Reusable? | Notes |
|---------|-------------|-----------|-------|
| MH-TREE-01 | Music tree (büyük) | ✅ | Yuvarlak yaprak kümeleri, tını veren |
| MH-TREE-02 | Music tree (küçük) | ✅ | Daha alçak, daha kompakt |
| MH-FLOWER-01 | Melody pink flower | ✅ | Yuvarlak, yumuşak |
| MH-STONE-01 | Stepping stone | ✅ | Yuvarlak, düz, coral |
| MH-PATH-01 | Winding path | ✅ | Warm sand rengi |
| MH-LEAF-CHIME | Leaf chime cluster | ✅ | Yaprak çanı — ağaç üzerinde |

---

## Camera Rules

| Rule | Standard |
|------|----------|
| Default lens | 35mm–50mm equivalent |
| Camera height | Child eye-level (0.70–1.10m) |
| Establishing shot | Wide from bottom of hill, looking up |
| Medium shot | Characters among trees, trees dominate |
| Close-up | Face readable, tree leaves soft in background |
| Movement | Slow pan up the hill, gentle push-in, locked-off |
| Yasak | Dutch angle, fisheye, shaky cam, fast zoom, dramatic crane |

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
| Leaf chimes | Ağaç yaprakları | Rüzgar estiğinde |
| Soft wind | Rüzgar | Sürekli |
| Bird calls | Kuşlar | Aralıklarla |
| Gentle footsteps | Karakterler | Yürüdüğünde |
| Leaf rustle | Yapraklar | Temas ettiğinde |

### Sound identity

```
Rhythmic, gentle, natural.
Music comes from nature — not from instruments.
Every sound is soft, warm, and inviting.
No loud sounds, no drums, no electronic music.
```

### Forbidden sounds

- Loud drums
- Electronic beats
- Realistic instrument sounds
- Traffic noise
- Human crowd noise
- Sudden loud sounds

---

## Forbidden

### Visual

- Sharp edges, thorns, thistles
- Realistic musical instruments (guitar, piano, drum)
- Modern objects (speakers, microphones, headphones)
- Neon colours, harsh contrasts
- Dark shadows, scary lighting
- Crowded scenes
- Fast-moving objects
- Text, watermarks, signs

### Behavioural

- Competition, racing, scoring
- Aggressive movement
- Loud shouting
- Instrument playing (characters listen, don't play)
-破坏 trees or flowers

---

## Story Opportunities

| Theme | Story idea |
|-------|------------|
| Music discovery | Ağaçların tınısını keşfetme |
| Rhythm | Birlikte ritim tutma |
| Listening | Sessizlikte bile sesleri bulma |
| Creativity | Doğadan müzik yapma |
| Friendship | Birlikte şarkı söyleme |

---

## Emotional Tone

| Emotion | Intensity | When |
|---------|-----------|------|
| Curiosity | Medium | İlk kez geldiğinde |
| Joy | High | Müzik duyduğunda |
| Wonder | High | Ağaçların tınısını keşfettiğinde |
| Calm | Medium | Dinlenirken |
| Connection | High | Birlikte müzik yaparken |

---

## Production Notes

- Music Hill, S01E24 "Music Trees" bölümünde kullanılmıştır.
- Noah (müzikçi) ve Arda (dansçı) bu mekanda etkileşime girer.
- Mekan sakin ve davetkar olmalı; fazla hareket veya kalabalık yasaktır.
- Ağaçlar ritmik olarak sallanmalı ama devrilmemeli.
- Hero View henüz oluşturulmamıştır — production öncesi oluşturulmalıdır.

---

## Visual Richness & World Charm

### Richness layers

| Layer | Element | Purpose |
|-------|---------|---------|
| Foreground | Flowers, grass detail | Depth |
| Mid-ground | Trees, path, stepping stones | Story space |
| Background | Sky, distant hills | Atmosphere |

### World charm

- Her ağaç kendine özgü bir tınıya sahip
- Rüzgar estiğinde yapraklar hafifçe sallanır
- Kuşlar ağaçlarda oturur, ara sıra şarkı söyler
- Stepping stones hafifçe parlak — sanki müzik çalıyormuş gibi

---

## World Identity Lock

```
LOCKED ELEMENTS:
- 3–5 music trees with round leaf clusters
- Tree trunks: soft brown #A1887F
- Tree leaves: musical green #66BB6A
- Flowers: melody pink #F48FB1
- Path: warm sand #FFE0B2
- Stepping stones: soft coral #FFAB91
- Sky: clear blue #81D4FA

DO NOT:
- Change tree shape or leaf cluster form
- Remove flowers or change their colour
- Add buildings, fences, or modern objects
- Change path colour or material
- Add realistic instruments
- Make the hill sharp or angular
```

---

## Hero View Technical Specification

| Field | Value |
|-------|-------|
| Resolution | 1920×1080, 16:9 |
| Format | PNG, 16-bit |
| Naming | `01-hero-view.png` |
| Content | Full hill with trees, path, flowers, sky |
| Characters | None (environment only) |
| Props | None (environment only) |
| Status | ❌ Pending — Hero View henüz oluşturulmamıştır |

---

## Camera Identity

| Rule | Standard |
|------|----------|
| Default lens | 35mm–50mm |
| Camera height | 0.70–1.10m (child eye-level) |
| Establishing | Wide, hill fills frame |
| Characters | Small (10–12% of frame) |
| Movement | Slow, gentle, locked-off preferred |
| Yasak | Fast movement, dramatic angles, Dutch angle |

---

## Lighting Identity

| Condition | Standard |
|-----------|----------|
| Daylight | Warm diffused sunlight, soft shadows |
| Golden hour | Gentle amber glow on tree leaves |
| Overcast | Soft grey with warm undertone |
| Night | Soft blue, never black; gentle glow |

**Kural:** Işık her zaman yumuşak ve davetkar olmalı. Sert gölge, dramatik kontrast veya karanlık atmosfer yasaktır.

---

## Colour Identity

### Primary palette

| Element | Colour | Hex |
|---------|--------|-----|
| Grass | Warm green | #81C784 |
| Trees (trunk) | Soft brown | #A1887F |
| Trees (leaves) | Musical green | #66BB6A |
| Flowers | Melody pink | #F48FB1 |
| Sky | Clear blue | #81D4FA |
| Path | Warm sand | #FFE0B2 |
| Stepping stones | Soft coral | #FFAB91 |

### Atmosphere

```
Warm, inviting, rhythmic.
Every colour feels like a note — soft, harmonious, alive.
No harsh contrasts. No cold tones. No neon.
```

---

## Environmental Sound Identity

| Element | Sound | Volume |
|---------|-------|--------|
| Wind through leaves | Soft chime-rustle | Low |
| Bird calls | Gentle tweets | Low–Medium |
| Footsteps on path | Soft crunch | Low |
| Leaf movement | Gentle rustle | Low |
| Silence | Warm ambient hum | Very Low |

---

## Continuity Rules

1. Tree positions must remain identical across shots
2. Path must wind the same way in every shot
3. Flower positions must remain identical
4. Stepping stones must not move
5. Sky must remain consistent (same cloud pattern)
6. Lighting must not change between shots
7. Characters may move; environment never moves

---

## Production QA

### Before generation

- [ ] Hero View reference loaded
- [ ] Character reference loaded
- [ ] Scene-specific prompt ready
- [ ] Lighting matching previous shot

### After generation

- [ ] Trees match bible (round leaf clusters, correct colours)
- [ ] Path visible and correct colour
- [ ] Flowers visible and correct colour
- [ ] Sky consistent
- [ ] No modern objects
- [ ] No sharp edges
- [ ] Characters 10–12% of frame
- [ ] No text or watermarks

---

## Canonical Reusable Assets

| Asset ID | Description | Reusable across |
|----------|-------------|-----------------|
| MH-TREE-01 | Large music tree | All Music Hill episodes |
| MH-TREE-02 | Small music tree | All Music Hill episodes |
| MH-FLOWER-01 | Melody pink flower | All Music Hill episodes |
| MH-STONE-01 | Stepping stone | All Music Hill episodes |
| MH-PATH-01 | Winding path section | All Music Hill episodes |
| MH-LEAF-CHIME | Leaf chime cluster | All Music Hill episodes |

---

## Production Summary

| Field | Value |
|-------|-------|
| Episodes used | S01E24 "Music Trees" |
| Characters | Noah, Arda |
| Props needed | Music trees, flowers, stepping stones |
| Lighting | Warm daylight |
| Complexity | Low–Medium |
| Hero View status | ❌ Pending |

---

## World Navigation

```
Little Forest ←→ Music Hill ←→ Rainbow Creek
     (batı)        (merkez)        (güney)
```

### Entry points

| From | To | Path |
|------|----|------|
| Little Forest | Music Hill | Patika ile batıdan giriş |
| Rainbow Creek | Music Hill | Patika ile güneyden giriş |

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
| Noah | Musician — ağaçların tınısını keşfeder | S01E24 |
| Arda | Dancer — müziğe dans eder | S01E24 |
| Kiko | Observer — dinler ve keşfeder | Potansiyel |
| Mimi | Listener — kulaklar, sallanır | Potansiyel |

---

## Typical Episode Usage

| Episode | Characters | Story | Duration |
|---------|------------|-------|----------|
| S01E24 | Noah, Arda | Ağaçların tınısını keşfetme, birlikte ritim tutma | 90 sn |

---

## Common Generation Failures

| # | Failure | Prevention |
|---|---------|------------|
| 1 | Ağaçlar normal ağaç gibi görünüyor | Music trees = yuvarlak, renkli, tını veren yapraklar |
| 2 | Müzik enstrümanları gerçekçi | Enstrümanlar doğal: yaprak, taş, rüzgar |
| 3 | Karakterler enstrüman çalıyor | Karakterler dinliyor, sallanıyor, ritim tutuyor |
| 4 | Fazla kalabalık | Maksimum 2-3 karakter, sakin ortam |
| 5 | Sert ses dalgaları visible | Ses dalgaları görünmez, sadece hissedilir |
| 6 | Hill sharp or angular | Hill must be perfectly round and soft |
| 7 | Flowers in rows | Flowers scattered naturally |
| 8 | Path too straight | Path must wind gently |

---

## Video Generation Rules

| Rule | Standard |
|------|----------|
| Camera | 35mm–50mm, child eye-level |
| Movement | Slow pan, gentle push-in, locked-off |
| Lighting | Warm diffused daylight always |
| Characters | 10–12% of frame, never larger |
| Trees | Never move, only leaves sway gently |
| Flowers | Never move |
| Sound | Natural ambience only, no music tracks |
| Yasak | Fast cuts, shaky cam, dramatic movement |

---

## Consistency Checklist

- [ ] Tree positions identical across shots
- [ ] Path winding identical across shots
- [ ] Flower positions identical across shots
- [ ] Stepping stones not moved
- [ | Sky consistent (same cloud pattern)
- [ ] Lighting consistent between shots
- [ ] Characters 10–12% of frame
- [ ] No modern objects
- [ ] No sharp edges
- [ ] No text or watermarks
- [ ] Colour palette matches bible
- [ ] Tree leaf clusters round and musical

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 3.0 | 7 July 2026 | Initial canon bible created |
| 4.0 | 7 July 2026 | Full canon definition, current pipeline format |
