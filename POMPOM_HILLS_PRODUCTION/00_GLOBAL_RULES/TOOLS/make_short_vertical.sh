#!/bin/bash

# Pompom Hills — Vertical Shorts Converter
# Converts a landscape (16:9) video into a centred 9:16 vertical Short by
# scaling to fill height and cropping the centre — NOT blur-padding.
# This follows POMPOM_HILLS_PRODUCTION/00_GLOBAL_RULES/SHORTS_PRODUCTION_STANDARD.md
# §1 (character must stay CENTRED and CLEAR — no blurred top/bottom bars)
# and §2 (1080x1920, 24fps, H.264, max ~28MB).
#
# Usage: ./make_short_vertical.sh <input.mp4> [output.mp4]
#
# Example:
#   ./make_short_vertical.sh "Kiko's Home Tour.mp4" kikos-home-tour-short.mp4

INPUT="$1"
OUTPUT="$2"

RED='\033[0;31m'; GREEN='\033[0;32m'; NC='\033[0m'
log() { echo -e "${GREEN}[✓]${NC} $1"; }
err() { echo -e "${RED}[✗]${NC} $1"; exit 1; }

if [ -z "$INPUT" ]; then
  echo "Usage: $0 <input.mp4> [output.mp4]"
  exit 1
fi

[ -f "$INPUT" ] || err "Input file not found: $INPUT"
command -v ffmpeg &>/dev/null || err "ffmpeg not found"

if [ -z "$OUTPUT" ]; then
  BASE="$(basename "$INPUT")"
  BASE="${BASE%.*}"
  OUTPUT="$(dirname "$INPUT")/${BASE}-short.mp4"
fi

log "Input:  $INPUT"
log "Output: $OUTPUT"

# Scale to fill 1920 height, then centre-crop to 1080x1920.
# Character stays centred and fully readable — no blur-fill bars top/bottom.
# Bitrate capped so a ~60s clip stays near/under the 28MB Shorts standard.
ffmpeg -y -i "$INPUT" \
  -filter_complex "[0:v]scale=-2:1920,crop=1080:1920,setsar=1[v]" \
  -map "[v]" -map 0:a \
  -c:v libx264 -preset medium -b:v 3300k -maxrate 3600k -bufsize 7200k \
  -pix_fmt yuv420p -r 24 \
  -c:a aac -b:a 128k -ar 48000 \
  -movflags +faststart \
  "$OUTPUT" || err "ffmpeg conversion failed"

DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUTPUT")
SIZE=$(du -h "$OUTPUT" | cut -f1)
echo ""
log "Duration: ${DUR}s"
log "Size: ${SIZE}"
log "Done!"
