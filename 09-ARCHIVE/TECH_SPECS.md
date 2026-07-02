# Pompom Hills - 3D Technical Specifications v2.1

## 1. Production Lock

Bu dosya, **Pompom Hills** 3D animasyon serisinin üretim standardıdır. Bu dosya yoksa modelci, rigger, lookdev artist, animator, render artist ve bütçe çıkaran stüdyo aynı kalite seviyesine fiyat veremez.

| Karar | Kilit Değer |
| --- | --- |
| Seri adı | Pompom Hills |
| Format | 3D animasyon serisi |
| Hedef yaş | 3-4 |
| Bölüm süresi | 7 dakika |
| Sezon 1 | 26 bölüm |
| Görsel stil | Soft 3D cartoon animation, rounded shapes, pastel colours, warm daylight, gentle shadows, toy-like appearance |
| Üretim yaklaşımı | AI destekli konsept + kontrollü 3D modelleme + geleneksel rig/animasyon/lookdev |
| Ana karakterler | Kiko, Mimi, Opa |
| Teknik öncelik | Tutarlılık, tekrar kullanılabilir asset, düşük revizyon maliyeti |

## 2. Master Deliverable Specs

| Alan | Standart |
| --- | --- |
| Master çözünürlük | 1920x1080, 16:9 |
| Çalışma çözünürlüğü | 1920x1080, 16:9 |
| Pitch frame opsiyonu | 3840x2160 still frame |
| FPS | 24 fps |
| Frame count / 7 dk | 10,080 frame |
| Ses miks hedefi | Stereo, 48 kHz, 24-bit WAV |
| Video teslim | ProRes 422 HQ veya H.264 review export |
| Still teslim | PNG, 16-bit tercih edilir; JPG sadece review için |
| Renk yönetimi | ACEScg veya eşdeğer linear workflow |
| Güvenli alan | 90% action safe, 80% title safe |

## 3. DCC, Render, Versioning

| Alan | Varsayılan |
| --- | --- |
| Ana DCC | Blender 4.x |
| Alternatif stüdyo DCC | Maya kabul edilir, ama teslim formatları değişmez |
| Previs render | Blender Eevee / viewport render |
| Final render | Blender Cycles veya stüdyo onaylı eşdeğer path-traced render |
| Realtime opsiyonu | Unreal sadece ayrı pipeline kararıyla açılır |
| Dosya versiyonlama | `assetName_task_v###.blend` veya DCC eşdeğeri |
| Review export | MP4 H.264, burnt-in shot code ve frame number |
| Kaynak dosya teslimi | `.blend`, `.fbx`, `.usd/usda`, `.abc` gerektiğinde |

**Kilit kural:** Render engine pilot lookdev testinden önce değiştirilemez. Engine değişirse shader, ışık, render time ve texture davranışı yeniden fiyatlanır.

## 4. World Scale And Units

3D üretimde dünya ölçüsüz olamaz. Bütün assetler aşağıdaki ölçeğe göre üretilir.

| Ölçü | Değer |
| --- | --- |
| Unit system | Metric |
| 1 Blender unit | 1 metre |
| Kiko boy | 1.00 m |
| Mimi boy | 0.80 m gövde (80 birim); kulaklarla maksimum 0.92 m |
| Opa boy | 1.20 m (120 birim), en uzun; alçak sahnelenir, göz çizgisi 0.82-0.92 m; kanat açıklığı maksimum 1.20 m |
| Standart kapı yüksekliği | 1.35 m |
| Standart ev içi tavan | 2.20 m |
| Round stepping stone çapı | 0.35 m |
| Big Pompom Tree yüksekliği | 5.00-6.00 m |
| Kamera göz seviyesi | 0.70-1.10 m arası |

**Kilit kural:** Kiko en uzun karakterdir. Mimi Kiko'dan biraz kısadır. Opa orta boy, kompakt ve yuvarlaktır. Bu oran bozulursa trio staging ve merchandising ölçeği çöker.

## 5. Character Model Budgets

Bu seri mid-poly, stylized ve rig-friendly üretilir. Micro-detail yasaktır; şekil dili büyük, yumuşak ve okunabilir kalır.

| Asset | Triangle Budget | Texture Set | Not |
| --- | ---: | --- | --- |
| Kiko hero model | 20k-35k tris | 2K body + 1K face/hair if needed | Parmak yok, yuvarlak el formu |
| Mimi hero model | 18k-30k tris | 2K body + 1K ears/t-shirt if needed | Fur geometry yok; soft blue surface |
| Opa hero model | 22k-38k tris | 2K body + 1K glasses/shawl if needed | Feather detail modelleme değil, shader/shape |
| Secondary character | 10k-20k tris | 1K-2K | S1'de sınırlı kullanılacak |
| Background character | 5k-10k tris | 1K | Yakın plan yasak |
| Hero prop | 1k-5k tris | 1K | Lost toy, snack basket, flower pot |
| Background prop | 300-1.5k tris | 512-1K | Tekrar kullanılabilir |
| Hero environment set | 80k-180k tris | 2K-4K atlas | Central square, house interiors |
| Background environment | 20k-80k tris | 1K-2K atlas | Distant hills, sky cards |

**Kilit kural:** "OpenArt gibi daha detaylı dursun" isteği polycount artışıyla çözülmez. Stil shader, form, ışık ve renk ile korunur.

## 6. Character-Specific Model Requirements

### Kiko

| Alan | Standart |
| --- | --- |
| Tip | 3-4 yaş hissinde human girl, 3-4 hedef kitleye uygun |
| Saç | Warm brown #8D6E63, iki küçük pigtail, solid stylized hair mass |
| Göz | Brown #795548, büyük yuvarlak göz, iki beyaz highlight |
| Kıyafet | Coral pink shirt #F8BBD0, white shorts #FFFFFF, coral socks/shoes #F8BBD0 |
| Topoloji | Deformasyon halkaları omuz, kalça, ağız, göz çevresi |
| Yasak | Tek tek saç teli, gerçekçi cilt pore, parmak detayları, aksesuar kalabalığı |

### Mimi

| Alan | Standart |
| --- | --- |
| Tip | Cute baby rabbit, Kiko'nun en yakın arkadaşı |
| Fur rengi | Soft blue #90CAF9 |
| Belly | White #FFFFFF |
| Göz | Green #66BB6A |
| Burun | Pink #F48FB1 |
| T-shirt | Soft yellow #FFF59D |
| Topoloji | Kulak köklerinde yumuşak deformasyon, hop cycle için pelvis/leg loops |
| Yasak | Lavender versiyon, detailed fur, gerçekçi tüy simülasyonu, pantolon/ayakkabı |

### Opa

| Alan | Standart |
| --- | --- |
| Tip | Wise owl guide, medium-sized round owl |
| Feather rengi | Warm green #A5D6A7 |
| Belly | Light green #C8E6C9 |
| Göz | Brown #795548 |
| Gözlük | Round golden glasses #FFD54F |
| Beak/feet | Orange #FF7043 |
| Shawl | Soft brown #A1887F |
| Topoloji | Kanat açma, gözlük sabitleme, shawl overlap için ayrı mesh |
| Yasak | Keskin gaga, gerçekçi tüy, metalik gözlük parlaması, tehditkar silüet |

## 7. Topology Rules

| Kural | Uygulama |
| --- | --- |
| Silhouette first | Asset önce uzaktan okunmalı, detay sonra gelmeli |
| Roundness | Bütün köşeler bevel veya smooth form ile yumuşatılır |
| Deformation loops | Ağız, göz, omuz, kalça, kulak, kanat ve diz/dirsek hissi olan bölgelerde loop gerekir |
| No razor edges | Hiçbir assette keskin uç, ince sivri parça, tehlikeli form yok |
| Large forms | Küçük noise, pore, fabric weave, hair strand, feather strand yok |
| Clean normals | Smooth normals kontrollü; pinching, faceting ve broken shading kabul edilmez |
| Mirror-safe design | Sol/sağ simetri base modelde korunur; asymmetry sadece approved lookdev ile |

## 8. Materials And Shading

Pompom Hills'in lookdev'i gerçekçi malzeme taklidi değil, soft toy ve matte pastel yüzey standardıdır.

| Malzeme Alanı | Standart |
| --- | --- |
| Base shader | Soft matte, high roughness, low specular |
| Skin | Stylized smooth surface, no pores, no realistic subsurface detail |
| Hair | Solid stylized mass, broad highlights only |
| Mimi fur | Smooth plush-like shader, no hair particles, no strand fur |
| Opa feathers | Broad feather-shaped colour zones, no individual feather detail |
| Fabric | Matte, soft, no woven texture close-up |
| Glasses | Gold colour #FFD54F, non-metallic or very low metallic, no sharp glare |
| Environment | Matte toy set surface, soft bevels, low-frequency colour variation |

**Texture map minimum:**
- Base Color
- Roughness
- Normal only for very soft broad forms

**Texture map yasakları:**
- Pore map
- Photographic fabric texture
- Real fur cards
- Harsh grunge
- High-frequency dirt
- Horror-style ambient occlusion

## 9. Texture Resolution Rules

| Asset Tipi | Texture Resolution |
| --- | --- |
| Hero character body | 2048x2048 |
| Hero character face/hair accessory | 1024x1024 |
| Secondary character | 1024x1024 veya 2048x2048 |
| Hero prop | 1024x1024 |
| Background prop | 512x512 veya 1024x1024 |
| Hero environment set | 2048x2048 atlas veya 4096x4096 atlas |
| Distant background | 512x512 veya procedural colour |

**Kilit kural:** Texture çözünürlüğü "daha kaliteli" görünmek için rastgele yükseltilmez. Yakın plan ihtiyacı yoksa 4K texture israftır.

## 10. Rig Requirements Summary

Detaylı rig standardı `RIG_REQUIREMENTS.md` dosyasında açılacaktır. Bu dosya çıkana kadar minimum rig seviyesi aşağıdadır.

| Sistem | Minimum |
| --- | --- |
| Body rig | FK/IK arms and legs, simple squash-stretch controls |
| Facial rig | Eyes, brows, mouth corners, smile/frown, blink, cheek puff |
| Kiko | Pigtail bounce controls, simple head/body squash |
| Mimi | Ear flop controls, hop squash, tail secondary motion |
| Opa | Wing controls, perched/flying switch, glasses locked to face |
| Prop interaction | Hand/paw/wing attachment points |
| Export | Animator-friendly control rig + baked export option |

**Kilit kural:** Bu seri preschool/toddler-safe hareket istediği için rig karmaşıklığı animasyonu yavaşlatmamalı. Aşırı facial rig, bütçeyi yer ve ekranda görünmez.

## 11. Animation Specs

| Alan | Standart |
| --- | --- |
| Hareket dili | Gentle, rounded, slow, readable |
| Timing | Büyük hareketler yavaş ease-in/ease-out |
| Squash-stretch | Var, ama çok abartılı değil |
| Camera motion | Slow pan, slow push-in, locked-off shots |
| Yasak | Fast cuts, shaky cam, aggressive anticipation, hard impacts |
| Walk cycle | Kiko gentle bounce, Mimi hop-hop, Opa short steps/perch/fly |
| Expression readability | Tek frame'de anlaşılır büyük yüz ifadeleri |
| Motion blur | Çok hafif veya kapalı; toddler clarity öncelikli |

## 12. Environment And Set Rules

| Set | Minimum Asset List |
| --- | --- |
| Central village square | Big Pompom Tree, round plaza, stepping stones, 3-5 background houses, flowers |
| Kiko house exterior | Coral house, round door, circular windows, small garden |
| Kiko house interior | Rounded bed/chair/table, circular rug, window, soft shelves |
| Mimi burrow exterior | Round burrow door, soft blue/yellow accents, grass mound, stepping stones |
| Mimi burrow interior | Rounded underground room, cushions, blanket, simple shelves |
| Opa tree/perch | Pompom tree, rounded perch, story corner |
| Hills | Flower Hill, Cloud Hill, Stone Hill, Tree Hill |
| Weather | Day, sunset, night, rainy, snowy variants |

**Set reuse rule:** Season 1 bütçesi için her bölüm sıfır set açamaz. İlk 26 bölümde ana hikayeler 6-8 modular set içinde dönmelidir.

## 13. Lighting Specs

| Senaryo | Standart |
| --- | --- |
| Daylight | Warm soft daylight, broad area light feeling |
| Interior | Warm gentle lamp + soft fill |
| Sunset | Soft orange/pink, no dramatic contrast |
| Night | Gentle blue, never black, all characters readable |
| Rain | Diffused soft light, no storm contrast |
| Snow | Cool gentle light, still pastel and safe |

**Shadow rule:** Shadow sadece formu yere oturtur. Korku, drama veya sert kontrast yaratmaz.

## 14. Camera And Layout Specs

| Alan | Standart |
| --- | --- |
| Lens dili | 35mm-50mm equivalent, minimal distortion |
| Default camera height | Character eye-level |
| Establishing shot | Slightly above eye-level, never epic/dramatic |
| Close-up | Face readable, background simple |
| Character staging | Maksimum 3 speaking character |
| Composition | One focal point, clean frame, no visual clutter |
| Safe space | Karakter etrafında breathing room |

## 15. File Formats And Folder Standard

Önerilen üretim klasörleri:

```text
assets/
  characters/
    kiko/
      model/
      rig/
      texture/
      lookdev/
    mimi/
    opa/
  environments/
  props/
shots/
  s01e001/
    layout/
    animation/
    lighting/
    render/
exports/
  review/
  final/
references/
  openart/
  model_sheets/
  lookdev/
```

| Deliverable | Format |
| --- | --- |
| Model source | `.blend` primary, `.ma/.mb` only if Maya vendor |
| Interchange | `.fbx`, `.usd/usda`, `.abc` when needed |
| Texture | `.png` or `.exr`; JPG not for final texture |
| Review video | `.mp4` H.264 |
| Final video | ProRes 422 HQ |
| Still frame | `.png` or `.exr` |

## 16. Asset Naming Convention

| Tip | Format |
| --- | --- |
| Character model | `chr_kiko_model_v001.blend` |
| Character rig | `chr_kiko_rig_v001.blend` |
| Character texture | `chr_kiko_body_basecolor_v001.png` |
| Prop | `prp_lostToy_model_v001.blend` |
| Environment | `env_centralSquare_model_v001.blend` |
| Shot layout | `s01e001_sh010_layout_v001.blend` |
| Animation playblast | `s01e001_sh010_anim_v001.mp4` |
| Final render | `s01e001_sh010_lighting_v001.mov` |

**Kilit kural:** Dosya adı yaratıcı alan değildir. İsim standardı bozulursa shot tracking, vendor teslimi ve revizyon takibi bozulur.

## 17. AI Concept To 3D Conversion Rules

OpenArt görselleri konsept referansıdır; final 3D asset değildir. AI görselde görünen her detay modele alınmaz.

| AI Referans Öğesi | 3D Kararı |
| --- | --- |
| Ana silüet | Korunur |
| Renk paleti | Hex kodlarıyla korunur |
| Outfit | Korunur |
| Rastgele süs/detail | Atılır |
| Texture noise | Atılır |
| Işık hissi | Lookdev'e çevrilir |
| Kamera açısı | Model sheet için ortho referansa dönüştürülür |
| Inconsistent geometry | Model supervisor karar verir |

**AI-to-3D gate:**
1. AI reference approved.
2. Front/side/back orthographic sheet produced.
3. Scale check with Kiko/Mimi/Opa lineup.
4. Mid-poly model blockout approved.
5. Lookdev clay render approved.
6. Texture/shader pass approved.
7. Rig deformation test approved.
8. Animation test approved.

## 18. Required Review Gates

| Gate | Çıkmadan Sonraki Aşamaya Geçilmez |
| --- | --- |
| Concept lock | Character/world prompt, colour lock, negative prompt |
| Model sheet lock | Front, side, back, scale, expression references |
| Blockout approval | Scale, silhouette, proportion |
| Model approval | Clean topology, correct forms, no forbidden detail |
| Lookdev approval | Shader, colour, lighting response |
| Rig approval | Deformation, controls, expression readability |
| Animation test | Walk/hop/fly/perch, facial test |
| Shot test | 10-20 second pilot scene with final-ish lighting |
| Render test | Time per frame, noise level, colour consistency |

## 19. Pilot Shot Technical Target

Yatırımcı ve stüdyo fiyatlaması için ilk teknik test tek bir kısa sahne olmalıdır.

| Alan | Hedef |
| --- | --- |
| Süre | 10-20 saniye |
| Karakter | Kiko + Mimi, Opa opsiyonel |
| Set | Central village square veya Big Pompom Tree |
| Aksiyon | Walking + discovery + simple expression change |
| Teknik test | Scale, rig, shader, lighting, render time |
| Çıktı | 1080p MP4 review + 3 still frame + render time report |

**Kilit kural:** Pilot shot olmadan 26x7 dk bütçe konuşulmaz. Kağıt üstündeki fiyat sahada patlar.

## 20. Render Performance Targets

| Alan | Hedef |
| --- | --- |
| Preview render | Realtime veya dakikalar içinde |
| Final frame target | 2-8 dakika/frame tek makine hedefi |
| Heavy frame upper limit | 15 dakika/frame üstü alarm |
| Noise | Preschool clean look; visible grain yok |
| Motion test | Her karakter için playblast before final lighting |
| Render farm need | Pilot shot render time raporundan sonra karar |

## 21. Missing Dependent Documents

Bu dosya tek başına üretimi tamamlamaz. Aşağıdaki dosyalar yazılmadan 3D üretim tam kilitlenmiş sayılmaz.

| Dosya | Neden Gerekli |
| --- | --- |
| `CHARACTER_MODEL_SHEET.md` | Kiko, Mimi, Opa için ortho, scale, expression ve pose standardı |
| `RIG_REQUIREMENTS.md` | Body/facial rig, control set, deformation testleri |
| `SHADING_GUIDE.md` | Soft matte look, material library, render response |
| `ENVIRONMENT_SCALE_GUIDE.md` | Ev, ağaç, path, hill ve interior ölçüleri |
| `SHOT_LIST_PILOT.md` | İlk 7 dakikanın asset/shot/bütçe kırılımı |
| `PIPELINE_DIAGRAM.md` | AI concept -> model -> rig -> layout -> animation -> lighting -> final akışı |
| `PRODUCTION_SCHEDULE.md` | 26 bölüm sezon takvimi ve dependency planı |
| `BUDGET_BREAKDOWN.md` | Asset, rig, shot, render, ses, edit ve contingency bütçesi |

## 22. Non-Negotiables

- Kiko'nun coral pink outfit #F8BBD0 ve warm brown pigtails #8D6E63 tasarımı değişmez.
- Mimi soft blue #90CAF9 kalır; lavender versiyon yoktur.
- Mimi'nin soft yellow t-shirt #FFF59D kıyafeti değişmez.
- Opa warm green #A5D6A7, golden glasses #FFD54F, orange beak #FF7043 ve soft brown shawl #A1887F ile kalır.
- Bütün formlar rounded, soft, toy-like olur.
- Realistic skin, detailed fur, sharp edges, harsh shadows, neon colour ve scary elements yasaktır.
- Her yeni asset bu dosyadaki scale, naming, texture ve review gate standardından geçer.

## 23. Open Decisions Before Vendor Quote

Bu kararlar alınmadan dış stüdyo veya freelancer fiyatı sadece tahmindir.

| Karar | Gerekli Çıktı |
| --- | --- |
| Final render engine | 10-20 saniyelik pilot shot render test |
| Rig complexity | `RIG_REQUIREMENTS.md` + facial expression test |
| Episode asset reuse ratio | Season 1 episode map + set reuse table |
| Voice/language strategy | Dialogue and dubbing plan |
| Delivery platform | TRT Çocuk / Netflix / YouTube teslim standardı |
| Production location | In-house, freelance, vendor, hybrid |
| Final budget tier | `BUDGET_BREAKDOWN.md` |
| Final schedule | `PRODUCTION_SCHEDULE.md` |
