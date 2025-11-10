# FHIR R4 Crawl Deliverable Bundle

This bundle packages everything needed to reproduce and consume the validated FHIR R4 markdown dataset: the pinned Python requirements, the Crawl4AI-based extraction scripts, and the final rebuilt markdown outputs.

## Folder Map

| Path | Description |
| --- | --- |
| `requirements/` | Copy of the exact `requirements.txt` used for the project plus usage guidance. |
| `extraction_scripts/` | Self-contained Crawl4AI pipeline scripts (`scripts/*.py`) and supporting modules (`src/*.py`). |
| `outputs_markdown/` | Canonical markdown dataset rebuilt from the official HL7 download (55 files, ~6.6 MB). |

Each subfolder contains an in-depth README describing its contents, prerequisites, and step-by-step usage.

## Quick Start

1. **Review requirements** – see `requirements/README.md` for environment setup instructions.
2. **Run extraction scripts** – follow `extraction_scripts/README.md` to regenerate outputs if desired.
3. **Consume outputs** – `outputs_markdown/README.md` explains the markdown structure, validation checks, and suggested workflows.

## Provenance

- Source repo: `/Users/sivak/Development/fhir-r4-crawl`
- Bundle generated: 2025-11-08
- Output dataset: `03_OUTPUTS_COMPLETE/markdown_rebuilt` ➜ copied to `outputs_markdown/markdown_rebuilt`

For any downstream distribution, ship this folder as-is to guarantee that requirements, code, and artifacts stay in sync.
