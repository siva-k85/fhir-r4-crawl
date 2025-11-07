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
if [ ! -f "docs/CONFIG/browser.yml" ] || [ ! -f "docs/CONFIG/crawler.yml" ]; then
    echo "❌ Configuration files not found. Please ensure browser.yml and crawler.yml exist."
    exit 1
fi

# Run Crawl4AI CLI inventory scan
echo "→ Running breadth-first crawl (this may take a few minutes)..."
echo "  Target: https://hl7.org/fhir/R4/"
echo "  Strategy: BFS (breadth-first)"
echo "  Max pages: 400"
echo ""

crwl crawl https://hl7.org/fhir/R4/ \
    -B docs/CONFIG/browser.yml \
    -C docs/CONFIG/crawler.yml \
    --deep-crawl bfs \
    --max-pages 400 \
    -o all \
    > logs/inventory_bfs.json

echo "  ✓ Crawl complete"
echo ""

# Parse JSON to CSV
echo "→ Parsing results to CSV..."
python -m src.inventory_builder logs/inventory_bfs.json inventory

echo ""
echo "═══════════════════════════════════════════════"
echo "  ✅ Inventory generation complete!"
echo "═══════════════════════════════════════════════"
echo ""
echo "Generated files:"
echo "  • logs/inventory_bfs.json (raw output)"
echo "  • inventory/links.csv (parsed links)"
echo "  • inventory/summary.md (statistics)"
echo ""
echo "Next step:"
echo "  python scripts/03_create_shortlist.py"
echo ""
