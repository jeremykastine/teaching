document.addEventListener('DOMContentLoaded', function () {
  var resetGestures = [];
  var activePointers = new Set();
  function resetAllGestures() {
    resetGestures.forEach(function (reset) { reset(); });
  }
  // Scrolling, pinching, and interrupted gestures must never count as taps.
  document.addEventListener('scroll', resetAllGestures, true);
  window.addEventListener('blur', function () {
    activePointers.clear();
    resetAllGestures();
  });
  if (window.PointerEvent) {
    document.addEventListener('pointerdown', function (event) {
      if (event.pointerType === 'mouse') return;
      activePointers.add(event.pointerId);
      if (activePointers.size > 1) resetAllGestures();
    }, true);
    ['pointerup', 'pointercancel'].forEach(function (type) {
      document.addEventListener(type, function (event) {
        activePointers.delete(event.pointerId);
      }, true);
    });
  } else {
    document.addEventListener('touchstart', function (event) {
      if (event.touches.length > 1) resetAllGestures();
    }, { passive: true, capture: true });
  }
  document.querySelectorAll('.worked-example').forEach(function (example, index) {
    var panel = example.querySelector('[data-solution-panel]');
    var problem = example.querySelector('.problem-statement');
    if (!panel || !problem) return;
    var number = index + 1;
    var problemLabel = document.createElement('p');
    problemLabel.className = 'example-label problem-label';
    problemLabel.innerHTML = '<strong>Problem ' + number + '</strong>';
    problem.insertBefore(problemLabel, problem.firstChild);
    var solutionLabel = document.createElement('p');
    solutionLabel.className = 'example-label solution-label';
    solutionLabel.innerHTML = '<strong>Solution ' + number + '</strong>';
    panel.insertBefore(solutionLabel, panel.firstChild);

    // A wrapper receives input while the color-concealed contents retain their
    // natural height, including after math rendering and responsive reflow.
    var area = document.createElement('div');
    area.className = 'solution-area';
    panel.parentNode.insertBefore(area, panel);
    area.appendChild(panel);
    panel.id = 'solution-' + number;
    area.tabIndex = 0;
    area.setAttribute('role', 'button');
    area.setAttribute('aria-controls', panel.id);
    area.setAttribute('aria-keyshortcuts', 'Enter Space');
    var visible = false;
    var start = null;
    var lastTap = null;
    var ignoreMouseUntil = 0;
    var tapInterval = 400;
    var moveTolerance = 12;
    var tapDistance = 32;
    function resetGesture() { start = null; lastTap = null; }
    resetGestures.push(resetGesture);
    function setVisible(value) {
      visible = value;
      panel.classList.toggle('solution-visible', visible);
      // Conceal only by color: text stays readable to extraction and assistive tools.
      panel.style.color = visible ? '' : '#ffffff';
      area.setAttribute('aria-expanded', String(visible));
      area.setAttribute('aria-label', (visible ? 'Hide' : 'Show') + ' solution to Problem ' + number);
    }
    function beginTap(point, id) {
      ignoreMouseUntil = Date.now() + 800;
      start = { x: point.clientX, y: point.clientY, id: id, time: Date.now() };
    }
    function moveTap(point) {
      if (start && Math.hypot(point.clientX - start.x, point.clientY - start.y) > moveTolerance) resetGesture();
    }
    function finishTap(point, id) {
      ignoreMouseUntil = Date.now() + 800;
      if (!start || start.id !== id) return;
      moveTap(point);
      if (!start) return;
      var now = Date.now();
      var bounds = area.getBoundingClientRect();
      if (now - start.time > tapInterval || point.clientX < bounds.left || point.clientX > bounds.right ||
          point.clientY < bounds.top || point.clientY > bounds.bottom) {
        resetGesture();
        return;
      }
      if (lastTap && now - lastTap.time <= tapInterval &&
          Math.hypot(point.clientX - lastTap.x, point.clientY - lastTap.y) <= tapDistance) {
        setVisible(!visible);
        resetGesture();
      } else {
        lastTap = { x: point.clientX, y: point.clientY, time: now };
        start = null;
      }
    }
    area.addEventListener('dblclick', function (event) {
      // Touch browsers can also synthesize dblclick; avoid a second toggle.
      if (Date.now() < ignoreMouseUntil || (event.sourceCapabilities && event.sourceCapabilities.firesTouchEvents)) return;
      event.preventDefault();
      resetGesture();
      setVisible(!visible);
    });
    area.addEventListener('keydown', function (event) {
      if (event.target !== area || (event.key !== 'Enter' && event.key !== ' ')) return;
      event.preventDefault();
      if (!event.repeat) { resetGesture(); setVisible(!visible); }
    });
    // Assistive technology activates custom buttons with a detail-zero click.
    area.addEventListener('click', function (event) {
      if (event.detail === 0) { resetGesture(); setVisible(!visible); }
    });
    if (window.PointerEvent) {
      area.addEventListener('pointerdown', function (event) {
        if (event.pointerType === 'mouse') { ignoreMouseUntil = 0; resetGesture(); return; }
        if (!event.isPrimary || activePointers.size > 1) { resetGesture(); return; }
        beginTap(event, event.pointerId);
      });
      area.addEventListener('pointermove', function (event) {
        if (start && start.id === event.pointerId) moveTap(event);
      });
      area.addEventListener('pointerup', function (event) {
        if (event.pointerType !== 'mouse') finishTap(event, event.pointerId);
      });
      area.addEventListener('pointercancel', resetGesture);
    } else {
      // Older touch browsers without Pointer Events use the same tap rules.
      area.addEventListener('touchstart', function (event) {
        if (event.touches.length !== 1) { resetGesture(); return; }
        beginTap(event.touches[0], event.touches[0].identifier);
      }, { passive: true });
      area.addEventListener('touchmove', function (event) {
        if (event.touches.length === 1) moveTap(event.touches[0]);
        else resetGesture();
      }, { passive: true });
      area.addEventListener('touchend', function (event) {
        if (event.touches.length === 0 && event.changedTouches.length === 1) finishTap(event.changedTouches[0], event.changedTouches[0].identifier);
        else resetGesture();
      }, { passive: true });
      area.addEventListener('touchcancel', resetGesture);
    }
    setVisible(false);
  });
});
