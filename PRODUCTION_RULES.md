# Pompom Hills - Production Rules v1.0

## Kural 1: Kamera Sürekliliği

Her sahne bir önceki sahnenin bittiği kamera açısından devam etmelidir.

### Nasıl uygulanır:

| Sahne Sonu | Bir Sonraki Sahne Başlangıcı |
|---|---|
| Wide shot, sol taraf | Wide shot, sol taraftan devam |
| Close-up, merkez | Medium shot, merkezden genişleme |
| Push-in, sağa doğru | Pull-out, sağdan başlama |

### Örnek:

Sahne 01 biterken: Kamera wide, Kiko merkezde, ev sol tarafta
Sahne 02 başlarken: Kamera wide, Kiko hâlâ merkezde, ev hâlâ sol tarafta

### Yasak olan:

- Sahne 1'de sol taraftaki ev, sahne 2'de sağa geçemez
- Kamera açısı aniden değişemez
- Karakter pozisyonu tutarsız olamaz

---

## Kural 2: Mekan Tutarlılığı

Her mekanda objelerin pozisyonu tüm sahneler boyunca aynı kalmalıdır.

### Nasıl uygulanır:

Her mekan için bir "Spatial Layout" tanımı olmalıdır:

```text
## Spatial Layout — [MEKAN ADI]

| Objey | Pozisyon | Renk |
|---|---|---|
| Kiko | Merkez, 0.85 m yükseklik | Coral pink #F8BBD0 |
| Top | Kiko'nun sağında, yerde | Sarı #FFD54F |
| Ağaç | Sol arka plan | Yeşil #81C784 |
| Ev | Sol taraf | Pembe #F8BBD0 |
```

### Örnek:

Sahne 02'de top Kiko'nun sağındaysa, sahne 03'te de Kiko'nun sağındadır.
Sahne 02'de ağaç sol taraftaysa, sahne 03'te de sol taraftadır.

### Yasak olan:

- Objeler sahneler arası yer değiştiremez
- Kamera açısı değişse bile mekan düzeni aynı kalır
- Yeni objeler rastgele eklenemez (sadece senaryo gereği)

---

## Kural 3: Karakter Pozisyonu

Karakterlerin sahne içindeki pozisyonu tutarlı olmalıdır.

### nasıl uygulanır:

| Karakter | Varsayılan Pozisyon | Not |
|---|---|---|
| Kiko | Merkez veya hafif sol | Ana karakter |
| Mimi | Kiko'nun yanında veya sağında | Arkadaş |
| Opa | Üstte (ağaç dalı) | Gözlemci |

### Yasak olan:

- Kiko bir sahnede solda, diğerinde sağda olamaz (hareket yoksa)
- Mimi Kiko'nun önünde olamaz (arkadaş pozisyonu)

---

## Kural 4: Işık Tutarlılığı

Aynı mekandaki tüm sahnelerde ışık yönü ve rengi aynı olmalıdır.

### Nasıl uygulanır:

| Mekan | Işık Yönü | Renk |
|---|---|---|
| Flower Hill | Sol üst | Sıcak sarı #FFF9C4 |
| Butterfly Meadow | Merkez üst | Sıcak sarı #FFF9C4 |
| Central Square | Merkez üst | Sıcak sarı #FFF9C4 |
| Opa's Tree | Sol üst | Sıcak sarı #FFF9C4 |

### Yasak olan:

- Bir sahne güneşli, diğeri bulutlu olamaz
- Işık yönü değişemez (sabah/akşam geçişi yoksa)

---

## Kural 5: Ses Sürekliliği

Sahne geçişlerinde sesler kesintisiz aktarılmalıdır.

### Nasıl uygulanır:

| Geçiş | Ses Davranışı |
|---|---|
| Aynı mekan | Ambiyans aynı kalır |
| Farklı mekan | Ambiyans yavaşça değişir (crossfade) |
| Koşma | Adım sesleri devam eder |
| Durma | Sesler yavaşça azalır |

### Yasak olan:

- Aniden sessizlik
- Aniden yüksek ses
- Tutarsız ambiyans

---

## Kural 6: Zaman Tutarlılığı

Günün saati tüm bölüm boyunca aynı kalmalıdır.

### Nasıl uygulanır:

| Bölüm | Günün Saati | Işık |
|---|---|---|
| Sabah bölümü | Sabah | Sıcak günışığı |
| Öğle bölümü | Öğle | Parlak günışığı |
| Akşam bölümü | Akşam | Turuncu-pembe |
| Gece bölümü | Gece | Mavi-ay ışığı |

### Yasak olan:

- Bir sahne sabah, diğeri akşam olamaz
- Gökyüzü rengi değişemez (aynı bölüm içinde)

---

## Uygulama Şablonu

Her sahne dosyasına şu bölümler eklenmelidir:

### 1. Camera Continuity

```text
## Camera Continuity

| Alan | Değer |
| --- | --- |
| Previous scene end | [Önceki sahnenin son kamera açısı] |
| This scene start | [Bu sahnenin başlangıç açısı] |
| This scene end | [Bu sahnenin bitiş açısı] |
| Next scene will start | [Bir sonraki sahne nereden başlayacak] |
```

### 2. Spatial Layout

```text
## Spatial Layout

| Obje | Pozisyon | Renk | Not |
| --- | --- | --- | --- |
| [Obje adı] | [X, Y koordinatı] | [Hex kodu] | [Ek bilgi] |
```

---

## Kontrol Listesi

Her sahne yayınlanmadan önce kontrol edilmelidir:

- [ ] Kamera açısı bir önceki sahneyle uyumlu mu?
- [ ] Mekandaki objelerin pozisyonu tutarlı mı?
- [ ] Karakter pozisyonu mantıklı mı?
- [ ] Işık yönü ve rengi tutarlı mı?
- [ ] Sesler kesintisiz mi?
- [ ] Günün sahi değişmedi mi?

---

## Kural 7: Etkileşimli Öğeler (3-4 Yaş)

3-4 yaş grubu çocukları ekranla etkileşim kurar. Bu etkileşimler kasıtlı ve kontrollü olmalıdır.

### Karakterin İzleyiciye Bakması

| Durum | Süre | Not |
|---|---|---|
| Doğrudan bakış | 2-3 saniye | Göz teması, güven hissi |
| Selamlama | 1-2 saniye | El sallama, gülümseme |
| Davet | 2-3 saniye | "Gel", "Birlikte bakalım" |

### Soru Sorma

| Tür | Örnek | Süre |
|---|---|---|
| Basit soru | "What's that?" | 3-4 saniye |
| Seçim sorusu | "Red or blue?" | 4-5 saniye |
| Tekrar sorusu | "Can you say hello?" | 3-4 saniye |

### Bekleme Süreleri

| Durum | Süre | Not |
|---|---|---|
| Soru sonrası | 3-4 saniye | Çocuğun cevap vermesi için |
| Keşif sonrası | 2-3 saniye | İzlemenin tadını çıkarması için |
| Gülme sonrası | 1-2 saniye | Paylaşma anı |

### Tekrar Öğeleri

| Öğe | Tekrar | Amaç |
|---|---|---|
| Cümle | 3-4 kez | Öğrenme |
| Hareket | 2-3 kez | Taklit |
| Melodi | Her bölüm | Tanıdıklık |

### Etkileşim Kuralları

```
✓ Yavaş ve kontrollü
✓ Sıcak ve davetkar
✓ Tekrar edilebilir
✓ Basit ve anlaşılır

✗ Hızlı ve rahatsız edici
✗ Zorlayıcı veya utandırıcı
✗ Karmaşık
✗ Korkutucu
```

---

*Bu belge PomPom Hills production kuralları için referansdır.*
