# YOUTUBE WORKFLOW — PomPom Hills

---

## Amaç

Bu dosya YouTube'a yükleme sürecini tanımlar.

Üretim, prompt veya stil kuralları içermez.

---

## 1. Video Formatları

| Format | Boyut | Kullanım |
|---|---|---|
| Landscape | 1280x720 (16:9) | Ana YouTube kanalı |
| Shorts | 1080x1920 (9:16) | YouTube Shorts |

---

## 2. Üretim Sırası

1. Shot videosunu üret (15 sn)
2. Shorts versiyonunu oluştur (9:16 crop)
3. Tüm shot'ları birleştir (60 sn)
4. Final episode'u kaydet

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

## 5. Başlık Formülü

```
[Karakter Adı] [Aksiyon] [Nesne]? [Emoji] PomPom Hills
```

Örnekler:
- "Kiko Topu Nereye Götürdü? 🟡 PomPom Hills"
- "Ağaç da Uykulu Mu? 🌳 PomPom Hills"
- "Mimi Neden Uyuyor? 🌙 PomPom Hills"

---

## 6. Thumbnail Kuralları

- Tek mutlu yüz
- Net aksiyon
- İçeriği temsil eden nesne
- Sıcak renkler
- Sağ alt köşe boş (süre bandı)

**Yasak:** Kalabalık, karanlık, çok metin

---

## 7. Açıklama Yapısı

```
İlk 3 cümle: Konu özeti
Orta: Hikaye kısa özet
Son: "İzlemeye devam et" + linkler
Anahtar kelimeler: preschool, toddler, gentle, safe, educational
```

---

## 8. Etiketler

```
kids animation, preschool, toddler, Pompom Hills, gentle, safe, educational, baby cartoon, 3 year old, 4 year old, soft animation, rounded shapes, pastel colors
```

---

## 9. Yaş Sınırı

Tüm içerikler "Made for Kids" olarak işaretlenmeli.

---

## 10. Yayın Kontrol Listesi

```
✓ Video 16:9 mü?
✓ Ses net mi?
✓ Thumbnail hazır mı?
✓ Başlık formüle uygun mu?
✓ Açıklama yazıldı mı?
✓ Etiketler eklendi mi?
✓ Yaş sınırı doğru mu?
```
