#!/usr/bin/env python3
"""
FHIR R4 URL Validator Script
Version: 1.0
Date: November 10, 2025
Author: Symphony Corp

Purpose: Validate and clean discovered URLs before filtering
"""

import argparse
import logging
import re
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple
from urllib.parse import urlparse, urlunparse

import pandas as pd
import requests

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class URLValidator:
    """
    Validates and cleans FHIR URLs:
    - Valid HTTP/HTTPS scheme
    - HL7 domain only
    - R4 version enforcement
    - Deduplication
    - Optional accessibility check
    """

    def __init__(self,
                 strict_r4: bool = True,
                 allow_other_domains: bool = False,
                 check_accessibility: bool = False,
                 accessibility_timeout: int = 5):
        """
        Initialize validator

        Args:
            strict_r4: Enforce R4-only (exclude other versions)
            allow_other_domains: Allow non-HL7 domains
            check_accessibility: Perform HTTP HEAD check
            accessibility_timeout: Timeout for HEAD requests (seconds)
        """
        self.strict_r4 = strict_r4
        self.allow_other_domains = allow_other_domains
        self.check_accessibility = check_accessibility
        self.accessibility_timeout = accessibility_timeout

        # Statistics
        self.stats = {
            'processed': 0,
            'valid': 0,
            'invalid': 0,
            'rejection_reasons': Counter(),
            'version_distribution_excluded': Counter(),
            'invalid_examples': []
        }

        # Configure logging
        log_file = f'logs/url_validator_{datetime.now():%Y%m%d_%H%M%S}.log'
        Path('logs').mkdir(exist_ok=True)
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        logger.addHandler(file_handler)

        logger.info("Initialized URLValidator")
        logger.info(f"  strict_r4: {strict_r4}")
        logger.info(f"  allow_other_domains: {allow_other_domains}")
        logger.info(f"  check_accessibility: {check_accessibility}")

    def validate_url(self, url: str) -> Tuple[bool, str]:
        """
        Validate a single URL

        Args:
            url: URL to validate

        Returns:
            (is_valid, rejection_reason)
        """
        # Parse URL
        try:
            parsed = urlparse(url)
        except Exception as e:
            return False, f"Invalid URL format: {str(e)[:50]}"

        # Check scheme
        if parsed.scheme not in ['http', 'https']:
            return False, f"Invalid scheme: {parsed.scheme}"

        # Check domain
        if not self.allow_other_domains:
            if 'hl7.org' not in parsed.netloc:
                return False, f"Non-HL7 domain: {parsed.netloc}"

        # Check R4 if strict
        if self.strict_r4:
            path_lower = parsed.path.lower()

            # Must contain R4 or known IG paths
            has_r4 = '/r4/' in path_lower
            has_ig_path = any(ig in path_lower for ig in ['/us/', '/uv/', '/ig/'])

            if not (has_r4 or has_ig_path):
                return False, "Missing R4 in path"

            # Exclude other versions
            version_match = re.search(r'/(r5|r4b|dstu2?|stu3)/', path_lower)
            if version_match:
                version = version_match.group(1).upper()
                self.stats['version_distribution_excluded'][version] += 1
                return False, f"Non-R4 version: {version}"

        # Optional accessibility check
        if self.check_accessibility:
            try:
                response = requests.head(url, timeout=self.accessibility_timeout, allow_redirects=True)
                if response.status_code != 200:
                    return False, f"Not accessible: HTTP {response.status_code}"
            except requests.Timeout:
                return False, "Timeout during HEAD request"
            except requests.RequestException as e:
                return False, f"Request error: {str(e)[:50]}"

        return True, ""

    def canonicalize_url(self, url: str) -> str:
        """
        Canonicalize URL (strip fragments and query params)

        Args:
            url: URL to canonicalize

        Returns:
            Canonical URL
        """
        parsed = urlparse(url)
        canonical = urlunparse((
            parsed.scheme,
            parsed.netloc,
            parsed.path,
            '', '', ''  # params, query, fragment
        ))
        return canonical

    def validate_batch(self, urls_data: List[Dict]) -> List[Dict]:
        """
        Validate a batch of URLs

        Args:
            urls_data: List of URL dictionaries

        Returns:
            List of valid URL dictionaries
        """
        logger.info(f"Validating {len(urls_data)} URLs...")

        valid_urls = []
        seen_canonical = set()
        duplicates = 0

        for url_data in urls_data:
            self.stats['processed'] += 1

            # Get URL
            if isinstance(url_data, str):
                url = url_data
                url_dict = {'url': url}
            else:
                url = url_data.get('url', '')
                url_dict = url_data.copy()

            # Validate
            is_valid, reason = self.validate_url(url)

            if not is_valid:
                self.stats['invalid'] += 1
                self.stats['rejection_reasons'][reason] += 1

                # Store example if we don't have many yet
                if len(self.stats['invalid_examples']) < 100:
                    self.stats['invalid_examples'].append({
                        'url': url[:120],
                        'reason': reason
                    })

                logger.debug(f"Rejected: {url[:60]} - {reason}")
                continue

            # Canonicalize and check for duplicates
            canonical = self.canonicalize_url(url)

            if canonical in seen_canonical:
                duplicates += 1
                self.stats['rejection_reasons']['Duplicate'] += 1
                logger.debug(f"Duplicate: {url[:60]}")
                continue

            seen_canonical.add(canonical)

            # Valid!
            self.stats['valid'] += 1
            valid_urls.append(url_dict)

        self.stats['invalid'] += duplicates

        logger.info(f"Validation complete: {self.stats['valid']} valid, "
                   f"{self.stats['invalid']} invalid ({duplicates} duplicates)")

        return valid_urls

    def generate_report(self) -> str:
        """
        Generate Markdown validation report

        Returns:
            Markdown string
        """
        total = self.stats['processed']
        valid = self.stats['valid']
        invalid = self.stats['invalid']

        valid_pct = (valid / total * 100) if total > 0 else 0
        invalid_pct = (invalid / total * 100) if total > 0 else 0

        md_lines = [
            "# URL Validation Report",
            "",
            "## Summary",
            f"- **Processed**: {total:,} URLs",
            f"- **Valid**: {valid:,} URLs ({valid_pct:.1f}%)",
            f"- **Invalid**: {invalid:,} URLs ({invalid_pct:.1f}%)",
            ""
        ]

        # Rejection reasons
        if self.stats['rejection_reasons']:
            md_lines.extend([
                "## Rejection Reasons",
                "| Reason | Count | Percentage |",
                "|--------|-------|------------|"
            ])

            sorted_reasons = sorted(self.stats['rejection_reasons'].items(),
                                   key=lambda x: x[1], reverse=True)

            for reason, count in sorted_reasons:
                pct = (count / total * 100) if total > 0 else 0
                md_lines.append(f"| {reason} | {count:,} | {pct:.2f}% |")

            md_lines.append("")

        # Version distribution (excluded)
        if self.stats['version_distribution_excluded']:
            md_lines.extend([
                "## Version Distribution (Excluded)",
                "| Version | Count |",
                "|---------|-------|"
            ])

            sorted_versions = sorted(self.stats['version_distribution_excluded'].items(),
                                    key=lambda x: x[1], reverse=True)

            for version, count in sorted_versions:
                md_lines.append(f"| {version} | {count:,} |")

            md_lines.append("")

        # Sample invalid URLs
        if self.stats['invalid_examples']:
            md_lines.extend([
                "## Sample Invalid URLs",
                "(Top 50 shown)",
                ""
            ])

            for i, example in enumerate(self.stats['invalid_examples'][:50], 1):
                md_lines.append(f"{i}. `{example['url']}` - {example['reason']}")

            md_lines.append("")

        # Validation settings
        md_lines.extend([
            "## Validation Settings",
            f"- **Strict R4**: {self.strict_r4}",
            f"- **Allow Other Domains**: {self.allow_other_domains}",
            f"- **Check Accessibility**: {self.check_accessibility}",
            ""
        ])

        # Timestamp
        md_lines.extend([
            "## Validation Timestamp",
            datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC"),
            ""
        ])

        return "\n".join(md_lines)


def load_url_data(input_path: Path) -> List[Dict]:
    """
    Load URL data from CSV

    Args:
        input_path: Path to input CSV

    Returns:
        List of URL dictionaries
    """
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    logger.info(f"Loading URLs from {input_path}")

    df = pd.read_csv(input_path)
    df = df.fillna('')

    urls_data = df.to_dict('records')

    logger.info(f"Loaded {len(urls_data)} URLs")

    return urls_data


def save_validated_data(urls_data: List[Dict], output_path: Path):
    """
    Save validated URLs to CSV

    Args:
        urls_data: List of valid URL dictionaries
        output_path: Output file path
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame(urls_data)
    df.to_csv(output_path, index=False)

    logger.info(f"Saved {len(urls_data)} validated URLs to {output_path}")


def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(description='FHIR R4 URL Validator')

    parser.add_argument('input', type=Path, help='Input CSV file with URLs')
    parser.add_argument('-o', '--output', type=Path, required=True, help='Output validated CSV file')
    parser.add_argument('--report', type=Path, help='Generate Markdown validation report')
    parser.add_argument('--strict-r4', action='store_true', default=True,
                       help='Enforce R4-only (exclude R5, R4B, DSTU, STU3)')
    parser.add_argument('--no-strict-r4', action='store_false', dest='strict_r4',
                       help='Allow non-R4 versions')
    parser.add_argument('--allow-other-domains', action='store_true',
                       help='Allow non-HL7 domains')
    parser.add_argument('--check-accessibility', action='store_true',
                       help='Perform HTTP HEAD check for accessibility')
    parser.add_argument('--accessibility-timeout', type=int, default=5,
                       help='Timeout for HEAD requests (seconds)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose logging')

    args = parser.parse_args()

    # Set logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    try:
        # Load input data
        urls_data = load_url_data(args.input)

        # Initialize validator
        validator = URLValidator(
            strict_r4=args.strict_r4,
            allow_other_domains=args.allow_other_domains,
            check_accessibility=args.check_accessibility,
            accessibility_timeout=args.accessibility_timeout
        )

        # Validate URLs
        valid_urls = validator.validate_batch(urls_data)

        # Save results
        save_validated_data(valid_urls, args.output)

        # Generate report if requested
        if args.report:
            report = validator.generate_report()

            args.report.parent.mkdir(parents=True, exist_ok=True)
            with open(args.report, 'w') as f:
                f.write(report)

            logger.info(f"Report saved to {args.report}")

        # Print summary
        print("\n" + "=" * 60)
        print("URL VALIDATION SUMMARY")
        print("=" * 60)
        print(f"Processed: {validator.stats['processed']:,}")
        print(f"Valid: {validator.stats['valid']:,} ({validator.stats['valid']/validator.stats['processed']*100:.1f}%)")
        print(f"Invalid: {validator.stats['invalid']:,} ({validator.stats['invalid']/validator.stats['processed']*100:.1f}%)")

        if validator.stats['rejection_reasons']:
            print(f"\nTop Rejection Reasons:")
            for reason, count in list(validator.stats['rejection_reasons'].most_common(5)):
                print(f"  {reason}: {count:,}")

        print(f"\n✅ Validation complete! {len(valid_urls)} valid URLs saved to {args.output}")
        if args.report:
            print(f"Report: {args.report}")

    except Exception as e:
        logger.error(f"Validation failed: {e}")
        raise


if __name__ == "__main__":
    main()
