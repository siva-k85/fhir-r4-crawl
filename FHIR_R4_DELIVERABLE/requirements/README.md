# Requirements

Install these pinned dependencies inside a clean virtual environment before running any extraction or rebuild scripts.

```bash
python3 -m venv .venv-fhir
source .venv-fhir/bin/activate
python -m pip install --upgrade pip
pip install -r requirements/requirements.txt
python -m playwright install chromium
```

The requirements list covers Crawl4AI 0.7.6, Playwright 1.55, lxml 5.4, and all auxiliary libraries (aiohttp, httpx, litellm, etc.).
