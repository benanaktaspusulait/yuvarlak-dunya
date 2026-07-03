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

## Voice Continuity

For Shot 01, match the approved character Voice ID or voice reference.

For Shot 02+, match the previous speaking shot.

The speaking voice MUST remain identical to the previous shot.

Maintain:

- same voice identity
- same pitch
- same timbre
- same speaking speed
- same emotional warmth
- same preschool narration style

Do not generate a different narrator or alternate voice.

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
COLOUR CONTINUITY
Match the colour grading of the previous shot.
Maintain identical white balance, warmth, exposure, saturation, pastel palette and contrast.
Avoid any colour shift.
No blue tint. No green tint. No orange shift. No HDR look. No cinematic LUT.
The entire episode must appear colour graded as one continuous film.

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
- Voice continuity: same Voice ID or approved voice reference for each speaking character
- Colour continuity: match previous shot white balance, exposure, saturation and contrast

## QA Checklist

Reference: `16_VIDEO_QA_SPEC.md`

- [ ] Character integrity verified
- [ ] Character consistency verified
- [ ] Voice identity verified
- [ ] Object persistence verified
- [ ] No rendering artefacts
- [ ] Camera consistency verified
- [ ] Lighting consistency verified
- [ ] Colour identity verified
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
