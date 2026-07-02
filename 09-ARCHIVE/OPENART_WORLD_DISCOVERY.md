# OpenArt World Production Discovery

---

## Test Sonucu

OpenArt, referans görsellerdeki **yazıları, etiketleri ve tabloları görmezden gelmez.**

Bu yanlış bir varsayımdı.

---

## Sonuç

### Documentation Images (Bible için)

- Hero View + etiket
- Left View + etiket
- Right View + etiket
- Top View + etiket
- Açıklamalar, tablolar, notlar

**Kullanım:** İnsan referansı, Bible dokümanı

### Clean Images (OpenArt World için)

- Aynı açılar
- Ama yazısız
- Etiketsiz
- Tabelasız
- Açıklamasız

**Kullanım:** OpenArt World oluşturma

---

## Yeni Pipeline

```
Environment Bible
    │
    ├── Documentation Images (yazılı) → İnsan referansı
    │
    └── Clean Images (yazısız) → OpenArt World
            │
            ├── Hero Clean
            ├── Left Clean
            ├── Right Clean
            └── Top Clean
            │
            ▼
        World LOCK
```

---

## Test Edilmesi Gerekenler

1. **Clean referanslar** yazı sorununu çözüyor mu?
2. **Kaç referans** World oluşturmak için yeterli? (1, 2 veya 4)
3. **Left ve Right** sadece sahne tutarlılığı için mi kullanılmalı?

---

## Not

Bu bilgi production pipeline'ın temelini değiştirir.

OpenArt World için **her zaman clean PNG** kullanılmalıdır.

Documentation PNG'leri sadece Bible referansıdır.
