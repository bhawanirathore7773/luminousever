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

  /* ---- Magnetic CTA: [data-magnetic] — desktop pointer only ---- */
  const isTouch = window.matchMedia("(pointer: coarse)").matches;
  if (!prefersReduced && !isTouch && window.gsap) {
    document.querySelectorAll("[data-magnetic]").forEach((el) => {
      const strength = 0.35;
      el.addEventListener("mousemove", (e) => {
        const rect = el.getBoundingClientRect();
        const x = e.clientX - rect.left - rect.width / 2;
        const y = e.clientY - rect.top - rect.height / 2;
        gsap.to(el, { x: x * strength, y: y * strength, duration: 0.4, ease: "expo.out" });
      });
      el.addEventListener("mouseleave", () => {
        gsap.to(el, { x: 0, y: 0, duration: 0.6, ease: "elastic.out(1, 0.4)" });
      });
    });
  }

  /* ---- Hero visual: subtle cursor parallax on the network nodes ---- */
  const heroVisual = document.querySelector("[data-hero-visual]");
  if (heroVisual && !prefersReduced && !isTouch && window.gsap) {
    const nodes = heroVisual.querySelectorAll("[data-hero-node]");
    heroVisual.addEventListener("mousemove", (e) => {
      const rect = heroVisual.getBoundingClientRect();
      const px = (e.clientX - rect.left) / rect.width - 0.5;
      const py = (e.clientY - rect.top) / rect.height - 0.5;
      nodes.forEach((node, i) => {
        const depth = 8 + (i % 3) * 5;
        gsap.to(node, { x: px * depth, y: py * depth, duration: 0.6, ease: "power2.out" });
      });
    });
    heroVisual.addEventListener("mouseleave", () => {
      nodes.forEach((node) => gsap.to(node, { x: 0, y: 0, duration: 0.8, ease: "elastic.out(1, 0.5)" }));
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

  /* ---- Touch-friendly mega-menu (Phase 13) ----
     :hover doesn't fire reliably on touch. On coarse-pointer/no-hover
     devices, the first tap on a mega-menu trigger opens the menu instead
     of navigating away; a second tap (menu already open) follows the
     link normally. Only affects touch-capable devices at desktop-nav
     widths (≥1080px) — narrow but real (touch laptops, large tablets). */
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

  /* ---- Mobile full-screen nav: [data-mobile-nav-toggle] + [data-mobile-nav] ---- */
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

  /* ---- Portfolio filter tabs: [data-filter-tabs] + [data-filter-item] ---- */
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

  /* ---- Newsletter form ----
     Client-side only for now — the real subscribe endpoint is wired up
     when the leads app lands in Phase 9. Always give feedback either way
     rather than letting the submit silently do nothing. */
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
