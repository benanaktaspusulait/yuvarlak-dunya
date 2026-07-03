#!/bin/bash

# World Bible Validation Script
# Validates all world definitions against current production pipeline
# Supports both v3.0 (GLOBAL_ENVIRONMENT_STANDARD) and v4.0 (single Hero View) formats

WORLDS_DIR="/Users/benanaktas/project/video/yuvarlak-dunya/02-WORLDS"
ERRORS=0
WARNINGS=0
PASSED=0

echo "============================================"
echo "  WORLD BIBLE VALIDATION SCRIPT"
echo "  Current Pipeline Check (v3.0 + v4.0)"
echo "============================================"
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

# Core sections required in ALL bibles (both v3.0 and v4.0)
CORE_SECTIONS=(
    "Overview"
    "Purpose"
    "Why This World Exists"
    "Emotional Purpose"
    "Play Philosophy"
    "World Position"
    "Colour Identity"
    "Lighting Identity"
    "Camera Identity"
    "Reusable Assets"
    "Common Generation Failures"
    "Story Opportunities"
    "Production Notes"
    "Consistency Checklist"
    "Changelog"
)

# v3.0 additional sections (old format)
V3_SECTIONS=(
    "Visual Identity"
    "Spatial Layout"
    "Props"
    "Camera Rules"
    "Canonical Prompt Reference Pack"
    "Prompt Generation Rules"
    "Soundscape"
    "Forbidden"
    "World Identity Lock"
    "Hero View Technical Specification"
    "Environmental Sound Identity"
    "Continuity Rules"
    "Production QA"
    "Canonical Reusable Assets"
    "World Navigation"
    "View Transition Rules"
    "Character Occupancy"
    "Typical Episode Usage"
    "Video Generation Rules"
    "Production Summary"
)

# v4.0 additional sections (new format)
V4_SECTIONS=(
    "Generation Workflow"
    "Hero View Creation Mode"
    "Connected Canon Locations"
    "Flower Density"
)

# World-spec sections (both formats)
SPEC_SECTIONS=(
    "Purpose"
    "Identity"
    "Must Preserve"
    "Hero View Composition"
    "Colour Palette"
    "Lighting"
    "Spatial Layout"
    "Playable Areas"
    "Materials"
    "Scale"
    "Atmosphere"
    "Consistency Rules"
    "Reusable Assets"
    "Generation Failures"
    "Video Rules"
)

for WORLD_DIR in "$WORLDS_DIR"/*/; do
    WORLD_NAME=$(basename "$WORLD_DIR")
    
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
    if grep -qi "Version 4\.\|v4\." "$BIBLE_FILE"; then
        echo -e "  ${GREEN}✓ Bible v4.0 (current pipeline)${NC}"
        PASSED=$((PASSED + 1))
    elif grep -qi "Version 3\.\|v3\.\|Version [5-9]\.\|v[5-9]\." "$BIBLE_FILE"; then
        echo -e "  ${CYAN}ℹ Bible v3.0+ (legacy format)${NC}"
        PASSED=$((PASSED + 1))
    else
        echo -e "  ${RED}✗ Bible version unknown${NC}"
        ERRORS=$((ERRORS + 1))
    fi
    
    # Check core sections
    echo "  Core sections:"
    MISSING_CORE=0
    for SECTION in "${CORE_SECTIONS[@]}"; do
        if grep -qi "$SECTION" "$BIBLE_FILE"; then
            PASSED=$((PASSED + 1))
        else
            echo -e "    ${RED}✗ Missing: $SECTION${NC}"
            ERRORS=$((ERRORS + 1))
            MISSING_CORE=$((MISSING_CORE + 1))
        fi
    done
    
    if [ $MISSING_CORE -eq 0 ]; then
        echo -e "    ${GREEN}✓ All core sections present${NC}"
    fi
    
    # Check for outdated multi-reference language
    MULTI_REF=$(grep -ci "max 4 referans\|entrance view.*separate\|trail view.*separate\|detail view.*separate\|reference pack workflow\|4 referans" "$BIBLE_FILE" 2>/dev/null || echo "0")
    if [ "$MULTI_REF" -gt 0 ]; then
        echo -e "  ${YELLOW}⚠ Outdated multi-reference language found ($MULTI_REF instances)${NC}"
        WARNINGS=$((WARNINGS + 1))
    fi
    
    # Check for broken text
    BROKEN=$(grep -ci "preschool安全\|孩子\|Hız$" "$BIBLE_FILE" 2>/dev/null)
    BROKEN=${BROKEN:-0}
    if [ "$BROKEN" -gt 0 ]; then
        echo -e "  ${YELLOW}⚠ Broken/corrupted text found ($BROKEN instances)${NC}"
        WARNINGS=$((WARNINGS + 1))
    fi
    
    # Check Hero View status in metadata
    if grep -q "Hero View:.*❌\|Hero View:.*Pending" "$BIBLE_FILE"; then
        echo -e "  ${CYAN}ℹ Hero View: Pending (expected for unreached worlds)${NC}"
    elif grep -q "Hero View:.*✅" "$BIBLE_FILE"; then
        echo -e "  ${GREEN}✓ Hero View: Approved${NC}"
        PASSED=$((PASSED + 1))
    fi
    
    # Check world-spec sections
    if [ -n "$SPEC_FILE" ]; then
        MISSING_SPEC=0
        for SECTION in "${SPEC_SECTIONS[@]}"; do
            if grep -qi "$SECTION" "$SPEC_FILE"; then
                PASSED=$((PASSED + 1))
            else
                MISSING_SPEC=$((MISSING_SPEC + 1))
            fi
        done
        
        if [ $MISSING_SPEC -eq 0 ]; then
            echo -e "  ${GREEN}✓ World Spec: All sections present${NC}"
        else
            echo -e "  ${YELLOW}⚠ World Spec: $MISSING_SPEC sections missing${NC}"
            WARNINGS=$((WARNINGS + 1))
        fi
    fi
    
    # Check file size
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
