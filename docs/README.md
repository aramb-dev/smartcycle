# SmartCycle Book — Build & Deploy

This site is built with MyST Markdown and Jupyter Book.

## Build locally

```bash
# Create/activate your Python environment first
pip install -r ../requirements.txt
jupyter-book build . --path-output ..
open ../_build/html/index.html
```

## Deploy to GitHub Pages

- Configure Pages to serve from `gh-pages` or `docs/_build/html`.
- Manual: push `_build/html` to `gh-pages`.
- Actions: add a workflow to build and deploy automatically.

## Structure

- Config: `_config.yml`
- ToC: `_toc.yml`
- Entry: `index.md`
- Modules: `modules/*.md` (include files from `../module*/`)

## Build a PDF with Typst

Typst provides fast, high-quality PDF output.

### Install Typst (macOS)

```bash
brew install typst
```

### Compile the PDF

```bash
cd ..
typst compile --root . docs/typst/book.typ book.pdf
open book.pdf
```

The Typst sources live in `typst/` and use `--root` to access repository files.
