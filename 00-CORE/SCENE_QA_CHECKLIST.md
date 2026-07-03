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
- [ ] 4 shot dosyası var mı? (shot-01, shot-02, shot-03, shot-04)
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

### 3. Shot-02+ Kontrolü

- [ ] Frame Lock var mı? (frame zero, @image1)
- [ ] Camera Lock var mı? (identical camera position)
- [ [ ] Lighting Lock var mı? (first frame must preserve exact lighting)
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
- [ ] Character presence var mı?
- [ ] Text Safety var mı?

### 7. World Continuity

- [ ] Doğru mekan kullanılmış mı?
- [ ] Mekan LOCKED mı?
- [ ] Yeni establishing shot yasak mı?
- [ ] Dünya yeniden tasarlanmamış mı?

### 8. Character Continuity

- [ ] Doğru karakterler kullanılmış mı?
- [ ] Karakterler zaten sahnede mi? (shot-02+)
- [ ] Karakter ölçeği doğru mu? (6-8% frame)
- [ ] Yeni karakter girişi yasak mı?

### 9. Lighting Continuity

- [ ] Işık continuity reference'dan mı geliyor?
- [ ] Exposure kilitli mi?
- [ ] Brightness kilitli mi?
- [ ] Colour grading kilitli mi?
- [ ] Sahne parlaklaşmamış/kararmamış mı?

### 10. Camera Continuity

- [ ] Kamera mesafesi korunuyor mu?
- [ ] Close-up kaçınılmış mı?
- [ ] Dramatic push-in/pull-back yok mu?
- [ ] Yeni establishing shot yok mu?

### 11. Dialogue Continuity

- [ ] Diyalog talimatları çelişkili mi?
- [ ] Bir shot'ta hem diyalog var hem "no dialogue" denmiş mi?
- [ ] Önceki shot'tan diyalog tekrarlanmış mı?
- [ ] Sessiz shot'larda diyalog satırı var mı?
- [ ] Devam shot'larında neden devam ettiği açıklanmış mı?

### 12. Shot Duration Feasibility

- [ ] Shot süresi, diyalog, aksiyon, kamera hareketi ve geçiş için gerçekçi mi?
- [ ] Diyalog + gezinme varsa minimum 8 saniye mi?
- [ ] Diyalog + kapı + yeni alana geçiş varsa minimum 10 saniye mi?
- [ ] Dışarıdan içeriye geçiş varsa minimum 10-12 saniye mi?
- [ ] Shot aşırı yüklü değil mi? (gerekirse iki shot'a bölünmeli)

---

## Otomatik Kontrol Script'i

```bash
# Scene QA doğrulama
bash scripts/validate-scene.sh 04-SCENES/season-01/s01eXX-episode-name/
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
| 5 | Character presence yok | Evet → Red |
| 6 | Text Safety yok | Evet → Red |
| 7 | Close-up var | Evet → Red |
| 8 | Karakter ölçeği yanlış | Evet → Red |
| 9 | Dünya yeniden tasarlanmış | Evet → Red |
| 10 | Yeni establishing shot | Evet → Red |

---

## Onay Süreci

1. **Sahne oluşturuldu** → QA kontrolü yap
2. **Tüm maddeler geçildi** → Video üretimine geç
3. **Bir madde eksik** → Düzelt, tekrar kontrol et
4. **Video üretildi** → Pre-render checklist uygula

---

*Bu belge sahne kalite kontrolü için tek kaynaktır.*
*Her yeni sahne bu listeden geçirilmelidir.*
