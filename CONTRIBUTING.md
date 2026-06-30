# Contributing v2.1

Bu repo Pompom Hills / Yuvarlak Dunya prodüksiyon dosyasıdır. Katkılar; 3-4 yaş pedagojisi, görsel güvenlik ve üretim tutarlılığına göre değerlendirilir.

## Prompt Ekleme Kuralları

1. Prompt metni İngilizce yazılır.
2. Açıklama, kullanım notu ve onay süreci Türkçe kalabilir.
3. Her prompt `{style}`, `{camera}`, `{lighting}` değişkenlerini içermek zorundadır.
4. Her prompt karakter kilitlerini korur:
   - Kiko = 100 birim, coral shirt #F8BBD0, white shorts #FFFFFF.
   - Mimi = 80 birim, soft blue #90CAF9, yellow t-shirt #FFF59D.
   - Opa = 120 birim, low-staged, warm green #A5D6A7, gold glasses #FFD54F, brown shawl #A1887F.
5. Her prompt `NEGATIVE_PROMPTS.md` ile birlikte kullanılacak şekilde yazılır.
6. Görselde yazı sadece moodboard, poster veya palette card gibi özellikle belirtilen assetlerde kullanılabilir.

## Görsel Onay Süreci

| Aşama | Kontrol | Onay Kriteri |
| --- | --- | --- |
| 1. Prompt QA | Değişkenler var mı? | `{style}`, `{camera}`, `{lighting}` eksiksiz |
| 2. Pedagoji QA | 3-4 yaş için güvenli mi? | Korku, şiddet, utandırma, bağırma yok |
| 3. Tasarım QA | Form dili doğru mu? | Yuvarlak, pastel, oyuncak gibi |
| 4. Karakter QA | Ölçek ve kıyafet doğru mu? | Kiko/Mimi/Opa kilitleri bozulmamış |
| 5. Metadata QA | Tekrar üretilebilir mi? | Prompt, model, seed, negative prompt kayıtlı |

## Naming Convention

Dosya adları küçük harf, tire ayracı ve sürüm bilgisiyle yazılır.

```text
examples/kiko-front-v2.1.png
examples/kiko-front-v2.1.txt
examples/trio-scale-v2.1.png
examples/trio-scale-v2.1.txt
```

Prompt dosyaları:

```text
ai-prompts/<CATEGORY>_PROMPTS.md
```

Karakter dosyaları:

```text
characters/pompom-hills/01-kiko.md
characters/pompom-hills/02-mimi.md
characters/pompom-hills/03-opa.md
```

## Pull Request Checklist

- [ ] Yeni veya değişen promptlarda `{style}`, `{camera}`, `{lighting}` var.
- [ ] `NEGATIVE_PROMPTS.md` ile çelişen ifade yok.
- [ ] README dosya listesi güncel.
- [ ] Örnek görsel eklendiyse `.txt` metadata dosyası yanında.
- [ ] 3-4 yaş için korkutucu, hızlı, sert veya karmaşık sahne yok.
