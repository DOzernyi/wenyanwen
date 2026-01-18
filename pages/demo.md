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
  古之學者必有師{% include fn.html label="注" color="#e74c3c" text="師：老師，指有專門知識或技能的人。" %}。師者，所以傳道受業解惑也{% include fn.html label="解讀" color="#3498db" text="這句話說明老師的三個職責：傳授道理、教授學業、解答疑惑。" %}。人非生而知之者，孰能無惑{% include fn.html label="注" color="#e74c3c" text="孰：誰。" %}？惑而不從師，其為惑也{% include fn.html label="解讀" color="#3498db" text="有疑惑卻不向老師請教，那疑惑就永遠無法解開。" %}，終不解矣{% include fn.html label="脂批" color="#9b59b6" text="此開卷第一回也。作者自云曾歷過一番夢幻之後，故將真事隱去。" %}。
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

### Annotated Text (Simple Syntax with Auto-Numbering)

Footnotes are now **automatically numbered** by label type. Just specify the label (like "注", "解讀", "脂批") and the system adds the number for you.

**Usage:** In your content, use the `fn.html` include with a `label` parameter:

```liquid
{% raw %}{% capture main_text %}
<p>
  Your text{% include fn.html label="注" color="#e74c3c" text="First note explanation" %} here.
  More text{% include fn.html label="解讀" color="#3498db" text="First interpretation" %} continues.
  Another note{% include fn.html label="注" color="#e74c3c" text="Second note explanation" %} follows.
</p>
{% endcapture %}

{% include annotated_text.html content=main_text %}{% endraw %}
```

This will display as: 注1, 解讀1, 注2 - each label type gets its own counter!

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