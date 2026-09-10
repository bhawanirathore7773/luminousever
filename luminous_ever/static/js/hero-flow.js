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

    // Keep CTA buttons fixed in place. The existing magnetic CTA effect
    // moves elements toward the cursor; override it on the next animation
    // frame so event-listener order cannot cause the button to drift.
    if (window.gsap && !window.matchMedia("(pointer: coarse)").matches) {
      document.querySelectorAll("[data-magnetic]").forEach((el) => {
        el.addEventListener("mousemove", () => {
          window.requestAnimationFrame(() => {
            window.gsap.killTweensOf(el);
            window.gsap.to(el, {
              x: 0,
              y: 0,
              scale: 1.04,
              duration: 0.22,
              ease: "power2.out",
              overwrite: true,
            });
          });
        });

        el.addEventListener("mouseleave", () => {
          window.requestAnimationFrame(() => {
            window.gsap.killTweensOf(el);
            window.gsap.to(el, {
              x: 0,
              y: 0,
              scale: 1,
              duration: 0.28,
              ease: "power2.out",
              overwrite: true,
            });
          });
        });
      });
    }

    /*
     * Center hub hover: keep its percentage-based anchor completely
     * separate from GSAP's x/y transform system. The old generic node
     * handler could overwrite translate(-50%, -50%) and make the hub
     * appear to jump sideways/down when the cursor entered it.
     *
     * The center now uses CSS custom properties for scale/tilt while the
     * actual transform always contains the original centering translate.
     */
    if (center && window.gsap && !window.matchMedia("(pointer: coarse)").matches) {
      const applyCenterTransform = () => {
        center.style.setProperty(
          "transform",
          "perspective(900px) translate(-50%, -50%) scale(var(--hero-center-scale, 1)) rotateX(var(--hero-center-rx, 0deg)) rotateY(var(--hero-center-ry, 0deg))",
          "important"
        );
      };

      applyCenterTransform();
      center.style.setProperty("--hero-center-scale", "1");
      center.style.setProperty("--hero-center-rx", "0deg");
      center.style.setProperty("--hero-center-ry", "0deg");
      center.style.setProperty("transform-style", "preserve-3d");
      center.style.setProperty("will-change", "transform");

      center.addEventListener("mousemove", (e) => {
        e.stopImmediatePropagation();

        const rect = center.getBoundingClientRect();
        const px = (e.clientX - rect.left) / rect.width - 0.5;
        const py = (e.clientY - rect.top) / rect.height - 0.5;

        window.gsap.to(center, {
          "--hero-center-scale": 1.07,
          "--hero-center-rx": `${py * -5}deg`,
          "--hero-center-ry": `${px * 5}deg`,
          duration: 0.32,
          ease: "power3.out",
          overwrite: true,
        });
      }, true);

      center.addEventListener("mouseleave", (e) => {
        e.stopImmediatePropagation();

        window.gsap.to(center, {
          "--hero-center-scale": 1,
          "--hero-center-rx": "0deg",
          "--hero-center-ry": "0deg",
          duration: 0.5,
          ease: "power3.out",
          overwrite: true,
        });
      }, true);
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