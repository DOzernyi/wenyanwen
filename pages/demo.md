---
layout: default
title: Demo - Annotated Text & Connection Diagrams
notes:
  - id: 解讀12
    color: "#e74c3c"
    text: "學者：求學的人。古時指讀書人。"
  - id: 2
    color: "#3498db"
    text: "傳道：傳授道理。受業：教授學業。解惑：解答疑惑。"
  - id: 3
    color: "#2ecc71"
    text: "生而知之：生來就懂得道理。孰：誰。"
  - id: 注4
    color: "#9b59b6"
    text: "從師：跟從老師學習。終：最終。"
   - id: 5
    color: "#9b59b6"
    text: "我想要寫的任何說明或注意。"

---

# Feature Demo

This page demonstrates the two main features: **annotated text with side footnotes** and **connection diagrams**.

---

## 1. Annotated Text with Side Footnotes

Use the annotated text component to display text with footnotes in a side column. Each footnote can have a different color.

{% capture main_text %}
<p>
  古之學者必有師{% include fn.html id="解讀12" color="#e74c3c" %}。師者，所以傳道受業解惑也{% include fn.html id="2" color="#3498db" %}。人非生而知之者，孰能無惑{% include fn.html id="3" color="#2ecc71" %}？惑而不從師，其為惑也{% include fn.html id="5" color="#9b59b6" %}，終不解矣{% include fn.html id="注4" color="#9b59b6" %}。
</p>
{% endcapture %}

{% include annotated_text.html content=main_text notes=page.notes %}

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

<div class="connection-diagram" data-pairs='[[0,2],[1,0],[2,3],[3,1]]'>
  <div class="connection-row connection-row-top">
    <div class="word-box word-top" data-index="0">The</div>
    <div class="word-box word-top" data-index="1">cat</div>
    <div class="word-box word-top" data-index="2">sits</div>
    <div class="word-box word-top" data-index="3">here</div>
  </div>
  <svg class="connection-lines"></svg>
  <div class="connection-row connection-row-bottom">
    <div class="word-box word-bottom" data-index="0">貓</div>
    <div class="word-box word-bottom" data-index="1">這裡</div>
    <div class="word-box word-bottom" data-index="2">那</div>
    <div class="word-box word-bottom" data-index="3">坐</div>
  </div>
</div>

---

## How to Use These Features

### Annotated Text (Simple Syntax)

**Step 1:** Define your notes in the page front-matter:

```yaml
---
notes:
  - id: 1
    color: "#e74c3c"
    text: "Your first footnote explanation"
  - id: 2
    color: "#3498db"
    text: "Your second footnote explanation"
---
```

**Step 2:** In your content, use the `fn.html` include for inline markers:

```liquid
{% raw %}{% capture main_text %}
Your text here{% include fn.html id="1" color="#e74c3c" %} with markers.
{% endcapture %}

{% include annotated_text.html content=main_text notes=page.notes %}{% endraw %}
```

### Connection Diagrams

To create a connection diagram, use this structure:

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

The `data-pairs` attribute defines which words connect:
- `[0,1]` means word at index 0 (top) connects to word at index 1 (bottom)
- Each connection gets a different color automatically
