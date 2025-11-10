#!/usr/bin/env python3
"""Rebuild FHIR R4 markdown outputs from the downloaded local HTML mirror."""

import asyncio
from dataclasses import dataclass
from pathlib import Path
from typing import List

import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.utils import ensure_directory

try:
    from crawl4ai import AsyncWebCrawler, CrawlerRunConfig
except ImportError as exc:  # pragma: no cover
    raise SystemExit("crawl4ai must be installed to rebuild markdown: pip install crawl4ai") from exc


@dataclass
class TargetPage:
    name: str
    url: str
    relative_path: str
    source_md: Path


def parse_targets(markdown_dir: Path) -> List[TargetPage]:
    targets: List[TargetPage] = []

    for md_file in sorted(markdown_dir.glob('*.md')):
        with md_file.open('r', encoding='utf-8') as handle:
            url_line = next((line.strip() for line in handle if line.startswith('url:')), None)

        if not url_line:
            print(f"⚠️  Skipping {md_file.name}: missing url frontmatter")
            continue

        url = url_line.split('url: ', 1)[1].strip()
        if '/R4/' not in url:
            print(f"⚠️  Skipping {md_file.name}: url not in R4 scope -> {url}")
            continue

        relative = url.split('/R4/', 1)[1]
        targets.append(TargetPage(name=md_file.name, url=url, relative_path=relative, source_md=md_file))

    return targets


async def rebuild_from_local(html_root: Path, targets: List[TargetPage], output_dir: Path) -> None:
    ensure_directory(str(output_dir))

    config = CrawlerRunConfig(word_count_threshold=50, verbose=False)

    missing = []
    failures = []

    async with AsyncWebCrawler() as crawler:
        for target in targets:
            local_html = html_root / target.relative_path

            if not local_html.exists():
                missing.append(target)
                print(f"❌ Missing local HTML for {target.relative_path} (source {target.name})")
                continue

            file_url = local_html.absolute().as_uri()
            print(f"Processing {target.relative_path} -> {target.name}")

            try:
                result = await crawler.arun(file_url, config=config)
            except Exception as exc:  # pragma: no cover
                failures.append((target, str(exc)))
                print(f"❌ Error converting {target.relative_path}: {exc}")
                continue

            if not result:
                failures.append((target, 'empty result set'))
                print(f"❌ Empty markdown generated for {target.relative_path}")
                continue

            doc = result[0]
            title = getattr(doc, 'title', None) or target.relative_path
            markdown = getattr(doc, 'markdown', None)

            if not markdown:
                failures.append((target, 'missing markdown attribute'))
                print(f"❌ No markdown content for {target.relative_path}")
                continue

            header = """---\nurl: {url}\ntitle: {title}\nsource: official_download\nextracted: local_file_conversion\nmirror_path: {relative}\n---\n\n""".format(
                url=target.url,
                title=title.strip(),
                relative=target.relative_path
            )

            output_path = output_dir / target.name
            output_path.write_text(header + markdown, encoding='utf-8')
            print(f"✓ Saved {output_path}")

    if missing:
        print("\nMissing HTML files:")
        for target in missing:
            print(f"  - {target.relative_path} (from {target.name})")

    if failures:
        print("\nConversion failures:")
        for target, reason in failures:
            print(f"  - {target.relative_path}: {reason}")

    if not missing and not failures:
        print("\n✅ Rebuild complete without errors")


def main() -> None:
    html_dir = Path('downloads/site')
    source_markdown_dir = Path('03_OUTPUTS_COMPLETE/markdown')
    output_dir = Path('03_OUTPUTS_COMPLETE/markdown_rebuilt')

    if not html_dir.exists():
        raise SystemExit("Downloaded spec not found. Expected directory: downloads/site")

    targets = parse_targets(source_markdown_dir)
    if not targets:
        raise SystemExit("No markdown files found to rebuild")

    print(f"Found {len(targets)} markdown files to rebuild")
    asyncio.run(rebuild_from_local(html_dir, targets, output_dir))


if __name__ == '__main__':
    main()
