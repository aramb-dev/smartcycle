# SmartCycle Book — Build & Deploy

This site is built with MyST Markdown and Jupyter Book.

## Build locally

```bash
# Create/activate your Python environment first
pip install -r ../requirements.txt
jupyter-book build .
open _build/html/index.html
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
