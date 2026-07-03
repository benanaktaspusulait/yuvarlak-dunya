# Architecture Decisions

---

## Why This Document Exists

Over time, many production decisions will be made.

Months or years later, team members should be able to understand:

- Why was this decision made?
- What alternatives were considered?
- What problem did it solve?
- Should it still be followed today?

This document preserves that knowledge.

Production history matters because decisions that seem obvious today may seem confusing tomorrow. Documenting reasoning is more valuable than documenting outcomes.

This is the project's institutional memory.

---

## Decision Template

Use this template for every new decision:

```markdown
### ADR-[NUMBER]: [TITLE]

**Date:** [DATE]
**Status:** Accepted | Superseded | Deprecated
**Category:** Production | Storytelling | Rendering | Characters | World Building | Publishing | Pipeline | Creative Direction

**Decision:**
[Describe the decision.]

**Context:**
[What problem existed?]

**Alternatives Considered:**
- [Alternative 1]
- [Alternative 2]
- [Alternative 3]

**Reasoning:**
[Explain why this decision was chosen.]

**Impact:**
- Positive: [Benefits]
- Negative: [Trade-offs]

**Review:**
[Should this decision ever be reconsidered?]

**Related Documents:**
- [Reference other files]
```

---

## Decision Records

---

### ADR-001: Low-Stimulation Preschool Philosophy

**Date:** Project inception
**Status:** Accepted
**Category:** Creative Direction

**Decision:**
Pompom Hills will follow a low-stimulation preschool philosophy. All content will prioritize calm, gentle, and safe experiences over excitement and stimulation.

**Context:**
The preschool animation market is dominated by high-stimulation content (fast cuts, loud sounds, bright colours). Research shows that excessive stimulation can overwhelm young children and disrupt attention development. A gap exists for calm, gentle content.

**Alternatives Considered:**
- High-stimulation approach (like Cocomelon) — rejected because it conflicts with child development principles
- Mixed stimulation approach — rejected because inconsistency confuses the target audience
- Educational/classroom approach — rejected because it feels clinical rather than warm

**Reasoning:**
Low stimulation aligns with child development research for ages 3–4. It creates a distinctive brand position. It supports the "safe world" concept. It enables bedtime viewing.

**Impact:**
- Positive: Unique market position, child-safe content, bedtime viewing potential
- Negative: Slower pacing may reduce initial engagement metrics

**Review:**
This decision should be reviewed only if child development research fundamentally changes.

**Related Documents:**
- `06_STORY_BIBLE.md`
- `00-CORE/CHILD_SAFETY_RULES.md`

---

### ADR-002: Small Core Cast Before Expansion

**Date:** Project inception
**Status:** Accepted
**Category:** Characters

**Decision:**
The project begins with a small set of core characters (Kiko, Mimi, Opa) before expanding the universe. Supporting characters (Luca, Noah, Arda) are introduced after the core trio is established.

**Context:**
Toddler audiences (3-4 years) form emotional attachments slowly. Introducing too many characters simultaneously fragments attention and weakens attachment.

**Alternatives Considered:**
- Full ensemble from episode 1 — rejected because it overwhelms toddlers
- Two main characters — rejected because it splits emotional focus
- One character only — rejected because it limits story variety

**Reasoning:**
A small core cast allows deep emotional attachment. Supporting characters add variety without confusion. The hybrid model (one primary + core supporting) mirrors how toddlers actually form relationships.

**Impact:**
- Positive: Strong emotional attachment, clear character hierarchy, simpler production
- Negative: Limited initial variety, requires patience before expansion

**Review:**
This decision is permanent. The core trio structure should never change.

**Related Documents:**
- `04_CHARACTER_BIBLE.md`
- `02_SEASON_STRATEGY.md`

---

### ADR-003: Character Intros Before Story Production

**Date:** Pre-production
**Status:** Accepted
**Category:** Production

**Decision:**
Character introduction videos are produced before large-scale story production begins. Each active character receives a 15-second intro in both landscape and Shorts format.

**Context:**
Before producing episodes, the production pipeline needs to be tested with simple, contained content. Character intros provide this opportunity while also creating reusable marketing assets.

**Alternatives Considered:**
- Start directly with episodes — rejected because the pipeline isn't proven yet
- Produce intros and episodes simultaneously — rejected because it splits focus
- Skip intros entirely — rejected because they serve as essential marketing assets

**Reasoning:**
Character intros test the production pipeline with simple content. They create reusable assets for marketing. They establish character consistency before complex stories. They provide early content for the YouTube channel.

**Impact:**
- Positive: Pipeline tested, marketing assets created, character consistency established
- Negative: Delays episode production slightly

**Review:**
This decision applies to Season 1. In future seasons, new characters may be introduced through episodes rather than separate intros.

**Related Documents:**
- `03_PRODUCTION_STATUS.md`
- `08_ASSET_LIBRARY.md`

---

### ADR-004: 1-Minute Episodes as Starting Format

**Date:** Project inception
**Status:** Accepted
**Category:** Production

**Decision:**
Production starts with 1-minute episodes (4 shots × 15 seconds). Longer episodes will be introduced gradually as production maturity increases.

**Context:**
The production pipeline is new and unproven. Starting with shorter episodes reduces risk, allows faster iteration, and builds team confidence before tackling more complex content.

**Alternatives Considered:**
- Start with 7-minute episodes — rejected because the pipeline can't support this yet
- Start with 30-second episodes — rejected because it's too short for meaningful stories
- Start with variable lengths — rejected because consistency aids learning

**Reasoning:**
1-minute episodes are producible with current resources. They allow rapid iteration and learning. They build the production pipeline incrementally. They match toddler attention spans for initial content.

**Impact:**
- Positive: Faster iteration, lower risk, pipeline development
- Negative: Limited story complexity initially

**Review:**
This decision should be revisited after 20 episodes are produced. At that point, the pipeline should be mature enough for 2-3 minute episodes.

**Related Documents:**
- `07_PRODUCTION_PIPELINE.md`
- `01_PROJECT_ROADMAP.md`

---

### ADR-005: Worlds as Reusable Long-Term Assets

**Date:** Project inception
**Status:** Accepted
**Category:** World Building

**Decision:**
Every world created becomes a permanent, reusable asset. Worlds are never deleted, redesigned, or retired. Each world must support at least 5 future episodes before being created.

**Context:**
Animation production is expensive. Creating a world that is used only once wastes resources. Treating worlds as permanent assets ensures maximum return on investment and maintains visual consistency.

**Alternatives Considered:**
- Create new worlds for each episode — rejected because it's wasteful and inconsistent
- Allow world redesign — rejected because it breaks continuity
- Limit worlds to single episodes — rejected because it doesn't justify creation cost

**Reasoning:**
Permanent worlds reduce production costs over time. They maintain visual consistency. They create a sense of a lived-in world. They support the "familiar yet fresh" storytelling approach.

**Impact:**
- Positive: Cost efficiency, visual consistency, world depth
- Negative: Requires careful world planning before creation

**Review:**
This decision is permanent. Worlds are assets, not disposable content.

**Related Documents:**
- `05_WORLD_BIBLE.md`
- `08_ASSET_LIBRARY.md`

---

### ADR-006: Frame Continuity Over Scene Recreation

**Date:** After Episode 1 production
**Status:** Accepted
**Category:** Pipeline

**Decision:**
The OpenArt continuity workflow uses frame continuity (selecting the best frame from the previous shot) rather than recreating scenes from scratch for each shot.

**Context:**
During Episode 1 production, it was discovered that using the final frame of each shot as the reference for the next shot sometimes caused visual jumps. The AI would reinterpret the scene, changing lighting, composition, or character positions.

**Alternatives Considered:**
- Use final frame automatically — rejected because it causes visual jumps
- Recreate each scene from scratch — rejected because it breaks continuity
- Use fixed camera positions — rejected because it limits storytelling

**Reasoning:**
Intentional frame selection produces smoother transitions. The best continuity frame may occur before the final frame. This approach gives the production team control over visual flow while maintaining the AI generation pipeline.

**Impact:**
- Positive: Smoother transitions, better visual continuity, production control
- Negative: Requires manual frame selection, adds review step

**Review:**
This decision should be revisited if AI video generation improves significantly in frame-to-frame consistency.

**Related Documents:**
- `07_PRODUCTION_PIPELINE.md`
- `00-CORE/PRODUCTION_PIPELINE.md` (Reference Frame Selection section)

---

### ADR-007: Quality Over Speed

**Date:** Project inception
**Status:** Accepted
**Category:** Pipeline

**Decision:**
Production quality takes priority over production speed. Milestones are based on production maturity rather than fixed dates.

**Context:**
Many animation projects fail because they prioritize speed over quality. Rushed content damages brand reputation and audience trust. A sustainable pace builds long-term value.

**Alternatives Considered:**
- Fixed deadline approach — rejected because it prioritizes speed over quality
- Speed-first approach — rejected because it leads to inconsistent output
- Quality-only approach (no deadlines) — rejected because it lacks accountability

**Reasoning:**
Quality-focused production builds a sustainable brand. Milestones based on maturity ensure the team is ready before advancing. This approach prevents the "burn bright, burn fast" pattern that kills many animation projects.

**Impact:**
- Positive: Consistent quality, sustainable pace, brand integrity
- Negative: Slower initial output, requires patience

**Review:**
This decision is permanent. Quality should never be sacrificed for speed.

**Related Documents:**
- `01_PROJECT_ROADMAP.md`
- `07_PRODUCTION_PIPELINE.md`

---

### ADR-008: Reusable Assets Over Disposable Content

**Date:** Project inception
**Status:** Accepted
**Category:** Pipeline

**Decision:**
Every new asset should be reusable across many future episodes. Before creating any asset, the team must ask how many future episodes can use it.

**Context:**
Animation production is resource-intensive. Creating assets that are used only once wastes time and money. Building a library of reusable assets maximizes return on investment.

**Alternatives Considered:**
- Create custom assets per episode — rejected because it's wasteful
- Use generic stock assets — rejected because it lacks brand identity
- Limit asset creation — rejected because it restricts creativity

**Reasoning:**
Reusable assets reduce per-episode production costs. They maintain visual consistency. They build a rich, layered world over time. They enable faster production as the asset library grows.

**Impact:**
- Positive: Cost efficiency, visual consistency, production speed
- Negative: Requires upfront planning, limits one-off creative experiments

**Review:**
This decision is permanent. Assets are investments, not expenses.

**Related Documents:**
- `08_ASSET_LIBRARY.md`
- `01_PROJECT_ROADMAP.md`

---

### ADR-009: Episode-Level Music Over Shot-Level Music

**Date:** After Episode 14 production
**Status:** Accepted
**Category:** Production

**Decision:**
Background music is added at the episode level during editing, not at the shot level during generation. OpenArt-generated music should be muted or removed.

**Context:**
During production, it was observed that shot-level music creates audio discontinuities when shots are edited together. Music restarts between shots, breaking the viewing experience.

**Alternatives Considered:**
- Use OpenArt-generated music per shot — rejected because it creates audio jumps
- Add music during generation — rejected because it limits editing flexibility
- No music at all — rejected because it reduces emotional impact

**Reasoning:**
Episode-level music ensures audio continuity across the entire episode. It gives the editing team control over musical flow. It allows for proper fades and transitions. It creates a cohesive viewing experience.

**Impact:**
- Positive: Audio continuity, editing flexibility, cohesive experience
- Negative: Requires separate music production step

**Review:**
This decision should be revisited if AI video generation develops reliable episode-level music generation.

**Related Documents:**
- `07_PRODUCTION_PIPELINE.md`
- `00-CORE/EPISODE_AUDIO_WORKFLOW.md`

---

### ADR-010: Single Documentation Source Per Topic

**Date:** After initial documentation system creation
**Status:** Accepted
**Category:** Pipeline

**Decision:**
Every topic has exactly one canonical documentation file. Other files reference this file rather than repeating its content.

**Context:**
The project had accumulated duplicate information across multiple files. This made maintenance difficult and created confusion about which version was current.

**Alternatives Considered:**
- Multiple files per topic — rejected because it creates confusion
- Single massive document — rejected because it becomes unwieldy
- No documentation — rejected because knowledge is lost

**Reasoning:**
Single source of truth eliminates confusion. Cross-references maintain connectivity without duplication. This approach scales well as the project grows.

**Impact:**
- Positive: Clear ownership, easy maintenance, no confusion
- Negative: Requires discipline to maintain references

**Review:**
This decision is permanent. Documentation should always follow the single source principle.

**Related Documents:**
- All documents in the documentation system

---

### ADR-011: UK-Based Licensing Strategy

**Date:** After documentation system creation
**Status:** Accepted
**Category:** Publishing

**Decision:**
The project pursues UK-based licensing for international expansion, leveraging London's position as Europe's licensing hub.

**Context:**
UK-based companies have access to major licensing events (BLE), strong IP protection, and proximity to European and English-speaking markets.

**Alternatives Considered:**
- US-based licensing — rejected because UK provides better European access
- No licensing focus — rejected because it limits revenue potential
- Direct manufacturing — rejected because it requires different expertise

**Reasoning:**
UK provides the strongest position for European licensing. London hosts Brand Licensing Europe. UK IP law is internationally recognized. English-language content has global reach.

**Impact:**
- Positive: Access to European market, strong IP protection, licensing event access
- Negative: Requires UK business presence

**Review:**
This decision should be revisited if the project targets specific non-European markets.

**Related Documents:**
- `10-LICENSING/LICENSING_STRATEGY.md`

---

### ADR-012: One World Per Episode

**Date:** After Season 1 production began
**Status:** Accepted
**Category:** Production

**Decision:**
Each episode takes place in exactly one world. Episodes do not transition between multiple worlds within a single 60-second runtime.

**Context:**
Early production showed that multi-world episodes create continuity errors, increase production complexity, and confuse young viewers who cannot track location changes.

**Alternatives Considered:**
- Multi-world episodes — rejected because it breaks continuity and confuses toddlers
- World transitions within episodes — rejected because it requires establishing shots that waste runtime
- Random world assignment — rejected because it prevents asset reuse planning

**Reasoning:**
One world per episode simplifies production, maintains continuity, and creates clear episode identity. It also maximizes asset reuse — each world is used across multiple episodes.

**Impact:**
- Positive: Simplified production, better continuity, clearer episode identity
- Negative: Limited world variety per episode

**Review:**
This decision may be revisited for longer episodes (2+ minutes) where a world transition could be justified.

**Related Documents:**
- `05_WORLD_BIBLE.md`
- `07_PRODUCTION_PIPELINE.md`

---

### ADR-013: Maximum Three Active Characters

**Date:** After initial character analysis
**Status:** Accepted
**Category:** Characters

**Decision:**
Each episode features a maximum of 3 active characters. Additional characters may appear in the background but do not participate in the story.

**Context:**
Character analysis showed that episodes with more than 3 active characters lose emotional focus. Toddler viewers (3-4 years) cannot track relationships between more than 3 characters simultaneously.

**Alternatives Considered:**
- 4-5 active characters — rejected because it fragments emotional attention
- 2 character minimum — rejected because it limits story variety
- Variable character count — rejected because inconsistency confuses toddlers

**Reasoning:**
Three characters provide enough variety for relationships while maintaining emotional clarity. The core trio (Kiko, Mimi, Opa) plus one supporting character creates four possible configurations — enough for 26+ episodes without repetition.

**Impact:**
- Positive: Clear emotional focus, simpler production, stronger character attachment
- Negative: Limited ensemble moments

**Review:**
This decision is permanent for 60-second episodes. Longer formats may allow more characters.

**Related Documents:**
- `04_CHARACTER_BIBLE.md`
- `02_SEASON_STRATEGY.md`

---

### ADR-014: Facebook Stories Generated Daily

**Date:** After content reuse strategy defined
**Status:** Accepted
**Category:** Publishing

**Decision:**
Facebook Stories are generated daily as part of the content output pipeline. Each story is a single-frame or short-loop asset designed for Facebook's story format.

**Context:**
Facebook Stories provide a high-frequency, low-effort distribution channel. They keep the brand visible between episode releases and reach audiences who may not use YouTube.

**Alternatives Considered:**
- Weekly Stories — rejected because daily presence builds faster audience recognition
- No Facebook strategy — rejected because Facebook reaches parents of preschool children
- Shared content with YouTube — rejected because Stories require format-specific optimization

**Reasoning:**
Daily Stories create consistent brand presence. They are cheaper to produce than episodes. They serve as a discovery funnel for the YouTube channel.

**Impact:**
- Positive: Daily brand presence, low production cost, audience discovery
- Negative: Requires daily production discipline

**Review:**
This decision should be revisited after 30 days of analytics data.

**Related Documents:**
- `09_YOUTUBE_STRATEGY.md`
- `03_PRODUCTION_STATUS.md`

---

### ADR-015: Shorts Produced From Long Episodes

**Date:** After initial content production
**Status:** Accepted
**Category:** Production

**Decision:**
Shorts (15-30 seconds) are derived from existing long episodes (60 seconds), not produced as independent content. Each long episode should yield 1-2 Shorts.

**Context:**
Producing Shorts independently doubles production cost. Deriving them from episodes ensures visual consistency and maximizes return on production investment.

**Alternatives Considered:**
- Independent Short production — rejected because it doubles cost without doubling content
- No Shorts strategy — rejected because Shorts are a primary discovery mechanism on YouTube
- Random clip extraction — rejected because it produces inconsistent quality

**Reasoning:**
Episode-derived Shorts are visually consistent with the main content. They create a natural content funnel: Short → Episode → Channel subscription. They reduce production cost per piece of content.

**Impact:**
- Positive: Reduced production cost, visual consistency, content funnel
- Negative: Shorts are dependent on episode production schedule

**Review:**
This decision is permanent. Shorts are always derived from episodes.

**Related Documents:**
- `09_YOUTUBE_STRATEGY.md`
- `07_PRODUCTION_PIPELINE.md`

---

### ADR-016: Reference Continuity Frame Instead of Final Frame

**Date:** After Episode 1 production
**Status:** Accepted
**Category:** Pipeline

**Decision:**
When generating subsequent shots, the continuity reference is selected from the best frame of the previous shot — not automatically the final frame.

**Context:**
Using the final frame caused visual jumps because the AI would reinterpret the scene between the last frame and the next generation. The best continuity frame often occurs before the final frame.

**Alternatives Considered:**
- Use final frame automatically — rejected because it causes visual jumps
- Recreate each scene from scratch — rejected because it breaks continuity
- Use fixed camera positions — rejected because it limits storytelling

**Reasoning:**
Intentional frame selection produces smoother transitions. The production team selects the frame that provides the best visual continuity, regardless of its position in the shot timeline.

**Impact:**
- Positive: Smoother transitions, better visual continuity, production control
- Negative: Requires manual frame selection, adds review step

**Review:**
This decision should be revisited if AI video generation improves significantly in frame-to-frame consistency.

**Related Documents:**
- `07_PRODUCTION_PIPELINE.md`
- `00-CORE/PRODUCTION_PIPELINE.md`

---

### ADR-017: Character Introductions Before Story Episodes

**Date:** Pre-production
**Status:** Accepted
**Category:** Production

**Decision:**
All active characters receive standalone introduction videos before story episodes featuring them are produced. Intros serve as both character establishment and production pipeline testing.

**Context:**
Characters need to be visually consistent before they appear in complex story scenarios. Intros provide a controlled environment to establish and verify character consistency.

**Alternatives Considered:**
- Introduce characters within episodes — rejected because it splits audience attention
- Skip introductions — rejected because it removes a key marketing asset
- Produce intros after episodes — rejected because character consistency is not yet proven

**Reasoning:**
Intros establish character consistency in a controlled setting. They create reusable marketing assets. They test the production pipeline with simple content before complex stories.

**Impact:**
- Positive: Character consistency proven, marketing assets created, pipeline tested
- Negative: Delays episode production slightly

**Review:**
This decision applies to Season 1. Future seasons may introduce characters through episodes.

**Related Documents:**
- `04_CHARACTER_BIBLE.md`
- `08_ASSET_LIBRARY.md`

---

### ADR-018: No Text Inside Generated Videos

**Date:** After initial production attempts
**Status:** Accepted
**Category:** Pipeline

**Decision:**
No text, titles, subtitles, or graphic overlays are embedded within AI-generated video frames. All text is added in post-production or as platform-native overlays.

**Context:**
AI video generation produces inconsistent, misspelled, or illegible text. Embedding text in generated frames creates quality issues and makes corrections impossible without regenerating.

**Alternatives Considered:**
- Generate text within frames — rejected because AI produces inconsistent text
- Use text-heavy thumbnails — rejected because thumbnails are separate from video
- Add text via post-production only — accepted as the correct approach

**Reasoning:**
Post-production text addition provides full control over spelling, placement, timing, and style. It allows corrections without regenerating video content. It maintains visual quality.

**Impact:**
- Positive: Full text control, easy corrections, consistent quality
- Negative: Additional post-production step

**Review:**
This decision is permanent. Text in video is always post-production.

**Related Documents:**
- `07_PRODUCTION_PIPELINE.md`
- `00-CORE/TECH_SPECS.md`

---

*This document preserves the reasoning behind important project decisions.*
*Every significant decision should be recorded here.*
*Last updated: 2 Temmuz 2026*
