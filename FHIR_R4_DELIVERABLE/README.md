# FHIR R4 Crawl – Ready-to-Zip Bundle

This directory packages everything required to understand, reproduce, and consume the validated FHIR R4 markdown dataset. Zip `FHIR_R4_DELIVERABLE/` as-is for distribution.

## Structure

| Folder | Purpose |
| --- | --- |
| `docs/` | Manifest, methodology, provenance, and validation reports. |
| `requirements/` | Pinned Python requirements plus install guide. |
| `extraction/` | Crawl4AI scripts (`scripts/*.py`) and supporting modules (`src/*.py`). |
| `outputs/` | Canonical markdown dataset (`markdown_rebuilt/`, 55 files). |

## Usage Workflow

1. **Read Docs** – Start with `docs/00_MANIFEST.md` and `docs/COMPREHENSIVE_VALIDATION_REPORT.md` to understand the project scope and QA status.
2. **Set Up Environment** – Follow `requirements/README.md` to create the virtual environment and install dependencies.
3. **Reproduce Extraction (Optional)** – Use the instructions in `extraction/README.md` to rerun the crawl and rebuild steps (requires `downloads/site`).
4. **Consume Outputs** – Leverage the files in `outputs/markdown_rebuilt/` for downstream LLM ingestion or documentation tasks.

All content reflects the revalidated build completed on **2025-11-08**.
