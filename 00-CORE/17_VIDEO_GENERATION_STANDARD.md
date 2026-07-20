# 17 — Video Generation Standard

> Tüm shot dosyaları bu standarttan üretir.
> Her shot bu dosyaya atıfta bulunur, aynı kuralları tekrar etmez.
> Pacing, hook, camera-emphasis and ending style (retention) decisions are defined in
> `00-CORE/18_VIDEO_STYLE_AND_RETENTION_STANDARD.md` — that document does not override the
> continuity/technical rules below (e.g. Camera Rules, Text Safety), it builds on top of them.

---

## SHOT COMPLETION AND QUALITY RESET RULE — HIGHEST CONTINUITY PRIORITY

This section overrides every older instruction that makes exact final-frame continuity the
default or permits an unlimited recursive frame chain.

### Complete Action Inside Each Shot

Every shot must begin, perform and complete one manageable main visual action. Do not end
while a character is walking, entering, approaching, leaving, turning, pointing, reaching,
jumping, landing, bouncing, gesturing, sitting, standing or otherwise changing position.
Camera movement must also complete and settle inside the shot.

The final approximately 1–2 seconds must show a stable, natural and grounded ending state.
Subtle breathing, blinking, a tiny eye-focus change, a small expression settle and gentle
environmental motion may continue. The ending must not feel frozen, empty or padded.

If an action does not fit, simplify it, begin it earlier, shorten dialogue, merge the action
or redesign the shot division. Never plan the next shot to resume unfinished movement.

### Fresh-Generation Default

Start each new shot as a fresh highest-quality generation using the canonical approved
World, approved character identity references, a clean shot-specific starting composition,
approved visual style and the highest reliable quality mode. Preserve continuity through
identity, costume, world, screen direction, approximate placement, lighting, colour,
dialogue and editing. A clean editorial cut is preferred over progressive degradation.

### Exact Generated-Frame Chaining Limit

Exact final-frame continuity is allowed only when genuinely necessary for a continuous
physical action or camera event and only when the generated frame passes visual QA.

- Normal maximum: 2 consecutively linked shots.
- Exceptional maximum: 3 consecutively linked shots.
- A shot after Linked Continuity Shot 2 should normally reset.
- A shot after Linked Continuity Shot 3 must always reset.
- Never create a chain of 4 or more shots.

Reject the linked frame if character identity, anatomy, world layout, camera distance,
colour, contrast, sharpness, scale or prop identity has drifted. Quality takes priority over
pixel-perfect matching. Do not preserve a degraded frame merely because it matches the cut.

### Mandatory Quality Reset

A reset uses the canonical approved World, approved character references, a newly composed
clean start frame, approved camera/colour/lighting and the highest reliable production mode.
The previous generated final frame is not the reset shot's primary visual source.

### Mandatory Pre-Production Schedule and Fields

Decide the reset schedule before video generation. Label every shot with exactly one mode:

- `FRESH QUALITY-RESET SHOT`
- `LINKED CONTINUITY SHOT 1`
- `LINKED CONTINUITY SHOT 2`
- `LINKED CONTINUITY SHOT 3 — EXCEPTIONAL MAXIMUM`

Every future shot document must contain:

- `Production Mode`
- `Clean Start State`
- `Complete Main Action`
- `Completed End State`
- `Stable Final Anchor`
- `Next-Shot Dependency`

`Next-Shot Dependency` is one of:

- `NONE — next shot starts fresh`
- `LIMITED VISUAL CONTINUITY ONLY`
- `EXACT FRAME CONTINUITY REQUIRED`

Exact dependency is rare and requires written justification.

### Generated-Frame QA Gate

A generated frame may become the next linked shot's input only when the chain is within the
2–3 shot limit and the frame passes checks for identity, world layout, camera distance,
colour, contrast, sharpness, scale and object persistence. If any check fails, break the
chain and use a fresh quality reset.

### Legacy Wording Interpretation

Interpret older `@image1`, “previous final frame” and “continue from previous shot” wording
through the pre-planned Production Mode. Fresh shots use clean canonical references. Linked
shots may use a QA-approved generated final frame only within the chain limit.

### Authoritative Summary

`Every shot completes its own main action. Exact AI-generated final-frame continuity is limited to normally two and exceptionally three consecutive shots. After that, production must restart from clean canonical World and character references at the highest reliable quality. A clean cut between high-quality shots is always preferred over seamless continuity with progressive visual degradation.`

---

## Üretim Kuralı: Sadece OpenArt Prompt

> Bir bölüm için SADECE OpenArt prompt dosyaları (03_VIDEO_EXPORTS/shot-XX-openart-prompt.md) oluşturulur.
> Başka production dosyası oluşturmaya gerek yoktur.
> Shot markdown dosyaları (01_SHOTS/) zaten mevcuttur ve içeriği bellidir.
> Yeni bir bölüm için yapılması gereken tek şey: her shot için openart prompt oluşturmaktır.

---

## Colour Drift Gate and Anchor Pipeline

> OpenArt video modelleri her shot'ta karanleştirme ve contrast artırma eğilimindedir.
> Prompt talimatları yeterli değildir. Tek çözüm: sabit anchor + ölçülü normalizasyon + Drift Gate.
>
> **Kanıt (S01E12):** Shot 1→8 arası %15.7 progressive darkening, %12.7 contrast artışı.
> Bu nedenle generated final frame zincirleri varsayılan değildir; yalnızca önceden planlanmış
> linked shot'larda, QA onayıyla ve 2–3 shot sınırı içinde kullanılabilir.

### Shot Düzeltme Kuralları (Final Post-Production Pass)

Bu ölçüm ve düzeltme adımları yalnızca tüm shot'lar tamamlanıp onaylandıktan sonra, tek
episode-wide final colour-matching pass içinde uygulanır:

1. **Final frame çıkar** (`ffmpeg -sseof -0.1`)
2. **Parlaklık ölç** (PIL ImageStat)
3. **Shot 1 referansına ±5% içinde mi?** kontrol et
4. **Eğer dışındaysa:** `eq=brightness=X` ile düzelt (sadece parlaklık, kontrast/değil)
5. **Eğer ±5% içindeyse:** dokunma, olduğu gibi bırak

**Düzeltme Formülleri (S01E12'den çıkarılan):**

| Fark | Brightness | Saturation |
|------|:----------:|:----------:|
| -8% | +0.04 | +1.03 |
| -5% | +0.03 | +1.03 |
| -3% | +0.02 | +1.02 |
| ±2% | +0.005 | +1.01 |
| 0% | 0 | 1.00 |
| +3% | -0.02 | +1.02 |
| +5% | -0.03 | +1.02 |
| +8% | -0.04 | +1.02 |

**Önemli:**
- Sadece parlaklık ve doygunluk düzelt (kontrast/değil)
- Düzeltme sonrası final frame yalnızca QA kanıtı olarak çıkarılabilir
- shot-XX-final-frame.png yalnızca QA/raporlama çıktısıdır
- Post-production'da düzeltilmiş/normalize edilmiş bu türev frame, sonraki shot'ın `@image1`'i
  veya production anchor'ı olamaz. Linked kullanım gerekiyorsa yalnızca düzeltme öncesi özgün
  generated final frame QA'dan geçirilir ve zincir sınırı içinde kullanılır.

### Temel Kural

```
Approve clean start/end stills → Generate motion → Complete and approve all shots → One final episode-wide upscale and colour-match pass

VARSAYILAN: Ayrı üretilmiş ve onaylanmış fresh clean start-frame still kullan.
İSTİSNA: Önceden planlanmış linked shot'ta özgün generated final frame'i QA onayıyla kullan;
normalize/grade/upscale edilmiş türev frame'i production anchor yapma.
```

### EPISODE_COLOR_MASTER.png

- Bölümün başından onaylanmış sabit bir görsel
- Sonradan üretilmiş bir video frame'inden ALINMAZ
- Tüm bölüm boyunca DEĞİŞTİRİLMEZ
- Tüm tamamlanmış shot'lar final episode-wide pass içinde bu master'a göre eşleştirilir

### normalize_shot.py

Gerekirse yalnızca tüm shot'lar tamamlandıktan sonra final assembly aşamasında batch olarak
çalıştırılır. Ürettiği frame'ler sonraki generasyonlara girdi olamaz:

```bash
python3 POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/TOOLS/normalize_shot.py \
  EPISODE_COLOR_MASTER.png \
  shot-XX.mp4 \
  ./output/
```

Çıktılar:
- `shot-XX-normalized.mp4` — normalize edilmiş video
- `shot-XX-final-frame-normalized.png` — normalize edilmiş son frame
- `shot-XX-drift-report.json` — JSON rapor
- `shot-XX-qa-report.txt` — İnsan okunabilir rapor

### Drift Gate Eşikleri

| Metrik | Eşik | Açıklama |
|--------|:----:|----------|
| Parlaklık | ±5% | Master'dan sapma |
| Yerel Kontrast | ≤+100% | Encoding farkından dolayı geniş |
| Sharpness | ≤+100% | Encoding farkından dolayı geniş |
| Doygunluk | ±7% | Master'dan sapma |
| Gölge derinliği | ≤±15% | Belirgin derinleşme olamaz |
| Highlight clipping | ≤+2% | Artamaz |

### Continuity Rule

```
Fresh shot'ta ayrı onaylanmış clean start-frame still kullan. Linked shot'ta yalnızca özgün,
QA-onaylı generated final frame bir sonraki `@image1` olabilir. Normalde iki, istisnai olarak
üç linked shot'tan sonra canonical kaynaklardan zorunlu fresh quality reset yap. Düzeltilmiş,
normalize edilmiş, graded veya upscaled türev frame'i production anchor yapma.
```

### Prompt Kuralı

Her shot prompt'unda COMPACT bir satır olmalı:

```
Preserve the soft warm matte preschool baseline; no darkening, local-contrast growth, oversharpening, HDR, gloss, or harsh shadows.
```

Birincil koruma clean still anchor'lar, bağımsız kalite resetleri ve final episode-wide
Drift Gate'tir.

### Final-Edit Rule

Upscale ve final colour matching'i yalnızca bir kez, bütün shot'lar tamamlandıktan sonra
uygula. Intermediate graded/normalized frame'leri generation input olarak kullanma.

---

## Production Pipeline

Gerçek üretim akışı:

```
Canonical World + approved character references
    ↓
Clean Shot 01 start still (+ clean end still whenever possible)
    ↓
Generate Shot 01 motion and complete the action
    ↓
Fresh clean Shot 02 start still from canonical references
    ↓
Generate Shot 02 motion and complete the action
    ↓
Quality reset at least after 2–3 exactly linked clean-anchor shots
    ↓
Complete all shots → one final upscale and colour-matching pass
```

---

## First Frame Continuity

Every shot uses a pre-approved start source. The default is a fresh shot-specific composition
from canonical references, not the previous shot video.

When exact linkage is genuinely necessary, the original generated final frame of the previous
shot may be reused as the next exact start still after QA approval, within the 2–3 shot limit.
Reject soft, distorted, colour-drifted or artifacted frames and reset fresh instead. A clean
editorial cut is acceptable.

Maintain:
- character position
- camera height
- framing
- lighting
- colour grading
- world identity

---

## Voice Continuity

> OpenArt her shot'ta yeni ses üretme eğilimindedir. Bu kural bunu engeller.

The speaking voices MUST remain identical across the whole episode.

### Zorunlu Ses Kuralı (Her Shot İçin)

Her shot'ta açıkça belirtilmeli:

```text
Use the exact same approved saved [CHARACTER] voice asset / voice preset / voice ID.
Do not generate a new [CHARACTER] voice.
Do not use a narrator voice.
Do not change pitch, age, accent, speed, stability, similarity, or voice style.
[CHARACTER] must sound [description] — same as the approved [CHARACTER] voice.
```

### Voice Asset Kullanım Kuralı

- Her karakter için onaylanmış bir ses kaydı (voice asset / preset / ID) vardır
- Bu ses kaydı tüm shot'larda AYNI olmalıdır
- Yeni ses ÜRETİLMEMELİDIR
- Narrator voice KULLANILMAMALIDIR
- Pitch, age, accent, speed, stability, similarity, style DEĞİŞTİRİLMEMELİDİR
- OpenArt'ta elle kontrol edilmeli: aynı kayıtlı ses seçili olmalı

### Character-Specific Voice Rules

**Kiko:**
```text
Use the exact same approved saved Kiko voice asset / voice preset / voice ID.
Do not generate a new Kiko voice.
Kiko must sound curious, playful, then warm — same as the approved Kiko voice.
```

**Opa:**
```text
Use the exact same approved saved Opa voice asset / voice preset / voice ID.
Do not generate a new Opa voice.
Do not use a narrator voice.
Opa must sound warm, gentle, wise, grandfatherly, and soft — same as the approved Opa voice.
```

**Mimi:**
```text
Use the exact same approved saved Mimi voice asset / voice preset / voice ID.
Do not generate a new Mimi voice.
Mimi must sound curious, cozy, gentle — same as the approved Mimi voice.
```

### Voice QA Kontrolü

Her speaking shot için QA checklist'e eklenmeli:
```text
- [ ] Same voice identity as previous shot (no new voice generation)
- [ ] Voice matches approved saved voice asset / preset / ID
```

---

## Colour Continuity

Match the approved Episode Colour Master and episode lighting identity. A linked previous frame
may guide placement and action continuity, but it never replaces the Episode Colour Master.

CRITICAL: Do NOT desaturate between shots. Do NOT make colours softer or paler.
Each shot must maintain the SAME saturation level as the first shot.

Maintain:
- identical white balance
- identical warmth
- identical exposure
- identical saturation (DO NOT reduce)
- identical pastel palette (DO NOT soften)
- identical contrast

Avoid:
- blue tint
- green tint
- orange shift
- desaturation
- softening of colours
- fading of colours
- HDR look
- cinematic LUT

The entire episode must appear colour graded as one continuous film.

---

## Reference Source Policy

Never use screenshots as production reference images.

Do not use:
- browser screenshots
- macOS screenshots
- screen captures
- preview-window captures
- compressed viewer images
- social media exports
- images copied from the screen

Use only:
- original downloaded PNG/JPG from the generation tool
- separately approved clean production stills created from canonical references
- approved production stills from the asset folder
- for a pre-planned linked shot only: the original, QA-approved generated final frame, within
  the 2–3 shot chain limit

Exported video frames may be used for QA inspection only, never as generation references.

Reason:

Screenshots can change colour through browser rendering, monitor colour profiles, Display P3 vs sRGB conversion, OS screenshot processing, compression, scaling and preview rendering.

Screenshots can cause:
- faded colour
- lower saturation
- incorrect brightness
- shifted white balance
- generational colour drift

If only a screenshot exists, do not use it as a production reference. Re-export or re-download the original frame/image.

---

## Episode Colour Master

Every episode must have one approved Episode Colour Master.

Usually this is the approved original first-frame still from Shot 01.

The Episode Colour Master defines:
- white balance
- exposure
- saturation
- contrast
- warmth
- pastel palette
- shadow softness
- highlight behaviour

Every shot must use two forms of clean reference:

1. Clean Shot-Specific Start Still
   Purpose:
   - shot composition
   - character position
   - camera and scale lock
   - initial pose

2. Episode Colour Master
   Purpose:
   - colour stability
   - white balance stability
   - exposure stability
   - saturation stability
   - preventing generational colour drift

Do not derive colour from a previous generated shot.

Every shot must remain visually matched to the Episode Colour Master.

Add this exact line to the Production Standard section of every shot:

Colour master: use the approved original Shot 01 still as the Episode Colour Master. Do not use a screenshot. Do not allow colour to fade, desaturate, cool down, warm up, brighten, darken or drift from the Episode Colour Master.

---

## Colour Drift Prevention

Generative video can lose saturation or shift colour across multiple shot generations.

To prevent this:

- Use the Episode Colour Master in every shot.
- Use a linked previous frame only when the reset schedule requires exact action/placement
  continuity; otherwise start fresh from canonical references.
- Do not use a screenshot as colour reference.
- Do not allow the model to "improve" or "rebalance" the image.
- Do not allow automatic exposure correction.
- Do not allow automatic white balance correction.
- Do not allow a new colour grade.
- Do not allow fading or desaturation between shots.

Every continuation shot must maintain:
- same white balance
- same exposure
- same colour temperature
- same saturation
- same contrast
- same pastel palette
- same shadow softness
- same highlight behaviour
- same warm morning feeling

Reject if:
- colour looks more faded than the Episode Colour Master
- saturation drops
- image becomes cooler
- image becomes more grey
- image becomes more orange
- contrast changes visibly
- lighting looks like a different time of day

---

## Lighting Continuity

Preserve the approved episode lighting identity. In a linked shot, also preserve the previous
frame's light direction and exposure unless doing so would carry visible degradation.

Maintain:
- identical light direction
- identical light intensity
- identical shadow softness
- identical ambient lighting
- identical highlight behaviour

Do not reinterpret the lighting. Continue it.

---

## Camera Rules

- Child eye level throughout
- Gentle 35mm framing
- Slow stable movement
- No zoom
- No handheld motion
- No sudden camera reset
- No tight framing

> **Locked camera by default (Global Camera Stability Rule).**
> The camera stays locked unless a camera move is explicitly required by the story beat AND
> explicitly written in the shot document. OpenArt must never invent camera movement, sudden angle
> changes, surprise reframing, or camera-follow on its own. The approved first frame defines the
> camera angle, height, distance, framing and composition lock for the entire shot; the video must
> not drift into a new angle later. Characters and small elements (leaves, butterflies, wind-driven
> props) may move inside the frame, but the camera must not follow them — if an action would need
> the camera to move to stay visible, redesign the shot so it fits the existing frame. When a shot
> is meant to be visually stable, the OpenArt-facing prompt must say: "Locked camera only. No pan.
> No zoom. No push-in. No pull-back. No camera movement. No reframing. No angle change. No reveal."
> Full rule, "when movement is allowed", prompt-wording rule and failure pattern:
> `00-CORE/18_OPENART_CONTINUITY_AND_MOTION_RULES.md` §18.

---

## Text Safety

Do not display dialogue as on-screen text.

No speech bubbles.
No captions.
No subtitles.
No text.

---

## Ball Continuity

The same round yellow ball must persist through the entire episode.

The ball must not change colour, size, texture, or shape.

---

## World Continuity

Central Square must remain visually consistent.

- Big Pompom Tree in background whenever composition allows
- Warm morning light throughout
- Soft pastel colours
- Safe open play space
- No new environment
- No extra characters
- No redesign

---

## Scale

Characters should feel small and childlike within Central Square, but must remain readable for facial expression and action.

Use wide framing for environment identity and medium framing for emotional beats.

---

## Animation Quality

- All movements slow and natural
- No sudden gestures
- No fast cuts
- Characters never fully frozen — idle animations present
- Grass moves gently in wind
- Environmental rhythm consistent

---

## Child Safety

- No sharp edges or dark shadows
- No threatening imagery
- All characters express only positive or gently curious emotions
- No violence, conflict, or distressing content
- Soft and safe throughout

---

## Spatial Continuity

Canonical World and shot-specific clean still references must jointly guarantee location
continuity. A previous generated video is not a permitted reference.

The AI may understand the general environment but place the characters in a similar, incorrect area.

Therefore every shot must explicitly restate the physical location using environment anchors.

Spatial continuity means:

- same physical place
- same relative camera direction
- same major landmarks
- same character-to-landmark relationship
- same prop position
- same environment identity
- no relocation within the world unless the shot explicitly shows movement

Every shot must include a short section named:

## Environment Anchors

This section describes the stable landmarks and their relative positions.

For example:

- Big Pompom Tree remains in the background.
- Luca and Noah remain in the open grass play area in front of the tree.
- The round yellow ball remains between or near the children.
- The camera remains at child eye level.
- The shot does not relocate to another part of Central Square.
- No new path, building, bush, flowerbed, bench or object is introduced unless already part of Central Square canon.

Add this rule:

Do not let the AI infer location from any previous generated video. Use the canonical World,
the approved clean shot-specific still and an explicit local environment description.

---

## Intra-Shot Background Persistence

Every generated video shot must preserve the background objects visible in its first frame.

Background landmarks are not decorative.
They are part of the physical location.

If an object is visible in the first frame, it must not:
- disappear
- transform
- be replaced
- change position
- change scale
- change identity
- become a different object
- be swapped with a tree, bush, house, path, flowerbed, or bench

This applies to:
- benches
- trees
- bushes
- paths
- lamps
- flowerbeds
- distant houses
- fences if canon
- landmarks
- props
- large background shapes

A bench must remain a bench.
A tree must remain the same tree.
A path must remain the same path.
A visible landmark must remain in the same relative position.

The AI must not repaint or reinterpret the background during the video.

Only character motion, prop motion, and explicitly requested camera motion may change.

---

## First Frame Object Lock

The first visible frame of every video shot defines the physical set for that shot.

Lock the following from the first frame:

- character positions
- prop positions
- background objects
- landmark positions
- camera angle
- camera height
- camera side
- lighting
- colour grade
- depth layout

The video may animate movement, but it must not regenerate the set.

If the first frame contains:
- a bench on the right,
- a bench on the left,
- Big Pompom Tree in the background,
- a path behind the characters,
- a yellow ball between the characters,

then those objects must remain consistent throughout the shot.

Objects may only leave the frame if the camera physically pans away from them.
They must not vanish while still inside the visible area.

---

## Background Drift Prevention

Generative video models may accidentally repaint the background during movement.

To prevent this:

- Keep camera movement minimal.
- Avoid unnecessary pans when background continuity matters.
- Avoid "reveal" language unless the shot truly reveals a new area.
- Do not allow the model to invent new background objects.
- Do not allow a bench to become a tree.
- Do not allow a tree to become a bush.
- Do not allow a path to change shape.
- Do not allow background houses to shift.
- Do not allow landmarks to slide or morph.

Use language such as:

"The background is locked from the first frame. Do not repaint the set. Maintain all visible benches, trees, paths and landmarks in the same relative positions throughout the shot."

---

## Global OpenArt Continuity Locks

These rules apply to every generated Pompom Hills video shot before approval. They are
global production gates, not episode-specific preferences.

### Hard Background Lock

Every video shot must treat the environment as a fixed physical stage. All visible
background objects must keep their position, scale, identity and relationship during the
shot and between continuity-linked shots.

Objects that must not move, morph, duplicate, disappear, swap identity or change
position include trees, tree trunks, benches, planters, bushes, flowerbeds, rounded
paths, paving stones, stepping stones, grass patches, bunting, flags, houses, walls,
landmarks and any object visible in the first frame.

A bench cannot become a planter. A bush cannot become a tree. A flowerbed cannot become
a grass mound. A path cannot become a road. A planter cannot move to a new side of the
frame. A landmark cannot resize, duplicate, disappear or shift position.

### Intra-Shot Character Continuity Lock

Character continuity must remain unbroken inside the same video clip. This applies
within a single shot, not only between shots.

A character must remain the same continuous physical character from first frame to final
frame. Characters must not disappear, reappear, regenerate after occlusion, teleport,
duplicate, switch sides suddenly, jump position, change scale suddenly, change identity,
or become hidden and then appear elsewhere.

Each character must follow one clear visible path inside the shot. The path must be
readable frame-to-frame.

### Single Visible Path Rule

Characters must stay on visible walkable areas only: clear paths, paving stones,
stepping stones, clear open grass patches, or open visible areas beside objects.

Characters must not walk through bushes, flowerbeds, planters, tree trunks, benches,
houses, walls, dense grass, foreground plants, decorative objects, or any object that
should physically block them.

Characters must not enter from one side, disappear behind an object, and exit from
another side. Characters must not change walking direction unless the turn is clearly
visible.

### Occlusion Is Not A Transition

Do not use occlusion as a transition.

Characters must not be hidden behind bushes, flowers, benches, tree trunks, planters,
walls, houses, flags or foreground plants as a way to continue or reset motion.
Characters must remain clearly visible for the full shot.

A tiny natural partial overlap is allowed only if it lasts less than half a second, does
not hide the character's full body, does not hide the character's direction of travel,
and the character does not reappear somewhere else after the overlap. Full-body
occlusion is not allowed.

### Camera Must Not Break Continuity

Camera movement must protect continuity. Allowed camera movement: tiny push-in, tiny
settle, very slow stable drift, nearly locked-off camera.

Forbidden camera movement: camera reset, fast pan, whip pan, orbit, fast zoom, sudden
angle jump, tracking move that changes the set layout, movement that causes background
objects to shift, movement that hides a character behind foreground objects, movement
that reveals a different location, or movement that makes the environment feel
regenerated.

For preschool continuity, stable visible action is more important than cinematic
movement.

### First Second Continuity Hold

For every continuity-linked shot, the first 1 second must hold extremely close to
`@image1`.

During the first 1 second: camera angle, camera height and lens feel must not change;
character positions and scale must not jump; background objects must not move; no new
object may appear; no object may disappear; no character may teleport or switch sides;
lighting and colour grading must not change.

After the first second, only small character motion and tiny camera settle are allowed.

### Object Identity Lock

Every visible object keeps its identity for the full shot and across continuity-linked
shots. Reject if a bench becomes a planter, planter becomes bush, bush becomes tree,
flowerbed becomes grass mound, grass becomes road, house becomes shop, path becomes
road, tree changes trunk shape or location, landmark changes silhouette, object
duplicates, object disappears, object changes side of the frame, or object scale changes
unnaturally.

### Interaction Object Usability Rule

A shot may interact with an object only if that object is visible in `@image1` and
usable for the planned action at its current size, shape, position, and distance.

Visible is not enough.

If the object is too small, too far away, too crowded, partly cropped, or not shaped for
the planned action, simplify the character action to fit the existing object.

Do not enlarge, multiply, move, reshape, replace, spawn, or relocate any object to
satisfy an action.

Characters adapt to the environment.
The environment does not adapt to the characters.

### Environment Object Lock

All environment objects visible in `@image1` are locked in place.

Trees, flowers, grass patches, hills, stones, doorways, props, sky elements, furniture,
anchors, and landmarks must not move, grow, shrink, slide, drift, pop in, enter frame,
leave frame, or reposition.

Only characters may move unless the shot explicitly allows a planned location
transition, such as a threshold crossing.

The camera must not move to make an object more usable.
The object must not move toward the character.
The shot must use the existing composition exactly.

### Action Scale Check

Before generating any shot, answer these questions:

1. Which object does this shot interact with?
2. Is the object visible in `@image1`?
3. Is the object usable for the action in its current size, shape, position, and
   distance?
4. Would the character need camera movement to reach or use it?
5. Would the model be forced to enlarge, move, multiply, reshape, or spawn the object?
6. Does the action finish and settle into the approved clean end still, or into a stable
   final 1–2 second pose when End Frame mode is unavailable?

If any answer fails, do not spend video credits. Simplify the action, change the staging,
or regenerate the prerequisite still before generating video.

### Character Action Reduction For Stability

If a shot has background morphing, occlusion or teleport risk, reduce character
movement. Prefer pointing, looking, head turn, tiny step, smiling, gentle reaction,
small body turn, and shared still moment.

Avoid walking across the set, crossing behind objects, entering or exiting frame, moving
behind bushes, moving behind benches, moving behind planters, using foreground objects
as transitions, and travelling from object to object inside one short shot.

QA should flag shots with unnecessary walking as higher risk.

### Global Rejection Criteria

Reject any generated video if any character disappears inside the same shot, reappears
inside the same shot, teleports, regenerates after occlusion, is fully hidden by
bushes/flowers/benches/trees/planters/walls/houses/flags/foreground plants, walks
through blocking objects, emerges from the opposite side after being hidden, changes
side without visible continuous movement, or has a movement path that is not
continuously readable.

Reject any generated video if foreground plants cover a character's full body, camera
movement hides a character and reveals them elsewhere, any tree/bench/planter/bush
changes position, any path changes layout, any landmark shifts/duplicates/resizes/
disappears/changes shape, background objects morph, background layout changes, the
environment feels regenerated, camera resets, lighting or colour grading changes
unexpectedly, exposure/brightness/contrast/saturation/colour temperature drifts, extra
characters appear, or forbidden text/logo/caption/title/subscription/end-card graphics
appear unless explicitly required by a separate approved asset.

### Character Introduction After Empty Opening Rule

When a reusable world micro-opening has no characters, the first story shot must introduce the first character naturally. A character must not suddenly appear in the first story shot as if spawned into the environment.

After an empty opening, the first character introduction must use one of these approved methods:

#### Approved Method A — Camera Reveal
The first story shot begins from the opening final frame or very close to it. The camera then moves gently, slowly and naturally to reveal the character who was already logically present just outside the opening composition.

Allowed camera movement:
- tiny pan
- tiny tilt
- slow child-eye-level settle
- soft push-in with slight reframing
- gentle reveal from the edge of the same set

Not allowed:
- camera reset
- jump cut to a new angle
- fast pan
- whip pan
- sudden zoom
- reveal of a different location
- environment redesign

The character must be revealed inside the same physical set, not created in a new layout.

#### Approved Method B — Visible Character Entrance
The first story shot begins from the opening final frame or very close to it. The character enters through a visible, safe, walkable path. The entrance path must be fully visible from the first moment the character appears.

The character may enter from:
- visible rounded path
- visible paving stones
- visible stepping-stone path
- clear open walkable area
- camera-facing side of the same set

The character must not enter from:
- behind bushes
- behind trees
- behind benches
- behind planters
- behind houses
- behind walls
- dense grass
- foreground plants
- hidden off-screen area that causes sudden pop-in

No teleporting. No pop-in. No sudden appearance. No hidden entrance. No character emerging from bushes.

#### Approved Method C — First Frame Character Already Partially Visible
If OpenArt cannot perform a clean visible entrance, the first story shot may begin with the character already partially visible at the edge of the frame.

This is allowed only if:
- the character is not fully centered suddenly
- the character feels like they are entering the scene
- the character is on a visible walkable path
- the first second still matches the opening environment
- the character's movement continues naturally from that position

This is safer than a hidden pop-in.

#### NOT ALLOWED
Do not start Shot 01 after an empty opening with a fully centered character suddenly standing in the environment unless the story explicitly uses a cutaway or time jump.

For normal world episodes, avoid:
- character suddenly appearing in the middle of the frame
- character already standing in a place that was empty in the opening with no camera explanation
- character popping into frame
- character materializing after the opening
- hard cut from empty world to character-centered frame with no entrance logic
- camera reset that hides the pop-in
- character entering from behind bushes or foreground objects
- character being revealed by occlusion

#### Global Generation Standard Update
For any episode using an empty world micro-opening, Shot 01 must be planned as an entrance/reveal shot. Shot 01 should not simply say "character already visible" unless the character is partially visible at the edge or the shot is clearly designed as a natural reveal.

Preferred Shot 01 structure after empty opening:
- 0-1 sec: Hold very close to opening final frame.
- 1-4 sec: Camera gently reveals the character OR character begins entering through visible path.
- 4-10 sec: Character performs first story action.
- 10-15 sec: Dialogue / emotional beat / warm hold.

Do not center the character immediately at frame 0 after an empty opening unless the opening final frame already included the character, which normal world micro-openings should not.

### Strict Frame Match Rule for Character Introduction

When a new character is introduced after a locked continuity frame, the existing frame has priority over the character entrance.

The model must not recompose the scene to introduce the character.

This rule applies to:
- Empty opening frame → first story shot
- One-character shot → two-character shot
- Any shot where a new character enters after the first frame
- Any continuity-linked shot using `@image1`

The first frame of the new shot must match the previous approved final continuity frame as closely as possible.

Preserve:
- Camera angle
- Camera height
- Lens feel
- Framing
- Character positions already present
- Character scale
- Background object positions
- Landmark positions
- Path layout
- Lighting
- Colour grading
- Exposure
- Contrast

Do not:
- Recompose the scene for the entering character
- Move existing characters to make room
- Reset the camera
- Change lens feel
- Create a new establishing shot
- Zoom in to hide the transition
- Move background objects
- Create new paths or cleaner layouts
- Use the previous frame as loose inspiration only

The entering character must adapt to the locked frame.

If the full entrance path cannot be shown safely inside the locked composition, the character may begin already partially visible at the edge of the existing frame. This is preferred over changing the camera, changing the layout, or causing pop-in.

Continuity priority order:
1. Approved clean start-still match
2. Existing character position and scale
3. Background object lock
4. Entering character visibility
5. Entrance path clarity

The entering character's movement is secondary to continuity.

### No Pull-Back Continuity Rule

When a shot begins from a locked clean start still, the generated video must not begin
wider than that clean still.

Never pull back at the beginning of a continuation shot in order to introduce a character.

Do not reveal more environment, more sky, more side objects, or additional props at the first frame.

If the entering character cannot be shown without widening or recomposing the frame, the entering character should begin already partially visible at the frame edge.

Priority:
1. Approved clean start-still match
2. No wider reset
3. No new object reveal
4. Entering character visibility

Global QA for continuation shots:
- [ ] Shot does not begin wider than its approved clean start still.
- [ ] No pull-back occurs at shot start.
- [ ] No new side objects are revealed at first frame.
- [ ] Entering character adapts to the locked frame instead of forcing recomposition.

### No New Character In First Frames Rule

When a shot begins from a locked clean `@image1`, no character absent from that approved
clean still may pop in during the first 2 seconds.

The first 2 seconds are reserved for strict continuity matching.

During the first 2 seconds:
- Match `@image1` as closely as possible
- Preserve camera angle
- Preserve camera distance
- Preserve framing
- Preserve lens feel
- Preserve all visible background object positions
- Preserve lighting, colour grading, exposure and contrast
- Preserve any already-present characters in the same position, scale and direction
- Do not introduce new characters
- Do not reveal new side objects
- Do not pull back
- Do not push in
- Do not recompose
- Do not create a new establishing shot

After the first 2 seconds, the new character may enter naturally inside the locked composition.

The entering character must adapt to the existing frame.
The camera must not adapt to the entering character.

If the entrance cannot be shown clearly without changing the camera, the new character may begin partially visible at the frame edge AFTER the 2-second hold.

This rule applies to:
- Empty opening frame → first story shot
- One-character shot → two-character shot
- Any shot where a new character is introduced
- Any continuity-linked shot using `@image1`

Priority order:
1. First 2 seconds match `@image1`
2. No camera pull-back or recomposition
3. Existing character/background continuity
4. New character entrance after 2 seconds
5. Entrance path clarity

---

## How to Use This Standard

In each shot file, replace the repeated sections with:

```text
Use the production generation standard (00-CORE/17_VIDEO_GENERATION_STANDARD.md).

Reference source:
Use original downloaded/exported production media only. Never use screenshots.

Episode Colour Master:
Approved original Shot 01 still.

Clean Start Anchor:
Separately approved clean shot-specific start-frame still; never a generated-video frame.

Clean End Anchor:
Separately approved clean end-frame still whenever Start Frame + End Frame mode is supported.
Location: Central Square.
Lighting: Warm morning light.
Ball: Same round yellow ball.
```

This keeps shot files short and maintainable.

---

## Mandatory Application Rule

This standard applies to ALL episodes and ALL shots.

Every shot file must include:
- Background Object Lock section (after Environment Anchors or after the episode-specific environment description)
- Background persistence sentence in the Visual Prompt
- Intra-shot background drift QA checklist items
- Required Global QA Locks section referencing Hard Background Lock, Intra-Shot
  Character Continuity Lock, Single Visible Path Rule, Occlusion Is Not A Transition,
  Camera Must Not Break Continuity, First Second Continuity Hold and Object Identity
  Lock

No shot may omit these sections.

No episode may skip background persistence rules.

No episode may skip the Global OpenArt Continuity Locks.

This rule was added after discovering intra-shot background drift in generated video.

---

## Shorts Üretim Kuralları

> Detaylı plan: `11-DOCS/24_SHORTS_PRODUCTION_QUALITY.md`

### Altın Kural

**16:9 videodan 9:16'ya kırperken karakterler her zaman çerçevede kalmalı.**

### Kompozisyon Kuralları (16:9 Üretim Sırasında)

| Kural | Değer |
|-------|-------|
| **Güvenli bölge** | 16:9'un ortasındaki %60 |
| **Karakter pozisyonu** | Güvenli bölge içinde |
| **Kenar bölgeler** | Sadece arka plan (karakter yok) |
| **Metin/altyazı** | Güvenli bölge dışında, sonra eklenebilir |

### Güvenli Bölge Haritası

```
16:9 Video (1920×1080)
┌─────────────────────────────────────┐
│  Tehlikeli  │  GÜVENLİ  │ Tehlikeli │
│   Bölge    │   BÖLGE   │  Bölge   │
│  (kayıp)   │  (kalır)  │ (kayıp)  │
└─────────────────────────────────────┘
         ↓ Kırpma
    9:16 Video (1080×1920)
    ┌───────────┐
    │ GÜVENLI   │
    │  BÖLGE    │
    │ (tamamı)  │
    └───────────┘
```

### Shorts Üretim Adımları

1. **Shot listesi oluştur** — Hangi sahneler shorts için uygun?
2. **Kompozisyon planı** — Karakter pozisyonları güvenli bölgede mi?
3. **Çift üretim** — Hem 16:9 hem 9:16 için üret (mümkünse)
4. **Kalite kontrolü** — Her formatta karakter görünür mü?

### Shorts Kontrol Listesi

- [ ] Karakter her zaman çerçevede mi?
- [ ] Arka plan dikey formata uygun mu?
- [ ] İlk 3 saniye dikkat çekici mi?
- [ ] Metin/altyazı okunabilir mi?
- [ ] Kalite düşüşü var mı?

---

## Shot Dosyası Format Standardı (v1.0)

> S01E12 üretiminden çıkarılan kalıcı standart. Tüm yeni shot dosyaları bu formata uymalıdır.

### Zorunlu Bölümler

> **Üretim Kuralı:** Bir bölüm için SADECE OpenArt prompt dosyaları oluşturulur.
> Başka production dosyası oluşturmaya gerek yoktur. Shot markdown dosyaları zaten mevcuttur.

Her shot markdown dosyası şu bölümleri içermelidir:

1. **Scene Context** — Episode, Shot numarası/süresi, Location, Characters, Time of Day
2. **Purpose** — Shot'ın kısa amacı (1 cümle)
3. **Production Mode** — Fresh reset veya linked continuity chain sırası
4. **Clean Start State** — Pozisyon, yön, scale, kamera, anchor ve duygu
5. **Complete Main Action** — Aynı shot içinde başlayıp biten tek ana aksiyon
6. **Completed End State** — Tüm büyük hareket bittikten sonraki kesin görsel durum
7. **Stable Final Anchor** — Son 1–2 saniyelik doğal, grounded hold
8. **Next-Shot Dependency** — NONE / LIMITED / EXACT (exact ise gerekçeli)
9. **Continuity** — Yalnız gerekli görsel/hikâye sürekliliği
10. **Clean Start-Frame Continuity** — Production Mode'a göre fresh veya linked @image1
11. **World Reference** (Shot 01 ve quality-reset shot'ları için)
6. **Background Object Lock** — Arka plan sabitliği
7. **Visual Prompt** — OpenArt prompt'u ({style} {camera} {lighting} ile biter)
   - Shot 01: "CRITICAL: Maintain warm golden autumn colour saturation throughout the entire video" içermeli
   - Tüm shot'lar: clean `@image1` kompozisyonunu ve canonical World identity'yi korumalı
8. **Camera Direction** — Kamera yönü
9. **Dialogue** — 3 satır dialog (her shot'ta)
10. **Shot Breakdown** — Zaman dilimleri (0-3, 3-6, 7-10, 11-15)
11. **Natural Character Motion Rule** — Hareket kuralları
12. **Sound** — Ses tasarımı
13. **Voice Rule** — Ses kuralı (her speaking shot için zorunlu)
14. **Lighting** — Aydınlatma
14. **Colour / Contrast Stability** — Renk/kontrast sabitliği
15. **Negative Prompt** — Yasak listesi
16. **QA Checklist** — Kalite kontrol listesi

### Clean Start-Frame Continuity Bölümü (Tüm Shot'lar İçin Zorunlu)

```text
## Frame-to-Video Continuity

Production Mode: [FRESH QUALITY-RESET SHOT / LINKED CONTINUITY SHOT 1 / LINKED CONTINUITY SHOT 2 / LINKED CONTINUITY SHOT 3 — EXCEPTIONAL MAXIMUM]
@image1 = [fresh canonical shot-specific start / approved linked generated final frame].
For a fresh reset, rebuild from canonical World and character references at the highest reliable quality.
For a linked shot, verify the source frame and chain count before use.
First visible frame must match @image1.
Do not use failed or visibly degraded frames.
Do not redesign, recompose, widen, zoom, or reset the environment.
Keep all trees, paths, leaves, ground, lighting, and character positions consistent with @image1.
Locked camera only.
No pan, tilt, zoom, push-in, pull-back, tracking, reframe, camera reveal, or angle change.
Complete the main action inside this shot. Settle the camera and all major movement before the final 1–2 seconds.
```

### Camera Direction Kuralı

- **Shot 01**: Kendi camera direction'ı serbest (medium shot, static, vb.)
- **Tüm shot'lar**: kendi onaylı clean @image1 kompozisyonuna kilitli:

```text
Begin from the approved clean @image1 with the same camera angle, framing, lens feeling and composition. Locked camera. No zoom, reframe, widen, close-up reset or angle change.
```

Clean anchor onayından sonra kullanılamaz:
- Close-up
- Medium wide
- Medium close-up
- Wide shot (yeni kompozisyon olarak)
- Yüzde bazlı boyut hedefleri (25-30% of frame vb.)

### Colour / Contrast Stability Bölümü (Tüm Shot'lar Zorunlu)

#### Shot 01 — Baseline Version (İlk shot, önceki frame yok)

```text
## Colour / Contrast Stability

Establish the episode baseline look.

Use a soft pastel preschool look.
Use medium-low contrast.
Use warm sunlight / golden light.
Use gentle warmth.
Use soft shadows.
Use matte handcrafted toy-set materials.

Do not make the first shot overly saturated.
Do not make the colours too intense, neon, or heavy.
Do not add HDR effect.
Do not add extra sharpening.
Do not add glossy plastic highlights.
Do not create harsh shadows.
Do not brighten highlights into a blown-out look.
Do not make dark areas deep, cave-like, or high-contrast.

The first shot should feel soft, calm, warm, matte, and preschool-safe.
It must establish a gentle visual baseline for the whole episode.

Never make the first shot stronger, sharper, glossier, darker, more saturated, or more contrasty than the soft Pompom Hills preschool style.
```

#### Tüm Shot'lar — Clean @image1 Colour Stability

```text
## Colour / Contrast Stability

This shot begins from @image1, its separately approved clean start-frame still.

Match @image1 for lighting, colour temperature, softness, exposure, shadow level, material feel, and overall atmosphere.

Preserve the soft pastel preschool look.
Preserve medium-low contrast.
Preserve warm sunlight / golden light.
Preserve gentle warmth.
Preserve soft shadows.
Preserve matte handcrafted toy-set materials.

Do not intensify the previous frame.
Do not increase contrast.
Do not increase saturation.
Do not decrease brightness.
Do not make the scene darker than @image1.
Do not add HDR effect.
Do not add extra sharpening.
Do not add glossy plastic highlights.
Do not create harsher shadows.
Do not brighten highlights into a blown-out look.
Do not make dark areas deeper, heavier, or more cave-like.
Do not make the colours more orange, red, neon, or intense than @image1.
Do not make the scene look more cinematic, dramatic, glossy, or high-energy than @image1.

CRITICAL: Video generation models tend to darken frames and increase contrast with each shot. This MUST NOT happen. Match @image1 EXACTLY for brightness, colour temperature, and saturation. The previous shots (S01E12) showed brightness dropping from 109 to 97 to 93 — this pattern must be prevented.

If any visual adjustment happens, it must move slightly softer, calmer, warmer, and more matte — never stronger, sharper, glossier, darker, more saturated, or more contrasty.
```

### Colour Retention Rule (Video Generation)

> Video üretim modelleri frame-to-frame geçişte renk doygunluğunu düşürme ve karanlaştırma eğilimindedir.
> S01E12'de her shot'ta parlaklık düştü (109 → 97 → 93). Bu kural bunu engeller.

### @image2 Shot 1 Colour Reference (Kalıcı Çözüm)

> `@image1` her shot'ın ayrı onaylanmış clean start still'idir. `@image2` bölümün ayrı
> onaylanmış clean Episode Colour Master'ıdır; ikisi de video frame'i değildir.

```text
Use @image2 = EPISODE_COLOR_MASTER.png (the approved clean episode colour still).
@image2 is the colour, brightness, and contrast reference for the entire episode.
Use @image2 ONLY for colour, brightness, contrast, saturation, shadow softness, and matte material feel.
Do not use @image2 for composition, layout, character position, or camera angle.
If @image1 does not match the approved colour baseline, reject/regenerate the still or let
@image2 control colour while @image1 controls composition.
```

### Colour Retention Rules

```text
The first frame sets the warm colour baseline. During video generation:
- Preserve the exact same warm tones from first frame to last frame
- Preserve the exact same brightness level from first frame to last frame
- Do not let colours drift toward gray, brown, cool, or desaturated
- Do not let warm sunlight fade or become neutral
- Do not decrease brightness — the frame must NOT become darker than the first frame
- Do not increase contrast — the frame must NOT become more contrasty than the first frame
- If colours begin to drift, correct them back to the warm baseline
- If brightness begins to drop, correct it back to the baseline level
- CRITICAL: Use @image2 (Shot 01 frame) as the colour brightness and contrast reference. If the frame becomes darker than @image2, correct it back to @image2's level.
- The video must feel like a continuous warm scene, not a desaturated or darkened version
```

### QA Checklist Standart Maddeleri

#### Shot 01 — Baseline QA (İlk shot)

```text
- [ ] Establishes soft pastel autumn baseline
- [ ] Medium-low contrast
- [ ] No oversaturation
- [ ] No HDR / glossy / oversharpened look
- [ ] No harsh shadows or blown highlights
- [ ] Autumn colours are warm and gentle, not intense orange/red/neon
- [ ] Overall look is matte, calm, and preschool-safe
- [ ] Warm golden colour baseline established for video generation
```

#### Tüm Shot'lar — Clean Anchor Continuity QA

Her shot 02-12 QA checklist'ine şu 11 madde eklenmelidir:

```text
- [ ] Camera framing matches @image1; no new close-up/wide reset
- [ ] First visible frame matches @image1
- [ ] No sudden new character pop-in
- [ ] No character disappears suddenly from the approved clean start still
- [ ] Colour and lighting match @image1
- [ ] No contrast increase from previous shot
- [ ] No saturation increase from previous shot
- [ ] No HDR / glossy / oversharpened look
- [ ] No harsher shadows or blown highlights
- [ ] Autumn colours remain soft pastel, not intense orange/red/neon
- [ ] Overall look stays matte, warm, calm, and preschool-safe
- [ ] Warm golden colour baseline retained from @image1 throughout video
```

### Karakter Süreklilik Kuralları

#### Yeni Karakter Tanıtımı (Shot 02+)

Eğer bir karakter shot'ın başında görünmeliyse, clean `@image1` oluşturulurken canonical
reference ile doğru konum, ölçek ve kimlikte yerleştirilmelidir. Video içinde sonradan
girecekse:

1. İlk frame clean @image1 ile aynı olmalı
2. 1-2 saniye sonra yeni karakter mevcut sahede doğal şekilde görünmeli
3. "Already seated nearby" / "already visible in background" gibi ifadeler kullanılmalı
4. "Not a sudden pop-in" / "not appearing from nowhere" ifadeleri negatif prompt'a eklenmeli
5. Kamera reframe yapmamalı, yeni establishing shot olmamalı

#### Prop / Nesne Süreklilik Kuralı

> Prop durumu her shot'ın ayrı onaylanmış clean start still'inde doğru kurulmalıdır.

Bir shot'ta @image1'de görünmeyen bir prop/nesne (yaprak, taş, çiçek, oyuncak vb.) ilk karede aniden beliremez:

1. İlk frame @image1 ile aynı olmalı (prop henüz elde değilse, elde değildir)
2. Prop'u kazanma/kavrama eylemi ilk 1-3 saniyede olmalı
3. "Reaches for and catches" / "picks up" / "finds" gibi eylem fiilleri kullanılmalı
4. "Holds [object]" / "carrying [object]" gibi pasif ifadeler KULLANILMAZ (eğer @image1'de zaten elde değilse)
5. Visual Prompt'ta "First visible frame matches @image1" denilmeli, sonra prop kazanma eylemi gelmeli

Örnek — Yanlış:
```
Kiko holds a golden leaf in her hands...  (ama @image1'de elinde yok!)
```

Örnek — Doğru:
```
First visible frame matches the approved clean shot-specific start still — Kiko reaching for leaf.
She catches it gently in both hands. She holds it, looking at it...
```

#### Karakter Ön Hazırlık (Clean Still Staging) Kuralı

Bir sonraki shot'ta yeni bir karakter görünecekse onu önceki videoya zorla ekleme. Yeni
shot'ın clean start still'ini canonical World ve approved character references ile ayrı
üret; karakteri hikâyeye uygun, doğru ölçekli ve grounded biçimde bu temiz kompozisyonda
kur. Böylece pop-in önlenirken önceki videonun bozulması yeni shot'a taşınmaz.

#### Opa Görünürlük Kuralı (Voice-First Approach)

> S01E12 final lesson: @image1'de Opa görünmüyorsa, Opa ilk karede GÖRÜNMEMELİ.

Eğer @image1'de Opa görünmüyorsa:
1. Opa ilk karede aniden belirmemeli
2. Opa sadece ses olarak duyulmalı (voice-only)
3. Kiko sesin geldiği yöne dönmeli
4. Opa sadece sonraki karelerde, mevcut saheden doğal şekilde görünmeli
5. Eğer kamera hareketi olmadan Opa gösterilemiyorsa, bu shot'ta Opa sadece ses olmalı
6. Opa asla "suddenly appearing" / "already seated" olarak ilk karede olmamalı

#### Arka Plan Karakter Kullanımı

Bir karakter arka planda小small ve sessiz kalıyorsa:
- "background-only" / "small and non-dominant" olarak tanımlanmalı
- Dialog almamalı
- Saheden küçük olmalı
- @image1'de görünüyorsa first frame'de kalmalı

#### Kanat/Kol Tutma Kuralı (Kuş Karakterler İçin)

Kiko gibi insan karakterler kuş karakterlerin kanadını tutarsa:
- Kanat her zaman "owl-like and feathered" / "feathered wing" olarak tanımlanmalı
- "Like an arm" / "curved like an arm" KULLANILMAZ
- Negative prompt'a eklenmeli: "human hand on [character], arm-like deformation, [character] with human arms, extra limb"
- QA checklist: "Kiko holds only the soft edge/tip of [character] feathered wing — not hand, not arm, not extra limb"

### Pompom Items Görsel Prompt Kuralı

Bir shot'ta Pompom Item (Ball, Flower, Cloud, Leaf, Stone, Star, Raindrop) kullanılıyorsa:

1. Visual Prompt'ta item'ın kayıtlı specs'i kullanılmalı (bkz. `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/POMPOM_ITEMS/`)
2. Item'ın OpenArt keyword'leri Visual Prompt'a eklenmeli
3. Renk kodları kayıtlı spec'e uygun olmalı
4. Negative prompt'a item'ın yasak özellikleri eklenmeli (örn. Leaf için: "realistic leaf, pointed leaf, leaf veins, wilting leaf")
5. QA checklist'e item kontrolü eklenmeli (örn. "Leaves are fluffy Pompom Leaves")

Örnek — Pompom Leaf kullanımı:
```text
Visual Prompt: '...fluffy plush Pompom Leaf (soft round cotton-like leaf, autumn gold #FFCC80, no veins, soft edges)...'
Negative Prompt: '...realistic leaf, pointed leaf, leaf veins, leaf texture, wilting leaf, dry leaf, dead leaf, sharp leaf edges...'
QA: '- [ ] Leaves are fluffy Pompom Leaves (round, cotton-like, no veins)'
```

## OPENART PROMPT CHARACTER LIMIT RULE

### Limit

18 Temmuz 2026 tarihli gerçek OpenArt video alanı testi, ana video alanında **5.200 karaktere
kadar** paste-ready payload kabul edildiğini gösterdi. Bu resmi belgelenmiş platform limiti
değil, üretimde gözlemlenen proje sınırıdır ve OpenArt arayüzü değişirse yeniden ölçülmelidir.

Zorunlu üretim sınırı:

```text
Complete OpenArt paste-ready payload <= 5,200 characters
Preferred target: 4,500-4,900 characters
```

Sayaç, OpenArt ana video prompt alanına gerçekten yapıştırılan **tüm metni** kapsar: dosya
başlığı, production metadata, reference map, start-frame notu, ana prompt, diyalog, voice,
lip-sync ve sound instruction; boşluklar, noktalama ve satır sonları dahil.

Uzun Negative Prompt ayrı OpenArt alanına girilir ve 5.200 karakterlik ana alan sayacına dahil
edilmez. Bilinen en yüksek-riskli hatalar için kısa bir `AVOID:` satırı ana payload'ın sonunda
kalabilir. Ayrıntılı liste ayrı `*-negative-prompt.txt` dosyasında tutulur.

Şunlar paste-ready payload'a konmaz:

- Internal QA Checklist
- tekrarlanan `Exact Dialogue Script`
- tekrarlanan `Audio Direction`
- OpenArt Settings ve production/editing notes
- acceptance checklist ve açıklamalar
- Negative Prompt

5.200 karakter hiçbir paste-ready export dosyasında aşılamaz.

### Zorunlu Dosya Yapısı ve Workflow

Her mevcut ve gelecekteki OpenArt video export dosyası üretime alınmadan önce:

1. Ayrıntılı internal production document hazırlanır.
2. OpenArt export dosyası yalnızca tek seferde ana video alanına yapıştırılacak payload'ı
   içerir; internal QA tekrarları bu export'a kopyalanmaz.
3. Negative Prompt ayrı `*-negative-prompt.txt` dosyasına yazılır.
4. Export dosyasının **tamamı**, ilk karakterden son satır sonuna kadar `wc -m` veya eşdeğer
   Unicode karakter sayacıyla ölçülür.
5. Tam toplam 5.200 veya altında tutulur; 4.500-4.900 tercih edilir.
6. Sayaç 5.200'ü geçiyorsa dosya production-ready sayılmaz. Tekrarlı ifade internal belgeye
   taşınır; kritik continuity, action, exact dialogue, voice/lip-sync, sound veya camera
   kontrolleri silinmez.

### Compression Priority

Önce korunacak kontroller:

- `@image1` continuity ve exact first-frame match
- camera lock
- character ve object persistence
- no character/object pop-in
- no disappearance veya position jump
- shot'ın ana aksiyonu ve exact dialogue
- same approved saved voice
- colour/contrast stability
- gerektiğinde no music

Önce sıkıştırılacak veya pasted prompt dışına taşınacak içerik:

- tekrarlı açıklamalar ve nedenler
- duplicate negative terms
- uzun stil tarifleri
- QA dili
- OpenArt arayüzünden kontrol edilen ayarlar
- tekrarlanan kamera, ışık ve voice açıklamaları
- ana timeline'da zaten bulunan ayrı Exact Dialogue Script / Audio Direction tekrarları

Karakter limiti hiçbir zaman kritik continuity kuralı silinerek çözülmez. Tercih edilen
kompakt kalıplar:

```text
locked camera; no reset/reframe/movement
no pop-in, disappearance, duplication, or position jump
same bright warm soft matte look; no darkening/HDR/colour drift
same approved saved voice
natural ambience only; no music
```

### Negative Prompt

- Uzun liste ana video payload'ına birleştirilmez; ayrı OpenArt Negative Prompt alanına yapıştırılır.
- Ana payload'ın sonunda yalnızca kısa, shot-specific yüksek-risk `AVOID:` satırı kalabilir.
- Ayrı `*-negative-prompt.txt` dosyasında tutulur.
- Yüksek riskli failure term'ler önceliklendirilir.
- Ana promptta yeterince açık olan kural, bilinen tekrarlayan bir üretim hatası değilse
  negative promptta yinelenmez.
- Generic quality terimleri yerine gerçek production failure'ları öncelik alır.

### Internal QA Checklist

Tam ayrıntılı kontroller internal dokümanda korunur. Checklist OpenArt'a yapıştırılmaz ve
5.200 karakterlik paste-ready payload sınırına dahil edilmez.

Bu kural tüm mevcut ve gelecekteki Pompom Hills OpenArt video export payload'larına uygulanır.
Uygulama sırasında story content, dialogue, character canon veya shot intent değiştirilmez.

---

# Mandatory Dialogue Embedding and Audio Failure Prevention Rule

This rule applies to every OpenArt video shot containing spoken dialogue.

## Core Rule

OpenArt may ignore dialogue that exists only in a separate Markdown `Dialogue` section, timing table, production note or screenplay section.

Therefore, for every shot containing speech:

1. Every exact spoken line must appear directly inside the actual OpenArt-facing `Video Prompt`.
2. Each embedded line must include:
   - speaker name
   - exact dialogue wording
   - approximate timing
3. A separate `Dialogue` section may still exist for documentation, but it must never be the only location containing the dialogue.
4. Never approve a video prompt when the dialogue exists only outside the actual `Video Prompt`.

## Mandatory Priority Block

Every OpenArt Video Prompt containing dialogue must begin with a strong audio-priority block similar to:

`SPOKEN DIALOGUE IS MANDATORY. Generate every dialogue line exactly as written below using the manually assigned saved character voices. Do not omit, shorten, replace, reorder or paraphrase any line. Dialogue must begin within approximately the first 0.4–0.6 seconds. If speech generation fails, do not replace speech with music or silent staring.`

Immediately follow it with:

`ABSOLUTELY NO MUSIC, background music, melody, song, humming, percussion, soundtrack, instrumental audio, magical chimes or cinematic audio.`

The no-music instruction must appear near the beginning of the Video Prompt, not only in settings or the Negative Prompt.

## Dialogue Embedding Format

Inside the actual Video Prompt, include lines in this form:

`0.4–1.6 Kiko says: "Exact line."`
`2.1–3.3 Mimi says: "Exact line."`

Do not rely only on Markdown tables that OpenArt may not process.

Every required line must be repeated directly in the prompt field that is pasted into OpenArt.

## Character Voice Rule

For every speaking shot:

- Kiko → manually select the approved saved Kiko voice
- Mimi → manually select the approved saved Mimi voice
- other characters → manually select their approved saved canonical voices
- Auto Voice: Off
- Generated Dialogue: On
- Generated Audio: On
- Spoken Language: correct episode language
- Music: Off

Written instructions inside a file do not activate OpenArt interface settings automatically.

Before every generation, manually confirm in the OpenArt interface that:

1. every required saved voice is selected
2. Auto Voice is Off
3. Generated Dialogue is On
4. Generated Audio is On
5. Music is Off

Do not approve production readiness based only on what the Markdown file says.

## Lip-Sync Rule

- Only the assigned speaker moves its mouth.
- Every listener keeps a relaxed closed mouth.
- No two characters move their mouths simultaneously unless overlap is intentionally scripted.
- No wrong-character lip-sync.
- No voice swapping.
- No silent mouth movement.
- No spoken line may be assigned to the wrong character.

## Silence and Timing Rule

For every 15-second preschool shot:

- first spoken line begins within approximately 0.4–0.6 seconds
- normal gaps between lines should usually be approximately 0.4–0.7 seconds
- no unmotivated silence may exceed 1.0 second
- do not compress all dialogue into the first 8–10 seconds and leave a long final hold
- final seconds must contain a purposeful reaction or motivated micro-action
- biting, chewing, swallowing, reaching or object handling may create longer non-speaking sections only when the action is visibly motivated
- no silent staring
- no frozen listening pose
- no unexplained dead air

## Music-Failure Prevention

If OpenArt cannot generate the requested dialogue:

- it must not substitute music
- it must not substitute humming
- it must not create instrumental background audio
- it must not fill the shot with silent staring
- it must not remove the spoken lines

Add these terms near the beginning of every relevant Negative Prompt:

`missing dialogue, omitted line, shortened dialogue, paraphrased dialogue, silent characters, silent staring, no speech, speech replaced by music, background music, instrumental music, melody, song, humming, percussion, soundtrack, wrong voice, voice swapping, wrong-character lip-sync, both mouths moving, overlapping dialogue`

## Mandatory Pre-Production QA Gate

A dialogue shot must be marked `NOT READY` if any of the following is true:

- dialogue appears only in a separate Dialogue section
- exact lines are absent from the actual Video Prompt
- "spoken dialogue is mandatory" is missing
- no-music instruction appears only in settings
- voice selection is assumed rather than manually confirmed
- the first line begins too late
- dialogue ends too early and leaves a long inactive hold
- there is unmotivated silence longer than 1.0 second
- speaker and listener mouth rules are missing
- OpenArt can interpret the shot as silent acting instead of spoken dialogue

Do not give APPROVE merely because:

- the screenplay contains enough lines
- the dialogue table looks complete
- the OpenArt Settings section says dialogue is On
- the file says Music Off
- the timing mathematically fits 15 seconds

Approval requires that the instructions are executable by OpenArt from the actual pasted Video Prompt.

## Mandatory Post-Generation QA

After generation, reject the result if:

- any required line is missing
- any line is shortened or paraphrased
- the wrong voice is used
- characters only stare at each other
- music appears
- the wrong character moves its mouth
- both mouths move together
- dialogue starts too late
- there is unexplained dead air
- the final section becomes a frozen hold

A failed dialogue generation must never be used as a continuity source for the next shot.

## Approval Language

For every dialogue-video review, explicitly check and report:

- exact number of required lines
- whether every line is embedded in the Video Prompt
- first spoken-line time
- longest non-speaking interval
- whether that interval contains motivated action
- whether saved voices must be manually selected
- whether music is strongly prohibited
- final verdict: APPROVE or NOT READY

---

*Bu belge tüm shot'lar için tek kaynaktır.*
*Versiyon: 5.9 — Mandatory Dialogue Embedding and Audio Failure Prevention Rule eklendi*
