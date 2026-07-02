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
echo "📁 02-WORLDS/ kontrolü..."
for f in 02-WORLDS/*-bible.md; do
    filename=$(basename "$f")
    if [[ ! "$filename" =~ ^[0-9]{2}-[a-z-]+-bible\.md$ ]]; then
        echo "  ❌ HATALI: $filename (beklenen: NN-slug-bible.md)"
        ERRORS=$((ERRORS + 1))
    fi
done

# Sahne dosyaları kontrolü
echo "📁 04-SCENES/ kontrolü..."
for d in 04-SCENES/season-01/s01e*/; do
    dirname=$(basename "$d")
    if [[ ! "$dirname" =~ ^s01e[0-9]{2}-[a-z-]+$ ]]; then
        echo "  ❌ HATALI: $dirname (beklenen: s01eXX-bolum-adi)"
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
