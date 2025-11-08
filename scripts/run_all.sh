#!/bin/bash
# Master script to run entire FHIR R4 crawler pipeline

set -e

echo "╔═══════════════════════════════════════════════╗"
echo "║  FHIR R4 Documentation Crawler - Full Pipeline  ║"
echo "╚═══════════════════════════════════════════════╝"
echo ""
echo "This will run all 5 steps sequentially:"
echo "  1. Environment setup"
echo "  2. Inventory scan"
echo "  3. Shortlist creation"
echo "  4. Markdown extraction (web crawl)"
echo "  5. Local HTML conversion (from official download)"
echo ""
echo "Estimated time: 20-30 minutes"
echo ""
read -p "Continue? (y/n) " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Cancelled."
    exit 0
fi

START_TIME=$(date +%s)

# Step 1: Setup
echo ""
echo "▶ Running Step 1: Environment Setup"
bash scripts/01_setup_environment.sh

# Activate environment for remaining steps
source .venv-fhir/bin/activate

# Step 2: Inventory
echo ""
echo "▶ Running Step 2: Inventory Scan"
bash scripts/02_run_inventory.sh

# Step 3: Shortlist
echo ""
echo "▶ Running Step 3: Shortlist Creation"
python scripts/03_create_shortlist.py

# Step 4: Extraction
echo ""
echo "▶ Running Step 4: Markdown Extraction (Web Crawl)"
python scripts/04_extract_markdown.py

# Step 5: Local HTML Conversion
echo ""
echo "▶ Running Step 5: Local HTML Conversion"
# Note: Requires fhir-spec.zip to be downloaded and extracted to downloads/site
if [ -d "downloads/site" ]; then
    python scripts/08_convert_local_html.py downloads/site 03_OUTPUTS_COMPLETE/markdown
else
    echo "⚠️  Skipping: downloads/site not found. Download fhir-spec.zip first."
fi

# Calculate duration
END_TIME=$(date +%s)
DURATION=$((END_TIME - START_TIME))
MINUTES=$((DURATION / 60))
SECONDS=$((DURATION % 60))

echo ""
echo "╔═══════════════════════════════════════════════╗"
echo "║  ✅ FHIR R4 Crawler Pipeline Complete!          ║"
echo "╚═══════════════════════════════════════════════╝"
echo ""
echo "Duration: ${MINUTES}m ${SECONDS}s"
echo ""
echo "Outputs:"
echo "  • 01_INPUTS_VALIDATED/inventory/ (links.csv, summary.md)"
echo "  • 01_INPUTS_VALIDATED/shortlist/ (urls.txt, rationale.md)"
echo "  • 03_OUTPUTS_COMPLETE/markdown/*.md (55 files)"
echo "  • 00_DOCUMENTATION/ (README.md, PROVENANCE.md, EXTRACTION_METHODOLOGY.md)"
echo "  • 04_VALIDATION_REPORTS/ (comprehensive + critical issues)"
echo ""
echo "Next: Review outputs and push to GitHub"
echo ""
