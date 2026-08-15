# TTS Voice Replacement Workflow — Pompom Hills

> **Tek yetkili kapsam:** OpenArt'ın ürettiği videolardaki karakter seslerini, onaylanmış
> referans seslerle değiştirme (voice replacement / voice overlay) teknik süreci.
>
> Bu doküman ses üretim parametrelerini, araçları, workflow adımlarını ve QA kurallarını tanımlar.
> İlgili kaynak: `00-CORE/AUDIO_GUIDE.md` (genel ses felsefesi), `00-CORE/EPISODE_AUDIO_WORKFLOW.md`
> (bölüm seviyesi ses iş akışı).

---

## 1. Problem

OpenArt/Seedance video üretimi sırasında "Auto Voice" kapatılsa bile bazı shotlarda:

- Yanlış karakter sesi atanır (Arda satırında Mimi/Kiko sesi gelir)
- Ses kalitesi bozulur, çizirtili veya robotik çıkar
- Konuşma hızı uyumsuz olur

Bu durumda ilgili satır(lar) TTS ile yeniden üretilip videoya overlay yapılır.

---

## 2. Araçlar ve Ortam

### TTS Engine

| Alan | Değer |
|---|---|
| Model | Coqui XTTS-v2 (`tts_models/multilingual/multi-dataset/xtts_v2`) |
| Kütüphane | TTS 0.22.0 |
| Python | 3.11 |
| PyTorch | 2.5.1 |
| Transformers | 4.39.3 |
| GPU | Opsiyonel (CPU yeterli, ~3-4s/satır) |

### Python Venv

```bash
# Mevcut venv konumu
/Users/benanaktas/project/video/yuvarlak-dunya/tts_venv/

# Aktivasyon
source /Users/benanaktas/project/video/yuvarlak-dunya/tts_venv/bin/activate

# Veya doğrudan python çağrısı
/Users/benanaktas/project/video/yuvarlak-dunya/tts_venv/bin/python
```

### Venv Kurulumu (Sıfırdan Gerekirse)

```bash
python3.11 -m venv tts_venv
source tts_venv/bin/activate
pip install torch==2.5.1 --index-url https://download.pytorch.org/whl/cpu
pip install TTS==0.22.0
pip install transformers==4.39.3
```

### Video İşleme

- **ffmpeg** — ses overlay, tempo değiştirme, video birleştirme
- **ffprobe** — ses süresi ve video bilgisi kontrolü

---

## 3. Onaylanmış Ses Referansları

| Karakter | Referans Dosyası | Not |
|---|---|---|
| Arda | `05-AI-PROMPTS/voice/Arda-Approved-voice-reference-10s.wav` | 10 saniyelik temiz referans |
| Luca | `05-AI-PROMPTS/voice/09-luca-approved-reference.wav` | Onaylanmış referans |

> Yeni karakter sesi eklendiğinde bu tabloya eklenmeli.
> Referans dosya ~10 saniye temiz konuşma içermeli, arka plan gürültüsü olmamalı.

---

## 4. TTS Üretim Parametreleri

### Arda İçin Optimize Edilmiş Parametreler

```python
tts.tts_to_file(
    text='[satır metni]',
    speaker_wav='05-AI-PROMPTS/voice/Arda-Approved-voice-reference-10s.wav',
    language='en',
    file_path='[çıktı yolu]',
    temperature=0.15,
    repetition_penalty=6.0,
    top_k=15,
    top_p=0.6,
    speed=0.9,          # Doğal tempo — ayarlanabilir
    length_penalty=1.0
)
```

### Parametre Açıklamaları

| Parametre | Değer | Neden |
|---|---|---|
| `temperature` | 0.15 | Düşük = tutarlı, tekrarlanabilir ses; yüksek = yaratıcı ama kararsız |
| `repetition_penalty` | 6.0 | Tekrarlayan hece/ses sorununu önler |
| `top_k` | 15 | Token seçim havuzunu daraltır → daha tutarlı |
| `top_p` | 0.6 | Düşük nucleus → daha öngörülebilir çıktı |
| `speed` | 0.9 | Genel başlangıç noktası. Satıra göre ayarlanır |
| `length_penalty` | 1.0 | Nötral uzunluk — kısaltma/uzatma baskısı yok |

### Speed Parametresi Rehberi

| Hız | Kullanım |
|---|---|
| 0.9 | Genel doğal başlangıç noktası |
| 1.0 | XTTS'te non-linear davranış gösterebilir — dikkatli kullan |
| 1.15 | Biraz hızlı konuşma — kısa ünlem cümleleri için |
| 1.4 | Enerjik, hızlı — "Got it!" gibi kısa cümleler için |

> **ÖNEMLİ:** XTTS'te speed parametresi her zaman linear çalışmaz. Aynı cümle farklı speed
> değerlerinde beklenmedik süre üretebilir. Sorun olursa ffmpeg `atempo` filtresi ile
> post-processing yap.

### ffmpeg Tempo Ayarlama (Post-Processing)

```bash
# Yavaşlatma (örn. %12 yavaş)
ffmpeg -y -i input.wav -filter:a "atempo=0.88" output.wav

# Hızlandırma (örn. %30 hızlı)
ffmpeg -y -i input.wav -filter:a "atempo=1.3" output.wav
```

> atempo değeri 0.5–2.0 arasında olmalı. Daha fazla değişiklik için zincirleme kullan:
> `atempo=2.0,atempo=1.5` (toplam 3x)

---

## 5. Tam TTS Üretim Script'i (Örnek)

```python
import torch
from TTS.api import TTS

tts = TTS(model_name='tts_models/multilingual/multi-dataset/xtts_v2', gpu=False)

ref = '/Users/benanaktas/project/video/yuvarlak-dunya/05-AI-PROMPTS/voice/Arda-Approved-voice-reference-10s.wav'

tts.tts_to_file(
    text='I can roll it back.',
    speaker_wav=ref,
    language='en',
    file_path='/path/to/output/arda_shot03_roll_it_back_v1.wav',
    temperature=0.15,
    repetition_penalty=6.0,
    top_k=15,
    top_p=0.6,
    speed=0.9,
    length_penalty=1.0
)
```

---

## 6. Video Overlay Workflow

### Adım 1: Hedef Videonun Ses Zamanlamasını Belirle

Script dosyasından satırın başladığı saniyeyi oku (ör. "I can roll it back" → 6.0s).

Gerçek videoda tam olarak nerede konuşma başladığını dinleyerek doğrula.

### Adım 2: Eski Sesi Sil + Yeni Sesi Yerleştir

```bash
ffmpeg -y \
  -i video_input.mp4 \
  -i new_voice.wav \
  -filter_complex "\
[1:a]adelay=START_MS|START_MS[new_voice];\
[0:a]volume=0:enable='between(t,START_SEC,END_SEC)'[orig_ducked];\
[orig_ducked][new_voice]amix=inputs=2:duration=first:dropout_transition=0[aout]" \
  -map 0:v -map "[aout]" -c:v copy -c:a aac -b:a 192k \
  video_output.mp4
```

**Parametreler:**

| Değişken | Açıklama |
|---|---|
| `START_MS` | Yeni sesin başlama noktası (milisaniye) — `adelay` için |
| `START_SEC` | Eski sesin silineceği başlangıç (saniye) — `volume=0` için |
| `END_SEC` | Eski sesin silineceği bitiş (saniye) = START_SEC + wav süresi |

### Adım 3: Birden Fazla Satır Değiştirme

```bash
ffmpeg -y \
  -i video.mp4 \
  -i line1.wav \
  -i line2.wav \
  -i line3.wav \
  -filter_complex "\
[1:a]adelay=T1_MS|T1_MS[voice1];\
[2:a]adelay=T2_MS|T2_MS[voice2];\
[3:a]adelay=T3_MS|T3_MS[voice3];\
[0:a]volume=0:enable='between(t,S1,E1)',volume=0:enable='between(t,S2,E2)',volume=0:enable='between(t,S3,E3)'[orig_ducked];\
[orig_ducked][voice1][voice2][voice3]amix=inputs=4:duration=first:dropout_transition=0[aout]" \
  -map 0:v -map "[aout]" -c:v copy -c:a aac -b:a 192k \
  output.mp4
```

> `-c:v copy` sayesinde video yeniden encode edilmez — hızlı ve kalite kaybı yok.

---

## 7. Zamanlama Ayarı (Offset Fine-Tuning)

OpenArt'ın ürettiği videonun gerçek konuşma zamanlaması, script'teki zamanlamadan
farklı olabilir. Bu normaldir.

### Yaklaşım

1. Script zamanlamasını başlangıç noktası al
2. Kullanıcıya videoyu izlettir
3. Feedback'e göre 0.2–0.5s adımlarla kayır
4. "Erken" = `adelay` değerini azalt, "Geç" = `adelay` değerini artır

### Dikkat

- Eski sesin silinme aralığını (volume=0 between) yeni zamana göre güncelle
- Komşu satırların sesini silmemeye dikkat et (aralığı daralt)
- Özellikle birbirine yakın iki satır varsa, aralarındaki boşluk minimum 0.3s olmalı

---

## 8. QA / Onay Süreci

### Üretim QA

1. **Ses kalitesi** — Çizirtisiz, temiz, doğal mı?
2. **Hız** — Çok hızlı / çok yavaş değil mi?
3. **Karakter uyumu** — Referans sesle aynı kişi gibi mi duyuluyor?
4. **Telaffuz** — Kelimeler net ve doğru mu?

### Overlay QA

1. **Zamanlama** — Dudak hareketi ile ses eşleşiyor mu?
2. **Eski ses** — Tamamen silindi mi, artık duyuluyor mu?
3. **Komşu sesler** — Diğer karakterlerin sesleri bozuldu mu?
4. **Geçiş** — Sesler arası doğal boşluk var mı?

### Red Flags

- Çizirtili çıktı → v2 üret (XTTS her seferinde farklı sonuç verir)
- Robotik ses → temperature'ı 0.2'ye çık veya referans dosyayı kontrol et
- Çok yavaş/hızlı → speed parametresini ayarla veya ffmpeg atempo kullan
- Eski ses kalıntısı → volume=0 aralığını genişlet

---

## 9. Dosya İsimlendirme Kuralı

```
arda_shot{NN}_{kisa_aciklama}_v{VV}.wav
```

Örnekler:
- `arda_shot03_roll_it_back_v4.wav`
- `arda_shot04_ready_kiko_v1.wav`
- `arda_shot08_bye_everyone_v1.wav`

Video çıktısı:
- `shot-{N}_hd_new_voice.mp4`

---

## 10. Bilinen Sınırlamalar ve Çözümler

| Sorun | Çözüm |
|---|---|
| XTTS speed parametresi non-linear | ffmpeg atempo ile post-process |
| Aynı parametrelerle farklı sonuç | Birden fazla deneme üret, en iyisini seç |
| Kısa kelimeler (Yeah!, Got it!) garip çıkıyor | Birkaç versiyon üret, referansı direk kullan yaklaşımı dene |
| Uzun cümleler yarım kalıyor | Cümleyi böl, ayrı ayrı üret, birleştir |
| 24kHz çıktı vs 48kHz video | ffmpeg otomatik resample eder, sorun değil |

---

## 11. Karakter Bazında Onaylanmış Parametre Setleri

### Arda — Kesinleşmiş

```python
temperature=0.15
repetition_penalty=6.0
top_k=15
top_p=0.6
speed=0.9        # Doğal tempo
length_penalty=1.0
```

> Kısa enerjik cümleler için speed=1.15 denenebilir, ancak ffmpeg hızlandırma
> genellikle daha tutarlı sonuç verir.

### Luca — Henüz Test Edilmedi

Referans mevcut: `05-AI-PROMPTS/voice/09-luca-approved-reference.wav`

İlk denemede Arda parametreleri ile başla, sonra ayarla.

### Diğer Karakterler

Henüz TTS referansı yok. Yeni karakter sesi eklendiğinde:
1. ~10s temiz referans kaydet
2. Arda parametreleriyle başla
3. 3-5 deneme üret, kullanıcıya dinlet
4. Onaylanan parametreleri bu dosyaya ekle

---

## 12. Hızlı Referans — Tek Satır Değiştirme

```bash
# 1. TTS üret
/Users/benanaktas/project/video/yuvarlak-dunya/tts_venv/bin/python -c "
from TTS.api import TTS
tts = TTS(model_name='tts_models/multilingual/multi-dataset/xtts_v2', gpu=False)
tts.tts_to_file(
    text='SATIN METNI',
    speaker_wav='05-AI-PROMPTS/voice/Arda-Approved-voice-reference-10s.wav',
    language='en',
    file_path='CIKTI.wav',
    temperature=0.15, repetition_penalty=6.0, top_k=15, top_p=0.6, speed=0.9, length_penalty=1.0
)
"

# 2. Süreyi kontrol et
ffprobe -i CIKTI.wav -show_entries format=duration -v quiet -of csv="p=0"

# 3. Videoya overlay (START_MS ve DURATION_SEC'i ayarla)
ffmpeg -y -i VIDEO.mp4 -i CIKTI.wav \
  -filter_complex "[1:a]adelay=START_MS|START_MS[v];[0:a]volume=0:enable='between(t,START_SEC,END_SEC)'[d];[d][v]amix=inputs=2:duration=first:dropout_transition=0[a]" \
  -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k OUTPUT.mp4
```

---

*Oluşturulma: 15 Ağustos 2026*
*İlgili dosyalar: `00-CORE/AUDIO_GUIDE.md`, `00-CORE/EPISODE_AUDIO_WORKFLOW.md`*
*Bu doküman TTS voice replacement teknik süreci için tek kaynaktır.*
