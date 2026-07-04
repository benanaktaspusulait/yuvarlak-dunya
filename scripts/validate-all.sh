#!/bin/bash
# validate-all.sh — Tüm bölümleri validate et
# Kullanım: bash scripts/validate-all.sh
#
# Blocking gate  : 04-SCENES/season-01/s01e*   (exit kodunu etkiler)
# Informational  : 04-SCENES/season-02-onboarding/onb-e*  (taslak, bloklamaz)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SCENES_DIR="$REPO_ROOT/04-SCENES/season-01"
ONBOARDING_DIR="$REPO_ROOT/04-SCENES/season-02-onboarding"
# World-based production packages (POMPOM_HILLS_PRODUCTION). Episodes migrated into a
# world package are validated here and remain part of the blocking gate.
PKG_GLOB="$REPO_ROOT/POMPOM_HILLS_PRODUCTION/02_WORLDS/*/04_EPISODE_PACKAGES/*/"

TOTAL=0
PASSED=0
FAILED=0
WARN_EPISODES=0

echo "============================================"
echo "  TÜM BÖLÜMLER QA KONTROLÜ"
echo "  Dizin: $SCENES_DIR"
echo "============================================"
echo

for dir in "$SCENES_DIR"/s01e*/; do
    [ -d "$dir" ] || continue
    EP_NAME=$(basename "$dir")
    TOTAL=$((TOTAL + 1))

    # Validate and capture output
    OUTPUT=$(bash "$SCRIPT_DIR/validate-scene.sh" "$dir" 2>&1)
    EXIT_CODE=$?

    if [ $EXIT_CODE -eq 0 ]; then
        # Uyarı var mı? (hata yok ama ⚠️ mevcut)
        if echo "$OUTPUT" | grep -q "⚠️"; then
            echo "✅ $EP_NAME  (⚠️  uyarılar var)"
            echo "$OUTPUT" | grep "⚠️" | sed 's/^/   /'
            WARN_EPISODES=$((WARN_EPISODES + 1))
        else
            echo "✅ $EP_NAME"
        fi
        PASSED=$((PASSED + 1))
    else
        echo "❌ $EP_NAME"
        FAILED=$((FAILED + 1))
        # Show errors
        echo "$OUTPUT" | grep "❌" | sed 's/^/   /'
    fi
done

# --- World-based episode packages (blocking gate) ---
for dir in $PKG_GLOB; do
    [ -d "$dir" ] || continue
    EP_NAME="$(basename "$(dirname "$(dirname "$dir")")")/$(basename "$dir")"
    TOTAL=$((TOTAL + 1))

    OUTPUT=$(bash "$SCRIPT_DIR/validate-scene.sh" "$dir" 2>&1)
    EXIT_CODE=$?

    if [ $EXIT_CODE -eq 0 ]; then
        if echo "$OUTPUT" | grep -q "⚠️"; then
            echo "✅ $EP_NAME  (⚠️  uyarılar var)"
            echo "$OUTPUT" | grep "⚠️" | sed 's/^/   /'
            WARN_EPISODES=$((WARN_EPISODES + 1))
        else
            echo "✅ $EP_NAME"
        fi
        PASSED=$((PASSED + 1))
    else
        echo "❌ $EP_NAME"
        FAILED=$((FAILED + 1))
        echo "$OUTPUT" | grep "❌" | sed 's/^/   /'
    fi
done

echo
echo "============================================"
echo "  ÖZET (blocking gate)"
echo "============================================"
echo "  Toplam: $TOTAL bölüm"
echo "  ✅ Geçen: $PASSED"
echo "  ❌ Kalan: $FAILED"
echo "  ⚠️  Uyarılı geçen: $WARN_EPISODES"
echo "============================================"

# --- Informational: Season 2 Onboarding (taslaklar, exit kodunu etkilemez) ---
if [ -d "$ONBOARDING_DIR" ]; then
    echo
    echo "--- Season 2 Onboarding (bilgilendirme — bloklamaz) ---"
    for dir in "$ONBOARDING_DIR"/onb-e*/; do
        [ -d "$dir" ] || continue
        EP_NAME=$(basename "$dir")
        OUTPUT=$(bash "$SCRIPT_DIR/validate-scene.sh" "$dir" 2>&1)
        if [ $? -eq 0 ]; then
            echo "✅ $EP_NAME"
        else
            ERRCOUNT=$(echo "$OUTPUT" | grep -oE '[0-9]+ hata' | head -1)
            echo "⚠️  $EP_NAME (taslak — ${ERRCOUNT:-hatalı})"
        fi
    done
    echo "============================================"
fi

exit $FAILED
