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
\begin{tikzpicture}[roundnode/.style={circle, draw=black!60, fill=white!5, very thick, minimum size=15mm},squarednode/.style={rectangle, draw=blue!60, fill=blue!5, very thick, minimum size=20mm},
]
%Nodes
\node[squarednode]  (1u) {w};
\node[squarednode]  (2u) [right=of 1u] {w};
\node[squarednode]  (3u) [right=of 2u] {w};
\node[squarednode]  (4u) [right=of 3u] {w};

\node[roundnode]  (1b) [below=of 1u] {w};
\node[roundnode]  (2b) [below=of 2u] {w};
\node[roundnode]  (3b) [below=of 3u] {u};
\node[roundnode]  (4b) [below=of 4u] {w};

%Lines
% \draw[dashed, ->] (1u.south) .. controls +(right:7mm) and +(up:7mm) .. (1b.north);
\draw[dashed, ->] (2u.south) -- (2b.north);
% \draw[dashed, ->] (lowercircle.east) .. controls +(right:7mm) and +(down:7mm) .. (rightsquare.south);
% \draw[->] (uppercircle.south) -- (maintopic.north);
% \draw[->] (maintopic.south) -- (lowercircle.north);
% \draw[dashed, ->] (uppercircle.west) .. controls +(left:20mm) and +(left:20mm) .. (lowercircle.west);
% \draw[dashed, ->] (maintopic.west) .. controls +(left:10mm) and +(left:10mm) .. (lowercircle.west);
\end{tikzpicture}
</script>

html
 <html>
  <head>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['sankey']});
      google.charts.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'From');
        data.addColumn('string', 'To');
        data.addColumn('number', 'Weight');
        data.addRows([
          [ 'A', 'B', 1 ],
          [ 'C', 'D', 1 ],
          [ 'E', 'F', 1 ],
          [ 'G', 'H', 1 ],
          [ 'I', 'K', 1 ],
          [ 'L', 'M', 1 ]
        ]);
        // Sets chart options.
        var options = {
          width: 500,
        };
        // Instantiates and draws our chart, passing in some options.
        var chart = new google.visualization.Sankey(document.getElementById('sankey_basic'));
        chart.draw(data, options);
      }
    </script>
  </head>
  <body>
    <div id="sankey_basic" style="width: 700px; height: 900px;"></div>
  </body>
</html>


span class="inline-latex">{% latex latex %}\LaTeX{% endlatex %}</span>

[Link to another page](./pages/bhbaihua/rumen.html).
