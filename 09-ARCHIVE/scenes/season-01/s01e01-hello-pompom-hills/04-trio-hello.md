# Scene 04 - Trio Hello v3.0

## Scene ID

| Alan | Değer |
| --- | --- |
| Episode | S01E01 - Hello Pompom Hills |
| Scene | 04 |
| Version | 3.0 |
| Süre | 15 sn |

## Production Lock

| Alan | Değer |
| --- | --- |
| Karakter | Kiko, Mimi, Opa (üçlü) |
| Mekan | Central Square — Pompom Hills meydanı |
| Ana duygu | Birlikte olma, neşe |
| Pedagojik hedef | Çocuk izleyici üç ana karakterin birlikte eğlendiğini görür |
| Ölçek | Kiko=100, Mimi=80, Opa=120 (alçak/yuvarlak) |
| Günün saati | Sabah-öğle arası |
| Hava durumu | Açık gökyüzü, güneşli, yumuşak bulutlar |

## Previous Scene End State

| Alan | Değer |
| --- | --- |
| Kiko konumu | X=0 / Z=0, merkezde |
| Mimi konumu | X=32 / Z=0, Kiko'nun sağında |
| Opa konumu | X=62 / Z=35, ağaç dalında |
| Yellow ball konumu | X=8 / Z=0, yerde |

## Start State

| Alan | Değer |
| --- | --- |
| Kiko konumu | X=0 / Z=0, merkezde |
| Mimi konumu | X=32 / Z=0, Kiko'nun sağında |
| Opa konumu | X=62 / Z=35, ağaç dalında |
| Yellow ball konumu | X=8 / Z=0, yerde |
| Kamera yüksekliği | 0.85 m |
| Lens | 50mm |
| Hava | Sabah-öğle arası, 2 bulut, rüzgar 0.2 m/sn |
| Gölge opacity | Max %12 |

## Environment Plate

| Alan | Değer |
| --- | --- |
| Dosya yolu | `environment/1-central-square.png` |
| Arka plan | Üç karakter aynı karede; Opa yukarıda ağaçta |

## Coordinate Map (Kiko=100 birim)

| Element | X | Z | Not |
| --- | --- | --- | --- |
| Kiko | 0 | 0 | Merkez, ortada |
| Mimi | 32 | 0 | Sağda |
| Opa | 62 | 35 | Ağaç dalında, yukarıda |
| Yellow ball | 8 | 0 | Yerde |
| Trio aralığı | 18-24 birim | — | Karakterler arası boşluk |
| Kamera yüksekliği | — | — | 0.85 m |

## Character Positions

| Karakter | Başlangıç | Bitiş |
| --- | --- | --- |
| Kiko | X=0 / Z=0 | X=0 / Z=0 |
| Mimi | X=32 / Z=0 | X=32 / Z=0 |
| Opa | X=62 / Z=35 (ağaçta) | X=62 / Z=35 (ağaçta) |

## Prop Positions

| Prop | Başlangıç | Bitiş | Durum |
| --- | --- | --- | --- |
| Yellow ball | X=8 / Z=0 | X=8 / Z=0 | Yerde sabit |

## Weather Lock

| Alan | Değer |
| --- | --- |
| Saat | Sabah-öğle arası |
| Işık | Warm soft daylight |
| Bulut sayısı | 2 |
| Rüzgar yönü/hızı | Screen left → right, 0.2 m/sn |
| Gölge opacity | Max %12 |

## Sahne Atmosferi

| Alan | Değer |
| --- | --- |
| Gökyüzü | Açık açık mavi #BBDEFB, 2 yuvarlak beyaz bulut #FFFFFF |
| Güneş | Büyük yuvarlak sıcak sarı #FFF9C4 |
| Ağaç | Büyük ponpon ağaç, Opa dalında |
| Çimen | Yumuşak yeşil #C8E6C9 |
| Genel his | Birlikte olma, neşe, güvenli |

## Beat Sheet

| Beat | Süre | Aksiyon |
| --- | ---: | --- |
| 1 | 0-4 sn | Üçlü aynı karede. Kiko ortada, Mimi sağda, Opa yukarıda ağaçta. Sakin bir an. |
| 2 | 4-8 sn | Kiko el sallar. Mimi hop hop eder. Opa kanat selamı verir. |
| 3 | 8-12 sn | Hepsi birlikte gülümser. Kiko topa bakar. |
| 4 | 12-15 sn | Kiko "Together!" der. Mimi ve Opa onaylar. |

## Shot Plan

| Shot | Süre | Lens | Kamera Yüksekliği | Aksiyon | Ses |
| --- | ---: | --- | --- | --- | --- |
| 01 | 4 sn | 50mm wide | 0.85 m | Üçlü aynı karede, sakin an | Kuş cıvıltısı |
| 02 | 4 sn | 50mm medium | 0.85 m | Kiko el sallar, Mimi hop, Opa selam | Kiko: "Hello!" |
| 03 | 4 sn | 50mm medium | 0.85 m | Hepsi gülümser | Kiko: "We're friends!" |
| 04 | 3 sn | 50mm wide, sabit | 0.85 m | Birlikte poz | Kiko: "Together!" |

## Dialogue

```text
Kiko: Hello!
Kiko: We're friends!
Kiko: Together!
```

**Voice tone guide:** Warm, joyful, inclusive. All three characters speak with safety and warmth.

## Visual Prompt

```text
Kiko, Mimi and Opa together in Central Square of Pompom Hills, Kiko is 100 units tall center waving, Mimi is 80 units tall right hopping gently, Opa is 120 units total height perched on pompom tree branch far right wise smile, warm brown pigtails #8D6E63 coral pink shirt #F8BBD0, soft blue rabbit #90CAF9 yellow t-shirt #FFF59D floppy ears, wise owl #A5D6A7 golden glasses #FFD54F brown shawl #A1887F, round yellow ball on ground, morning warm soft daylight, light blue sky #BBDEFB round white clouds, warm yellow sun, soft green grass #C8E6C9, {style}, {camera}, {lighting}, 16:9
```

## Animation Notes

| Alan | Değer |
| --- | --- |
| Kiko wave | 2 küçük el hareketi, 18 frame |
| Mimi hop | Max 8 birim, kulak flop |
| Opa salute | Sağ kanat 12 frame kalkar |
| Trio rhythm | Hareketler aynı anda değil, 2-4 frame gecikmeyle |
| Squash-stretch | Kiko max %4, Mimi max %6, Opa max %3 |

## End State

| Alan | Değer |
| --- | --- |
| Kiko konumu | X=0 / Z=0 |
| Mimi konumu | X=32 / Z=0 |
| Opa konumu | X=62 / Z=35 (ağaçta) |
| Yellow ball konumu | X=8 / Z=0 |
| Kamera | 0.85 m, 50mm |
| Duygu | Üçlü birlikte, mutlu |

## Continuity Handoff

| Alan | Değer |
| --- | --- |
| Sonraki sahne | 05-arda-intro |
| Devredilen durum | Üçlü aynı pozisyonda, birlikte mutlu |
| Kamera | 0.85 m, 50mm |
| Hava | Aynı |

## Existing Assets

| Asset | Dosya yolu |
| --- | --- |
| Environment | `environment/1-central-square.png` |
| Kiko | `characters/drawings/kiko.png` |
| Mimi | `characters/drawings/mimi.png` |
| Opa | `characters/drawings/opa.png` |
| Yellow ball | `Props/Toys/1-yellow-ball.png` |

## Missing Assets

| Asset | Durum |
| --- | --- |
| Yok | Tüm assetler mevcut |

## Safety Check

- Üç karakter de sakin ve kontrollü.
- Opa ağaçtan inmez; yukarıda kalır.
- Hareketler yavaş ve yumuşak.
- Çatışma yok.

## Negative Prompt

Use `NEGATIVE_PROMPTS.md` common negative prompt.
