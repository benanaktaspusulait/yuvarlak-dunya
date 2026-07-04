#!/bin/bash
# validate-all.sh — Tüm bölümleri validate et
# Kullanım: bash scripts/validate-all.sh
#
# Bölümler artık dünya-bazlı üretim paketlerinde yaşıyor:
#   POMPOM_HILLS_PRODUCTION/02_WORLDS/<WORLD>/04_EPISODE_PACKAGES/<EPISODE>/
#
# Blocking gate  : S01Exx_* paketleri (eski "04-SCENES/season-01/s01e*/" gate'iyle
#                  bire bir aynı kapsam)
# Informational  : ONB_* (Season 2 onboarding taslakları) ve OPA_STORYTIME_*
#                  (bu alt-seri migration öncesi de hiçbir zaman blocking gate'e
#                  girmemişti — mevcut davranış korunuyor, bloklamaz)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PKG_GLOB="$REPO_ROOT/POMPOM_HILLS_PRODUCTION/02_WORLDS/*/04_EPISODE_PACKAGES/*/"

TOTAL=0
PASSED=0
FAILED=0
WARN_EPISODES=0

echo "============================================"
echo "  TÜM BÖLÜMLER QA KONTROLÜ"
echo "  Dizin: POMPOM_HILLS_PRODUCTION/02_WORLDS/*/04_EPISODE_PACKAGES/"
echo "============================================"
echo

ONB_DIRS=()

for dir in $PKG_GLOB; do
    [ -d "$dir" ] || continue
    PKG_NAME=$(basename "$dir")
    WORLD_NAME=$(basename "$(dirname "$(dirname "$dir")")")
    EP_NAME="$WORLD_NAME/$PKG_NAME"

    # Season 2 onboarding (ONB_*) ve Opa's Storytime (OPA_STORYTIME_*) paketleri
    # bilgilendirme amaçlı, blocking gate'e girmez (migration öncesi de girmiyordu).
    if [[ "$PKG_NAME" == ONB_* || "$PKG_NAME" == OPA_STORYTIME_* ]]; then
        ONB_DIRS+=("$dir")
        continue
    fi

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
if [ ${#ONB_DIRS[@]} -gt 0 ]; then
    echo
    echo "--- Season 2 Onboarding (bilgilendirme — bloklamaz) ---"
    for dir in "${ONB_DIRS[@]}"; do
        PKG_NAME=$(basename "$dir")
        WORLD_NAME=$(basename "$(dirname "$(dirname "$dir")")")
        EP_NAME="$WORLD_NAME/$PKG_NAME"
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
