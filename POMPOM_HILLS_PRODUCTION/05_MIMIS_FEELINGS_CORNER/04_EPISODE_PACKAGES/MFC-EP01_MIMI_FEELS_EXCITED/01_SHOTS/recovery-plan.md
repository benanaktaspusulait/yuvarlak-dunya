# Shot 5 & Shot 6 — Kurtarma Planı

> Tarih: 15 Temmuz 2026
> Durum: UYGULANACAK
> Kapsam: Shot 5 (sharpness + character) ve Shot 6 (character)

---

## Sorun Özeti

| Shot | Sharpness | Brightness | Character | Kamera |
|------|-----------|------------|-----------|--------|
| 1 | 7.4 ✅ | 147.9 ✅ | Mimi ✅ | Sabit ✅ |
| 4 | 7.2 ✅ | 144.1 ✅ | Yanlış karakter ❌ | Sabit ✅ |
| 5 | **5.1 ❌** | 142.5 (-5.4) | **Yanlış karakter ❌** | **Yaklaşmış ❌** |
| 6 | 7.6 ✅ | 145.7 ✅ | Yanlış karakter ❌ | Sabit ✅ |

---

## Kurtarma Stratejisi

### Shot 5 — Tam Kurtarma

Shot 5'i yeniden OpenArt'a vermek yerine mevcut materyallerden edit içinde yeniden kur.

#### Adım 1: Yedekleme
```
Orijinal shot-5.mp4 → shot-5-backup.mp4 (değiştirilmeden korunur)
```

#### Adım 2: Yanlış Kiko'yu Kaldır
1. Yanlış karakterin etrafına hareketli maske çiz
2. Karakteri videodan kaldır
3. Arkada kalan alanı temiz Flower Hill karesiyle doldur (clean background plate)

#### Adım 3: Doğru Kiko Katmanı Ekle
Öncelik sırası:
1. Aynı kamera açısından daha önce doğru üretilmiş temiz Kiko görüntüsü
2. Shot 3 veya Shot 4'teki doğru Kiko hareketinden kesilmiş kısa bir parça
3. Onaylı Kiko PNG'si kullanılarak hazırlanmış hafif animasyonlu katman
4. Son çare olarak yalnızca Kiko'nun bulunduğu küçük bölgeyi yeniden üretmek

#### Adım 4: Küçük Hareketleri Edit İçinde Oluştur
Shot 5'te karakterler yürümüyor, konumları sabit ve yalnızca küçük jestler yapıyor:
- Nefes alma
- Göz kırpma
- Tek el hareketi

#### Adım 5: AI Restoration
```
Orijinal Shot 5
→ hafif temporal noise reduction
→ AI video restoration / 2× upscale
→ tekrar hedef çözünürlüğe küçültme
```

> Not: Videoyu 2× iyileştirip tekrar hedef çözünürlüğe küçültmek, doğrudan `unsharp` uygulamaktan daha temiz sonuç verir. Ancak kayıp detay tamamen geri gelmez; AI bazı detayları tahmin eder.

#### Adım 6: Colour Match
Shot 1 veya Shot 4'ten referans kare seç:
- siyah seviyesi
- orta tonlar
- highlight seviyesi
- white balance
- saturation

**Sabite değer kullanma** — referans kareden eşleştir.

#### Adım 7: Final Sharpening
Çok hafif final sharpening uygula.

---

### Shot 6 — Lokal Kurtarma

Shot 6 için tüm shot'ı yeniden üretmeye gerek yok. Yalnızca sorunlu bölge değiştirilir.

#### Adım 1: Yedekleme
```
Orijinal shot-6.mp4 → shot-6-backup.mp4
```

#### Adım 2: Yanlış Karakteri Maskelenir
- Yanlış Kiko maskeyle kaldırılır
- Doğru karakter katmanı eklenir

#### Adım 3: Zıplama Bölgesi
Eğer zıplama tam beden görünümü gerektiriyorsa:
- Temiz geniş kompozisyon üzerinden shot yeniden kurulur
- Zıplama çok karmaşıksa yalnızca 1–1.5 saniyelik zıplama bölgesi lokal olarak yeniden üretilip mevcut videoya eklenir

#### Adım 4: Geri Kalan Kısım
Konuşma, nefes ve izleyici bekleme bölümü mevcut videodan korunur.

---

## Kamera Yaklaşması Sorunu

Shot 5'te yalnızca bulanıklık değil, kamera da Shot 4'e göre yaklaşmış durumda. Bunu sharpening düzeltemez.

### Seçenek A — Mevcut Yakın Kadrajı Kabul Et (Önerilen)
- Shot 5'i bilinçli bir medium shot gibi kullan
- Shot 4'ten Shot 5'e temiz cut yapılır
- Yanlış Kiko değiştirilir
- Görsel restoration uygulanır
- **En az iş isteyen yöntem**

### Seçenek B — Geniş Kadrajı Edit İçinde Yeniden Kur
- Shot 4'ün temiz geniş karesi arka plan olarak kullanılır
- Mimi ve doğru Kiko ayrı katmanlar hâlinde yerleştirilir
- Shot 5'in küçük jestleri edit içinde canlandırılır
- **Görsel devamlılık açısından en temiz sonuç**

---

## Uygulanacak Gerçek Kurtarma Planı

```
1. Shot 5 ve Shot 6 orijinal dosyalarını değiştirmeden yedekle.

2. Shot 5:
   - yanlış Kiko'yu maskeyle kaldır
   - temiz background plate oluştur
   - doğru Kiko katmanı ekle
   - küçük hareketleri edit içinde oluştur
   - AI restoration uygula
   - Shot 1/4'e colour-match et

3. Shot 6:
   - yalnızca sorunlu karakter veya zıplama bölgesini değiştir
   - tüm shot'ı gereksiz yere yeniden üretme
   - aynı restoration ve colour-match zincirini uygula

4. Bütün 90 saniyelik bölüm tamamlanınca:
   - tek final colour pass
   - tek final upscale
   - tek final encode yap
```

---

## Araçlar

- **Maskeleme/Compositing:** After Effects, DaVinci Resolve, veya Nuke
- **AI Restoration:** Topaz Video AI, DaVinci Neural Engine, veya Real-ESRGAN
- **Colour Match:** DaVinci Resolve Color Match veya手动 curves

---

## Dürüst Sonuç

| İşlem | Durum |
|-------|-------|
| Bulanıklık düzeltme | Kısmen düzeltilebilir, tamamen eski detayına döndürülemez |
| Yanlış karakter değiştirme | **Kesin olarak değiştirilebilir**, maskeleme/compositing gerekir |
| Kamera yaklaşmasını düzeltme | Sharpening ile mümkün değildir |
| En sağlam çözüm | Shot 5 ve Shot 6'yı mevcut materyallerden edit içinde yeniden kur |
| Diğer 4 video | Dokunmaya gerek yok |

---

*Bu dosya MFC-EP01 kurtarma planı için tek kaynaktır.*
