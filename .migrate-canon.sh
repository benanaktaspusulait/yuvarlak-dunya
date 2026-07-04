#!/bin/bash
set -e
cd /Users/benanaktas/project/video/yuvarlak-dunya

move_canon() {
  local src="$1" world="$2"
  local dst="POMPOM_HILLS_PRODUCTION/02_WORLDS/$world"
  echo ">> $src -> $dst"

  for f in "$src"/*; do
    [ -f "$f" ] || continue
    base=$(basename "$f")
    case "$base" in
      *-bible.md|*world-bible.md)
        git mv "$f" "$dst/00_CANON/$base" ;;
      *-world-spec.md|*world-spec.md)
        git mv "$f" "$dst/02_WORLD_SPEC/$base" ;;
      *hero-view*.png|*hero-view*.jpg)
        git mv "$f" "$dst/01_HERO_VIEW/$base" ;;
      *openart-prompt*.md)
        git mv "$f" "$dst/01_HERO_VIEW/$base" ;;
      *)
        # anything unexpected goes to CANON as a catch-all, flagged in output
        echo "   ?? unexpected file, placing in 00_CANON: $base"
        git mv "$f" "$dst/00_CANON/$base" ;;
    esac
  done

  rmdir "$src" 2>/dev/null || rm -rf "$src"
}

move_canon "02-WORLDS/01-central-square" CENTRAL_SQUARE
move_canon "02-WORLDS/02-cloud-hill" CLOUD_HILL
move_canon "02-WORLDS/03-kikos-home" KIKOS_HOME
move_canon "02-WORLDS/04-sun-hill" SUN_HILL
move_canon "02-WORLDS/05-mimis-burrow" MIMIS_BURROW
move_canon "02-WORLDS/06-opas-tree" OPA_TREE
move_canon "02-WORLDS/07-tillos-garden" TILLOS_GARDEN
move_canon "02-WORLDS/08-lulus-greenhouse" LULUS_GREENHOUSE
move_canon "02-WORLDS/09-poppys-bakery" POPPYS_BAKERY
move_canon "02-WORLDS/10-bennys-playground" BENNYS_PLAYGROUND
move_canon "02-WORLDS/11-tillos-treehouse" TILLOS_TREEHOUSE
move_canon "02-WORLDS/12-milos-pond" MILOS_POND
move_canon "02-WORLDS/13-rosies-rose-garden" ROSIES_ROSE_GARDEN
move_canon "02-WORLDS/14-lilys-lavender-farm" LILYS_LAVENDER_FARM
move_canon "02-WORLDS/15-rainbow-bridge" RAINBOW_BRIDGE
move_canon "02-WORLDS/16-friendship-meadow" FRIENDSHIP_MEADOW
move_canon "02-WORLDS/17-butterfly-meadow" BUTTERFLY_MEADOW
move_canon "02-WORLDS/18-little-forest" LITTLE_FOREST
move_canon "02-WORLDS/19-rainbow-creek" RAINBOW_CREEK
move_canon "02-WORLDS/20-wish-pond" WISH_POND
move_canon "02-WORLDS/21-camping-grove" CAMPING_GROVE
move_canon "02-WORLDS/22-story-circle" STORY_CIRCLE
move_canon "02-WORLDS/23-art-corner" ART_CORNER
move_canon "02-WORLDS/24-adventure-trail" ADVENTURE_TRAIL
move_canon "02-WORLDS/25-flower-hill" FLOWER_HILL
move_canon "02-WORLDS/26-tree-hill" TREE_HILL
move_canon "02-WORLDS/27-stone-hill" STONE_HILL
move_canon "02-WORLDS/28-paddle-cove" PADDLE_COVE
move_canon "02-WORLDS/29-pony-meadow" PONY_MEADOW
move_canon "02-WORLDS/30-hobby-horse-trail" HOBBY_HORSE_TRAIL
move_canon "02-WORLDS/31-learning-room" LEARNING_ROOM

echo "ALL WORLD CANON MOVED"
