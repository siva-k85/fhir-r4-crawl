#!/usr/bin/env python3
"""
FHIR R4 Markdown Extraction - Reference Implementation
This is a standalone reference script stored in CONFIG/
The main implementation is in src/markdown_extractor.py
"""

import asyncio
import os
import re
from pathlib import Path


async def extract_fhir_r4_markdown(shortlist_file="shortlist/urls.txt", output_dir="extracted/markdown"):
    """
    Extract markdown from FHIR R4 URLs using Crawl4AI Python API

    This demonstrates the hybrid approach:
    - CLI for inventory
    - Python API for precise extraction with custom filters
    """

    from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
    from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
    from crawl4ai.deep_crawling.filters import (
        FilterChain,
        URLPatternFilter,
        DomainFilter,
        ContentTypeFilter
    )

    # Define R4-only filters
    ALLOW_PATTERNS = ["*hl7.org/fhir/R4/*"]
    BLOCK_PATTERNS = ["*R5/*", "*R4B/*", "*R3/*", "*R2/*", "*.zip", "*.tgz", "*/ballot/*"]

    filter_chain = FilterChain([
        DomainFilter(allowed_domains=["hl7.org"]),
        URLPatternFilter(patterns=ALLOW_PATTERNS),
        URLPatternFilter(patterns=BLOCK_PATTERNS, allow=False),
        ContentTypeFilter(allowed_types=["text/html"])
    ])

    # Configure deep crawl strategy
    strategy = BFSDeepCrawlStrategy(
        max_depth=1,
        include_external=False,
        max_pages=50,
        filter_chain=filter_chain
    )

    # Crawler config
    config = CrawlerRunConfig(
        deep_crawl_strategy=strategy,
        word_count_threshold=50,
        verbose=True,
        cache_mode="enabled",
        wait_until="domcontentloaded",
        page_timeout=45000
    )

    # Read shortlist URLs
    with open(shortlist_file, 'r') as f:
        urls = [line.strip() for line in f if line.strip()]

    print(f"Extracting from {len(urls)} seed URLs...")

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    # Extract from each URL
    async with AsyncWebCrawler() as crawler:
        for url in urls:
            print(f"\nProcessing: {url}")

            # Run crawler
            results = await crawler.arun(url, config=config)

            # Save each result
            for result in results:
                # Generate safe filename
                filename = re.sub(r'[^a-zA-Z0-9_-]+', '_', result.url.strip('/'))[:200] + ".md"
                filepath = os.path.join(output_dir, filename)

                # Add metadata header
                header = f"""---
url: {result.url}
title: {getattr(result, 'title', 'Unknown')}
crawled: {getattr(result, 'timestamp', 'unknown')}
depth: {getattr(result, 'depth', 0)}
---

"""

                # Write markdown
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(header + result.markdown)

                print(f"  ✓ Saved: {filename}")

            # Polite delay between seeds
            await asyncio.sleep(2)

    print(f"\n✅ Extraction complete!")


if __name__ == '__main__':
    asyncio.run(extract_fhir_r4_markdown())
