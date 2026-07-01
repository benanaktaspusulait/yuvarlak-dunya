# Yuvarlak Dünya Projesi - Üretim Dokümantasyon Güncelleme Planı

**Tarih:** 1 Temmuz 2026  
**Durum:** Aktif  
**Öncelik:** Yüksek  

## Genel Durum

Projemizde scene (sahne) dosyalarının Visual Prompt (OpenArt Director Format) bölümleri OpenArt'ın anlayamayacağı şekilde yazılmış durumda. OpenArt, PRODUCTION_PIPELINE.md referanslarını ve NEGATIVE_PROMPTS.md dosyalarını okuyamıyor, bu da şu sorunlara yol açıyor:

1. **Environment yeniden tasarlanıyor** - OpenArt referans dosyaları görmezden gelip ortamı yeniden üretiyor
2. **Karakterlerin ölçeği değişiyor** - Noah gibi karakterler gerçek bir okul öncesi çocuğundan daha büyük görünüyor
3. **Referans kilitleri çalışmıyor** - Character Reference ve World Reference kuralları prompt'ta tekrar edilmediği için dikkate alınmıyor
4. **Üretim standartları kayboluyor** - Pipeline kuralları OpenArt'a iletilemiyor

## Çözüm: OpenArt Director Format Yeniden Yapılandırması

**06-noah-intro.md dosyasındaki başarılı formata geçiş yapılacak:**

1. PRODUCTION_PIPELINE.md referanslarının tamamen kaldırılması
2. Tüm kuralların prompt'un içine gömülmesi
3. Açık ve net "ABSOLUTELY LOCKED" ifadelerinin kullanılması
4. Tüm known failure modların NEGATIVE listesinde açıkça belirtilmesi

## Güncellenecek Dosyalar

### S01E01 - Hello Pompom Hills (15 sahne)
- [x] `01-kiko-intro.md` - Ana karakter girişi **✓ GÜNCELLENDİ**
- [x] `02-mimi-intro.md` - Mimi girişi **✓ GÜNCELLENDİ**
- [ ] `03-opa-intro.md` - Opa girişi
- [ ] `04-trio-hello.md` - Üçlü selamlaşma
- [ ] `05-arda-intro.md` - Arda girişi
- [x] `06-noah-intro.md` - **✓ ZATEN GÜNCELLENDİ** (model)
- [ ] `07-aiko-intro.md` - Aiko girişi
- [ ] `08-amara-intro.md` - Amara girişi
- [ ] `09-sofia-intro.md` - Sofia girişi
- [ ] `10-luca-intro.md` - Luca girişi
- [ ] `11-freya-intro.md` - Freya girişi
- [ ] `12-tillo-intro.md` - Tillo girişi
- [ ] `13-mirnik-intro.md` - Mirnik girişi
- [ ] `14-mimo-intro.md` - Mimo girişi
- [ ] `15-goodbye-handoff.md` - Veda sahnesi

### Diğer Bölümler (S01E02 - S01E06)
*Not: Önce S01E01 tamamlandıktan sonra diğer bölümlere geçilecek*

- [ ] S01E02 - Bounce Bounce Kiko (tüm sahneler)
- [ ] S01E03 - The Little Flower (tüm sahneler)
- [ ] S01E04 - Mimi's Big Yawn (tüm sahneler)
- [ ] S01E05 - Colours Everywhere (tüm sahneler)
- [ ] S01E06 - The Soft Wind (tüm sahneler)

## Güncelleme Standardı

Her sahne dosyası şu değişiklikleri içermeli:

### 1. Başlık ve Versiyon Güncellemesi
```markdown
# Scene [numara] - [Karakter Adı] [Açıklama] v3.4
```

### 2. PRODUCTION_PIPELINE.md Referanslarının Kaldırılması
- Dosya başındaki "Follow PRODUCTION_PIPELINE.md" notu kaldırılacak
- Environment Plate bölümündeki world reference notu kaldırılacak
- Production Standard bölümü tamamen kaldırılacak

### 3. Visual Prompt (OpenArt Director Format) Bölümünün Yeniden Yazılması

**Yeni format şablonu:**
```
Create a cinematic 16:9 shot inside the EXISTING [Environment Name] of Pompom Hills.

IMPORTANT: The supplied [Environment Name] world reference is ABSOLUTELY LOCKED.
Treat it as an already-built location.
DO NOT redesign it. DO NOT regenerate it. DO NOT reinterpret it. DO NOT restyle it. DO NOT replace any objects.

Preserve EXACTLY:
- [Environment-specific öğeler listesi]

The environment MUST remain visually identical to the supplied [Environment Name] reference.
Only add [Character Name] into the existing world.

----------------------------------------
CHARACTER
Use the supplied [Character Name] reference sheet exactly.
Never redesign [Character Name].
Keep:
- [Karakter özellikleri listesi]
No costume changes. No hairstyle changes. No facial redesign.

----------------------------------------
SCALE
[Character Name] is a SMALL preschool child.
He/She occupies ONLY about [X]% of the entire frame.
He/She is NOT the visual focus.
The environment is the hero.
[Environment objects] must appear life-sized relative to [Character Name].
No oversized child.

----------------------------------------
ACTION
[Karakter aksiyonu detaylı açıklama]

----------------------------------------
CAMERA
[Kamera ayarları]

----------------------------------------
LIGHTING
[Işık ayarları]

----------------------------------------
STYLE
[Stil tanımı]

----------------------------------------
NEGATIVE
Reject immediately if any of these happen:

- [Karakter] larger than a real preschool child
- [Environment öğeleri] change color/shape/position
- Environment regenerated
- New environment created
- Different landscape
- Different world layout
- Extra buildings
- Random text
- Wrong proportions
- [Sahneye özgü reddetme kuralları]

The final image should look exactly like the supplied [Environment Name] world, with only [Character Name] naturally inserted into it.
```

### 4. Production Standard Bölümünün Basitleştirilmesi
Yerine şu basit not konulacak:
```markdown
## Animation Notes

- [Karakter]'un hareketleri yumuşak, doğal ve sakin.
- [Sahneye özgü animasyon notları]
- Kamerada hafifçe yavaş hareket (slow‑in / slow‑out).
- Gölgeler yumuşak, kontrast düşük.
```

## Öncelik Sırası

1. **S01E01'in tüm sahneleri** - Çünkü bu bölümdeki karakter girişleri projenin temelini oluşturuyor
2. **Central Square ortamını kullanan sahneler** - Aynı ortamda tutarlılık sağlamak için
3. **Diğer ortamlardaki sahneler** - Her ortam için ayrı template oluşturulacak
4. **TR versiyonları** - İngilizce versiyonlar tamamlandıktan sonra

## Kontrol Listesi (Her Dosya İçin)

- [ ] Versiyon numarası güncellendi mi? (v3.4)
- [ ] PRODUCTION_PIPELINE.md referansları kaldırıldı mı?
- [ ] Visual Prompt yeni OpenArt Director Format'a göre yazıldı mı?
- [ ] "ABSOLUTELY LOCKED" ifadesi kullanıldı mı?
- [ ] Environment öğeleri "Preserve EXACTLY" listesinde belirtildi mi?
- [ ] Karakter özellikleri "Keep:" listesinde belirtildi mi?
- [ ] Scale açıkça tanımlandı mı? (%8-10 frame)
- [ ] NEGATIVE listesi tüm known failure modları kapsıyor mu?
- [ ] Production Standard bölümü basitleştirildi mi?
- [ ] Dosya Türkçe karakterlerle sorunsuz kaydedildi mi?
- [ ] Git commit yapıldı mı?

## Beklenen Sonuçlar

1. **OpenArt'ın anlama oranında %90+ artış** - Prompt'lar artık AI'nın anlayacağı dilde
2. **Environment tutarlılığında %95+ iyileşme** - Ortamlar artık yeniden tasarlanmayacak
3. **Karakter ölçeğinde %100 tutarlılık** - Tüm karakterler gerçek okul öncesi çocuk boyutunda
4. **Üretim hızında %40 artış** - Daha az regenerate, daha çok kabul edilebilir output
5. **Ekip iletişiminde iyileşme** - Tüm kurallar prompt'un içinde, ek dosya referansı yok

## Riskler ve Mitigasyon

| Risk | Olasılık | Etki | Mitigasyon |
|------|----------|------|------------|
| Bazı sahnelerde ortam değişikliği gerekebilir | Düşük | Orta | Her sahne için ortam kontrol listesi oluşturulacak |
| Karakter referans dosyaları eksik olabilir | Orta | Yüksek | `characters/drawings/` dizini kontrol edilecek |
| TR versiyonlarda çeviri hataları | Düşük | Düşük | İngilizce versiyonlar tamamlandıktan sonra kontrol |
| Dosya sayısı fazla, iş yükü yüksek | Yüksek | Orta | Otomasyon script'i yazılabilir, batch processing |

## Sonraki Adımlar

1. ✅ Noah dosyasını güncelle (model olarak kullan)
2. [ ] Kiko dosyasını güncelle
3. [ ] Mimi dosyasını güncelle
4. [ ] Opa dosyasını güncelle
5. [ ] Tüm S01E01 sahnelerini tamamla
6. [ ] Otomasyon script'i yaz (opsiyonel)
7. [ ] Diğer bölümlere geç

## İlerleme Takibi

**Toplam Sahne:** 15 (S01E01) + ~60 (diğer bölümler) = ~75 sahne  
**Tamamlanan:** 3/75 (%4.0)  
**Tahmini Tamamlanma:** 2-3 gün  
**Son Güncelleme:** 1 Temmuz 2026 (Kiko ve Mimi güncellendi)