# Asset Registry — Pompom Hills

> Central registry for all reusable environmental assets.
> Every asset used in a World Bible or shot file must be registered here.
> Source of truth for Asset IDs across all worlds and all episodes.

---

## How to Use

- **World Bibles** define assets in their Canonical Reusable Assets section using IDs from this registry.
- **World Specs** reference these IDs in the Colour Palette and Reusable Assets tables.
- **Shot files** reference IDs directly: `Use: CH-STONE-01, CH-CLOUD-A` instead of re-describing the asset.
- When a new asset is created, register it here before using it in any document.

---

## ID Format

```
[WORLD-PREFIX]-[TYPE]-[INDEX]

World prefix : 2–3 uppercase letters from world name
Type         : GRASS / CLOUD / STONE / TREE / FLOWER / FENCE / DOOR /
               BED / RUG / SHELF / AMB / BIRD / PATH / HILL / OTHER
Index        : 01, 02, A, B — for variants of the same type
```

---

## ENV-002 — Cloud Hill (CH)

| Asset ID | Description | Hex / Notes | Used In |
|----------|-------------|-------------|---------|
| CH-HILL-DOME | Full-width smooth grass dome silhouette | — | All wide shots |
| CH-SUMMIT | Flat grassy plateau at top, ~3–4 m diameter | — | All summit scenes |
| CH-STONE-01 | Flat round grey sitting stone, 40 cm × 15 cm, summit right-of-centre | #ECEFF1 | Dialogue, rest scenes |
| CH-DAISY-01 | Sparse white daisy clusters, 3–5 per group | petals #FFFFFF, centre #FFF59D | Hillside + summit |
| CH-CLOUD-A | Large rounded cumulus, left of sky centre | #F5F5F5 | Hero View, establishing shots |
| CH-CLOUD-B | Medium cumulus, upper right near sun | #F5F5F5 | Hero View, establishing shots |
| CH-GRASS-01 | Short even plush grass, matte surface | #A5D6A7 | All exterior frames |
| CH-HILL-BG | Low pastel hill silhouettes on horizon | #C8E6C9 | All wide shots |
| CH-WIND-AMB | Soft continuous wind audio, low breathy tone | — | All scenes |
| CH-BIRD-01 | Single distant melodic bird call | — | All scenes |

---

## ENV-003 — Kiko's Home (KH)

| Asset ID | Description | Hex / Notes | Used In |
|----------|-------------|-------------|---------|
| KH-HOUSE-EXT | Full exterior — round coral pink cottage, dome roof, white arched door | walls #F8BBD0, roof #E91E63 | All exterior shots |
| KH-DOOR-01 | White round arched front door, 1.35 m tall, opens outward | #FFFFFF | Entry/exit scenes |
| KH-WINDOW-01 | Round window with coral pink curtain, slightly open | frame #FFFFFF, curtain #F8BBD0 | Exterior + interior shots |
| KH-FENCE-01 | Low coral pink rounded fence, 0.50 m tall | #F8BBD0 | All exterior shots |
| KH-FLOWER-RED | Large round red garden flower | #EF5350 | Front garden |
| KH-FLOWER-YEL | Large round yellow garden flower | #FFD54F | Front garden |
| KH-FLOWER-PNK | Large round pink garden flower | #F48FB1 | Front garden |
| KH-PATH-01 | Round stepping stone path to front door | #E0E0E0 | Exterior shots |
| KH-BED-01 | Round coral pink bed with round pillow | #F8BBD0 | Sleeping corner |
| KH-TABLE-01 | Round white table, 4 rounded legs | #FFFFFF | Living room / kitchen nook |
| KH-CHAIR-01 | Round white chair | #FFFFFF | Living room (×2) |
| KH-RUG-01 | Round white rug with coral pink polka dots | #FFFFFF + #F8BBD0 | Living room floor |
| KH-TOYBOX-01 | Round yellow toy box | #FFD54F | Living room right corner |
| KH-SHELF-01 | Round white shelf with books and toys | #FFFFFF | Reading corner |
| KH-GRASS-01 | Soft green garden grass | #C8E6C9 | Front + back garden |

---

## ENV-001 — Central Square (CS)

| Asset ID | Description | Hex / Notes | Used In |
|----------|-------------|-------------|---------|
| CS-TREE-01 | Big Pompom Tree — round fluffy green canopy, thick trunk | canopy #81C784, trunk #A1887F | All Central Square shots |
| CS-STONE-PNK | Round pink stepping stone | #F8BBD0 | Stone circle around tree |
| CS-STONE-YEL | Round yellow stepping stone | #FFD54F | Stone circle around tree |
| CS-STONE-BLU | Round blue stepping stone | #90CAF9 | Stone circle around tree |
| CS-STONE-GRN | Round green stepping stone | #A5D6A7 | Stone circle around tree |
| CS-GRASS-01 | Soft carpet-like green ground | #C8E6C9 | All Central Square shots |

---

## How to Add a New Asset

1. Choose the world prefix (or create one if the world doesn't have a prefix yet).
2. Choose the type tag from the standard list above.
3. Assign the next available index for that type in that world.
4. Add the row to this registry.
5. Add the same asset to the world's Bible (Canonical Reusable Assets section) and World Spec.

---

## World Prefix Index

| Prefix | World | ENV ID |
|--------|-------|--------|
| CH | Cloud Hill | ENV-002 |
| KH | Kiko's Home | ENV-003 |
| CS | Central Square | ENV-001 |
| SH | Sun Hill | ENV-004 |
| MB | Mimi's Burrow | ENV-005 |
| OT | Opa's Tree | ENV-006 |
| TG | Tillo's Garden | ENV-007 |
| LG | Lulu's Greenhouse | ENV-008 |
| PB | Poppy's Bakery | ENV-009 |
| BP | Benny's Playground | ENV-010 |
| TT | Tillo's Treehouse | ENV-011 |
| MP | Milo's Pond | ENV-012 |
| RG | Rosie's Rose Garden | ENV-013 |
| LL | Lily's Lavender Farm | ENV-014 |
| RB | Rainbow Bridge | ENV-015 |
| FM | Friendship Meadow | ENV-016 |
| BM | Butterfly Meadow | ENV-017 |
| LF | Little Forest | ENV-018 |
| RC | Rainbow Creek | ENV-019 |
| WP | Wish Pond | ENV-020 |
| CG | Camping Grove | ENV-021 |
| SC | Story Circle | ENV-022 |
| AC | Art Corner | ENV-023 |
| AT | Adventure Trail | ENV-024 |
| FH | Flower Hill | ENV-025 |
| TH | Tree Hill | ENV-026 |
| ST | Stone Hill | ENV-027 |
| PC | Paddle Cove | ENV-028 |
| PM | Pony Meadow | ENV-029 |
| HT | Hobby Horse Trail | ENV-030 |

---

*Bu belge tüm çevre assetleri için merkezi kayıttır.*
*Versiyon: 1.0*
*Son güncelleme: 3 Temmuz 2026*
