# FHIR R4 URL Discovery Guide

**Version**: 1.0
**Date**: November 8, 2025
**Author**: Symphony Corp
**Purpose**: Step-by-step tutorial for discovering and analyzing FHIR R4 URLs using pre-crawl methodology

---

## Quick Start

```bash
# 1. Discover all FHIR R4 URLs
python scripts/pre_crawl_discovery.py --domain hl7.org --pattern "*/fhir/R4/*"

# 2. Categorize discovered URLs
python scripts/url_categorizer.py --input outputs/discovered_urls.csv

# 3. Filter for your project
python scripts/project_filter.py --project andor --config configs/andor_crawl_config.yml

# 4. Estimate costs
python scripts/cost_estimator.py --urls outputs/andor_filtered_urls.csv
```

Expected time: 10-15 minutes total

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation and Setup](#installation-and-setup)
3. [Step 1: URL Discovery](#step-1-url-discovery)
4. [Step 2: Metadata Extraction](#step-2-metadata-extraction)
5. [Step 3: Categorization](#step-3-categorization)
6. [Step 4: Project Filtering](#step-4-project-filtering)
7. [Step 5: Depth Optimization](#step-5-depth-optimization)
8. [Step 6: Cost Estimation](#step-6-cost-estimation)
9. [Interpreting Results](#interpreting-results)
10. [Troubleshooting](#troubleshooting)
11. [Advanced Usage](#advanced-usage)
12. [Performance Tuning](#performance-tuning)

---

## Prerequisites

### System Requirements

- Python 3.11 or higher
- 4GB RAM minimum
- 10GB free disk space
- Stable internet connection (10+ Mbps recommended)

### Python Environment

```bash
# Check Python version
python --version  # Should be 3.11+

# Create virtual environment
python -m venv .venv-fhir
source .venv-fhir/bin/activate  # On Windows: .venv-fhir\Scripts\activate
```

### Required Packages

```bash
# Install dependencies
pip install crawl4ai>=0.7.6
pip install pandas>=2.1.0
pip install pyyaml>=6.0
pip install aiohttp>=3.9.0
pip install scikit-learn>=1.3.0  # For BM25 scoring
```

---

## Installation and Setup

### Step 1: Clone or Update Repository

```bash
# If starting fresh
git clone https://github.com/siva-k85/fhir-r4-crawl.git
cd fhir-r4-crawl

# If updating existing
git pull origin main
```

### Step 2: Verify Directory Structure

```bash
# Create necessary directories
mkdir -p 02_CONFIGURATION/configs
mkdir -p outputs
mkdir -p logs

# Verify structure
tree -L 2
```

Expected structure:
```
fhir-r4-crawl/
├── 00_DOCUMENTATION/
├── 01_INPUTS_VALIDATED/
├── 02_CONFIGURATION/
│   └── configs/
├── 03_OUTPUTS_COMPLETE/
├── logs/
├── outputs/
└── scripts/
```

### Step 3: Configure Environment

```bash
# Create configuration file
cat > .env << EOF
# Optional: API keys if needed
COMMON_CRAWL_API_KEY=your_key_here  # If using Common Crawl API
LOG_LEVEL=INFO
MAX_CONCURRENT_REQUESTS=20
EOF
```

---

## Step 1: URL Discovery

### Basic Discovery

Run the discovery script to find all FHIR R4 URLs:

```bash
python scripts/pre_crawl_discovery.py \
    --domain hl7.org \
    --pattern "*/fhir/R4/*" \
    --source sitemap
```

### Advanced Discovery with Common Crawl

```bash
python scripts/pre_crawl_discovery.py \
    --domain hl7.org \
    --pattern "*/fhir/R4/*" \
    --source "sitemap+cc" \
    --max-urls 10000 \
    --output outputs/discovered_urls.csv
```

### Discovery Options

| Option | Description | Default | Example |
|--------|-------------|---------|---------|
| `--domain` | Target domain | Required | `hl7.org` |
| `--pattern` | URL pattern filter | `*` | `*/fhir/R4/*` |
| `--source` | Discovery source | `sitemap` | `sitemap+cc` |
| `--max-urls` | Maximum URLs to discover | 10000 | 5000 |
| `--exclude` | Patterns to exclude | None | `*example*,*test*` |
| `--output` | Output CSV file | `outputs/discovered_urls.csv` | Custom path |
| `--cache` | Use cached results | `true` | `false` |

### Expected Output

```
Starting URL discovery for hl7.org...
Source: sitemap
Pattern: */fhir/R4/*

[Phase 1: Sitemap Discovery]
✓ Found sitemap at: https://hl7.org/sitemap.xml
✓ Parsing sitemap entries...
✓ Found 5,432 total URLs
✓ Filtered to 2,145 R4 URLs

[Phase 2: Validation]
✓ Checking URL accessibility...
✓ Valid URLs: 1,987
✓ Invalid/404: 158

Discovery complete!
- Total URLs discovered: 1,987
- Time elapsed: 45 seconds
- Output saved to: outputs/discovered_urls.csv
```

### Output File Format

`outputs/discovered_urls.csv`:
```csv
url,discovered_from,timestamp,status
https://hl7.org/fhir/R4/patient.html,sitemap,2025-11-08T10:00:00Z,valid
https://hl7.org/fhir/R4/coverage.html,sitemap,2025-11-08T10:00:01Z,valid
https://hl7.org/fhir/R4/modules.html,cc,2025-11-08T10:00:02Z,valid
```

---

## Step 2: Metadata Extraction

### Extract HEAD Metadata

```bash
python scripts/pre_crawl_discovery.py \
    --input outputs/discovered_urls.csv \
    --extract-head \
    --output outputs/urls_with_metadata.csv
```

### Extraction Process

```
[Metadata Extraction]
Loading 1,987 URLs from outputs/discovered_urls.csv...

Processing batch 1/20 (100 URLs)...
[████████████████████████] 100% Complete
Rate: 15.3 URLs/sec

Processing batch 2/20 (100 URLs)...
[████████████████████████] 100% Complete
Rate: 14.8 URLs/sec

...

Extraction Summary:
- Total URLs: 1,987
- Successful: 1,843 (92.8%)
- Failed: 144 (7.2%)
- Time elapsed: 3 minutes 12 seconds
- Average rate: 10.3 URLs/sec
```

### Metadata Fields Extracted

| Field | Description | Example |
|-------|-------------|---------|
| `title` | Page title | "Patient - FHIR v4.0.1" |
| `description` | Meta description | "Demographics and other administrative information" |
| `og:type` | OpenGraph type | "website" |
| `og:title` | OpenGraph title | "Patient Resource" |
| `keywords` | SEO keywords | "fhir,patient,resource" |
| `content-type` | MIME type | "text/html; charset=utf-8" |
| `canonical` | Canonical URL | "https://hl7.org/fhir/R4/patient.html" |

### Enhanced Output

`outputs/urls_with_metadata.csv`:
```csv
url,title,description,og_type,keywords,content_type,canonical,status
https://hl7.org/fhir/R4/patient.html,Patient - FHIR v4.0.1,Demographics and other administrative information,website,fhir patient resource,text/html,https://hl7.org/fhir/R4/patient.html,valid
```

---

## Step 3: Categorization

### Run Categorization

```bash
python scripts/url_categorizer.py \
    --input outputs/urls_with_metadata.csv \
    --output outputs/categorized_urls.csv
```

### Categorization Logic

The script categorizes URLs into:

1. **Resources** (`patient.html`, `coverage.html`)
2. **Modules** (`administration-module.html`)
3. **Implementation** (`datatypes.html`, `search.html`)
4. **ValueSets** (`valueset-*.html`)
5. **Examples** (`*-examples.html`)
6. **Other** (uncategorized)

### Categorization Output

```
[URL Categorization]
Loading 1,843 URLs with metadata...

Categorizing URLs...
✓ Resources: 485 URLs
✓ Modules: 52 URLs
✓ Implementation: 287 URLs
✓ ValueSets: 623 URLs
✓ Examples: 312 URLs
✓ Other: 84 URLs

Category Statistics:
┌─────────────────┬───────┬────────┐
│ Category        │ Count │ Percent│
├─────────────────┼───────┼────────┤
│ Resources       │   485 │  26.3% │
│ ValueSets       │   623 │  33.8% │
│ Examples        │   312 │  16.9% │
│ Implementation  │   287 │  15.6% │
│ Modules         │    52 │   2.8% │
│ Other           │    84 │   4.6% │
└─────────────────┴───────┴────────┘

Subcategory Breakdown (Top 10):
- patient: 12 URLs
- coverage: 8 URLs
- observation: 15 URLs
- medication: 22 URLs
...

Output saved to: outputs/categorized_urls.csv
```

### Categorized File Structure

`outputs/categorized_urls.csv`:
```csv
url,title,category,subcategory,priority,depth_recommendation
https://hl7.org/fhir/R4/patient.html,Patient,resource,patient,high,0
https://hl7.org/fhir/R4/administration-module.html,Administration Module,module,administration,medium,1
https://hl7.org/fhir/R4/valueset-address-use.html,AddressUse,valueset,address-use,medium,1
```

---

## Step 4: Project Filtering

### Filter for Andor Health System

```bash
python scripts/project_filter.py \
    --project andor \
    --input outputs/categorized_urls.csv \
    --config configs/andor_crawl_config.yml \
    --output outputs/andor_filtered_urls.csv
```

### Filter for WHIO APCD

```bash
python scripts/project_filter.py \
    --project whio \
    --input outputs/categorized_urls.csv \
    --config configs/whio_crawl_config.yml \
    --output outputs/whio_filtered_urls.csv
```

### Filtering Process

```
[Project Filtering: Andor]
Loading configuration: configs/andor_crawl_config.yml
Input URLs: 1,843

Applying BM25 scoring...
Queries:
1. "patient practitioner organization clinical observation"
2. "quality measure reporting measurereport"
3. "US Core implementation guide"
4. "bulk data export operation"

Scoring complete. Score distribution:
- High (>0.7): 187 URLs
- Medium (0.4-0.7): 423 URLs
- Low (<0.4): 1,233 URLs

Applying filters...
✓ Required resources: 145 URLs included
✓ Score threshold (0.3): 610 URLs pass
✓ Pattern matching: 578 URLs match
✓ Category limits applied

Final Results:
- Total filtered: 512 URLs
- By category:
  • Resources: 185
  • Modules: 42
  • Implementation: 98
  • ValueSets: 145
  • Examples: 42

Output saved to: outputs/andor_filtered_urls.csv
```

### Project Comparison

```bash
# Compare both projects
python scripts/project_filter.py --compare andor whio

Project Comparison:
┌──────────────┬────────┬──────┐
│ Metric       │ Andor  │ WHIO │
├──────────────┼────────┼──────┤
│ Total URLs   │   512  │  287 │
│ Resources    │   185  │  124 │
│ Modules      │    42  │   18 │
│ Implementation│    98  │   65 │
│ ValueSets    │   145  │   68 │
│ Examples     │    42  │   12 │
├──────────────┼────────┼──────┤
│ Avg Score    │  0.54  │ 0.61 │
│ High Priority│   187  │  142 │
└──────────────┴────────┴──────┘
```

---

## Step 5: Depth Optimization

### Assign Crawl Depths

```bash
python scripts/depth_optimizer.py \
    --input outputs/andor_filtered_urls.csv \
    --config configs/andor_crawl_config.yml \
    --output outputs/andor_urls_with_depth.csv
```

### Depth Assignment Logic

```
[Depth Optimization]
Loading 512 filtered URLs...
Applying depth strategy from config...

Depth Assignment Rules:
- Required resources: depth 0
- High score (>0.7): depth +1
- Category defaults:
  • Resources: 0
  • Modules: 1
  • Implementation: 1
  • ValueSets: 1
  • Examples: 2

Processing URLs...
[████████████████████████] 100% Complete

Depth Distribution:
┌────────┬───────┬─────────┐
│ Depth  │ Count │ Percent │
├────────┼───────┼─────────┤
│ 0      │  203  │  39.6%  │
│ 1      │  215  │  42.0%  │
│ 2      │   94  │  18.4%  │
│ 3      │    0  │   0.0%  │
└────────┴───────┴─────────┘

Estimated crawl expansion:
- Depth 0: 203 seed URLs only
- Depth 1: ~2,150 URLs (10 children each)
- Depth 2: ~4,700 URLs (50 grandchildren each)
Total estimated: ~7,053 URLs to crawl

Output saved to: outputs/andor_urls_with_depth.csv
```

### Depth Optimization Output

`outputs/andor_urls_with_depth.csv`:
```csv
url,title,category,score,depth,estimated_children
https://hl7.org/fhir/R4/patient.html,Patient,resource,0.92,0,0
https://hl7.org/fhir/R4/us-core-patient.html,US Core Patient,resource,0.88,1,12
https://hl7.org/fhir/R4/patient-examples.html,Patient Examples,example,0.45,2,25
```

---

## Step 6: Cost Estimation

### Estimate Crawl Costs

```bash
python scripts/cost_estimator.py \
    --urls outputs/andor_urls_with_depth.csv \
    --output outputs/andor_cost_estimate.json
```

### Cost Calculation Output

```
[Cost Estimation]
Loading 512 URLs with depth assignments...

Time Estimation:
┌─────────────────┬──────────┐
│ Component       │ Time     │
├─────────────────┼──────────┤
│ Discovery       │ 1 min    │
│ HEAD Extraction │ 2 min    │
│ Depth 0 Crawl   │ 7 min    │
│ Depth 1 Crawl   │ 36 min   │
│ Depth 2 Crawl   │ 24 min   │
├─────────────────┼──────────┤
│ Total Serial    │ 70 min   │
│ Concurrent (5x) │ 14 min   │
└─────────────────┴──────────┘

Token Estimation:
┌──────────────┬────────────┬──────┐
│ Category     │ Tokens     │ Cost │
├──────────────┼────────────┼──────┤
│ Resources    │   925,000  │ $9.25│
│ Modules      │   315,000  │ $3.15│
│ Implementation│   392,000  │ $3.92│
│ ValueSets    │   217,500  │ $2.18│
│ Examples     │   168,000  │ $1.68│
├──────────────┼────────────┼──────┤
│ Total        │ 2,017,500  │$20.18│
└──────────────┴────────────┴──────┘

Comparison with Full Crawl:
- Full crawl (1,987 URLs): $59.61
- Filtered crawl (512 URLs): $20.18
- Savings: $39.43 (66.2%)

Cost breakdown saved to: outputs/andor_cost_estimate.json
```

### Cost Report JSON

`outputs/andor_cost_estimate.json`:
```json
{
  "project": "andor",
  "urls": {
    "total": 512,
    "by_depth": {
      "0": 203,
      "1": 215,
      "2": 94
    }
  },
  "time": {
    "discovery_minutes": 1,
    "extraction_minutes": 2,
    "crawl_minutes": 11,
    "total_minutes": 14
  },
  "tokens": {
    "total": 2017500,
    "by_category": {
      "resources": 925000,
      "modules": 315000,
      "implementation": 392000,
      "valuesets": 217500,
      "examples": 168000
    }
  },
  "cost_usd": {
    "total": 20.18,
    "per_url": 0.039,
    "savings_vs_full": 39.43
  }
}
```

---

## Interpreting Results

### Understanding Scores

BM25 scores range from 0.0 to 1.0:

| Score Range | Interpretation | Action |
|-------------|---------------|--------|
| 0.8 - 1.0 | Highly relevant | Always include, depth 0-1 |
| 0.5 - 0.8 | Relevant | Include if under limit, depth 1 |
| 0.3 - 0.5 | Somewhat relevant | Include selectively, depth 0-1 |
| 0.0 - 0.3 | Low relevance | Exclude unless required |

### Category Priorities

| Category | Andor Priority | WHIO Priority | Typical Depth |
|----------|---------------|---------------|---------------|
| Resources | High | High | 0 |
| Modules | Medium | Low | 1 |
| Implementation | High | Medium | 0-1 |
| ValueSets | Medium | Medium | 1 |
| Examples | Low | Very Low | 2 |

### Depth Impact

| Depth | URLs Crawled | Time Multiplier | Token Multiplier |
|-------|--------------|-----------------|------------------|
| 0 | 1x (seed only) | 1x | 1x |
| 1 | ~10x | 2.5x | 2.5x |
| 2 | ~50x | 7.5x | 5x |
| 3 | ~200x | 20x | 10x |

---

## Troubleshooting

### Common Issues and Solutions

#### Issue: Discovery returns 0 URLs

```bash
# Check domain accessibility
curl -I https://hl7.org/sitemap.xml

# Try alternative source
python scripts/pre_crawl_discovery.py --source cc --domain hl7.org

# Check logs
tail -f logs/pre_crawl.log
```

#### Issue: HEAD extraction fails

```bash
# Reduce concurrency
python scripts/pre_crawl_discovery.py --max-concurrent 5

# Increase timeout
python scripts/pre_crawl_discovery.py --timeout 30

# Skip failed URLs
python scripts/pre_crawl_discovery.py --skip-errors
```

#### Issue: Low relevance scores

```bash
# Adjust queries in config
vim configs/andor_crawl_config.yml

# Lower threshold
python scripts/project_filter.py --threshold 0.2

# Check query matching
python scripts/project_filter.py --debug --show-scores
```

#### Issue: Memory errors with large URL sets

```bash
# Process in batches
python scripts/pre_crawl_discovery.py --batch-size 500

# Clear cache
rm -rf .cache/

# Increase memory limit
export PYTHONMAXMEM=4G
```

### Debug Mode

Enable detailed logging:

```bash
# Set debug environment
export LOG_LEVEL=DEBUG

# Run with verbose output
python scripts/pre_crawl_discovery.py -v

# Save debug output
python scripts/pre_crawl_discovery.py 2>&1 | tee debug.log
```

### Validation Checks

```bash
# Validate discovered URLs
python scripts/validate_urls.py outputs/discovered_urls.csv

# Check for duplicates
sort outputs/discovered_urls.csv | uniq -d

# Verify R4-only
grep -v "/R4/" outputs/discovered_urls.csv

# Compare with existing inventory
python scripts/compare_inventory.py \
    outputs/discovered_urls.csv \
    01_INPUTS_VALIDATED/inventory/links.csv
```

---

## Advanced Usage

### Custom Query Configuration

Create custom project configuration:

```yaml
# configs/custom_project.yml
project:
  name: "Custom Project"
  focus: "Specific domain focus"

bm25_queries:
  - "your custom query terms"
  - "specific resources or concepts"

filter_patterns:
  include:
    - "*/fhir/R4/specific-*"
  exclude:
    - "*/examples/*"

score_threshold: 0.4

max_urls:
  total: 300
  per_category:
    resources: 100
    modules: 50
```

### Parallel Processing

Run multiple projects in parallel:

```bash
# Discover once
python scripts/pre_crawl_discovery.py --output outputs/all_urls.csv

# Filter for multiple projects in parallel
python scripts/project_filter.py --project andor --input outputs/all_urls.csv &
python scripts/project_filter.py --project whio --input outputs/all_urls.csv &
wait

# Compare results
python scripts/compare_projects.py andor whio
```

### Incremental Updates

Update existing discoveries:

```bash
# Check for new URLs since last run
python scripts/pre_crawl_discovery.py \
    --incremental \
    --since "2025-11-01" \
    --merge outputs/discovered_urls.csv
```

### Export Formats

Export results in different formats:

```bash
# JSON export
python scripts/export_results.py \
    --format json \
    --input outputs/andor_filtered_urls.csv \
    --output outputs/andor_urls.json

# Markdown report
python scripts/export_results.py \
    --format markdown \
    --input outputs/andor_filtered_urls.csv \
    --output reports/andor_urls.md

# Excel workbook
python scripts/export_results.py \
    --format excel \
    --input outputs/andor_filtered_urls.csv \
    --output outputs/andor_urls.xlsx
```

---

## Performance Tuning

### Optimization Parameters

```python
# In scripts/pre_crawl_discovery.py
PERFORMANCE_CONFIG = {
    'max_concurrent': 20,      # Concurrent requests
    'batch_size': 100,         # URLs per batch
    'timeout': 10,             # Seconds per request
    'retry_count': 2,          # Retries on failure
    'cache_ttl': 604800,       # 7 days cache
    'rate_limit': 10           # Requests per second
}
```

### Network Optimization

```bash
# Test network speed
speedtest-cli

# Optimize DNS
echo "nameserver 1.1.1.1" | sudo tee /etc/resolv.conf

# Use connection pooling
export AIOHTTP_CONN_LIMIT=100
```

### Memory Optimization

```python
# Enable garbage collection
import gc
gc.enable()
gc.collect()

# Limit DataFrame memory
pd.options.mode.chained_assignment = None
pd.options.display.max_rows = 100
```

### Cache Management

```bash
# View cache size
du -sh .cache/

# Clear old cache
find .cache/ -mtime +7 -delete

# Disable cache for testing
export USE_CACHE=false
```

### Monitoring Performance

```bash
# Monitor in real-time
watch -n 1 "ps aux | grep python"

# Track network usage
nethogs

# Profile script execution
python -m cProfile scripts/pre_crawl_discovery.py
```

---

## Best Practices

### 1. Start Small

Test with a subset first:
```bash
python scripts/pre_crawl_discovery.py --max-urls 100 --pattern "*/patient*"
```

### 2. Use Caching

Always use cache for repeated runs:
```bash
python scripts/pre_crawl_discovery.py --cache --cache-dir .cache/
```

### 3. Log Everything

Maintain detailed logs:
```bash
python scripts/pre_crawl_discovery.py --log-file logs/discovery_$(date +%Y%m%d).log
```

### 4. Validate Results

Always validate before proceeding:
```bash
python scripts/validate_results.py outputs/filtered_urls.csv
```

### 5. Monitor Resources

Track system resources:
```bash
# Before running
free -h
df -h

# During execution
htop
```

---

## Next Steps

After completing URL discovery:

1. **Review filtered URLs**: Manually check a sample for relevance
2. **Adjust configuration**: Fine-tune queries and thresholds if needed
3. **Run test crawl**: Crawl a small subset to validate approach
4. **Execute full crawl**: Use filtered URLs with assigned depths
5. **Validate outputs**: Check extracted content quality
6. **Generate report**: Create summary of crawl results

---

## Appendix A: Command Reference

### Discovery Commands

```bash
# Basic discovery
python scripts/pre_crawl_discovery.py --domain hl7.org

# With HEAD extraction
python scripts/pre_crawl_discovery.py --extract-head

# Pattern filtering
python scripts/pre_crawl_discovery.py --pattern "*/fhir/R4/*"

# Exclude patterns
python scripts/pre_crawl_discovery.py --exclude "*example*,*test*"

# Custom output
python scripts/pre_crawl_discovery.py --output my_urls.csv
```

### Filtering Commands

```bash
# Project filter
python scripts/project_filter.py --project andor

# Custom config
python scripts/project_filter.py --config my_config.yml

# Score threshold
python scripts/project_filter.py --threshold 0.5

# Debug mode
python scripts/project_filter.py --debug
```

### Analysis Commands

```bash
# Cost estimation
python scripts/cost_estimator.py --urls filtered_urls.csv

# Depth optimization
python scripts/depth_optimizer.py --strategy conservative

# Comparison
python scripts/compare_projects.py project1 project2
```

---

## Appendix B: Configuration Templates

### Minimal Configuration

```yaml
# configs/minimal.yml
project:
  name: "Minimal Project"

bm25_queries:
  - "essential terms only"

score_threshold: 0.5
max_urls:
  total: 100
```

### Comprehensive Configuration

```yaml
# configs/comprehensive.yml
project:
  name: "Comprehensive Project"
  focus: "All FHIR resources"

bm25_queries:
  - "fhir resource implementation"
  - "clinical administrative financial"
  - "operation search rest api"

filter_patterns:
  include:
    - "*/fhir/R4/*"
  exclude:
    - "*/ballot/*"
    - "*/test/*"

scoring:
  score_threshold: 0.2
  category_weights:
    resource: 1.0
    module: 0.9
    implementation: 0.9
    valueset: 0.8
    example: 0.6

depth_strategy:
  resource: 1
  module: 1
  implementation: 1
  valueset: 1
  example: 2

max_urls:
  total: 2000
  per_category:
    resource: 500
    module: 100
    implementation: 400
    valueset: 500
    example: 500
```

---

**Document Version**: 1.0
**Last Updated**: November 8, 2025
**Next Review**: February 8, 2026

---

*For methodology details, see PRE_CRAWL_METHODOLOGY.md*
*For project-specific guidance, see PROJECT_SELECTION_FRAMEWORK.md*