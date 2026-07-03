#!/bin/bash
# validate-all.sh — Tüm bölümleri validate et
# Kullanım: bash scripts/validate-all.sh

SCENES_DIR="/Users/benanaktas/project/video/yuvarlak-dunya/04-SCENES/season-01"
SCRIPT_DIR="/Users/benanaktas/project/video/yuvarlak-dunya/scripts"

TOTAL=0
PASSED=0
FAILED=0
WARNED=0

echo "============================================"
echo "  TÜM BÖLÜMLER QA KONTROLÜ"
echo "  Dizin: $SCENES_DIR"
echo "============================================"
echo

for dir in "$SCENES_DIR"/s01e*/; do
    EP_NAME=$(basename "$dir")
    TOTAL=$((TOTAL + 1))
    
    # Validate and capture output
    OUTPUT=$(bash "$SCRIPT_DIR/validate-scene.sh" "$dir" 2>&1)
    EXIT_CODE=$?
    
    if [ $EXIT_CODE -eq 0 ]; then
        echo "✅ $EP_NAME"
        PASSED=$((PASSED + 1))
    else
        echo "❌ $EP_NAME"
        FAILED=$((FAILED + 1))
        # Show errors
        echo "$OUTPUT" | grep "❌" | sed 's/^/   /'
    fi
done

echo
echo "============================================"
echo "  ÖZET"
echo "============================================"
echo "  Toplam: $TOTAL bölüm"
echo "  ✅ Geçen: $PASSED"
echo "  ❌ Geçen: $FAILED"
echo "============================================"

exit $FAILED
