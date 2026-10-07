window.MathJax = {
  tex: {
    inlineMath: [['\\(', '\\)']],
    displayMath: [['\\[', '\\]']]
  },
  output: {
    displayOverflow: 'linebreak',
    linebreaks: { inline: true, width: '100%', lineleading: 0.2 }
  },
  options: {
    skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
  },
  startup: {
    pageReady: function () {
      return MathJax.startup.defaultPageReady().then(function () {
        var main = document.querySelector('main');
        if (!main) return;
        function contentWidth() {
          var style = getComputedStyle(main);
          return main.clientWidth - parseFloat(style.paddingLeft) - parseFloat(style.paddingRight);
        }
        var width = contentWidth();
        var timer;
        window.addEventListener('resize', function () {
          clearTimeout(timer);
          timer = setTimeout(function () {
            var nextWidth = contentWidth();
            if (nextWidth === width) return;
            width = nextWidth;
            // Recompute container metrics as well as line breaks after rotation
            // or resizing. Rerendering from METRICS preserves the compiled math.
            MathJax.startup.document.rerenderPromise(MathJax._.core.MathItem.STATE.METRICS)
              .catch(function (error) { console.error('Math layout failed:', error); });
          }, 150);
        });
      });
    }
  }
};
