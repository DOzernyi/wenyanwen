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
│   ├── annotated_text.html    # Side footnotes component
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

### 1. Annotated Text with Side Footnotes

Displays text with color-coded footnotes in a side column. Usage:

```html
<div class="annotated-container">
  <div class="annotated-main">
    Your text with <span class="note-ref" style="background-color: #e74c3c;">1</span> markers.
  </div>
  <div class="annotated-notes">
    <div class="sidenote" style="border-left-color: #e74c3c;">
      <span class="note-marker" style="background-color: #e74c3c;">1</span>
      Footnote text here.
    </div>
  </div>
</div>
```

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
