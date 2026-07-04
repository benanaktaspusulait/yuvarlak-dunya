# Stone Hill Adventures — Micro-Opening

> Reusable, story-external micro-opening for Stone Hill episodes.
> Optional lead-in placed before the main story. It does not change the story length.
>
> Type: **World Micro-Opening** (not a Series Bumper). See
> `POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/MICRO_OPENING_AND_CLOSING_STANDARD.md` §2B for the
> rule set this follows. Unlike a series bumper (e.g. Opa's Storytime), this has **no matching
> reusable closing** — normal Stone Hill episodes close on their own final shot (see
> `MICRO_OPENING_AND_CLOSING_STANDARD.md` §3).
>
> Render prompts: `POMPOM_HILLS_PRODUCTION/02_WORLDS/STONE_HILL/03_OPENINGS/STONE_HILL_ADVENTURES_MICRO_OPENING/render-prompts.md`
> World canon: `POMPOM_HILLS_PRODUCTION/02_WORLDS/STONE_HILL/00_CANON/27-stone-hill-bible.md`
>
> **Reuse note:** Future Stone Hill episodes should reference this reusable package instead
> of redefining the opening from scratch. It is not an episode story shot and should not
> live inside an episode's `01_SHOTS/` folder or be numbered as `shot-00`. An episode may
> reference it in its own overview as an "Optional Pre-Roll" (see
> `s01e07-preroll-reference.md` in this same folder for the S01E07 example).

## Duration

3–4 seconds.

## Use

Optional opening for 90–120 second Stone Hill episodes. The final frame should hand off
into the first story shot.

## Characters

None by default.

## Text & Safety

- No readable text generated inside the AI video.
- No subtitles.
- No logo animation.

## Visual

Smooth rounded toy-like stones, soft pebble path, warm moss patches, small grass tufts,
gentle slope, warm morning daylight.

## Motion

Gentle camera glide or a soft push-in.

## Mood

Warm, safe, tactile, curious, preschool-friendly.

## Sound

A soft warm 3–4 second music motif with gentle marimba or rounded wooden tones, very light
ambient wind, and one tiny pebble-like chime. Calm, tactile, safe and curious. No loud logo
sting, no vocals, no fast whoosh. Follows the general music motif rule in
`POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/MICRO_OPENING_AND_CLOSING_STANDARD.md` §2C and the
volume/instrument limits in `00-CORE/AUDIO_GUIDE.md`.

## Transition

The final frame should visually connect into the first story shot of the episode.

## Production Workflow

This micro-opening may be produced either still-first or shot-first.

**Preferred practical workflow: Shot-first.**

Reason: the asset is ultimately used as a 3–4 second video lead-in, so generating it
directly as a short opening shot can be faster and more production-friendly than always
generating a still first.

**Shot-first rules:**

- Treat this as `Stone Hill Adventures Micro-Opening Shot`.
- Do not number it as `shot-00` inside an episode's `01_SHOTS/` folder. When an episode
  uses it, reference it in the episode overview as an "Optional Pre-Roll" instead (see
  example below and `s01e07-preroll-reference.md` in this folder).
- It is not part of the main story duration.
- It does not replace Shot 01.
- Characters still begin in Shot 01.
- The micro-opening shows only Stone Hill atmosphere.
- After rendering, export:
  - first frame
  - final frame
  - final video clip
- Save these assets in the Stone Hill opening package.

**Clarify:** this is a reusable world asset, not a normal story shot. It should live under:

```text
POMPOM_HILLS_PRODUCTION/02_WORLDS/STONE_HILL/03_OPENINGS/STONE_HILL_ADVENTURES_MICRO_OPENING/
```

not inside every episode folder.

If an episode wants to reference it, the episode overview can list it as:

```text
Optional Pre-Roll: Stone Hill Adventures Micro-Opening
Duration: 3–4 seconds
Source: POMPOM_HILLS_PRODUCTION/02_WORLDS/STONE_HILL/03_OPENINGS/STONE_HILL_ADVENTURES_MICRO_OPENING/
```

See `render-prompts.md` § Option A / Option B for the still-first vs. shot-first render
prompts.
