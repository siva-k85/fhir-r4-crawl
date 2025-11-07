# FHIR R4 Documentation Crawler

A comprehensive web crawler for HL7 FHIR R4 documentation, designed to extract and process payer-focused resources (Patient, Coverage, ExplanationOfBenefit) with automated markdown extraction and beautiful PDF documentation generation.

## Overview

This project uses a hybrid approach combining Crawl4AI CLI (for fast inventory scans) and Python API (for precise extraction with custom filters) to:

1. **Inventory**: Scan and catalog all FHIR R4 documentation pages
2. **Shortlist**: Identify payer-relevant resources and shared components
3. **Extract**: Generate clean, LLM-ready markdown for selected pages
4. **Document**: Create comprehensive documentation with publication-quality PDFs
5. **Package**: Bundle everything into a timestamped ZIP deliverable

## Quick Start

### 1. Environment Setup

```bash
# Create virtual environment
python3 -m venv .venv-fhir
source .venv-fhir/bin/activate  # On Windows: .venv-fhir\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup Crawl4AI
crawl4ai-setup
crawl4ai-doctor

# Install Playwright browsers
python -m playwright install --with-deps chromium

# Run setup script
bash scripts/01_setup_environment.sh
```

### 2. Run Full Pipeline

```bash
# Option A: Run all steps sequentially
bash scripts/02_run_inventory.sh
python scripts/03_create_shortlist.py
python scripts/04_extract_markdown.py
python scripts/05_generate_docs_and_pdfs.py
bash scripts/06_package_and_push.sh

# Option B: One-line execution (after setup)
bash scripts/run_all.sh
```

### 3. Outputs

```
output/FHIR_R4_crawl_2025-11-07.zip containing:
├── inventory/
│   ├── links.csv           # URL inventory with metadata
│   └── summary.md          # Statistics and metrics
├── shortlist/
│   ├── urls.txt            # Selected pages
│   └── rationale.md        # Selection criteria
├── extracted/
│   └── markdown/           # Clean markdown files
├── docs/
│   ├── README.md/.pdf      # Methodology documentation
│   ├── PROVENANCE.md/.pdf  # Execution provenance
│   └── CONFIG/             # All configuration files
└── logs/                   # Execution logs
```

## Project Structure

```
fhir-r4-crawl/
├── inventory/              # Step 2: Pre-crawl inventory
├── shortlist/              # Step 3: Shortlisted pages
├── extracted/markdown/     # Step 4: Extracted content
├── docs/                   # Step 5: Documentation
├── logs/                   # Execution logs
├── scripts/                # Automation scripts
├── src/                    # Python source code
└── output/                 # Final deliverables
```

## Key Features

- **Hybrid Architecture**: CLI for speed + Python API for control
- **Smart Filtering**: R4-only (excludes R5, R4B, binaries)
- **Beautiful PDFs**: Publication-quality documentation with syntax highlighting
- **Compliance**: Respects robots.txt and rate limits
- **Reproducible**: All configs, commands, and versions documented
- **GitHub Ready**: Automated push with proper .gitignore

## Technology Stack

- **Crawl4AI 0.7+**: Modern async web crawler optimized for LLMs
- **Playwright**: Headless browser automation
- **WeasyPrint**: HTML/CSS to PDF conversion
- **Pandas**: Data manipulation and CSV generation
- **PyYAML**: Configuration management

## Payer-Focused Scope

### Core Resources
- **Patient**: Demographics and identity management
- **Coverage**: Insurance coverage information
- **ExplanationOfBenefit**: Adjudicated claims (patient-facing)

### Shared Components
- Search capabilities and parameters
- Data types and structures
- Terminologies (CodeSystem, ValueSet)
- Metadata (StructureDefinition)

## Compliance & Ethics

- Custom user agent identifies crawler purpose and contact
- Conservative rate limiting and depth restrictions
- R4-only filtering (no version mixing)
- Robots.txt compliance
- HL7 site terms of use respected

## Timeline

| Step | Duration | Success Rate |
|------|----------|--------------|
| Setup | 5 min | 95% |
| Inventory | 10 min | 95% |
| Shortlist | 10 min | 95% |
| Extraction | 15 min | 90% |
| Documentation | 10 min | 95% |
| Package & Push | 10 min | 90% |

## References

- [Crawl4AI Documentation](https://docs.crawl4ai.com/)
- [HL7 FHIR R4 Specification](https://hl7.org/fhir/R4/)
- [GitHub Repository](https://github.com/siva-k85/fhir-r4-crawl)

## License

MIT License - See LICENSE file for details

## Contact

For questions or issues, please open a GitHub issue or contact: data@symphonycorp.com
