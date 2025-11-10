#!/usr/bin/env python3
"""
FHIR R4 Pre-Crawl Discovery Script
Version: 1.0
Date: November 8, 2025
Author: Symphony Corp

Purpose: Discover and analyze FHIR R4 URLs using Crawl4AI's URL seeding capabilities
"""

import asyncio
import argparse
import csv
import json
import logging
import os
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlparse, urljoin

import aiohttp
import pandas as pd
import yaml
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'logs/pre_crawl_discovery_{datetime.now():%Y%m%d_%H%M%S}.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Performance configuration
PERFORMANCE_CONFIG = {
    'max_concurrent': 20,      # Concurrent HEAD requests
    'batch_size': 100,         # URLs per batch
    'timeout': 10,             # Seconds per request
    'retry_count': 2,          # Retries on failure
    'cache_ttl': 604800,       # 7 days cache
    'rate_limit': 10           # Requests per second
}


class FHIRUrlSeeder:
    """
    Discovers and analyzes FHIR R4 URLs using various sources
    """

    def __init__(self, config: Optional[Dict] = None):
        """
        Initialize URL seeder with configuration

        Args:
            config: Optional configuration dictionary
        """
        self.config = config or PERFORMANCE_CONFIG
        self.discovered_urls = []
        self.metadata_cache = {}
        self.session = None

    async def discover_from_sitemap(self, domain: str, pattern: str = None) -> List[str]:
        """
        Discover URLs from sitemap

        Args:
            domain: Target domain
            pattern: Optional URL pattern filter

        Returns:
            List of discovered URLs
        """
        logger.info(f"Discovering URLs from sitemap for {domain}")

        sitemap_urls = [
            f"https://{domain}/sitemap.xml",
            f"https://{domain}/sitemap_index.xml",
            f"https://{domain}/fhir/R4/sitemap.xml"
        ]

        discovered = []

        async with aiohttp.ClientSession() as session:
            for sitemap_url in sitemap_urls:
                try:
                    async with session.get(sitemap_url, timeout=30) as response:
                        if response.status == 200:
                            content = await response.text()
                            urls = self._parse_sitemap(content, pattern)
                            discovered.extend(urls)
                            logger.info(f"Found {len(urls)} URLs in {sitemap_url}")
                except Exception as e:
                    logger.warning(f"Failed to fetch {sitemap_url}: {e}")

        return list(set(discovered))  # Remove duplicates

    def _parse_sitemap(self, content: str, pattern: str = None) -> List[str]:
        """
        Parse sitemap XML content

        Args:
            content: Sitemap XML content
            pattern: Optional URL pattern filter

        Returns:
            List of URLs from sitemap
        """
        urls = []

        # Simple XML parsing (could use lxml for robustness)
        import re
        url_pattern = r'<loc>(.*?)</loc>'
        matches = re.findall(url_pattern, content)

        for url in matches:
            # Apply pattern filter if provided
            if pattern:
                if re.search(pattern, url):
                    urls.append(url)
            else:
                urls.append(url)

        return urls

    async def discover_from_crawl(self, start_url: str, max_depth: int = 1, max_urls: int = 1000) -> List[str]:
        """
        Discover URLs through web crawling

        Args:
            start_url: Starting URL for crawl
            max_depth: Maximum crawl depth
            max_urls: Maximum URLs to discover

        Returns:
            List of discovered URLs
        """
        logger.info(f"Discovering URLs through crawling from {start_url}")

        discovered = []

        browser_config = BrowserConfig(
            headless=True,
            browser_type="chromium",
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
            extra_headers={
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.9'
            }
        )

        crawler_config = CrawlerRunConfig(
            cache_mode="enabled",
            wait_for="networkidle",
            page_timeout=30000
        )

        try:
            async with AsyncWebCrawler(config=browser_config) as crawler:
                result = await crawler.arun(
                    url=start_url,
                    config=crawler_config
                )

                if result.success:
                    # Extract all links from the page
                    from bs4 import BeautifulSoup
                    soup = BeautifulSoup(result.html, 'html.parser')

                    for link in soup.find_all('a', href=True):
                        url = urljoin(start_url, link['href'])
                        if self._is_valid_fhir_url(url):
                            discovered.append(url)

                        if len(discovered) >= max_urls:
                            break

                    logger.info(f"Discovered {len(discovered)} URLs through crawling")

        except Exception as e:
            logger.error(f"Crawl discovery failed: {e}")

        return discovered[:max_urls]

    def _is_valid_fhir_url(self, url: str) -> bool:
        """
        Check if URL is a valid FHIR R4 URL

        Args:
            url: URL to validate

        Returns:
            True if valid FHIR R4 URL
        """
        # Basic validation
        if not url.startswith('http'):
            return False

        # Check for R4 in path
        if '/R4/' not in url and '/r4/' not in url.lower():
            return False

        # Exclude non-HTML resources
        excluded_extensions = ['.js', '.css', '.png', '.jpg', '.pdf', '.xml', '.json', '.xsd']
        if any(url.lower().endswith(ext) for ext in excluded_extensions):
            return False

        return True

    async def extract_head_metadata(self, urls: List[str]) -> List[Dict]:
        """
        Extract HEAD metadata from URLs

        Args:
            urls: List of URLs to process

        Returns:
            List of metadata dictionaries
        """
        logger.info(f"Extracting HEAD metadata from {len(urls)} URLs")

        metadata_list = []
        semaphore = asyncio.Semaphore(self.config['max_concurrent'])

        async def extract_single(url: str) -> Dict:
            async with semaphore:
                try:
                    return await self._extract_head_single(url)
                except Exception as e:
                    logger.warning(f"Failed to extract metadata from {url}: {e}")
                    return {'url': url, 'status': 'failed', 'error': str(e)}

        # Process in batches
        for i in range(0, len(urls), self.config['batch_size']):
            batch = urls[i:i + self.config['batch_size']]
            logger.info(f"Processing batch {i // self.config['batch_size'] + 1}/{(len(urls) - 1) // self.config['batch_size'] + 1}")

            tasks = [extract_single(url) for url in batch]
            results = await asyncio.gather(*tasks)
            metadata_list.extend(results)

            # Rate limiting
            await asyncio.sleep(1)

        return metadata_list

    async def _extract_head_single(self, url: str) -> Dict:
        """
        Extract HEAD metadata from a single URL

        Args:
            url: URL to process

        Returns:
            Metadata dictionary
        """
        # Check cache first
        if url in self.metadata_cache:
            return self.metadata_cache[url]

        metadata = {'url': url}

        browser_config = BrowserConfig(
            headless=True,
            browser_type="chromium"
        )

        crawler_config = CrawlerRunConfig(
            cache_mode="enabled",
            wait_for="domcontentloaded",  # Faster for HEAD extraction
            page_timeout=self.config['timeout'] * 1000,
            exclude_external_links=True
        )

        try:
            async with AsyncWebCrawler(config=browser_config) as crawler:
                result = await crawler.arun(
                    url=url,
                    config=crawler_config
                )

                if result.success:
                    # Extract metadata from result
                    metadata.update({
                        'status': 'valid',
                        'title': result.metadata.get('title', ''),
                        'description': result.metadata.get('description', ''),
                        'og_type': result.metadata.get('og:type', ''),
                        'og_title': result.metadata.get('og:title', ''),
                        'keywords': result.metadata.get('keywords', ''),
                        'canonical': result.metadata.get('canonical', url),
                        'content_type': 'text/html',
                        'extracted_at': datetime.now().isoformat()
                    })

                    # Cache the metadata
                    self.metadata_cache[url] = metadata
                else:
                    metadata['status'] = 'failed'

        except Exception as e:
            metadata['status'] = 'error'
            metadata['error'] = str(e)

        return metadata

    def calculate_bm25_scores(self, metadata_list: List[Dict], queries: List[str]) -> Dict[str, float]:
        """
        Calculate BM25 relevance scores for URLs

        Args:
            metadata_list: List of URL metadata
            queries: List of query strings

        Returns:
            Dictionary of URL to score mappings
        """
        logger.info(f"Calculating BM25 scores for {len(metadata_list)} URLs")

        try:
            from rank_bm25 import BM25Okapi
        except ImportError:
            # Fallback to simple scoring if BM25 not available
            logger.warning("BM25 not available, using simple scoring")
            return self._simple_scoring(metadata_list, queries)

        # Create corpus from metadata
        corpus = []
        urls = []

        for meta in metadata_list:
            if meta.get('status') == 'valid':
                doc = f"{meta.get('title', '')} {meta.get('description', '')} {meta.get('keywords', '')}"
                corpus.append(doc.lower().split())
                urls.append(meta['url'])

        if not corpus:
            return {}

        # Initialize BM25
        bm25 = BM25Okapi(corpus)

        # Calculate scores for each query
        scores = {}
        for url in urls:
            scores[url] = 0

        for query in queries:
            query_tokens = query.lower().split()
            query_scores = bm25.get_scores(query_tokens)

            for url, score in zip(urls, query_scores):
                scores[url] = max(scores[url], score)  # Take maximum score across queries

        # Normalize scores to 0-1 range
        max_score = max(scores.values()) if scores else 1
        if max_score > 0:
            scores = {url: score / max_score for url, score in scores.items()}

        return scores

    def _simple_scoring(self, metadata_list: List[Dict], queries: List[str]) -> Dict[str, float]:
        """
        Simple keyword-based scoring fallback

        Args:
            metadata_list: List of URL metadata
            queries: List of query strings

        Returns:
            Dictionary of URL to score mappings
        """
        scores = {}

        for meta in metadata_list:
            if meta.get('status') != 'valid':
                continue

            url = meta['url']
            content = f"{meta.get('title', '')} {meta.get('description', '')} {meta.get('keywords', '')}".lower()

            score = 0
            for query in queries:
                keywords = query.lower().split()
                matches = sum(1 for keyword in keywords if keyword in content)
                score = max(score, matches / len(keywords) if keywords else 0)

            scores[url] = score

        return scores

    async def discover_and_analyze(
        self,
        domain: str,
        source: str = "sitemap",
        pattern: str = None,
        extract_head: bool = False,
        queries: List[str] = None,
        max_urls: int = 10000
    ) -> Dict:
        """
        Complete discovery and analysis pipeline

        Args:
            domain: Target domain
            source: Discovery source (sitemap, crawl, or both)
            pattern: URL pattern filter
            extract_head: Whether to extract HEAD metadata
            queries: BM25 scoring queries
            max_urls: Maximum URLs to discover

        Returns:
            Results dictionary
        """
        results = {
            'domain': domain,
            'timestamp': datetime.now().isoformat(),
            'urls': [],
            'metadata': [],
            'scores': {},
            'statistics': {}
        }

        # Phase 1: Discovery
        logger.info("=" * 50)
        logger.info("Phase 1: URL Discovery")
        logger.info("=" * 50)

        if source in ["sitemap", "both"]:
            sitemap_urls = await self.discover_from_sitemap(domain, pattern)
            results['urls'].extend(sitemap_urls)
            logger.info(f"Discovered {len(sitemap_urls)} URLs from sitemap")

        if source in ["crawl", "both"]:
            start_url = f"https://{domain}/fhir/R4/"
            crawl_urls = await self.discover_from_crawl(start_url, max_urls=max_urls)
            results['urls'].extend(crawl_urls)
            logger.info(f"Discovered {len(crawl_urls)} URLs from crawling")

        # Remove duplicates and apply pattern filter
        results['urls'] = list(set(results['urls']))

        if pattern:
            import re
            results['urls'] = [url for url in results['urls'] if re.search(pattern, url)]

        results['urls'] = results['urls'][:max_urls]
        logger.info(f"Total unique URLs after filtering: {len(results['urls'])}")

        # Phase 2: HEAD Extraction (optional)
        if extract_head and results['urls']:
            logger.info("=" * 50)
            logger.info("Phase 2: HEAD Metadata Extraction")
            logger.info("=" * 50)

            results['metadata'] = await self.extract_head_metadata(results['urls'])

            valid_count = sum(1 for m in results['metadata'] if m.get('status') == 'valid')
            logger.info(f"Successfully extracted metadata from {valid_count}/{len(results['metadata'])} URLs")

            # Phase 3: Scoring (if queries provided)
            if queries:
                logger.info("=" * 50)
                logger.info("Phase 3: BM25 Scoring")
                logger.info("=" * 50)

                results['scores'] = self.calculate_bm25_scores(results['metadata'], queries)
                logger.info(f"Calculated scores for {len(results['scores'])} URLs")

        # Calculate statistics
        results['statistics'] = self._calculate_statistics(results)

        return results

    def _calculate_statistics(self, results: Dict) -> Dict:
        """
        Calculate discovery statistics

        Args:
            results: Results dictionary

        Returns:
            Statistics dictionary
        """
        stats = {
            'total_urls': len(results['urls']),
            'metadata_extracted': len(results['metadata']),
            'valid_metadata': sum(1 for m in results['metadata'] if m.get('status') == 'valid'),
            'scored_urls': len(results['scores'])
        }

        if results['scores']:
            scores = list(results['scores'].values())
            stats.update({
                'avg_score': sum(scores) / len(scores),
                'max_score': max(scores),
                'min_score': min(scores),
                'above_0.5': sum(1 for s in scores if s > 0.5),
                'above_0.3': sum(1 for s in scores if s > 0.3)
            })

        return stats


def save_results(results: Dict, output_path: str, format: str = "csv"):
    """
    Save discovery results to file

    Args:
        results: Results dictionary
        output_path: Output file path
        format: Output format (csv or json)
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if format == "csv":
        # Prepare data for CSV
        rows = []

        if results['metadata']:
            # Use metadata if available
            for meta in results['metadata']:
                row = {
                    'url': meta['url'],
                    'status': meta.get('status', ''),
                    'title': meta.get('title', ''),
                    'description': meta.get('description', ''),
                    'og_type': meta.get('og_type', ''),
                    'keywords': meta.get('keywords', ''),
                    'relevance_score': results['scores'].get(meta['url'], 0),
                    'discovered_from': 'sitemap',  # Could be enhanced
                    'timestamp': results['timestamp']
                }
                rows.append(row)
        else:
            # Just URLs
            for url in results['urls']:
                rows.append({
                    'url': url,
                    'discovered_from': 'sitemap',
                    'timestamp': results['timestamp']
                })

        # Save to CSV
        df = pd.DataFrame(rows)
        df.to_csv(output_path, index=False)
        logger.info(f"Saved {len(rows)} rows to {output_path}")

    elif format == "json":
        # Save as JSON
        with open(output_path, 'w') as f:
            json.dump(results, f, indent=2)
        logger.info(f"Saved results to {output_path}")


async def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(description='FHIR R4 URL Discovery Tool')

    parser.add_argument('--domain', default='hl7.org', help='Target domain')
    parser.add_argument('--source', default='sitemap', choices=['sitemap', 'crawl', 'both'],
                       help='Discovery source')
    parser.add_argument('--pattern', help='URL pattern filter (regex)')
    parser.add_argument('--extract-head', action='store_true', help='Extract HEAD metadata')
    parser.add_argument('--query', action='append', dest='queries',
                       help='BM25 scoring query (can be repeated)')
    parser.add_argument('--max-urls', type=int, default=10000, help='Maximum URLs to discover')
    parser.add_argument('--output', default='outputs/discovered_urls.csv', help='Output file path')
    parser.add_argument('--format', default='csv', choices=['csv', 'json'], help='Output format')
    parser.add_argument('--config', help='Configuration file path')
    parser.add_argument('--cache', action='store_true', help='Use cached results if available')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')

    args = parser.parse_args()

    # Set logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Load configuration if provided
    config = PERFORMANCE_CONFIG
    if args.config:
        with open(args.config, 'r') as f:
            config.update(yaml.safe_load(f))

    # Default queries if none provided
    if not args.queries:
        args.queries = [
            "fhir resource implementation guide",
            "patient observation coverage claim"
        ]

    # Initialize seeder
    seeder = FHIRUrlSeeder(config)

    # Run discovery and analysis
    logger.info("Starting FHIR R4 URL Discovery")
    logger.info(f"Domain: {args.domain}")
    logger.info(f"Source: {args.source}")
    logger.info(f"Pattern: {args.pattern or 'None'}")
    logger.info(f"Extract HEAD: {args.extract_head}")
    logger.info(f"Queries: {args.queries}")

    start_time = time.time()

    results = await seeder.discover_and_analyze(
        domain=args.domain,
        source=args.source,
        pattern=args.pattern or "*/fhir/R4/*",
        extract_head=args.extract_head,
        queries=args.queries,
        max_urls=args.max_urls
    )

    elapsed_time = time.time() - start_time

    # Print summary
    print("\n" + "=" * 50)
    print("Discovery Summary")
    print("=" * 50)
    print(f"Total URLs discovered: {results['statistics']['total_urls']}")

    if args.extract_head:
        print(f"Metadata extracted: {results['statistics']['metadata_extracted']}")
        print(f"Valid metadata: {results['statistics']['valid_metadata']}")

    if results['scores']:
        print(f"Scored URLs: {results['statistics']['scored_urls']}")
        print(f"Average score: {results['statistics'].get('avg_score', 0):.3f}")
        print(f"URLs above 0.5: {results['statistics'].get('above_0.5', 0)}")
        print(f"URLs above 0.3: {results['statistics'].get('above_0.3', 0)}")

    print(f"Time elapsed: {elapsed_time:.2f} seconds")

    # Save results
    save_results(results, args.output, args.format)
    print(f"\nResults saved to: {args.output}")


if __name__ == "__main__":
    asyncio.run(main())