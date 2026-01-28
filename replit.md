# 閱讀古文 (Reading Classical Chinese)

A Jekyll-based website for reading and studying classical Chinese texts.

## Overview

This site uses the Jekyll static site generator with the minimal theme. It includes custom components for educational content.

## Project Structure

```
├── _config.yml          # Jekyll configuration
├── _layouts/            # Page layouts
│   └── default.html     # Main layout
├── _includes/           # Reusable components
│   ├── fn.html          # Footnote marker (simple inline tag)
│   ├── annotated_text.html  # Full annotated text container
│   └── connection_diagram.html # Word connection diagram
├── _sass/               # SCSS stylesheets
│   ├── jekyll-theme-minimal.scss
│   ├── _annotated.scss  # Styles for annotated text
│   └── _connections.scss # Styles for connection diagrams
├── assets/
│   ├── css/style.scss   # Main stylesheet
│   └── js/
│       └── connection-diagram.js # Connection diagram logic
├── pages/               # Site pages
│   └── demo.md          # Feature demo page
└── index.md             # Homepage
```

## Custom Features

### 1. Annotated Text with Auto-Numbered Footnotes

Add footnotes with **automatic numbering** by label type. Just specify the label (like "注", "解讀", "脂批") and the system adds the number for you:

```liquid
{% capture main_text %}
<p>
  Your text{% include fn.html label="注" color="#e74c3c" text="First note" %} here.
  More text{% include fn.html label="解讀" color="#3498db" text="First interpretation" %} continues.
  Another{% include fn.html label="注" color="#e74c3c" text="Second note" %} follows.
</p>
{% endcapture %}

{% include annotated_text.html content=main_text %}
```

This displays as: **注1**, **解讀1**, **注2** - each label type has its own counter!

Each footnote includes:
- `label` - The footnote label type (e.g., "注", "解讀", "脂批") - numbers are added automatically
- `color` - The color for this footnote (e.g., "#e74c3c")
- `text` - The explanation text shown in the sidebar

**Positioning behavior:**
- Footnotes are positioned adjacent to their anchored text (not accumulated at top)
- When a paragraph has many footnotes that extend beyond its height, subsequent paragraphs are automatically pushed down to avoid overlap

### 2. Connection Diagrams

Shows word-by-word connections between two sentences with colored lines:

```html
<div class="connection-diagram" data-pairs='[[0,1],[1,0],[2,2]]'>
  <div class="connection-row connection-row-top">
    <div class="word-box word-top" data-index="0">Word1</div>
    <div class="word-box word-top" data-index="1">Word2</div>
  </div>
  <svg class="connection-lines"></svg>
  <div class="connection-row connection-row-bottom">
    <div class="word-box word-bottom" data-index="0">Translation1</div>
    <div class="word-box word-bottom" data-index="1">Translation2</div>
  </div>
</div>
```

The `data-pairs` array defines connections: `[top_index, bottom_index]`.

## MD to DOCX Conversion

Convert markdown files with annotations to DOCX format with vertical Chinese text:

```bash
# Convert a single file
python scripts/md_to_docx.py pages/紅樓夢/紅樓夢1.md

# Convert all markdown files
python scripts/md_to_docx.py --all pages output_docx
```

The generated DOCX files feature:
- Vertical text direction (top-to-bottom, right-to-left columns)
- Landscape A4 page orientation
- Annotations collected as footnotes at the end

## Development

Run locally with:
```bash
bundle exec jekyll serve --host 0.0.0.0 --port 5000 --livereload
```

## Deployment

Configured for static deployment. Build with:
```bash
bundle exec jekyll build
```

Output is in `_site/` directory.
