# Scene Template — PomPom Hills

---

## Kullanım

Bu şablonu kullanarak yeni sahne dosyası oluşturun.

---

## Template

```markdown
# Scene [NUMARA] — [KARAKTER] [AÇIKLAMA] v3.0

## Production Lock

| Alan | Değer |
| --- | --- |
| Karakter | [Karakter adı] |
| Mekan | [Mekan adı] |
| Ölçek | Kiko=100, Mimi=80, Opa=120 |
| Hava | [Gündüz/Gece/Gün batımı] |
| En-boy | 16:9 |
| Süre | 15 saniye |

## Beat

- 0-5 sn: [Açıklama]
- 5-10 sn: [Açıklama]
- 10-15 sn: [Açıklama]

## Dialogue

```
[Karakter]: [Replik]
```

## Visual Prompt

```text
[OPENART DIRECTOR FORMAT]

Create a cinematic 16:9 shot inside the EXISTING [Mekan Adı] of Pompom Hills.

IMPORTANT: The supplied [Mekan Adı] world reference is ABSOLUTELY LOCKED.
Treat it as an already-built location.
DO NOT redesign it. DO NOT regenerate it. DO NOT reinterpret it. DO NOT restyle it. DO NOT replace any objects.

Preserve EXACTLY:
- [Mekana özgü öğeler]

The environment MUST remain visually identical to the supplied [Mekan Adı] reference.
Only add [Karakter Adı] into the existing world.

----------------------------------------
CHARACTER
Use the supplied [Karakter Adı] reference sheet exactly.
Never redesign [Karakter Adı].
Keep:
- [Karakter özellikleri]
No costume changes. No hairstyle changes. No facial redesign.

----------------------------------------
SCALE
[Karakter Adı] is a SMALL preschool child.
He/She occupies ONLY about [X]% of the entire frame.
He/She is NOT the visual focus.
The environment is the hero.
[Mekan nesneleri] must appear life-sized relative to [Karakter Adı].
No oversized child.

----------------------------------------
ACTION
[Karakter aksiyonu]

----------------------------------------
CAMERA
[Kamera ayarları]

----------------------------------------
LIGHTING
[Işık ayarları]

----------------------------------------
STYLE
[Stil tanımı]

----------------------------------------
NEGATIVE
Reject immediately if any of these happen:

- [Karakter] larger than a real preschool child
- [Mekan öğeleri] change color/shape/position
- Environment regenerated
- New environment created
- Different landscape
- Different world layout
- Extra buildings
- Random text
- Wrong proportions
- [Sahneye özgü reddetme kuralları]

Do not display dialogue as on-screen text. No speech bubbles. No captions. No text.
```

## Animation Notes

- [Karakter]'ın hareketleri yumuşak, doğal ve sakin.
- [Sahneye özgü animasyon notları]
- Kamerada hafifçe yavaş hareket (slow‑in / slow‑out).
- Gölgeler yumuşak, kontrast düşük.

## Continuity

- Önceki sahne: [Önceki sahne referansı]
- Continuity frame: [Kare referansı]
- Devam kuralları: `CONTINUITY_RULES.md`

## QA Checklist

Reference: `16_VIDEO_QA_SPEC.md`

- [ ] Character integrity verified
- [ ] Character consistency verified
- [ ] Object persistence verified
- [ ] No rendering artefacts
- [ ] Camera consistency verified
- [ ] Lighting consistency verified
- [ ] Canonical rules followed
```

---

## Kurallar

- Bu template her yeni sahne dosyasında kullanılmalıdır.
- `[]` ile belirtilen yerler sahneye göre değiştirilir.
- Her sahne 15 saniye (4 shot × 15 sn = 60 sn toplam bölüm).
- Maksimum 3 karakter.
- Tek mekan tercih edilir.
- Tek duygusal hedef.

---

*Bu belge tüm yeni sahneler için standart şablondur.*
