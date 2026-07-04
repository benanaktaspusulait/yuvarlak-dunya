# World Spec — Opa's Tree

## Purpose

Opa's Tree, çocukların Opa'nın hikayelerini dinlediği, bilgelik ve huzur mekanıdır. Büyük, eski bir ağaç etrafında doğal bir yaşam alanı sunar. Sessiz, saygılı ve bilge bir atmosfer.

## Immutable Identity

- **ID:** ENV-006
- **Name:** Opa's Tree
- **Type:** Living World
- **Status:** Production Ready
- **Key Landmark:** Dev eski ağaç (#5D4037 gövde, #66BB6A taç)

## Visual Identity

Büyük, yuvarlak, eski bir ağaç. Kalın gövde, geniş taç. Sessiz, bilge, saygılı. Yosunlu zemin, yumuşak gölge.

## World Layout

```
Ana yol
        ↓
Opa's Tree (giriş)
        ↓
Gövde etrafı (oturma alanı)
        ↓
Taç altında (dinlenme)
```

## Spatial Relationships

- Ağaç her yerden görünür
- Gövde etrafında doğal çember
- Taç altında geniş gölge
- Sessiz, izole atmosfer

## Playable Areas

- Gövde etrafı (oturma)
- Taç altında (gölge)
- Yosun bahçesi
- Gözlem noktası

## Materials

- Gövde: Koyu kahverengi, doğal (#5D4037)
- Taç: Koyu yeşil, yuvarlak (#66BB6A)
- Yosun: Yeşil, yumuşak (#81C784)
- Taşlar: Yuvarlak, gri

## Lighting

- Sabah: Yapraklar arasından süzülen
- Öğle: Gölge, maximum
- Akşam: Altın ışık
- Gece: Ay ışığı + ateş

## Colour Palette

- Ana renk: Koyu yeşil #66BB6A
- Gövde: Koyu kahverengi #5D4037
- Yosun: Yeşil #81C784
- Taşlar: Sıcak gri #BDBDBD

## Scale

- Ağaç Yüksekliği: 5-6 metre
- Gövde Çapı: 1.5 metre
- Alan: ~15 metre çap

## Atmosphere

Bilge, sessiz, saygılı. Zamanın durduğu bir mekan. Hikaye anlatma ve dinleme alanı.

## Consistency Rules

- Ağaç her zaman eski ve büyük
- Gövde her zaman kalın ve yuvarlak
- Taç her zaman geniş ve yuvarlak
- Yosun her zaman yumuşak
- Sessiz atmosfer korunur

## Generation Considerations

- Hero View: Dev ağaç merkezde, taç yukarıda
- Gövde detayı close-up
- Yosun zemin view
- Işık yapraklar arasından süzülmeli

## Visual Richness Layer

> See `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/WORLD_STANDARDS/GLOBAL_ENVIRONMENT_STANDARD.md` § Visual Richness Principle.
> Opa's Tree must never be reduced to "a big tree." OT-BRANCH-01 (Opa's
> storytelling branch) is the mandatory landmark in every shot where Opa
> is present.

**Allowed charm details:** OT-BRANCH-01 wide storytelling branch (landmark),
OT-TRUNK-01 thick textured trunk, dappled sunlight patterns through the
canopy, soft moss texture at the base, OT-FLOWERS-01 small Pompom flowers
(pink/yellow/purple), gentle leaf rustle, occasional single drifting leaf.

**Forbidden clutter:** generic tree with no storytelling branch, tree that
reads as small/unremarkable, sharp or thin branches, modern
structures/ladders/platforms, dark or cold-lit canopy, crowded unrelated
background props.

### Art Direction Layer (use with Technical Canon above)

```text
premium preschool animation, handcrafted toy-set feeling, warm sheltering
atmosphere, storybook wisdom-and-safety beauty, thumbnail-appeal
composition, makes a child want to sit and listen to a story
```

### Hero View Quality Tests

1. **Silhouette Test** — recognisable from the tree canopy + storytelling branch shape alone?
2. **Colour Test** — recognisable from the warm green/brown/gold palette alone?
3. **Charm Test** — does it feel safe, wise, and inviting for a story?

If any test fails, reject.