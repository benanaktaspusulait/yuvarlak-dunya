# Examples

Bu klasör prodüksiyon referansı değildir; repo içinde **placeholder preview ve metadata
standardını** gösterir. Final görseller, aynı isimlendirme ve `.txt` metadata formatı
korunarak onaylı AI çıktılarıyla değiştirilmelidir.

## Naming Convention

```text
examples/kiko-front-v2.1.png
examples/kiko-front-v2.1.txt
examples/trio-scale-v2.1.png
examples/trio-scale-v2.1.txt
```

- `.png` : örnek/placeholder görsel
- `.txt` : o görselin metadata dosyası (aynı taban ad)

## Metadata Standardı (`.txt`)

Her `.png` yanında birebir aynı adlı bir `.txt` bulunmalıdır:

```text
prompt: <kullanılan tam positive prompt>
negative_prompt: <NEGATIVE_PROMPTS.md içinden ilgili satır>
model: <ör. SDXL 1.0 / Midjourney v6 / Flux.1>
seed: <sayı>
variables:
  style: <{style} değeri>
  camera: <{camera} değeri>
  lighting: <{lighting} değeri>
approved: <true|false>
approval_date: <YYYY-MM-DD>
notes: <opsiyonel>
```

## Onay Kapısı

Bir görsel ancak `README.md` > "Visual Approval Gate" bölümündeki üç şartı geçerse
ana referans olabilir (doğru ölçek, görsel güvenlik, kayıtlı metadata).
