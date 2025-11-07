"""
PDF Generator for FHIR R4 Documentation
Adapted from generate_markdown_pdf.py with FHIR-specific styling
"""

import logging
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Optional, Tuple, List

try:
    import markdown
except ImportError:
    raise ImportError("Missing dependency 'markdown'. Install: pip install markdown")

try:
    from weasyprint import HTML
except ImportError:
    raise ImportError("Missing dependency 'weasyprint'. Install: pip install weasyprint")

from src.utils import ensure_directory

logger = logging.getLogger(__name__)

# FHIR-themed CSS
FHIR_THEME_CSS = """
@page {
    size: A4;
    margin: 2.4cm 2.2cm 2.6cm 2.2cm;
    @top-center {
        content: string(doc_title);
        font-family: 'Manrope', 'Inter', sans-serif;
        font-weight: 600;
        font-size: 10pt;
        color: #7b8794;
        letter-spacing: 0.08em;
    }
    @bottom-left {
        content: string(running_header);
        font-family: 'Manrope', 'Inter', sans-serif;
        font-size: 8.5pt;
        color: #98a4b5;
    }
    @bottom-right {
        content: "Page " counter(page) " of " counter(pages);
        font-family: 'Manrope', 'Inter', sans-serif;
        font-size: 8.5pt;
        color: #98a4b5;
    }
}

@page:first {
    margin: 0;
    @top-center { content: normal; }
    @bottom-left { content: normal; }
    @bottom-right { content: normal; }
}

@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700&family=Merriweather:wght@300;400;700&family=Fira+Code:wght@400;500;600&display=swap');

:root {
    --fhir-blue: #005a9c;
    --fhir-light-blue: #4b8fe2;
    --accent-primary: #005a9c;
    --accent-secondary: #4b8fe2;
    --text-primary: #24324a;
    --text-secondary: #4b5563;
    --border-soft: #e3e8f2;
    --surface-soft: #eef1f8;
}

body {
    margin: 0;
    padding: 0;
    font-family: 'Merriweather', Georgia, serif;
    color: var(--text-primary);
    background: #ffffff;
    line-height: 1.65;
    font-size: 11pt;
}

.cover-page {
    min-height: 100vh;
    box-sizing: border-box;
    padding: 3.6cm 3.2cm 3cm;
    background: linear-gradient(130deg, rgba(0,90,156,0.92) 0%, rgba(75,143,226,0.85) 100%);
    color: #ffffff;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.cover-kicker {
    font-family: 'Manrope', 'Inter', sans-serif;
    font-size: 11pt;
    font-weight: 600;
    letter-spacing: 0.4em;
    text-transform: uppercase;
    margin-bottom: 24px;
    opacity: 0.8;
}

.cover-page h1 {
    font-family: 'Manrope', 'Inter', sans-serif;
    font-size: 48pt;
    font-weight: 700;
    line-height: 1.12;
    margin: 0 0 30px;
    string-set: doc_title content();
}

.cover-page h2 {
    font-family: 'Manrope', 'Inter', sans-serif;
    font-size: 18pt;
    font-weight: 400;
    margin: 0 0 36px;
    opacity: 0.9;
}

.cover-meta {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: 16px;
    max-width: 80%;
    margin-top: 32px;
}

.cover-meta-item {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    padding: 16px 18px;
    backdrop-filter: blur(6px);
}

.cover-meta-label {
    font-family: 'Manrope', 'Inter', sans-serif;
    font-size: 9pt;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    opacity: 0.75;
}

.cover-meta-value {
    font-family: 'Manrope', 'Inter', sans-serif;
    font-size: 12pt;
    font-weight: 600;
    margin-top: 6px;
}

.page-break { page-break-after: always; }

.page {
    background: #ffffff;
    padding: 2cm 2.2cm;
}

main.content h1,
main.content h2,
main.content h3,
main.content h4 {
    font-family: 'Manrope', 'Inter', sans-serif;
    font-weight: 700;
    color: var(--fhir-blue);
    margin-top: 32px;
    margin-bottom: 14px;
    page-break-after: avoid;
}

main.content h1 { font-size: 26pt; }
main.content h2 { font-size: 20pt; string-set: running_header content(); }
main.content h3 { font-size: 15pt; color: #3f4d6b; }
main.content h4 { font-size: 13pt; color: #44546f; }

main.content p, main.content li {
    color: var(--text-secondary);
    font-size: 11pt;
    letter-spacing: 0.01em;
}

main.content ul, main.content ol {
    padding-left: 18px;
    margin: 12px 0 18px;
}

main.content blockquote {
    border-left: 4px solid var(--fhir-light-blue);
    background: var(--surface-soft);
    margin: 20px 0;
    padding: 16px 20px;
    font-style: italic;
    color: #3e4c66;
    border-radius: 10px;
}

main.content pre, main.content code {
    font-family: 'Fira Code', 'SFMono-Regular', Consolas, monospace;
    font-size: 9.5pt;
}

main.content pre {
    background: #0f172a;
    color: #f8fafc;
    padding: 16px 20px;
    border-radius: 10px;
    overflow-x: auto;
    margin: 20px 0;
}

main.content code {
    background: rgba(0, 90, 156, 0.1);
    color: #003d6b;
    padding: 2px 6px;
    border-radius: 4px;
}

main.content table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    font-size: 10pt;
    background: #ffffff;
    border: 1px solid var(--border-soft);
    border-radius: 10px;
    overflow: hidden;
}

main.content table thead tr {
    background: linear-gradient(120deg, rgba(0,90,156,0.95), rgba(75,143,226,0.9));
    color: #ffffff;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    font-family: 'Manrope', 'Inter', sans-serif;
    font-weight: 600;
}

main.content th, main.content td {
    padding: 10px 12px;
    border-bottom: 1px solid var(--border-soft);
    text-align: left;
}

main.content tbody tr:nth-child(odd) {
    background: #f9fafc;
}

.toc-wrapper {
    background: #ffffff;
    border-radius: 16px;
    padding: 24px 28px;
    box-shadow: 0 16px 50px rgba(0, 90, 156, 0.1);
}

.toc-wrapper h2 {
    margin-top: 0;
    font-family: 'Manrope', 'Inter', sans-serif;
    font-size: 20pt;
    color: var(--fhir-blue);
}

.toc-wrapper ul {
    list-style: none;
    padding-left: 0;
    margin: 0;
}

.toc-wrapper li {
    font-family: 'Manrope', 'Inter', sans-serif;
    margin: 8px 0;
    font-size: 10.5pt;
    color: #43526f;
}

.toc-wrapper a {
    color: inherit;
    text-decoration: none;
}

.toc-wrapper li::before {
    content: '•';
    color: var(--fhir-light-blue);
    font-weight: 700;
    display: inline-block;
    width: 16px;
}

hr {
    border: none;
    height: 6px;
    width: 100px;
    background: linear-gradient(90deg, var(--fhir-blue), rgba(0,90,156,0));
    margin: 32px auto;
    border-radius: 999px;
}
"""


@dataclass
class DocumentMetadata:
    """Document metadata"""
    title: str
    subtitle: Optional[str] = None
    date: Optional[str] = None
    version: Optional[str] = None
    project: Optional[str] = None


class PDFGenerator:
    """Generate beautiful PDFs from markdown"""

    def __init__(self, output_dir: str = "docs"):
        """
        Initialize PDF generator

        Args:
            output_dir: Directory to save PDFs
        """
        self.output_dir = output_dir
        ensure_directory(output_dir)

    def _escape_html(self, text: str) -> str:
        """Escape HTML special characters"""
        return (
            text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&#39;")
        )

    def _build_cover_html(self, meta: DocumentMetadata) -> str:
        """Build cover page HTML"""
        meta_items = []

        if meta.project:
            meta_items.append(self._cover_meta_item("Project", meta.project))

        if meta.version:
            meta_items.append(self._cover_meta_item("Version", meta.version))

        if meta.date:
            meta_items.append(self._cover_meta_item("Generated", meta.date))
        else:
            meta_items.append(
                self._cover_meta_item("Generated", datetime.now().strftime("%B %d, %Y"))
            )

        cover_parts = [
            "<section class='cover-page'>",
            "<div class='cover-kicker'>FHIR R4 Documentation</div>",
            f"<h1>{self._escape_html(meta.title)}</h1>",
        ]

        if meta.subtitle:
            cover_parts.append(f"<h2>{self._escape_html(meta.subtitle)}</h2>")

        if meta_items:
            cover_parts.append("<div class='cover-meta'>" + "".join(meta_items) + "</div>")

        cover_parts.extend(["</section>", "<div class='page-break'></div>"])
        return "".join(cover_parts)

    def _cover_meta_item(self, label: str, value: str) -> str:
        """Build cover metadata item"""
        return (
            "<div class='cover-meta-item'>"
            f"<div class='cover-meta-label'>{self._escape_html(label)}</div>"
            f"<div class='cover-meta-value'>{self._escape_html(value)}</div>"
            "</div>"
        )

    def _convert_markdown_to_html(
        self, markdown_text: str, enable_toc: bool = True
    ) -> Tuple[str, str]:
        """Convert markdown to HTML"""
        extensions = [
            "extra",
            "codehilite",
            "sane_lists",
            "tables",
        ]

        if enable_toc:
            extensions.append("toc")

        md = markdown.Markdown(
            extensions=extensions,
            extension_configs={
                "codehilite": {"guess_lang": False, "pygments_style": "monokai"},
                "toc": {"permalink": "#", "baselevel": 2},
            },
            output_format="xhtml1",
        )

        body_html = md.convert(markdown_text)
        toc_html = md.toc if enable_toc and hasattr(md, 'toc') else ""
        return body_html, toc_html

    def _build_toc_html(self, raw_toc: str) -> Optional[str]:
        """Build table of contents HTML"""
        if not raw_toc or "<li" not in raw_toc:
            return None

        return (
            "<section class='page'>"
            "<div class='toc-wrapper'>"
            "<h2>Table of Contents</h2>"
            f"{raw_toc}"
            "</div>"
            "</section>"
            "<div class='page-break'></div>"
        )

    def _compose_document(
        self, meta: DocumentMetadata, body_html: str, toc_html: Optional[str]
    ) -> str:
        """Compose complete HTML document"""
        parts = [
            "<!DOCTYPE html>",
            "<html lang='en'>",
            "<head>",
            "    <meta charset='utf-8'>",
            f"    <title>{self._escape_html(meta.title)}</title>",
            "    <style>" + FHIR_THEME_CSS + "</style>",
            "</head>",
            "<body>",
            self._build_cover_html(meta),
        ]

        if toc_html:
            parts.append(toc_html)

        parts.append("<section class='page'><main class='content'>")
        parts.append(body_html)
        parts.append("</main></section>")
        parts.append("</body></html>")
        return "".join(parts)

    def generate_pdf(
        self,
        markdown_file: str,
        output_name: Optional[str] = None,
        metadata: Optional[DocumentMetadata] = None,
        save_html: bool = False,
    ) -> str:
        """
        Generate PDF from markdown file

        Args:
            markdown_file: Path to markdown file
            output_name: Optional output filename (without extension)
            metadata: Optional document metadata
            save_html: Whether to save intermediate HTML

        Returns:
            Path to generated PDF
        """
        logger.info(f"Generating PDF from {markdown_file}")

        # Read markdown
        markdown_path = Path(markdown_file)
        if not markdown_path.exists():
            raise FileNotFoundError(f"Markdown file not found: {markdown_file}")

        markdown_text = markdown_path.read_text(encoding="utf-8")

        # Strip YAML front matter if present
        front_matter_pattern = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)
        markdown_text = front_matter_pattern.sub("", markdown_text)

        # Create default metadata if not provided
        if metadata is None:
            metadata = DocumentMetadata(
                title=markdown_path.stem.replace("_", " ").replace("-", " ").title(),
                project="FHIR R4 Crawler",
                version="1.0.0",
            )

        # Convert markdown to HTML
        body_html, toc_html_raw = self._convert_markdown_to_html(markdown_text)
        toc_html = self._build_toc_html(toc_html_raw)

        # Compose document
        composed_html = self._compose_document(metadata, body_html, toc_html)

        # Determine output paths
        if output_name:
            pdf_name = output_name if output_name.endswith(".pdf") else f"{output_name}.pdf"
        else:
            pdf_name = f"{markdown_path.stem}.pdf"

        pdf_path = Path(self.output_dir) / pdf_name
        html_path = pdf_path.with_suffix(".html")

        # Generate PDF
        logger.info(f"Writing PDF to {pdf_path}")
        HTML(string=composed_html, base_url=str(markdown_path.parent)).write_pdf(str(pdf_path))

        # Optionally save HTML
        if save_html:
            logger.info(f"Saving HTML preview to {html_path}")
            html_path.write_text(composed_html, encoding="utf-8")

        logger.info(f"✓ PDF generated: {pdf_path}")
        return str(pdf_path)


def main():
    """Main entry point for CLI usage"""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m src.pdf_generator <markdown_file> [output_name]")
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_name = sys.argv[2] if len(sys.argv) > 2 else None

    generator = PDFGenerator()
    pdf_path = generator.generate_pdf(markdown_file, output_name, save_html=True)

    print(f"\n✓ PDF generated successfully!")
    print(f"  {pdf_path}")


if __name__ == "__main__":
    main()
