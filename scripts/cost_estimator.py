#!/usr/bin/env python3
"""
FHIR R4 Cost Estimator Script
Version: 1.0
Date: November 10, 2025
Author: Symphony Corp

Purpose: Estimate time and token costs for crawl plan, compare to full crawl
"""

import argparse
import json
import logging
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List

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


class CostEstimator:
    """
    Estimates time and token costs for FHIR crawl plan
    """

    # Default token averages per category
    DEFAULT_TOKEN_AVGS = {
        'resource': 6500,
        'module': 4500,
        'profile': 5000,
        'operation': 3500,
        'valueset': 2200,
        'codesystem': 2600,
        'extension': 2000,
        'example': 2500,
        'searchparameter': 1800,
        'other': 3000
    }

    # Default time per page (seconds)
    TIME_BASE_D0 = 4  # Base time for depth 0 page
    TIME_ADD = {1: 6, 2: 12, 3: 20}  # Additional seconds per child at each depth

    def __init__(self,
                 token_avgs: Dict[str, int] = None,
                 time_base: float = None,
                 time_add: Dict[int, float] = None):
        """
        Initialize cost estimator

        Args:
            token_avgs: Override token averages per category
            time_base: Override base time per page
            time_add: Override additional time per depth
        """
        self.token_avgs = token_avgs or self.DEFAULT_TOKEN_AVGS
        self.time_base = time_base or self.TIME_BASE_D0
        self.time_add = time_add or self.TIME_ADD

        # Statistics
        self.stats = {
            'total_pages': 0,
            'total_estimated_children': 0,
            'total_time_seconds': 0,
            'total_tokens': 0,
            'by_depth': {
                0: {'pages': 0, 'time_sec': 0, 'tokens': 0},
                1: {'pages': 0, 'time_sec': 0, 'tokens': 0},
                2: {'pages': 0, 'time_sec': 0, 'tokens': 0},
                3: {'pages': 0, 'time_sec': 0, 'tokens': 0}
            },
            'by_category': defaultdict(lambda: {'pages': 0, 'tokens': 0, 'avg_tokens': 0})
        }

        logger.info("Initialized CostEstimator")

    def estimate_time(self, depth: int, children: int) -> float:
        """
        Estimate time for a single URL

        Args:
            depth: Crawl depth
            children: Number of children

        Returns:
            Estimated time in seconds
        """
        # Base time + additional time per child
        time = self.time_base + (children * self.time_add.get(depth, 0))
        return time

    def estimate_tokens(self, category: str, pages: int) -> int:
        """
        Estimate tokens for pages in a category

        Args:
            category: URL category
            pages: Number of pages (including children)

        Returns:
            Estimated total tokens
        """
        avg_tokens = self.token_avgs.get(category, self.token_avgs['other'])
        total_tokens = pages * avg_tokens
        return total_tokens

    def estimate_costs(self, urls_data: List[Dict]) -> Dict:
        """
        Estimate costs for all URLs

        Args:
            urls_data: List of URL dictionaries with depths

        Returns:
            Cost estimate dictionary
        """
        logger.info(f"Estimating costs for {len(urls_data)} URLs...")

        self.stats['total_pages'] = len(urls_data)

        # Process each URL
        for url_data in urls_data:
            depth = url_data.get('assigned_depth', 0)
            children = url_data.get('estimated_children', 0)
            category = url_data.get('category', 'other')

            # Estimate time for this URL
            time_sec = self.estimate_time(depth, children)

            # Estimate tokens for this URL + children
            total_pages = 1 + children
            tokens = self.estimate_tokens(category, total_pages)

            # Update global stats
            self.stats['total_estimated_children'] += children
            self.stats['total_time_seconds'] += time_sec
            self.stats['total_tokens'] += tokens

            # Update by_depth stats
            self.stats['by_depth'][depth]['pages'] += 1
            self.stats['by_depth'][depth]['time_sec'] += time_sec
            self.stats['by_depth'][depth]['tokens'] += tokens

            # Update by_category stats
            self.stats['by_category'][category]['pages'] += total_pages
            self.stats['by_category'][category]['tokens'] += tokens

        # Calculate category averages
        for category, stats in self.stats['by_category'].items():
            if stats['pages'] > 0:
                stats['avg_tokens'] = round(stats['tokens'] / stats['pages'])

        # Calculate total pages
        self.stats['total_pages'] = len(urls_data) + self.stats['total_estimated_children']

        logger.info(f"Estimated {self.stats['total_pages']:,} total pages, "
                   f"{self.stats['total_time_seconds']:,} seconds, "
                   f"{self.stats['total_tokens']:,} tokens")

        return dict(self.stats)

    def compare_to_full_crawl(self,
                              full_crawl_url_count: int = 2000,
                              full_crawl_depth: int = 3) -> Dict:
        """
        Compare to full crawl baseline

        Args:
            full_crawl_url_count: Number of URLs in full crawl
            full_crawl_depth: Depth for full crawl

        Returns:
            Comparison dictionary
        """
        logger.info(f"Comparing to full crawl: {full_crawl_url_count} URLs at depth {full_crawl_depth}")

        # Estimate full crawl time
        # Assume average children per depth from our estimates
        avg_children = {
            0: 0,
            1: 2,
            2: 5,
            3: 10
        }

        full_children = avg_children[full_crawl_depth]
        full_time_per_url = self.time_base + (full_children * self.time_add.get(full_crawl_depth, 0))
        full_crawl_time = full_crawl_url_count * full_time_per_url

        # Estimate full crawl tokens
        # Assume average distribution across categories
        avg_tokens = sum(self.token_avgs.values()) / len(self.token_avgs)
        full_pages = full_crawl_url_count * (1 + full_children)
        full_crawl_tokens = full_pages * avg_tokens

        # Calculate savings
        time_saved = full_crawl_time - self.stats['total_time_seconds']
        tokens_saved = full_crawl_tokens - self.stats['total_tokens']

        time_reduction_pct = (time_saved / full_crawl_time * 100) if full_crawl_time > 0 else 0
        token_reduction_pct = (tokens_saved / full_crawl_tokens * 100) if full_crawl_tokens > 0 else 0

        comparison = {
            'full_crawl_url_count': full_crawl_url_count,
            'full_crawl_depth': full_crawl_depth,
            'full_crawl_time_sec': round(full_crawl_time),
            'full_crawl_tokens': round(full_crawl_tokens),
            'filtered_crawl_time_sec': round(self.stats['total_time_seconds']),
            'filtered_crawl_tokens': self.stats['total_tokens'],
            'time_saved_sec': round(time_saved),
            'time_saved_human': self._format_duration(time_saved),
            'tokens_saved': round(tokens_saved),
            'time_reduction_pct': round(time_reduction_pct, 1),
            'token_reduction_pct': round(token_reduction_pct, 1)
        }

        logger.info(f"Savings: {time_reduction_pct:.1f}% time, {token_reduction_pct:.1f}% tokens")

        return comparison

    def _format_duration(self, seconds: float) -> str:
        """
        Format duration in human-readable form

        Args:
            seconds: Duration in seconds

        Returns:
            Formatted string (e.g., "2h 30m")
        """
        if seconds < 0:
            return "0m"

        td = timedelta(seconds=int(seconds))
        hours, remainder = divmod(td.seconds, 3600)
        minutes, _ = divmod(remainder, 60)

        parts = []
        if td.days > 0:
            parts.append(f"{td.days}d")
        if hours > 0:
            parts.append(f"{hours}h")
        if minutes > 0 or not parts:
            parts.append(f"{minutes}m")

        return " ".join(parts)

    def generate_report(self, comparison: Dict = None) -> Dict:
        """
        Generate comprehensive cost report

        Args:
            comparison: Optional full crawl comparison

        Returns:
            Report dictionary
        """
        report = {
            'timestamp': datetime.now().isoformat(),
            'total_pages': self.stats['total_pages'],
            'total_estimated_children': self.stats['total_estimated_children'],
            'total_time_seconds': round(self.stats['total_time_seconds']),
            'total_time_human': self._format_duration(self.stats['total_time_seconds']),
            'total_tokens': self.stats['total_tokens'],
            'by_depth': {},
            'by_category': {},
            'assumptions': {
                'per_category_token_avg': dict(self.token_avgs),
                'per_depth_time_sec': {
                    'base_d0': self.time_base,
                    'd1_add': self.time_add.get(1, 0),
                    'd2_add': self.time_add.get(2, 0),
                    'd3_add': self.time_add.get(3, 0)
                }
            }
        }

        # Add by_depth breakdown
        for depth in range(4):
            depth_stats = self.stats['by_depth'][depth]
            report['by_depth'][str(depth)] = {
                'pages': depth_stats['pages'],
                'time_sec': round(depth_stats['time_sec']),
                'time_human': self._format_duration(depth_stats['time_sec']),
                'tokens': depth_stats['tokens']
            }

        # Add by_category breakdown
        for category, stats in self.stats['by_category'].items():
            report['by_category'][category] = {
                'pages': stats['pages'],
                'tokens': stats['tokens'],
                'avg_tokens': stats['avg_tokens']
            }

        # Add comparison if provided
        if comparison:
            report['full_crawl_comparison'] = comparison

        return report

    def generate_markdown_report(self, report: Dict, project_name: str) -> str:
        """
        Generate Markdown-formatted cost report

        Args:
            report: Cost report dictionary
            project_name: Project name

        Returns:
            Markdown string
        """
        md_lines = [
            f"# FHIR R4 Pre-Crawl Cost Estimate: {project_name.title()}",
            "",
            "## Summary",
            f"- **Total Pages**: {report['total_pages']:,} ({report['total_pages'] - report['total_estimated_children']} seed + {report['total_estimated_children']} children)",
            f"- **Estimated Time**: {report['total_time_human']}",
            f"- **Estimated Tokens**: {report['total_tokens']:,}",
        ]

        if 'full_crawl_comparison' in report:
            comp = report['full_crawl_comparison']
            md_lines.extend([
                f"- **Cost Reduction**: {comp['time_reduction_pct']}% time, {comp['token_reduction_pct']}% tokens vs full crawl",
                ""
            ])

        md_lines.extend([
            "## Breakdown by Depth",
            "| Depth | Pages | Time | Tokens | Avg Tokens/Page |",
            "|-------|-------|------|--------|-----------------|"
        ])

        for depth in range(4):
            depth_str = str(depth)
            if depth_str in report['by_depth']:
                d = report['by_depth'][depth_str]
                avg_tokens = round(d['tokens'] / d['pages']) if d['pages'] > 0 else 0
                md_lines.append(
                    f"| {depth} | {d['pages']} | {d['time_human']} | {d['tokens']:,} | {avg_tokens:,} |"
                )

        md_lines.extend([
            "",
            "## Breakdown by Category",
            "| Category | Pages | Tokens | Avg Tokens/Page |",
            "|----------|-------|--------|-----------------|"
        ])

        # Sort categories by page count
        sorted_cats = sorted(report['by_category'].items(),
                           key=lambda x: x[1]['pages'], reverse=True)

        for category, stats in sorted_cats:
            md_lines.append(
                f"| {category} | {stats['pages']} | {stats['tokens']:,} | {stats['avg_tokens']:,} |"
            )

        if 'full_crawl_comparison' in report:
            comp = report['full_crawl_comparison']
            md_lines.extend([
                "",
                "## Full Crawl Comparison",
                f"- **Full Crawl**: {comp['full_crawl_url_count']:,} URLs at depth {comp['full_crawl_depth']} = {self._format_duration(comp['full_crawl_time_sec'])}, {comp['full_crawl_tokens']:,} tokens",
                f"- **Pre-Crawl**: {report['total_pages']:,} pages = {report['total_time_human']}, {report['total_tokens']:,} tokens",
                f"- **Savings**: {comp['time_saved_human']} ({comp['time_reduction_pct']}%), {comp['tokens_saved']:,} tokens ({comp['token_reduction_pct']}%)",
                ""
            ])

        md_lines.extend([
            "## Assumptions",
            "",
            "### Token Averages per Category",
            "| Category | Avg Tokens |",
            "|----------|------------|"
        ])

        for cat, tokens in sorted(report['assumptions']['per_category_token_avg'].items()):
            md_lines.append(f"| {cat} | {tokens:,} |")

        time_assumptions = report['assumptions']['per_depth_time_sec']
        md_lines.extend([
            "",
            "### Time per Page (seconds)",
            f"- **Base (depth 0)**: {time_assumptions['base_d0']}s",
            f"- **Depth 1 add**: +{time_assumptions['d1_add']}s per child",
            f"- **Depth 2 add**: +{time_assumptions['d2_add']}s per child",
            f"- **Depth 3 add**: +{time_assumptions['d3_add']}s per child",
            "",
            f"---",
            f"*Generated: {report['timestamp']}*"
        ])

        return "\n".join(md_lines)


def load_depth_data(input_path: Path) -> List[Dict]:
    """
    Load URLs with depths from CSV

    Args:
        input_path: Path to CSV with assigned depths

    Returns:
        List of URL dictionaries
    """
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    logger.info(f"Loading depth data from {input_path}")

    df = pd.read_csv(input_path)
    df = df.fillna('')

    urls_data = df.to_dict('records')

    logger.info(f"Loaded {len(urls_data)} URLs")

    return urls_data


def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(description='FHIR R4 Cost Estimator')

    parser.add_argument('input', type=Path, help='Input CSV with assigned depths')
    parser.add_argument('-o', '--output', type=Path, required=True, help='Output JSON file')
    parser.add_argument('--report', type=Path, help='Generate Markdown report')
    parser.add_argument('--full-crawl-urls', type=int, default=2000,
                       help='Full crawl URL count for comparison (default: 2000)')
    parser.add_argument('--full-crawl-depth', type=int, default=3,
                       help='Full crawl depth for comparison (default: 3)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose logging')

    args = parser.parse_args()

    # Set logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    try:
        # Load input data
        urls_data = load_depth_data(args.input)

        # Initialize estimator
        estimator = CostEstimator()

        # Estimate costs
        estimator.estimate_costs(urls_data)

        # Compare to full crawl
        comparison = estimator.compare_to_full_crawl(
            full_crawl_url_count=args.full_crawl_urls,
            full_crawl_depth=args.full_crawl_depth
        )

        # Generate report
        report = estimator.generate_report(comparison=comparison)

        # Save JSON report
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, 'w') as f:
            json.dump(report, f, indent=2)

        logger.info(f"Report saved to {args.output}")

        # Generate Markdown report if requested
        if args.report:
            project_name = args.input.stem.split('_')[0]  # e.g., 'andor' from 'andor_urls_with_depth'
            markdown = estimator.generate_markdown_report(report, project_name)

            args.report.parent.mkdir(parents=True, exist_ok=True)
            with open(args.report, 'w') as f:
                f.write(markdown)

            logger.info(f"Markdown report saved to {args.report}")

        # Print summary
        print("\n" + "=" * 60)
        print("COST ESTIMATE SUMMARY")
        print("=" * 60)
        print(f"Total Pages: {report['total_pages']:,}")
        print(f"Estimated Time: {report['total_time_human']}")
        print(f"Estimated Tokens: {report['total_tokens']:,}")
        print(f"\nFull Crawl Comparison:")
        print(f"  Time Reduction: {comparison['time_reduction_pct']}%")
        print(f"  Token Reduction: {comparison['token_reduction_pct']}%")
        print(f"  Time Saved: {comparison['time_saved_human']}")
        print(f"  Tokens Saved: {comparison['tokens_saved']:,}")

        print(f"\n✅ Cost estimation complete!")
        print(f"JSON: {args.output}")
        if args.report:
            print(f"Markdown: {args.report}")

    except Exception as e:
        logger.error(f"Cost estimation failed: {e}")
        raise


if __name__ == "__main__":
    main()
