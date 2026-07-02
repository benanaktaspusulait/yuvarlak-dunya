# PROMPT RULES — PomPom Hills

---

## Amaç

Bu dosya AI promptlarının nasıl yazılacağını tanımlar.

---

## 1. Visual Prompt Kuralları

Visual Prompt yalnızca **görünen hareketleri** tanımlar.

Diyalog tanımlamaz.

Konusma baloncuğu oluşturmaz.

Yazı oluşturmaz.

---

## 2. Dialogue Rules

Diyalog yalnızca `Dialogue` bölümünde bulunur.

Visual Prompt'da asla tekrar edilmez.

---

## 3. Negative Prompt Rules

Her shot dosyasının sonunda bulunur.

Ortak negative prompt `NEGATIVE_PROMPTS.md`'de tutulur.

---

## 4. Reference Image Rules

```
✗ @image1, @image2 gibi platform-specific tag'ler
✗ Dosya adları ("3.png")
✓ "provided reference image"
✓ "final frame from the previous shot"
✓ "continuity frame from the previous shot"
```

---

## 5. Anti-Text Instructions

Her Visual Prompt'un sonunda:

```
Do not display dialogue as on-screen text.
No speech bubbles.
No captions.
No text.
```

---

## 6. Prompt Writing Principles

- Kısa ve net olmalı
- Yalnızca görünen şeyleri tanımlamalı
- Platform bağımsız olmalı
- Tekrar içermemeli

---

## 7. Prompt Yapısı

```
[Continuity Reference]
[Environment Lock]
[Character Lock]
[Action Description]
[Camera Direction]
[Lighting]
[Atmosphere]
[Anti-text instructions]
```

---

## 8. Yasak Olanlar

```
✗ @image tag'leri
✗ Dosya adları
✗ Dialogue tanımları
✗ Caption talimatları
✗ Platform-specific referanslar
✗ Gereksiz markdown
```
