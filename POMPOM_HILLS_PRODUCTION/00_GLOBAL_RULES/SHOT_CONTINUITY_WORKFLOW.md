# Shot Continuity Workflow

> This is the practical per-episode application of the **SHOT COMPLETION AND QUALITY RESET
> RULE** in `00-CORE/17_VIDEO_GENERATION_STANDARD.md`. That section has priority over all
> historical final-frame and video-reference wording in this file.

---

## 1. Why This Exists

Earlier production used recursive final-frame chaining:

```
generated Shot 01 final frame → Shot 02 @image1 → Shot 03 @image1 → ...
```

That pipeline accumulated degradation and is superseded. The default is now independent,
highest-quality shot generation from canonical clean references. Exact generated-frame
continuity is allowed only for a pre-planned two-shot normal chain or three-shot exceptional
chain, and only while every linked frame passes visual QA.

---

## 2. The Standard Workflow

For every episode:

- World opening is optional pre-roll, not a story shot.
- Label every shot's Production Mode before generation and record the episode reset schedule.
- For fresh shots, create and approve a clean start-frame still from the canonical World,
  approved character references and a shot-specific composition.
- Whenever possible, create and approve a separate clean end-frame still and use Start
  Frame + End Frame mode.
- Complete every action inside its shot and reserve the final 1–2 seconds for a stable,
  grounded ending pose.
- Default to a clean editorial cut and a fresh highest-quality generation for the next shot.
- If exact linkage is necessary, use Shot N's generated final frame only after it passes
  identity, world, camera, colour, contrast, sharpness, scale and prop QA.
- Limit exact generated-frame linkage to 2 shots normally and 3 only exceptionally; then
  reset from canonical clean references.
- Create or update the per-episode Object Continuity Map before generating shot video.
- Check every first-frame still / cheap take against the Object Continuity Map before
  spending video credits.
- Watch the full video for intra-shot character continuity, not only first/final frames.
- Watch the full video again for hard background/object stability.
- Apply the Global OpenArt Continuity Locks from
  `00-CORE/17_VIDEO_GENERATION_STANDARD.md` to every generated shot.

This is deliberately short. It is the checklist version of §3-§5 below and of the fuller
rules already defined in `00-CORE/CONTINUITY_RULES.md` §9 (Reference Frame Workflow),
§9.1 (First Frame Master Lock) and §13 (Video Continuation Rules) — this document does not
override those, it is the per-episode application of them plus the world-opening step
that `00-CORE/CONTINUITY_RULES.md` does not cover.

---

## 3. World Opening → Shot 01

If the episode uses a world micro-opening (see
`POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/MICRO_OPENING_AND_CLOSING_STANDARD.md` §2B), treat
its approved final frame as the environment continuity reference for Shot 01 — not as the
Episode Colour Master. Shot 01 itself defines the Episode Colour Master once its own still
is approved.

### Character Introduction After Empty Opening
When the opening has no characters, Shot 01 must introduce the first character naturally using one of the approved methods from `00-CORE/17_VIDEO_GENERATION_STANDARD.md` § Character Introduction After Empty Opening Rule:
- Camera Reveal (Method A)
- Visible Character Entrance (Method B)
- First Frame Character Already Partially Visible (Method C)

Do not allow character pop-in or sudden appearance. The character must not suddenly spawn into the middle of the frame after an empty opening. See the global QA test in `11-DOCS/16_VIDEO_QA_SPEC.md` for rejection criteria.

The micro-opening is not part of the story duration and is not renumbered as `shot-00`
inside the episode's shot list (see `MICRO_OPENING_AND_CLOSING_STANDARD.md` §2B and the
S01E07 example at
`POMPOM_HILLS_PRODUCTION/02_WORLDS/STONE_HILL/03_OPENINGS/STONE_HILL_ADVENTURES_MICRO_OPENING/s01e07-preroll-reference.md`).

If the episode does not use a micro-opening, Shot 01 has no previous-shot reference at
all — it is a fresh take shot per `00-CORE/CONTINUITY_RULES.md` §9.

---

## 4. Shot N → Shot N+1 (the core rule)

For every shot after Shot 01, `@image1` follows the pre-planned Production Mode. By default
it is a fresh shot-specific composition generated from the canonical World and approved
character identity references.

Only when exact linkage is genuinely necessary may a QA-approved generated final frame of
Shot N become Shot N+1's start. This is limited to 2 linked shots normally and 3
exceptionally. The next shot then resets fresh even in the same location.

The first frame of the new shot should match `@image1` as closely as possible in:

- camera angle
- camera height
- lens feel
- framing
- character positions
- character scale
- background object positions
- world-specific locked landmark positions (e.g. pebble path / stone clusters for Stone
  Hill; whatever the equivalent locked elements are for the world in use)
- lighting
- colour grading
- exposure
- contrast

The new shot begins and completes its own main action. Preserve screen direction, character placement,
world identity, scale family and editorial logic, but do not continue unfinished movement.
A clean cut is acceptable and preferred when exact matching would reduce quality.

Practical rule of thumb: the first 1 second of a shot should visually hold close to
`@image1` before the shot's own action becomes noticeable. See
`POMPOM_HILLS_PRODUCTION/02_WORLDS/STONE_HILL/04_EPISODE_PACKAGES/S01E07_THE_ROUND_STONE/01_SHOTS/`
for five worked examples of this per-shot wording (Shot 02 through Shot 06).

The first second hold is also an intra-shot safety gate: no character may teleport,
switch sides, pop in, disappear, or change scale during that first second, and no visible
background object may move, disappear, duplicate, or change identity.

### Colour / Contrast Drift Control Rule

When a shot begins from its separately approved clean `@image1`, the visual style must not
become progressively more contrasty, saturated, sharp, glossy, HDR-looking or harsh during
the generated motion.

OpenArt sometimes increases:
- contrast
- saturation
- sharpness
- glossy plastic highlights
- HDR-like lighting
- harsh shadows
- blown highlights
- deeper dark areas
- over-polished CGI look

This must be prevented globally.

For every frame-to-video continuity prompt, include a Colour / Contrast Stability section:

```
Colour / Contrast Stability:
Use @image1 for continuity, first-frame composition, character positions, object layout and
action placement.
Use the Episode Colour Master for colour, brightness, contrast, saturation, shadow softness
and matte material feel.
If the production tool supports multiple image references, upload the Episode Colour Master
as @image2.
@image2 = Episode Colour Master only. Do not copy @image2 camera, framing, character
position, background layout, or action.
If @image1 has accumulated video-generation drift and is darker, harsher, sharper, glossier,
more saturated, or more contrasty than @image2, keep @image1 composition but correct colour
back toward @image2.
Preserve the soft pastel preschool look.
Preserve medium-low contrast.
Preserve warm morning dappled sunlight.
Preserve gentle golden warmth.
Preserve soft shadows.
Preserve matte handcrafted toy-set materials.
Do not increase contrast.
Do not increase saturation.
Do not add HDR effect.
Do not add extra sharpening.
Do not add glossy plastic highlights.
Do not create harsher shadows.
Do not brighten highlights into a blown-out look.
Do not make dark areas deeper or more cave-like.
Do not make the scene look more intense than @image1.
If any adjustment happens, it should be slightly softer and calmer, never stronger,
sharper, glossier, darker, or more contrasty.
```

OpenArt-facing prompt wording:

```
@image1 = separately approved clean start-frame still for the current shot.
@image2 = Episode Colour Master: [approved original Shot 01 still].

Use @image1 as the exact locked first frame and only composition/action continuity source.
Use @image2 only as the fixed colour, brightness, contrast, saturation, shadow softness,
and matte material reference.
@image1 controls first-frame composition, character positions, action continuity, and
object layout.
@image2 controls colour grade only. Do not copy @image2 camera, framing, character
position, background layout, or action.
If the clean @image1 differs from @image2, keep @image1 composition while matching the
approved episode colour baseline. Reject and regenerate a materially degraded clean still.
```

Add these terms to the global negative prompt for all OpenArt video prompts:

```
high contrast, contrast increase, overly saturated, saturation increase, HDR, HDR look,
glossy plastic, glossy CGI, harsh highlights, harsh shadows, blown highlights,
oversharpened, extra sharp, over-polished CGI, colour drift, exposure drift, saturation
drift, contrast drift, dark areas growing darker, highlights growing brighter, lighting
becoming harsher
```

Add this checklist item to every frame-to-video approval checklist:

```
- [ ] No contrast / saturation / HDR / glossy / oversharpened drift from @image1
- [ ] Colour, brightness, saturation and contrast match the Episode Colour Master
- [ ] @image1 is not allowed to intensify contrast over the Episode Colour Master
```

### Character Voice Lock Rule

Every character must use the same locked voice across all shots in an episode and across
the entire series. Voice changes between shots break immersion and confuse young viewers.

OpenArt and post-production voice assignment must follow these rules:

1. **One voice per character.** Each character has one locked Voice ID / voice reference
   that never changes.

2. **Voice IDs must be registered** in `08-PRODUCTION/VOICE_TRACKER.md` before production
   begins. No shot may be generated without a confirmed Voice ID for every speaking
   character.

3. **Every shot prompt must specify** the locked Voice ID for each speaking character.
   Never let OpenArt or any TTS system "choose" a voice.

4. **Voice identity includes:**
   - Same pitch
   - Same timbre
   - Same age impression
   - Same speaking speed
   - Same warmth
   - Same preschool energy
   - Same speaking rhythm
   - Same pronunciation
   - Same accent
   - Same recording quality

5. **Reference-based voice lock:** If the system supports voice reference, use the
   approved Shot 01 voice sample as the reference for every subsequent shot. Never
   generate a new voice mid-episode.

6. **Forbidden:**
   - Different narrator voice for the same character
   - Alternate voice or voice variant
   - Older/younger sounding replacement
   - Different performer feel
   - AI-generated voice that drifts from the registered voice
   - Any voice not registered in VOICE_TRACKER.md

Add this to every OpenArt shot prompt that has dialogue:

```
Voice Lock:
Each character must use their registered locked voice from VOICE_TRACKER.md.
Do not let OpenArt choose or generate voices.
Do not change voice between shots.
Same pitch, same timbre, same age, same speed, same warmth.
```

Add this checklist item to every approval checklist:

```
- [ ] Character voices match registered Voice IDs — no drift
```

### Pompom Items — World Signature Objects

Pompom Hills has a unique visual identity built around "Pompom" items — soft, round,
fluffy objects that appear across the world. Every episode must include at least one
Pompom item to reinforce the brand identity.

#### Pompom Item Catalog

| Item | Description | Used In |
|------|-------------|---------|
| Pompom Ball | Soft, fluffy, colorful bouncing ball | Play scenes, games |
| Pompom Flower | Round, fluffy flower with pastel petals | Flower Hill, nature |
| Pompom Cloud | Cotton-like fluffy cloud in the sky | Outdoor daytime scenes |
| Pompom Leaf | Round, fluffy leaf shape | Little Forest, autumn |
| Pompom Stone | Soft-looking rounded stone | Stone Hill |
| Pompom Star | Glowing round star | Night scenes |
| Pompom Raindrop | Round, soft raindrop shape | Rain scenes |

#### Rules

1. **Every episode must include at least 1 Pompom item** — either as a story object
   or as a background detail.
2. **Pompom items are always round, fluffy, and soft-looking** — never sharp, angular,
   or hard.
3. **Color palette:** pastel (pink, purple, orange, yellow, soft blue).
4. **Pompom items are friends, not enemies** — characters can touch, hold, and play
   with them.
5. **Pompom Ball** is the most common — used in play/game episodes with "find and
   bounce" themes.
6. **Pompom items may appear in background** if not the main story object, but must
   be visually identifiable as Pompom items (round + fluffy).
7. **No sharp edges, no hard textures, no realistic materials** on Pompom items.
   They must feel like soft toys.

Add this to episode planning checklists:

```
- [ ] At least 1 Pompom item included in the episode
```

### Hero View OpenArt Prompt Standard

Every world needs TWO separate prompt files for the hero view:

1. **Image Generation Prompt** (`03-openart-prompt.md`) — Creates the canonical hero view image
2. **World Builder Prompt** (optional, separate file) — Uses the hero view image to build 3D world

#### File 1: Image Generation Prompt (`03-openart-prompt.md`)

This is the PRIMARY prompt. It generates the canonical hero view image that becomes the
visual reference for all shots in that world.

**Required Sections (9 sections):**

1. **Opening Statement** — One sentence defining the image goal. Must state this is a
   "premium master world image" not a generic scene, poster, or concept board.

2. **Format and Composition** — Technical specifications:
   - Aspect ratio (16:9)
   - Camera height (child-eye, ~0.80m)
   - Lens feeling (35mm)
   - Composition type (ultra-wide establishing shot)
   - Depth layers (foreground → middle ground → horizon)
   - Readability and breathability requirements

3. **Primary World Identity** — What makes this world instantly recognisable:
   - Core identity description (2-3 sentences)
   - Key landmark or feature that defines the world
   - How it should feel as a location

4. **Environment** — Physical world details:
   - Ground cover (grass, path, stones)
   - Vegetation (flowers, trees, bushes)
   - Spatial qualities (open, dense, flat, hilly)
   - Differentiation from other worlds
   - Sky and horizon details

5. **Colour Direction** — Specific colour instructions:
   - Palette character (brighter, softer, warmer, etc.)
   - Specific colours to use
   - Relationship to Pompom Hills base palette
   - What to avoid (neon, harsh, oversaturated)

6. **Style** — Rendering and visual language:
   - Pompom Hills visual language reference
   - Quality level (high-quality preschool animation)
   - Material feel (matte, handcrafted, toy-like)
   - Lighting (warm morning, soft shadows)
   - Technical rendering rules (no HDR, no gloss, etc.)

7. **Mood** — Emotional atmosphere:
   - 3-5 mood descriptors
   - How children should feel when looking at it
   - What the scene should evoke

8. **Important Differentiation** — Explicit comparison to other worlds:
   - List 3-5 specific worlds it must NOT look like
   - State what it must NOT be (generic, theme park, poster, etc.)

9. **Forbidden** — Comprehensive negative list:
   - No text/labels/signs/logo
   - No characters/children/animals
   - No buildings/structures
   - No world-specific forbidden elements
   - No rendering issues (HDR, gloss, harsh shadows)

**Quality Checklist:**
- [ ] Opening statement defines premium quality
- [ ] Composition includes camera height, lens, aspect ratio
- [ ] World identity has unique landmark/feature
- [ ] Environment differentiates from other worlds
- [ ] Colour direction specifies palette and avoids
- [ ] Style includes all rendering rules
- [ ] Mood defines emotional atmosphere
- [ ] Differentiation lists specific worlds to avoid
- [ ] Forbidden list is comprehensive

#### File 2: World Builder Prompt (Optional)

Used only when building 3D world from the approved hero view image.

**Required Sections (8 sections):**

1. **Purpose** — This is only the OpenArt World Builder input guide
2. **World Builder Reality Check** — Honest limitations of the tool
3. **Required Input Method** — 1 Image Mode / 2-4 Image Mode instructions
4. **OpenArt Text Prompt** — Supplementary style hint (world-specific)
5. **Negative Prompt** — World-specific forbidden output
6. **Identity Lock** — MUST read as / MUST NOT read as
7. **Production QA After World Build** — Verification checklist
8. **Final Usage Note** — Reject and regenerate if quality fails

#### Forbidden Patterns

- ❌ No generic prompts without world-specific identity
- ❌ No prompts that could produce a different world
- ❌ No prompts with dominant animals/insects/characters
- ❌ No prompts allowing HDR, glossy, or harsh contrast
- ❌ No prompts without differentiation from other worlds
- ❌ No prompts without comprehensive forbidden list

Add this to world creation checklists:

```
- [ ] Hero view has image generation prompt (03-openart-prompt.md)
- [ ] Image prompt has all 9 required sections
- [ ] Image prompt differentiates from other worlds
- [ ] Image prompt includes comprehensive forbidden list
```
- [ ] Hero view openart prompt has all 8 required sections
- [ ] Text prompt includes world-specific identity elements
- [ ] Negative prompt includes world-specific forbidden elements
- [ ] Identity Lock defines what world MUST and MUST NOT read as
```

### Object Continuity Map Gate

Every episode that depends on persistent objects must maintain an Object Continuity Map
before video credits are spent.

The map lists, shot by shot:

- required objects from `@image1`
- optional objects to preserve if visible
- current action object
- usability checks
- forbidden object changes
- clean end-frame requirements for the current shot and, only when exact linkage is
  justified, the next shot's identical clean start still

A shot is not approved only because an object is mentioned in the prompt. A shot is
approved only if the required object is visible in `@image1` and usable for the planned
action at its existing size, shape, position, and distance.

Visible is not enough.

If the object is too small, too far away, too crowded, partly cropped, or not shaped for
the planned action, simplify the character action instead of changing the object.

Characters adapt to the environment.
The environment does not adapt to the characters.

Do not enlarge, move, multiply, reshape, replace, relocate, or spawn objects to satisfy
an action.

All environment objects visible in `@image1` are locked in place. Trees, flowers, grass
patches, hills, stones, doorways, props, sky elements, furniture, anchors, and landmarks
must not move, grow, shrink, slide, drift, pop in, enter frame, leave frame, or
reposition.

Only characters may move unless the shot explicitly allows a planned location
transition, such as an entrance crossing. The camera must not move to make an object
more usable.

Before generation, label the shot:

- **SAFE:** all required objects are visible and usable; generate.
- **RISKY:** usable but with quality risk; simplify action or add stricter locks before
  generating.
- **NOT READY:** required object is missing or unusable; do not spend video credits.
- **RESET REQUIRED:** the current visual source is degraded; reject it and regenerate a
  clean shot-specific still from canonical references.

Before generating any shot, answer:

1. Which object does this shot interact with?
2. Is the object visible in `@image1`?
3. Is the object usable for the action at its current size, position, shape, and
   distance?
4. Would the character need camera movement to reach or use it?
5. Would the model need to enlarge, move, multiply, reshape, or spawn the object?
6. Does the action finish and settle into the separately approved clean end still?

If any answer fails, do not generate video. Simplify the action, regenerate the
prerequisite still, or mark the shot as salvage with frozen-layout rules.

---

## 5. Export and QA

After each shot is generated, export:

- first frame
- final frame
- final video

For edit QA only, compare:

- previous shot final video frame
- next shot first video frame

These exported frames are review evidence by default. A final frame may be promoted to a
linked-shot production input only when the pre-production plan calls for exact continuity,
the chain limit permits it and the frame passes every linked-frame QA check.

Then watch the full video twice:

1. Once only for character continuity inside the shot.
2. Once only for hard background/object stability.

Approve the transition only if:

- colour does not fade or shift
- any editorial camera change is intentional and clean
- character scale stays consistent
- background/world-locked elements stay in the same layout
- persistent props (e.g. a discovered object being carried between shots) stay consistent
- story continuity remains clear even when the new shot is a fresh setup
- no character disappears, reappears, teleports, regenerates after occlusion, switches
  sides without visible motion, or has an unreadable path inside the shot
- no foreground object fully hides a character
- no background object moves, morphs, duplicates, disappears, changes identity or changes
  side of the frame

**If a transition has a small jump:**

1. Keep the previous shot. Do not regenerate it.
2. Break the linked chain; do not preserve a degraded frame.
3. Regenerate or adjust the next shot's clean start still from canonical World and
   character references.
4. Preserve story placement and screen direction, then regenerate only the next video.
5. Prefer a clean editorial cut over forcing pixel-exact continuity.

This export-and-compare step, plus the repair procedure, is what turns "hope the model
gets it right" into a repeatable QA gate. See
`POMPOM_HILLS_PRODUCTION/02_WORLDS/STONE_HILL/04_EPISODE_PACKAGES/S01E07_THE_ROUND_STONE/00_EPISODE_OVERVIEW/01-overview.md`
§ Transition QA for the worked version of this section.

For same-shot character continuity, QA must not rely only on the first and final frames.
The full video must be watched because disappearance, occlusion transition, teleporting
and character regeneration can happen inside the shot.

---

## 6. Transition Repair Prompt (reusable add-on)

Use this add-on whenever a regenerated shot needs a cleaner start while preserving story
continuity:

```text
TRANSITION REPAIR PROMPT ADD-ON:

Use the Production Mode approved @image1 as the exact start-frame reference.
For a fresh repair, rebuild @image1 from canonical World and character references.

The first second must match @image1 very closely: same camera angle, same lens feel,
same character scale, same character positions, same locked background/world layout,
same lighting and same colour grading.

After the first second, begin and complete the planned action slowly and naturally inside
this shot. Finish in a stable, grounded pose for the final 1–2 seconds.

Do not reset the camera. Do not recompose the shot. Do not move the characters to a new
location. Do not redesign the world. Do not change the background layout. Do not change
exposure, saturation, contrast or colour temperature.
```

Substitute the world's own locked elements where "same locked background/world layout"
appears (e.g. for Stone Hill: pebble path position, stone cluster positions; for Central
Square: Big Pompom Tree position and stepping-stone ring; etc. — see each world's own
canon bible §Visual Richness & World Charm / §World Identity Lock for its locked list).

---

## 7. Per-Episode Application

Every new episode's shot files and episode overview must apply this workflow:

- Every shot records Production Mode, Clean Start State, Complete Main Action, Completed End
  State, Stable Final Anchor and Next-Shot Dependency.
- Every fresh/reset shot gets a `## Clean Start-Frame Still` section naming the canonical
  World, approved character references and shot-specific composition used to create `@image1`.
- Whenever possible, every shot also gets a separately approved clean end still and uses
  Start Frame + End Frame mode.
- Any intentionally linked pair/trio records the generated source frame, its QA approval and
  the current chain count. A mandatory quality reset follows the third linked shot and
  normally follows the second.
- The episode overview gets one `## Transition QA` section (export rule, approval
  criteria, repair procedure) that every shot file's Transition Continuity Rule section
  points back to, instead of repeating the full repair prompt in every shot file.

This keeps the repair prompt and QA criteria in one place per episode while keeping the
shot-specific clean-anchor instruction local to each shot file.

---

## 8. What This Does Not Change

- Character design, world design, dialogue, and story beats are untouched by this
  document — it only governs the technical hand-off between shots.
- This does not introduce a new closing-bumper requirement; normal episodes still close on
  their own final shot per `MICRO_OPENING_AND_CLOSING_STANDARD.md` §3.
- This does not replace `00-CORE/CONTINUITY_RULES.md` — it is the per-episode checklist
  built on top of it, specifically adding the world-opening → Shot 01 step and the
  standard Transition QA / repair procedure.
- This document governs clean-anchor and editorial continuity between shots inside the same
  world/episode. For multi-shot videos that are generated as separate standalone shots and
  combined later in editing (especially videos that move between different worlds), the
  standalone-shot generation rule and the in-file post-production transition note are defined
  in `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/STANDALONE_SHOT_AND_TRANSITION_STANDARD.md`.
  That standard complements this one: transitions between worlds are never generated in
  OpenArt, they are handled in editing using each shot's Post-Production Transition Note.

---

*This document is the single source of truth for the shot-to-shot continuity workflow
across episodes and worlds.*
*Validated on: S01E07 — The Round Stone (Stone Hill).*
*Version: 2.0 — 15 July 2026 — Clean anchors, completed actions and mandatory quality resets*
