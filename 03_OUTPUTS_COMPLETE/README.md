# FHIR R4 Extracted Markdown - Output Reference

**Output Type**: Clean, LLM-ready markdown documentation
**Total Files**: 55 validated markdown files
**Total Size**: ~2.7MB
**Format**: Markdown with YAML frontmatter
**Encoding**: UTF-8

---

## Overview

This directory contains **55 high-quality markdown files** extracted from FHIR R4 documentation using a validated hybrid approach:
- **10 shortlist pages** (from official download): Patient, Coverage, ExplanationOfBenefit, and 7 shared components
- **45 auxiliary pages** (from web crawl): Index, modules, foundation, security, terminology, and more

All files have been validated for:
- ✅ Actual FHIR content (no CAPTCHA pages)
- ✅ Substantial content (10.5KB - 699KB per file)
- ✅ Valid UTF-8 encoding
- ✅ YAML metadata frontmatter
- ✅ R4-only content (no version mixing)

---

## File Format

Each markdown file follows this structure:

```markdown
---
url: https://hl7.org/fhir/R4/patient.html
title: Patient
source: official_download | web_crawl
extracted: local_file_conversion | 2025-11-07
depth: 0
---

# Clean markdown content follows

[FHIR logo and navigation]

# 8.1 Resource Patient - Content

Demographics and other administrative information...
```

**Frontmatter Fields**:
- `url`: Original FHIR R4 URL
- `title`: Page title
- `source`: Extraction method (`official_download` or `web_crawl`)
- `extracted`: Conversion type or date
- `depth`: Crawl depth (for web crawl files)

---

## Shortlist Pages (Priority Content)

These 10 pages were specifically curated for payer-focused use cases:

### Core Resources (3 files)

| File | Size | Description |
|------|------|-------------|
| `hl7_org_fhir_R4_patient.md` | 136KB | Patient demographics and administrative information |
| `hl7_org_fhir_R4_coverage.md` | 109KB | Insurance coverage details and relationships |
| `hl7_org_fhir_R4_explanationofbenefit.md` | 699KB | Claims adjudication and payment details |

### Shared Components - Search (2 files)

| File | Size | Description |
|------|------|-------------|
| `hl7_org_fhir_R4_search.md` | 99KB | Search parameter framework and REST API search |
| `hl7_org_fhir_R4_searchparameter.md` | 132KB | Search parameter definitions and usage |

### Shared Components - Data Types (2 files)

| File | Size | Description |
|------|------|-------------|
| `hl7_org_fhir_R4_datatypes.md` | 527KB | Primitive and complex data types |
| `hl7_org_fhir_R4_structuredefinition.md` | 196KB | Resource structure definitions |

### Shared Components - Terminology (3 files)

| File | Size | Description |
|------|------|-------------|
| `hl7_org_fhir_R4_terminologies.md` | 34KB | Code system framework overview |
| `hl7_org_fhir_R4_codesystem.md` | 213KB | Terminology code system resource |
| `hl7_org_fhir_R4_valueset.md` | 263KB | Value set definitions and bindings |

---

## Auxiliary Pages (45 files)

Additional pages successfully extracted via web crawl:

### Foundation & Architecture
- `hl7_org_fhir_R4_index_html.md` - FHIR R4 homepage
- `hl7_org_fhir_R4_foundation-module_html.md` - Base framework
- `hl7_org_fhir_R4_overview_html.md` - Overview and roadmap
- `hl7_org_fhir_R4_overview-arch_html.md` - Architect's introduction
- `hl7_org_fhir_R4_overview-dev_html.md` - Developer's introduction
- `hl7_org_fhir_R4_overview-clinical_html.md` - Clinical introduction
- `hl7_org_fhir_R4_summary_html.md` - Executive summary

### Modules & Organization
- `hl7_org_fhir_R4_implsupport-module_html.md` - Implementer support
- `hl7_org_fhir_R4_exchange-module_html.md` - Exchange mechanisms
- `hl7_org_fhir_R4_conformance-module_html.md` - Conformance framework
- `hl7_org_fhir_R4_terminology-module_html.md` - Terminology module
- `hl7_org_fhir_R4_secpriv-module_html.md` - Security & privacy

### Core Specifications
- `hl7_org_fhir_R4_datatypes_html.md` - Data types (web crawl version)
- `hl7_org_fhir_R4_search_html.md` - Search (web crawl version)
- `hl7_org_fhir_R4_http_html.md` - REST API
- `hl7_org_fhir_R4_json_html.md` - JSON representation
- `hl7_org_fhir_R4_xml_html.md` - XML representation
- `hl7_org_fhir_R4_extensibility_html.md` - Extensions framework
- `hl7_org_fhir_R4_profiling_html.md` - Profiling guide

### Security & Conformance
- `hl7_org_fhir_R4_security_html.md` - Security guidelines
- `hl7_org_fhir_R4_consent_html.md` - Consent resource
- `hl7_org_fhir_R4_auditevent_html.md` - Audit event resource
- `hl7_org_fhir_R4_capabilitystatement_html.md` - Capability statement
- `hl7_org_fhir_R4_implementationguide_html.md` - Implementation guide resource

### Terminology & Code Systems
- `hl7_org_fhir_R4_codesystem_html.md` - Code system (web crawl version)
- `hl7_org_fhir_R4_terminologies-systems_html.md` - Terminology systems
- `hl7_org_fhir_R4_terminology-service_html.md` - Terminology service
- `hl7_org_fhir_R4_conceptmap_html.md` - Concept map resource

### Documentation & Reference
- `hl7_org_fhir_R4_documentation_html.md` - Documentation index
- `hl7_org_fhir_R4_toc_html.md` - Table of contents
- `hl7_org_fhir_R4_resourcelist_html.md` - Complete resource list
- `hl7_org_fhir_R4_operationslist_html.md` - Operations list
- `hl7_org_fhir_R4_downloads_html.md` - Downloads page
- `hl7_org_fhir_R4_license_html.md` - License information
- `hl7_org_fhir_R4_credits_html.md` - Community credits
- `hl7_org_fhir_R4_history_html.md` - Version history

### Exchange & Messaging
- `hl7_org_fhir_R4_messaging_html.md` - Messaging framework
- `hl7_org_fhir_R4_documents_html.md` - Document bundles

### Metadata & Navigation
- `hl7_org_fhir_R4_searchform_html.md` - Search form
- `hl7_org_fhir_R4_versions_html.md` - Version management
- `hl7_org_fhir_R4_versioning_html.md` - Versioning rules
- `hl7_org_fhir_R4_testing_html.md` - Testing guidelines
- `hl7_org_fhir_R4_usecases_html.md` - Use cases
- `hl7_org_fhir_R4_extensibility-registry_html.md` - Extension registry

---

## Usage Examples

### Read Specific Resource Documentation

```bash
# View Patient resource
cat markdown/hl7_org_fhir_R4_patient.md | less

# Extract just the Scope and Usage section
grep -A 50 "## .*Scope and Usage" markdown/hl7_org_fhir_R4_patient.md

# Check file size to confirm substantial content
ls -lh markdown/hl7_org_fhir_R4_patient.md
```

### Search Across All Files

```bash
# Find all mentions of "insurance"
grep -r "insurance" markdown/ | head -20

# Find files discussing search parameters
grep -l "search parameter" markdown/*.md

# Count total lines of documentation
wc -l markdown/*.md | tail -1
```

### List All Files

```bash
# List by size (largest first)
ls -lhS markdown/

# List shortlist pages only
ls -lh markdown/hl7_org_fhir_R4_{patient,coverage,explanationofbenefit,search,searchparameter,datatypes,structuredefinition,terminologies,codesystem,valueset}.md

# Count total files
ls -1 markdown/*.md | wc -l
```

### Extract Metadata

```bash
# Get all source URLs
head -10 markdown/*.md | grep "^url:"

# Check extraction source
head -10 markdown/*.md | grep "^source:"

# Verify no CAPTCHA pages
grep -l "Let's confirm you are human" markdown/*.md
# (should return nothing)
```

---

## Quality Assurance

### File Size Distribution

```bash
# Check file sizes
ls -lh markdown/*.md | awk '{print $5, $9}' | sort -h

# Verify all files > 10KB (no CAPTCHA stubs)
find markdown -name "*.md" -size -10k
# (should return nothing)
```

**Expected Output**:
- Smallest file: ~10.5KB (terminologies.md)
- Largest file: ~699KB (explanationofbenefit.md)
- Average: ~50KB
- No files under 10KB

### Content Validation

```bash
# Verify FHIR headers present
grep -c "Resource.*Content" markdown/hl7_org_fhir_R4_patient.md
# (should be > 0)

# Check for CAPTCHA contamination
grep -c "Let's confirm you are human" markdown/*.md
# (all counts should be 0)

# Validate UTF-8 encoding
file markdown/*.md | grep -v "UTF-8"
# (should return nothing)
```

---

## Integration Examples

### Load into Python

```python
import frontmatter
from pathlib import Path

# Load single file
post = frontmatter.load("markdown/hl7_org_fhir_R4_patient.md")
print(post.metadata)  # {'url': '...', 'title': 'Patient', ...}
print(post.content[:500])  # Markdown content

# Load all files
markdown_dir = Path("markdown")
for md_file in markdown_dir.glob("*.md"):
    post = frontmatter.load(md_file)
    print(f"{post['title']}: {len(post.content)} chars")
```

### Parse with LLM

```python
import openai

# Read Patient resource doc
with open("markdown/hl7_org_fhir_R4_patient.md") as f:
    content = f.read()

# Ask LLM questions
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a FHIR R4 expert."},
        {"role": "user", "content": f"Based on this documentation:\n\n{content}\n\nWhat are the required fields for a Patient resource?"}
    ]
)
```

### Generate Index

```python
import frontmatter
from pathlib import Path

# Generate markdown index
files = sorted(Path("markdown").glob("*.md"))
for f in files:
    post = frontmatter.load(f)
    size_kb = f.stat().st_size // 1024
    print(f"- [{post['title']}]({f.name}) ({size_kb}KB)")
```

---

## File Naming Convention

All files follow the pattern: `hl7_org_fhir_R4_<page-name>_html.md` or `hl7_org_fhir_R4_<page-name>.md`

**Pattern Explanation**:
- `hl7_org_fhir_R4_` - Consistent prefix for domain and version
- `<page-name>` - Original HTML filename without extension
- `_html` - Suffix for web crawl extractions (distinguishes from downloads)
- `.md` - Markdown extension

**Examples**:
- `hl7_org_fhir_R4_patient.md` - From official download
- `hl7_org_fhir_R4_patient_html.md` - From web crawl (different file)
- `hl7_org_fhir_R4_datatypes.md` - Shortlist version (527KB)
- `hl7_org_fhir_R4_datatypes_html.md` - Web crawl version (11KB)

Note: Some pages appear twice (shortlist version + web crawl version). Prefer the larger file from official download.

---

## Troubleshooting

### Empty or Small Files

If you find files under 10KB:
```bash
find markdown -name "*.md" -size -10k -delete
```

These are likely CAPTCHA pages that should have been filtered during validation.

### Missing Files

If shortlist pages are missing:
```bash
# Re-run local HTML conversion
python scripts/08_convert_local_html.py downloads/site markdown/
```

### Encoding Issues

If you encounter encoding errors:
```bash
# Verify UTF-8 encoding
file markdown/*.md

# Convert if needed (should not be necessary)
iconv -f ISO-8859-1 -t UTF-8 input.md > output.md
```

---

## See Also

- [00_MANIFEST.md](../00_MANIFEST.md) - Complete package manifest
- [00_DOCUMENTATION/README.md](../00_DOCUMENTATION/README.md) - Project overview
- [00_DOCUMENTATION/EXTRACTION_METHODOLOGY.md](../00_DOCUMENTATION/EXTRACTION_METHODOLOGY.md) - Detailed methodology
- [01_INPUTS_VALIDATED/shortlist/](../01_INPUTS_VALIDATED/shortlist/) - Shortlist source URLs
- [04_VALIDATION_REPORTS/](../04_VALIDATION_REPORTS/) - Quality validation reports

---

**Output Version**: 1.0
**Generated**: 2025-11-07
**Total Files**: 55 markdown files
**Total Size**: ~2.7MB
**Quality**: ✅ VALIDATED - All files contain actual FHIR content
