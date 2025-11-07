"""
Inventory Builder - Parse Crawl4AI output into CSV and summary
"""

import csv
import json
import logging
from collections import defaultdict, Counter
from pathlib import Path
from typing import Dict, List, Any
from urllib.parse import urlparse

from src.utils import ensure_directory, load_json, get_timestamp

logger = logging.getLogger(__name__)


class InventoryBuilder:
    """Build inventory from Crawl4AI CLI output"""

    def __init__(self, json_file: str, output_dir: str = "inventory"):
        """
        Initialize inventory builder

        Args:
            json_file: Path to Crawl4AI JSON output
            output_dir: Directory to save inventory files
        """
        self.json_file = json_file
        self.output_dir = output_dir
        ensure_directory(output_dir)

    def parse_crawl_output(self) -> List[Dict[str, Any]]:
        """
        Parse Crawl4AI JSON output

        Returns:
            List of page records
        """
        logger.info(f"Parsing {self.json_file}")

        try:
            with open(self.json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Handle different output formats
            if isinstance(data, list):
                pages = data
            elif isinstance(data, dict) and 'results' in data:
                pages = data['results']
            elif isinstance(data, dict) and 'pages' in data:
                pages = data['pages']
            else:
                # Try to find pages in nested structure
                pages = data

            logger.info(f"Found {len(pages)} pages in output")
            return pages

        except Exception as e:
            logger.error(f"Error parsing JSON: {e}")
            return []

    def extract_record(self, page: Dict[str, Any]) -> Dict[str, str]:
        """
        Extract record from page data

        Args:
            page: Page data from crawler

        Returns:
            Record dictionary
        """
        url = page.get('url', '')

        return {
            'url': url,
            'depth': str(page.get('depth', 0)),
            'status': str(page.get('status_code', page.get('status', 'unknown'))),
            'content_type': page.get('content_type', page.get('headers', {}).get('content-type', 'unknown')),
            'parent': page.get('parent_url', page.get('parent', '')),
            'first_seen': page.get('timestamp', get_timestamp()),
            'title': page.get('title', '')[:100],  # Truncate long titles
            'word_count': str(page.get('word_count', 0))
        }

    def generate_csv(self, pages: List[Dict[str, Any]]) -> str:
        """
        Generate CSV inventory

        Args:
            pages: List of page records

        Returns:
            Path to generated CSV file
        """
        csv_path = Path(self.output_dir) / 'links.csv'

        fieldnames = ['url', 'depth', 'status', 'content_type', 'parent', 'first_seen', 'title', 'word_count']

        try:
            with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

                for page in pages:
                    record = self.extract_record(page)
                    writer.writerow(record)

            logger.info(f"Generated CSV: {csv_path}")
            return str(csv_path)

        except Exception as e:
            logger.error(f"Error generating CSV: {e}")
            return ""

    def generate_summary(self, pages: List[Dict[str, Any]]) -> str:
        """
        Generate summary markdown

        Args:
            pages: List of page records

        Returns:
            Path to generated summary file
        """
        summary_path = Path(self.output_dir) / 'summary.md'

        # Calculate statistics
        total_pages = len(pages)
        unique_urls = len(set(p.get('url', '') for p in pages))

        # Depth distribution
        depth_counts = Counter(p.get('depth', 0) for p in pages)

        # Status code distribution
        status_counts = Counter(p.get('status_code', p.get('status', 'unknown')) for p in pages)

        # Content type distribution
        content_type_counts = Counter(p.get('content_type', 'unknown') for p in pages)

        # Domain analysis
        domains = Counter()
        for page in pages:
            url = page.get('url', '')
            if url:
                domain = urlparse(url).netloc
                domains[domain] += 1

        # Top sections (by URL path)
        sections = Counter()
        for page in pages:
            url = page.get('url', '')
            if '/R4/' in url:
                # Extract section after /R4/
                parts = url.split('/R4/')
                if len(parts) > 1:
                    section = parts[1].split('/')[0].split('.')[0]
                    if section:
                        sections[section] += 1

        # Generate summary markdown
        summary = f"""# FHIR R4 Crawl Inventory Summary

Generated: {get_timestamp()}

## Overview

- **Total Pages Crawled**: {total_pages}
- **Unique URLs**: {unique_urls}

## Depth Distribution

| Depth | Count | Percentage |
|-------|-------|-----------|
"""

        for depth in sorted(depth_counts.keys()):
            count = depth_counts[depth]
            pct = (count / total_pages * 100) if total_pages > 0 else 0
            summary += f"| {depth} | {count} | {pct:.1f}% |\n"

        summary += f"""
## HTTP Status Codes

| Status | Count |
|--------|-------|
"""

        for status in sorted(status_counts.keys()):
            count = status_counts[status]
            summary += f"| {status} | {count} |\n"

        summary += f"""
## Content Types

| Content Type | Count |
|--------------|-------|
"""

        for content_type, count in content_type_counts.most_common(10):
            summary += f"| {content_type} | {count} |\n"

        summary += f"""
## Top Domains

| Domain | Count |
|--------|-------|
"""

        for domain, count in domains.most_common(5):
            summary += f"| {domain} | {count} |\n"

        summary += f"""
## Top R4 Sections

| Section | Count |
|---------|-------|
"""

        for section, count in sections.most_common(20):
            summary += f"| {section} | {count} |\n"

        summary += f"""
## Quality Metrics

- **R4 URLs**: {sum(1 for p in pages if '/R4/' in p.get('url', ''))}
- **HTML Pages**: {sum(1 for p in pages if 'html' in p.get('content_type', '').lower())}
- **Successful Fetches (2xx)**: {sum(1 for p in pages if str(p.get('status_code', p.get('status', 0))).startswith('2'))}

## Notes

- This inventory was generated from Crawl4AI CLI output
- Only includes pages discovered during the breadth-first scan
- Depth limited to prevent excessive crawling
- See `links.csv` for full details
"""

        try:
            with open(summary_path, 'w', encoding='utf-8') as f:
                f.write(summary)

            logger.info(f"Generated summary: {summary_path}")
            return str(summary_path)

        except Exception as e:
            logger.error(f"Error generating summary: {e}")
            return ""

    def build(self) -> Dict[str, str]:
        """
        Build complete inventory

        Returns:
            Dictionary with paths to generated files
        """
        logger.info("Building inventory...")

        # Parse crawl output
        pages = self.parse_crawl_output()

        if not pages:
            logger.error("No pages found in crawl output")
            return {}

        # Generate CSV
        csv_path = self.generate_csv(pages)

        # Generate summary
        summary_path = self.generate_summary(pages)

        return {
            'csv': csv_path,
            'summary': summary_path,
            'page_count': len(pages)
        }


def main():
    """Main entry point for CLI usage"""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m src.inventory_builder <json_file> [output_dir]")
        sys.exit(1)

    json_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "inventory"

    builder = InventoryBuilder(json_file, output_dir)
    results = builder.build()

    print(f"\n✓ Inventory built successfully!")
    print(f"  CSV: {results.get('csv')}")
    print(f"  Summary: {results.get('summary')}")
    print(f"  Pages: {results.get('page_count')}")


if __name__ == '__main__':
    main()
