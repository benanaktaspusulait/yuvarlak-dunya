# S01E06 — Coordinate Map

## Ölçek Sistemi

Kiko = 100 birim (1.00 m)

## Karakter Boyutları

| Karakter | Toplam Boy | Kiko Oranı |
| --- | --- | --- |
| Kiko | 100 birim | %100 |
| Mimi | 80 birim | %80 |
| Opa | 120 birim | %120 |

## Ana Mekan: Little Forest (`environment/18-little-forest.png`)

### Sabit Elementler

| Element | X | Z | Not |
| --- | --- | --- | --- |
| Ağaçlar | -30, -10, 15, 35 | 20-40 | Yuvarlak ponpon ağaçlar |
| Yaprak yaması | 0 | 10 | Yaprakların düştüğü alan |
| Çiçekler | -20, 20 | 5 | Sallanan çiçekler |
| Mimi'nin kulak alanı | 10 | 0 | Kulak flap hareketi |

### Karakter Konumları

| Karakter | Başlangıç | Bitiş | Not |
| --- | --- | --- | --- |
| Kiko | -10 | 0 | Merkeze doğru |
| Mimi | 15 | 5 | Sağdan |
| Opa | 35 | 30 | Ağaçta (son sahne) |

### Rüzgar Vektörü

| Alan | Değer |
| --- | --- |
| Yön | Screen left → right |
| Hız | 0.4-0.8 m/sn |
| Bulut drift | Aynı vektör |
| Çiçek sway | Aynı vektör |
| Yaprak hareketi | Aynı vektör |
| Mimi kulak flap | Max 18 derece |

## Hava Kilidi

| Alan | Değer |
| --- | --- |
| Saat | Öğle sonrası |
| Bulut sayısı | 3 |
| Rüzgar | Screen left → right, 0.4-0.8 m/sn |
| Gölge opacity | Max %10 |
