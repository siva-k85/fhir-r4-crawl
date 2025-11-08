#!/bin/bash
# Run inventory scan using Crawl4AI CLI

set -e

echo "═══════════════════════════════════════════════"
echo "  Step 2: Inventory Generation"
echo "═══════════════════════════════════════════════"
echo ""

# Ensure virtual environment is active
if [ -z "$VIRTUAL_ENV" ]; then
    echo "⚠️  Virtual environment not active. Activating..."
    source .venv-fhir/bin/activate
fi

# Check required files
if [ ! -f "02_CONFIGURATION/CONFIG/browser.yml" ] || [ ! -f "02_CONFIGURATION/CONFIG/crawler.yml" ]; then
    echo "❌ Configuration files not found. Please ensure browser.yml and crawler.yml exist in 02_CONFIGURATION/CONFIG/."
    exit 1
fi

# Run Crawl4AI CLI inventory scan
echo "→ Running breadth-first crawl (this may take a few minutes)..."
echo "  Target: https://hl7.org/fhir/R4/"
echo "  Strategy: BFS (breadth-first)"
echo "  Max pages: 400"
echo ""

crwl crawl https://hl7.org/fhir/R4/ \
    -B 02_CONFIGURATION/CONFIG/browser.yml \
    -C 02_CONFIGURATION/CONFIG/crawler.yml \
    --deep-crawl bfs \
    --max-pages 400 \
    -o all \
    > logs/inventory_bfs.json

echo "  ✓ Crawl complete"
echo ""

# Parse JSON to CSV
echo "→ Parsing results to CSV..."
python -m src.inventory_builder logs/inventory_bfs.json 01_INPUTS_VALIDATED/inventory

echo ""
echo "═══════════════════════════════════════════════"
echo "  ✅ Inventory generation complete!"
echo "═══════════════════════════════════════════════"
echo ""
echo "Generated files:"
echo "  • logs/inventory_bfs.json (raw output)"
echo "  • 01_INPUTS_VALIDATED/inventory/links.csv (parsed links)"
echo "  • 01_INPUTS_VALIDATED/inventory/summary.md (statistics)"
echo ""
echo "Next step:"
echo "  python scripts/03_create_shortlist.py"
echo ""
