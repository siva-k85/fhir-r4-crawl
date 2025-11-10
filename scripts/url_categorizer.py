#!/usr/bin/env python3
"""
FHIR R4 URL Categorizer Script
Version: 1.0
Date: November 8, 2025
Author: Symphony Corp

Purpose: Categorize discovered FHIR R4 URLs into taxonomy (resource, module, implementation, etc.)
"""

import argparse
import csv
import json
import logging
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd
import yaml

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'logs/url_categorizer_{datetime.now():%Y%m%d_%H%M%S}.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


# FHIR R4 URL Taxonomy
FHIR_TAXONOMY = {
    'resource': {
        'pattern': r'/R4/([a-z]+)\.html$',
        'exclude_pattern': r'-(profiles?|examples?|definitions?|mappings?|operations?|search|notes)\.html$',
        'examples': ['patient.html', 'coverage.html', 'observation.html'],
        'priority': 'high',
        'depth': 0,
        'description': 'Core FHIR resource definitions'
    },
    'module': {
        'pattern': r'-module\.html$',
        'examples': ['administration-module.html', 'clinical-module.html'],
        'priority': 'medium',
        'depth': 1,
        'description': 'FHIR modules grouping related resources'
    },
    'implementation': {
        'pattern': r'/(datatypes|search|http|operations?|messaging|documents?|terminologies?|security|conformance)\.html$',
        'examples': ['datatypes.html', 'search.html', 'http.html'],
        'priority': 'high',
        'depth': 1,
        'description': 'Implementation and technical specifications'
    },
    'valueset': {
        'pattern': r'/(valueset|vs)-[^/]+\.html$',
        'examples': ['valueset-address-use.html', 'valueset-administrative-gender.html'],
        'priority': 'medium',
        'depth': 1,
        'description': 'Value sets for coded elements'
    },
    'codesystem': {
        'pattern': r'/codesystem-[^/]+\.html$',
        'examples': ['codesystem-observation-status.html'],
        'priority': 'medium',
        'depth': 1,
        'description': 'Code system definitions'
    },
    'profile': {
        'pattern': r'/(profile|structuredefinition)-[^/]+\.html$',
        'examples': ['profile-vitalsigns.html', 'structuredefinition-patient.html'],
        'priority': 'medium',
        'depth': 1,
        'description': 'Resource profiles and structure definitions'
    },
    'extension': {
        'pattern': r'/extension-[^/]+\.html$',
        'examples': ['extension-patient-birthPlace.html'],
        'priority': 'low',
        'depth': 1,
        'description': 'FHIR extensions'
    },
    'example': {
        'pattern': r'-(examples?|instances?)\.html$',
        'examples': ['patient-examples.html', 'observation-examples.html'],
        'priority': 'low',
        'depth': 2,
        'description': 'Resource examples and samples'
    },
    'operation': {
        'pattern': r'/operation-[^/]+\.html$',
        'examples': ['operation-patient-everything.html', 'operation-validate.html'],
        'priority': 'medium',
        'depth': 1,
        'description': 'FHIR operations'
    },
    'searchparameter': {
        'pattern': r'/searchparameter-[^/]+\.html$',
        'examples': ['searchparameter-patient-name.html'],
        'priority': 'low',
        'depth': 1,
        'description': 'Search parameter definitions'
    }
}


class URLCategorizer:
    """
    Categorizes FHIR R4 URLs into taxonomy categories
    """

    def __init__(self):
        """Initialize categorizer"""
        self.categories = FHIR_TAXONOMY
        self.statistics = defaultdict(int)
        self.subcategory_counts = defaultdict(lambda: defaultdict(int))

    def categorize_url(self, url: str, metadata: Optional[Dict] = None) -> Dict:
        """
        Categorize a single URL

        Args:
            url: URL to categorize
            metadata: Optional metadata dictionary

        Returns:
            Categorization result dictionary
        """
        result = {
            'url': url,
            'category': 'other',
            'subcategory': None,
            'priority': 'low',
            'depth_recommendation': 0,
            'confidence': 0.0
        }

        # Check each category pattern
        for cat_name, cat_info in self.categories.items():
            pattern = cat_info['pattern']

            # Check if URL matches pattern
            if re.search(pattern, url):
                # Check exclude pattern if present
                if 'exclude_pattern' in cat_info:
                    if re.search(cat_info['exclude_pattern'], url):
                        continue

                result['category'] = cat_name
                result['priority'] = cat_info['priority']
                result['depth_recommendation'] = cat_info['depth']
                result['confidence'] = 0.9  # High confidence from pattern match

                # Extract subcategory
                result['subcategory'] = self._extract_subcategory(url, cat_name)

                # Update statistics
                self.statistics[cat_name] += 1
                if result['subcategory']:
                    self.subcategory_counts[cat_name][result['subcategory']] += 1

                break

        # If still 'other', try to categorize based on metadata
        if result['category'] == 'other' and metadata:
            result = self._categorize_by_metadata(result, metadata)

        return result

    def _extract_subcategory(self, url: str, category: str) -> Optional[str]:
        """
        Extract subcategory from URL

        Args:
            url: URL to process
            category: Main category

        Returns:
            Subcategory name or None
        """
        if category == 'resource':
            # Extract resource name
            match = re.search(r'/R4/([a-z]+)\.html$', url)
            if match:
                return match.group(1)

        elif category == 'module':
            # Extract module name
            match = re.search(r'([a-z]+)-module\.html$', url)
            if match:
                return f"{match.group(1)}-module"

        elif category == 'valueset':
            # Extract valueset name
            match = re.search(r'/(?:valueset|vs)-([^/]+)\.html$', url)
            if match:
                return match.group(1)

        elif category == 'codesystem':
            # Extract codesystem name
            match = re.search(r'/codesystem-([^/]+)\.html$', url)
            if match:
                return match.group(1)

        elif category == 'profile':
            # Extract profile name
            match = re.search(r'/(?:profile|structuredefinition)-([^/]+)\.html$', url)
            if match:
                return match.group(1)

        elif category == 'operation':
            # Extract operation name
            match = re.search(r'/operation-([^/]+)\.html$', url)
            if match:
                return match.group(1)

        return None

    def _categorize_by_metadata(self, result: Dict, metadata: Dict) -> Dict:
        """
        Try to categorize based on metadata when pattern matching fails

        Args:
            result: Current categorization result
            metadata: URL metadata

        Returns:
            Updated categorization result
        """
        title = str(metadata.get('title', '')).lower() if metadata.get('title') and str(metadata.get('title')) != 'nan' else ''
        description = str(metadata.get('description', '')).lower() if metadata.get('description') and str(metadata.get('description')) != 'nan' else ''
        keywords = str(metadata.get('keywords', '')).lower() if metadata.get('keywords') and str(metadata.get('keywords')) != 'nan' else ''

        combined_text = f"{title} {description} {keywords}"

        # Check for category keywords
        category_keywords = {
            'resource': ['resource', 'patient', 'observation', 'medication'],
            'module': ['module', 'group', 'category'],
            'valueset': ['value set', 'valueset', 'code list'],
            'codesystem': ['code system', 'codesystem', 'terminology'],
            'implementation': ['implementation', 'technical', 'specification'],
            'profile': ['profile', 'constraint', 'structure definition'],
            'example': ['example', 'sample', 'instance']
        }

        for cat, keywords in category_keywords.items():
            if any(kw in combined_text for kw in keywords):
                result['category'] = cat
                result['priority'] = self.categories.get(cat, {}).get('priority', 'low')
                result['depth_recommendation'] = self.categories.get(cat, {}).get('depth', 0)
                result['confidence'] = 0.6  # Lower confidence from metadata
                self.statistics[cat] += 1
                break

        return result

    def categorize_batch(self, urls_data: List[Dict]) -> List[Dict]:
        """
        Categorize a batch of URLs

        Args:
            urls_data: List of URL data dictionaries

        Returns:
            List of categorized URL dictionaries
        """
        categorized = []

        for url_data in urls_data:
            if isinstance(url_data, str):
                # Just a URL string
                url = url_data
                metadata = None
            else:
                # Dictionary with URL and metadata
                url = url_data.get('url', url_data)
                metadata = url_data

            result = self.categorize_url(url, metadata)

            # Merge with original data if dict
            if isinstance(url_data, dict):
                result.update(url_data)

            categorized.append(result)

        return categorized

    def get_statistics(self) -> Dict:
        """
        Get categorization statistics

        Returns:
            Statistics dictionary
        """
        total = sum(self.statistics.values())

        stats = {
            'total_urls': total,
            'categories': dict(self.statistics),
            'category_percentages': {},
            'subcategories': {},
            'top_subcategories': {}
        }

        # Calculate percentages
        if total > 0:
            for cat, count in self.statistics.items():
                stats['category_percentages'][cat] = round(count / total * 100, 1)

        # Add subcategory information
        for cat, subcats in self.subcategory_counts.items():
            stats['subcategories'][cat] = dict(subcats)

            # Top 5 subcategories
            if subcats:
                top_5 = sorted(subcats.items(), key=lambda x: x[1], reverse=True)[:5]
                stats['top_subcategories'][cat] = top_5

        return stats

    def print_statistics(self):
        """Print formatted statistics"""
        stats = self.get_statistics()

        print("\n" + "=" * 50)
        print("Categorization Statistics")
        print("=" * 50)
        print(f"Total URLs: {stats['total_urls']}")
        print("\nCategory Distribution:")
        print("-" * 30)

        # Sort categories by count
        sorted_cats = sorted(stats['categories'].items(), key=lambda x: x[1], reverse=True)

        for cat, count in sorted_cats:
            pct = stats['category_percentages'].get(cat, 0)
            desc = self.categories.get(cat, {}).get('description', '')
            print(f"{cat:20} {count:6} ({pct:5.1f}%) - {desc}")

        # Print top subcategories
        print("\nTop Subcategories by Category:")
        print("-" * 30)

        for cat, top_subcats in stats['top_subcategories'].items():
            if top_subcats:
                print(f"\n{cat}:")
                for subcat, count in top_subcats:
                    print(f"  - {subcat}: {count}")


def load_input_data(input_path: str) -> List[Dict]:
    """
    Load input data from CSV or JSON file

    Args:
        input_path: Path to input file

    Returns:
        List of URL data dictionaries
    """
    input_path = Path(input_path)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    logger.info(f"Loading input data from {input_path}")

    if input_path.suffix == '.csv':
        df = pd.read_csv(input_path)
        return df.to_dict('records')

    elif input_path.suffix == '.json':
        with open(input_path, 'r') as f:
            data = json.load(f)
            if isinstance(data, dict):
                # Handle results from pre_crawl_discovery.py
                if 'metadata' in data:
                    return data['metadata']
                elif 'urls' in data:
                    return [{'url': url} for url in data['urls']]
            return data

    else:
        raise ValueError(f"Unsupported input format: {input_path.suffix}")


def save_categorized_data(data: List[Dict], output_path: str, format: str = "csv"):
    """
    Save categorized data to file

    Args:
        data: Categorized data
        output_path: Output file path
        format: Output format (csv or json)
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if format == "csv":
        df = pd.DataFrame(data)

        # Reorder columns for better readability
        column_order = ['url', 'category', 'subcategory', 'priority', 'depth_recommendation', 'confidence']
        # Add other columns that might exist
        other_cols = [col for col in df.columns if col not in column_order]
        column_order.extend(other_cols)

        # Only include columns that exist
        column_order = [col for col in column_order if col in df.columns]

        df = df[column_order]
        df.to_csv(output_path, index=False)

    elif format == "json":
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=2)

    logger.info(f"Saved {len(data)} categorized URLs to {output_path}")


def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(description='FHIR R4 URL Categorizer')

    parser.add_argument('--input', required=True, help='Input CSV or JSON file')
    parser.add_argument('--output', default='outputs/categorized_urls.csv', help='Output file path')
    parser.add_argument('--format', default='csv', choices=['csv', 'json'], help='Output format')
    parser.add_argument('--stats', action='store_true', help='Print statistics')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')

    args = parser.parse_args()

    # Set logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    try:
        # Load input data
        input_data = load_input_data(args.input)
        logger.info(f"Loaded {len(input_data)} URLs from {args.input}")

        # Initialize categorizer
        categorizer = URLCategorizer()

        # Categorize URLs
        logger.info("Categorizing URLs...")
        categorized_data = categorizer.categorize_batch(input_data)

        # Print statistics if requested
        if args.stats:
            categorizer.print_statistics()

        # Save results
        save_categorized_data(categorized_data, args.output, args.format)

        # Print summary
        stats = categorizer.get_statistics()
        print(f"\nCategorization complete!")
        print(f"Total URLs processed: {stats['total_urls']}")
        print(f"Results saved to: {args.output}")

        # Print category summary
        print("\nCategory Summary:")
        for cat, count in sorted(stats['categories'].items(), key=lambda x: x[1], reverse=True):
            print(f"  {cat}: {count}")

    except Exception as e:
        logger.error(f"Categorization failed: {e}")
        raise


if __name__ == "__main__":
    main()