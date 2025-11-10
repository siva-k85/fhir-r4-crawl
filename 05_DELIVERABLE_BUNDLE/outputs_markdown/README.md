# Canonical Markdown Outputs

This folder contains `markdown_rebuilt/`, the authoritative set of 55 FHIR R4 markdown files generated on 2025-11-08 by rerunning the canonical rebuild script against the official HL7 mirror.

## Key Facts

- **Source**: `downloads/site` copy of `https://hl7.org/fhir/R4/fhir-spec.zip` plus manually downloaded `searchform.html`.
- **Generator**: `scripts/10_rebuild_markdown_from_local.py` (see `../extraction_scripts`).
- **Content Size**: ~6.6 MB total; each file ranges from ~10 KB to ~700 KB.
- **Front Matter**: `url`, `title`, `source`, `extracted`, `mirror_path` (and `depth` only on legacy files outside this folder).
- **Validation**: No CAPTCHA text, UTF‑8 clean, R4-only URLs.

## Structure

```
outputs_markdown/
└── markdown_rebuilt/
    ├── hl7_org_fhir_R4_patient.md
    ├── hl7_org_fhir_R4_coverage.md
    ├── ... (52 more files)
    └── hl7_org_fhir_R4_xml_html.md
```

### Shortlist Highlights

- `hl7_org_fhir_R4_patient.md`
- `hl7_org_fhir_R4_coverage.md`
- `hl7_org_fhir_R4_explanationofbenefit.md`
- `hl7_org_fhir_R4_search.md`
- `hl7_org_fhir_R4_searchparameter.md`
- `hl7_org_fhir_R4_datatypes.md`
- `hl7_org_fhir_R4_structuredefinition.md`
- `hl7_org_fhir_R4_terminologies.md`
- `hl7_org_fhir_R4_codesystem.md`
- `hl7_org_fhir_R4_valueset.md`

### Auxiliary Coverage

Includes index pages, module overviews, terminology modules, security content, and navigation artifacts such as `hl7_org_fhir_R4_toc_html.md` and `hl7_org_fhir_R4_index_html.md`.

## Usage Examples

```bash
# Inspect metadata
head -n 10 outputs_markdown/markdown_rebuilt/hl7_org_fhir_R4_patient.md

# Count files
ls -1 outputs_markdown/markdown_rebuilt | wc -l

# Search for a term
rg "Claim" outputs_markdown/markdown_rebuilt/hl7_org_fhir_R4_explanationofbenefit.md
```

For ingestion into other pipelines, treat this folder as read-only and regenerate via the extraction scripts if updates are needed.
