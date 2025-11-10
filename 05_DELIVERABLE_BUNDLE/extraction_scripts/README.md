# Crawl4AI Extraction Scripts

This directory contains every Python component required to gather and rebuild the FHIR R4 markdown dataset.

## Layout

| File | Role |
| --- | --- |
| `scripts/04_extract_markdown.py` | Launches the Crawl4AI BFS crawl against the shortlist URLs with anti-bot settings. |
| `scripts/08_convert_local_html.py` | Converts local HTML pages from the official `fhir-spec.zip` mirror into markdown, bypassing CAPTCHA. |
| `scripts/10_rebuild_markdown_from_local.py` | Canonical rebuild step that reprocesses **all** markdown files from the local mirror into `markdown_rebuilt/`. |
| `src/markdown_extractor.py` | Async helper class wrapping Crawl4AI APIs (filter chains, BFS strategy, saving markdown + metadata). |
| `src/utils.py` | Shared utilities (path helpers, sanitizers, validation helpers) imported by the scripts. |

## Execution Flow

1. **Web crawl** – `python scripts/04_extract_markdown.py`
   - Reads shortlist URLs (`01_INPUTS_VALIDATED/shortlist/urls.txt`).
   - Uses Crawl4AI BFS strategy with domain/content-type filters.
   - Writes preliminary markdown into `03_OUTPUTS_COMPLETE/markdown/`.

2. **Local HTML conversion** – `python scripts/08_convert_local_html.py downloads/site 03_OUTPUTS_COMPLETE/markdown`
   - Requires `downloads/site` extracted from `fhir-spec.zip`.
   - Adds high-value shortlist pages via `file://` crawling (no network).

3. **Canonical rebuild** – `python scripts/10_rebuild_markdown_from_local.py`
   - Reads URLs from existing markdown front matter.
   - Opens the corresponding local HTML (`downloads/site/<page>.html`).
   - Writes clean, deterministic markdown into `03_OUTPUTS_COMPLETE/markdown_rebuilt/`.

## Configuration Notes

- All scripts expect `requirements/requirements.txt` to be installed (Crawl4AI, Playwright, etc.).
- `scripts/10_rebuild_markdown_from_local.py` is idempotent and safe to rerun; it overwrites `markdown_rebuilt/` with fresh conversions.
- Update `downloads/site/searchform.html` manually if HL7 removes it from the ZIP (already handled in this bundle).

Refer to the root README for the high-level pipeline sequence.
