# Scene QA Checklist

---

## Usage

Her yeni sahne dosyası bu kontrol listesinden geçirilir.

Sahne oluşturulduktan hemen sonra kontrol edilir.

Video üretiminden ÖNCE tamamlanmalıdır.

---

## Kontrol Maddeleri

### 1. Dosya Yapısı

- [ ] `shots/` klasörü var mı?
- [ ] 6 shot dosyası var mı? (shot-01 ... shot-06)
- [ ] `09-render-prompts.md` var mı?
- [ ] `01-overview.md` var mı?

### 2. Shot-01 Kontrolü

- [ ] Yeni Take Shot olarak tanımlanmış mı?
- [ ] World reference belirtilmiş mi?
- [ ] Character reference belirtilmiş mi?
- [ ] Opening Hook bölümü var mı?
- [ ] Scale talimatı var mı? (6-8% frame)
- [ ] Text Safety var mı? (No subtitles)
- [ ] Negative Prompt var mı?

### 2B. Master Frame Action Layout Gate (master setup shot'ları — §0.1)

> Sadece obje "var mı?" değil, "aksiyon için doğru sahnelenmiş mi?" kontrolü.
> Ref: `00-CORE/19_VIDEO_PRODUCTION_PREFLIGHT_SYSTEM.md` §0.1.

- [ ] Sonraki shot'larda kullanılacak her aksiyon objesi belirlendi mi?
- [ ] Her aksiyon objesi master frame'de görünür mü? (cropped değil)
- [ ] Her aksiyon objesi sadece dekoratif değil, kullanılabilir interaction zone mu?
- [ ] Her aksiyon objesi karakterin doğal ulaşabileceği mesafede mi? (2–3 küçük adım)
- [ ] Her aksiyon objesi planlanan etkileşim için yeterince büyük mü?
- [ ] Kamera hareketi olmadan etkileşilebilir mi?
- [ ] Obje sonradan hareket/büyüme/çoğalma/spawn gerektirmeyecek şekilde mi konumlanmış?
- [ ] Aksiyon alanları ana landmark / transition objesiyle aynı wide frame içinde birlikte çalışıyor mu?
- [ ] Onay kriteri **var + yakın + usable + aksiyona uygun** sağlanıyor mu?

> Herhangi bir aksiyon objesi uzak / küçük / sadece dekoratif / karakter arkasında /
> sadece background ise → master frame **NOT READY**. First-frame still'i yeniden üret,
> kredi harcama.

### 3. Shot-02+ Kontrolü

- [ ] Frame Lock var mı? (frame zero, @image1)
- [ ] First visible frame visually indistinguishable from @image1 olarak yazılmış mı?
- [ ] @image1 complete visual master reference olarak tanımlanmış mı?
- [ ] Camera Lock var mı? (identical camera position)
- [ ] Lighting Lock var mı? (first frame must preserve exact lighting)
- [ ] Colour Identity Lock var mı? (white balance, exposure, saturation, contrast)
- [ ] Voice Continuity bölümü var mı? (speaking shots için)
- [ ] Character presence var mı? (already present at the beginning)
- [ ] Text Safety var mı? (No subtitles)
- [ ] Negative Prompt var mı?
- [ ] Micro Actions bölümü var mı?
- [ ] Reference Usage bölümü var mı?

### 4. Shot-03 Kontrolü

- [ ] Emotional Beat bölümü var mı?
- [ ] Close-up yok mu?
- [ ] Camera direction yumuşak mı?

### 5. Shot-04 Kontrolü

- [ ] Stronger Ending bölümü var mı?
- [ ] Emotional resting point tanimlı mı?
- [ ] Son saniye sabit mi?
- [ ] Yeni establishing shot yasak mı?

### 6. Render Prompts Kontrolü

- [ ] Her shot için render prompt var mı?
- [ ] @image1 kullanılıyor mu?
- [ ] Lighting lock var mı?
- [ ] Colour identity lock var mı?
- [ ] Speaking shot'larda Voice Continuity var mı?
- [ ] Character presence var mı?
- [ ] Text Safety var mı?

### 7. World Continuity

- [ ] Doğru mekan kullanılmış mı?
- [ ] Mekan LOCKED mı?
- [ ] Yeni establishing shot yasak mı?
- [ ] Dünya yeniden tasarlanmamış mı?
- [ ] Bu mekanın sub-zone'u varsa (örn. Flower Hill — Nature Field Zone / Home Cluster Zone), doğru zone belirtilmiş mi (sadece mekan adı değil)?
- [ ] Zone sahne boyunca tutarlı mı (sahne içinde zone habersiz değişmiyor mu)?

### 8. Character Continuity

- [ ] Doğru karakterler kullanılmış mı?
- [ ] Karakterler zaten sahnede mi? (shot-02+)
- [ ] Karakter ölçeği doğru mu? (6-8% frame)
- [ ] Yeni karakter girişi yasak mı?
- [ ] Intra-shot character continuity lock var mı? Karakter aynı shot içinde kaybolup tekrar belirmiyor mu?
- [ ] Single visible path rule var mı? Karakter yolu frame-to-frame okunuyor mu?
- [ ] Occlusion transition yasak mı? Karakter hiçbir noktada tam gövde saklanmıyor mu?
- [ ] Karakter hareketi fiziksel olarak mümkün, yavaş ve preschool-safe mi?

### 9. Lighting Continuity

- [ ] Işık continuity reference'dan mı geliyor?
- [ ] Light direction unchanged mı?
- [ ] Light intensity unchanged mı?
- [ ] Shadow softness unchanged mı?
- [ ] Ambient lighting unchanged mı?
- [ ] Highlight behaviour unchanged mı?
- [ ] Cloud brightness unchanged mı?
- [ ] Grass brightness unchanged mı?
- [ ] Exposure kilitli mi?
- [ ] Brightness kilitli mi?
- [ ] Sahne parlaklaşmamış/kararmamış mı?

### 10. Colour Identity

- [ ] White balance unchanged mı?
- [ ] Exposure unchanged mı?
- [ ] Colour temperature unchanged mı?
- [ ] Saturation unchanged mı?
- [ ] Contrast unchanged mı?
- [ ] Brightness unchanged mı?
- [ ] Pastel palette korunuyor mu?
- [ ] Cool shift / warm shift yok mu?
- [ ] Blue tint / green tint / magenta tint / orange grading yok mu?
- [ ] HDR look veya cinematic LUT yok mu?
- [ ] Episode tek bir continuous recording gibi görünüyor mu?

### 11. Camera Continuity

- [ ] Kamera mesafesi korunuyor mu?
- [ ] Close-up kaçınılmış mı?
- [ ] Dramatic push-in/pull-back yok mu?
- [ ] Yeni establishing shot yok mu?
- [ ] Camera must not break continuity kuralı var mı?
- [ ] Kamera hareketi karakteri foreground obje arkasında saklamıyor mu?
- [ ] Kamera background object shift / layout morphing oluşturmuyor mu?

### 11B. Global OpenArt Continuity Locks

- [ ] Hard Background Lock uygulanmış mı?
- [ ] Intra-Shot Character Continuity Lock uygulanmış mı?
- [ ] Single Visible Path Rule uygulanmış mı?
- [ ] Occlusion Is Not A Transition uygulanmış mı?
- [ ] Camera Must Not Break Continuity uygulanmış mı?
- [ ] First Second Continuity Hold uygulanmış mı? (`@image1` continuity shot'larda)
- [ ] Object Identity Lock uygulanmış mı?
- [ ] Gereksiz yürüme / set içinde uzun traversal varsa risk olarak flag'lenmiş mi?
- [ ] Negative Prompt global disappearance / occlusion / object morphing terimlerini içeriyor mu?

### 12. Dialogue Continuity

- [ ] Diyalog talimatları çelişkili mi?
- [ ] Bir shot'ta hem diyalog var hem "no dialogue" denmiş mi?
- [ ] Önceki shot'tan diyalog tekrarlanmış mı?
- [ ] Sessiz shot'larda diyalog satırı var mı?
- [ ] Devam shot'larında neden devam ettiği açıklanmış mı?

### 13. Voice QA

- [ ] Voice matches previous shot mı?
- [ ] Same voice identity korunuyor mu?
- [ ] Same pitch korunuyor mu?
- [ ] Same timbre korunuyor mu?
- [ ] Same speaking speed korunuyor mu?
- [ ] Same emotional tone korunuyor mu?
- [ ] Same age impression korunuyor mu?
- [ ] Same personality korunuyor mu?
- [ ] Same warmth korunuyor mu?
- [ ] Same speaking rhythm korunuyor mu?
- [ ] Same pronunciation korunuyor mu?
- [ ] Same accent korunuyor mu?
- [ ] Same recording quality korunuyor mu?
- [ ] Voice ID veya voice reference aynı mı?
- [ ] Previous shot audio voice reference olarak kullanılmış mı?
- [ ] Farklı narrator veya alternate voice oluşmamış mı?

### 14. Shot Duration Feasibility

- [ ] Shot süresi, diyalog, aksiyon, kamera hareketi ve geçiş için gerçekçi mi?
- [ ] Diyalog + gezinme varsa minimum 8 saniye mi?
- [ ] Diyalog + kapı + yeni alana geçiş varsa minimum 10 saniye mi?
- [ ] Dışarıdan içeriye geçiş varsa minimum 10-12 saniye mi?
- [ ] Shot aşırı yüklü değil mi? (gerekirse iki shot'a bölünmeli)

---

## Otomatik Kontrol Script'i

```bash
# Scene QA doğrulama
bash scripts/validate-scene.sh POMPOM_HILLS_PRODUCTION/02_WORLDS/<WORLD_NAME>/04_EPISODE_PACKAGES/S01Exx_EPISODE_NAME/
```

---

## Red Nedenleri

Bir sahne şu durumlarda reddedilir:

| # | Neden | Aşırı mı? |
|---|-------|----------|
| 1 | Shot dosyası eksik | Evet → Red |
| 2 | Frame Lock yok | Evet → Red |
| 3 | Camera Lock yok | Evet → Red |
| 4 | Lighting Lock yok | Evet → Red |
| 5 | Colour Identity Lock yok | Evet → Red |
| 6 | Speaking shot'ta Voice Continuity yok | Evet → Red |
| 7 | Character presence yok | Evet → Red |
| 8 | Text Safety yok | Evet → Red |
| 9 | Close-up var | Evet → Red |
| 10 | Karakter ölçeği yanlış | Evet → Red |
| 11 | Dünya yeniden tasarlanmış | Evet → Red |
| 12 | Renk tonu shot'lar arasında değişmiş | Evet → Red |
| 13 | Karakter sesi shot'lar arasında değişmiş | Evet → Red |
| 14 | Yeni establishing shot | Evet → Red |
| 15 | İlk frame @image1'den ayırt edilebilir derecede farklı | Evet → Red |
| 16 | Light direction / intensity / shadow softness değişmiş | Evet → Red |
| 17 | Voice pitch / pronunciation / accent / recording quality değişmiş | Evet → Red |
| 18 | Karakter aynı shot içinde kayboluyor, tekrar beliriyor, teleport oluyor veya side-switch yapıyor | Evet → Red |
| 19 | Karakter yolu sürekli görünür değil veya fiziksel olarak mümkün değil | Evet → Red |
| 20 | Foreground obje karakteri tam gövde saklıyor veya occlusion transition kullanılıyor | Evet → Red |
| 21 | Kamera hareketi karakteri saklayıp başka yerde yeniden gösteriyor | Evet → Red |
| 22 | Background obje pozisyon/ölçek/kimlik değiştiriyor veya layout morphing oluşuyor | Evet → Red |
| 23 | Bench/planter/bush/tree/path/house gibi bir obje kimlik değiştiriyor | Evet → Red |
| 24 | Master setup frame'de gelecek aksiyon objesi görünür ama uzak / küçük / dekoratif / ulaşılamaz (staging fail, §0.1) | Evet → Red |

Voice QA, Colour QA veya Lighting QA maddelerinden herhangi biri fail olursa shot reddedilir.

---

## Onay Süreci

1. **Sahne oluşturuldu** → QA kontrolü yap
2. **Tüm maddeler geçildi** → Video üretimine geç
3. **Bir madde eksik** → Düzelt, tekrar kontrol et
4. **Video üretildi** → Pre-render checklist uygula

---

*Bu belge sahne kalite kontrolü için tek kaynaktır.*
*Her yeni sahne bu listeden geçirilmelidir.*
