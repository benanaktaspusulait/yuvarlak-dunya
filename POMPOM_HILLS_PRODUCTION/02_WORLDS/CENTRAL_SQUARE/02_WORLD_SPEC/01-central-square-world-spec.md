# World Spec — Central Square

## Purpose

Central Square, Pompom Hills'in kalbi ve buluşma noktasıdır. Tüm karakterler burada bir araya gelir. Ana meydan, Big Pompom Tree (#81C784) etrafında doğal bir yaşam alanı sunar. Güvenli, tanıdık ve sıcak bir başlangıç noktasıdır.

## Immutable Identity

- **ID:** ENV-001
- **Name:** Central Square
- **Type:** Living World
- **Status:** Production Ready
- **Key Landmark:** Big Pompom Tree (#81C784)

## Visual Identity

Yuvarlak, geniş, yeşil bir meydan. Merkezde büyük, yuvarlak ponpon ağaç (#81C784). Sıcak, davetkar, tanıdık. Her şey yuvarlak ve yumuşak.

## World Layout

```
Tüm mekanlara bağlantı
        ↓
Central Square (ana meydan)
        ↓
Big Pompom Tree (merkez)
        ↓
Çevre yolları (tüm mekanlara)
```

## Spatial Relationships

- Big Pompom Tree her yerden görünür
- Tüm patikalar buradan başlar
- Açık geniş alan, manzara serbest

## Playable Areas

- Meydan (geniş, yeşil)
- Big Pompom Tree gölgesi
- Yol kavşakları
- Çevre bankları

## Materials

- Çimen: Yeşil, yumuşak (#C8E6C9)
- Taşlar: Yuvarlak, gri (#BDBDBD)
- Ağaç: Büyük, yuvarlak taç (#81C784)
- Banklar: Ahşap, doğal

## Lighting

- Sabah: Sıcak günışığı
- Öğle: Parlak, minimum gölge
- Akşam: Altın ışık
- Gece: Yumuşak ay ışığı

## Colour Palette

- Ana renk: Yeşil #81C784
- İkincil: Sıcak gri #BDBDBD
- Vurgu: Sıcak sarı #FFF9C4
- Zemin: Yeşil #C8E6C9

## Scale

- Alan: ~30 metre çap
- Ağaç Yüksekliği: 4-5 metre
- Bank Yüksekliği: 0.45 metre

## Atmosphere

Sıcak, tanıdık, güvenli. Tüm mekanların buluşma noktası. Her macera buradan başlar veya biter.

## Consistency Rules

- Big Pompom Tree her zaman merkezde
- Tüm yollar kavisli ve yuvarlak
- Sivri köşe yok
- Yeşil palet baskın
- Sıcak ışık her zaman

## Generation Considerations

- Hero View: Big Pompom Tree merkezde
- Tüm mekanlara bağlantı yolları görünür
- Açık geniş alan hissi
- Karakter yok referanslarda

## Visual Richness Layer

> See `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/WORLD_STANDARDS/GLOBAL_ENVIRONMENT_STANDARD.md` § Visual Richness Principle.
> Central Square must never be reduced to "a plaza." The Big Pompom Tree
> (CS-TREE-01) is the mandatory landmark in every wide shot.

**Allowed charm details:** CS-TREE-01 Big Pompom Tree (always centred),
coloured stepping-stone ring (CS-STONE-PNK/YEL/BLU/GRN), soft carpet-like
green ground (CS-GRASS-01), dappled tree-shadow on the grass, low pastel
houses at the edge of the square (background, not redesigned), gentle leaf
rustle.

**Forbidden clutter:** empty plaza with no tree, undersized tree, market
stalls or signage, modern street furniture, sharp-edged geometric paving,
dark or dramatic lighting.

### Art Direction Layer (use with Technical Canon above)

```text
premium preschool animation, handcrafted toy-set feeling, warm communal
atmosphere, storybook village-square beauty, thumbnail-appeal composition,
makes a child want to run in and meet their friends
```

### Hero View Quality Tests

1. **Silhouette Test** — recognisable from the tree + stone-ring shape alone?
2. **Colour Test** — recognisable from the green canopy + pastel palette alone?
3. **Charm Test** — does it feel like a place friends meet and play?

If any test fails, reject.