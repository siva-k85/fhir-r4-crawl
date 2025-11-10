# Extraction & Rebuild Scripts

## What's Here

- `scripts/04_extract_markdown.py` – Crawl4AI BFS crawl against shortlist URLs.
- `scripts/08_convert_local_html.py` – Converts official `fhir-spec.zip` HTML pages to markdown.
- `scripts/10_rebuild_markdown_from_local.py` – Canonical rebuild for all markdown files using the local mirror.
- `src/markdown_extractor.py` – Async helper used by the crawl script.
- `src/utils.py` – Shared helper functions (path handling, URL validation, etc.).

## Typical Run Sequence

```bash
source .venv-fhir/bin/activate
python scripts/04_extract_markdown.py
python scripts/08_convert_local_html.py downloads/site 03_OUTPUTS_COMPLETE/markdown
python scripts/10_rebuild_markdown_from_local.py
```

`downloads/site` should contain the extracted `fhir-spec.zip` mirror (plus the manually downloaded `searchform.html`). The rebuild script writes the canonical dataset to `03_OUTPUTS_COMPLETE/markdown_rebuilt/`.
