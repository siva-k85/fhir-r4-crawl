#!/usr/bin/env python3
"""
Extract clean markdown using Crawl4AI Python API
"""

import asyncio
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.markdown_extractor import MarkdownExtractor


async def main():
    """Extract markdown from shortlist"""
    print("═══════════════════════════════════════════════")
    print("  Step 4: Markdown Extraction")
    print("═══════════════════════════════════════════════")
    print("")

    # Check shortlist exists
    shortlist_file = "shortlist/urls.txt"
    if not Path(shortlist_file).exists():
        print(f"❌ Shortlist not found: {shortlist_file}")
        print("   Please run: python scripts/03_create_shortlist.py")
        sys.exit(1)

    # Create extractor
    extractor = MarkdownExtractor(
        output_dir="extracted/markdown",
        max_depth=1,
        max_pages=50,
        word_threshold=50
    )

    print("→ Extracting markdown from shortlist...")
    print("  Max depth: 1 (include immediate child links)")
    print("  Max pages: 50 per seed URL")
    print("  Word threshold: 50")
    print("")
    print("  This may take 5-10 minutes depending on network speed...")
    print("")

    # Extract
    results = await extractor.extract_from_shortlist(shortlist_file)

    # Summary
    print("")
    print("═══════════════════════════════════════════════")
    print("  ✅ Extraction complete!")
    print("═══════════════════════════════════════════════")
    print("")
    print("Results:")
    print(f"  • Seed URLs processed: {results['successful']}/{results['total_urls']}")
    print(f"  • Total pages extracted: {results['total_pages']}")
    print(f"  • Markdown files saved: {len(results['files_saved'])}")
    print("")
    print("Output:")
    print("  • extracted/markdown/*.md")
    print("")
    print("Next step:")
    print("  python scripts/05_generate_docs_and_pdfs.py")
    print("")


if __name__ == "__main__":
    asyncio.run(main())
