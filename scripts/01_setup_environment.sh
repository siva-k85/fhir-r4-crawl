#!/bin/bash
# Setup script for FHIR R4 crawler environment

set -e  # Exit on error

echo "═══════════════════════════════════════════════"
echo "  FHIR R4 Crawler - Environment Setup"
echo "═══════════════════════════════════════════════"
echo ""

# Check Python version
echo "→ Checking Python version..."
python3 --version || { echo "❌ Python 3 not found. Please install Python 3.10+"; exit 1; }

# Create virtual environment
echo "→ Creating virtual environment..."
if [ ! -d ".venv-fhir" ]; then
    python3 -m venv .venv-fhir
    echo "  ✓ Virtual environment created"
else
    echo "  ℹ Virtual environment already exists"
fi

# Activate virtual environment
echo "→ Activating virtual environment..."
source .venv-fhir/bin/activate

# Upgrade pip
echo "→ Upgrading pip..."
pip install --upgrade pip -q

# Install dependencies
echo "→ Installing dependencies..."
pip install -r requirements.txt -q
echo "  ✓ Dependencies installed"

# Setup Crawl4AI
echo "→ Setting up Crawl4AI..."
crawl4ai-setup
echo "  ✓ Crawl4AI setup complete"

# Run diagnostics
echo "→ Running Crawl4AI diagnostics..."
crawl4ai-doctor

# Install Playwright browsers
echo "→ Installing Playwright browsers..."
python -m playwright install --with-deps chromium
echo "  ✓ Playwright chromium installed"

# Create .gitkeep files
echo "→ Creating .gitkeep files..."
touch logs/.gitkeep
touch output/.gitkeep
echo "  ✓ Directory markers created"

echo ""
echo "═══════════════════════════════════════════════"
echo "  ✅ Environment setup complete!"
echo "═══════════════════════════════════════════════"
echo ""
echo "Next steps:"
echo "  1. Activate environment: source .venv-fhir/bin/activate"
echo "  2. Run inventory: bash scripts/02_run_inventory.sh"
echo ""
