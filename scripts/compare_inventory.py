#!/usr/bin/env python3
"""
FHIR R4 Inventory Comparison Script
Version: 1.0
Date: November 10, 2025
Author: Symphony Corp

Purpose: Compare pre-crawl results with existing inventory
"""

import argparse
import logging
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Set

import pandas as pd

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class InventoryComparator:
    """
    Compares pre-crawl filtered URLs with existing inventory
    """

    def __init__(self):
        """Initialize comparator"""
        self.stats = {
            'precrawl_total': 0,
            'inventory_total': 0,
            'overlap': 0,
            'new_in_precrawl': 0,
            'potentially_missed': 0,
            'category_comparison': defaultdict(lambda: {
                'precrawl': 0,
                'inventory': 0,
                'overlap': 0,
                'new': 0,
                'missed': 0
            })
        }

        logger.info("Initialized InventoryComparator")

    def compare(self,
                precrawl_urls: List[Dict],
                inventory_urls: List[Dict]) -> Dict:
        """
        Compare pre-crawl results with inventory

        Args:
            precrawl_urls: List of pre-crawl URL dictionaries
            inventory_urls: List of inventory URL dictionaries

        Returns:
            Comparison results
        """
        logger.info(f"Comparing {len(precrawl_urls)} pre-crawl URLs "
                   f"with {len(inventory_urls)} inventory URLs...")

        # Extract URL sets
        precrawl_set = {url['url'] for url in precrawl_urls}
        inventory_set = {url.get('url', url.get('URL', '')) for url in inventory_urls}

        # Calculate overlap and differences
        overlap = precrawl_set & inventory_set
        new_in_precrawl = precrawl_set - inventory_set
        potentially_missed = inventory_set - precrawl_set

        # Update stats
        self.stats['precrawl_total'] = len(precrawl_set)
        self.stats['inventory_total'] = len(inventory_set)
        self.stats['overlap'] = len(overlap)
        self.stats['new_in_precrawl'] = len(new_in_precrawl)
        self.stats['potentially_missed'] = len(potentially_missed)

        logger.info(f"Overlap: {len(overlap)} ({len(overlap)/len(precrawl_set)*100:.1f}% of pre-crawl)")
        logger.info(f"New in pre-crawl: {len(new_in_precrawl)}")
        logger.info(f"Potentially missed: {len(potentially_missed)}")

        # Category-wise comparison
        self._compare_categories(precrawl_urls, inventory_urls, overlap, new_in_precrawl, potentially_missed)

        # Prepare results
        results = {
            'overlap_urls': sorted(list(overlap)),
            'new_urls': sorted(list(new_in_precrawl))[:100],  # Top 100
            'missed_urls': sorted(list(potentially_missed))[:100]  # Top 100
        }

        return results

    def _compare_categories(self,
                           precrawl_urls: List[Dict],
                           inventory_urls: List[Dict],
                           overlap: Set[str],
                           new: Set[str],
                           missed: Set[str]):
        """
        Compare categories between pre-crawl and inventory

        Args:
            precrawl_urls: Pre-crawl URL dictionaries
            inventory_urls: Inventory URL dictionaries
            overlap: Overlapping URL set
            new: New URL set
            missed: Potentially missed URL set
        """
        # Build category maps for pre-crawl
        precrawl_by_category = defaultdict(set)
        for url_data in precrawl_urls:
            category = url_data.get('category', 'other')
            precrawl_by_category[category].add(url_data['url'])

        # Build category maps for inventory (if available)
        inventory_by_category = defaultdict(set)
        for url_data in inventory_urls:
            url = url_data.get('url', url_data.get('URL', ''))
            category = url_data.get('category', url_data.get('Category', 'unknown'))
            inventory_by_category[category].add(url)

        # Compare each category
        all_categories = set(precrawl_by_category.keys()) | set(inventory_by_category.keys())

        for category in all_categories:
            precrawl_cat_urls = precrawl_by_category.get(category, set())
            inventory_cat_urls = inventory_by_category.get(category, set())

            cat_overlap = precrawl_cat_urls & inventory_cat_urls
            cat_new = precrawl_cat_urls - inventory_cat_urls
            cat_missed = inventory_cat_urls - precrawl_cat_urls

            self.stats['category_comparison'][category] = {
                'precrawl': len(precrawl_cat_urls),
                'inventory': len(inventory_cat_urls),
                'overlap': len(cat_overlap),
                'new': len(cat_new),
                'missed': len(cat_missed)
            }

    def generate_report(self, project_name: str, results: Dict) -> str:
        """
        Generate Markdown comparison report

        Args:
            project_name: Project name
            results: Comparison results

        Returns:
            Markdown string
        """
        precrawl = self.stats['precrawl_total']
        inventory = self.stats['inventory_total']
        overlap = self.stats['overlap']
        new = self.stats['new_in_precrawl']
        missed = self.stats['potentially_missed']

        overlap_pct = (overlap / precrawl * 100) if precrawl > 0 else 0
        new_pct = (new / precrawl * 100) if precrawl > 0 else 0
        missed_pct = (missed / inventory * 100) if inventory > 0 else 0

        md_lines = [
            f"# Inventory Comparison: {project_name.title()}",
            "",
            f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            "## Summary",
            f"- **Pre-Crawl URLs**: {precrawl:,}",
            f"- **Inventory URLs**: {inventory:,}",
            f"- **Overlap**: {overlap:,} ({overlap_pct:.1f}% of pre-crawl)",
            f"- **New in Pre-Crawl**: {new:,} ({new_pct:.1f}%)",
            f"- **Potentially Missed**: {missed:,} ({missed_pct:.1f}% of inventory)",
            ""
        ]

        # Category-wise comparison
        if self.stats['category_comparison']:
            md_lines.extend([
                "## Category-Wise Comparison",
                "| Category | Pre-Crawl | Inventory | Overlap | New | Missed |",
                "|----------|-----------|-----------|---------|-----|--------|"
            ])

            sorted_cats = sorted(self.stats['category_comparison'].items(),
                               key=lambda x: x[1]['precrawl'], reverse=True)

            for category, stats in sorted_cats:
                md_lines.append(
                    f"| {category} | {stats['precrawl']} | {stats['inventory']} | "
                    f"{stats['overlap']} | {stats['new']} | {stats['missed']} |"
                )

            md_lines.append("")

        # Top new discoveries
        if results['new_urls']:
            md_lines.extend([
                "## Top New Discoveries (Not in Inventory)",
                f"*Showing {min(50, len(results['new_urls']))} of {new} new URLs*",
                ""
            ])

            for i, url in enumerate(results['new_urls'][:50], 1):
                md_lines.append(f"{i}. {url}")

            md_lines.append("")

        # Top potentially missed
        if results['missed_urls']:
            md_lines.extend([
                "## Top Potentially Missed (In Inventory, Not in Pre-Crawl)",
                f"*Showing {min(50, len(results['missed_urls']))} of {missed} missed URLs*",
                ""
            ])

            for i, url in enumerate(results['missed_urls'][:50], 1):
                md_lines.append(f"{i}. {url}")

            md_lines.append("")

        # Interpretation
        md_lines.extend([
            "## Interpretation",
            ""
        ])

        if overlap_pct >= 80:
            md_lines.append(f"✅ **Good overlap**: {overlap_pct:.1f}% of pre-crawl URLs are in the inventory.")
        elif overlap_pct >= 60:
            md_lines.append(f"⚠️  **Moderate overlap**: {overlap_pct:.1f}% of pre-crawl URLs are in the inventory.")
        else:
            md_lines.append(f"❌ **Low overlap**: Only {overlap_pct:.1f}% of pre-crawl URLs are in the inventory.")

        md_lines.append("")

        if new > 0:
            md_lines.append(f"- **{new} new URLs** were discovered in the pre-crawl that aren't in the inventory.")
            md_lines.append("  - These may be new additions to FHIR R4 since the inventory was created")
            md_lines.append("  - Or they may be URLs that weren't captured in the original crawl")

        md_lines.append("")

        if missed > 0:
            md_lines.append(f"- **{missed} potentially missed URLs** are in the inventory but not in the pre-crawl.")
            md_lines.append("  - These may not match the project's required resources or BM25 queries")
            md_lines.append("  - Or they may have been filtered out by score thresholds or category limits")

        md_lines.append("")
        md_lines.append("---")
        md_lines.append(f"*Report generated: {datetime.now().isoformat()}*")

        return "\n".join(md_lines)


def load_precrawl_data(path: Path) -> List[Dict]:
    """
    Load pre-crawl filtered URLs

    Args:
        path: Path to filtered CSV

    Returns:
        List of URL dictionaries
    """
    if not path.exists():
        raise FileNotFoundError(f"Pre-crawl file not found: {path}")

    logger.info(f"Loading pre-crawl data from {path}")

    df = pd.read_csv(path)
    df = df.fillna('')

    urls = df.to_dict('records')

    logger.info(f"Loaded {len(urls)} pre-crawl URLs")

    return urls


def load_inventory_data(path: Path) -> List[Dict]:
    """
    Load existing inventory

    Args:
        path: Path to inventory CSV

    Returns:
        List of URL dictionaries
    """
    if not path.exists():
        logger.warning(f"Inventory file not found: {path}")
        return []

    logger.info(f"Loading inventory from {path}")

    df = pd.read_csv(path)
    df = df.fillna('')

    urls = df.to_dict('records')

    logger.info(f"Loaded {len(urls)} inventory URLs")

    return urls


def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(description='FHIR R4 Inventory Comparison')

    parser.add_argument('precrawl', type=Path, help='Pre-crawl filtered CSV file')
    parser.add_argument('inventory', type=Path, help='Existing inventory CSV file')
    parser.add_argument('-o', '--output', type=Path, required=True,
                       help='Output Markdown report')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose logging')

    args = parser.parse_args()

    # Set logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    try:
        # Load data
        precrawl_urls = load_precrawl_data(args.precrawl)
        inventory_urls = load_inventory_data(args.inventory)

        if not inventory_urls:
            logger.warning("No inventory data found. Comparison will be limited.")

        # Initialize comparator
        comparator = InventoryComparator()

        # Compare
        results = comparator.compare(precrawl_urls, inventory_urls)

        # Generate report
        project_name = args.precrawl.stem.split('_')[0]  # e.g., 'andor' from 'andor_filtered_urls'
        report = comparator.generate_report(project_name, results)

        # Save report
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, 'w') as f:
            f.write(report)

        logger.info(f"Report saved to {args.output}")

        # Print summary
        print("\n" + "=" * 60)
        print("INVENTORY COMPARISON SUMMARY")
        print("=" * 60)
        print(f"Pre-Crawl URLs: {comparator.stats['precrawl_total']:,}")
        print(f"Inventory URLs: {comparator.stats['inventory_total']:,}")
        print(f"Overlap: {comparator.stats['overlap']:,} ({comparator.stats['overlap']/comparator.stats['precrawl_total']*100:.1f}%)")
        print(f"New: {comparator.stats['new_in_precrawl']:,}")
        print(f"Missed: {comparator.stats['potentially_missed']:,}")

        print(f"\n✅ Comparison complete! Report saved to {args.output}")

    except Exception as e:
        logger.error(f"Comparison failed: {e}")
        raise


if __name__ == "__main__":
    main()
