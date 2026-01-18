---
layout: default
title: Demo - Annotated Text & Connection Diagrams
---

# Feature Demo

This page demonstrates the two main features: **annotated text with side footnotes** and **connection diagrams**.

---

## 1. Annotated Text with Side Footnotes

Use the annotated text component to display text with footnotes in a side column. Each footnote can have a different color.

{% capture main_text %}
<p>
  古之學者必有師{% include fn.html id="解讀1" color="#e74c3c" text="學者：求學的人。古時指讀書人。" %}。師者，所以傳道受業解惑也{% include fn.html id="注2" color="#3498db" text="傳道：傳授道理。受業：教授學業。解惑：解答疑惑。" %}。人非生而知之者，孰能無惑{% include fn.html id="注3" color="#2ecc71" text="生而知之：生來就懂得道理。孰：誰。" %}？惑而不從師，其為惑也{% include fn.html id="注4" color="#9b59b6" text="從師：跟從老師學習。" %}，終不解矣{% include fn.html id="注5" color="#f39c12" text="終：最終。解：理解。" %}。
</p>
{% endcapture %}

{% include annotated_text.html content=main_text %}

---

## 2. Connection Diagrams

Use connection diagrams to show word-by-word relationships between two sentences. Lines connect words from the top sentence to words in the bottom sentence.

### Example: Classical Chinese to Modern Chinese

<div class="connection-diagram" data-pairs='[[0,0],[1,1],[2,2],[3,3]]'>
  <div class="connection-row connection-row-top">
    <div class="word-box word-top" data-index="0">學</div>
    <div class="word-box word-top" data-index="1">而</div>
    <div class="word-box word-top" data-index="2">時</div>
    <div class="word-box word-top" data-index="3">習</div>
  </div>
  <svg class="connection-lines"></svg>
  <div class="connection-row connection-row-bottom">
    <div class="word-box word-bottom" data-index="0">學習</div>
    <div class="word-box word-bottom" data-index="1">而且</div>
    <div class="word-box word-bottom" data-index="2">時常</div>
    <div class="word-box word-bottom" data-index="3">溫習</div>
  </div>
</div>

### Example: Cross-connections

<div class="connection-diagram" data-pairs='[[0,1],[1,0],[2,2]]'>
  <div class="connection-row connection-row-top">
    <div class="word-box word-top" data-index="0">吾</div>
    <div class="word-box word-top" data-index="1">愛</div>
    <div class="word-box word-top" data-index="2">汝</div>
  </div>
  <svg class="connection-lines"></svg>
  <div class="connection-row connection-row-bottom">
    <div class="word-box word-bottom" data-index="0">愛</div>
    <div class="word-box word-bottom" data-index="1">我</div>
    <div class="word-box word-bottom" data-index="2">你</div>
  </div>
</div>

---

## How to Use These Features

### Adding Annotated Text (Inline Method - No YAML Needed!)

Just add footnotes directly inline with your text:

```liquid
{% raw %}{% capture main_text %}
Your text{% include fn.html id="注1" color="#e74c3c" text="Your explanation here" %} continues here.
{% endcapture %}

{% include annotated_text.html content=main_text %}{% endraw %}
```

Each footnote includes:
- `id` - The label shown in the marker (e.g., "注1", "解讀2")
- `color` - The color for this footnote (e.g., "#e74c3c")
- `text` - The explanation shown in the sidebar

### Connection Diagrams

```html
<div class="connection-diagram" data-pairs='[[0,1],[1,0]]'>
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
