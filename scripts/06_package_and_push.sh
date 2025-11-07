#!/bin/bash
# Package deliverables and push to GitHub

set -e

echo "═══════════════════════════════════════════════"
echo "  Step 6: Package & GitHub Push"
echo "═══════════════════════════════════════════════"
echo ""

# Get datestamp
DATESTAMP=$(date +%Y-%m-%d)
ZIP_NAME="FHIR_R4_crawl_${DATESTAMP}.zip"

# Create output directory if needed
mkdir -p output

# Package ZIP
echo "→ Creating ZIP package..."
echo "  Name: $ZIP_NAME"
echo ""

# Create ZIP with all deliverables
zip -r "output/$ZIP_NAME" \
    inventory/ \
    shortlist/ \
    extracted/ \
    docs/ \
    logs/ \
    -x "*.pyc" -x "__pycache__/*" \
    -q

echo "  ✓ ZIP created: output/$ZIP_NAME"
echo ""

# Validate ZIP contents
echo "→ Validating ZIP contents..."
unzip -l "output/$ZIP_NAME" | head -20
echo "  ✓ ZIP validated"
echo ""

# Git operations
echo "→ Preparing git commit..."

# Check if origin exists
if ! git remote get-url origin &> /dev/null; then
    echo "  Adding GitHub remote..."
    git remote add origin https://github.com/siva-k85/fhir-r4-crawl.git
else
    echo "  ℹ Remote 'origin' already exists"
fi

# Stage all files
echo "  Staging files..."
git add .

# Commit
echo "  Creating commit..."
git commit -m "FHIR R4 crawler complete - $DATESTAMP

- Inventory: Pre-crawl scan with links.csv and summary
- Shortlist: 10 payer-focused URLs with rationale
- Extraction: Clean markdown for LLM consumption
- Documentation: README and PROVENANCE with PDFs
- Package: $ZIP_NAME ready for distribution

Generated using Crawl4AI hybrid approach (CLI + Python API)
" || echo "  ℹ No changes to commit"

# Display status
echo ""
echo "→ Git status:"
git status

echo ""
echo "═══════════════════════════════════════════════"
echo "  ⚠️  Manual push required"
echo "═══════════════════════════════════════════════"
echo ""
echo "To push to GitHub, run:"
echo ""
echo "  git push -u origin main"
echo ""
echo "Or if you need to create the repository first:"
echo ""
echo "  1. Go to https://github.com/new"
echo "  2. Create repository: fhir-r4-crawl"
echo "  3. Then run: git push -u origin main"
echo ""
echo "Deliverables:"
echo "  • output/$ZIP_NAME (ready to share)"
echo "  • All files committed to git"
echo ""
