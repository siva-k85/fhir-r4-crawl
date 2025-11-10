#!/usr/bin/env python3
"""
Convert local HTML files from FHIR spec download to markdown
This bypasses CAPTCHA issues by working with official downloaded files
"""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.markdown_extractor import MarkdownExtractor
from src.utils import sanitize_filename


async def convert_local_html(html_dir: str, output_dir: str):
    """Convert local HTML files to markdown"""

    from crawl4ai import AsyncWebCrawler, CrawlerRunConfig

    # Files we need (from shortlist)
    target_files = [
        "patient.html",
        "coverage.html",
        "explanationofbenefit.html",
        "search.html",
        "searchparameter.html",
        "datatypes.html",
        "structuredefinition.html",
        "terminologies.html",
        "codesystem.html",
        "valueset.html",
    ]

    html_dir = Path(html_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    results = {
        'successful': 0,
        'failed': 0,
        'files_saved': []
    }

    # Configure crawler for local files
    config = CrawlerRunConfig(
        word_count_threshold=50,
        verbose=False
    )

    async with AsyncWebCrawler() as crawler:
        for filename in target_files:
            file_path = html_dir / filename

            if not file_path.exists():
                print(f"❌ Not found: {filename}")
                results['failed'] += 1
                continue

            print(f"Processing: {filename}")

            try:
                # Convert file:// URL
                file_url = f"file://{file_path.absolute()}"

                # Crawl local file
                result = await crawler.arun(file_url, config=config)

                if result and len(result) > 0:
                    # Generate safe filename
                    safe_name = f"hl7_org_fhir_R4_{sanitize_filename(filename[:-5])}.md"
                    output_file = output_dir / safe_name

                    # Add metadata header
                    header = f"""---
url: https://hl7.org/fhir/R4/{filename}
title: {filename[:-5].replace('_', ' ').title()}
source: official_download
extracted: local_file_conversion
---

"""

                    # Write markdown
                    with open(output_file, 'w', encoding='utf-8') as f:
                        f.write(header + result[0].markdown)

                    print(f"✓ Saved: {safe_name}")
                    results['successful'] += 1
                    results['files_saved'].append(str(output_file))
                else:
                    print(f"❌ Empty result for {filename}")
                    results['failed'] += 1

            except Exception as e:
                print(f"❌ Error processing {filename}: {e}")
                results['failed'] += 1

    print(f"\n{'='*60}")
    print(f"Conversion complete!")
    print(f"  Successful: {results['successful']}/{len(target_files)}")
    print(f"  Failed: {results['failed']}/{len(target_files)}")
    print(f"{'='*60}")

    return results


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python scripts/08_convert_local_html.py <html_dir> <output_dir>")
        print("Example: python scripts/08_convert_local_html.py downloads/site extracted/markdown")
        sys.exit(1)

    html_dir = sys.argv[1]
    output_dir = sys.argv[2]

    asyncio.run(convert_local_html(html_dir, output_dir))
