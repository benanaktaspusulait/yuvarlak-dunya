# Scene 15 - Goodbye Handoff v3.0

## Scene ID

| Alan | Değer |
| --- | --- |
| Episode | S01E01 - Hello Pompom Hills |
| Scene | 15 |
| Version | 3.0 |
| Süre | 15 sn |

## Production Lock

| Alan | Değer |
| --- | --- |
| Karakter | Kiko, Mimi, Opa (üçlü) |
| Mekan | Central Square — Pompom Hills meydanı |
| Ana duygu | Güle güle, güvenli vedalaşma |
| Pedagojik hedef | Çocuk izleyici vedalaşmayı ve "bir dahaki sefere" beklentisini öğrenir |
| Ölçek | Kiko=100, Mimi=80, Opa=120 |
| Günün saati | Sabah-öğle arası |
| Hava durumu | Açık gökyüzü, güneşli |

## Previous Scene End State

| Alan | Değer |
| --- | --- |
| Kiko konumu | X=0 / Z=0 |
| Mimi konumu | X=32 / Z=0 |
| Opa konumu | X=62 / Z=35 (ağaçta) |
| Yellow ball konumu | X=8 / Z=0 |

## Start State

| Alan | Değer |
| --- | --- |
| Kiko konumu | X=0 / Z=0, merkezde |
| Mimi konumu | X=32 / Z=0, Kiko'nun sağında |
| Opa konumu | X=62 / Z=35, ağaç dalında |
| Yellow ball konumu | X=8 / Z=0, yerde |
| Kamera yüksekliği | 0.85 m |
| Lens | 50mm |

## Environment Plate

| Alan | Değer |
| --- | --- |
| Dosya yolu | `environment/01-central-square/hero-view.png` |

## Coordinate Map (Kiko=100 birim)

| Element | X | Z | Not |
| --- | --- | --- | --- |
| Kiko | 0 | 0 | Merkez |
| Mimi | 32 | 0 | Sağda |
| Opa | 62 | 35 | Ağaçta |
| Yellow ball | 8 | 0 | Yerde |

## Character Positions

| Karakter | Başlangıç | Bitiş |
| --- | --- | --- |
| Kiko | X=0 / Z=0 | X=0 / Z=0 |
| Mimi | X=32 / Z=0 | X=32 / Z=0 |
| Opa | X=62 / Z=35 | X=62 / Z=35 |

## Prop Positions

| Prop | Başlangıç | Bitiş | Durum |
| --- | --- | --- | --- |
| Yellow ball | X=8 / Z=0 | X=8 / Z=0 | Yerde sabit |

## Weather Lock

| Alan | Değer |
| --- | --- |
| Saat | Sabah-öğle arası |
| Bulut sayısı | 2 |
| Rüzgar | 0.2 m/sn |

## Beat Sheet

| Beat | Süre | Aksiyon |
| --- | ---: | --- |
| 1 | 0-4 sn | Üçlü sakin durur. Kiko kameraya bakar. |
| 2 | 4-8 sn | Kiko el sallar: "Bye bye!" Mimi de el/pat sallar. Opa kanat selamı verir. |
| 3 | 8-12 sn | Kiko: "See you soon!" Gülümseme. |
| 4 | 12-15 sn | Kamera yavaşça geri çekilir. Üçlü aynı karede kalır. Yavaş fade. |

## Shot Plan

| Shot | Süre | Lens | Kamera Yüksekliği | Aksiyon | Ses |
| --- | ---: | --- | --- | --- | --- |
| 01 | 4 sn | 50mm medium | 0.85 m | Üçlü sakin, Kiko kameraya bakar | Kuş cıvıltısı |
| 02 | 4 sn | 50mm medium | 0.85 m | El sallama | Kiko: "Bye bye!" |
| 03 | 4 sn | 50mm medium | 0.85 m | Gülümseme | Kiko: "See you soon!" |
| 04 | 3 sn | 50mm wide | 0.85 m | Kamera geri çekilir, fade | Sessizlik + kuş |

## Dialogue

```text
Kiko: Bye bye!
Kiko: See you soon!
```

**Voice tone guide:** Warm, gentle farewell. Not sad, just a happy "see you next time."

## Visual Prompt

```text
Kiko, Mimi and Opa saying goodbye in Central Square of Pompom Hills, Kiko is 100 units tall center waving at viewer, Mimi is 80 units tall right waving, Opa is 120 units total perched on pompom tree branch far right with wing salute, warm friendly smiles, round yellow ball on ground, morning warm soft daylight, light blue sky #BBDEFB round white clouds, warm yellow sun, soft green grass #C8E6C9, {style}, {camera}, {lighting}, 16:9
```

## Animation Notes

| Alan | Değer |
| --- | --- |
| Kiko wave | Yavaş, 2 el hareketi, her biri 24 frame |
| Mimi wave | Pat sallama, 18 frame |
| Opa salute | Kanat selamı, 20 frame |
| Camera pull | Yavaşça genişler, 3 sn |
| Fade | Son 1 sn'de yavaşça kararma |

## End State

| Alan | Değer |
| --- | --- |
| Kiko konumu | X=0 / Z=0 |
| Mimi konumu | X=32 / Z=0 |
| Opa konumu | X=62 / Z=35 |
| Yellow ball konumu | X=8 / Z=0 |
| Kamera | 0.85 m, geniş |
| Duygu | Mutlu veda |

## Continuity Handoff

| Alan | Değer |
| --- | --- |
| Sonraki sahne | S01E02 (yeni bölüm) |
| Not | Bu bölüm sonu; sonraki bölüm farklı mekan ile başlayabilir |

## Existing Assets

| Asset | Dosya yolu |
| --- | --- |
| Environment | `environment/01-central-square/hero-view.png` |
| Kiko | `01-CHARACTERS/drawings/kiko.png` |
| Mimi | `01-CHARACTERS/drawings/mimi.png` |
| Opa | `01-CHARACTERS/drawings/opa.png` |
| Yellow ball | `03-PROPS/Toys/1-yellow-ball.png` |

## Missing Assets

| Asset | Durum |
| --- | --- |
| Yok | Tüm assetler mevcut |

## Safety Check

- Sakin veda; ağlama, üzülme yok.
- Hareketler yavaş.
- Kamera yavaşça geri çekilir.
- Sert kesme yok; yavaş fade.

## Negative Prompt

Use `NEGATIVE_PROMPTS.md` common negative prompt.
- No subtitles burned into video. No text on screen. No captions.
