---
layout: default
---
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
          width: 600,
        };

        // Instantiates and draws our chart, passing in some options.
        var chart = new google.visualization.Sankey(document.getElementById('sankey_basic'));
        chart.draw(data, options);
      }
    </script>
  </head>
  <body>
    <div id="sankey_basic" style="width: 900px; height: 300px;"></div>
  </body>
</html

1 1

[Link to another page](./pages/bhbaihua/rumen.html).
