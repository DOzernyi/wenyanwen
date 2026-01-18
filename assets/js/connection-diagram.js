document.addEventListener('DOMContentLoaded', function() {
  const diagrams = document.querySelectorAll('.connection-diagram');
  
  diagrams.forEach(function(diagram) {
    drawConnections(diagram);
  });
  
  window.addEventListener('resize', function() {
    diagrams.forEach(function(diagram) {
      drawConnections(diagram);
    });
  });
});

function drawConnections(diagram) {
  const svg = diagram.querySelector('.connection-lines');
  const pairsData = diagram.dataset.pairs;
  
  if (!svg || !pairsData) return;
  
  let pairs;
  try {
    pairs = JSON.parse(pairsData);
  } catch (e) {
    console.error('Invalid pairs data:', e);
    return;
  }
  
  svg.innerHTML = '';
  
  const topRow = diagram.querySelector('.connection-row-top');
  const bottomRow = diagram.querySelector('.connection-row-bottom');
  const topWords = diagram.querySelectorAll('.word-top');
  const bottomWords = diagram.querySelectorAll('.word-bottom');
  
  if (!topRow || !bottomRow || topWords.length === 0 || bottomWords.length === 0) return;
  
  const diagramRect = diagram.getBoundingClientRect();
  const topRowRect = topRow.getBoundingClientRect();
  const bottomRowRect = bottomRow.getBoundingClientRect();
  
  const svgTop = topRowRect.bottom - diagramRect.top;
  const svgBottom = bottomRowRect.top - diagramRect.top;
  const svgHeight = svgBottom - svgTop;
  
  svg.style.position = 'absolute';
  svg.style.top = svgTop + 'px';
  svg.style.left = '0';
  svg.style.width = '100%';
  svg.style.height = svgHeight + 'px';
  diagram.style.position = 'relative';
  
  if (pairs.length > 1) {
    diagram.setAttribute('data-color-mode', 'true');
  }
  
  pairs.forEach(function(pair, index) {
    const topIndex = pair[0];
    const bottomIndex = pair[1];
    
    const topWord = topWords[topIndex];
    const bottomWord = bottomWords[bottomIndex];
    
    if (!topWord || !bottomWord) return;
    
    const topWordRect = topWord.getBoundingClientRect();
    const bottomWordRect = bottomWord.getBoundingClientRect();
    
    const x1 = topWordRect.left + topWordRect.width / 2 - diagramRect.left;
    const y1 = 0;
    const x2 = bottomWordRect.left + bottomWordRect.width / 2 - diagramRect.left;
    const y2 = svgHeight;
    
    const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
    line.setAttribute('x1', x1);
    line.setAttribute('y1', y1);
    line.setAttribute('x2', x2);
    line.setAttribute('y2', y2);
    line.setAttribute('class', 'pair-line pair-line-' + (index % 8));
    
    if (pair[2]) {
      line.setAttribute('stroke', pair[2]);
    }
    
    svg.appendChild(line);
  });
}
