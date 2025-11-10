"""
Markdown Extractor - Extract clean markdown using Crawl4AI Python API
"""

import asyncio
import logging
import os
from pathlib import Path
from typing import List, Dict, Any

from src.utils import ensure_directory, sanitize_filename, is_r4_url, read_file_lines

logger = logging.getLogger(__name__)


class MarkdownExtractor:
    """Extract markdown from FHIR R4 pages using Crawl4AI"""

    def __init__(
        self,
        output_dir: str = "extracted/markdown",
        max_depth: int = 1,
        max_pages: int = 50,
        word_threshold: int = 50
    ):
        """
        Initialize markdown extractor

        Args:
            output_dir: Directory to save markdown files
            max_depth: Maximum crawl depth per seed
            max_pages: Maximum pages per seed
            word_threshold: Minimum word count threshold
        """
        self.output_dir = output_dir
        self.max_depth = max_depth
        self.max_pages = max_pages
        self.word_threshold = word_threshold
        ensure_directory(output_dir)

    async def extract_from_url(self, url: str, crawler: Any) -> List[Dict[str, Any]]:
        """
        Extract markdown from a single URL

        Args:
            url: URL to extract
            crawler: AsyncWebCrawler instance

        Returns:
            List of extraction results
        """
        logger.info(f"Extracting: {url}")

        try:
            # Import here to avoid issues if crawl4ai not installed yet
            from crawl4ai import CrawlerRunConfig
            from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
            from crawl4ai.deep_crawling.filters import (
                FilterChain,
                URLPatternFilter,
                DomainFilter,
                ContentTypeFilter
            )

            # Define filters - simplified for Crawl4AI 0.7.6
            filter_chain = FilterChain([
                DomainFilter(allowed_domains=["hl7.org"]),
                URLPatternFilter(patterns=["*hl7.org/fhir/R4/*"]),
                ContentTypeFilter(allowed_types=["text/html"])
            ])

            # Configure deep crawl strategy
            strategy = BFSDeepCrawlStrategy(
                max_depth=self.max_depth,
                include_external=False,
                max_pages=self.max_pages,
                filter_chain=filter_chain
            )

            # Create config with anti-detection
            config = CrawlerRunConfig(
                deep_crawl_strategy=strategy,
                word_count_threshold=self.word_threshold,
                verbose=False,
                cache_mode="bypass",  # Fresh fetch to avoid cached CAPTCHA
                wait_until="networkidle",  # Wait for page to fully load
                page_timeout=60000,  # Longer timeout
                simulate_user=True,  # Simulate human behavior
                override_navigator=True,  # Override navigator properties
                magic=True  # Enable anti-detection magic mode
            )

            # Run crawler
            results = await crawler.arun(url, config=config)

            logger.info(f"Extracted {len(results)} pages from {url}")
            return results

        except Exception as e:
            logger.error(f"Error extracting from {url}: {e}")
            return []

    def save_markdown(self, result: Any) -> str:
        """
        Save markdown result to file

        Args:
            result: Crawl result object

        Returns:
            Path to saved file
        """
        try:
            # Generate safe filename
            filename = sanitize_filename(result.url) + ".md"
            filepath = Path(self.output_dir) / filename

            # Extract markdown content
            markdown_content = result.markdown

            # Add header with metadata
            header = f"""---
url: {result.url}
title: {getattr(result, 'title', 'Unknown')}
crawled: {getattr(result, 'timestamp', 'unknown')}
depth: {getattr(result, 'depth', 0)}
---

"""

            # Write to file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(header + markdown_content)

            logger.info(f"Saved: {filepath}")
            return str(filepath)

        except Exception as e:
            logger.error(f"Error saving markdown for {result.url}: {e}")
            return ""

    async def extract_from_shortlist(self, shortlist_file: str) -> Dict[str, Any]:
        """
        Extract markdown from all URLs in shortlist

        Args:
            shortlist_file: Path to shortlist file (one URL per line)

        Returns:
            Summary of extraction results
        """
        logger.info(f"Loading shortlist from {shortlist_file}")

        # Read URLs
        urls = read_file_lines(shortlist_file)
        logger.info(f"Found {len(urls)} URLs to extract")

        # Import AsyncWebCrawler
        try:
            from crawl4ai import AsyncWebCrawler, BrowserConfig
        except ImportError:
            logger.error("Crawl4AI not installed. Run: pip install crawl4ai")
            return {}

        results_summary = {
            'total_urls': len(urls),
            'successful': 0,
            'failed': 0,
            'total_pages': 0,
            'files_saved': []
        }

        # Configure anti-detection browser
        browser_config = BrowserConfig(
            headless=True,
            verbose=False,
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            extra_args=["--disable-blink-features=AutomationControlled"]
        )

        # Extract from each URL with anti-detection
        async with AsyncWebCrawler(config=browser_config) as crawler:
            for idx, url in enumerate(urls):
                if not url.startswith('http'):
                    logger.warning(f"Skipping invalid URL: {url}")
                    continue

                logger.info(f"Processing URL {idx+1}/{len(urls)}: {url}")

                # Extract
                results = await self.extract_from_url(url, crawler)

                if results:
                    results_summary['successful'] += 1
                    results_summary['total_pages'] += len(results)

                    # Save each result
                    for result in results:
                        if is_r4_url(result.url):
                            filepath = self.save_markdown(result)
                            if filepath:
                                results_summary['files_saved'].append(filepath)
                else:
                    results_summary['failed'] += 1

                # Longer delay between seeds to avoid rate limiting (5-10 seconds)
                delay = 7 + (idx % 3)  # 7-9 seconds, varying delay
                logger.info(f"Waiting {delay} seconds before next URL...")
                await asyncio.sleep(delay)

        logger.info(f"Extraction complete: {results_summary['successful']}/{results_summary['total_urls']} successful")
        return results_summary


def main():
    """Main entry point for CLI usage"""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m src.markdown_extractor <shortlist_file> [output_dir]")
        sys.exit(1)

    shortlist_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "extracted/markdown"

    extractor = MarkdownExtractor(output_dir=output_dir)

    # Run async extraction
    results = asyncio.run(extractor.extract_from_shortlist(shortlist_file))

    print(f"\n✓ Extraction complete!")
    print(f"  URLs processed: {results['successful']}/{results['total_urls']}")
    print(f"  Total pages: {results['total_pages']}")
    print(f"  Files saved: {len(results['files_saved'])}")


if __name__ == '__main__':
    main()
