#!/bin/bash
# ============================================================
# Pompom Hills — S01E06 The Soft Wind — Video Assembly (v2)
# Finds all shot-*.mp4 files in this folder and joins them
# DIRECTLY, with NO black gap between shots (seamless concat).
# Adapted from assemble_s01e06_shots.sh
# ============================================================

OUTPUT_NAME="s01e06-the-soft-wind-all-shots-nogap.mp4"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
OUTPUT_PATH="${SCRIPT_DIR}/${OUTPUT_NAME}"

RED='\033[0;31m'; GREEN='\033[0;32m'; NC='\033[0m'
log() { echo -e "${GREEN}[✓]${NC} $1"; }
err() { echo -e "${RED}[✗]${NC} $1"; exit 1; }

command -v ffmpeg &>/dev/null || err "ffmpeg not found"

# Find all shot videos, sorted naturally
SHOTS=($(ls "${SCRIPT_DIR}"/shot-*.mp4 "${SCRIPT_DIR}"/shot0*.mp4 2>/dev/null | grep -v 'all-shots' | sort -t'-' -k2 -n))
[ ${#SHOTS[@]} -eq 0 ] && err "No shot-*.mp4 files found"
log "Found ${#SHOTS[@]} shots:"
for s in "${SHOTS[@]}"; do log "  $(basename "$s")"; done

# Get video properties from first shot
SR=$(ffprobe -v error -select_streams a:0 -show_entries stream=sample_rate -of csv=p=0 "${SHOTS[0]}")
CH=$(ffprobe -v error -select_streams a:0 -show_entries stream=channels -of csv=p=0 "${SHOTS[0]}")

# Temp files
TCONCAT="${SCRIPT_DIR}/.tmp_concat_nogap.txt"
trap 'rm -f "$TCONCAT"' EXIT

# Build concat file: shot1 + shot2 + ... + shotN (NO gaps)
log "Building concat list (no gaps)..."
> "$TCONCAT"
for s in "${SHOTS[@]}"; do
    echo "file '${s}'" >> "$TCONCAT"
done

log "Concatenating ${#SHOTS[@]} shots directly (seamless)..."
ffmpeg -y -hide_banner -loglevel warning \
    -f concat -safe 0 -i "$TCONCAT" \
    -c:v libx264 -pix_fmt yuv420p \
    -c:a aac -ar "$SR" -ac "$CH" \
    "$OUTPUT_PATH" || err "Concat failed"

DUR=$(ffprobe -v error -select_streams v:0 -show_entries format=duration -of csv=p=0 "$OUTPUT_PATH")
echo ""
log "Output: ${OUTPUT_PATH}"
log "Duration: ${DUR}s"
log "Done (no black gaps)!"
