# Kalite Kontrol Rehberi — Yeni Seriler

## 1. Amaç

Her üretilen bölümün kalitesini standartlara uygun olarak kontrol etmek ve yayın öncesi onay almak.

---

## 2. Kontrol Listesi (Her Bölüm İçin)

### 2.1 Görsel Kalite

- [ ] Karakter merkezde mi? (%15-20 scale)
- [ ] Karakter net mi? (bulanık yok)
- [ ] Karakter crop edilmemiş mi?
- [ ] Renkler canlı ve tutarlı mı?
- [ ] Arka plan temiz mi? (çok karmaşık değil)
- [ ] Işık yeterli mi? (karanlık değil)

### 2.2 Ses Kalitesi

- [ ] Ses net mi?
- [ ] Arka plan sesi çok mu yüksek? (olmamalı)
- [ ] Müzik sakin mi? (hızlı değil)
- [ ] Karakter sesi duyuluyor mu?

### 2.3 İçerik Kalitesi

- [ ] İlk 3 saniyede dikkat çekiyor mu?
- [ ] Hikaye anlaşılır mı?
- [ ] Tekrar eden cümle doğru mu?
- [ ] Kapanış sıcak mı?
- [ ] Pedagojik mesaj net mi?

### 2.4 Teknik Kalite

- [ ] Çözünürlük doğru mu? (1080x1920)
- [ ] Süre doğru mu? (belirtilen sn)
- [ ] FPS doğru mu? (24)
- [ ] Encoding doğru mu? (H.264, CRF 18)

---

## 3. QA Sonrası Aksiyonlar

| Durum | Aksiyon |
|-------|---------|
| ✅ Tüm kontrollerden geçti | Yayına hazırla |
| ⚠️ Ufak sorunlar var | Düzelt ve yeniden kontrol et |
| ❌ Ciddi sorunlar var | Yeniden üret |

---

## 4. Red Kuralları

| Durum | Neden | Çözüm |
|-------|-------|-------|
| Karakter görünmüyor | İzleyici ne izlediğini anlayamaz | Prompt'ta karakter pozisyonunu netleştir |
| Karakter çok küçük | Karakter tanınamaz | Scale'i %15-20'ye çıkar |
| Karakter crop edilmiş | Kısmi görünüm kafa karıştırıcı | Karakteri merkeze al |
| Ses çok yüksek | Çocukları rahatsız edebilir | Sesi düşür |
| Hızlı kurgu | Çocuklar takip edemez | Kurguyu yavaşlat |

---

## 5. Thumbnail Kontrolü

Her bölüm için 6 frame çıkar ve en iyisini seç:

```bash
for t in 2 8 15 45 90 110; do
  ffmpeg -y -ss $t -i [ANA_VIDEO] -vframes 1 -q:v 2 "thumb_${t}s.jpg"
done
```

**Seçim Kriterleri:**
- Karakter görünür mü?
- Renkler canlı mı?
- Duygu var mı?
- Arka plan temiz mi?

---

*Oluşturulma: 10 Temmuz 2026*
