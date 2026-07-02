# POMPOM HILLS v3.1 — Eksik Tamamlama Görev Listesi

**Tek Dosya Halinde Kapsamlı Görev Planı**
**Tarih:** 2 Temmuz 2026
**Durum:** Aktif

---

## MEVCUT DURUM

| Kategori | Mevcut | Hedef | Durum |
|----------|--------|-------|-------|
| 00-CORE master dosya | 14 | 14 | ✅ |
| Karakter bible (.md) | 14 | 14 | ✅ |
| Karakter görseli (.png) | 14 | 14 | ✅ |
| Mekan bible (.md) | 27 | 27 | ✅ |
| Mekan görseli (.png) | 27 | 27 | ✅ |
| Bölüm klasörü | 15 | 26 | 🟡 11 eksik |
| _COMPLETED set | 1 | 26 | 🟡 25 eksik |
| AI prompt dosyası | 5 | 5 | ✅ |
| Voice dosyası | 14 | 14 | ✅ |
| Marka görseli | 4 | 4+ | ✅ |
| YouTube workflow | 1 | 1 | ✅ |
| Thumbnail template | 1 | 1 | ✅ |
| Metadata | 27 | 27 | ✅ |
| SRT dosyaları | 52 | 52 | ✅ |
| COPPA checklist | 1 | 1 | ✅ |
| Child safety rules | 1 | 1 | ✅ |
| Budget tracker | 1 | 1 | ✅ |
| Voice tracker | 1 | 1 | ✅ |
| Production calendar | 1 | 1 | ✅ |
| Music licenses | 1 | 1 | ✅ |
| scripts/ | 3 | 3 | ✅ |
| GitHub Actions | 1 | 1 | ✅ |
| Subtitles | 0 | 1 | ✅ yeni eklendi |
| Music licenses | 0 | 1 | ✅ yeni eklendi |
| scripts/ | 0 | 4+ | ❌ |

---

## GÖREV 1 — Dosya Varlık Kontrolü

### 1.1 Eksik Dosyaları Tespit Et
- [ ] README'de bahsedip repo'da olmayan dosyaları listele
- [ ] CHANGELOG'da "eklendi" denmiş ama olmayan dosyaları bul
- [ ] Eksikleri ya oluştur ya da dokümandan kaldır

### 1.2 Kritik Dosya Kontrolü
- [x] `00-CORE/CONTINUITY_RULES.md` — ✅ VAR
- [x] `00-CORE/NEGATIVE_PROMPTS.md` — ✅ VAR
- [x] `04-SCENES/_templates/SCENE_TEMPLATE.md` — ✅ VAR
- [x] `07-BRANDING/YOUTUBE_WORKFLOW.md` — ✅ YENİ EKLENDİ
- [x] `08-PRODUCTION/QC_CHECKLIST.md` — ✅ VAR
- [x] `08-PRODUCTION/TODO.md` — ✅ VAR
- [x] `08-PRODUCTION/SEASON_2_PLAN.md` — ✅ VAR

---

## GÖREV 2 — Karakter/Mekan Bible Tutarlılığı

### 2.1 Karakter Dosyaları
- [x] 01-CHARACTERS/ içinde 13 karakter .md — ✅ 14 dosya var
- [ ] 01-CHARACTERS/drawings/ içinde karakter PNG'leri — ❌ YOK
- [ ] Karakter görsellerini geri getir veya yeniden üret

### 2.2 Mekan Dosyaları
- [x] 02-WORLDS/ içinde 27 mekan .md — ✅ 27+2 dosya var
- [x] environment/ PNG'leri — ✅ 23/27 mevcut

### 2.3 Numara Eşleşmesi
- [ ] 25=flower-hill, 26=tree-hill, 27=stone-hill kontrolü
- [ ] Eksik 4 mekan görseli için prompt üret

---

## GÖREV 3 — Prompt Variable Sistemi

### 3.1 Değişken Tanımları
- [x] 00-CORE/VARIABLES.md içinde {style} {camera} {lighting} — ✅ VAR

### 3.2 Prompt Uyumu
- [ ] 05-AI-PROMPTS/ altındaki tüm promptlar bu 3 değişkenle başlıyor mu?
- [ ] Uymayan prompt bul ve düzelt
- [ ] Her sahne dosyasında değişken kullanımı kontrolü

---

## GÖREV 4 — Prod Pipeline Boşlukları

### 4.1 OpenArt Ayarları
- [ ] Resolution: 1920x1080
- [ ] FPS: 24
- [ ] Duration: 15 saniye/sahne
- [ ] Seed kullanımı tanımla

### 4.2 QC Reject Kuralları
- [x] PRODUCTION_PIPELINE.md'de reject kuralları — ✅ VAR (§Known Failure Modes)
- [ ] Her madde için somut kontrol maddesi ekle

### 4.3 Asset Versioning
- [ ] v01, v02 nasıl yönetiliyor tanımla
- [ ] Dosya isimlendirme standardı: `assetName_task_v###.blend`

---

## GÖREV 5 — Çocuk Güvenliği / Compliance

### 5.1 CREATIVE_BIBLE.md İçeriği
- [x] YouTube Kids COPPA uyum checklist — ✅ YENİ DOSYA OLUŞTURULDU
- [x] Yasak renk kombinasyonları — ✅ CHILD_SAFETY_RULES.md'de
- [x] Ses desibel limiti — ✅ CHILD_SAFETY_RULES.md'de
- [x] Kültürel hassasiyet — ✅ CHILD_SAFETY_RULES.md'de

### 5.2 Ek Kurallar
- [ ] CREATIVE_BIBLE.md'ye çocuk güvenliği referansı ekle
- [ ] Her bölüm dosyasında child safety check ekle

---

## GÖREV 6 — Teknik Eksikler

### 6.1 TECH_SPECS.md Kontrolü
- [x] Polygon count: Kiko 20k-35k tris — ✅ TANIMLI
- [x] Texture çözünürlük: 2K body + 1K face — ✅ TANIMLI
- [x] Render motoru: Blender Eevee/Cycles — ✅ TANIMLI
- [ ] Export format bitrate: H.264 için spesifik bitrate ekle

### 6.2 Belirsizlikleri Netleştir
- [ ] Motion blur ayarı (açık/kapalı)
- [ ] Render time hedefi (dakika/frame)
- [ ] Noise level standardı

---

## GÖREV 7 — Branding/Yayın

### 7.1 Mevcut Dosyalar
- [x] YOUTUBE_WORKFLOW.md — ✅ OLUŞTURULDU
- [x] THUMBNAIL_TEMPLATE.md — ✅ OLUŞTURULDU
- [x] METADATA/s01e01.md — ✅ ÖRNEK OLUŞTURULDU
- [x] MUSIC_SFX_LICENSES.md — ✅ OLUŞTURULDU

### 7.2 Eksikler
- [ ] Kalan 25 bölüm için metadata dosyaları (s01e02-s01e26)
- [ ] Channel banner 2560x1440 safe area şablonu
- [ ] Thumbnail PSD/Figma şablonu (görsel olarak)

---

## GÖREV 8 — Üretim Takip

### 8.1 Takip Dosyaları
- [x] PRODUCTION_CALENDAR.md — ✅ OLUŞTURULDU
- [x] BUDGET_TRACKER.md — ✅ OLUŞTURULDU
- [x] VOICE_TRACKER.md — ✅ OLUŞTURULDU

### 8.2 Eksikler
- [ ] EPISODE_TRACKER.md güncelle (s01e11-s01e26 ekle)
- [ ] Haftalık ilerleme raporu şablonu

---

## GÖREV 9 — Yazılı Bölümleri _COMPLETED Standardına Yükselt

### 9.1 Referans Şablon
- [x] S01E01/_COMPLETED/ klasörü — ✅ MEVCUT (15 dosya)

### 9.2 Eksik Bölümler
- [ ] S01E02 için _COMPLETED seti üret
- [ ] S01E03 için _COMPLETED seti üret
- [ ] S01E04 için _COMPLETED seti üret
- [ ] S01E05 için _COMPLETED seti üret
- [ ] S01E06 için _COMPLETED seti üret
- [ ] S01E07 için _COMPLETED seti üret
- [ ] S01E08 için _COMPLETED seti üret
- [ ] S01E09 için _COMPLETED seti üret
- [ ] S01E10 için _COMPLETED seti üret
- [ ] S01E11 için _COMPLETED seti üret (_COMPLETED'dan ana dizine taşı)
- [ ] S01E12-S01E15 için _COMPLETED seti üret

### 9.3 Her Bölüm İçin 9 Kanonik Dosya
```
01-overview.md
02-beat-sheet.md
03-storyboard.md
04-assets.md
05-camera.md
06-dialogues.md (TR + EN)
07-sfx.md
08-animation-notes.md
09-render-prompts.md
COORDINATE_MAP.md
EPISODE_SUMMARY.md (TR + EN)
```

---

## GÖREV 10 — Eksik Bölümleri Yaz (S01E16-S01E26)

### 10.1 Karakter Rotasyonunu Düzelt
- [ ] Aiko'ya en az 1 ana rol ver
- [ ] Amara'ya en az 1 ana rol ver
- [ ] Sofia'ya en az 1 ana rol ver
- [ ] Freya'ya en az 1 ana rol ver
- [ ] Tillo'ya en az 1 ana rol ver
- [ ] Mirnik'e en az 1 ana rol ver
- [ ] Mimo'ya en az 1 ana rol ver

### 10.2 Yeni Bölüm Senaryoları
- [ ] S01E16: [Bölüm adı] — Karakter: [X], Mekan: [Y]
- [ ] S01E17: [Bölüm adı] — Karakter: [X], Mekan: [Y]
- [ ] S01E18: [Bölüm adı] — Karakter: [X], Mekan: [Y]
- [ ] S01E19: [Bölüm adı] — Karakter: [X], Mekan: [Y]
- [ ] S01E20: [Bölüm adı] — Karakter: [X], Mekan: [Y]
- [ ] S01E21: [Bölüm adı] — Karakter: [X], Mekan: [Y]
- [ ] S01E22: [Bölüm adı] — Karakter: [X], Mekan: [Y]
- [ ] S01E23: [Bölüm adı] — Karakter: [X], Mekan: [Y]
- [ ] S01E24: [Bölüm adı] — Karakter: [X], Mekan: [Y]
- [ ] S01E25: [Bölüm adı] — Karakter: [X], Mekan: [Y]
- [ ] S01E26: [Bölüm adı] — Karakter: [X], Mekan: [Y]

### 10.3 Her Bölüm İçin
- [ ] 4+ sahne
- [ ] TR + EN diyalog
- [ ] Render prompt (OpenArt format)
- [ ] Continuity handoff

---

## GÖREV 11 — Görsel Varlık Boşlukları

### 11.1 Eksik Mekan Görselleri
- [ ] 4 eksik mekan için hero view prompt üret
- [ ] 05-AI-PROMPTS/ENVIRONMENT_PROMPTS.md'ye ekle

### 11.2 Prop Görselleri
- [ ] 03-PROPS/ klasörlerini PROP_ASSETS.md ile karşılaştır
- [ ] Eksik prop'lar için prompt üret

### 11.3 Karakter Görselleri
- [ ] characters/drawings/ klasörünü geri getir
- [ ] 13 karakter için PNG görselleri üret

---

## GÖREV 12 — Yayın & Metadata Katmanı

### 12.1 YouTube Workflow
- [x] YOUTUBE_WORKFLOW.md — ✅ OLUŞTURULDU

### 12.2 Metadata
- [x] s01e01.md — ✅ ÖRNEK
- [ ] s01e02-s01e26 için metadata dosyaları

### 12.3 Altyazı
- [x] SRT_TEMPLATE.md — ✅ OLUŞTURULDU
- [ ] 26 bölüm için SRT dosyaları (TR + EN)

---

## GÖREV 13 — Uyumluluk

### 13.1 COPPA
- [x] COPPA_MADE_FOR_KIDS_CHECKLIST.md — ✅ OLUŞTURULDU

### 13.2 Çocuk Güvenliği
- [x] CHILD_SAFETY_RULES.md — ✅ OLUŞTURULDU

### 13.3 Ek Kontroller
- [ ] Her bölüm dosyasında child safety check
- [ ] YouTube ayarları kontrol listesi

---

## GÖREV 14 — Otomasyon & Doğrulama

### 14.1 Scripts
- [ ] scripts/validate-naming.sh
- [ ] scripts/validate-continuity.py
- [ ] scripts/lint-prompts.py

### 14.2 GitHub Actions
- [ ] .github/workflows/validate.yml

---

## GÖREV 15 — Dokümantasyon Tutarlılığı

### 15.1 README/CHANGELOG
- [ ] README'de bahsedip olmayan dosyaları tespit et
- [ ] Eksikleri oluştur veya dokümandan kaldır

### 15.2 CONTRIBUTING
- [ ] Yeni scripts/ ve QC akışına göre güncelle

---

## Öncelik Sırası

| # | Görev | Durum | Öncelik |
|---|-------|-------|---------|
| 1 | Dosya varlık kontrolü | 🟡 Kısmen | Yüksek |
| 2 | Karakter/mekan tutarlılığı | ❌ Eksik görseller | Yüksek |
| 3 | Prompt variable uyumu | ✅ Kontrol gerekli | Orta |
| 4 | Prod pipeline boşlukları | 🟡 Kısmen | Orta |
| 5 | Çocuk güvenliği | ✅ Tamamlandı | Yüksek |
| 6 | Teknik eksikler | 🟡 Kısmen | Orta |
| 7 | Branding/yayın | 🟡 Kısmen | Yüksek |
| 8 | Üretim takip | ✅ Tamamlandı | Orta |
| 9 | _COMPLETED setleri | ❌ 25 eksik | Yüksek |
| 10 | Yeni bölümler | ❌ 11 eksik | Yüksek |
| 11 | Görsel boşluklar | ❌ Eksikler var | Orta |
| 12 | Yayın/metadata | 🟡 Kısmen | Yüksek |
| 13 | Uyumluluk | ✅ Tamamlandı | Yüksek |
| 14 | Otomasyon | ❌ Hiç yok | Düşük |
| 15 | Dokümantasyon | ⏳ Bekliyor | Düşük |

---

*Bu dosya tüm eksiklerin tek listesidir.*
*Son güncelleme: 2 Temmuz 2026*
