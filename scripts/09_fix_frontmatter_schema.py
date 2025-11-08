#!/usr/bin/env python3
"""
Fix frontmatter schema mismatch in markdown files.
Changes 'crawled' and 'depth' to 'source' and 'extracted' for consistency.
"""

import re
from pathlib import Path

def fix_frontmatter(file_path: Path):
    """Fix frontmatter schema in a single file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if this is a web-crawl file (has 'crawled' field)
    if 'crawled:' not in content:
        return False  # Already has correct schema or is shortlist file

    # Replace frontmatter fields
    # crawled: unknown -> source: web_crawl
    # depth: 0 -> extracted: web_crawler_run
    content = re.sub(r'crawled: unknown', 'source: web_crawl', content)
    content = re.sub(r'depth: (\d+)', 'extracted: crawl4ai_web_crawler', content)

    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

def main():
    markdown_dir = Path('03_OUTPUTS_COMPLETE/markdown')
    fixed_count = 0

    for md_file in markdown_dir.glob('*.md'):
        if fix_frontmatter(md_file):
            fixed_count += 1
            print(f"✓ Fixed: {md_file.name}")

    print(f"\nTotal files fixed: {fixed_count}")

if __name__ == '__main__':
    main()
