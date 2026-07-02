# YouTube Workflow — PomPom Hills

---

## Amaç

Bu dosya YouTube'a yükleme sürecini, Made for Kids gereksinimlerini ve yayın stratejisini tanımlar.

---

## 1. Video Formatları

| Format | Boyut | Kullanım |
|--------|-------|----------|
| Landscape | 1280x720 (16:9) | Ana YouTube kanalı |
| Shorts | 1080x1920 (9:16) | YouTube Shorts |

---

## 2. Üretim Sırası

```
1. Shot videosunu üret (15 sn)
2. Shorts versiyonunu oluştur (9:16 crop)
3. Tüm shot'ları birleştir (60 sn veya 7 dk)
4. Ses ekle (diyalog + SFX + müzik)
5. Altyazı ekle (TR + EN)
6. Final episode'u kaydet
7. Thumbnail oluştur
8. Metadata hazırla (başlık, açıklama, tag)
9. YouTube'a yükle
```

---

## 3. Shorts Oluşturma

```bash
ffmpeg -i shot-01-video.mp4 -vf "crop=ih*9/16:ih,scale=1080:1920" -c:a copy shot-01-shorts.mp4
```

---

## 4. Birleştirme

```bash
echo "file 'shot-01-video.mp4'" > concat.txt
echo "file 'shot-02-video.mp4'" >> concat.txt
echo "file 'shot-03-video.mp4'" >> concat.txt
echo "file 'shot-04-video.mp4'" >> concat.txt
ffmpeg -f concat -safe 0 -i concat.txt -c copy final-episode.mp4
```

---

## 5. Thumbnail Kuralları

### Boyut ve Safe Area

| Alan | Değer |
|------|-------|
| Toplam boyut | 1280 x 720 px |
| Safe area (mobil) | 1168 x 658 px |
| Safe area (desktop) | 1280 x 720 px |
| Sol alt köşe | Süre bandı için boş bırak |
| Sağ alt köşe | Süre bandı için boş bırak |

### Tasarım Kuralları

- **Tek mutlu yüz:** Maksimum 1 karakter, yüz net görünür
- **Net aksiyon:** Karakter bir şey yapıyor
- **İçeriği temsil eden nesne:** Top, çiçek, yıldız vb.
- **Sıcak renkler:** Pastel, neon yok
- **Büyük metin:** Maks. 3 kelime, okunabilir
- **Kontrast:** Karakter arka plandan ayrılmalı

### Yasaklar

```
✗ Kalabalık (3+ karakter)
✗ Karanlık arka plan
✗ Çok metin (4+ kelime)
✗ Küçük yüz (okunamaz)
✗ Sert gölge
✗ Neon renk
```

### Thumbnail Prompt Şablonu

```text
Pompom Hills thumbnail, [KARAKTER] [AKSİYON] in [MEKAN],
warm pastel colors, round soft shapes, happy expression,
close-up face, child-friendly, 1280x720, {style} {lighting}
```

---

## 6. Başlık Formülü

```
[Karakter Adı] [Aksiyon] [Nesne]? [Emoji] PomPom Hills
```

**Kurallar:**
- Maks. 60 karakter
- Emoji ekle (1-2 adet)
- "Pompom Hills" her zaman sonda
- Büyük harf: Sadece ilk kelime ve özel isimler

**Örnekler:**
- "Kiko Topu Nereye Götürdü? 🟡 PomPom Hills"
- "Ağaç da Uykulu Mu? 🌳 PomPom Hills"
- "Mimi Neden Uyuyor? 🌙 PomPom Hills"

---

## 7. Açıklama Yapısı

```markdown
## [Bölüm Adı] 🎬

[Bölümün 2-3 cümlelik özeti]

### Bu bölümde ne öğreniyoruz?
• [Öğrenme 1]
• [Öğrenme 2]

### Karakterler
• [Karakter listesi]

### Mekan
• [Mekan adı]

---

🔔 Abone ol ve zili çal!
👍 Beğen ve paylaş!
💬 Yorum bırak!

#PompomHills #Preschool #Toddler #KidsAnimation #[BölümEtiketi]
```

---

## 8. Etiket Stratejisi

### Anahtar Kelimeler (15-20 adet)

```
kids animation, preschool, toddler, Pompom Hills, gentle, safe,
educational, baby cartoon, 3 year old, 4 year old, soft animation,
rounded shapes, pastel colors, bedtime story, learning colors,
sharing is caring, friendship, nature, animals, soft music
```

### Hashtag Seti

```
#PompomHills #YuvarlakDunya #Preschool #Toddler
#KidsAnimation #GentleKids #SafeContent
#BedtimeStory #LearningColors #Friendship
```

---

## 9. Playlist Stratejisi

| Playlist | İçerik | Amaç |
|----------|--------|------|
| **Full Episodes** | Tüm bölümler | Ana içerik |
| **Bedtime Stories** | Uyku bölümleri | Gece izleme |
| **Colors & Shapes** | Renk/şekil bölümleri | Eğitim |
| **Songs & Music** | Müzik bölümleri | Eğlence |
| **Best Of** | En popüler bölümler | Keşif |
| **New Episodes** | Son eklenenler | Takip |

---

## 10. Made for Kids Ayarları

### Zorunlu Ayarlar

| Ayar | Değer | Not |
|------|-------|-----|
| **Yaş grubu** | "Made for Kids" | COPPA uyumlu |
| **Yorumlar** | Kapalı | 13 yaş altı için zorunlu |
| **Bildirimler** | Kapalı | Çocuklar için |
| **Kişiselleştirilmiş reklamlar** | Kapalı | COPPA |
| **Altyazılar** | Açık | TR + EN |

### Yasak Ayarlar

```
✗ Kişiselleştirilmiş reklamlar
✗ Yorum bölümü açık
✗ Bildirimler açık
✗ Harici linkler (açıklamada link yok)
✗ Anketler
✗ Bağış
```

---

## 11. Yükleme Kontrol Listesi

```
□ Video 1280x720 (16:9) mü?
□ Ses net mi? (-6 dB tepe)
□ Thumbnail hazır mı? (1280x720)
□ Başlık formüle uygun mu? (≤60 karakter)
□ Açıklama yazıldı mı? (chapter'lı)
□ Etiketler eklendi mi? (15-20 adet)
□ Hashtag eklendi mi? (5-10 adet)
□ Yaş sınırı doğru mu? ("Made for Kids")
□ Yorumlar kapalı mı?
□ Altyazılar eklendi mi? (TR + EN)
□ Playlist'e eklendi mi?
□ Shorts versiyonu hazır mı?
```

---

## 12. Yükleme Zamanlaması

| Gün | Saat (UK) | Neden |
|-----|-----------|-------|
| Cumartesi | 10:00 | Çocuklar en çok cumartesi izler |
| Pazar | 09:00 | Sabah rutini |
| Çarşamba | 15:00 | Hafta ortası, okul sonrası |

**En iyi zaman:** Cumartesi 10:00 UK saati (UTC+1/GMT)

---

## 13. Analytics Takibi

| Metrik | Hedef | Frekans |
|--------|-------|---------|
| İzlenme süresi | 10+ dk/oturum | Haftalık |
| Abone artışı | +500/ay | Aylık |
| Etkileşim oranı | %5+ | Haftalık |
| Tıklama oranı (CTR) | %5+ | Haftalık |
| Retention oranı | %50+ (3 dk) | Bölüm bazında |

---

*Bu belge YouTube yükleme süreci için tek kaynaktır.*
*Son güncelleme: 2 Temmuz 2026*
