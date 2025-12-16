# Typst PDF Build

This directory contains a Typst project to generate a consolidated PDF book.

## Prerequisites (macOS)

- Install Typst:

```bash
brew install typst
```

- First run may fetch the `@preview/markdown` package automatically.

## Build the PDF

```bash
cd ../..
typst compile --root . docs/typst/book.typ book.pdf
open book.pdf
```

## Notes

- The Typst project uses `--root` to access files across the repository.
- File paths in `book.typ` are relative to the repository root.
- Markdown and code files are included as syntax-highlighted raw blocks.
- Excalidraw diagrams cannot be rendered; they are referenced as external files.
