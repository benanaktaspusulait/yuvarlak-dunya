# Season 01 Scene Continuity TODO v2.1

## Ana Karar

- [ ] Season 01 sahneleri mevcut haliyle fikir ve ton olarak uygun, ancak prodüksiyon devamlılığı için yeterince kilitli değil.
- [ ] 1.5 yaş üstü hedef için her bölümde tek ana fikir, tek ana duygu ve en fazla 2 aktif karakter kullanılmalı.
- [ ] 3-4 yaş hedef korunacaksa bile S01E01'de 13 karakter tanıtımı fazla; ana üçlü Kiko, Mimi, Opa ile sınırlanmalı, yan karakterler sonraki bölümlere yayılmalı.
- [ ] Her sahne, önceki sahnenin tam bittiği fiziksel durumdan başlamalı; karakterler, kamera, hava, prop konumu ve duygu durumu resetlenmemeli.
- [ ] Her sahneye `Start State`, `End State` ve `Continuity Handoff` tablosu eklenmeli.

## Zorunlu Sahne Standardı

Her sahne dosyasında aşağıdaki başlıklar bulunmalı:

| Başlık | Zorunlu İçerik |
| --- | --- |
| Scene ID | Episode, scene no, versiyon, toplam süre |
| Previous Scene End State | Önceki sahnedeki son karakter/prop/kamera/hava durumu |
| Start State | Bu sahnenin ilk karesindeki kesin durum |
| Environment Plate | Kullanılan kesin dosya yolu, örn. `environment/1-central-square.png` |
| Coordinate Map | Kiko=100 birim sisteminde X/Z konumları, kamera yüksekliği, prop uzaklığı |
| Character Positions | Her karakterin başlangıç ve bitiş konumu |
| Prop Positions | Her propun başlangıç ve bitiş konumu; yerde mi, elde mi, arkada mı |
| Weather Lock | Saat, ışık, bulut sayısı, rüzgar yönü/hızı |
| Action Beats | 3-5 basit beat; 1.5+ için beat başına tek aksiyon |
| Dialogue | İngilizce replikler, 2-4 kelime, bağırma yok |
| End State | Son karede herkesin/propun/kameranın kesin durumu |
| Continuity Handoff | Sonraki sahnenin ilk karesi için devredilen bilgiler |
| Existing Assets | Environment, character, prop dosya yolları |
| Missing Assets | Yeni görsel gerekiyorsa prompt, seed, model notu |
| QA | Yaş uygunluğu, tekrar yok, continuity var, asset path doğru |

## Global Asset ve Naming İşleri

- [ ] `Props/` ve `props/` klasörleri çift görünüyor; tek kanonik klasör `Props/` olmalı.
- [ ] Sahne dosyalarındaki `Props/Nature/2-Flowers.png` referansları gerçek dosya adı olan `Props/Nature/2-flowers.png` ile düzeltilmeli.
- [ ] Environment dosya adları slug standardına alınmalı; boşluk, apostrof ve büyük/küçük harf karmaşası kaldırılmalı.
- [ ] Örnek rename listesi: `13-Rosie's Rose Garden.png` -> `13-rosies-rose-garden.png`, `16-friendship-meadow .png` -> `16-friendship-meadow.png`, `18-little-forest .png` -> `18-little-forest.png`.
- [ ] Rename sonrası tüm scene, asset ve prompt dosyalarındaki referanslar güncellenmeli.
- [ ] `characters/drawings/all character.png` dosya adı üretim standardına uygun değil; `all-characters.png` olarak normalize edilmeli.
- [ ] Sahnelerde geçen her asset için var/yok kontrolü yapılmalı; olmayan prop ve background hiçbir sahnede doğrudan kullanılamaz.

## S01E01 - Hello Pompom Hills

### Mevcut Durum

- [ ] 13 ayrı tanıtım sahnesi var; bu 1.5+ hedef için fazla karakter yükü oluşturuyor.
- [ ] Kiko, Mimi ve Opa sahneleri ayrı kartlar gibi başlıyor; fiziksel devamlılık yok.
- [ ] TR ve EN dosyaları paralel ama güncelleme sırasında drift riski var.

### Önerilen Güçlü Revizyon

- [ ] S01E01 ana üçlüye indirilmeli: `01-kiko-intro`, `02-mimi-intro`, `03-opa-intro`, `04-trio-hello`, `05-goodbye-handoff`.
- [ ] Yan karakter intro dosyaları sezon içi ileriki bölümlere taşınmalı veya `archive/side-character-intros/` altında bekletilmeli.
- [ ] Bölüm tek ana mekanda geçmeli: önerilen environment `environment/1-central-square.png`.
- [ ] Kiko'nun evi, Mimi'nin çalısı ve Opa'nın ağacı aynı plate içinde arka plan landmark olarak tarif edilmeli; sahne atlaması yapılmamalı.

### 01-kiko-intro.md Güncelleme

- [ ] Background kesinleştirilmeli: öneri `environment/1-central-square.png`; alternatif `environment/3-kikos-home.png` ancak 02 sahneye yürüyüş handoff gerekir.
- [ ] Yellow ball dosyası kilitlenmeli: `Props/Toys/1-yellow-ball.png`.
- [ ] Start State eklenmeli: Kiko ekran sol arka X=-45/Z=20, sarı top X=25/Z=0, kamera 0.85 m, lens 50mm.
- [ ] End State eklenmeli: Kiko topun yanında X=0/Z=0, top iki elinin arasında veya ayak önünde sabit; sonraki sahneye aynı konum devredilmeli.
- [ ] Hava kilidi eklenmeli: sabah-öğle arası, 2 bulut, rüzgar 0.2 m/sn, gölge opacity max %12.
- [ ] Replikler korunabilir; 1.5+ için `Hello!`, `I'm Kiko.`, `I look!` yeterli.
- [ ] Süre 15 sn uygun; 1.5+ için her shot en az 3 sn görsel tutma içermeli.

### 02-mimi-intro.md Güncelleme

- [ ] Sahne 01'in son karesinden başlamalı; Kiko ve yellow ball kaybolmamalı.
- [ ] Mimi çalısı aynı plate üzerinde konumlanmalı: öneri X=55/Z=12.
- [ ] Start State: Kiko sahne merkezinde top yanında bekler; Mimi kulakları çalının üstünden görünür.
- [ ] End State: Mimi Kiko'nun sağında X=32/Z=0 durur; top X=8/Z=0 yerde kalır.
- [ ] `no extra characters` promptu düzeltilmeli; artık Kiko continuity karakteri olarak sahnede olabilir.
- [ ] Mimi'nin hop hareketi max 6-8 birim kalmalı; hızlı giriş ve sürpriz çıkış yok.

### 03-opa-intro.md Güncelleme

- [ ] Sahne 02'nin son halinden başlamalı; Kiko ve Mimi altta aynı konumda kalmalı.
- [ ] Opa ağacı aynı plate üzerinde arka sağda konumlanmalı: X=62/Z=35.
- [ ] Opa'nın inişi "aniden" olmamalı; 1.5+ için önce gölge/kanat değil, Opa'nın yuvarlak silüeti sakin görünmeli.
- [ ] Opa boyu karakter rehberiyle tutarlı kilitlenmeli: Kiko=100, Mimi=80, Opa=120 ama alçak/yuvarlak hacimli.
- [ ] End State: Üçlü aynı karede, Kiko ortada, Mimi sağda, Opa ağaç dalında; sonraki trio sahnesine direkt geçiş.

### 04-13 Yan Karakter Intro Dosyaları

- [ ] Arda, Noah, Aiko, Amara, Sofia, Luca, Freya, Tillo, Mirnik, Mimo intro sahneleri S01E01 ana akışından çıkarılmalı.
- [ ] Eğer sezon içinde kullanılacaklarsa her biri için character guide, scale table, voice rule ve asset lock kontrol edilmeli.
- [ ] Yan karakter intro sahneleri tek tek bağımsız tanıtım değil, ana üçlüyle basit etkileşim içinde yazılmalı.

## S01E02 - Bounce, Bounce, Kiko!

- [ ] 3 dakikada 6 lokasyon fazla; ana lokasyon 1 veya 2'ye indirilmeli.
- [ ] Önerilen lokasyon akışı: `environment/3-kikos-home.png` -> aynı patikanın devamı olarak `environment/17-butterfly-meadow.png`; diğer lokasyonlar kullanılmamalı.
- [ ] Yellow ball süre boyunca aynı prop olmalı; her sahnede X/Z konumu ve elde/yerde/yuvarlanıyor durumu yazılmalı.
- [ ] Sahne 04'ten 05'e Mimi'nin girişi topun hareketiyle bağlanmalı; Mimi birden yeni mekanda başlamamalı.
- [ ] "Top yuvarlandı ve kayboldu" korku yaratmadan yazılmalı; top her zaman kadrajda veya 1 saniye içinde tekrar görünür olmalı.
- [ ] Opa sadece son sahnede kullanılacaksa, Opa'nın ağacı bölüm boyunca arka planda landmark olarak önce gösterilmeli.
- [ ] Asset düzeltmesi: `Props/Nature/2-Flowers.png` -> `Props/Nature/2-flowers.png`.
- [ ] Missing prompt gerekir: tekil "round safe bounce squash yellow ball contact poses" için render referansı.

## S01E03 - The Little Flower

- [ ] `Seed`, `Watering Can`, `Sprout` yeni prop olarak tanımlanmış ama görsel dosyaları yok; promptları hazırlanmalı.
- [ ] Tillo yalnızca sahne 03'te geliyorsa 1.5+ için yeni karakter yükü yüksek; Tillo ya çıkarılmalı ya da sessiz arka plan bahçıvanı olmalı.
- [ ] Mekan akışı sadeleşmeli: ana lokasyon `environment/7-tillos-garden.png`; ilk tohum bulma da aynı bahçenin kenarında geçmeli.
- [ ] "Every day" ifadesi 3 dakikada zaman sıçraması yaratır; 1.5+ için "wait a little" olarak tek gün içinde anlatılmalı.
- [ ] Tohum, filiz ve çiçek dönüşümü aynı saksı/toprak yaması üzerinde sabit koordinatla yapılmalı.
- [ ] Final flower mevcut `Props/Nature/2-flowers.png` sheetinden değil, tekil hero flower prop olarak üretilmeli.

## S01E04 - Mimi's Big Yawn

- [ ] Bölüm rest/uyku fikri iyi; ancak çok lokasyon denemesi 1.5+ için dağınık.
- [ ] Ana lokasyon `environment/5-mimis-burrow.png` olmalı; rahat yer arama aynı burrow çevresindeki 3 mini noktayla yapılmalı.
- [ ] "Too windy, too bright, too noisy" üç ayrı stres gibi artmamalı; güvenli ve komik küçük farklar olarak yazılmalı.
- [ ] Mimi'nin yorgunluğu hastalık gibi görünmemeli; yüz ifadesi sakin ve güvende kalmalı.
- [ ] Sunny Spot ayrı prop/alan olarak tanımlanmalı: X=20/Z=10, yuvarlak ışık lekesi, gölge opacity max %8.
- [ ] Opa son sahnede fiziksel olarak gelmek yerine uzaktan sakin ses veya ağaç landmarkı olarak düşünülebilir.

## S01E05 - Colours Everywhere

- [ ] Renk öğretimi için iyi bölüm; ancak renkler aynı mekanda keşfedilmeli.
- [ ] Önerilen ana lokasyon: `environment/16-friendship-meadow.png` veya `environment/17-butterfly-meadow.png`.
- [ ] `Rosie's Rose Garden` dosya adı normalize edilmeli ve sadece kırmızı/pembe çiçek gerekiyorsa ayrı prop olarak kullanılmalı.
- [ ] Repeated phrase `What colour is this?` 1.5+ için soru yükü yaratabilir; alternatif `Red flower!`, `Blue sky!`, `Yellow sun!`.
- [ ] Rainbow yapma eylemi fiziksel boya/karmaşa gerektiriyorsa yeni prop gerekir; daha güvenlisi gökyüzünde kısa pastel rainbow arc efekti.
- [ ] Her renk için tek obje, tek kadraj, 3 sn bekleme kuralı eklenmeli.

## S01E06 - The Soft Wind

- [ ] Duyu teması güçlü; hareketler çok hızlı olmamalı.
- [ ] Ana lokasyon `environment/18-little-forest.png` olarak önerilir; mevcut dosya adında trailing space var ve normalize edilmeli.
- [ ] Leaves prop dosyası yok; yeni prop prompt gerekir.
- [ ] Rüzgar yönü bölüm boyunca sabit olmalı: screen left -> right, hız 0.4-0.8 m/sn.
- [ ] Mimi'nin kulak flap hareketi eğlenceli ama kontrolsüz savrulma gibi görünmemeli; kulak açısı max 18 derece.
- [ ] Bulut drift, çiçek sway, yaprak hareketi aynı rüzgar vektörüne bağlı olmalı.
- [ ] "Blow, blow, blow!" çok nefes verme taklidi yaratıyorsa `Soft wind!` veya `Feel the wind!` ile pedagojik olarak yumuşatılmalı.

## Yeni Görsel / Prop Promptları

### Seed Prop

```text
single tiny round brown seed prop for a preschool 3D toy world, diameter 6 units in Kiko=100 scale, matte warm brown #A1887F, rounded bean shape, no sharp tip, clean transparent background, centered orthographic front view, {style}, {camera}, {lighting}, 1:1
```

### Watering Can Prop

```text
round blue watering can prop for a preschool 3D toy world, height 32 units in Kiko=100 scale, bulbous body, short rounded spout, thick rounded handle, pastel blue #90CAF9, white soft highlight, matte material roughness 0.78, no metal realism, transparent background, centered orthographic front view, {style}, {camera}, {lighting}, 1:1
```

### Sprout Prop

```text
small safe round sprout prop for a preschool 3D toy world, height 18 units in Kiko=100 scale, two rounded leaves, tiny mound of soft soil, pastel green #81C784, warm brown soil #A1887F, no realistic dirt texture, transparent background, centered orthographic front view, {style}, {camera}, {lighting}, 1:1
```

### Hero Flower Prop

```text
single hero round flower prop for a preschool 3D toy world, height 42 units in Kiko=100 scale, circular yellow center #FFD54F, six rounded pink petals #F48FB1, thick safe green stem #81C784, matte toy material, no thin sharp petals, transparent background, centered orthographic front view, {style}, {camera}, {lighting}, 1:1
```

### Round Bush Prop

```text
round fluffy bush prop for Pompom Hills preschool 3D world, width 85 units and height 55 units in Kiko=100 scale, clustered spherical leaves, pastel green #81C784 and #C8E6C9, no sharp branches, no realistic leaf texture, transparent background, centered orthographic front view, {style}, {camera}, {lighting}, 1:1
```

### Soft Wind Leaves Prop

```text
set of five rounded pastel leaves for a preschool 3D toy world, each leaf 10-14 units long in Kiko=100 scale, rounded oval shapes, mint green #C8E6C9, warm yellow green #DCE775, no pointed tips, arranged for gentle wind motion reference, transparent background, centered orthographic view, {style}, {camera}, {lighting}, 1:1
```

### Central Intro Stage Background

```text
Pompom Hills central intro stage environment for preschool 3D animation, wide 16:9 background, round central square with curved stepping stone path, Kiko's coral round house visible far left, Mimi's round green bush mid right, Opa's big pompom tree far right, pastel hills in background, warm morning daylight, 2 round white clouds, no text, no signs, no sharp edges, stable object positions for scene continuity, {style}, {camera}, {lighting}, 16:9
```

## Öncelik Sırası

1. [ ] `Props/` / `props/` klasör kararı ve dosya adı normalizasyonu.
2. [ ] Tüm scene asset path hatalarının düzeltilmesi.
3. [ ] S01E01'in 13 introdan ana üçlü continuity bölümüne sadeleştirilmesi.
4. [ ] Her sahneye Start State / End State / Continuity Handoff eklenmesi.
5. [ ] S01E02-S01E06 lokasyon sayılarının azaltılması.
6. [ ] Eksik prop promptlarının görsele dönüştürülmesi.
7. [ ] Her bölüm için tek coordinate map dosyası oluşturulması.
8. [ ] TR ve EN sahne dosyaları için tek kaynak veya senkron kontrol kararı.
9. [ ] Yaş uygunluğu QA: 1.5+ için tek aksiyon, tek duygu, kısa replik, yavaş tempo.
10. [ ] Final continuity pass: her sahnenin ilk karesi önceki sahnenin son karesiyle eşleşiyor mu?
