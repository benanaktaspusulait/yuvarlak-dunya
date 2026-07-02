# PROMPT RULES — PomPom Hills

---

## Temel Kural

Production dosyaları insanlar için yazılır.

Visual Prompt'lar AI için yazılır.

Birbirine karıştırılmaz.

---

## Visual Prompt Kuralları

Visual Prompt yalnızca **görünen hareketleri** tanımlar.

Diyalog tanımlamaz.

Konusma baloncuğu oluşturmaz.

Yazı oluşturmaz.

---

## Yasak Olanlar

```
✗ @image1, @image2 gibi platform-specific tag'ler
✗ "speech bubble"
✗ "caption"
✗ "subtitle"
✗ "on-screen text"
✗ Dialogue satırları
```

---

## Kullanılacak Ifadeler

```
✓ "Continue naturally from the provided reference image."
✓ "final frame from the previous shot"
✓ "continuity frame from the previous shot"
✓ "Maintain the existing composition"
```

---

## Negative Prompt

Negative prompt mümkün olduğunca ayrı tutulur.

Her shot dosyasının sonunda bulunur.

Ortak negative prompt `NEGATIVE_PROMPTS.md`'de tutulur.

---

## Prompt Yapısı

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

## Örnek

```text
Continue naturally from the provided reference image.

Maintain the existing composition, lighting, characters and environment.

[Action description here]

No new objects.
No new characters.
No environment redesign.
No text.
No captions.
No speech bubbles.
```
