# TODO — Proje Tutarlılık ve Sorun Listesi (ÇÖZÜLDÜ)

Bu dosya, Yuvarlak Dünya / Pompom Hills reposunun detaylı incelemesi sonucu bulunan
sorunları ve yapılan düzeltmeleri kaydeder. Tüm maddeler işlendi.

## Yapılan Ana Kararlar (Single Source of Truth)
- **Karakter renk/tür/ölçek:** `CHARACTER_REFERENCE_GUIDE_v2.1.md` + `VARIABLES.md` + `characters/pompom-hills/*` esas alındı.
- **Bölüm sayısı:** Sezon 1 = **26 bölüm** (README, TECH_SPECS, CHANGELOG, CHARACTER_REFERENCE ile uyumlu).
- **Karakter stratejisi:** Repo 13 karakterlik kadroya taşınmış durumda; strateji dokümanları buna göre "Production Update" notlarıyla uzlaştırıldı (trio çıpa + cameo kadro).
- **İsim yazımı:** "Pompom Hills" (tek yazım).

---

## 🔴 Kritik — Karakter Renk / Tür
- [x] Mimi rengi/türü: `NAMING_REFINEMENT.md` lavanta tavşan → soft mavi `#90CAF9`, sarı t-shirt. (Diğer kaynaklar zaten "lavender yasak" diyordu.)
- [x] Kiko rengi: `NAMING_REFINEMENT.md` `#FFAB91` → Coral Pink `#F8BBD0`.
- [x] `NAMING_REFINEMENT.md` AI-consistency satırları güncellendi.

## 🔴 Kritik — Ölçek
- [x] `VARIABLES.md`: Opa 0.75 m → **1.20 m** (en uzun), Mimi 0.85 → **0.80 m**, Kiko notu düzeltildi.
- [x] `PRODUCTION_RULES.md`: Kiko "0.85 m yükseklik" → "1.00 m boy".

## 🔴 Kritik — Sezon / Bölüm Sayısı ve Strateji
- [x] Bölüm sayısı: `SERIES_STRUCTURE_v2.1.md` 20/30 → **26** (fazlar, oranlar, yüzdeler, lead özet tablosu güncellendi).
- [x] "Sezon 1 sadece trio" çelişkisi: `SERIES_STRUCTURE` §10 ve `NAMING_REFINEMENT` §10'a "Production Update" notu eklendi (13 karakterlik cameo kadro + trio çıpa).
- [x] Mirnik çelişkisi: "gelecek yan karakter" listesinden çıkarıldı, ana cameo kadrosu olarak not düşüldü.
- [x] Plan↔klasör uyumu: Örnek plan "illüstratif havuz" olarak etiketlendi; kanonik sıra `scenes/season-01/` (ilk 6 üretilen bölüm listelendi).
- [x] Catchphrase: `CHARACTER_REFERENCE_GUIDE`'a EN catchphrase eşlemeleri eklendi (Bak!/What's that? vb.).

## 🟠 Yüksek — Eksik / Yanlış Referanslar
- [x] `examples/` klasörü oluşturuldu (`examples/README.md` — metadata standardı).
- [x] `ai-prompts/VOICE_PROMPTS.md` referansı → `ai-prompts/voice/` olarak düzeltildi (README tablo + workflow).
- [x] README "Production Files" tablosuna eksik dosya/klasörler eklendi (VARIABLES, PRODUCTION_RULES, AUDIO_STYLE_GUIDE, TECH_SPECS, Color/, Environments/, environment/, Props/, characters/, videos/, ozel/).
- [x] Boş `Story Bible/` klasörü kaldırıldı (içerik `WORLD_BIBLE_v2.1.md`'de).
- [x] Boş prop klasörlerine `.gitkeep` eklendi (Props/Backgrounds, Props/SceneSpecific/S01E01–06).

## 🟠 Yüksek — Environments Numaralandırma
- [x] Tekrarlı numaralar giderildi: flower/tree/stone hill bibleları → `25/26/27` (01–24 render setiyle çakışmıyor).
- [x] `environment/8-lulu-greenhouse.png` → `8-lulus-greenhouse.png` (bible ile eşleşti).
- [x] `Environments/README.md` eklendi (numaralandırma + `environment/`↔`Environments/` ilişkisi).

## 🟠 Yüksek — Scene (S01E01) Yapısı
- [x] Tekrarlı 04/05 numaraları giderildi; yeni sıra: 04-trio, 05-arda … 14-mimo, **15-goodbye-handoff (sonda)**.
- [x] Dosya içi "Scene NN" etiketleri ve "Sonraki sahne" zinciri yeni numaralara göre güncellendi.
- [x] `scenes/README.md` intro-arc tablosu ve `s01e01/README.md` Scene Order + Visual Continuity (Opa artık görünür) güncellendi.
- [x] Eksik İngilizce/detaylı `EPISODE_SUMMARY.md` dosyaları e03–e06 için oluşturuldu.

## 🟡 Orta — İsimlendirme / Sürümleme / Prompt
- [x] "PomPom" → "Pompom" (9 dosyada, global).
- [x] `CHANGELOG.md` sürüm başlıkları: v2.1 / **v2.0** / **v1.0**; "v1/v2.0" referansı düzeltildi.
- [x] `{camera}` ve `{lighting}` tanımları README ↔ VARIABLES arasında tek metne getirildi.
- [x] `{background}` opsiyonel 4. değişken olarak README'de netleştirildi.

## 🟢 Düşük — Yazım / İçerik Bütünlüğü
- [x] `PRODUCTION_RULES.md`: "Objey"→"Obje", "nasıl"→"Nasıl", "Günün sahi"→"Günün saati".
- [x] `SERIES_STRUCTURE_v2.1.md`: "neverdwelled"→"never dwelled".
- [x] CJK bozuk karakterler temizlendi: `WORLD.md` başlık, `CHARACTER_DESIGN_GUIDE.md` (圆/急), `04-trio-hello.md` (同一), `s01e04 COORDINATE_MAP` (更强), `05-arda`/`15-goodbye` scene metinleri. (WORLD.md'deki Japonca dünya adı bilinçli, korundu.)
- [x] Karakter–mekân eşlemesi: `WORLD_BIBLE_v2.1.md`'ye "Residents & Location Ownership" bölümü eklendi (13 kadro + ambient owner-name ayrımı).

## Notlar — Sorun Olmayan / Bilgi
- `.DS_Store` ve video dosyaları git'te izlenmiyor (`.gitignore` çalışıyor); ek işlem gerekmedi.
- README ASCII Türkçe (aksansız) yazımı bilinçli bir stildir; "Yuvarlak Dunya - Pompom Hills" iki dilli alt başlık olarak korundu.

## Kullanıcı Kararına Bırakılanlar (creative)
- Örnek bölüm havuzu 26 satıra genişletilmedi; kanonik sıra `scenes/` altındadır. İstenirse tam 26 bölümlük plan yazılabilir.
- "Trio-only vs ensemble" yönü dokümanlarda uzlaştırıldı ama kadro küçültülmedi; nihai yaratıcı karar sizindir.
