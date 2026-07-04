import os, re, sys

# world dir slug -> WORLD_NAME
world_map = {
"01-central-square": "CENTRAL_SQUARE",
"02-cloud-hill": "CLOUD_HILL",
"03-kikos-home": "KIKOS_HOME",
"04-sun-hill": "SUN_HILL",
"05-mimis-burrow": "MIMIS_BURROW",
"06-opas-tree": "OPA_TREE",
"07-tillos-garden": "TILLOS_GARDEN",
"08-lulus-greenhouse": "LULUS_GREENHOUSE",
"09-poppys-bakery": "POPPYS_BAKERY",
"10-bennys-playground": "BENNYS_PLAYGROUND",
"11-tillos-treehouse": "TILLOS_TREEHOUSE",
"12-milos-pond": "MILOS_POND",
"13-rosies-rose-garden": "ROSIES_ROSE_GARDEN",
"14-lilys-lavender-farm": "LILYS_LAVENDER_FARM",
"15-rainbow-bridge": "RAINBOW_BRIDGE",
"16-friendship-meadow": "FRIENDSHIP_MEADOW",
"17-butterfly-meadow": "BUTTERFLY_MEADOW",
"18-little-forest": "LITTLE_FOREST",
"19-rainbow-creek": "RAINBOW_CREEK",
"20-wish-pond": "WISH_POND",
"21-camping-grove": "CAMPING_GROVE",
"22-story-circle": "STORY_CIRCLE",
"23-art-corner": "ART_CORNER",
"24-adventure-trail": "ADVENTURE_TRAIL",
"25-flower-hill": "FLOWER_HILL",
"26-tree-hill": "TREE_HILL",
"27-stone-hill": "STONE_HILL",
"28-paddle-cove": "PADDLE_COVE",
"29-pony-meadow": "PONY_MEADOW",
"30-hobby-horse-trail": "HOBBY_HORSE_TRAIL",
"31-learning-room": "LEARNING_ROOM",
}

def new_base(world_slug, world_name, filename):
    """Given old filename inside a world folder, compute new relative path (subfolder/filename)."""
    if filename.endswith("-bible.md") or filename == "01-world-bible.md":
        return f"00_CANON/{filename}"
    if filename.endswith("-world-spec.md") or filename == "02-world-spec.md":
        return f"02_WORLD_SPEC/{filename}"
    if "hero-view" in filename or "openart-prompt" in filename:
        return f"01_HERO_VIEW/{filename}"
    return None

# Build replacement patterns: most specific first (full file path), then bare dir.
replacements = []  # list of (regex, replacement)

for slug, name in world_map.items():
    base_old = f"02-WORLDS/{slug}"
    base_new = f"POMPOM_HILLS_PRODUCTION/02_WORLDS/{name}"
    # full path with filename e.g. 02-WORLDS/06-opas-tree/06-opas-tree-bible.md
    replacements.append((re.compile(re.escape(base_old) + r"/([A-Za-z0-9_.\-]+\.(?:md|png|jpg))"),
                          lambda m, base_new=base_new, slug=slug, name=name: base_new + "/" + (new_base(slug, name, m.group(1)) or m.group(1))))
    # bare dir reference with trailing slash
    replacements.append((re.compile(re.escape(base_old) + r"/(?!\S)"), base_new + "/"))
    # bare dir reference with trailing slash immediately before closing backtick/paren/quote
    replacements.append((re.compile(re.escape(base_old) + r"/(?=[`'\")\]])"), base_new + "/"))
    # bare dir reference without trailing slash (word boundary)
    replacements.append((re.compile(re.escape(base_old) + r"\b(?!/)"), base_new))

# generic 02-WORLDS/ (catch remaining, must run AFTER specific ones)
generic = (re.compile(r"02-WORLDS/"), "POMPOM_HILLS_PRODUCTION/02_WORLDS/")

EXCLUDE_DIRS = {".git"}
EXCLUDE_FILES = {".fix-refs.py", ".build-map.py", ".path-map.txt", ".migrate-canon.sh"}

changed_files = []
for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
    for fn in files:
        if fn in EXCLUDE_FILES:
            continue
        if not (fn.endswith(".md") or fn.endswith(".sh") or fn.endswith(".py") or fn.endswith(".yml")):
            continue
        path = os.path.join(root, fn)
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception:
            continue
        orig = content
        for pattern, repl in replacements:
            if callable(repl):
                content = pattern.sub(repl, content)
            else:
                content = pattern.sub(repl, content)
        # catch-all for any remaining bare 02-WORLDS/
        content = generic[0].sub(generic[1], content)
        if content != orig:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            changed_files.append(path)

print(f"Changed {len(changed_files)} files")
for p in changed_files:
    print(" -", p)
