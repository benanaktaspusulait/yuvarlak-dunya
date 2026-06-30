# Yuvarlak Dunya - Pompom Hills World Bible v2.0

| Alan | Kilit Standart |
| --- | --- |
| Format | 3D animasyon serisi |
| Hedef yas | 3-4 yas |
| Bolum | 7 dakika x 26 bolum |
| Olcu sistemi | Kiko = 100 birim |
| Ana duygu | Guvenli kesif, kucuk duygu, hizli onarim |
| Ana sekil | Daire, oval, egri hat |

---

## 1. TEMEL FELSEFE

### 3 Cumle Logline

1. Kiko, Mimi ve Opa, Pompom Hills vadisinde her bolum tek bir kucuk soruyu kesfeder: "Bu ne?", "Nereye yuvarlanir?", "Nasil beklerim?"
2. Dunya fiziksel olarak yuvarlaktir: tepeler, evler, yollar, agaclar, oyuncaklar ve kamera hareketleri daire, oval ve yay formlarindan kurulur.
3. Dunya duygusal olarak da yuvarlaktir: her kucuk sorun sivrilmeden baslar, 15 saniye icinde yumusar, destekle kapanir ve karakterler tekrar guvenli iliskiye doner.

### 5 Ana Tema

| Tema | 3-4 Yas Karsiligi | Yuvarlaklik Baglantisi |
| --- | --- | --- |
| Merak | "Bakmak, sormak, dokunmadan once anlamak" | Kamera merak aninda karakter etrafinda 12-18 derece yay hareketi yapar. |
| Duygu Adlandirma | "Mutlu, uzgun, sasirmis, uykulu" | Duygular keskin patlama degil; yuz formlari daireden ovale gecerek okunur. |
| Bekleme | "Sira bana gelecek" | Bekleme sahneleri dairesel oyun sirasi, halka yol veya yuvarlak taslarla kurulur. |
| Yardim Isteme | "Ben yapamiyorum, yardim alabilirim" | Cozum fiziksel yakinlasma ile yuvarlanir: yan yana oturma, el tutma, sarilma. |
| Dunyanin Yuvarlakligi | "Top, elma, dunya, tepe yuvarlanabilir" | Fizik dersi degil; yuvarlanma, donme, halka ve kure ile sezgisel kavram verilir. |

---

## 2. FIZIK KURALLARI

| Kural | 3D Teknik Karsiligi | Ornek |
| --- | --- | --- |
| Yercekimi gercek dunyadan %30 daha nazik | Gravity scale 0.70; karakter dususlerinde maksimum dikey hiz 90 birim/sn | Kiko 12 birimlik tepeden inerken ziplama degil, 18 frame ease-out ile seker. |
| Yuvarlanma hiz limiti | Top/prop rolling max 120 birim/sn; karakter rolling max 75 birim/sn | Elma tepeden iner, kamera takip eder, elma kadrajdan firlamaz. |
| Sert temas yok | Collision restitution 0.18-0.28; contact squash 4-8%; impact sound max -18 LUFS | Mimi topa carparsa "boop" sesi gelir, geri savrulmaz. |
| Isik sert golge uretmez | Key light size min 5 m; shadow softness 0.65-0.85; contact shadow opacity max 25% | Kiko'nun yuzunde burun golgesi olusmaz. |
| Gece siyah degildir | World color min value #3F51B5; exposure -0.6 stop; fill light 35% | Uyku sahnesinde karakterlerin gozleri ve elleri net okunur. |
| Ses yuvarlak ve alttadir | Foley attack 20-40 ms; high shelf -2 dB at 8 kHz; no sharp transient | Tas ustune basinca "tok" degil, "boop" duyulur. |
| Olcek Kiko'ya baglidir | Kiko = 100 birim; set kapilari 140 birim; kamera goz seviyesi 55-95 birim | Kiko kapidan gecince 20 birim ust bosluk kalir. |
| Kamera cocuk hizinda hareket eder | Pan max 18 derece/sn; dolly max 35 birim/sn; no handheld noise | Yeni mekan acilisinda 3 sn yavas push-in. |
| Egim guvenli kalir | Yuru-nebilir zemin max 12 derece; oyun tepesi max 18 derece; dekor tepesi max 28 derece | Rolling hill 18 dereceyi gecmez. |
| Hava olaylari tehditkar olmaz | Rain particle speed max 35 birim/sn; snow max 15 birim/sn; lightning yok | Yagmur damlalari yuvarlak boncuk gibi duser. |

---

## 3. COGRAFYA

| Mekan | Amac | Boyut [Kiko=100] | Renk HEX | Ozel Asset | Yasak Detay |
| --- | --- | --- | --- | --- | --- |
| Merkez Ponpon Meydani | Uclusunun bulusma, cozum ve kapanis alani | Cap 420 birim; Big Pompom Tree 520 birim yukseklik; oturma halkasi cap 180 | Zemin #C8E6C9, taslar #E0E0E0, agac #A5D6A7 | Big Pompom Tree, 12 yuvarlak oturma tasi, halka yol | Koseli bank, tabelali sokak, kalabalik pazar, sert kaldirim |
| Kiko'nun Kure Evi | Merak baslatan guvenli ev noktasi | Ev yukseklik 180; kapı 140; oda cap 260 | Dis #F8BBD0, trim #FFFFFF, cati #FFCC80 | Yuvarlak pencere, coral kapı, 3 oyuncak rafı | Merdiven boslugu, cam keskinligi, gercekci tugla, karanlik oda |
| Mimi'nin Mavi Oyuk Evi | Duygu destek, sakinlesme, saklanmadan dinlenme | Giris cap 110; ic oda cap 220; tavan 150 | Giris #90CAF9, ic #BBDEFB, minder #FFF59D | Kulak battaniyesi, yuvarlak minder, mini havuc bahcesi | Derin tunel, karanlik magara, dar gecit, gercekci toprak dokusu |
| Opa'nin Alcak Hikaye Dali | Rehberlik, aciklama, rituel cumle | Dal yuksekligi 85; Opa toplam 120; goz cizgisi 82-92 | Dal #A1887F, yaprak #A5D6A7, fener #FFD54F | Alcak perch, hikaye taslari, ay seklinde minder | Yuksek ucum riski, sivri dal, korkutucu orman, metal kafes |
| Yuvarlanma Tepesi | Fiziksel yuvarlaklik, hareket ve sebep-sonuc | Tepe yuksekligi 80; genislik 360; egim 12-18 derece | Cim #C8E6C9, cicek #F8BBD0, yol #FFF59D | Rolling apple, soft globe, halka oyuncak, durma cicek patch'i | Ucurum, hizli dusus, toz bulutu, sert kaya, carpma efekti |

---

## 4. RENK & MATERYAL

### Ana Renkler

| Renk | HEX | Kullanim | RGB | Not |
| --- | --- | --- | --- | --- |
| Kiko Coral | #F8BBD0 | Kiko kiyafet, ev aksani | 248, 187, 208 | Frame basina max %18 alan |
| Mimi Blue | #90CAF9 | Mimi tuy, oyuk kapisi | 144, 202, 249 | Lavender'a kaymaz; hue 205-210 derece |
| Opa Green | #A5D6A7 | Opa tuy, ponpon agac | 165, 214, 167 | Doygunluk max %35 |
| Grass Mint | #C8E6C9 | Zemin, tepe, guvenli alan | 200, 230, 201 | Genis arka plan ana rengi |
| Sun Cream | #FFF9C4 | Gunes, sicak highlight | 255, 249, 196 | Patlama yok; value clamp 0.92 |

### Destek Renkler

| Renk | HEX | Kullanim | Sinir |
| --- | --- | --- | --- |
| Night Blue | #5C6BC0 | Gece gokyuzu | Siyah yerine kullanilir; min luminance %24 |
| Warm Brown | #8D6E63 | Kiko sac, ahsap | Grain texture yok; solid color + broad gradient |
| Star Gold | #FFD54F | Opa gozluk, yildiz, vurgu | Metalik shader yok; metallic 0.0-0.1 |

### Shader Kurallari

| Malzeme | Base Roughness | Specular/IOR | SSS | Normal/Bump | Yasak |
| --- | ---: | --- | --- | --- | --- |
| Kiko ten | 0.72-0.82 | IOR 1.36; specular 0.25 | SSS weight 0.18; radius 2.0 cm | Bump yok; normal amplitude max 0.01 | Pore, damar, gercekci cilt |
| Mimi tuy yuzeyi | 0.80-0.92 | IOR 1.34; specular 0.18 | SSS weight 0.10; radius 1.2 cm | Fur strand yok; velvet normal max 0.015 | Hair particles, gercekci fur |
| Opa tuy/kumas | 0.78-0.88 | IOR 1.35; specular 0.20 | SSS weight 0.08; radius 1.0 cm | Feather line sadece broad color zones | Tek tek tuy, sert gaga |
| Plastik oyuncak prop | 0.58-0.72 | IOR 1.46; specular 0.35 | SSS yok | Bevel normal 0.02 | Parlak sert plastik, keskin highlight |
| Cim/tepe zemini | 0.86-0.95 | IOR 1.33; specular 0.12 | SSS yok | Noise scale min 80 birim; amplitude max 0.015 | Gercekci cim telleri |
| Goz cami/gozluk | 0.35-0.50 | IOR 1.45; specular 0.30 | SSS yok | Bump yok | Keskin parilti, gercek yansima |

---

## 5. HIKAYE KURALLARI

1. Her bolum tek ana kavram tasir: bir duygu, bir nesne, bir sosyal beceri veya bir fiziksel yuvarlaklik kesfi.
2. Catisma maksimum 15 saniye surer; cozum en gec 2 sahne icinde baslar.
3. Duygu yukselisi 3-4 yas seviyesindedir: korku yerine "sasirdim", kayip yerine "bulamiyorum", kizginlik yerine "istemiyorum".
4. Cozum bedensel guvenle biter: yan yana oturma, el tutma, sarilma, Opa'nin alcak sesli tekrar cumlesi.
5. Hicbir karakter bilerek zarar vermez, kandirmaz, alay etmez, dislamaz veya cezalandirilmaz.
6. Her 7 dakikalik bolumde 3 tekrar cumlesi vardir; her cumle 3-6 kelimeyi gecmez.
7. Final sahnesi dairesel kapanir: ayni mekan, ayni nesne veya ayni duygu daha sakin halde tekrar gorulur.

---

## 6. NEGATIF PROMPT

sharp edges, angular shapes, realistic skin pores, realistic fur strands, horror lighting, black night sky, hard cast shadows, high contrast rim light, neon colours, dirty grunge texture, metallic glare, glass shards, weapons, vehicles, city streets, stairs without rounded rails, cliffs, deep tunnels, lightning storms, fast crash motion, crying meltdown, yelling faces, angry eyebrows, villain pose, punishment scene, sarcasm, crowd density, tiny unreadable props, text labels in scene, watermark, photorealism, adult proportions, visible fingers, sharp beak, pointed teeth, realistic animal anatomy, handheld shaky camera, fisheye distortion, Dutch angle, motion blur over 20%, cluttered background, unsafe height, dark forest, isolated lonely child

---

## DO/DONT GORSEL KONTROL LISTESI

### DO - Dogru 10 Madde

| # | Kontrol |
| --- | --- |
| 1 | Kiko toplam 100 birim; tum set olculeri buna gore kurulmus. |
| 2 | Mimi 80 birim; Kiko'nun yaninda destekleyici ve daha kucuk okunuyor. |
| 3 | Opa 120 birim ama goz cizgisi 82-92 birimde; alttan rehberlik ediyor. |
| 4 | Gecede siyah yok; Night Blue #5C6BC0 veya daha acik kullaniliyor. |
| 5 | Golge opacity %25'i gecmiyor; yuzde sert golge yok. |
| 6 | Tum ana formlar daire, oval veya egri hat uzerinden okunuyor. |
| 7 | Prop carpismalari 4-8% squash ile yumusuyor. |
| 8 | Kamera hareketi 35 birim/sn veya 18 derece/sn limitinde. |
| 9 | Her sahnede 1 ana duygu okunuyor; ikinci duygu destekleyici. |
| 10 | Cozum fiziksel yakinlik veya sakin tekrar cumlesiyle bitiyor. |

### DONT - Yanlis 10 Madde

| # | Kontrol |
| --- | --- |
| 1 | Kiko'nun boyunu sahneden sahneye degistirme. |
| 2 | Mimi'yi lavender, gri veya beyaz tavsan yapma. |
| 3 | Opa'yi yuksekten bakan otorite gibi sahneleme. |
| 4 | Siyah arka plan, korkutucu gece veya uzun golge kullanma. |
| 5 | Parmak, tirnak, tuy teli, cilt gozenegi, kumas dokusu detaylandirma. |
| 6 | Hizi komedi carpmasi veya slapstick dusus olarak kullanma. |
| 7 | Catisma suresini 15 saniyeyi gecirme. |
| 8 | Kamera sallama, Dutch angle veya fisheye ile tehlike hissi verme. |
| 9 | Sahnede okunmayan kucuk prop kalabaligi yaratma. |
| 10 | Duyguyu ceza, utandirma veya "aglama" ile kapatma. |
