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
         [ '鳥', '(一隻)鳥', 1 ],
         [ '鳴', '叫', 1 ],
         [ '於', '在', 1 ],
         [ '樹', '樹 ', 1 ],
         [ '上', '上 ', 1 ],
         [ '-', '- ', 1 ]
       ]);
       // Sets chart options.
       var options = {
         width: 250,
       };
       // Instantiates and draws our chart, passing in some options.
       var chart = new google.visualization.Sankey(document.getElementById('sankey_basic'));
       chart.draw(data, options);
     }
   </script>
 </head>
 <body>
   <div id="sankey_basic" style="width: 300px; height: 250px;"></div>
 </body>
</html>


123

<html>
  <head>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {packages:["orgchart"]});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Name');
        data.addColumn('string', 'Manager');
        data.addColumn('string', 'ToolTip');

        // For each orgchart box, provide the name, manager, and tooltip to show.
        data.addRows([
          ['w1', 'w1 ', ''],
          ['w2', 'w2 ', ''],
          ['w3', 'w3 ', ''],
          ['w4', 'w4 ', ''],
          ['w5', 'w2 ', ''],
        ]);

        // Create the chart.
        var chart = new google.visualization.OrgChart(document.getElementById('chart_div'));
        // Draw the chart, setting the allowHtml option to true for the tooltips.
        chart.draw(data, {'allowHtml':true});
      }
   </script>
    </head>
  <body>
    <div id="chart_div"></div>
  </body>
</html>


[back](./)
