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
| Mekan Zone (varsa) | [Mekanın sub-zone'u var mı? Örn. Flower Hill — Nature Field Zone / Home Cluster Zone. Zone yoksa "—".] |
| Ölçek | Kiko=100, Mimi=80, Opa=120 |
| Hava | [Gündüz/Gece/Gün batımı] |
| En-boy | 16:9 |
| Süre | 15 saniye |

### Mekan Zone Kuralı

Bazı mekanların birden fazla üretim zone'u vardır (örn. Flower Hill →
Nature Field Zone / Home Cluster Zone, bkz. ilgili world bible §Visual
Richness & World Charm). Bir mekanın zone'u varsa, `Mekan` alanına yalnızca
mekan adını yazmak yeterli değildir — zone'u da belirtin:

```
Mekan: Flower Hill — Home Cluster Zone
```

Zone belirsizse tahmin etmeyin, şu notu ekleyin:

```
TODO: Bu mekan için doğru zone'u üretimden önce seç.
```

Zone belirlendiyse aşağıdaki iki alanı da doldurun:

**Spatial Anchor** — Bu shot'ı sabitleyen tam olarak ne? (örn. "S-curve taş
patika görünür", "aynı yuvarlak evler, aynı taş merdiven, aynı çit görünür")

**Reference Use** — Bu shot için hangi görsel referans kullanılmalı?
(örn. "Hero View'i görsel kalite çapası olarak kullan", "sol taraf shot'u
için left-view referansını kullan", "top-view sadece layout anlayışı için,
kamera çekimi için değil")

## Beat

- 0-5 sn: [Açıklama]
- 5-10 sn: [Açıklama]
- 10-15 sn: [Açıklama]

## Dialogue

```
[Karakter]: [Replik]
```

## Voice Continuity

Follow `00-CORE/SHOT_PRODUCTION_STANDARD.md`.

For Shot 01, match the approved character Voice ID or voice reference.

For Shot 02+, match the previous speaking shot.

When the production system provides a previous shot, the previous shot is also the voice reference.

The speaking voice MUST remain identical throughout the entire episode.

Maintain:

- same voice identity
- same timbre
- same pitch
- same speaking speed
- same warmth
- same preschool energy
- same pronunciation
- same accent
- same age impression
- same emotional tone
- same recording quality

Never generate a different interpretation of the character voice.
Never replace the voice with a narrator.
Never make the character sound older or younger.

If multiple shots belong to the same episode, their voices must sound as if they were recorded during the same recording session.

## First Frame Lock

For Shot 02+ continuation shots:

```text
Treat @image1 as the complete visual master reference.
Preserve not only framing, but also colour identity, lighting identity, exposure, white balance, atmosphere, environment identity, character proportions, and character performance.
The viewer must not perceive a shot boundary.

The first visible frame must be visually indistinguishable from @image1.
Not similar. Not close. Identical.

Only after the first frame matches perfectly may animation begin.
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
COLOUR CONTINUITY
Match the previous shot exactly.
Maintain identical white balance, exposure, colour temperature, saturation, contrast, brightness and pastel palette.
Never introduce cool shift, warm shift, green tint, magenta tint, orange grading, HDR look or cinematic LUT.
The entire episode must appear colour graded as one continuous film.

----------------------------------------
LIGHTING CONTINUITY
Preserve the lighting from the previous shot exactly.
Maintain identical light direction, light intensity, shadow softness, ambient lighting, highlight behaviour, cloud brightness and grass brightness.
Do not reinterpret the lighting. Continue it.

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
- Shot production standard: `00-CORE/SHOT_PRODUCTION_STANDARD.md`
- Colour continuity: match previous shot white balance, exposure, colour temperature, saturation, contrast, brightness and pastel palette
- Lighting continuity: match previous shot light direction, intensity, shadow softness, ambient lighting and highlight behaviour

## Required Global QA Locks

This shot must pass the global QA rules in `00-CORE/17_VIDEO_GENERATION_STANDARD.md`
and `11-DOCS/16_VIDEO_QA_SPEC.md` for:

- Hard Background Lock
- Intra-Shot Character Continuity Lock
- Single Visible Path Rule
- Occlusion Is Not A Transition
- Camera Must Not Break Continuity
- First Second Continuity Hold
- Object Identity Lock

Keep any shot-specific continuity notes below this section. Do not restate or weaken the
global rules locally.

## QA Checklist

Reference: `11-DOCS/16_VIDEO_QA_SPEC.md`
Standards: `00-CORE/17_VIDEO_GENERATION_STANDARD.md`,
`00-CORE/SHOT_PRODUCTION_STANDARD.md`

- [ ] If this world has sub-zones, the correct zone is specified in Mekan (not just the world name)
- [ ] Zone-specific Spatial Anchor and Reference Use are filled in (if zone applies)
- [ ] Required Global QA Locks section included
- [ ] Character integrity verified
- [ ] Character consistency verified
- [ ] Intra-shot character continuity verified
- [ ] Single visible character path verified
- [ ] No occlusion transition, teleport, disappearance or same-shot regeneration
- [ ] Voice identity verified
- [ ] Voice pitch, timbre, speaking speed, pronunciation, accent and recording quality match previous speaking shot
- [ ] Object persistence verified
- [ ] Hard background and object identity locks verified
- [ ] No rendering artefacts
- [ ] Camera consistency verified
- [ ] Camera does not create hiding, reset, layout morphing or a new location reveal
- [ ] Lighting consistency verified
- [ ] Light direction, intensity, shadow softness, ambient lighting and highlight behaviour match previous shot
- [ ] Colour identity verified
- [ ] White balance, exposure, colour temperature, saturation, contrast, brightness and pastel palette match previous shot
- [ ] The viewer cannot perceive a shot boundary
- [ ] Canonical rules followed
```

---

## Kurallar

- Bu template her yeni sahne dosyasında kullanılmalıdır.
- `[]` ile belirtilen yerler sahneye göre değiştirilir.
- Her shot 15 saniye (6 shot × 15 sn = 90 sn toplam bölüm).
- Maksimum 3 karakter.
- Tek mekan tercih edilir.
- Tek duygusal hedef.

---

*Bu belge tüm yeni sahneler için standart şablondur.*
