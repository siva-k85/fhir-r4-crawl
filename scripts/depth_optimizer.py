#!/usr/bin/env python3
"""
FHIR R4 Depth Optimizer Script
Version: 1.0
Date: November 10, 2025
Author: Symphony Corp

Purpose: Assign optimal crawl depths (0-3) based on relevance scores and project strategy
"""

import argparse
import logging
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List

import pandas as pd
import yaml

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class DepthOptimizer:
    """
    Assigns crawl depths to URLs based on:
    - Required resource status (force depth 0)
    - Relevance scores (high/medium/low thresholds)
    - Category defaults
    - Strategy adjustments
    """

    def __init__(self, config_path: Path):
        """
        Initialize depth optimizer

        Args:
            config_path: Path to project YAML config
        """
        self.config_path = config_path
        self.config = self._load_config()
        self.project_name = self.config_path.stem.split('_')[0]

        # Statistics
        self.stats = {
            'total_urls': 0,
            'by_depth': {0: 0, 1: 0, 2: 0, 3: 0},
            'by_category': defaultdict(lambda: {'count': 0, 'avg_depth': 0.0, 'total_depth': 0}),
            'total_children': 0,
            'total_pages': 0,
            'cap_adjustments': 0,
            'demoted_urls': []
        }

        # Configure logging
        log_file = f'logs/depth_optimizer_{self.project_name}_{datetime.now():%Y%m%d_%H%M%S}.log'
        Path('logs').mkdir(exist_ok=True)
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        logger.addHandler(file_handler)

        logger.info(f"Initialized DepthOptimizer for {self.project_name}")

    def _load_config(self) -> Dict:
        """Load and validate depth strategy configuration"""

        if not self.config_path.exists():
            raise FileNotFoundError(f"Config file not found: {self.config_path}")

        with open(self.config_path, 'r') as f:
            config = yaml.safe_load(f)

        # Extract depth_strategy, provide defaults if missing
        depth_strategy = config.get('depth_strategy', {})

        defaults = {
            'required': {
                'resource': 0,
                'profile': 0,
                'operation': 0
            },
            'thresholds': {
                'high': 0.80,
                'medium': 0.65,
                'low': 0.55
            },
            'category_defaults': {
                'resource': 1,
                'profile': 1,
                'operation': 1,
                'module': 1,
                'valueset': 0,
                'codesystem': 0,
                'extension': 0,
                'example': 0,
                'searchparameter': 0
            },
            'adjustments': {
                'example': -1,
                'operation': +1,
                'profile': +1
            },
            'min_depth': 0,
            'max_depth': 3,
            'cap_total_pages': 600,  # Default cap
            'children_estimates': {
                'resource': {0: 0, 1: 2, 2: 5, 3: 10},
                'profile': {0: 0, 1: 1, 2: 3, 3: 6},
                'operation': {0: 0, 1: 1, 2: 2, 3: 4},
                'module': {0: 0, 1: 2, 2: 4, 3: 6},
                'valueset': {0: 0, 1: 1, 2: 2, 3: 3},
                'codesystem': {0: 0, 1: 1, 2: 2, 3: 3},
                'extension': {0: 0, 1: 1, 2: 1, 3: 2},
                'example': {0: 0, 1: 1, 2: 1, 3: 2},
                'searchparameter': {0: 0, 1: 1, 2: 1, 3: 2},
                'other': {0: 0, 1: 1, 2: 2, 3: 3}
            }
        }

        # Merge defaults
        for key, default_value in defaults.items():
            if key not in depth_strategy:
                logger.warning(f"Missing depth_strategy.{key}, using default")
                depth_strategy[key] = default_value
            elif isinstance(default_value, dict):
                # Merge nested dicts
                for nested_key, nested_value in default_value.items():
                    if nested_key not in depth_strategy[key]:
                        depth_strategy[key][nested_key] = nested_value

        config['depth_strategy'] = depth_strategy

        logger.info(f"Loaded depth strategy: cap={depth_strategy['cap_total_pages']}, "
                   f"thresholds={depth_strategy['thresholds']}")

        return config

    def assign_depth(self, url_data: Dict) -> int:
        """
        Assign crawl depth for a single URL

        Args:
            url_data: URL dictionary with metadata

        Returns:
            Assigned depth (0-3)
        """
        strategy = self.config['depth_strategy']

        category = url_data.get('category', 'other')
        required_inclusion = url_data.get('required_inclusion', False)
        final_relevance = url_data.get('final_relevance', 0.0)

        # If required, use required depth
        if required_inclusion:
            depth = strategy['required'].get(category, 0)
            logger.debug(f"Required depth for {category}: {depth}")
            return max(strategy['min_depth'], min(depth, strategy['max_depth']))

        # Start from category default
        depth = strategy['category_defaults'].get(category, 1)

        # Adjust based on relevance score
        if final_relevance >= strategy['thresholds']['high']:
            depth += 1
        elif final_relevance >= strategy['thresholds']['medium']:
            depth += 0  # No change
        elif final_relevance < strategy['thresholds']['low']:
            depth = 0  # Low relevance -> depth 0

        # Apply category-specific adjustments
        adjustment = strategy['adjustments'].get(category, 0)
        depth += adjustment

        # Clamp to [min_depth, max_depth]
        depth = max(strategy['min_depth'], min(depth, strategy['max_depth']))

        return depth

    def estimate_children(self, category: str, depth: int) -> int:
        """
        Estimate number of children for a URL at given depth

        Args:
            category: URL category
            depth: Assigned depth

        Returns:
            Estimated number of children
        """
        strategy = self.config['depth_strategy']
        estimates = strategy['children_estimates']

        category_estimates = estimates.get(category, estimates.get('other', {}))
        children = category_estimates.get(depth, 0)

        return children

    def optimize_depths(self, urls_data: List[Dict]) -> List[Dict]:
        """
        Assign depths to all URLs and enforce cap

        Args:
            urls_data: List of filtered URL dictionaries

        Returns:
            List with assigned_depth, estimated_children, crawl_priority added
        """
        logger.info(f"Optimizing depths for {len(urls_data)} URLs...")

        self.stats['total_urls'] = len(urls_data)

        # Step 1: Assign initial depths
        for url_data in urls_data:
            depth = self.assign_depth(url_data)
            category = url_data.get('category', 'other')
            final_relevance = url_data.get('final_relevance', 0.0)

            # Estimate children
            children = self.estimate_children(category, depth)

            # Compute crawl priority
            priority = round(final_relevance * 100) + depth * 5

            # Add fields
            url_data['assigned_depth'] = depth
            url_data['estimated_children'] = children
            url_data['crawl_priority'] = priority

            # Update stats
            self.stats['by_depth'][depth] += 1
            self.stats['by_category'][category]['count'] += 1
            self.stats['by_category'][category]['total_depth'] += depth
            self.stats['total_children'] += children

        # Calculate total pages
        total_pages = len(urls_data) + self.stats['total_children']
        self.stats['total_pages'] = total_pages

        logger.info(f"Initial assignment: {total_pages} total pages "
                   f"({len(urls_data)} URLs + {self.stats['total_children']} children)")

        # Step 2: Enforce cap if needed
        cap = self.config['depth_strategy']['cap_total_pages']
        if total_pages > cap:
            logger.warning(f"Total pages ({total_pages}) exceeds cap ({cap}). Demoting low-priority URLs...")
            urls_data = self._enforce_cap(urls_data, cap)

        # Step 3: Calculate category averages
        for category, stats in self.stats['by_category'].items():
            if stats['count'] > 0:
                stats['avg_depth'] = round(stats['total_depth'] / stats['count'], 2)

        logger.info(f"Final assignment: {self.stats['total_pages']} total pages "
                   f"({len(urls_data)} URLs + {self.stats['total_children']} children)")

        return urls_data

    def _enforce_cap(self, urls_data: List[Dict], cap: int) -> List[Dict]:
        """
        Iteratively demote low-priority URLs until under cap

        Args:
            urls_data: List of URL dictionaries
            cap: Maximum total pages

        Returns:
            Adjusted list with demoted depths
        """
        # Sort by priority (ascending - lowest first)
        # Don't demote required URLs
        non_required = [u for u in urls_data if not u.get('required_inclusion', False)]
        required = [u for u in urls_data if u.get('required_inclusion', False)]

        non_required.sort(key=lambda x: x['crawl_priority'])

        # Iteratively demote
        while self.stats['total_pages'] > cap and non_required:
            # Find lowest-priority URL with depth > 0
            demoted = False
            for url_data in non_required:
                if url_data['assigned_depth'] > 0:
                    # Demote by 1
                    old_depth = url_data['assigned_depth']
                    new_depth = old_depth - 1

                    # Recalculate children
                    category = url_data['category']
                    old_children = url_data['estimated_children']
                    new_children = self.estimate_children(category, new_depth)

                    # Update
                    url_data['assigned_depth'] = new_depth
                    url_data['estimated_children'] = new_children

                    # Adjust stats
                    self.stats['by_depth'][old_depth] -= 1
                    self.stats['by_depth'][new_depth] += 1
                    self.stats['total_children'] += (new_children - old_children)
                    self.stats['total_pages'] = len(urls_data) + self.stats['total_children']
                    self.stats['cap_adjustments'] += 1

                    # Track demotion
                    self.stats['demoted_urls'].append({
                        'url': url_data['url'][:80],
                        'old_depth': old_depth,
                        'new_depth': new_depth
                    })

                    demoted = True
                    logger.debug(f"Demoted {url_data['url'][:60]} from depth {old_depth} → {new_depth}")

                    # Check if under cap now
                    if self.stats['total_pages'] <= cap:
                        break

            # If couldn't demote anyone, we're done
            if not demoted:
                logger.warning(f"Cannot demote further. Final: {self.stats['total_pages']} pages (cap: {cap})")
                break

        logger.info(f"Cap enforcement complete. Demoted {self.stats['cap_adjustments']} URLs")

        return urls_data

    def print_statistics(self):
        """Print formatted statistics"""

        print("\n" + "=" * 60)
        print("DEPTH OPTIMIZATION STATISTICS")
        print("=" * 60)
        print(f"Project: {self.project_name}")

        print(f"\nTotals:")
        print(f"  URLs: {self.stats['total_urls']}")
        print(f"  Estimated Children: {self.stats['total_children']:,}")
        print(f"  Total Pages: {self.stats['total_pages']:,}")
        print(f"  Cap: {self.config['depth_strategy']['cap_total_pages']:,}")

        print(f"\nDepth Distribution:")
        total = sum(self.stats['by_depth'].values())
        for depth in range(4):
            count = self.stats['by_depth'][depth]
            pct = (count / total * 100) if total > 0 else 0
            print(f"  Depth {depth}: {count:4} URLs ({pct:5.1f}%)")

        print(f"\nCategory Distribution:")
        sorted_cats = sorted(self.stats['by_category'].items(),
                           key=lambda x: x[1]['count'], reverse=True)
        for category, stats in sorted_cats:
            print(f"  {category:20} {stats['count']:4} URLs (avg depth: {stats['avg_depth']:.2f})")

        if self.stats['cap_adjustments'] > 0:
            print(f"\nCap Adjustments:")
            print(f"  Total demoted: {self.stats['cap_adjustments']}")
            print(f"  Final total pages: {self.stats['total_pages']:,}")

            if len(self.stats['demoted_urls']) <= 10:
                print(f"\n  Demoted URLs:")
                for d in self.stats['demoted_urls']:
                    print(f"    {d['url']}: depth {d['old_depth']} → {d['new_depth']}")


def load_filtered_data(input_path: Path) -> List[Dict]:
    """
    Load filtered URLs from CSV

    Args:
        input_path: Path to filtered CSV

    Returns:
        List of URL dictionaries
    """
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    logger.info(f"Loading filtered data from {input_path}")

    df = pd.read_csv(input_path)
    df = df.fillna('')

    urls_data = df.to_dict('records')

    logger.info(f"Loaded {len(urls_data)} URLs")

    return urls_data


def save_depth_data(urls_data: List[Dict], output_path: Path):
    """
    Save URLs with depths to CSV

    Args:
        urls_data: List of URL dictionaries with depths
        output_path: Output file path
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame(urls_data)

    # Reorder columns
    priority_cols = [
        'url', 'category', 'subcategory', 'assigned_depth',
        'estimated_children', 'crawl_priority', 'final_relevance',
        'required_inclusion', 'resource_type', 'implementation_guide'
    ]

    column_order = [col for col in priority_cols if col in df.columns]
    remaining = [col for col in df.columns if col not in column_order]
    column_order.extend(remaining)

    df = df[column_order]
    df.to_csv(output_path, index=False)

    logger.info(f"Saved {len(urls_data)} URLs with depths to {output_path}")


def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(description='FHIR R4 Depth Optimizer')

    parser.add_argument('input', type=Path, help='Input filtered CSV file')
    parser.add_argument('-c', '--config', type=Path, required=True, help='Project config YAML file')
    parser.add_argument('-o', '--output', type=Path, required=True, help='Output CSV with depths')
    parser.add_argument('--stats', action='store_true', help='Print statistics')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose logging')

    args = parser.parse_args()

    # Set logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    try:
        # Load input data
        urls_data = load_filtered_data(args.input)

        # Initialize optimizer
        optimizer = DepthOptimizer(args.config)

        # Optimize depths
        urls_data = optimizer.optimize_depths(urls_data)

        # Save results
        save_depth_data(urls_data, args.output)

        # Print statistics if requested
        if args.stats:
            optimizer.print_statistics()

        print(f"\n✅ Depth optimization complete! {len(urls_data)} URLs saved to {args.output}")

    except Exception as e:
        logger.error(f"Depth optimization failed: {e}")
        raise


if __name__ == "__main__":
    main()
