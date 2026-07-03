#!/bin/bash

# World Bible Validation Script
# Validates all world definitions are upgraded to Living World Bible v3.0 standard

WORLDS_DIR="/Users/benanaktas/project/video/yuvarlak-dunya/02-WORLDS"
ERRORS=0
WARNINGS=0
PASSED=0

echo "============================================"
echo "  WORLD BIBLE VALIDATION SCRIPT"
echo "  Living World Bible v3.0 Standard Check"
echo "============================================"
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Required sections in bible
BIBLE_SECTIONS=(
    "Version 3.0"
    "World Structure"
    "World Zones"
    "Transition Spaces"
    "Spatial Relationships"
    "Character Flow"
    "Living Rules"
    "Production Readiness"
    "World Position"
    "Exterior"
    "Camera Rules"
    "Permanent Objects"
    "Optional Props"
    "Seasonal Changes"
    "Time of Day"
    "Weather"
    "Soundscape"
    "Lighting"
    "Texture"
    "Character Usage"
    "Common Actions"
    "Animation Rules"
    "Story Opportunities"
    "Consistency Checklist"
    "Emotional Purpose"
    "Play Philosophy"
    "Material Language"
    "Quality Checklist"
    "Production Goal"
)

# Required sections in world-spec
SPEC_SECTIONS=(
    "Purpose"
    "Immutable Identity"
    "Visual Identity"
    "World Layout"
    "Spatial Relationships"
    "Playable Areas"
    "Materials"
    "Lighting"
    "Colour Palette"
    "Scale"
    "Atmosphere"
    "Consistency Rules"
    "Generation Considerations"
)

for WORLD_DIR in "$WORLDS_DIR"/*/; do
    WORLD_NAME=$(basename "$WORLD_DIR")
    WORLD_NUM=$(echo "$WORLD_NAME" | cut -d'-' -f1)
    WORLD_SLUG=$(echo "$WORLD_NAME" | sed 's/^[0-9]*-//')
    
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "📂 $WORLD_NAME"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    # Check bible file exists
    BIBLE_FILE=$(find "$WORLD_DIR" -name "*-bible.md" | head -1)
    if [ -z "$BIBLE_FILE" ]; then
        echo -e "  ${RED}✗ BIBLE FILE MISSING${NC}"
        ERRORS=$((ERRORS + 1))
        echo ""
        continue
    fi
    
    # Check world-spec file exists
    SPEC_FILE=$(find "$WORLD_DIR" -name "*-world-spec.md" | head -1)
    if [ -z "$SPEC_FILE" ]; then
        echo -e "  ${YELLOW}⚠ WORLD-SPEC FILE MISSING${NC}"
        WARNINGS=$((WARNINGS + 1))
    else
        echo -e "  ${GREEN}✓ World Spec exists${NC}"
        PASSED=$((PASSED + 1))
    fi
    
    # Check bible version
    if grep -q "Version 3.0" "$BIBLE_FILE"; then
        echo -e "  ${GREEN}✓ Bible v3.0${NC}"
        PASSED=$((PASSED + 1))
    else
        echo -e "  ${RED}✗ Bible NOT v3.0${NC}"
        ERRORS=$((ERRORS + 1))
    fi
    
    # Check bible sections
    echo "  Bible sections:"
    MISSING_BIBLE=0
    for SECTION in "${BIBLE_SECTIONS[@]}"; do
        if grep -qi "$SECTION" "$BIBLE_FILE"; then
            PASSED=$((PASSED + 1))
        else
            echo -e "    ${RED}✗ Missing: $SECTION${NC}"
            ERRORS=$((ERRORS + 1))
            MISSING_BIBLE=$((MISSING_BIBLE + 1))
        fi
    done
    
    if [ $MISSING_BIBLE -eq 0 ]; then
        echo -e "    ${GREEN}✓ All required sections present${NC}"
    fi
    
    # Check world-spec sections
    if [ -n "$SPEC_FILE" ]; then
        echo "  World Spec sections:"
        MISSING_SPEC=0
        for SECTION in "${SPEC_SECTIONS[@]}"; do
            if grep -qi "$SECTION" "$SPEC_FILE"; then
                PASSED=$((PASSED + 1))
            else
                echo -e "    ${RED}✗ Missing: $SECTION${NC}"
                ERRORS=$((ERRORS + 1))
                MISSING_SPEC=$((MISSING_SPEC + 1))
            fi
        done
        
        if [ $MISSING_SPEC -eq 0 ]; then
            echo -e "    ${GREEN}✓ All required sections present${NC}"
        fi
    fi
    
    # Check file size (should be substantial)
    BIBLE_SIZE=$(wc -c < "$BIBLE_FILE")
    if [ "$BIBLE_SIZE" -lt 5000 ]; then
        echo -e "  ${YELLOW}⚠ Bible file small ($BIBLE_SIZE bytes)${NC}"
        WARNINGS=$((WARNINGS + 1))
    else
        echo -e "  ${GREEN}✓ Bible size: $BIBLE_SIZE bytes${NC}"
        PASSED=$((PASSED + 1))
    fi
    
    if [ -n "$SPEC_FILE" ]; then
        SPEC_SIZE=$(wc -c < "$SPEC_FILE")
        if [ "$SPEC_SIZE" -lt 1000 ]; then
            echo -e "  ${YELLOW}⚠ World Spec file small ($SPEC_SIZE bytes)${NC}"
            WARNINGS=$((WARNINGS + 1))
        else
            echo -e "  ${GREEN}✓ World Spec size: $SPEC_SIZE bytes${NC}"
            PASSED=$((PASSED + 1))
        fi
    fi
    
    echo ""
done

echo "============================================"
echo "  VALIDATION SUMMARY"
echo "============================================"
echo ""
echo -e "  ${GREEN}✓ Passed: $PASSED${NC}"
echo -e "  ${RED}✗ Errors: $ERRORS${NC}"
echo -e "  ${YELLOW}⚠ Warnings: $WARNINGS${NC}"
echo ""

if [ $ERRORS -eq 0 ]; then
    echo -e "  ${GREEN}✅ ALL WORLDS VALIDATED SUCCESSFULLY${NC}"
    exit 0
else
    echo -e "  ${RED}❌ VALIDATION FAILED - $ERRORS ERRORS FOUND${NC}"
    exit 1
fi
