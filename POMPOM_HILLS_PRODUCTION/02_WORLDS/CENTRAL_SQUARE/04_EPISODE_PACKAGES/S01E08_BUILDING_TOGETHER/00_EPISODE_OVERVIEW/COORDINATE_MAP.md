# S01E08 — Coordinate Map

> Not: X/Z konumları henüz staging'de sabitlenmedi (**TBD**). Ölçek, karakter, mekan ve kamera
> yükseklikleri kaynak dosyalardan alınmıştır. Bölüm 8 shot / 120 sn yapısına göre güncellendi.

## Ölçek Sistemi

Kiko = 100 birim (1.00 m)

## Karakter Boyutları

| Karakter | Toplam Boy | Kiko Oranı | Not |
| --- | --- | --- | --- |
| Noah | 100 birim | %100 | Builder |
| Arda | 85 birim | %85 | Noah'tan biraz küçük/genç (karakter canon'u, `01-CHARACTERS/04-arda.md`) |

## Ana Mekan: Central Square (`environment/01-central-square/hero-view.png`)

### Karakter Konumları

| Karakter | Başlangıç | Bitiş | Not |
| --- | --- | --- | --- |
| Noah | TBD | TBD | Big Pompom Tree yakınında, blokları dizer |
| Arda | TBD | TBD | Yuvarlak yoldan gelir, birlikte inşa eder |

### Prop Konumları — Bloklar (tek movable prop, 6 blok)

| Prop | Başlangıç | Bitiş | Durum |
| --- | --- | --- | --- |
| 2 large flat block | TBD | TBD | Taban; big-block-first planında kullanılır |
| 4 medium round/flat block | TBD | TBD | Üst kısım; dizilir → devrilir → yeniden dizilir |

> Tower yüksekliği her zaman ≤ çocukların baş hizası. Blok sayısı tüm bölümde sabit: 6.

## Kamera (shot bazında)

| Shot | Lens | Yükseklik | Açı | Hareket |
| --- | --- | --- | --- | --- |
| 01 | Wide → Medium | 0.85 m | Eye level | Static (settle) |
| 02 | Medium | 0.80 m | Eye level | Static |
| 03 | Medium | 0.80 m | Eye level | Static |
| 04 | Medium | 0.80 m | Eye level | Static (no pull-back) |
| 05 | Medium | 0.80 m | Eye level | Static |
| 06 | Medium | 0.80 m | Eye level | Static |
| 07 | Medium | 0.80 m | Eye level | Static |
| 08 | Medium | 0.80 m | Eye level | Static (no pull-back) |

## Tower State Ledger

| Shot | Başlangıç (stacked / yükseklik) | Bitiş (stacked / yükseklik) |
| --- | --- | --- |
| 03 | 0 / yerde | ~4 / sallanan, göğüs hizası |
| 04 | ~4 | 0 stacked / 6 dağılmış (aynı 6 blok) |
| 06 | 6 dağılmış | 6 dağılmış (1 büyük blok taban olarak yerleşti) |
| 07 | 1 taban | ~5 / yükselen |
| 08 | ~5–6 | tam kule ayakta, ≤ baş hizası |

## Hava Kilidi

| Alan | Değer |
| --- | --- |
| Saat | Sabah (tüm shot'larda sabit; golden/sunset yok) |
| Bulut sayısı | 2 |
| Rüzgar | 0.2 m/sn |
| Gölge opacity | Max %12 |
