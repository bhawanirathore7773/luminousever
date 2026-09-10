/* ==========================================================================
   LUMINOUS EVER — MOTION LAYER
   Lenis (smooth scroll) + GSAP/ScrollTrigger (reveals, counters, magnetic
   CTA). Every effect checks prefers-reduced-motion first, and every path
   has a fallback that leaves content visible if a CDN script fails —
   motion should never be the reason content doesn't render.
   ========================================================================== */

(function () {
  "use strict";

  const prefersReduced = window.matchMedia(
    "(prefers-reduced-motion: reduce)"
  ).matches;

  /* ---- Smooth scroll (Lenis) ---- */
  let lenis = null;
  if (!prefersReduced && window.Lenis) {
    lenis = new Lenis({
      duration: 1.1,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
    });

    const raf = (time) => {
      lenis.raf(time);
      requestAnimationFrame(raf);
    };
    requestAnimationFrame(raf);

    if (window.gsap && window.ScrollTrigger) {
      lenis.on("scroll", ScrollTrigger.update);
      gsap.ticker.add((time) => lenis.raf(time * 1000));
      gsap.ticker.lagSmoothing(0);
    }
  }

  const hasGsap = Boolean(window.gsap && window.ScrollTrigger);
  if (hasGsap) {
    gsap.registerPlugin(ScrollTrigger);
  }

  /* ---- Scroll reveals: [data-reveal], optional [data-reveal-delay] (ms) ---- */
  document.querySelectorAll("[data-reveal]").forEach((el) => {
    if (prefersReduced || !hasGsap) {
      el.style.opacity = "1";
      el.style.transform = "none";
      return;
    }
    const delay = Number(el.getAttribute("data-reveal-delay") || 0) / 1000;
    gsap.set(el, { opacity: 0, y: 24 });
    gsap.to(el, {
      opacity: 1,
      y: 0,
      duration: 0.9,
      delay,
      ease: "expo.out",
      scrollTrigger: { trigger: el, start: "top 85%", once: true },
    });
  });

  /* ---- Count-up: <span data-counter data-counter-to="50" data-counter-suffix="+"> ---- */
  document.querySelectorAll("[data-counter]").forEach((el) => {
    const to = parseFloat(el.getAttribute("data-counter-to") || "0");
    const suffix = el.getAttribute("data-counter-suffix") || "";
    const decimals = Number(el.getAttribute("data-counter-decimals") || 0);

    if (prefersReduced || !hasGsap) {
      el.textContent = to.toFixed(decimals) + suffix;
      return;
    }

    const counterState = { val: 0 };
    gsap.to(counterState, {
      val: to,
      duration: 1.6,
      ease: "expo.out",
      onUpdate: () => {
        el.textContent = counterState.val.toFixed(decimals) + suffix;
      },
      scrollTrigger: { trigger: el, start: "top 90%", once: true },
    });
  });

  /* ---- CTA buttons: fixed position, no cursor movement, no zoom ---- */
  const isTouch = window.matchMedia("(pointer: coarse)").matches;
  if (!prefersReduced && !isTouch && window.gsap) {
    document.querySelectorAll("[data-magnetic]").forEach((el) => {
      gsap.set(el, { x: 0, y: 0, scale: 1 });
    });
  }

  /* ---- Hero visual: locked position + smooth 3D hover zoom ---- */
  const heroVisual = document.querySelector("[data-hero-visual]");
  if (heroVisual && !prefersReduced && !isTouch && window.gsap) {
    const nodes = heroVisual.querySelectorAll("[data-hero-node]");

    // Use xPercent/yPercent for the permanent centering transform.
    // This prevents GSAP's pixel transforms from fighting the CSS
    // translate(-50%, -50%) and makes the node stay exactly in place.
    nodes.forEach((node) => {
      const getScale = () => {
        if (node.classList.contains("hero-node--center")) {
          return node.classList.contains("is-hub-flow-active") ? 1.04 : 1;
        }
        return node.classList.contains("is-flow-active") ? 1.08 : 1;
      };

      gsap.set(node, {
        xPercent: -50,
        yPercent: -50,
        x: 0,
        y: 0,
        scale: getScale(),
        rotationX: 0,
        rotationY: 0,
        transformPerspective: 1000,
        transformOrigin: "50% 50%",
        force3D: true,
      });

      node.addEventListener("mouseenter", () => {
        gsap.to(node, {
          x: 0,
          y: 0,
          scale: getScale() * 1.045,
          duration: 0.48,
          ease: "power3.out",
          overwrite: true,
        });
      });

      node.addEventListener("mousemove", (e) => {
        const rect = node.getBoundingClientRect();
        const px = (e.clientX - rect.left) / rect.width - 0.5;
        const py = (e.clientY - rect.top) / rect.height - 0.5;

        gsap.to(node, {
          x: 0,
          y: 0,
          scale: getScale() * 1.045,
          rotationY: px * 7,
          rotationX: py * -7,
          duration: 0.5,
          ease: "power3.out",
          overwrite: true,
        });
      });

      node.addEventListener("mouseleave", () => {
        gsap.to(node, {
          x: 0,
          y: 0,
          scale: getScale(),
          rotationX: 0,
          rotationY: 0,
          duration: 0.6,
          ease: "power3.out",
          overwrite: true,
        });
      });
    });
  }

  /* ---- Header: transparent -> solid on scroll. Phase 3 adds the markup;
     this listener is a no-op until [data-site-header] exists in the DOM.
     Hooks into lenis.on('scroll') directly when Lenis is active, rather
     than only the native window scroll event — the scroll position Lenis
     animates toward and the native event timing aren't guaranteed to be
     perfectly in sync on every browser, so this removes that ambiguity
     rather than assuming they always match. ---- */
  const header = document.querySelector("[data-site-header]");
  if (header) {
    const toggleHeaderState = (scrollY) => {
      header.classList.toggle("is-scrolled", scrollY > 40);
    };
    toggleHeaderState(window.scrollY);
    if (lenis) {
      lenis.on("scroll", (e) => toggleHeaderState(e.scroll));
    } else {
      window.addEventListener("scroll", () => toggleHeaderState(window.scrollY), { passive: true });
    }
  }

  /* ---- Inline form validation: <form data-validate> wrapping .field blocks ---- */
  document.querySelectorAll("[data-validate]").forEach((form) => {
    form.querySelectorAll(".field").forEach((field) => {
      const input = field.querySelector("input, textarea, select");
      if (!input) return;
      input.addEventListener("blur", () => {
        if (input.value === "") {
          field.classList.remove("has-error", "has-success");
          return;
        }
        field.classList.toggle("has-error", !input.checkValidity());
        field.classList.toggle("has-success", input.checkValidity());
      });
    });
  });

  /* ---- Touch-friendly mega-menu (Phase 13) ---- */
  const isCoarsePointer = window.matchMedia("(hover: none), (pointer: coarse)").matches;
  const megaMenuTriggers = document.querySelectorAll(".nav-item--has-menu > a");
  if (isCoarsePointer && megaMenuTriggers.length) {
    megaMenuTriggers.forEach((trigger) => {
      trigger.addEventListener("click", (e) => {
        const parent = trigger.closest(".nav-item--has-menu");
        if (!parent.classList.contains("is-menu-open")) {
          e.preventDefault();
          document.querySelectorAll(".nav-item--has-menu.is-menu-open").forEach((el) => {
            el.classList.remove("is-menu-open");
          });
          parent.classList.add("is-menu-open");
        }
      });
    });
    document.addEventListener("click", (e) => {
      if (!e.target.closest(".nav-item--has-menu")) {
        document.querySelectorAll(".nav-item--has-menu.is-menu-open").forEach((el) => {
          el.classList.remove("is-menu-open");
        });
      }
    });
  }

  /* ---- Mobile full-screen nav ---- */
  const mobileNavToggles = document.querySelectorAll("[data-mobile-nav-toggle]");
  const mobileNav = document.querySelector("[data-mobile-nav]");
  if (mobileNavToggles.length && mobileNav) {
    const setOpen = (open) => {
      document.body.classList.toggle("mobile-nav-open", open);
      mobileNavToggles.forEach((btn) => btn.setAttribute("aria-expanded", String(open)));
    };
    mobileNavToggles.forEach((btn) => {
      btn.addEventListener("click", () => {
        setOpen(!document.body.classList.contains("mobile-nav-open"));
      });
    });
    mobileNav.querySelectorAll("a").forEach((link) => link.addEventListener("click", () => setOpen(false)));
    window.addEventListener("keydown", (e) => {
      if (e.key === "Escape") setOpen(false);
    });
  }

  /* ---- Portfolio filter tabs ---- */
  const filterTabsWrap = document.querySelector("[data-filter-tabs]");
  if (filterTabsWrap) {
    const tabs = filterTabsWrap.querySelectorAll("[data-filter-tab]");
    const items = document.querySelectorAll("[data-filter-item]");
    tabs.forEach((tab) => {
      tab.addEventListener("click", () => {
        const target = tab.getAttribute("data-filter-tab");
        tabs.forEach((t) => t.classList.toggle("is-active", t === tab));
        items.forEach((item) => {
          const matches = target === "all" || item.getAttribute("data-filter-item") === target;
          item.hidden = !matches;
        });
      });
    });
  }

  /* ---- Newsletter form ---- */
  const newsletterForm = document.querySelector("[data-newsletter-form]");
  if (newsletterForm) {
    const note = newsletterForm.parentElement.querySelector("[data-newsletter-note]");
    newsletterForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const input = newsletterForm.querySelector('input[type="email"]');
      if (!note) return;
      if (input && input.checkValidity()) {
        note.textContent = "Thanks — newsletter signups open soon.";
        newsletterForm.reset();
      } else {
        note.textContent = "Enter a valid email address.";
      }
    });
  }
})();
