"""Convert a PDF to a Markdown file.

Usage:
    python convert_pdf_to_markdown.py document.pdf
    python convert_pdf_to_markdown.py document.pdf --output notes.md

Extracted images are saved in an ``img`` folder next to the Markdown file.
"""

import argparse
import os
from pathlib import Path

import pymupdf4llm


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert a PDF to Markdown.")
    parser.add_argument("pdf", type=Path, help="PDF file to convert")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Markdown output file (defaults to the PDF name with a .md extension)",
    )
    args = parser.parse_args()

    pdf_path = args.pdf.resolve()
    if not pdf_path.is_file():
        parser.error(f"PDF file not found: {pdf_path}")

    output_path = (args.output or args.pdf.with_suffix(".md")).resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    current_dir = Path.cwd()
    try:
        os.chdir(output_path.parent)
        markdown = pymupdf4llm.to_markdown(
            str(pdf_path),
            write_images=True,
            image_path="img",
            image_format="png",
        )
    finally:
        os.chdir(current_dir)

    output_path.write_text(markdown, encoding="utf-8")
    print(f"Markdown saved to: {output_path}")
    print(f"Extracted images saved to: {output_path.parent / 'img'}")


if __name__ == "__main__":
    main()
