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
  --azure: #3d6b99;
}

.section-block {
  margin-bottom: 50px;
}

.section-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 28px;
  padding-bottom: 16px;
  border-bottom: 2px solid rgba(0,0,0,0.08);
}

.section-icon {
  font-size: 1.4em;
}

.section-title {
  font-size: 1.5em;
  color: var(--ink-dark);
  margin: 0;
  font-weight: 500;
  letter-spacing: 0.1em;
}

.level-group {
  margin-bottom: 24px;
}

.level-label {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 0.95em;
  color: var(--ink-light);
  margin-bottom: 12px;
  padding: 4px 12px;
  background: var(--paper-warm);
  border-radius: 4px;
}

.level-label.beginner { border-left: 3px solid var(--jade); }
.level-label.intermediate { border-left: 3px solid var(--azure); }
.level-label.advanced { border-left: 3px solid var(--vermilion); }

.text-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 12px;
}

.text-card {
  background: var(--paper-light);
  border-radius: 8px;
  padding: 14px 16px;
  border: 1px solid rgba(0,0,0,0.06);
  transition: all 0.2s ease;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}

.text-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(0,0,0,0.1);
  background: white;
}

.text-card a {
  color: var(--ink-dark);
  text-decoration: none;
  font-size: 1em;
  display: block;
}

.text-card:hover a {
  color: var(--vermilion);
}

.book-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 24px;
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
  padding: 20px 20px 14px;
  border-bottom: 1px solid rgba(0,0,0,0.06);
  position: relative;
}

.book-card.hong-lou .book-header {
  background: linear-gradient(135deg, rgba(178,74,59,0.08) 0%, transparent 100%);
}

.book-card.ru-lin .book-header {
  background: linear-gradient(135deg, rgba(77,124,108,0.08) 0%, transparent 100%);
}

.book-card.shui-hu .book-header {
  background: linear-gradient(135deg, rgba(61,107,153,0.08) 0%, transparent 100%);
}

.book-title {
  font-size: 1.4em;
  color: var(--ink-dark);
  margin: 0 0 6px 0;
  font-weight: 500;
  letter-spacing: 0.08em;
}

.book-card.hong-lou .book-title { color: var(--vermilion); }
.book-card.ru-lin .book-title { color: var(--jade); }
.book-card.shui-hu .book-title { color: var(--azure); }

.book-meta {
  display: flex;
  align-items: center;
  gap: 12px;
  color: var(--ink-light);
  font-size: 0.85em;
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
  padding: 16px 20px 20px;
}

.chapter-list {
  list-style: none;
  padding: 0;
  margin: 0 0 12px 0;
}

.chapter-item {
  padding: 12px 14px;
  margin-bottom: 6px;
  background: rgba(255,255,255,0.6);
  border-radius: 6px;
  border-left: 3px solid transparent;
  transition: all 0.2s ease;
}

.book-card.hong-lou .chapter-item { border-left-color: var(--vermilion); }
.book-card.ru-lin .chapter-item { border-left-color: var(--jade); }
.book-card.shui-hu .chapter-item { border-left-color: var(--azure); }

.chapter-item:hover {
  background: rgba(255,255,255,0.9);
  padding-left: 18px;
}

.chapter-link {
  color: var(--ink-dark);
  text-decoration: none;
  font-size: 0.95em;
  display: block;
  line-height: 1.5;
}

.chapter-link:hover { color: var(--vermilion); }
.book-card.ru-lin .chapter-link:hover { color: var(--jade); }
.book-card.shui-hu .chapter-link:hover { color: var(--azure); }

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
  padding: 24px;
  background: var(--paper-warm);
  border-radius: 12px;
}

.resources-title {
  font-size: 1.1em;
  color: var(--ink-medium);
  margin: 0 0 16px 0;
  padding-bottom: 10px;
  border-bottom: 2px solid rgba(0,0,0,0.08);
  letter-spacing: 0.08em;
}

.resources-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 10px;
}

.resource-link {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 14px;
  background: white;
  border-radius: 6px;
  color: var(--ink-dark);
  text-decoration: none;
  font-size: 0.9em;
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
  .book-grid {
    grid-template-columns: 1fr;
  }
  .text-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>

<!-- 文言文教材 Section -->
<div class="section-block">
  <div class="section-header">
    <span class="section-icon">📜</span>
    <h2 class="section-title">文言文教材</h2>
  </div>

  <div class="level-group">
    <div class="level-label beginner">初級</div>
    <div class="text-grid">
      <div class="text-card"><a href="/pages/白話文/入門/畫蛇添足.html">畫蛇添足</a></div>
      <div class="text-card"><a href="/pages/白話文/入門/以五十步笑百步.html">以五十步笑百步</a></div>
      <div class="text-card"><a href="/pages/白話文/入門/魚之樂.html">魚之樂</a></div>
      <div class="text-card"><a href="/pages/白話文/入門/曹劌論戰.html">曹劌論戰</a></div>
    </div>
  </div>

  <div class="level-group">
    <div class="level-label intermediate">中級</div>
    <div class="text-grid">
      <div class="text-card"><a href="/pages/白話文/入門/大學.html">大學</a></div>
      <div class="text-card"><a href="/pages/白話文/入門/兼愛.html">兼愛</a></div>
      <div class="text-card"><a href="/pages/白話文/入門/告子上選.html">告子上選</a></div>
      <div class="text-card"><a href="/pages/白話文/入門/王制.html">王制</a></div>
      <div class="text-card"><a href="/pages/白話文/入門/太王去邠.html">太王去邠</a></div>
    </div>
  </div>

  <div class="level-group">
    <div class="level-label advanced">高級</div>
    <div class="text-grid">
      <div class="text-card"><a href="/pages/白話文/入門/屠羊說不受賞.html">屠羊說不受賞</a></div>
      <div class="text-card"><a href="/pages/白話文/入門/馮諼客孟嘗君.html">馮諼客孟嘗君</a></div>
      <div class="text-card"><a href="/pages/白話文/入門/項羽本紀.html">項羽本紀</a></div>
      <div class="text-card"><a href="/pages/白話文/燕丹子.html">燕丹子</a></div>
    </div>
  </div>
</div>

<!-- 古典小說注 Section -->
<div class="section-block">
  <div class="section-header">
    <span class="section-icon">📚</span>
    <h2 class="section-title">古典小說注</h2>
  </div>

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
          <a href="/pages/紅樓夢/紅樓夢1.html" class="chapter-link">第一回　甄士隱夢幻識通靈　賈雨村風塵懷閨秀</a>
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
          <a href="/pages/儒林外史/儒林外史1.html" class="chapter-link">第一回　說楔子敷陳大義　借名流隱括全文</a>
        </li>
      </ul>
      <p class="coming-soon">更多章節即將推出</p>
    </div>
  </div>

  <div class="book-card shui-hu">
    <div class="book-header">
      <h3 class="book-title">《水滸傳》</h3>
      <div class="book-meta">
        <span class="book-author">施耐庵 著</span>
      </div>
    </div>
    <div class="book-body">
      <ul class="chapter-list">
        <li class="chapter-item" style="background: rgba(0,0,0,0.03); border-left-color: #ccc;">
          <span class="chapter-link" style="color: var(--ink-light); font-style: italic;">敬請期待</span>
        </li>
      </ul>
      <p class="coming-soon">章節準備中</p>
    </div>
  </div>

  </div>
</div>

<!-- 其他資源 Section -->
<div class="resources-section">
  <h2 class="resources-title">其他資源</h2>
  <div class="resources-grid">
    <a href="/pages/demo.html" class="resource-link">功能示範</a>
    <a href="https://docs.google.com/document/d/17izkGXYQcVRLE7M4e6zg7eM_1IEPqxfL/edit" class="resource-link">屈原列傳</a>
    <a href="https://docs.google.com/document/d/1u4yg8lehsZjKUoFGHDfxvp7VUWlGDR7X/edit" class="resource-link">離騷</a>
    <a href="https://docs.google.com/document/d/1dcgLw7Ky1fs8p-PPQmKK-l60tiahFK1g/edit" class="resource-link">尚書</a>
  </div>
</div>
