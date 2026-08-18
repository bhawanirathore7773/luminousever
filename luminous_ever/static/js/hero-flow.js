/* Luminous Ever — Hero Flow */
(() => {
  "use strict";

  function initHeroFlow() {
    const visual = document.querySelector("[data-hero-visual]");
    if (!visual) return;

    const nodes = [...visual.querySelectorAll("[data-hero-node][data-flow]")]
      .sort((a, b) => Number(a.dataset.flow) - Number(b.dataset.flow));

    const lines = [...visual.querySelectorAll(".hero__svg-lines line")];
    const center = visual.querySelector(".hero-node--center");

    if (!nodes.length) return;

    // Prevent duplicate initialization.
    if (visual.dataset.heroFlowReady === "1") return;
    visual.dataset.heroFlowReady = "1";

    let current = 0;
    let intervalId = null;

    function clearState() {
      nodes.forEach(node => {
        node.classList.remove("is-flow-active");
      });

      lines.forEach(line => {
        line.classList.remove("is-flow-active");
      });

      if (center) {
        center.classList.remove("is-hub-flow-active");
      }
    }

    function activateStep() {
      clearState();

      const node = nodes[current];
      const line = lines[current];

      if (node) {
        node.classList.add("is-flow-active");
      }

      if (line) {
        line.classList.add("is-flow-active");
      }

      if (center) {
        // Restart center hub animation cleanly.
        void center.offsetWidth;
        center.classList.add("is-hub-flow-active");
      }

      current = (current + 1) % nodes.length;
    }

    function start() {
      stop();

      // Activate first step immediately.
      activateStep();

      // Respect reduced-motion preference.
      if (
        window.matchMedia("(prefers-reduced-motion: reduce)").matches
      ) {
        return;
      }

      // Move to the next node every 900ms.
      intervalId = window.setInterval(activateStep, 900);
    }

    function stop() {
      if (intervalId !== null) {
        window.clearInterval(intervalId);
        intervalId = null;
      }
    }

    // Pause animation when browser tab is hidden.
    document.addEventListener("visibilitychange", () => {
      if (document.hidden) {
        stop();
      } else {
        start();
      }
    });

    start();
  }

  // Initialize after DOM is ready.
  if (document.readyState === "loading") {
    document.addEventListener(
      "DOMContentLoaded",
      initHeroFlow,
      { once: true }
    );
  } else {
    initHeroFlow();
  }
})();