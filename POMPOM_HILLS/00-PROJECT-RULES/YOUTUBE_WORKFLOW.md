# YOUTUBE WORKFLOW — PomPom Hills

---

## Video Formatları

| Format | Boyut | Kullanım |
|---|---|---|
| Landscape | 1280x720 (16:9) | Ana YouTube kanalı |
| Shorts | 1080x1920 (9:16) | YouTube Shorts |

---

## Üretim Sırası

1. Shot videosunu üret (15 sn)
2. Shorts versiyonunu oluştur (9:16 crop)
3. Tüm shot'ları birleştir (60 sn)
4. Final episode'u kaydet

---

## Dosya Yapısı

```
outputs/
├── shot-01-video.mp4
├── shot-02-video.mp4
├── shot-03-video.mp4
├── shot-04-video.mp4
├── final-episode.mp4
├── shorts/
│   ├── shot-01-shorts.mp4
│   ├── shot-02-shorts.mp4
│   ├── shot-03-shorts.mp4
│   └── shot-04-shorts.mp4
└── thumbnails/
    └── thumbnail.png
```

---

## Shorts Oluşturma

```bash
ffmpeg -i shot-01-video.mp4 -vf "crop=ih*9/16:ih,scale=1080:1920" -c:a copy shot-01-shorts.mp4
```

---

## Birleştirme

```bash
echo "file 'shot-01-video.mp4'" > concat.txt
echo "file 'shot-02-video.mp4'" >> concat.txt
echo "file 'shot-03-video.mp4'" >> concat.txt
echo "file 'shot-04-video.mp4'" >> concat.txt
ffmpeg -f concat -safe 0 -i concat.txt -c copy final-episode.mp4
```

---

## YouTube Yükleme Bilgileri

| Alan | Değer |
|---|---|
| Başlık | `{Character} | PomPom Hills | Episode {X}` |
| Açıklama | Bölüm özeti (İngilizce) |
| Etiketler | kids animation, preschool, toddler, Pompom Hills |
| Kategori | Education or Kids |
| Yaş sınırı | Made for Kids |
