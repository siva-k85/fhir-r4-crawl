#!/usr/bin/env python3
"""
FHIR R4 Project Filter Script
Version: 1.0
Date: November 10, 2025
Author: Symphony Corp

Purpose: Apply project-specific BM25 filtering, pattern matching, and required resource inclusion
"""

import argparse
import json
import logging
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from urllib.parse import urlparse, urlunparse

import pandas as pd
import yaml
from rank_bm25 import BM25Okapi

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class ProjectFilter:
    """
    Filters FHIR URLs using project-specific criteria:
    - BM25 scoring against project queries
    - Pattern-based include/exclude
    - Required resource inclusion
    - Category-based weighting and limits
    """

    def __init__(self, config_path: Path):
        """
        Initialize filter with project configuration

        Args:
            config_path: Path to project YAML config
        """
        self.config_path = config_path
        self.config = self._load_config()
        self.project_name = self.config_path.stem.split('_')[0]  # e.g., 'andor' from 'andor_crawl_config.yml'

        # Statistics
        self.stats = {
            'processed': 0,
            'kept': 0,
            'dropped': 0,
            'categories': defaultdict(lambda: {'kept': 0, 'dropped': 0}),
            'required_resources': {'covered': set(), 'missing': set()},
            'pattern_stats': {'include_hits': 0, 'exclude_drops': 0},
            'score_stats': {'min': 1.0, 'max': 0.0, 'sum': 0.0, 'count': 0},
            'top_queries': defaultdict(lambda: {'avg_score': 0.0, 'hits': 0, 'sum': 0.0})
        }

        # Configure logging
        log_file = f'logs/project_filter_{self.project_name}_{datetime.now():%Y%m%d_%H%M%S}.log'
        Path('logs').mkdir(exist_ok=True)
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        logger.addHandler(file_handler)

        logger.info(f"Initialized ProjectFilter for {self.project_name}")

    def _load_config(self) -> Dict:
        """Load and validate project configuration"""

        if not self.config_path.exists():
            raise FileNotFoundError(f"Config file not found: {self.config_path}")

        with open(self.config_path, 'r') as f:
            config = yaml.safe_load(f)

        # Provide defaults for missing keys
        defaults = {
            'required_resources': [],
            'implementation_guides': [],
            'bm25_queries': [],
            'include_patterns': [],
            'exclude_patterns': [],
            'category_weights': {
                'resource': 1.0,
                'profile': 0.9,
                'operation': 0.8,
                'module': 0.75,
                'valueset': 0.6,
                'codesystem': 0.6,
                'extension': 0.5,
                'example': 0.4,
                'searchparameter': 0.5
            },
            'max_urls_per_category': {
                'resource': 250,
                'profile': 150,
                'operation': 60,
                'module': 30,
                'valueset': 100,
                'codesystem': 80,
                'extension': 40,
                'example': 50,
                'searchparameter': 40
            },
            'score_threshold': 0.55
        }

        # Merge defaults with loaded config
        for key, default_value in defaults.items():
            if key not in config:
                logger.warning(f"Missing config key '{key}', using default")
                config[key] = default_value
            elif isinstance(default_value, dict):
                # Merge nested dicts
                for nested_key, nested_value in default_value.items():
                    if nested_key not in config[key]:
                        config[key][nested_key] = nested_value

        logger.info(f"Loaded config: {len(config['bm25_queries'])} queries, "
                   f"{len(config['required_resources'])} required resources")

        return config

    def _tokenize_url_data(self, url_data: Dict) -> List[str]:
        """
        Tokenize URL data for BM25 corpus

        Args:
            url_data: URL dictionary with metadata

        Returns:
            List of tokens
        """
        # Extract fields
        url = url_data.get('url', '')
        title = url_data.get('title', '')
        description = url_data.get('description', '')
        category = url_data.get('category', '')
        resource_type = url_data.get('resource_type', '')
        implementation_guide = url_data.get('implementation_guide', '')

        # Parse URL path and extract meaningful tokens
        parsed = urlparse(url)
        path_tokens = re.findall(r'[a-zA-Z0-9]+', parsed.path)

        # Combine all text
        text = ' '.join([
            ' '.join(path_tokens),
            title,
            description,
            category,
            resource_type or '',
            implementation_guide or ''
        ])

        # Tokenize: lowercase and split
        tokens = text.lower().split()

        # Remove very short tokens
        tokens = [t for t in tokens if len(t) >= 2]

        return tokens

    def _compute_bm25_scores(self, urls_data: List[Dict]) -> List[Dict]:
        """
        Compute BM25 scores for all URLs against project queries

        Args:
            urls_data: List of URL dictionaries

        Returns:
            List of URL dictionaries with bm25_score and matched_queries added
        """
        logger.info(f"Computing BM25 scores for {len(urls_data)} URLs...")

        # Build corpus
        corpus = [self._tokenize_url_data(url_data) for url_data in urls_data]

        # Initialize BM25
        try:
            bm25 = BM25Okapi(corpus)
        except Exception as e:
            logger.error(f"BM25 initialization failed: {e}")
            # Fallback: assign default scores
            for url_data in urls_data:
                url_data['bm25_score'] = 0.5
                url_data['matched_queries'] = []
            return urls_data

        # Score each URL
        queries = self.config['bm25_queries']
        max_score = 0.0

        for i, url_data in enumerate(urls_data):
            doc_scores = []
            matched_queries = []

            for query in queries:
                # Tokenize query
                query_tokens = query.lower().split()

                # Get score for this URL against this query
                doc_score = bm25.get_scores(query_tokens)[i]
                doc_scores.append(doc_score)

                # Track which queries matched (score > 0)
                if doc_score > 0:
                    matched_queries.append(query)

                    # Update query stats
                    self.stats['top_queries'][query]['sum'] += doc_score
                    self.stats['top_queries'][query]['hits'] += 1

            # Best score across all queries
            best_score = max(doc_scores) if doc_scores else 0.0
            max_score = max(max_score, best_score)

            url_data['bm25_raw_score'] = best_score
            url_data['matched_queries'] = '|'.join(matched_queries[:5])  # Top 5 matches

        # Normalize scores to [0, 1]
        if max_score > 0:
            for url_data in urls_data:
                url_data['bm25_score'] = url_data['bm25_raw_score'] / max_score
        else:
            for url_data in urls_data:
                url_data['bm25_score'] = 0.0

        logger.info(f"BM25 scoring complete. Max raw score: {max_score:.2f}")

        return urls_data

    def _apply_pattern_filters(self, url_data: Dict) -> Tuple[bool, float]:
        """
        Apply include/exclude pattern filters

        Args:
            url_data: URL dictionary

        Returns:
            (keep: bool, boost: float)
        """
        url = url_data['url']

        # Check exclude patterns first
        for pattern in self.config['exclude_patterns']:
            try:
                if re.search(pattern, url, re.IGNORECASE):
                    logger.debug(f"Excluded by pattern '{pattern}': {url}")
                    self.stats['pattern_stats']['exclude_drops'] += 1
                    return False, 0.0
            except re.error as e:
                logger.warning(f"Invalid exclude pattern '{pattern}': {e}")

        # Check include patterns for boost
        boost = 0.0
        for pattern in self.config['include_patterns']:
            try:
                if re.search(pattern, url, re.IGNORECASE):
                    boost = 0.05
                    self.stats['pattern_stats']['include_hits'] += 1
                    break
            except re.error as e:
                logger.warning(f"Invalid include pattern '{pattern}': {e}")

        return True, boost

    def _check_required_inclusion(self, url_data: Dict) -> bool:
        """
        Check if URL should be force-included due to required resources/IGs

        Args:
            url_data: URL dictionary

        Returns:
            True if required, False otherwise
        """
        url = url_data['url'].lower()
        resource_type = (url_data.get('resource_type') or '').lower()
        implementation_guide = (url_data.get('implementation_guide') or '').lower()

        # Check required resources
        for required in self.config['required_resources']:
            required_lower = required.lower()

            # Match by resource_type field
            if resource_type and resource_type == required_lower:
                self.stats['required_resources']['covered'].add(required)
                logger.debug(f"Required resource match (field): {required}")
                return True

            # Match by URL path
            if f'/{required_lower}.html' in url or f'/{required_lower}/' in url:
                self.stats['required_resources']['covered'].add(required)
                logger.debug(f"Required resource match (URL): {required}")
                return True

        # Check implementation guides
        for ig in self.config['implementation_guides']:
            ig_key = ig.get('key', '').lower()
            ig_base_url = ig.get('base_url', '').lower()

            if ig_key and ig_key in url:
                logger.debug(f"Required IG match: {ig_key}")
                return True

            if ig_base_url and ig_base_url in url:
                logger.debug(f"Required IG match (base URL): {ig_key}")
                return True

        return False

    def filter_urls(self, urls_data: List[Dict]) -> List[Dict]:
        """
        Apply complete filtering pipeline

        Args:
            urls_data: List of URL dictionaries from categorization

        Returns:
            List of filtered URL dictionaries
        """
        logger.info(f"Starting filtering for {len(urls_data)} URLs...")

        # Step 1: Compute BM25 scores
        urls_data = self._compute_bm25_scores(urls_data)

        # Step 2: Apply filters and compute final relevance
        filtered_urls = []

        for url_data in urls_data:
            self.stats['processed'] += 1

            # Get category
            category = url_data.get('category', 'other')

            # Apply pattern filters
            keep, pattern_boost = self._apply_pattern_filters(url_data)
            if not keep:
                self.stats['dropped'] += 1
                self.stats['categories'][category]['dropped'] += 1
                continue

            # Get category weight
            category_weight = self.config['category_weights'].get(category, 0.5)

            # Check required inclusion
            required_inclusion = self._check_required_inclusion(url_data)

            # Compute final relevance
            bm25_score = url_data['bm25_score']
            final_relevance = bm25_score * category_weight + pattern_boost

            # Required override: clamp minimum
            if required_inclusion:
                final_relevance = max(final_relevance, 0.65)

            # Add computed fields
            url_data['category_weight'] = category_weight
            url_data['pattern_boost'] = pattern_boost
            url_data['required_inclusion'] = required_inclusion
            url_data['final_relevance'] = round(min(final_relevance, 1.0), 3)

            # Apply score threshold
            if final_relevance < self.config['score_threshold'] and not required_inclusion:
                logger.debug(f"Dropped by threshold: {url_data['url']} (score: {final_relevance:.3f})")
                self.stats['dropped'] += 1
                self.stats['categories'][category]['dropped'] += 1
                continue

            # Update score stats
            self.stats['score_stats']['min'] = min(self.stats['score_stats']['min'], final_relevance)
            self.stats['score_stats']['max'] = max(self.stats['score_stats']['max'], final_relevance)
            self.stats['score_stats']['sum'] += final_relevance
            self.stats['score_stats']['count'] += 1

            filtered_urls.append(url_data)

        logger.info(f"After scoring/thresholding: {len(filtered_urls)} URLs kept")

        # Step 3: Apply per-category caps
        filtered_urls = self._apply_category_caps(filtered_urls)

        # Step 4: Deduplicate
        filtered_urls = self._deduplicate_urls(filtered_urls)

        # Step 5: Check for missing required resources
        self._check_missing_required_resources()

        logger.info(f"Final filtered count: {len(filtered_urls)} URLs")

        return filtered_urls

    def _apply_category_caps(self, urls_data: List[Dict]) -> List[Dict]:
        """
        Enforce max URLs per category

        Args:
            urls_data: List of URL dictionaries

        Returns:
            Capped list of URLs
        """
        logger.info("Applying category caps...")

        # Group by category
        by_category = defaultdict(list)
        for url_data in urls_data:
            category = url_data.get('category', 'other')
            by_category[category].append(url_data)

        # Apply caps
        capped_urls = []
        for category, urls in by_category.items():
            max_urls = self.config['max_urls_per_category'].get(category, 100)

            # Sort by final_relevance DESC, required_inclusion first
            urls.sort(key=lambda x: (x['required_inclusion'], x['final_relevance']), reverse=True)

            # Take top N
            kept = urls[:max_urls]
            dropped = urls[max_urls:]

            capped_urls.extend(kept)

            self.stats['categories'][category]['kept'] += len(kept)
            self.stats['categories'][category]['dropped'] += len(dropped)

            if dropped:
                logger.info(f"Category '{category}': kept {len(kept)}/{len(urls)} (cap: {max_urls})")

        self.stats['kept'] = len(capped_urls)
        self.stats['dropped'] = self.stats['processed'] - self.stats['kept']

        return capped_urls

    def _deduplicate_urls(self, urls_data: List[Dict]) -> List[Dict]:
        """
        Remove duplicate URLs (keep first occurrence)

        Args:
            urls_data: List of URL dictionaries

        Returns:
            Deduplicated list
        """
        logger.info("Deduplicating URLs...")

        seen_canonical = set()
        deduped = []
        duplicates = 0

        for url_data in urls_data:
            # Canonicalize URL (strip fragments and query params)
            url = url_data['url']
            parsed = urlparse(url)
            canonical = urlunparse((
                parsed.scheme,
                parsed.netloc,
                parsed.path,
                '', '', ''
            ))

            if canonical in seen_canonical:
                duplicates += 1
                continue

            seen_canonical.add(canonical)
            deduped.append(url_data)

        if duplicates > 0:
            logger.info(f"Removed {duplicates} duplicate URLs")

        return deduped

    def _check_missing_required_resources(self):
        """Check which required resources are missing from filtered set"""

        all_required = set(self.config['required_resources'])
        covered = self.stats['required_resources']['covered']
        missing = all_required - covered

        self.stats['required_resources']['missing'] = missing

        if missing:
            logger.warning(f"Missing {len(missing)} required resources: {', '.join(sorted(missing))}")
        else:
            logger.info(f"All {len(all_required)} required resources covered")

    def generate_report(self) -> Dict:
        """
        Generate filtering report

        Returns:
            Report dictionary
        """
        # Calculate query averages
        top_queries = []
        for query, data in self.stats['top_queries'].items():
            if data['hits'] > 0:
                avg_score = data['sum'] / data['hits']
                top_queries.append({
                    'query': query,
                    'avg_score': round(avg_score, 3),
                    'hits': data['hits']
                })

        # Sort by hits DESC
        top_queries.sort(key=lambda x: x['hits'], reverse=True)

        # Calculate score stats
        if self.stats['score_stats']['count'] > 0:
            mean_score = self.stats['score_stats']['sum'] / self.stats['score_stats']['count']
        else:
            mean_score = 0.0

        report = {
            'project': self.project_name,
            'timestamp': datetime.now().isoformat(),
            'totals': {
                'processed': self.stats['processed'],
                'kept': self.stats['kept'],
                'dropped': self.stats['dropped'],
                'kept_percentage': round(self.stats['kept'] / self.stats['processed'] * 100, 1) if self.stats['processed'] > 0 else 0
            },
            'categories': {
                cat: dict(data) for cat, data in self.stats['categories'].items()
            },
            'scores': {
                'min': round(self.stats['score_stats']['min'], 3) if self.stats['score_stats']['count'] > 0 else 0,
                'max': round(self.stats['score_stats']['max'], 3),
                'mean': round(mean_score, 3),
                'threshold': self.config['score_threshold']
            },
            'required_resources': {
                'total': len(self.config['required_resources']),
                'covered': len(self.stats['required_resources']['covered']),
                'covered_list': sorted(list(self.stats['required_resources']['covered'])),
                'missing': sorted(list(self.stats['required_resources']['missing']))
            },
            'pattern_stats': dict(self.stats['pattern_stats']),
            'top_queries': top_queries[:10]  # Top 10
        }

        return report


def load_categorized_data(input_path: Path) -> List[Dict]:
    """
    Load categorized URLs from CSV

    Args:
        input_path: Path to categorized_urls.csv

    Returns:
        List of URL dictionaries
    """
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    logger.info(f"Loading categorized data from {input_path}")

    df = pd.read_csv(input_path)

    # Handle NaN values
    df = df.fillna('')

    # Convert to list of dicts
    urls_data = df.to_dict('records')

    logger.info(f"Loaded {len(urls_data)} URLs")

    return urls_data


def save_filtered_data(urls_data: List[Dict], output_path: Path):
    """
    Save filtered URLs to CSV

    Args:
        urls_data: List of filtered URL dictionaries
        output_path: Output file path
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame(urls_data)

    # Reorder columns for readability
    column_order = [
        'url', 'category', 'subcategory', 'resource_type', 'implementation_guide',
        'is_r4', 'bm25_score', 'category_weight', 'pattern_boost',
        'required_inclusion', 'final_relevance', 'matched_queries',
        'title', 'description'
    ]

    # Only include columns that exist
    column_order = [col for col in column_order if col in df.columns]

    # Add remaining columns
    remaining = [col for col in df.columns if col not in column_order]
    column_order.extend(remaining)

    df = df[column_order]
    df.to_csv(output_path, index=False)

    logger.info(f"Saved {len(urls_data)} filtered URLs to {output_path}")


def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(description='FHIR R4 Project Filter')

    parser.add_argument('input', type=Path, help='Input categorized CSV file')
    parser.add_argument('-c', '--config', type=Path, required=True, help='Project config YAML file')
    parser.add_argument('-o', '--output', type=Path, required=True, help='Output filtered CSV file')
    parser.add_argument('--stats', action='store_true', help='Print statistics')
    parser.add_argument('--json', type=Path, help='Save report to JSON file')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose logging')

    args = parser.parse_args()

    # Set logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    try:
        # Load input data
        urls_data = load_categorized_data(args.input)

        # Initialize filter
        project_filter = ProjectFilter(args.config)

        # Filter URLs
        filtered_urls = project_filter.filter_urls(urls_data)

        # Save results
        save_filtered_data(filtered_urls, args.output)

        # Generate report
        report = project_filter.generate_report()

        # Print statistics if requested
        if args.stats:
            print("\n" + "=" * 60)
            print("PROJECT FILTERING STATISTICS")
            print("=" * 60)
            print(f"Project: {report['project']}")
            print(f"\nTotals:")
            print(f"  Processed: {report['totals']['processed']}")
            print(f"  Kept: {report['totals']['kept']} ({report['totals']['kept_percentage']}%)")
            print(f"  Dropped: {report['totals']['dropped']}")

            print(f"\nCategory Distribution:")
            for cat, stats in sorted(report['categories'].items(), key=lambda x: x[1]['kept'], reverse=True):
                print(f"  {cat:20} kept: {stats['kept']:4} | dropped: {stats['dropped']:4}")

            print(f"\nScore Statistics:")
            print(f"  Min: {report['scores']['min']:.3f}")
            print(f"  Max: {report['scores']['max']:.3f}")
            print(f"  Mean: {report['scores']['mean']:.3f}")
            print(f"  Threshold: {report['scores']['threshold']:.3f}")

            print(f"\nRequired Resources:")
            print(f"  Total: {report['required_resources']['total']}")
            print(f"  Covered: {report['required_resources']['covered']}")
            if report['required_resources']['missing']:
                print(f"  Missing: {', '.join(report['required_resources']['missing'])}")

            print(f"\nPattern Statistics:")
            print(f"  Include hits: {report['pattern_stats']['include_hits']}")
            print(f"  Exclude drops: {report['pattern_stats']['exclude_drops']}")

            if report['top_queries']:
                print(f"\nTop Queries:")
                for q in report['top_queries'][:5]:
                    print(f"  {q['query'][:40]:40} | hits: {q['hits']:3} | avg: {q['avg_score']:.3f}")

        # Save JSON report if requested
        if args.json:
            args.json.parent.mkdir(parents=True, exist_ok=True)
            with open(args.json, 'w') as f:
                json.dump(report, f, indent=2)
            logger.info(f"Report saved to {args.json}")

        print(f"\n✅ Filtering complete! {len(filtered_urls)} URLs saved to {args.output}")

    except Exception as e:
        logger.error(f"Filtering failed: {e}")
        raise


if __name__ == "__main__":
    main()
