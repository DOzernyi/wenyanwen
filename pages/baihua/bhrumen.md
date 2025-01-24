---
layout: default
---

<head>
  <!-- ... -->

  <link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/earlyaccess/cwtexkai.css">
  <style>
    body {
     font-family: "cwTeXKai", serif;
    }

    p.big {
      line-height: 1.8;
    }
    </style>
</head>


鳥鳴於樹上。兒以石擊之。父曰：「何以擊鳥？」兒曰：「人言：『鵲之鳴吉，鴉之鳴凶。』今鳴者，鴉也。以故擊之。」父曰：「人之智高於鳥之智。人不能知吉凶。鳥何以能知之？」


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
         [ '鳥', '鳥', 1 ],
         [ '鳴', '叫', 1 ],
         [ '於', '在', 1 ],
         [ '樹', '樹', 1 ],
         [ '上', '上', 1 ],
         [ '。', '。', 1 ]
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


[back](./)
