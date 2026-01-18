---
layout: default
title: Demo - Annotated Text & Connection Diagrams
---

# Feature Demo

This page demonstrates the two main features: **annotated text with side footnotes** and **connection diagrams**.

---

## 1. Annotated Text with Side Footnotes

Use the annotated text component to display text with footnotes in a side column. Each footnote can have a different color.

<div class="annotated-container">
  <div class="annotated-main">
    <p>
      古之學者必有師<span class="note-ref" style="background-color: #e74c3c;">1</span>。師者，所以傳道受業解惑也<span class="note-ref" style="background-color: #3498db;">2</span>。人非生而知之者，孰能無惑<span class="note-ref" style="background-color: #2ecc71;">3</span>？惑而不從師，其為惑也，終不解矣<span class="note-ref" style="background-color: #9b59b6;">4</span>。
    </p>
  </div>
  <div class="annotated-notes">
    <div class="sidenote" style="border-left-color: #e74c3c;">
      <span class="note-marker" style="background-color: #e74c3c;">1</span>
      學者：求學的人。古時指讀書人。
    </div>
    <div class="sidenote" style="border-left-color: #3498db;">
      <span class="note-marker" style="background-color: #3498db;">2</span>
      傳道：傳授道理。受業：教授學業。解惑：解答疑惑。
    </div>
    <div class="sidenote" style="border-left-color: #2ecc71;">
      <span class="note-marker" style="background-color: #2ecc71;">3</span>
      生而知之：生來就懂得道理。孰：誰。
    </div>
    <div class="sidenote" style="border-left-color: #9b59b6;">
      <span class="note-marker" style="background-color: #9b59b6;">4</span>
      從師：跟從老師學習。終：最終。
    </div>
  </div>
</div>

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

### Annotated Text

To create annotated text, use this HTML structure in your markdown:

```html
<div class="annotated-container">
  <div class="annotated-main">
    Your main text here with 
    <span class="note-ref" style="background-color: #e74c3c;">1</span>
    markers.
  </div>
  <div class="annotated-notes">
    <div class="sidenote" style="border-left-color: #e74c3c;">
      <span class="note-marker" style="background-color: #e74c3c;">1</span>
      Your footnote explanation here.
    </div>
  </div>
</div>
```

### Connection Diagrams

To create a connection diagram, use this structure:

```html
<div class="connection-diagram" data-pairs='[[0,1],[1,0],[2,2]]'>
  <div class="connection-row connection-row-top">
    <div class="word-box word-top" data-index="0">Word1</div>
    <div class="word-box word-top" data-index="1">Word2</div>
    <div class="word-box word-top" data-index="2">Word3</div>
  </div>
  <svg class="connection-lines"></svg>
  <div class="connection-row connection-row-bottom">
    <div class="word-box word-bottom" data-index="0">Translation1</div>
    <div class="word-box word-bottom" data-index="1">Translation2</div>
    <div class="word-box word-bottom" data-index="2">Translation3</div>
  </div>
</div>
```

The `data-pairs` attribute defines which words connect:
- `[0,1]` means word at index 0 (top) connects to word at index 1 (bottom)
- Each connection gets a different color automatically
- You can also specify a custom color: `[0,1,"#ff0000"]`
