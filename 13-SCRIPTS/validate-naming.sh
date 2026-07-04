#!/bin/bash
# validate-naming.sh — NN-slug isimlendirme doğrulama
# Kullanım: ./scripts/validate-naming.sh

echo "=== Pompom Hills Isimlendirme Doğrulama ==="
echo

ERRORS=0

# Karakter dosyaları kontrolü
echo "📁 01-CHARACTERS/ kontrolü..."
for f in 01-CHARACTERS/*.md; do
    filename=$(basename "$f")
    if [[ ! "$filename" =~ ^[0-9]{2}-[a-z]+\.md$ ]] && [ "$filename" != "COMPARISON.md" ]; then
        echo "  ❌ HATALI: $filename (beklenen: NN-slug.md)"
        ERRORS=$((ERRORS + 1))
    fi
done

# Mekan dosyaları kontrolü
# Not: bible dosyaları artık her world'ün kendi alt klasöründe (02-WORLDS/NN-slug/).
echo "📁 02-WORLDS/ kontrolü..."
for f in 02-WORLDS/*/*-bible.md; do
    [ -e "$f" ] || continue
    filename=$(basename "$f")
    if [[ ! "$filename" =~ ^[0-9]{2}-[a-z-]+-bible\.md$ ]]; then
        echo "  ❌ HATALI: $filename (beklenen: NN-slug-bible.md)"
        ERRORS=$((ERRORS + 1))
    fi
done

# Bölüm paketleri kontrolü (world-based production layout)
# Bölümler artık POMPOM_HILLS_PRODUCTION/02_WORLDS/<WORLD>/04_EPISODE_PACKAGES/<PKG>/
# içinde yaşıyor. Paket adı S01Exx_..., ONB_Exx_... veya OPA_STORYTIME_EPxx_... ile
# başlamalı (UPPERCASE_WITH_UNDERSCORES).
echo "📁 POMPOM_HILLS_PRODUCTION/02_WORLDS/*/04_EPISODE_PACKAGES/ kontrolü..."
for d in POMPOM_HILLS_PRODUCTION/02_WORLDS/*/04_EPISODE_PACKAGES/*/; do
    [ -d "$d" ] || continue
    dirname=$(basename "$d")
    if [[ ! "$dirname" =~ ^(S01E|ONB_E|OPA_STORYTIME_EP)[A-Z0-9_]+$ ]]; then
        echo "  ❌ HATALI: $dirname (beklenen: S01Exx_..., ONB_Exx_... veya OPA_STORYTIME_EPxx_...)"
        ERRORS=$((ERRORS + 1))
    fi
done

# AI prompt dosyaları kontrolü
echo "📁 05-AI-PROMPTS/ kontrolü..."
for f in 05-AI-PROMPTS/*.md; do
    filename=$(basename "$f")
    if [[ ! "$filename" =~ ^[A-Z_]+\.md$ ]]; then
        echo "  ❌ HATALI: $filename (beklenen: UPPERCASE.md)"
        ERRORS=$((ERRORS + 1))
    fi
done

echo
if [ $ERRORS -eq 0 ]; then
    echo "✅ Tüm dosya isimleri doğru!"
else
    echo "❌ $ERRORS hata bulundu"
fi

exit $ERRORS
