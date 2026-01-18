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

### 1. Annotated Text with Side Footnotes (Simple Syntax)

**Step 1:** Define notes in page front-matter using a map format (simpler than list):

```yaml
---
notes:
  解讀1:
    color: "#e74c3c"
    text: "First footnote explanation"
  注2:
    color: "#3498db"
    text: "Second footnote explanation"
---
```

To add a new note, just add a new ID followed by colon, then indent `color` and `text`:

```yaml
  新注釋:
    color: "#ff6600"
    text: "Your new note"
```

**Step 2:** Use `fn.html` for inline markers and `annotated_text.html` for the container:

```liquid
{% capture main_text %}
Your text{% include fn.html id="解讀1" color="#e74c3c" %} with markers.
{% endcapture %}

{% include annotated_text.html content=main_text notes=page.notes %}
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
