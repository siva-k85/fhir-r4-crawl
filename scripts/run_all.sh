#!/bin/bash
# Master script to run entire FHIR R4 crawler pipeline

set -e

echo "╔═══════════════════════════════════════════════╗"
echo "║  FHIR R4 Documentation Crawler - Full Pipeline  ║"
echo "╚═══════════════════════════════════════════════╝"
echo ""
echo "This will run all 6 steps sequentially:"
echo "  1. Environment setup"
echo "  2. Inventory scan"
echo "  3. Shortlist creation"
echo "  4. Markdown extraction"
echo "  5. Documentation & PDFs"
echo "  6. Package & GitHub prep"
echo ""
echo "Estimated time: 40-50 minutes"
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
echo "▶ Running Step 4: Markdown Extraction"
python scripts/04_extract_markdown.py

# Step 5: Documentation
echo ""
echo "▶ Running Step 5: Documentation & PDFs"
python scripts/05_generate_docs_and_pdfs.py

# Step 6: Package
echo ""
echo "▶ Running Step 6: Package & GitHub Prep"
bash scripts/06_package_and_push.sh

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
echo "  • inventory/links.csv & summary.md"
echo "  • shortlist/urls.txt & rationale.md"
echo "  • extracted/markdown/*.md"
echo "  • docs/README.md & README.pdf"
echo "  • docs/PROVENANCE.md & PROVENANCE.pdf"
echo "  • output/FHIR_R4_crawl_$(date +%Y-%m-%d).zip"
echo ""
echo "Next: Push to GitHub with 'git push -u origin main'"
echo ""
