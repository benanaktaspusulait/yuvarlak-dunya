# Worlds

Bu klasör her mekanın **story/production bible**'ını (`.md`) tutar.
Mekanların **referans görselleri (PNG)** `environment/` klasöründedir (proje root'unda).

## Klasör İlişkisi

| Klasör | İçerik |
| --- | --- |
| `POMPOM_HILLS_PRODUCTION/02_WORLDS/` | Mekan bibleları (bu klasör, `.md`) |
| `environment/` | Mekan referans görselleri (`.png`, proje root'unda) |

`POMPOM_HILLS_PRODUCTION/02_WORLDS/NN-<slug>-bible.md` ile `environment/NN-<slug>.png` **aynı numara ve slug**'ı paylaşır.

## Numaralandırma

- **01–27**: Tüm mekanların bible'ı bu klasördedir. Numaralar `environment/` içindeki görsel setiyle birebir eşleşir.
- Bazı mekanlar tek bir düz PNG (`environment/NN-slug.png`), bazıları ise çok görünümlü klasördür (`environment/NN-slug/` içinde `hero-view.png`, `left-view.png`, `right-view.png`, `top-view.png`).
- **25–27 tepeleri** (flower/tree/stone) çok görünümlü klasör olarak tutulur:
  - `25-flower-hill-bible.md` → `environment/25-flower-hill/`
  - `26-tree-hill-bible.md` → `environment/26-tree-hill/`
  - `27-stone-hill-bible.md` → `environment/27-stone-hill/`

## 01–24 Mekan Listesi

1. central-square · 2. cloud-hill · 3. kikos-home · 4. sun-hill · 5. mimis-burrow ·
6. opas-tree · 7. tillos-garden · 8. lulus-greenhouse · 9. poppys-bakery ·
10. bennys-playground · 11. tillos-treehouse · 12. milos-pond · 13. rosies-rose-garden ·
14. lilys-lavender-farm · 15. rainbow-bridge · 16. friendship-meadow · 17. butterfly-meadow ·
18. little-forest · 19. rainbow-creek · 20. wish-pond · 21. camping-grove · 22. story-circle ·
23. art-corner · 24. adventure-trail

> Not: `00-CORE/WORLD_BIBLE.md` altı ana tepeyi (Central, Cloud, Flower, Sun, Tree, Stone)
> coğrafi omurga olarak tanımlar. Bunların üçü (Flower/Tree/Stone) render plate'i olmadığı
> için 25–27 aralığında bible olarak tutulur.
