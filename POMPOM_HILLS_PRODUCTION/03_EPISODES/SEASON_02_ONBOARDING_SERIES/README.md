# Season 2 Onboarding — Scene Klasörü

---

## Amaç

Bu klasör, `Character and World Onboarding Policy` (`11-DOCS/02_SEASON_STRATEGY.md` §1-11, `08-PRODUCTION/PROJECT_ROADMAP.md` "Character and World Onboarding Policy") uyarınca Sezon 2 için üretilecek **tanıtım (intro) videolarının shot seviyesindeki sahne dosyalarını** içerir.

Bu klasör, planlama dokümantasyonunun (`SEASON_2_ONBOARDING/`) production-ready shot dosyalarına çevrildiği yerdir. Planlama dokümanları hâlâ tek doğruluk kaynağıdır; buradaki dosyalar onlardan üretilir.

Bu, düzenli bölüm numaralandırmasından (S02E01, S02E02, ...) **ayrı** bir klasördür. Onboarding videoları düzenli bölüm sırasına girmez; onboarding politikasının 10. maddesindeki sıraya göre önce yayınlanır, sonra ilgili karakter/dünya normal bölümlere girer.

---

## Onboarding Sırası (Policy §10)

```
1. Canon dokümantasyonu tamamlanır
2. Hero View / karakter referansı onaylanır
3. Tanıtım videosu üretilir      ← BU KLASÖR
4. Shorts çıkarılır
5. İlk basit hikaye üretilir
6. Düzenli bölüm kullanımı başlar
```

---

## Bölüm Listesi

| # | Klasör | Tür | Konu | Süre | Mekan | Durum |
|---|--------|-----|------|------|-------|-------|
| 01 | `onb-e01-meet-pip/` | Karakter | Meet Pip! | 45 sn (3×15) | Central Square | 🟡 Taslak — canon karakter dosyası bekliyor |
| 02 | `onb-e02-meet-tilly/` | Karakter | Meet Tilly! | 45 sn (3×15) | Tillo's Garden | 🟡 Taslak — canon karakter dosyası bekliyor |
| 03 | `onb-e03-meet-fifi/` | Karakter | Meet Fifi! | 45 sn (3×15) | Cloud Hill | 🟡 Taslak — canon karakter dosyası bekliyor |
| 04 | `onb-e04-welcome-to-crystal-cave/` | Dünya | Welcome to Crystal Cave | 45 sn (3×15) | Stone Hill → Crystal Cave | 🔴 Bloklu — Hero View + World Spec eksik |

---

## Onboarding Gate (Neden bazı bölümler "bloklu"?)

Policy §5 ve §10, bir dünyanın tanıtım videosu üretilmeden önce şu ikisinin tamamlanmasını şart koyar:

1. Canon Hero View onaylanmış olmalı
2. Production-ready World Spec tamamlanmış olmalı

Crystal Cave için ikisi de henüz yok (`SEASON_2_ONBOARDING/worlds/crystal-cave.md` → Status: Planned). Bu yüzden `onb-e04-welcome-to-crystal-cave/` klasöründeki shot dosyaları **taslak** olarak yazılmıştır; gerçek render'a girmeden önce:

- [ ] `POMPOM_HILLS_PRODUCTION/02_WORLDS/32-crystal-cave/` bible + world-spec dosyaları oluşturulmalı
- [ ] Hero View görseli onaylanmalı
- [ ] Bu shot dosyaları Hero View'e göre güncellenmeli

Aynı gate karakterler için de geçerlidir (Policy §2, madde 1: "Canon documentation complete" gerekir). Pip, Tilly ve Fifi için `01-CHARACTERS/` altında henüz numaralı bir canon karakter dosyası yok — sadece `SEASON_2_ONBOARDING/characters/*.md` onboarding taslağı var. Bu üç bölüm de gate durumuna göre 🟡 işaretlenmiştir: shot dosyaları yazılabilir ve prodüksiyon ekibi hazırlanabilir, ancak gerçek render öncesi canon karakter dosyası (`01-CHARACTERS/14-pip.md` vb.) onaylanmalıdır.

---

## Klasör Yapısı

Her bölüm klasörü şunları içerir:

| Dosya | İçerik |
|-------|--------|
| `01-overview.md` | Episode lock tablosu, onboarding gate durumu, karakter/dünya referansı |
| `shots/shot-01-...md` | İlk shot (giriş) |
| `shots/shot-02-...md` | İkinci shot (imza hareket / duygu anı) |
| `shots/shot-03-...md` | Üçüncü shot (Kiko ile karşılaşma / kapanış) |

Şablon: `04-SCENES/_templates/SCENE_TEMPLATE.md`
Continuity standardı: `00-CORE/SHOT_PRODUCTION_STANDARD.md`

---

## Sonraki Adımlar (her bölüm için)

1. Canon dokümantasyon / Hero View onayı (gate'i geç)
2. Bu klasördeki shot dosyalarını Hero View'e göre doğrula
3. Render prompts'u üret ve QA yap
4. `videos/intros/` altına landscape + shorts çıkışlarını yerleştir
5. `08-PRODUCTION/SEASON_1_EPISODE_GUIDE.md` tarzı bir "Intro Videoları" tablosuna işlensin

---

*Bu klasör Sezon 2 onboarding shot üretimi için tek kaynaktır.*
*Referans: `11-DOCS/02_SEASON_STRATEGY.md`, `SEASON_2_ONBOARDING/README.md`*
*Oluşturulma: 4 Temmuz 2026*
