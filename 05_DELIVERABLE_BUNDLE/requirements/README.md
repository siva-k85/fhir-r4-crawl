# Requirements Reference

This folder snapshots the exact `requirements.txt` used for the FHIR R4 Crawl pipeline. Install these packages into a fresh virtual environment to guarantee compatibility with the Crawl4AI scripts.

## Contents

- `requirements.txt` – pinned Python dependencies (Crawl4AI 0.7.6, Playwright 1.55, lxml 5.4, etc.).

## Recommended Setup

```bash
python3 -m venv .venv-fhir
source .venv-fhir/bin/activate
python -m pip install --upgrade pip
pip install -r requirements/requirements.txt
# Install Playwright browser binaries once
python -m playwright install chromium
```

## Notable Packages

- **Crawl4AI 0.7.6** – core async crawler + markdown extractor.
- **Playwright 1.55** – headless Chromium automation used by Crawl4AI.
- **litellm / httpx / aiohttp** – async networking stack leveraged by Crawl4AI.
- **lxml / beautifulsoup4** – HTML parsing for markdown cleanup.
- **pydantic / PyYAML** – configuration parsing utilities referenced by the scripts.

Keep this requirements file in sync with the scripts to avoid environment drift.
