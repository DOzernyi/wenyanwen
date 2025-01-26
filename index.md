---
layout: default
---

<head>
  <!-- ... -->
  <link rel="stylesheet" type="text/css" href="https://tikzjax.com/v1/fonts.css">
  <script src="https://tikzjax.com/v1/tikzjax.js"></script>
  <link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/earlyaccess/cwtexkai.css">
  <style>
    body {
     font-family: "cwTeXKai", serif;
    }

    p.big {
      line-height: 3;
      font-size: x-large;
    }
    p {
      font-size: 1.5em;
    }
    </style>

</head>

鳥鳴於樹上。兒以石擊之。父曰：「何以擊鳥？」兒曰：「人言：『鵲之鳴吉，鴉之鳴凶。』今鳴者，鴉也。以故擊之。」父曰：「人之智高於鳥之智。人不能知吉凶。鳥何以能知之？」




<script type="text/tikz">
\usepackage{xeCJK}

\begin{tikzpicture}[
roundnode/.style={circle, draw=black!60, fill=white!5, thick, minimum size=10mm},
squarednode/.style={rectangle, draw=blue!60, fill=blue!5, thick, minimum size=10mm},
]
\Large
\node[squarednode]  (1u) {w};
\node[squarednode]  (2u) [right=of 1u] {歐};
\node[squarednode]  (3u) [right=of 2u] {w};
\node[squarednode]  (4u) [right=of 3u] {w};
\node[squarednode]  (5u) [right=of 4u] {w};
\node[squarednode]  (6u) [right=of 5u] {w};
\node[squarednode]  (7u) [right=of 6u] {w};
\node[squarednode]  (8u) [right=of 7u] {w};
\node[squarednode]  (9u) [right=of 8u] {w};
\node[squarednode]  (10u) [right=of 9u] {w};

\node[roundnode]  (1b) [below=of 1u] {w};
\node[roundnode]  (2b) [below=of 2u] {w};
\node[roundnode]  (3b) [below=of 3u] {u};
\node[roundnode]  (4b) [below=of 4u] {w};
\node[roundnode]  (5b) [below=of 5u] {w};
\node[roundnode]  (6b) [below=of 6u] {w};
\node[roundnode]  (7b) [below=of 7u] {w};
\node[roundnode]  (8b) [below=of 8u] {w};
\node[roundnode]  (9b) [below=of 9u] {w};
\node[roundnode]  (10b) [below=of 10u] {w};

%Lines
\draw[dashed, ->] (1u.south) -- (1b.north);
\draw[dashed, ->] (2u.south) -- (2b.north);
\draw[dashed, ->] (3u.south) -- (3b.north);
\draw[dashed, ->] (4u.south) -- (4b.north);
\draw[dashed, ->] (5u.south) -- (5b.north);
\draw[dashed, ->] (6u.south) -- (6b.north);
\draw[dashed, ->] (7u.south) -- (7b.north);
\draw[dashed, ->] (8u.south) -- (8b.north);
\draw[dashed, ->] (9u.south) -- (9b.north);
\draw[dashed, ->] (10u.south) -- (10b.north);
\end{tikzpicture}
</script>

[Link to another page](./pages/bhbaihua/rumen.html).
