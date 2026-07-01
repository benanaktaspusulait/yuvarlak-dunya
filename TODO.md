# TODO — Proje Tutarlılık ve Sorun Listesi

Bu dosya, Yuvarlak Dünya / Pompom Hills prodüksiyon reposunun detaylı incelemesi sonucu
bulunan tutarsızlıkları, çelişkileri ve eksikleri listeler. Öncelik sırasına göre gruplanmıştır.

Not: Bu bir doküman/prodüksiyon reposudur (kod yok). "Sorun" = belgeler arası çelişki,
eksik dosya, yanlış referans veya isimlendirme/numaralandırma hatası.

---

## 🔴 Kritik — Karakter Renk ve Tür Çelişkileri

- [ ] **Mimi'nin rengi ve türü çelişkili (en kritik).**
  - `NAMING_REFINEMENT.md`: Mimi = **lavanta** tavşan, ana renk `#CE93D8`, lavanta t-shirt, "white with lavender patches".
  - `CHARACTER_REFERENCE_GUIDE_v2.1.md`, `VARIABLES.md`, `characters/pompom-hills/02-mimi.md`: Mimi = **soft mavi** `#90CAF9`, sarı t-shirt `#FFF59D`.
  - Dahası `CHARACTER_REFERENCE_GUIDE_v2.1.md` açıkça **"Lavender yasak"** ve "Lavender... versiyona dönüşmez" diyor.
  - → `NAMING_REFINEMENT.md` doğrudan diğer tüm kaynakların YASAKLADIĞI tanımı veriyor. Tek doğruya çekilmeli.

- [ ] **Kiko'nun ana rengi çelişkili.**
  - `NAMING_REFINEMENT.md`: Soft Coral `#FFAB91`, "coral shoes".
  - Diğer tüm kaynaklar (`VARIABLES.md`, `CHARACTER_REFERENCE_GUIDE_v2.1.md`, `CONTRIBUTING.md`, `01-kiko.md`): Coral Pink `#F8BBD0`.
  - → `NAMING_REFINEMENT.md`'deki hex güncellenmeli.

- [ ] `NAMING_REFINEMENT.md` genel olarak eski karakter tanımlarını taşıyor gibi. Baştan sona güncel karakter kilitleriyle (renk/tür/kıyafet) senkronlanmalı veya "tarihsel/arşiv" olarak işaretlenmeli.

---

## 🔴 Kritik — Ölçek (Boyut) Çelişkileri

- [ ] **Opa'nın boyu birçok dosyada ters.**
  - `README.md`, `CHANGELOG.md`, `PRODUCTION_RULES.md`, `CONTRIBUTING.md`, `CHARACTER_REFERENCE_GUIDE_v2.1.md`: Kiko=100, Mimi=80, **Opa=120 (en uzun)**.
  - `VARIABLES.md` "Boyut Standartları": Kiko=1.00 m, Mimi=**0.85 m**, Opa=**0.75 m (en kısa!)** ve "Kiko = En uzun karakter" notu.
  - → `VARIABLES.md` hem Opa'yı en kısa gösteriyor hem Mimi'yi 0.85 (0.80 olmalı) yapıyor. 100/80/120 standardına göre düzeltilmeli (ör. 1.00 m / 0.80 m / 1.20 m).

- [ ] **Kiko yüksekliği `PRODUCTION_RULES.md` Kural 2 örneğinde 0.85 m** olarak geçiyor; `VARIABLES.md`'de Kiko 1.00 m. Tek değere çekilmeli.

- [ ] Ölçü birimi tutarsız: bazı dosyalar "birim" (100/80/120), `VARIABLES.md` "metre" kullanıyor. Birim/metre dönüşümü net tanımlanmalı (örn. 100 birim = 1.00 m ise Opa 120 birim = 1.20 m).

---

## 🔴 Kritik — Sezon / Bölüm Sayısı ve Karakter Stratejisi Çelişkileri

- [ ] **Bölüm sayısı çelişkili.**
  - `README.md`, `CHANGELOG.md`, `CHARACTER_REFERENCE_GUIDE_v2.1.md`: **26 bölüm**.
  - `SERIES_STRUCTURE_v2.1.md`: sürekli **20 bölüm** ("Sample Season 1 Plan: 20 Episodes", "For 20 episodes") ve ayrıca "Episodes 21–30" (30) referansları.
  - → 20 / 26 / 30 karışık. Tek sayıda karar verilip her yerde güncellenmeli.

- [ ] **"Sezon 1 sadece ana trio" kuralı, üretilen içerikle çelişiyor.**
  - `SERIES_STRUCTURE_v2.1.md` ve `NAMING_REFINEMENT.md`: Sezon 1'de SADECE Kiko/Mimi/Opa; yan karakter Sezon 1'de konuşmaz; 5 bölümde en fazla 1 yeni karakter; rehber ilk 3 bölümde görünmez; bölüm 1–10'da en fazla 2 konuşan karakter.
  - Gerçek durum: `characters/pompom-hills/` altında **13 karakter** var ve `scenes/season-01/s01e01-hello-pompom-hills/` **tek bölümde 13 karakteri** (arda, noah, aiko, amara, sofia, luca, freya, tillo, mirnik, mimo dahil) tanıtıyor.
  - → Ya strateji dokümanları güncellenmeli ya da S01E01 yapısı kurallara uyacak şekilde yeniden planlanmalı.

- [ ] **Mirnik çelişkisi.** `SERIES_STRUCTURE_v2.1.md` Mirnik'i "gelecek yan karakter (kedi), Bölüm 16 görsel / Sezon 2 konuşma" olarak listeliyor; ama `characters/pompom-hills/12-mirnik.md` tam karakter olarak var ve S01E01'de tanıtılıyor (`12-mirnik-intro.md`). Karar netleştirilmeli.

- [ ] **Bölüm başlığı/numarası, planlanan sezonla uyuşmuyor.**
  - Plan (`SERIES_STRUCTURE_v2.1.md`): "The Little Flower"=Ep8, "Mimi's Big Yawn"=Ep10, "Colours Everywhere"=Ep11, "The Soft Wind"=Ep12.
  - Gerçek klasörler: `s01e03-the-little-flower`, `s01e04-mimis-big-yawn`, `s01e05-colours-everywhere`, `s01e06-the-soft-wind`.
  - Ayrıca `s01e02-bounce-bounce-kiko` planda yok. → Sezon planı ile scene klasörleri hizalanmalı.

- [ ] **Karakter catchphrase (nakarat) tutarsız.**
  - Kiko: `NAMING_REFINEMENT.md`/`01-kiko.md` "What's that?" vs `CHARACTER_REFERENCE_GUIDE_v2.1.md` "Bak!".
  - Mimi: "Let's see!" vs "Birlikte".
  - Opa: "Well done!" vs "Yavasca".
  - → Karakter başına tek resmi catchphrase (ya da EN/TR eşleşmesi) tanımlanmalı.

---

## 🟠 Yüksek — Eksik / Yanlış Dosya Referansları

- [ ] **`examples/` klasörü yok** ama `README.md` (Production Files tablosu + "Example Assets" bölümü) ve `CHANGELOG.md` ondan bahsediyor. Klasör oluşturulmalı ya da referanslar kaldırılmalı.

- [ ] **`ai-prompts/VOICE_PROMPTS.md` yok.** `README.md` bu dosyaya atıf yapıyor, ama gerçekte `ai-prompts/voice/` klasörü (00–13 numaralı dosyalar) var. README yolu düzeltilmeli.

- [ ] **`README.md` dosya listesi eksik.** Repoda olup tabloda yer almayanlar: `VARIABLES.md`, `AUDIO_STYLE_GUIDE.md`, `PRODUCTION_RULES.md`, `Color/`, `Environments/`, `Props/`, `characters/`, `ai-prompts/voice/`, `environment/`, `videos/`, `ozel/`, `Story Bible/`. Liste güncellenmeli.

- [ ] **`Story Bible/` klasörü boş.** Ya içerik eklenmeli ya kaldırılmalı (ayrıca isimde boşluk var — repo genel konvansiyonuna aykırı, bkz. `CONTRIBUTING.md` naming kuralı).

- [ ] Boş klasörler: `Props/Backgrounds/`, `Props/SceneSpecific/S01E02..S01E06/` (git boş klasör tutmaz — `.gitkeep` eklenmeli ya da doldurulmalı).

---

## 🟠 Yüksek — Environments Numaralandırma ve Eşleşme

- [ ] **`Environments/` içinde tekrarlı sıra numaraları:**
  - `03-flower-hill-bible.md` **ve** `03-kikos-home-bible.md` (ikisi de 03)
  - `05-mimis-burrow-bible.md` **ve** `05-tree-hill-bible.md` (ikisi de 05)
  - `06-opas-tree-bible.md` **ve** `06-stone-hill-bible.md` (ikisi de 06)
  - → Benzersiz numaralandırma yapılmalı.

- [ ] **`Environments/*.md` ile `environment/*.png` eşleşmiyor.**
  - `.png` seti: `3-kikos-home`, `5-mimis-burrow`, `6-opas-tree` ... (flower-hill / tree-hill / stone-hill PNG'leri YOK).
  - `.md` seti: flower-hill, tree-hill, stone-hill "bible"ları VAR ama karşılık PNG yok.
  - → Mekân listesi tek kaynaktan türetilip iki klasör senkronlanmalı.

- [ ] **İsim tutarsızlığı:** `environment/8-lulu-greenhouse.png` vs `Environments/08-lulus-greenhouse-bible.md` (lulu vs lulus). Tekilleştirilmeli.

- [ ] İki paralel klasör var: `environment/` (PNG) ve `Environments/` (MD). İsimlendirme (tekil/çoğul, büyük harf) kafa karıştırıcı; birleştirme ya da net ayrım dokümante edilmeli.

---

## 🟠 Yüksek — Scene (S01E01) Yapısı

- [ ] **`s01e01-hello-pompom-hills/` içinde tekrarlı sıra numaraları:**
  - `04-arda-intro` **ve** `04-trio-hello`
  - `05-goodbye-handoff` **ve** `05-noah-intro`
  - → Ayrıca `05-goodbye-handoff` mantıken bölümün SONUNDA olmalı, ortada değil. Numaralandırma yeniden düzenlenmeli.

- [ ] **Bölüm klasör yapısı tutarsız.** S01E01 karakter-intro dosyalarından oluşuyor; S01E02–E06 ise standart üretim dosyaları (`01-overview` … `09-render-prompts`). Ortak bir bölüm şablonu belirlenmeli.

- [ ] **`EPISODE_SUMMARY.md` (İngilizce) eksik.** Yalnızca `s01e02` hem `EPISODE_SUMMARY.md` hem `EPISODE_SUMMARY_TR.md` içeriyor. `s01e03`, `s01e04`, `s01e05`, `s01e06` sadece `_TR` sürümüne sahip. İngilizce özetler eklenmeli (veya standart tek dile karar verilmeli).

---

## 🟡 Orta — İsimlendirme ve Sürümleme

- [ ] **Proje adı büyük/küçük harf tutarsız:** `WORLD_BIBLE_v2.1.md` "**PomPom** Hills" kullanırken diğer dosyalar "**Pompom** Hills". Tek yazım seçilmeli.

- [ ] **Marka adı ikili:** "Yuvarlak Dunya" ve "Pompom Hills" farklı dosyalarda ana ad gibi kullanılıyor. Hangisinin resmi/alt başlık olduğu netleştirilmeli.

- [ ] **`CHANGELOG.md` sürüm başlıkları hatalı:** üç ayrı giriş de "## v2.1" başlıklı (Production Readiness Pass / Studio Bible Draft / Initial Concept Pack). Bunlar sırasıyla farklı sürüm olmalı (ör. v2.1 / v2.0 / v1.0). Ayrıca "Eski v1/v2.1 dosya referansları kaldırıldı" ifadesi kendi içinde çelişkili.

- [ ] Türkçe dosyalarda "Dunya" (ASCII) vs "Dünya" tutarsızlığı (README başlığı "Yuvarlak Dunya"). Karakter kodlaması/aksan politikası belirlenmeli.

---

## 🟡 Orta — Prompt Değişken Sistemi Tutarsızlığı

- [ ] **`{camera}` tanımı iki dosyada farklı:**
  - `README.md`: "stable **50mm** preschool camera, **eye-level or gentle wide shot**, no Dutch angle, no fisheye...".
  - `VARIABLES.md`: "stable **wide** preschool camera, clear readable staging, no fisheye, no shaky cam".

- [ ] **`{lighting}` tanımı iki dosyada farklı:**
  - `README.md`: "warm diffused daylight, soft contact shadows under 25 percent opacity, **no black night values**".
  - `VARIABLES.md`: "warm diffused daylight **or cozy blue night**, soft contact shadows under 25 percent, no hard darkness".
  - → "no black night values" vs "cozy blue night" çelişkisi (gece sahneleri var mı yok mu?).

- [ ] **`{background}` değişkeni** yalnızca `VARIABLES.md`'de var; `README.md` ve `CONTRIBUTING.md` "üç değişken" (`{style}`, `{camera}`, `{lighting}`) diyor. Dördüncü değişken resmileştirilmeli ya da kaldırılmalı.

---

## 🟢 Düşük — Yazım / Küçük Hatalar

- [ ] `PRODUCTION_RULES.md`:
  - "Kural 3" alt başlığı "### nasıl uygulanır:" küçük harfle (diğerleri "Nasıl").
  - Kontrol listesinde "Günün **sahi** değişmedi mi?" → "saati" olmalı.
  - Spatial Layout tablo başlığı "**Objey**" → "Obje".
- [ ] `SERIES_STRUCTURE_v2.1.md`: "feelings are acknowledged gently, **neverdwelled** upon" → "never dwelled" (eksik boşluk).
- [ ] `characters/.DS_Store` ve `characters/drawings/.DS_Store` repoda izleniyor gibi görünüyor; `.gitignore` `.DS_Store`'u yok saysa da daha önce commit'lenmiş olabilir. `git rm --cached` ile temizlenmeli.

---

## 🟢 Düşük — İçerik Bütünlüğü (Dünya Mantığı)

- [ ] **Mekân sahibi karakterler ile karakter kadrosu uyuşmuyor.**
  - `WORLD_BIBLE_v2.1.md` mekânları: Rosie's Rose Garden, Milo's Pond, Lily's Lavender Farm, Poppy's Bakery, Benny's Playground, Lulu's Greenhouse.
  - Ama `characters/pompom-hills/` içinde Rosie, Milo, Lily, Poppy, Benny, Lulu **yok**; buna karşılık kadroda olan arda, noah, aiko, amara, luca, freya, mirnik, mimo'nun **mekânı yok**.
  - → Karakter–mekân haritası tutarlı hale getirilmeli.

- [ ] `.gitignore` `*.mp4`, `*.mov`, `*.wav` yok sayıyor ama `videos/` klasörü repoda var (intro/short'lar). Video dosyalarının nasıl paylaşılacağı (LFS? harici?) netleştirilmeli.

---

## Önerilen İlk Adımlar

1. **Tek Kaynak (Single Source of Truth) belirle:** Karakter renk/tür/ölçek için `CHARACTER_REFERENCE_GUIDE_v2.1.md` + `VARIABLES.md`; `NAMING_REFINEMENT.md` ve `SERIES_STRUCTURE_v2.1.md`'yi buna göre güncelle.
2. **Ölçek çelişkisini** (Opa 0.75 → 1.20) hemen düzelt — üretim güvenliği açısından en riskli hata.
3. **Bölüm sayısına** (20 mi 26 mı) karar ver ve tüm dosyalarda tek değere çek.
4. **Environments ve scene numaralandırmalarındaki** tekrarları benzersizleştir.
5. **README dosya tablosunu** gerçek repo yapısıyla senkronla; olmayan (`examples/`, `VOICE_PROMPTS.md`) referansları düzelt.
