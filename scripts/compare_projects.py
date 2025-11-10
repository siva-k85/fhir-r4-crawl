#!/usr/bin/env python3
"""
FHIR R4 Project Comparison Script
Version: 1.0
Date: November 10, 2025
Author: Symphony Corp

Purpose: Compare Andor vs WHIO filtering results side-by-side
"""

import argparse
import json
import logging
from collections import Counter, defaultdict
from datetime import datetime
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


class ProjectComparator:
    """
    Compares two FHIR projects (e.g., Andor vs WHIO) side-by-side
    """

    def __init__(self, project1_name: str, project2_name: str):
        """
        Initialize comparator

        Args:
            project1_name: First project name
            project2_name: Second project name
        """
        self.project1_name = project1_name
        self.project2_name = project2_name

        logger.info(f"Initialized ProjectComparator: {project1_name} vs {project2_name}")

    def compare(self,
                project1_urls: List[Dict],
                project2_urls: List[Dict]) -> Dict:
        """
        Compare two projects

        Args:
            project1_urls: First project URL dictionaries
            project2_urls: Second project URL dictionaries

        Returns:
            Comparison results
        """
        logger.info(f"Comparing {len(project1_urls)} URLs from {self.project1_name} "
                   f"with {len(project2_urls)} URLs from {self.project2_name}")

        # Extract URL sets
        p1_urls = {url['url'] for url in project1_urls}
        p2_urls = {url['url'] for url in project2_urls}

        # Calculate overlap and differences
        shared = p1_urls & p2_urls
        p1_only = p1_urls - p2_urls
        p2_only = p2_urls - p1_urls

        # Category distributions
        p1_categories = Counter(url.get('category', 'other') for url in project1_urls)
        p2_categories = Counter(url.get('category', 'other') for url in project2_urls)

        # Implementation guide coverage
        p1_igs = Counter(url.get('implementation_guide', '') for url in project1_urls if url.get('implementation_guide'))
        p2_igs = Counter(url.get('implementation_guide', '') for url in project2_urls if url.get('implementation_guide'))

        # Score distributions
        p1_scores = [url.get('final_relevance', 0.0) for url in project1_urls]
        p2_scores = [url.get('final_relevance', 0.0) for url in project2_urls]

        # Depth distributions (if available)
        p1_depths = Counter(url.get('assigned_depth', 0) for url in project1_urls if 'assigned_depth' in url)
        p2_depths = Counter(url.get('assigned_depth', 0) for url in project2_urls if 'assigned_depth' in url)

        results = {
            'totals': {
                self.project1_name: len(p1_urls),
                self.project2_name: len(p2_urls)
            },
            'overlap': {
                'count': len(shared),
                f'{self.project1_name}_pct': round(len(shared) / len(p1_urls) * 100, 1) if p1_urls else 0,
                f'{self.project2_name}_pct': round(len(shared) / len(p2_urls) * 100, 1) if p2_urls else 0
            },
            'unique': {
                f'{self.project1_name}_only': len(p1_only),
                f'{self.project2_name}_only': len(p2_only)
            },
            'categories': {
                self.project1_name: dict(p1_categories),
                self.project2_name: dict(p2_categories)
            },
            'implementation_guides': {
                self.project1_name: dict(p1_igs),
                self.project2_name: dict(p2_igs)
            },
            'score_stats': {
                self.project1_name: {
                    'min': round(min(p1_scores), 3) if p1_scores else 0,
                    'max': round(max(p1_scores), 3) if p1_scores else 0,
                    'mean': round(sum(p1_scores) / len(p1_scores), 3) if p1_scores else 0
                },
                self.project2_name: {
                    'min': round(min(p2_scores), 3) if p2_scores else 0,
                    'max': round(max(p2_scores), 3) if p2_scores else 0,
                    'mean': round(sum(p2_scores) / len(p2_scores), 3) if p2_scores else 0
                }
            }
        }

        # Add depth distributions if available
        if p1_depths or p2_depths:
            results['depth_distribution'] = {
                self.project1_name: dict(p1_depths),
                self.project2_name: dict(p2_depths)
            }

        logger.info(f"Shared URLs: {len(shared)} ({results['overlap'][f'{self.project1_name}_pct']}% / "
                   f"{results['overlap'][f'{self.project2_name}_pct']}%)")

        return results

    def generate_report(self, results: Dict) -> str:
        """
        Generate Markdown comparison report

        Args:
            results: Comparison results

        Returns:
            Markdown string
        """
        p1 = self.project1_name.title()
        p2 = self.project2_name.title()

        md_lines = [
            f"# Project Comparison: {p1} vs {p2}",
            "",
            f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
            "## Overview",
            "| Metric | " + p1 + " | " + p2 + " |",
            "|--------|" + "-" * len(p1) + "-|" + "-" * len(p2) + "-|",
            f"| Total URLs | {results['totals'][self.project1_name]:,} | {results['totals'][self.project2_name]:,} |",
            ""
        ]

        # Shared vs unique
        md_lines.extend([
            "## Shared vs Unique URLs",
            f"- **Shared**: {results['overlap']['count']:,} "
            f"({results['overlap'][f'{self.project1_name}_pct']}% of {p1}, "
            f"{results['overlap'][f'{self.project2_name}_pct']}% of {p2})",
            f"- **{p1} Only**: {results['unique'][f'{self.project1_name}_only']:,}",
            f"- **{p2} Only**: {results['unique'][f'{self.project2_name}_only']:,}",
            ""
        ])

        # Category distribution
        md_lines.extend([
            "## Category Distribution",
            "| Category | " + p1 + " Count | " + p1 + " % | " + p2 + " Count | " + p2 + " % |",
            "|----------|" + "-" * (len(p1) + 6) + "|" + "-" * (len(p1) + 2) + "|" +
            "-" * (len(p2) + 6) + "|" + "-" * (len(p2) + 2) + "|"
        ])

        # Get all categories
        all_cats = set(results['categories'][self.project1_name].keys()) | \
                  set(results['categories'][self.project2_name].keys())

        sorted_cats = sorted(all_cats)

        for cat in sorted_cats:
            p1_count = results['categories'][self.project1_name].get(cat, 0)
            p2_count = results['categories'][self.project2_name].get(cat, 0)

            p1_pct = (p1_count / results['totals'][self.project1_name] * 100) if results['totals'][self.project1_name] > 0 else 0
            p2_pct = (p2_count / results['totals'][self.project2_name] * 100) if results['totals'][self.project2_name] > 0 else 0

            md_lines.append(f"| {cat} | {p1_count} | {p1_pct:.1f}% | {p2_count} | {p2_pct:.1f}% |")

        md_lines.append("")

        # Implementation guide coverage
        if results['implementation_guides'][self.project1_name] or results['implementation_guides'][self.project2_name]:
            md_lines.extend([
                "## Implementation Guide Coverage",
                "| IG | " + p1 + " URLs | " + p2 + " URLs |",
                "|----|" + "-" * (len(p1) + 5) + "|" + "-" * (len(p2) + 5) + "|"
            ])

            all_igs = set(results['implementation_guides'][self.project1_name].keys()) | \
                     set(results['implementation_guides'][self.project2_name].keys())

            sorted_igs = sorted(all_igs)

            for ig in sorted_igs:
                p1_count = results['implementation_guides'][self.project1_name].get(ig, 0)
                p2_count = results['implementation_guides'][self.project2_name].get(ig, 0)
                md_lines.append(f"| {ig} | {p1_count} | {p2_count} |")

            md_lines.append("")

        # Score distributions
        md_lines.extend([
            "## Score Distributions",
            "| Statistic | " + p1 + " | " + p2 + " |",
            "|-----------|" + "-" * len(p1) + "-|" + "-" * len(p2) + "-|",
            f"| Min | {results['score_stats'][self.project1_name]['min']:.3f} | {results['score_stats'][self.project2_name]['min']:.3f} |",
            f"| Max | {results['score_stats'][self.project1_name]['max']:.3f} | {results['score_stats'][self.project2_name]['max']:.3f} |",
            f"| Mean | {results['score_stats'][self.project1_name]['mean']:.3f} | {results['score_stats'][self.project2_name]['mean']:.3f} |",
            ""
        ])

        # Depth distribution (if available)
        if 'depth_distribution' in results:
            md_lines.extend([
                "## Depth Distribution",
                "| Depth | " + p1 + " URLs | " + p2 + " URLs |",
                "|-------|" + "-" * (len(p1) + 5) + "|" + "-" * (len(p2) + 5) + "|"
            ])

            for depth in range(4):
                p1_count = results['depth_distribution'][self.project1_name].get(depth, 0)
                p2_count = results['depth_distribution'][self.project2_name].get(depth, 0)
                md_lines.append(f"| {depth} | {p1_count} | {p2_count} |")

            md_lines.append("")

        # Interpretation
        md_lines.extend([
            "## Interpretation",
            ""
        ])

        overlap_pct_avg = (results['overlap'][f'{self.project1_name}_pct'] +
                          results['overlap'][f'{self.project2_name}_pct']) / 2

        if overlap_pct_avg >= 50:
            md_lines.append(f"- **High overlap** ({overlap_pct_avg:.1f}% average): Projects have significant shared requirements.")
        elif overlap_pct_avg >= 30:
            md_lines.append(f"- **Moderate overlap** ({overlap_pct_avg:.1f}% average): Projects have some common requirements.")
        else:
            md_lines.append(f"- **Low overlap** ({overlap_pct_avg:.1f}% average): Projects have distinct requirements.")

        md_lines.append("")
        md_lines.append("---")
        md_lines.append(f"*Report generated: {datetime.now().isoformat()}*")

        return "\n".join(md_lines)


def load_project_data(path: Path) -> List[Dict]:
    """
    Load project filtered URLs

    Args:
        path: Path to filtered CSV

    Returns:
        List of URL dictionaries
    """
    if not path.exists():
        raise FileNotFoundError(f"Project file not found: {path}")

    logger.info(f"Loading project data from {path}")

    df = pd.read_csv(path)
    df = df.fillna('')

    urls = df.to_dict('records')

    logger.info(f"Loaded {len(urls)} URLs")

    return urls


def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(description='FHIR R4 Project Comparison')

    parser.add_argument('project1', type=Path, help='First project filtered CSV file')
    parser.add_argument('project2', type=Path, help='Second project filtered CSV file')
    parser.add_argument('-o', '--output', type=Path, required=True,
                       help='Output Markdown report')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose logging')

    args = parser.parse_args()

    # Set logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    try:
        # Load data
        project1_urls = load_project_data(args.project1)
        project2_urls = load_project_data(args.project2)

        # Extract project names
        p1_name = args.project1.stem.split('_')[0]  # e.g., 'andor' from 'andor_filtered_urls'
        p2_name = args.project2.stem.split('_')[0]

        # Initialize comparator
        comparator = ProjectComparator(p1_name, p2_name)

        # Compare
        results = comparator.compare(project1_urls, project2_urls)

        # Generate report
        report = comparator.generate_report(results)

        # Save report
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, 'w') as f:
            f.write(report)

        logger.info(f"Report saved to {args.output}")

        # Print summary
        print("\n" + "=" * 60)
        print("PROJECT COMPARISON SUMMARY")
        print("=" * 60)
        print(f"{p1_name.title()}: {results['totals'][p1_name]:,} URLs")
        print(f"{p2_name.title()}: {results['totals'][p2_name]:,} URLs")
        print(f"Shared: {results['overlap']['count']:,} URLs")
        print(f"{p1_name.title()} Only: {results['unique'][f'{p1_name}_only']:,} URLs")
        print(f"{p2_name.title()} Only: {results['unique'][f'{p2_name}_only']:,} URLs")

        print(f"\n✅ Comparison complete! Report saved to {args.output}")

    except Exception as e:
        logger.error(f"Comparison failed: {e}")
        raise


if __name__ == "__main__":
    main()
