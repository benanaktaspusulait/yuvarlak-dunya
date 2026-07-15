#!/usr/bin/env python3
"""Split Arda's Stories 6-minute masters into standalone 120-second packages."""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SERIES = ROOT / "POMPOM_HILLS_PRODUCTION" / "07_ARDAS_STORIES"
PACKAGES = SERIES / "04_EPISODE_PACKAGES"
BUILD = SERIES / "04_EPISODE_PACKAGES_SPLIT_BUILD"
BACKUP = SERIES / "04_EPISODE_PACKAGES_LEGACY_BACKUP"


SPLITS = [
    ("AS-EP01_THE_RUNAWAY_POMPOM_BALL", "Three Bounces", "Arda's Home", "Establish the counting game and end when the Pompom Ball rolls through the play gate."),
    ("AS-EP01_THE_RUNAWAY_POMPOM_BALL", "Roll, Roll, Roll", "Safe connecting play path", "Explore slow and fast motion, try too soon, then watch, wait, and catch the ball."),
    ("AS-EP01_THE_RUNAWAY_POMPOM_BALL", "Your Turn", "Friendship Meadow", "Turn Arda's ball play into a shared counting and direction game with Luca and Noah."),
    ("AS-EP02_BUILDING_A_BRIDGE", "The Gap", "Arda's Home", "Find a way across the gap and improve a bridge that is first too short and then too narrow."),
    ("AS-EP02_BUILDING_A_BRIDGE", "Too Narrow", "Building Corner", "Improve the bridge with a better width and a gentle ramp, then practise taking turns."),
    ("AS-EP02_BUILDING_A_BRIDGE", "Let's Cross!", "Friendship Meadow", "Work together to extend the bridge and complete a full, safe crossing."),
    ("AS-EP03_THE_TALLER_TOWER", "The Fall", "Arda's Home — Indoor Play Area", "Build a tower, experience a safe tumble, and choose to try again."),
    ("AS-EP03_THE_TALLER_TOWER", "Wider Base", "Arda's Home — Indoor Play Area → Garden", "Observe the blocks, widen the base, and build a tower that stands tall."),
    ("AS-EP03_THE_TALLER_TOWER", "Let's Build Together", "Friendship Meadow", "Build with Luca and Noah and connect two towers with a shared bridge."),
    ("AS-EP04_THE_SHADOW_GAME", "First Shadow", "Arda's Home Garden", "Discover a shadow and explore why it keeps moving with Arda."),
    ("AS-EP04_THE_SHADOW_GAME", "Shadow Dance", "Arda's Home Garden → Path", "Test waves, stops, spins, and jumps to discover that a shadow mirrors movement."),
    ("AS-EP04_THE_SHADOW_GAME", "Our Shadows", "Path → Friendship Meadow", "Bring three friends and three shadows together for a gentle movement game."),
    ("AS-EP05_THE_ROLLING_DRUM", "First Tap", "Arda's Home Indoor Play Area", "Discover the drum's sound and rolling movement, then guide it safely outside."),
    ("AS-EP05_THE_ROLLING_DRUM", "The Beat", "Arda's Home Garden → Path", "Compare slow and fast rolling and find a comfortable middle rhythm."),
    ("AS-EP05_THE_ROLLING_DRUM", "Drum Circle", "Path → Friendship Meadow", "Create a shared drum circle and practise starting, stopping, and playing together."),
    ("AS-EP06_THE_COLOURFUL_PUDDLE", "First Splash", "Arda's Home Garden after rain", "Discover a colourful puddle, its reflection, and the ripples made by a gentle touch."),
    ("AS-EP06_THE_COLOURFUL_PUDDLE", "Reflection Game", "Arda's Home Garden → Path", "Watch still water and small ripples change a reflection."),
    ("AS-EP06_THE_COLOURFUL_PUDDLE", "Splash Friends", "Path → Friendship Meadow", "Share a safe puddle game with Luca and Noah and discover three reflections."),
    ("AS-EP07_THE_KITE_THAT_WOULD_NOT_FLY", "No Wind", "Arda's Home Garden → Small Hill", "Try several safe ways to launch a kite and notice that running alone is not enough."),
    ("AS-EP07_THE_KITE_THAT_WOULD_NOT_FLY", "Waiting for Wind", "Hilltop → Open Sky", "Observe leaves and feel the breeze before launching the kite successfully."),
    ("AS-EP07_THE_KITE_THAT_WOULD_NOT_FLY", "Flying Together", "Friendship Meadow", "Fly three kites with Luca and Noah in a gentle shared sky game."),
    ("AS-EP08_THE_HIDE_AND_SEEK_LEAF", "The Leaf Appears", "Arda's Home Garden", "Find a golden leaf, play with it, and follow when the wind carries it away."),
    ("AS-EP08_THE_HIDE_AND_SEEK_LEAF", "Where Did It Go?", "Flower Corner → Garden", "Search behind, under, and beside familiar objects to find the hidden leaf."),
    ("AS-EP08_THE_HIDE_AND_SEEK_LEAF", "Found Together", "Friendship Meadow", "Search carefully with Luca and Noah and turn finding the leaf into a shared game."),
    ("AS-EP09_THE_ROCKING_BOAT", "First Float", "Arda's Home Garden — shallow stream", "Test a toy boat, recover from a push that is too strong, and help it float gently."),
    ("AS-EP09_THE_ROCKING_BOAT", "Gentle Push", "Arda's Home Garden → Bridge Spot", "Use gentle breath and patient observation to guide the boat under a bridge."),
    ("AS-EP09_THE_ROCKING_BOAT", "Boat Parade", "Bridge Spot → Friendship Meadow", "Float three toy boats with Luca and Noah in a calm parade."),
    ("AS-EP10_THE_ROLLING_ACORN", "First Roll", "Arda's Home garden → Tree area", "Roll an acorn on a smooth path and grass to compare fast and slow movement."),
    ("AS-EP10_THE_ROLLING_ACORN", "Surface Discovery", "Tree area → Meadow path edges", "Test moss, sand, and leaves to discover how surfaces change rolling speed."),
    ("AS-EP10_THE_ROLLING_ACORN", "Rolling Race", "Friendship Meadow path", "Compare surfaces with Luca and Noah in a cooperative rolling game."),
]


def slug(title: str) -> str:
    value = title.upper().replace("'", "")
    value = re.sub(r"[^A-Z0-9]+", "_", value)
    return value.strip("_")


def display_id(number: int) -> str:
    return f"AS-EP{number:02d}"


def shot_time(local: int) -> str:
    start = (local - 1) * 15
    end = local * 15
    return f"{start // 60}:{start % 60:02d}–{end // 60}:{end % 60:02d}"


def section(text: str, heading: str, next_heading: str | None = None) -> str:
    start = text.find(heading)
    if start < 0:
        return ""
    start += len(heading)
    if next_heading:
        end = text.find(next_heading, start)
    else:
        match = re.search(r"\n## ", text[start:])
        end = start + match.start() if match else len(text)
    if end < 0:
        end = len(text)
    return text[start:end].strip()


def parse_table_value(text: str, field: str) -> str:
    match = re.search(rf"^\| {re.escape(field)} \| (.*?) \|$", text, re.M)
    return match.group(1).strip() if match else ""


def rebase_references(text: str, offset: int) -> str:
    def replace(match: re.Match[str]) -> str:
        number = int(match.group(2))
        if offset + 1 <= number <= offset + 8:
            number -= offset
        return f"{match.group(1)}{number:02d}"

    return re.sub(r"(Shot |shot-)(\d{2})", replace, text)


def replace_section(text: str, heading: str, body: str) -> str:
    pattern = rf"({re.escape(heading)}\n)(.*?)(?=\n---\n|\n## |\Z)"
    return re.sub(pattern, rf"\1\n{body.strip()}\n", text, count=1, flags=re.S)


def transform_shot(text: str, old_id: str, new_id: str, title: str, offset: int, local: int) -> str:
    text = rebase_references(text, offset)
    text = re.sub(r"^# .*? — Shot", f"# {title} — Shot", text, count=1, flags=re.M)
    text = text.replace(old_id, new_id)
    text = re.sub(r"^\| Episode \|.*?\|$", f"| Episode | {new_id} — {title} |", text, flags=re.M)
    text = re.sub(r"^\| Module \|.*?\|\n", "", text, flags=re.M)
    text = re.sub(r"^\| Shot \|.*?\|$", f"| Shot | {local:02d} / 08 |", text, flags=re.M)
    text = re.sub(r"\bModule [ABC]\b", "the episode", text, flags=re.I)
    if local == 1:
        continuity = (
            f"First story shot of {new_id} — {title}. Establish the characters, location, active "
            "prop, and action clearly from the first frame. This episode must be understandable "
            "without footage or context from any other episode."
        )
        text = replace_section(text, "## Continuity", continuity)
        if "## Start Frame" in text:
            text = replace_section(
                text,
                "## Start Frame",
                "Start from an approved episode-opening keyframe created for this standalone package. "
                "Do not inherit a frame from another episode.",
            )
        if "## Reference Usage" in text:
            text = replace_section(
                text,
                "## Reference Usage",
                "@image1 = approved episode-opening keyframe for this standalone episode.",
            )
        if "## Transition Continuity Rule" in text:
            text = replace_section(
                text,
                "## Transition Continuity Rule",
                "No prior-episode continuity frame is permitted. Begin from this episode's own approved opening keyframe.",
            )
    if local == 8:
        ending = f"""This is the final shot of {new_id} — {title}.

Recommended edit transition after this shot:
- soft crossfade to black or the episode end card
- 0.5–0.8 seconds
- no preview or footage from another episode
- no dramatic transition

Audio:
- gently fade the current ambience to silence
- no music
- no chime
- no whoosh
- no hard audio cut

Important:
This transition is done in editing only.
Do not ask OpenArt to generate the transition.
Do not include transition wording inside the OpenArt Visual Prompt."""
        text = replace_section(text, "## Post-Production Transition Note", ending)
    return text


def transform_prompt(text: str, offset: int, local: int) -> str:
    text = rebase_references(text, offset)
    text = re.sub(r"^# Shot \d{2}", f"# Shot {local:02d}", text, count=1, flags=re.M)
    text = re.sub(r"shot-\d{2}-", f"shot-{local:02d}-", text)
    if local == 1:
        text = re.sub(
            r"Use @image1 as continuity from Shot \d{2}\.",
            "Use @image1 as this standalone episode's approved opening keyframe.",
            text,
        )
    return text


def parse_beat_rows(text: str) -> list[tuple[int, str, str]]:
    rows = []
    for match in re.finditer(r"^\|\s*(\d{1,2})\s*\|\s*[^|]+\|\s*(.*?)\s*\|\s*(.*?)\s*\|$", text, re.M):
        rows.append((int(match.group(1)), match.group(2).strip(), match.group(3).strip()))
    return rows


def extract_screenplay_module(text: str, index: int, offset: int) -> str:
    parts = re.split(r"(?im)^## (?:MODULE|Module) [ABC].*?\n", text)
    body = parts[index + 1].strip() if len(parts) > index + 1 else ""
    body = rebase_references(body, offset)
    body = re.sub(
        r"(?m)^### Shot (\d{2}) — (.*?)(?: \([^\n]+\))?$",
        lambda m: f"### Shot {int(m.group(1)):02d} — {m.group(2)} ({shot_time(int(m.group(1)))})",
        body,
    )
    time_index = 0

    def replace_time(_: re.Match[str]) -> str:
        nonlocal time_index
        time_index += 1
        return f"**Time:** {shot_time(time_index)}"

    body = re.sub(r"(?m)^\*\*Time:\*\* .*?$", replace_time, body)
    return body


def make_overview(
    number: int,
    title: str,
    location: str,
    function: str,
    source_overview: str,
    characters: list[str],
) -> str:
    learning = parse_table_value(source_overview, "Learning areas") or "Movement, observation, persistence, shared play"
    canon = section(source_overview, "## Canon Locks")
    canon = canon.replace("all 24 shots", "all 8 shots").replace("24 shots", "8 shots")
    char_text = ", ".join(characters)
    return f"""# Arda's Stories EP{number:02d} — {title}

---

## Episode Lock

| Field | Value |
|---|---|
| Series | Arda's Stories |
| Playlist | Arda's Stories \\| Play, Move, and Learn |
| Published duration | 120 seconds |
| Episode structure | 8 shots × 15 seconds |
| Package type | Standalone episode |
| Audience | Ages 2–4 |
| Characters | {char_text} |
| Locations | {location} |
| Learning areas | {learning} |
| Opening | Direct in-story hook; no dependency on another episode |
| Closing | Complete 120-second ending; no transition into another episode |

---

## Logline

{function}

---

## Story Promise

This is a complete, independently publishable Arda's Stories episode. Its hook, action, learning
payoff, and closing are contained within eight 15-second shots.

---

## Canon Locks

{canon}

---

## Episode Structure

| Time | Shots | Story function |
|---:|---:|---|
| 0:00–2:00 | 01–08 | {function} |

---

## Learning Outcome

Children can follow one clear physical idea from setup through payoff in a calm, safe, repeatable
two-minute story.
"""


def make_beat_sheet(title: str, rows: list[tuple[int, str, str]], offset: int) -> str:
    lines = [
        f"# Beat Sheet — {title}",
        "",
        "| Shot | Time | Beat | Short potential |",
        "|---:|---:|---|---|",
    ]
    for local, (_, beat, potential) in enumerate(rows[offset:offset + 8], 1):
        lines.append(f"| {local:02d} | {shot_time(local)} | {beat} | {potential} |")
    lines.append("")
    return "\n".join(lines)


def make_shorts_plan(new_id: str, title: str, rows: list[tuple[int, str, str]], offset: int) -> str:
    lines = [
        f"# {new_id} — {title} — Shorts Plan",
        "",
        "## Overview",
        "",
        "This standalone 120-second episode contains eight pre-planned 15-second Short candidates.",
        "",
        "## Shorts List",
        "",
        "| # | Source Shot | Candidate hook | Payoff |",
        "|---:|---:|---|---|",
    ]
    for local, (_, beat, potential) in enumerate(rows[offset:offset + 8], 1):
        lines.append(f"| {local} | Shot {local:02d} | {beat} | {potential} |")
    lines.extend([
        "",
        "## Extraction Rules",
        "",
        "- Use only footage from this episode package.",
        "- Keep Arda, faces, and the active prop inside the central 60% safe region.",
        "- Preserve the original colour grade, locked voices, and natural ambience.",
        "- Add no loud music, meme text, arrows, or unrelated footage.",
        "- Each exported Short must retain a readable hook, action, and payoff.",
        "",
    ])
    return "\n".join(lines)


def main() -> None:
    if BUILD.exists() or BACKUP.exists():
        raise SystemExit("Build or backup directory already exists; inspect before rerunning.")
    BUILD.mkdir(parents=True)

    grouped: dict[str, list[tuple[int, str, str, str]]] = {}
    for number, (source, title, location, function) in enumerate(SPLITS, 1):
        grouped.setdefault(source, []).append((number, title, location, function))

    for source_name, episodes in grouped.items():
        source = PACKAGES / source_name
        overview_text = (source / "00_EPISODE_OVERVIEW" / "01-overview.md").read_text()
        beat_text = (source / "00_EPISODE_OVERVIEW" / "02-beat-sheet.md").read_text()
        screenplay_text = (source / "00_EPISODE_OVERVIEW" / "03-screenplay.md").read_text()
        beat_rows = parse_beat_rows(beat_text)
        if len(beat_rows) != 24:
            raise ValueError(f"Expected 24 beat rows in {source_name}, found {len(beat_rows)}")
        old_id = source_name.split("_", 1)[0]

        shot_files = sorted((source / "01_SHOTS").glob("shot-*.md"))
        prompt_files = sorted((source / "03_VIDEO_EXPORTS" / "openart").glob("shot-*-openart-prompt.md"))
        extra_prompt_files = [p for p in (source / "03_VIDEO_EXPORTS" / "openart").glob("*") if not p.name.startswith("shot-")]
        if len(shot_files) != 24 or len(prompt_files) != 24:
            raise ValueError(f"Expected 24 shots and prompts in {source_name}")

        for index, (number, title, location, function) in enumerate(episodes):
            offset = index * 8
            new_id = display_id(number)
            target = BUILD / f"{new_id}_{slug(title)}"
            overview_dir = target / "00_EPISODE_OVERVIEW"
            shots_dir = target / "01_SHOTS"
            prompts_dir = target / "03_VIDEO_EXPORTS" / "openart"
            shorts_dir = target / "04_SHORTS"
            for directory in (overview_dir, shots_dir, prompts_dir, shorts_dir):
                directory.mkdir(parents=True, exist_ok=True)

            characters = set()
            for local, source_shot in enumerate(shot_files[offset:offset + 8], 1):
                original = source_shot.read_text()
                char_value = parse_table_value(original, "Characters")
                for character in [v.strip() for v in char_value.split(",") if v.strip()]:
                    characters.add(character)
                new_name = re.sub(r"^shot-\d{2}-", f"shot-{local:02d}-", source_shot.name)
                transformed = transform_shot(original, old_id, new_id, title, offset, local)
                (shots_dir / new_name).write_text(transformed)

            for local, source_prompt in enumerate(prompt_files[offset:offset + 8], 1):
                transformed = transform_prompt(source_prompt.read_text(), offset, local)
                (prompts_dir / f"shot-{local:02d}-openart-prompt.md").write_text(transformed)

            for extra in extra_prompt_files:
                if extra.is_file():
                    shutil.copy2(extra, prompts_dir / extra.name)

            (overview_dir / "01-overview.md").write_text(
                make_overview(number, title, location, function, overview_text, sorted(characters))
            )
            (overview_dir / "02-beat-sheet.md").write_text(make_beat_sheet(title, beat_rows, offset))
            screenplay_body = extract_screenplay_module(screenplay_text, index, offset)
            screenplay = (
                f"# Full Screenplay — {title}\n\n"
                "> Standalone duration: 120 seconds. Every shot is exactly 15 seconds. No footage or "
                "context from another episode is required.\n\n---\n\n" + screenplay_body + "\n"
            )
            (overview_dir / "03-screenplay.md").write_text(screenplay)
            (shorts_dir / "00-shorts-plan.md").write_text(make_shorts_plan(new_id, title, beat_rows, offset))

    if len(list(BUILD.glob("AS-EP*"))) != 30:
        raise ValueError("Build did not produce exactly 30 episode packages")

    PACKAGES.rename(BACKUP)
    BUILD.rename(PACKAGES)
    shutil.rmtree(BACKUP)


def normalize_existing() -> None:
    for package in sorted(PACKAGES.glob("AS-EP*")):
        overview = (package / "00_EPISODE_OVERVIEW" / "01-overview.md").read_text()
        match = re.match(r"^# Arda's Stories EP(\d{2}) — ([^\n]+)", overview)
        if not match:
            raise ValueError(f"Cannot read episode identity from {package}")
        new_id = f"AS-EP{match.group(1)}"
        title = match.group(2)
        canonical_characters = []
        shot_source = "\n".join(path.read_text() for path in (package / "01_SHOTS").glob("*.md"))
        for character in ("Arda", "Luca", "Noah"):
            if re.search(rf"^\| Characters \|.*\b{character}\b.*\|$", shot_source, re.M):
                canonical_characters.append(character)
        overview = re.sub(
            r"^\| Characters \|.*?\|$",
            f"| Characters | {', '.join(canonical_characters)} |",
            overview,
            flags=re.M,
        )
        (package / "00_EPISODE_OVERVIEW" / "01-overview.md").write_text(overview)
        for path in package.rglob("*.md"):
            text = path.read_text()
            text = re.sub(r"Climax of Module [ABC]", "Episode climax", text, flags=re.I)
            text = re.sub(r"Module [ABC] cliffhanger", "episode cliffhanger", text, flags=re.I)
            text = re.sub(
                r"continuing from Module [ABC]",
                "continuing from the established episode ambience",
                text,
                flags=re.I,
            )
            text = re.sub(r"\bModule\s+[ABC]\b", "this episode", text, flags=re.I)
            text = text.replace("all 24 shots", "all 8 shots").replace("All 24 shots", "All 8 shots")
            text = text.replace("?.", "?").replace("!.", "!").replace("the the episode", "the episode")
            text = re.sub(r"(?m)^the episode opens", "The episode opens", text)
            if "/01_SHOTS/" in path.as_posix():
                text = re.sub(r"^\| Episode \|.*?\|$", f"| Episode | {new_id} — {title} |", text, flags=re.M)
                if path.name.startswith("shot-01-"):
                    text = re.sub(r"\bShot (?:0[9]|1[0-9]|2[0-4])\b", "the episode opening", text)
                    text = text.replace("Shot 08 final frame", "approved episode-opening frame")
                    text = text.replace("Shot 08 final", "approved episode opening")
                    text = text.replace("the episode opening final frame", "the approved episode-opening frame")
                    if "## Start Frame" in text:
                        text = replace_section(
                            text,
                            "## Start Frame",
                            "Start from an approved episode-opening keyframe created for this standalone package. "
                            "Do not inherit a frame from another episode.",
                        )
                    if "## Reference Usage" in text:
                        text = replace_section(
                            text,
                            "## Reference Usage",
                            "@image1 = approved episode-opening keyframe for this standalone episode.",
                        )
                    if "## Transition Continuity Rule" in text:
                        text = replace_section(
                            text,
                            "## Transition Continuity Rule",
                            "No prior-episode continuity frame is permitted. Begin from this episode's own approved opening keyframe.",
                        )
            if path.name == "03-screenplay.md":
                time_index = 0

                def replace_existing_time(_: re.Match[str]) -> str:
                    nonlocal time_index
                    time_index += 1
                    return f"**Time:** {shot_time(time_index)}"

                text = re.sub(r"(?m)^\*\*Time:\*\* .*?$", replace_existing_time, text)
                text = text.replace("\n---\n\n---\n", "\n---\n")
            if path.name == "QA_CHECKLIST_AND_CONTRAST_TERMS.md":
                text = re.sub(r"^# QA Checklist.*$", f"# QA Checklist and Contrast Terms — {new_id} {title}", text, count=1, flags=re.M)
            if "/03_VIDEO_EXPORTS/openart/" in path.as_posix() and path.name == "shot-01-openart-prompt.md":
                text = re.sub(
                    r"Use @image1 as continuity from Shot \d{2}\.",
                    "Use @image1 as this standalone episode's approved opening keyframe.",
                    text,
                )
            path.write_text(text)


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--normalize-existing":
        normalize_existing()
    else:
        main()
