# Examples

These examples are used to support tutorial blog posts as follows:

## Convert a PDF to Markdown

Install PyMuPDF4LLM, then run the converter with a PDF file:

```bash
python -m pip install pymupdf4llm
python examples/convert_pdf_to_markdown.py document.pdf
```

This creates `document.md` next to the PDF, saves extracted pictures as PNG
files in an `img` folder next to the Markdown file, and adds image links to the
Markdown automatically. To choose a different output filename, pass
`--output`, for example:

```bash
python examples/convert_pdf_to_markdown.py document.pdf --output notes.md
```

The script uses `pymupdf4llm.to_markdown()` to extract the PDF's content and
write it as UTF-8 Markdown.

## country-capitals

See: [Creating a RAG Chatbot with ChatGPT and PyMuPDF](https://artifex.com/blog/creating-a-rag-chatbot-with-chatgpt-and-pymupdf)



## GUI

See: [Building a RAG Chatbot GUI with the ChatGPT API and PyMuPDF](https://artifex.com/blog/building-a-rag-chatbot-gui-with-the-chatgpt-api-and-pymupdf)
