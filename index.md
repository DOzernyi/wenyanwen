---
layout: default
title: 通讀古文
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

.collapsible-section {
  margin-bottom: 50px;
}

.collapsible-section summary {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 28px;
  padding-bottom: 16px;
  border-bottom: 2px solid rgba(0,0,0,0.08);
  cursor: pointer;
  list-style: none;
  user-select: none;
}

.collapsible-section summary::-webkit-details-marker {
  display: none;
}

.collapsible-section summary::after {
  content: "▼";
  margin-left: auto;
  font-size: 0.8em;
  color: var(--ink-light);
  transition: transform 0.3s ease;
}

.collapsible-section:not([open]) summary::after {
  transform: rotate(-90deg);
}

.collapsible-section summary:hover {
  opacity: 0.8;
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

.section-content {
  animation: fadeIn 0.3s ease;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-10px); }
  to { opacity: 1; transform: translateY(0); }
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

.text-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.text-item {
  background: var(--paper-light);
  border-radius: 8px;
  padding: 14px 18px;
  border: 1px solid rgba(0,0,0,0.06);
  transition: all 0.2s ease;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  display: flex;
  align-items: baseline;
  gap: 12px;
}

.text-item:hover {
  transform: translateX(4px);
  box-shadow: 0 4px 16px rgba(0,0,0,0.1);
  background: white;
}

.text-item a {
  color: var(--ink-dark);
  text-decoration: none;
  font-size: 1.05em;
  font-weight: 500;
}

.text-item:hover a {
  color: var(--vermilion);
}

.text-source {
  color: var(--ink-light);
  font-size: 0.9em;
  font-style: italic;
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

.book-card.jing-hua .book-header {
  background: linear-gradient(135deg, rgba(156,89,182,0.08) 0%, transparent 100%);
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
.book-card.jing-hua .book-title { color: #9c59b6; }

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
.book-card.jing-hua .chapter-item { border-left-color: #9c59b6; }

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
.book-card.jing-hua .chapter-link:hover { color: #9c59b6; }

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
  .text-item {
    flex-direction: column;
    gap: 4px;
  }
}
</style>

<!-- 文言文教材 Section -->
<details class="collapsible-section" open>
  <summary>
    <span class="section-icon">📜</span>
    <h2 class="section-title">文言文教材</h2>
  </summary>
  <div class="section-content">
    <div class="level-group">
      <div class="level-label beginner">初級</div>
      <div class="text-list">
        <div class="text-item"><a href="/pages/白話文/入門/畫蛇添足.html">畫蛇添足</a><span class="text-source">《戰國策・齊策》</span></div>
        <div class="text-item"><a href="/pages/白話文/入門/以五十步笑百步.html">以五十步笑百步</a><span class="text-source">《孟子・梁惠王上》</span></div>
        <div class="text-item"><a href="/pages/白話文/入門/魚之樂.html">魚之樂</a><span class="text-source">《莊子・秋水》</span></div>
        <div class="text-item"><a href="/pages/白話文/入門/曹劌論戰.html">曹劌論戰</a><span class="text-source">《左傳・莊公十年》</span></div>
      </div>
    </div>

    <div class="level-group">
      <div class="level-label intermediate">中級</div>
      <div class="text-list">
        <div class="text-item"><a href="/pages/白話文/入門/大學.html">大學</a><span class="text-source">《禮記・大學》</span></div>
        <div class="text-item"><a href="/pages/白話文/入門/兼愛.html">兼愛</a><span class="text-source">《墨子・兼愛》</span></div>
        <div class="text-item"><a href="/pages/白話文/入門/告子上選.html">告子上選</a><span class="text-source">《孟子・告子上》</span></div>
        <div class="text-item"><a href="/pages/白話文/入門/王制.html">王制</a><span class="text-source">《荀子・王制》</span></div>
        <div class="text-item"><a href="/pages/白話文/入門/太王去邠.html">太王去邠</a><span class="text-source">《孟子・梁惠王下》</span></div>
      </div>
    </div>

    <div class="level-group">
      <div class="level-label advanced">高級</div>
      <div class="text-list">
        <div class="text-item"><a href="/pages/白話文/入門/屠羊說不受賞.html">屠羊說不受賞</a><span class="text-source">《莊子・讓王》</span></div>
        <div class="text-item"><a href="/pages/白話文/入門/馮諼客孟嘗君.html">馮諼客孟嘗君</a><span class="text-source">《戰國策・齊策》</span></div>
        <div class="text-item"><a href="/pages/白話文/入門/項羽本紀.html">項羽本紀</a><span class="text-source">《史記・項羽本紀》</span></div>
        <div class="text-item"><a href="/pages/白話文/燕丹子.html">燕丹子</a><span class="text-source">《燕丹子》</span></div>
      </div>
    </div>
  </div>
</details>

<!-- 古典小說注 Section -->
<details class="collapsible-section" open>
  <summary>
    <span class="section-icon">📚</span>
    <h2 class="section-title">古典小說注</h2>
  </summary>
  <div class="section-content">
    <div class="book-grid">

    <div class="book-card hong-lou">
      <div class="book-header">
        <h3 class="book-title">《紅樓夢》(注)(批選)</h3>
        <div class="book-meta">
          <span class="book-author">曹雪芹 著 (庚辰本為底本)</span>
        </div>
      </div>
      <div class="book-body">
        <ul class="chapter-list">
          <li class="chapter-item">
            <a href="/pages/紅樓夢/紅樓夢1.html" class="chapter-link">第一回　甄士隱夢幻識通靈　賈雨村風塵懷閨秀</a>
          </li>
          <li class="chapter-item">
            <a href="/pages/紅樓夢/紅樓夢2.html" class="chapter-link">第二回 賈夫人仙逝揚州城 冷子興演說榮國府</a>
          </li>
          <li class="chapter-item">
            <a href="/pages/紅樓夢/紅樓夢5.html" class="chapter-link">第五回 遊幻境指迷十二釵 飲仙醪曲演紅樓夢</a>
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
          <li class="chapter-item"><a href="/pages/儒林外史/儒林外史1.html" class="chapter-link">第一回　說楔子敷陳大義　借名流隱括全文</a></li>
          <li class="chapter-item"><a href="/pages/儒林外史/儒林外史2.html" class="chapter-link">第二回　王孝廉村學識同科　周蒙師暮年登上第</a></li>
          <li class="chapter-item"><a href="/pages/儒林外史/儒林外史3.html" class="chapter-link">第三回　周學道校士拔真才　胡屠戶行兇鬧捷報</a></li>
          <li class="chapter-item"><a href="/pages/儒林外史/儒林外史4.html" class="chapter-link">第四回　薦亡齋和尚喫官司　打秋風鄉紳遭橫事</a></li>
          <li class="chapter-item"><a href="/pages/儒林外史/儒林外史5.html" class="chapter-link">第五回　王秀才議立偏房　嚴監生疾終正寢</a></li>
          <li class="chapter-item"><a href="/pages/儒林外史/儒林外史6.html" class="chapter-link">第六回　鄉紳發病鬧船家　寡婦含冤控大伯</a></li>
          <li class="chapter-item"><a href="/pages/儒林外史/儒林外史7.html" class="chapter-link">第七回　范學道視學報師恩　王員外立朝敦友誼</a></li>
          <li class="chapter-item"><a href="/pages/儒林外史/儒林外史8.html" class="chapter-link">第八回　王觀察窮途逢世好　婁公子故里遇貧交</a></li>
          <li class="chapter-item"><a href="/pages/儒林外史/儒林外史9.html" class="chapter-link">第九回　婁公子捐金贖朋友　劉守備冒姓打船家</a></li>
          <li class="chapter-item"><a href="/pages/儒林外史/儒林外史10.html" class="chapter-link">第十回　魯翰林憐才擇婿　蘧公孫富室招親</a></li>
          <li class="chapter-item"><a href="/pages/儒林外史/儒林外史11.html" class="chapter-link">第十一回　魯小姐制義難新郎　楊司訓相府薦賢士</a></li>
          <li class="chapter-item"><a href="/pages/儒林外史/儒林外史12.html" class="chapter-link">第十二回　名士大宴鶯脰湖　俠客虛設人頭會</a></li>
          <li class="chapter-item"><a href="/pages/儒林外史/儒林外史13.html" class="chapter-link">第十三回　蘧駪夫求賢問業　馬純上仗義疎財</a></li>
          <li class="chapter-item"><a href="/pages/儒林外史/儒林外史14.html" class="chapter-link">第十四回　蘧公孫書坊送良友　馬秀才山洞遇神仙</a></li>
          <li class="chapter-item"><a href="/pages/儒林外史/儒林外史15.html" class="chapter-link">第十五回　葬神仙馬秀才送喪　思父母匡童生盡孝</a></li>
          <li class="chapter-item"><a href="/pages/儒林外史/儒林外史16.html" class="chapter-link">第十六回　大柳莊孝子事親　樂清縣賢宰愛士</a></li>
          <li class="chapter-item"><a href="/pages/儒林外史/儒林外史17.html" class="chapter-link">第十七回　匡秀才重遊舊地　趙醫生高踞詩壇</a></li>
          <li class="chapter-item"><a href="/pages/儒林外史/儒林外史18.html" class="chapter-link">第十八回　約詩會名士攜匡二　訪朋友書店會潘三</a></li>
          <li class="chapter-item"><a href="/pages/儒林外史/儒林外史19.html" class="chapter-link">第十九回　匡超人幸得良朋　潘自業橫遭禍事</a></li>
          <li class="chapter-item"><a href="/pages/儒林外史/儒林外史20.html" class="chapter-link">第二十回　匡超人高興長安道　牛布衣客死蕪湖關</a></li>
        </ul>
        <p class="coming-soon">更多章節即將推出（第二十一至三十七回）</p>
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
          <li class="chapter-item">
            <a href="/pages/水滸傳/水滸傳1.html" class="chapter-link">第一回　張天師祈禳瘟疫　洪太尉誤走妖魔</a>
          </li>
        </ul>
        <p class="coming-soon">更多章節即將推出</p>
      </div>
    </div>

    <div class="book-card jing-hua">
      <div class="book-header">
        <h3 class="book-title">《鏡花緣》</h3>
        <div class="book-meta">
          <span class="book-author">李汝珍 著</span>
        </div>
      </div>
      <div class="book-body">
        <ul class="chapter-list">
          <li class="chapter-item">
            <a href="/pages/鏡花緣/鏡花緣1.html" class="chapter-link">第一回　女魁星北斗垂景象　老王母西池賜芳筵</a>
          </li>
        </ul>
        <p class="coming-soon">更多章節即將推出</p>
      </div>
    </div>

    </div>
  </div>
</details>

<!-- 中華文學史閒劄 Section -->
<details class="collapsible-section" open>
  <summary>
    <span class="section-icon">🖊</span>
    <h2 class="section-title">中華文學史閒劄</h2>
  </summary>
  <div class="section-content">
    <div class="text-list">
      <div class="text-item"><a href="/pages/中華文學史閒劄/漢代.html">漢代：賦體、樂府詩、五言詩</a></div>
      <div class="text-item"><a href="/pages/中華文學史閒劄/魏晉.html">魏晉</a></div>
    </div>
  </div>
</details>

<!-- 翻譯 Translations Section -->
<details class="collapsible-section">
  <summary>
    <span class="section-icon">🌐</span>
    <h2 class="section-title">翻譯 Translations</h2>
  </summary>
  <div class="section-content">
    <div class="level-group">
      <div class="level-label intermediate">Українська</div>
      <div class="text-list">
        <div class="text-item"><a href="/pages/українська/вступ/畫蛇添足ukr.html">畫蛇添足</a></div>
        <div class="text-item"><a href="/pages/українська/вступ/以五十步笑百步ukr.html">以五十步笑百步</a></div>
        <div class="text-item"><a href="/pages/українська/вступ/魚之樂ukr.html">魚之樂</a></div>
        <div class="text-item"><a href="/pages/українська/вступ/曹劌論戰ukr.html">曹劌論戰</a></div>
        <div class="text-item"><a href="/pages/українська/вступ/大學ukr.html">大學</a></div>
        <div class="text-item"><a href="/pages/українська/вступ/兼愛ukr.html">兼愛</a></div>
        <div class="text-item"><a href="/pages/українська/вступ/告子上選ukr.html">告子上選</a></div>
        <div class="text-item"><a href="/pages/українська/вступ/王制ukr.html">王制</a></div>
        <div class="text-item"><a href="/pages/українська/вступ/太王去邠ukr.html">太王去邠</a></div>
        <div class="text-item"><a href="/pages/українська/вступ/屠羊說不受賞ukr.html">屠羊說不受賞</a></div>
        <div class="text-item"><a href="/pages/українська/вступ/馮諼客孟嘗君ukr.html">馮諼客孟嘗君</a></div>
        <div class="text-item"><a href="/pages/українська/вступ/項羽本紀ukr.html">項羽本紀</a></div>
        <div class="text-item"><a href="/pages/українська/燕丹子ukr.html">燕丹子</a></div>
      </div>
    </div>
    <div class="level-group">
      <div class="level-label beginner">English</div>
      <div class="text-list">
        <div class="text-item"><a href="/pages/english/燕丹子eng.html">燕丹子 (Prince Dan of Yan)</a></div>
      </div>
    </div>
  </div>
</details>

<!-- 其他資源 Section -->
<div class="resources-section">
  <h2 class="resources-title">其他資源</h2>
  <div class="resources-grid">
    <a href="/pages/guide.html" class="resource-link">編寫指南</a>
    <a href="/pages/demo.html" class="resource-link">功能示範</a>
    <a href="https://docs.google.com/document/d/17izkGXYQcVRLE7M4e6zg7eM_1IEPqxfL/edit" class="resource-link">屈原列傳</a>
    <a href="https://docs.google.com/document/d/1u4yg8lehsZjKUoFGHDfxvp7VUWlGDR7X/edit" class="resource-link">離騷</a>
    <a href="https://docs.google.com/document/d/1dcgLw7Ky1fs8p-PPQmKK-l60tiahFK1g/edit" class="resource-link">尚書</a>
  </div>
</div>
