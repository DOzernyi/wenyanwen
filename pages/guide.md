---
layout: default
title: 編寫指南
---

# 編寫指南

本頁說明本站所有可用的排版功能與 Markdown 語法。

---

## 一、基本 Markdown 語法

### 標題

```markdown
# 一級標題
## 二級標題
### 三級標題
#### 四級標題
```

### 文字格式

```markdown
**粗體文字**
*斜體文字*
~~刪除線~~
```

效果：**粗體文字**、*斜體文字*、~~刪除線~~

### 列表

**無序列表：**

```markdown
* 第一項
* 第二項
  * 子項目
  * 子項目
* 第三項
```

效果：

* 第一項
* 第二項
  * 子項目
  * 子項目
* 第三項

**有序列表：**

```markdown
1. 第一步
2. 第二步
   1. 子步驟
   2. 子步驟
3. 第三步
```

效果：

1. 第一步
2. 第二步
   1. 子步驟
   2. 子步驟
3. 第三步

### 引用

```markdown
> 學而時習之，不亦說乎？
> ——《論語》
```

效果：

> 學而時習之，不亦說乎？
> ——《論語》

### 連結

```markdown
[連結文字](https://example.com)
```

### 水平分隔線

```markdown
---
```

### 程式碼區塊

用三個反引號包圍：

````markdown
```
這是程式碼區塊
```
````

---

## 二、帶註腳的文本

在文中嵌入帶顏色的自動編號註腳，註腳會顯示在右側邊欄。頁面右上角會出現篩選按鈕，可以按標籤類型顯示或隱藏註腳。

### 基本結構

每個頁面的正文需要用 `capture` 包裹，然後交給 `annotated_text.html` 渲染：

```liquid
{% raw %}{% capture main_text %}

你的正文內容寫在這裡，可以使用 Markdown 語法。

{% endcapture %}

{% include annotated_text.html content=main_text %}{% endraw %}
```

### 加入註腳

在正文中用 `fn.html` 插入註腳標記：

```liquid
{% raw %}{% include fn.html label="注" color="#e74c3c" text="這是註解內容" %}{% endraw %}
```

參數說明：

| 參數 | 說明 | 範例 |
|------|------|------|
| `label` | 標籤類型（自動編號） | `"注"`、`"解讀"`、`"脂批"` |
| `color` | 標籤顏色 | `"#e74c3c"`（紅）、`"#3498db"`（藍） |
| `text` | 註解文字 | `"師：老師也。"` |

### 自動編號

同一個標籤類型會自動編號。例如：

```liquid
{% raw %}第一個注{% include fn.html label="注" color="#e74c3c" text="第一條注釋" %}
第二個注{% include fn.html label="注" color="#e74c3c" text="第二條注釋" %}
一個解讀{% include fn.html label="解讀" color="#3498db" text="解讀內容" %}{% endraw %}
```

會顯示為：**注1**、**注2**、**解讀1**——每種標籤各有自己的計數器。

### 完整範例

{% capture example_text %}

天下之事以利而合者{% include fn.html label="注" color="#e74c3c" text="以利而合：因利益而結合。" %}，亦以利而離{% include fn.html label="解讀" color="#3498db" text="有利則聚，無利則散，說明利益關係的脆弱。" %}。

{% endcapture %}

{% include annotated_text.html content=example_text id="example1" %}

上面範例的寫法：

```liquid
{% raw %}{% capture example_text %}

天下之事以利而合者{% include fn.html label="注" color="#e74c3c" text="以利而合：因利益而結合。" %}，亦以利而離{% include fn.html label="解讀" color="#3498db" text="有利則聚，無利則散，說明利益關係的脆弱。" %}。

{% endcapture %}

{% include annotated_text.html content=example_text id="example1" %}{% endraw %}
```

### 常用顏色參考

| 用途 | 顏色代碼 | 效果 |
|------|----------|------|
| 注釋 | `#e74c3c` | <span style="color:#e74c3c">紅色</span> |
| 解讀 | `#3498db` | <span style="color:#3498db">藍色</span> |
| 脂批 | `#9b59b6` | <span style="color:#9b59b6">紫色</span> |
| 備註 | `#27ae60` | <span style="color:#27ae60">綠色</span> |
| 校記 | `#e67e22` | <span style="color:#e67e22">橙色</span> |
| 解 | `#0437F2` | <span style="color:#0437F2">群青</span> |

---

## 三、文字方塊（Beamer 風格）

類似 LaTeX Beamer 簡報中的 block 環境，有彩色標題欄和淺色背景。

### 預設方塊（藍色）

<div class="block">
  <div class="block-title">方塊標題</div>
  <div class="block-body">這是方塊的內容。可以放入任何文字。</div>
</div>

```html
<div class="block">
  <div class="block-title">方塊標題</div>
  <div class="block-body">這是方塊的內容。</div>
</div>
```

### 顏色變體

加上 class 即可切換顏色：

<div class="block alert">
  <div class="block-title">重要提示（alert）</div>
  <div class="block-body">紅色方塊，適合標示重要事項。</div>
</div>

<div class="block example">
  <div class="block-title">範例（example）</div>
  <div class="block-body">綠色方塊，適合標示範例或正面內容。</div>
</div>

<div class="block warning">
  <div class="block-title">注意（warning）</div>
  <div class="block-body">橙色方塊，適合標示提醒。</div>
</div>

<div class="block purple">
  <div class="block-title">補充（purple）</div>
  <div class="block-body">紫色方塊，適合標示補充說明。</div>
</div>

```html
<div class="block alert">    <!-- 紅色 -->
<div class="block example">  <!-- 綠色 -->
<div class="block warning">  <!-- 橙色 -->
<div class="block purple">   <!-- 紫色 -->
```

---

## 四、詞語對應圖（Connection Diagram）

顯示兩個句子之間的詞語對應關係，自動以彩色線條連接。

### 直接對應

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

### 交叉對應

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

### 語法說明

```html
<div class="connection-diagram" data-pairs='[[0,1],[1,0],[2,2]]'>
  <div class="connection-row connection-row-top">
    <div class="word-box word-top" data-index="0">上方詞1</div>
    <div class="word-box word-top" data-index="1">上方詞2</div>
    <div class="word-box word-top" data-index="2">上方詞3</div>
  </div>
  <svg class="connection-lines"></svg>
  <div class="connection-row connection-row-bottom">
    <div class="word-box word-bottom" data-index="0">下方詞1</div>
    <div class="word-box word-bottom" data-index="1">下方詞2</div>
    <div class="word-box word-bottom" data-index="2">下方詞3</div>
  </div>
</div>
```

`data-pairs` 定義連線：`[上方索引, 下方索引]`，索引從 0 開始。每條連線自動分配不同顏色。

---

## 五、頁面基本架構

每個 `.md` 檔案需要以下結構：

```yaml
---
layout: default
title: 頁面標題
---
```

### 帶註腳的頁面模板

```liquid
{% raw %}---
layout: default
title: 頁面標題
---

{% capture main_text %}

# 標題

正文內容{% include fn.html label="注" color="#e74c3c" text="註解" %}。

* 列表項目
* 列表項目

## 小標題

更多內容{% include fn.html label="解讀" color="#3498db" text="解釋" %}。

{% endcapture %}

{% include annotated_text.html content=main_text %}

---{% endraw %}
```

### 純 Markdown 頁面（無註腳）

不需要 `capture` 區塊，直接寫 Markdown 即可：

```markdown
---
layout: default
title: 頁面標題
---

# 標題

正文內容。

* 項目一
* 項目二
```

---

## 六、DOCX 匯出

可將帶註腳的 Markdown 檔案轉換為直排中文 Word 文件：

```bash
# 轉換單一檔案
python scripts/md_to_docx.py pages/紅樓夢/紅樓夢1.md

# 轉換所有檔案
python scripts/md_to_docx.py --all pages output_docx
```

輸出的 DOCX 檔案特點：
* 直排文字方向（由上而下、由右而左）
* A4 橫向頁面
* 註腳自動轉換為 Word 腳註，保留顏色標籤

<script src="/assets/js/connection-diagram.js"></script>
