#!/usr/bin/env python3
"""
Simple JSON to CSV parser for Crawl4AI output
This is a standalone version for reference in CONFIG/
The main implementation is in src/inventory_builder.py
"""

import csv
import json
import sys
from pathlib import Path


def parse_json_to_csv(json_file, csv_file):
    """Parse Crawl4AI JSON output to CSV"""

    # Load JSON
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Handle different formats
    if isinstance(data, list):
        pages = data
    elif isinstance(data, dict) and 'results' in data:
        pages = data['results']
    elif isinstance(data, dict) and 'pages' in data:
        pages = data['pages']
    else:
        pages = [data]

    # Write CSV
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['url', 'depth', 'status', 'content_type', 'parent', 'first_seen']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for page in pages:
            writer.writerow({
                'url': page.get('url', ''),
                'depth': str(page.get('depth', 0)),
                'status': str(page.get('status_code', page.get('status', 'unknown'))),
                'content_type': page.get('content_type', page.get('headers', {}).get('content-type', 'unknown')),
                'parent': page.get('parent_url', page.get('parent', '')),
                'first_seen': page.get('timestamp', ''),
            })

    print(f"✓ Parsed {len(pages)} pages to {csv_file}")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python json_to_csv.py <input.json> <output.csv>")
        sys.exit(1)

    parse_json_to_csv(sys.argv[1], sys.argv[2])
