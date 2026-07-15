# 17 — Video Generation Standard

> Tüm shot dosyaları bu standarttan üretir.
> Her shot bu dosyaya atıfta bulunur, aynı kuralları tekrar etmez.
> Pacing, hook, camera-emphasis and ending style (retention) decisions are defined in
> `00-CORE/18_VIDEO_STYLE_AND_RETENTION_STANDARD.md` — that document does not override the
> continuity/technical rules below (e.g. Camera Rules, Text Safety), it builds on top of them.

---

## SHOT COMPLETION AND QUALITY RESET RULE — HIGHEST CONTINUITY PRIORITY

This section overrides every older instruction in this repository that says to use a
generated video, a raw video frame, a corrected video frame, a normalized video frame,
or the previous shot's exported final frame as the next shot's production anchor.

### Clean Anchor Definitions

- **Clean start-frame still:** a separately generated, visually reviewed and approved
  production still created from the canonical approved World, approved character identity
  references and a shot-specific composition. It is not extracted from video.
- **Clean end-frame still:** a separately generated, visually reviewed and approved
  production still defining the intended completed state of a shot. It is not extracted
  from video.
- **Linked shots:** shots whose approved clean end/start still is intentionally shared.
  The approved clean end still of Shot N becomes the exact same approved clean start still
  of Shot N+1. This does not permit extracting that still from generated video.

RAW GENERATED FINAL-FRAME CHAINING IS FORBIDDEN.

Never use a frame extracted directly from an AI-generated video as the next shot's
production anchor. Normalizing, correcting, grading, upscaling or exporting a generated
video frame does not turn it into a clean production still.

Every shot must use a separately approved clean start-frame still. Whenever the tool and
shot design support it, every shot must also use a separately approved clean end-frame
still through Start Frame + End Frame mode. Video generation creates motion only between
these approved still anchors. It must not redefine camera, world quality, character scale,
colour, lighting, sharpness or final-frame composition.

### Complete Action Inside Each Shot

Every shot must contain a complete visual action. Do not end a shot while a character is
walking, entering, turning, pointing, jumping, landing, reaching, gesturing, visibly
breathing or changing position. Every scripted action must begin, develop and finish
inside the same shot.

The final 1–2 seconds must show a stable, natural and fully grounded ending pose. Camera
movement must also finish and settle before the shot ends. The next shot must not require
instructions such as “continue walking,” “resume the previous movement,” “complete the
previous gesture,” or “continue exactly where the character stopped mid-motion.”

### Fresh Shot Default

Start each new shot as a fresh highest-quality generation using:

- the canonical approved World,
- approved character identity references,
- a clean shot-specific starting composition,
- and the highest approved quality settings.

Preserve story continuity through character placement, screen direction, world identity,
dialogue, sound and editing. Pixel-exact video continuation is not the default. A clean
editorial cut between two high-quality independent shots is preferred over a seamless
transition between progressively degraded shots.

### Exact Clean-Anchor Continuity Limit

Use exact linked clean anchors only when the story or edit genuinely requires them.

- Normal maximum: 2 consecutive linked shots.
- Exceptional maximum: 3 consecutive linked shots.
- After 2–3 linked shots: mandatory visual quality reset from canonical clean references.
- Never create a 4-shot, 5-shot or 6-shot recursive frame chain.

At a reset:

```text
Canonical approved World
+ approved character references
+ clean shot-specific composition
→ fresh highest-quality shot
```

When exact frame continuity conflicts with visual quality, character identity,
environment fidelity, correct scale or clean composition, visual quality wins.

### Post-Production Timing

Keep production-generation anchors clean and ungraded. Perform video upscaling and final
episode-wide colour matching only once, after all shots are completed and approved. Do not
upscale or repeatedly colour-normalize intermediate frames for reuse as generation inputs.

### Legacy Wording Interpretation

Until all historical shot packages are migrated, any older reference to `@image1`,
“previous final frame,” “exported continuity frame,” “normalized final frame” or “previous
shot video reference” must not be followed literally. Replace it with one of these:

1. the separately approved clean start-frame still for the current shot; or
2. when exact linkage is justified and within the 2–3 shot limit, the separately approved
   clean end still of Shot N, reused unchanged as Shot N+1's clean start still.

Generated video media remains review evidence and edit material only; it is never a
production-anchor source.

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
> Ham frame'ler asla @image1 olarak kullanılmamalıdır.

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
- Bu frame hiçbir sonraki shot'ın `@image1`'i veya production anchor'ı olamaz

### Temel Kural

```
Approve clean start/end stills → Generate motion → Complete and approve all shots → One final episode-wide upscale and colour-match pass

ASLA: Ham, düzeltilmiş veya normalize edilmiş video final frame'ini @image1 olarak kullanma.
SADECE: Ayrı üretilmiş ve onaylanmış clean start-frame still kullan.
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
ASLA ham, düzeltilmiş veya normalize edilmiş bir video final frame'ini bir sonraki @image1
olarak kullanma. SADECE ayrı onaylanmış clean start-frame still kullan.
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

Every shot uses its own separately approved clean start-frame still. The default is a fresh
shot-specific composition from canonical references, not the previous shot video.

When exact linkage is necessary, reuse only the separately approved clean end still of the
previous shot as the exact clean start still of the next shot, within the 2–3 shot limit.
Never use a frame extracted from generated video. A clean editorial cut is acceptable.

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

Match the colour grading of the previous shot exactly.

The previous shot is the colour master reference. Never rebalance colours between shots.

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
- Use the previous shot only for continuity of action and placement.
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

Preserve the lighting from the previous shot exactly.

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
3. **Continuity** — Önceki shot'tan devam edip etmediği
4. **Clean Start-Frame Continuity** (tüm shot'lar için zorunlu) — @image1 kuralları
5. **World Reference** (Shot 01 için) — İlk shot world reference kullanımı
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

@image1 = separately approved clean start-frame still for this shot.
Use @image1 as the only visual continuity source.
First visible frame must match @image1.
Do not use failed frames, generated videos or video-extracted frames as references.
Do not redesign, recompose, widen, zoom, or reset the environment.
Keep all trees, paths, leaves, ground, lighting, and character positions consistent with @image1.
Locked camera only.
No pan, tilt, zoom, push-in, pull-back, tracking, reframe, camera reveal, or angle change.
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

OpenArt'ın birleşik ana prompt + negative prompt alanı için gözlemlenen kabul sınırı yaklaşık
830 karakterdir; bu resmi belgelenmiş kesin bir platform limiti değildir.

Güvenli üretim sınırı:

```text
OpenArt Paste Prompt + Negative Prompt <= 800 characters
Preferred target: 700-780 characters
```

Sayaç; ana prompt, diyalog, voice instruction, sound instruction, negative prompt,
boşluklar, noktalama ve satır sonları dahil OpenArt'a gerçekten yapıştırılan tüm karakterleri
kapsar.

Şunlar OpenArt'a yapıştırılmadığı için sayılmaz:

- markdown başlıkları
- Internal QA Checklist
- OpenArt Settings
- production notes
- açıklamalar
- dosya başlığı

800 karakter, kullanıcı açıkça onaylamadıkça aşılamaz.

### Zorunlu Dosya Yapısı ve Workflow

Her mevcut ve gelecekteki `shot-XX-openart-prompt.md` dosyası üretime alınmadan önce:

1. Ayrıntılı internal production document hazırlanır.
2. OpenArt'a girecek metin ayrı bir `## OpenArt Paste Prompt` bölümüne konur.
3. Negative alanına girecek metin ayrı bir `## Negative Prompt` bölümüne konur.
4. Bu iki bölümün içerikleri, başlıklar hariç ve boşluk/noktalama/satır sonları dahil,
   birlikte sayılır.
5. Birleşik toplam 800 karakter veya altında tutulur; 700-780 tercih edilir.
6. Her dosyada, OpenArt'a yapıştırılmayan şu doğrulama satırı bulunur:

```text
OpenArt pasted character count: XXX / 800
```

7. Sayaç 800'ü geçiyorsa prompt approved/production-ready işaretlenmez. Tekrarlı ifade
   sıkıştırılır; kritik continuity korumaları silinmez.

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

- En fazla 15-20 yüksek riskli failure term kullanılır.
- Ana promptta yeterince açık olan kural, bilinen tekrarlayan bir üretim hatası değilse
  negative promptta yinelenmez.
- Generic quality terimleri yerine gerçek production failure'ları öncelik alır.

### Internal QA Checklist

Tam ayrıntılı kontroller internal dokümanda korunur. Checklist OpenArt'a yapıştırılmaz ve
800 karakter sınırına dahil edilmez.

Bu kural tüm mevcut ve gelecekteki Pompom Hills OpenArt video promptlarına uygulanır.
Uygulama sırasında story content, dialogue, character canon veya shot intent değiştirilmez.

---

*Bu belge tüm shot'lar için tek kaynaktır.*
*Versiyon: 5.6 — OpenArt Prompt Character Limit Rule eklendi (800 karakter güvenli sınır)*
