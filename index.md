---
layout: default
title: 閱讀古文
---

<style>
:root {
  --ink-dark: #2b2b2b;
  --ink-medium: #4a4a4a;
  --ink-light: #6b6b6b;
  --paper-warm: #f7f2e7;
  --paper-light: #fdfbf7;
  --vermilion: #b24a3b;
  --vermilion-light: #d4675a;
  --jade: #4d7c6c;
  --jade-light: #6a9b8a;
  --gold-accent: #c9a227;
}

.hero-section {
  text-align: center;
  padding: 40px 20px 50px;
  margin-bottom: 40px;
  background: linear-gradient(180deg, var(--paper-warm) 0%, var(--paper-light) 100%);
  border-radius: 8px;
  position: relative;
}

.hero-section::before {
  content: "文";
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 180px;
  color: rgba(0,0,0,0.03);
  font-family: 'cwTeXMing', serif;
  z-index: 0;
}

.hero-title {
  font-size: 2.2em;
  color: var(--ink-dark);
  margin: 0 0 12px 0;
  font-weight: 400;
  letter-spacing: 0.15em;
  position: relative;
  z-index: 1;
}

.hero-subtitle {
  font-size: 1.1em;
  color: var(--ink-light);
  margin: 0;
  font-weight: 300;
  position: relative;
  z-index: 1;
}

.divider {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 35px 0;
  color: var(--ink-light);
}

.divider::before,
.divider::after {
  content: "";
  flex: 1;
  height: 1px;
  background: linear-gradient(90deg, transparent, #ccc, transparent);
}

.divider-icon {
  padding: 0 20px;
  font-size: 1.2em;
  color: var(--gold-accent);
}

.toc-section-title {
  text-align: center;
  font-size: 1.4em;
  color: var(--ink-medium);
  margin-bottom: 30px;
  font-weight: 400;
  letter-spacing: 0.1em;
}

.book-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 28px;
  margin-bottom: 40px;
}

.book-card {
  background: var(--paper-light);
  border-radius: 12px;
  padding: 0;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(0,0,0,0.08);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  border: 1px solid rgba(0,0,0,0.06);
}

.book-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 30px rgba(0,0,0,0.12);
}

.book-header {
  padding: 24px 24px 16px;
  border-bottom: 1px solid rgba(0,0,0,0.06);
  position: relative;
}

.book-header::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 24px;
  right: 24px;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(0,0,0,0.08), transparent);
}

.book-card.hong-lou .book-header {
  background: linear-gradient(135deg, rgba(178,74,59,0.08) 0%, transparent 100%);
}

.book-card.ru-lin .book-header {
  background: linear-gradient(135deg, rgba(77,124,108,0.08) 0%, transparent 100%);
}

.book-title {
  font-size: 1.5em;
  color: var(--ink-dark);
  margin: 0 0 8px 0;
  font-weight: 500;
  letter-spacing: 0.08em;
}

.book-card.hong-lou .book-title {
  color: var(--vermilion);
}

.book-card.ru-lin .book-title {
  color: var(--jade);
}

.book-meta {
  display: flex;
  align-items: center;
  gap: 12px;
  color: var(--ink-light);
  font-size: 0.9em;
}

.book-author {
  display: flex;
  align-items: center;
  gap: 6px;
}

.book-author::before {
  content: "✦";
  font-size: 0.7em;
  opacity: 0.5;
}

.book-body {
  padding: 20px 24px 24px;
}

.chapter-list {
  list-style: none;
  padding: 0;
  margin: 0 0 16px 0;
}

.chapter-item {
  padding: 14px 16px;
  margin-bottom: 8px;
  background: rgba(255,255,255,0.6);
  border-radius: 8px;
  border-left: 3px solid transparent;
  transition: all 0.2s ease;
}

.book-card.hong-lou .chapter-item {
  border-left-color: var(--vermilion);
}

.book-card.ru-lin .chapter-item {
  border-left-color: var(--jade);
}

.chapter-item:hover {
  background: rgba(255,255,255,0.9);
  padding-left: 20px;
}

.chapter-link {
  color: var(--ink-dark);
  text-decoration: none;
  font-size: 1em;
  display: block;
  line-height: 1.5;
}

.chapter-link:hover {
  color: var(--vermilion);
}

.book-card.ru-lin .chapter-link:hover {
  color: var(--jade);
}

.coming-soon {
  display: flex;
  align-items: center;
  gap: 8px;
  color: var(--ink-light);
  font-size: 0.85em;
  font-style: italic;
  padding: 8px 0 0;
  border-top: 1px dashed rgba(0,0,0,0.1);
}

.coming-soon::before {
  content: "◇";
  font-size: 0.8em;
}

.resources-section {
  margin-top: 50px;
  padding: 30px;
  background: var(--paper-warm);
  border-radius: 12px;
}

.resources-title {
  font-size: 1.2em;
  color: var(--ink-medium);
  margin: 0 0 20px 0;
  padding-bottom: 12px;
  border-bottom: 2px solid rgba(0,0,0,0.08);
  letter-spacing: 0.08em;
}

.resources-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 12px;
}

.resource-link {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 16px;
  background: white;
  border-radius: 8px;
  color: var(--ink-dark);
  text-decoration: none;
  font-size: 0.95em;
  transition: all 0.2s ease;
  border: 1px solid rgba(0,0,0,0.05);
}

.resource-link:hover {
  background: var(--paper-light);
  transform: translateX(4px);
  color: var(--vermilion);
}

.resource-link::before {
  content: "→";
  color: var(--gold-accent);
  font-weight: bold;
}

@media screen and (max-width: 600px) {
  .hero-title {
    font-size: 1.8em;
  }
  .book-grid {
    grid-template-columns: 1fr;
  }
}
</style>

<div class="hero-section">
  <h1 class="hero-title">閱讀古文</h1>
  <p class="hero-subtitle">經典文學・註釋導讀・深入淺出</p>
</div>

<div class="divider">
  <span class="divider-icon">❖</span>
</div>

<h2 class="toc-section-title">經典選讀</h2>

<div class="book-grid">

<div class="book-card hong-lou">
  <div class="book-header">
    <h3 class="book-title">《紅樓夢》</h3>
    <div class="book-meta">
      <span class="book-author">曹雪芹 著</span>
    </div>
  </div>
  <div class="book-body">
    <ul class="chapter-list">
      <li class="chapter-item">
        <a href="/pages/紅樓夢/紅樓夢1.html" class="chapter-link">第一回　甄士隱夢幻識通靈<br>賈雨村風塵懷閨秀</a>
      </li>
    </ul>
    <p class="coming-soon">更多章節即將推出</p>
  </div>
</div>

<div class="book-card ru-lin">
  <div class="book-header">
    <h3 class="book-title">《儒林外史》</h3>
    <div class="book-meta">
      <span class="book-author">吳敬梓 著</span>
    </div>
  </div>
  <div class="book-body">
    <ul class="chapter-list">
      <li class="chapter-item">
        <a href="/pages/儒林外史/儒林外史1.html" class="chapter-link">第一回　說楔子敷陳大義<br>借名流隱括全文</a>
      </li>
      <li class="chapter-item">
        <a href="/pages/儒林外史/儒林外史2.html" class="chapter-link">第二回　說楔子敷陳大義<br>借名流隱括全文</a>
      </li>
    </ul>
    <p class="coming-soon">更多章節即將推出</p>
  </div>
</div>

</div>

<div class="resources-section">
  <h2 class="resources-title">其他資源</h2>
  <div class="resources-grid">
    <a href="/pages/demo.html" class="resource-link">功能示範</a>
    <a href="https://docs.google.com/document/d/17izkGXYQcVRLE7M4e6zg7eM_1IEPqxfL/edit" class="resource-link">屈原列傳</a>
    <a href="https://docs.google.com/document/d/1u4yg8lehsZjKUoFGHDfxvp7VUWlGDR7X/edit" class="resource-link">離騷</a>
    <a href="https://docs.google.com/document/d/1dcgLw7Ky1fs8p-PPQmKK-l60tiahFK1g/edit" class="resource-link">尚書</a>
  </div>
</div>
