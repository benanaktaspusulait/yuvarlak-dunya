# 17 — Video Generation Standard

> Tüm shot dosyaları bu standarttan üretir.
> Her shot bu dosyaya atıfta bulunur, aynı kuralları tekrar etmez.
> Pacing, hook, camera-emphasis and ending style (retention) decisions are defined in
> `00-CORE/18_VIDEO_STYLE_AND_RETENTION_STANDARD.md` — that document does not override the
> continuity/technical rules below (e.g. Camera Rules, Text Safety), it builds on top of them.

---

## Production Pipeline

Gerçek üretim akışı:

```
Shot 01 Image
    ↓
Frame to Video
    ↓
Shot 01 Video
    ↓
Shot 02 (Video Reference: Shot 01 Video)
    ↓
Shot 02 Video
    ↓
Shot 03 (Video Reference: Shot 02 Video)
    ↓
...devam eder
```

---

## First Frame Continuity

Shot 01 uses the approved original first-frame still.
Shot 02 and onward use the previous shot as the Video Reference.
If a still continuity frame is used, it must be the exported/downloaded original frame, not a screenshot.

The opening frame of each continuation shot should continue seamlessly from the previous shot reference.

The opening frame must continue seamlessly from the previous shot video reference or exported continuity frame. The viewer should not perceive a shot boundary.

Maintain:
- character position
- camera height
- framing
- lighting
- colour grading
- world identity

---

## Voice Continuity

The speaking voices MUST remain identical across the whole episode.

Maintain:
- same voice identity per character
- same pitch
- same timbre
- same speaking speed
- same warmth
- same preschool naturalness

Do not generate a narrator.
Do not generate alternate voices.

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
- exported original video frame
- exported final frame from the previous shot
- approved production stills from the asset folder

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

Continuation shots must use two forms of reference:

1. Previous Shot Reference
   Purpose:
   - action continuity
   - character position
   - camera continuity
   - motion continuity

2. Episode Colour Master
   Purpose:
   - colour stability
   - white balance stability
   - exposure stability
   - saturation stability
   - preventing generational colour drift

Do not let each shot rebalance colour from the previous generated shot alone.

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

The previous video reference alone is not enough to guarantee exact location continuity.

The AI may understand the general environment but place the characters in a similar, incorrect area.

Therefore every continuation shot must explicitly restate the physical location using environment anchors.

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

Do not let the AI infer the location from the previous video reference alone. Always describe the local physical environment in the shot prompt.

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
6. Does the final frame support the next shot?

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
1. Previous final frame match
2. Existing character position and scale
3. Background object lock
4. Entering character visibility
5. Entrance path clarity

The entering character's movement is secondary to continuity.

### No Pull-Back Continuity Rule

When a shot continues from a locked previous final frame, the new shot must not begin wider than the previous frame.

Never pull back at the beginning of a continuation shot in order to introduce a character.

Do not reveal more environment, more sky, more side objects, or additional props at the first frame.

If the entering character cannot be shown without widening or recomposing the frame, the entering character should begin already partially visible at the frame edge.

Priority:
1. Previous final frame match
2. No wider reset
3. No new object reveal
4. Entering character visibility

Global QA for continuation shots:
- [ ] Continuation shot does not begin wider than previous final frame.
- [ ] No pull-back occurs at shot start.
- [ ] No new side objects are revealed at first frame.
- [ ] Entering character adapts to the locked frame instead of forcing recomposition.

### No New Character In First Frames Rule

When a shot continues from a locked previous final frame using `@image1`, no new character may appear, enter, or begin entering during the first 2 seconds of the shot.

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

Continuity Reference:
Previous shot video reference or exported final frame.

Previous Shot: Use the previous shot as Video Reference.
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

*Bu belge tüm shot'lar için tek kaynaktır.*
*Versiyon: 4.1 — Shorts Üretim Kuralları Eklendi*
