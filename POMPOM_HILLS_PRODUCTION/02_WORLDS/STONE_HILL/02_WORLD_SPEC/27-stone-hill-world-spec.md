# World Spec — Stone Hill

## Purpose

Stone Hill, çocukların yuvarlak pastel taşlarla oynadığı, tırmanma ve keşif mekanıdır. Alçak, güvenli bir tepe etrafında doğal bir yaşam alanı sunar. Cesaret, macera ve doğal bağlantı duygusu taşır.

## Immutable Identity

- **ID:** ENV-027
- **Name:** Stone Hill
- **Type:** Living World
- **Status:** Production Ready
- **Key Landmark:** Yuvarlak pastel taşlar (#BDBDBD, #F48FB1, #CE93D8)

## Visual Identity

Alçak, yuvarlak bir tepe. Pastel renkli taşlar, yumuşak çimen. Güvenli tırmanma, doğal keşif. Her şey yuvarlak ve yumuşak.

## World Layout

```
Ana yol
        ↓
Stone Hill girişi
        ↓
Taş alanları (alt orta)
        ↓
Zirve (manzara)
        ↓
Dinlenme noktası
```

## Spatial Relationships

- Tepeden tüm çevre görünür
- Taşlar doğal dağılım
- Yollar kavisli ve yuvarlak
- Açık geniş manzara

## Playable Areas

- Taş alanları (keşif)
- Tırmanma yolu (alt)
- Zirve (manzara)
- Dinlenme noktası

## Materials

- Taşlar: Yuvarlak, pastel (#BDBDBD, #F48FB1, #CE93D8)
- Çimen: Yeşil, yumuşak (#C8E6C9)
- Yol: Yuvarlak taşlar
- Zemin: Yumuşak, doğal

## Lighting

- Sabah: Sıcak günışığı
- Öğle: Parlak, açık
- Akşam: Altın ışık
- Gece: Yumuşak ay ışığı

## Colour Palette

- Ana renk: Pastel taşlar
- Taş 1: Sıcak gri #BDBDBD
- Taş 2: Pembe #F48FB1
- Taş 3: Mor #CE93D8
- Zemin: Yeşil #C8E6C9

## Scale

- Tepe Yüksekliği: 1.5 metre
- Alan: ~18 metre çap
- Taş Boyutu: 0.2-0.5 metre

## Atmosphere

Cesur, maceracı, güvenli. Doğal keşif ve tırmanma deneyimi. Pastel renkler sakinlik katar.

## Consistency Rules

- Taşlar her zaman yuvarlak ve pastel
- Tırmanma her zaman güvenli
- Sivri köşe yok
- Çimen yumuşak
- Manzara her zaman görünür

## Generation Considerations

- Hero View: Yuvarlak tepe, pastel taşlar
- Close-up: Taş dokusu, renk detayı
- Zirve view: Manzara panoraması
- Tırmanma açısı: Düşük, güvenli

## Visual Richness Layer

> See `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/WORLD_STANDARDS/GLOBAL_ENVIRONMENT_STANDARD.md` § Visual Richness Principle.
> Stone Hill must never be reduced to "a hill with rocks."

This layer protects Stone Hill from becoming too plain. Keep the world
readable and the rounded silhouette clear — add only the canon-approved
charm details below. Do not add random objects. Do not remove the
brave-but-safe, natural-discovery emotional identity.

**Allowed charm details (use, do not omit):**
- SH-STONES-01, clusters of round pastel stones (warm grey #BDBDBD, pink #F48FB1, purple #CE93D8) scattered across the slope — primary landmark
- SH-CAVE-01, the small round friendly cave tucked into the hillside
- soft green grass (#C8E6C9) growing between the stones
- gently curved climbing paths winding between stone clusters
- varied stone sizes (0.2–0.5 m) grouped naturally, never uniform
- small trickling şelale (waterfall) near the cave with soft continuous water sound

**Forbidden clutter:** sharp-edged or jagged stones, a dark or maze-like cave, a generic grey rock pile with no colour identity, muddy or murky water, modern objects or climbing gear, harsh dramatic lighting inside the cave, realistic/photoreal rock texture.

### Art Direction Layer (use together with Technical Canon above)

```text
premium preschool animation, handcrafted toy-set feeling, sunlit pastel
stone hillside atmosphere, storybook beauty, thumbnail-appeal composition,
makes a child want to hop across the stones and peek into the little cave
```

### Hero View Quality Tests

1. **Silhouette Test** — is the low rounded hill with its scattered stone clusters recognisable as Stone Hill from shape alone?
2. **Colour Test** — is the world recognisable from the warm grey/pink/purple pastel stone palette alone?
3. **Charm Test** — does the image make a child want to climb the stones and look inside the cave?

If any test fails, reject — see Generation Failures table above and
`27-stone-hill-bible.md` § Forbidden Over-Simplification.

---

*Stone Hill — World Specification, aligned with Bible v3.1.*
*Visual Richness Layer added 4 Temmuz 2026.*