# Shot 5 — Hata Raporu ve Çözüm Analizi

> Tarih: 15 Temmuz 2026
> Durum: ÇÖZÜLMEDİ — Yeniden üretim gerekli

---

## 1. Tespit Edilen Sorunlar

### 1.1 Sharpness (Keskinlik) — KRİTİK

| Metrik | Shot 1 (Referans) | Shot 5 | Fark |
|--------|-------------------|--------|------|
| Edge @3s | 7.5 | 5.6 | -1.9 |
| Edge @7s | 7.2 | 4.9 | -2.3 |
| Edge @10s | 7.4 | 4.8 | -2.6 |
| **Ortalama** | **7.4** | **5.1** | **-2.3 (~%31)** |

**Neden kritik:** Tüm timecode'larda tutarlı biçimde düşük. Bu, encode sırasında oluşan bir sorun değil — kaynak videonun kendisinde var.

### 1.2 Brightness (Parlaklık)

- Shot 1: 147.9
- Shot 5: 142.5
- Fark: **-5.4 birim**

### 1.3 Contrast (Kontrast)

- Shot 5'in orijinal kontrastı zaten düşüktü
- `contrast=0.88` düzeltmesi onu daha da mat yaptı
- Renkler soluk, canlılık azalmış

### 1.4 Character Hallucination

Sol tarafta insan görünümlü karakter (kahverengi saç topuzu, pembe üst) belirmiş. Kiko olması gereken yerde pembe kedi yerine insan character çıkmış. Bu sorun shot 3, 4, 5, 6'da ortak.

---

## 2. Neden Çözülemedi

### 2.1 Encode Düzeltmeleri Yetersiz Kalıyor

Denenen düzeltmeler:

| Deneme | Parametre | Sonuç |
|--------|-----------|-------|
| 1 | `brightness=0.036, contrast=0.88, saturation=0.85` | Sharpness: 5.1 (değişmedi) |
| 2 | `unsharp=3:3:0.5:3:3:0` eklendi | Sharpness: 5.0 (değişmedi) |
| 3 | `unsharp=5:5:1.0:5:5:0.5` (güçlü) | Sharpness: 5.3 (hâlâ düşük) |

**Neden çalışmıyor:**

1. **Sharpness kaynaktan geliyor:** OpenArt video üretimi sırasında shot-5 daha düşük çözünürlükte veya daha agresif compression ile üretilmiş. Edge detection tüm timecode'larda (~5.0) sabit — bu, encoding artefactı değil, kaynak kalitesi sorunu.

2. **Unsharp mask yetersiz:** FFmpeg'in unsharp filtresi sadece mevcut edge bilgisini vurgular. Eğer kaynakta edge bilgisi zaten yoksa (bulanık), filtre yeni detay üretemiyor.

3. **Brightness düzeltmesi sharpness'ı etkiliyor:** Parıltı artırıldığında kontrast azalıyor, bu da sharpness algısını daha da düşürüyor.

### 2.2 Character Hallucination Çözülemez

OpenArt'ın Kiko character reference'ını doğru yorumlayamaması:
- Kiko pembe kedi olmalı
- Ama OpenArt insan görünümlü karakter üretiyor
- Bu sorun prompt'ta değil, modelin character reference anlama yeteneğinde
- Encode ile düzeltilmez

---

## 3. Root Cause Analizi

```
Shot 5 düşük kalitede üretilmiş
    ↓
Edge detection ~5.0 (Shot 1: ~7.4)
    ↓
FFmpeg unsharp mask denenmiş
    ↓
Kaynakta edge bilgisi olmadığı için filtre etkisiz
    ↓
Brightness düzeltmesi kontrastı daha da düşürmüş
    ↓
Sonuç: Çözümsüz — yeniden üretim gerekli
```

---

## 4. Öneri

**Shot 5'i yeniden üret.** Mevcut video encode ile kurtarılamaz.

Yeniden üretimde dikkat edilecekler:
- Character reference: Approved Mimi + Kiko (insan değil, pembe kedi)
- Prompt Enhancer: OFF
- Cinematic Camera: OFF
- Frame-to-Video modunda 15sn üret
- Üretim sonrası ilk kontrol: sharpness (edge ~7.4 olmalı)

---

## 5. İlgili Dosyalar

| Dosya | Durum |
|-------|-------|
| `shot-5.mp4` | Düşük kalite, yeniden üretim gerekli |
| `shot-5-last-frame.jpg` | Karakter hallucination mevcut |
| `video-b-openart-prompt.md` | Yeniden üretim için kullanılacak |
| `video-c-openart-prompt.md` | Shot 5 bağımlı |

---

*Bu dosya MFC-EP01 shot-5 hata analizi için tek kaynaktır.*
