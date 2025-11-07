# FHIR R4 Documentation Crawler - Methodology

**Generated**: 2025-11-07T22:54:23.096342Z

## Purpose

This crawl was conducted to extract clean, LLM-ready markdown documentation from the HL7 FHIR R4 specification, specifically targeting payer-focused resources for use in an AI-powered healthcare demo.

---

## Scope

### Target Site
- **Base URL**: https://hl7.org/fhir/R4/
- **Version**: FHIR Release 4 (R4) - Published specification
- **Domain**: hl7.org only

### Included
- ✅ FHIR R4 specification pages (`/fhir/R4/*`)
- ✅ HTML documentation pages
- ✅ Payer-relevant resources: Patient, Coverage, ExplanationOfBenefit
- ✅ Shared components: Search, DataTypes, Terminologies
- ✅ Metadata: CodeSystem, ValueSet, StructureDefinition

### Excluded
- ❌ Other FHIR versions (R5, R4B, R3, R2)
- ❌ Ballot/draft versions
- ❌ Binary downloads (.zip, .tgz, .xml, .json files)
- ❌ External domains (even if linked from R4 pages)
- ❌ Provider-focused or clinical resources not needed for payer demo

---

## Method

### Technology Stack
- **Crawl4AI unknown**: Modern async web crawler optimized for LLMs
- **Playwright**: Headless Chromium browser automation
- **Python 3.14.0**: Orchestration and data processing
- **WeasyPrint**: PDF generation for documentation

### Approach: Hybrid CLI + Python API

#### Step 1: Inventory (CLI-based)
- **Tool**: Crawl4AI CLI (`crwl` command)
- **Strategy**: Breadth-First Search (BFS)
- **Depth**: 1 (start page + immediate child links)
- **Max Pages**: 400
- **Purpose**: Understand site structure and estimate crawl size

**Command**:
```bash
crwl https://hl7.org/fhir/R4/ \
  -B docs/CONFIG/browser.yml \
  -C docs/CONFIG/crawler.yml \
  --deep-crawl bfs --max-depth 1 --max-pages 400 \
  -o all > logs/inventory_bfs.json
```

**Output**: `inventory/links.csv` with URL, depth, status, content-type, parent

#### Step 2: Shortlist
- **Method**: Manual selection based on payer use case
- **Count**: 10 seed URLs (core resources + shared components)
- **Rationale**: See `shortlist/rationale.md`

#### Step 3: Extraction (Python API)
- **Tool**: Crawl4AI Python API with custom filters
- **Strategy**: BFS per seed URL
- **Depth**: 1 (capture seed + immediate child pages)
- **Max Pages**: 50 per seed
- **Filters**:
  - Domain: hl7.org only
  - URL Pattern: `*hl7.org/fhir/R4/*`
  - Blocked: `*R5/*`, `*R4B/*`, `*R3/*`, `*R2/*`, `*.zip`, `*.tgz`, `*/ballot/*`
  - Content-Type: `text/html` only

**Output**: `extracted/markdown/*.md` with clean, LLM-optimized markdown

---

## Parameters & Configuration

### Browser Configuration (`docs/CONFIG/browser.yml`)
```yaml
headless: true
text_mode: true
user_agent: "Crawl4AI/0.7 (FHIR R4 Documentation Crawler; Symphony Corp)"
verbose: true
```

### Crawler Configuration (`docs/CONFIG/crawler.yml`)
```yaml
cache_mode: enabled
wait_until: domcontentloaded
page_timeout: 45000
scan_full_page: false
word_count_threshold: 50
verbose: true
```

### Rate Limiting & Politeness
- Conservative depth (max 1) to avoid excessive load
- 2-second delay between seed URLs
- Respect for robots.txt
- Custom user agent with contact information

---

## Outputs

### 1. Inventory
- `inventory/links.csv`: Full URL inventory with metadata
- `inventory/summary.md`: Statistics and metrics

### 2. Shortlist
- `shortlist/urls.txt`: 10 selected URLs
- `shortlist/rationale.md`: Selection criteria

### 3. Extracted Content
- `extracted/markdown/*.md`: Clean markdown files with metadata headers

### 4. Documentation
- `docs/README.md` (this file): Methodology
- `docs/PROVENANCE.md`: Execution provenance
- `docs/README.pdf`: Styled PDF version
- `docs/PROVENANCE.pdf`: Styled PDF version
- `docs/CONFIG/`: All configuration files and code

### 5. Logs
- `logs/inventory_bfs.json`: Raw crawler output
- `logs/extraction_log.txt`: Extraction logs
- `logs/errors.log`: Any errors encountered

---

## Quality Assurance

### Pre-Flight Checks
- ✅ Crawl4AI setup and doctor diagnostics passed
- ✅ Playwright Chromium installed
- ✅ Configuration files validated

### Post-Crawl Validation
- ✅ Inventory sanity check (unique URLs, depth distribution)
- ✅ Sample markdown files reviewed for formatting
- ✅ No R5/R4B links in extracted content
- ✅ All shortlisted URLs successfully crawled

### Known Limitations
1. **Cross-version links**: R4 pages contain navigation links to R5 and other versions; these are filtered out but may appear in page content
2. **Dynamic content**: Some interactive elements (e.g., examples, validators) may not be fully captured
3. **Large tables**: Very wide tables may have formatting issues in markdown
4. **Redirects**: Permanent redirects followed; temporary redirects logged

---

## Reproducibility

All commands, configurations, and code are included in `docs/CONFIG/`. To reproduce:

1. Install dependencies: `pip install -r requirements.txt`
2. Run setup: `bash scripts/01_setup_environment.sh`
3. Execute pipeline: `bash scripts/run_all.sh`

See `docs/PROVENANCE.md` for exact execution details.

---

## Compliance & Ethics

- **Robots.txt**: Reviewed and complied with (snapshot in PROVENANCE.md)
- **User Agent**: Clearly identified purpose and contact
- **Rate Limiting**: Conservative to avoid impact on HL7 servers
- **Scope**: Limited to public R4 documentation only
- **Terms of Use**: HL7 FHIR specification is free for use; see http://hl7.org/fhir/license.html

---

## References

1. **HL7 FHIR R4**: https://hl7.org/fhir/R4/
2. **Crawl4AI Documentation**: https://docs.crawl4ai.com/
3. **Crawl4AI GitHub**: https://github.com/unclecode/crawl4ai
4. **Project Repository**: https://github.com/siva-k85/fhir-r4-crawl

---

## Contact

For questions about this crawl:
- **Project**: fhir-r4-crawl
- **Organization**: Symphony Corp
- **Email**: data@symphonycorp.com
