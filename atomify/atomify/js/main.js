/* Kairos — interações (JS puro, sem dependências) */
(function () {
  "use strict";

  var $ = function (s, ctx) { return (ctx || document).querySelector(s); };
  var $$ = function (s, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(s)); };

  /* ---------- toast ---------- */
  var toastEl, toastTimer;
  function toast(msg) {
    if (!toastEl) {
      toastEl = document.createElement("div");
      toastEl.className = "toast";
      toastEl.setAttribute("role", "status");
      toastEl.setAttribute("aria-live", "polite");
      document.body.appendChild(toastEl);
    }
    toastEl.textContent = msg;
    toastEl.classList.add("show");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { toastEl.classList.remove("show"); }, 2800);
  }
  window.kairosToast = toast;

  /* ---------- navbar: menu mobile + dropdowns ---------- */
  $$(".nav").forEach(function (nav) {
    var burger = $(".nav__burger", nav);
    var items = $$(".nav__item", nav);

    function closeItems(except) {
      items.forEach(function (it) {
        if (it !== except) {
          it.classList.remove("open");
          var t = $(".nav__trigger", it);
          if (t) t.setAttribute("aria-expanded", "false");
        }
      });
    }

    if (burger) {
      burger.addEventListener("click", function () {
        var open = nav.classList.toggle("open");
        burger.setAttribute("aria-expanded", String(open));
        if (!open) closeItems();
      });
    }

    items.forEach(function (it) {
      var trigger = $(".nav__trigger", it);
      if (!trigger) return;
      trigger.addEventListener("click", function (e) {
        e.stopPropagation();
        var open = !it.classList.contains("open");
        closeItems(it);
        it.classList.toggle("open", open);
        trigger.setAttribute("aria-expanded", String(open));
      });
    });

    document.addEventListener("click", function (e) {
      if (!nav.contains(e.target)) {
        closeItems();
        if (nav.classList.contains("open")) {
          nav.classList.remove("open");
          if (burger) burger.setAttribute("aria-expanded", "false");
        }
      }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") {
        closeItems();
        nav.classList.remove("open");
        if (burger) burger.setAttribute("aria-expanded", "false");
      }
    });
  });

  /* ---------- FAQ (acordeão) ---------- */
  $$(".faq__item").forEach(function (item) {
    var btn = $(".faq__q", item);
    btn.addEventListener("click", function () {
      var open = !item.classList.contains("open");
      item.classList.toggle("open", open);
      btn.setAttribute("aria-expanded", String(open));
    });
  });

  /* ---------- tabs do dashboard ---------- */
  $$(".dash__tabs").forEach(function (tabs) {
    $$(".dash__tab", tabs).forEach(function (t) {
      t.addEventListener("click", function () {
        $$(".dash__tab", tabs).forEach(function (x) { x.classList.remove("on"); });
        t.classList.add("on");
      });
    });
  });

  /* ---------- escala do mockup de app (hero) ---------- */
  var scalers = $$(".app-frame__scale");
  function rescale() {
    scalers.forEach(function (el) {
      var frame = el.parentElement;
      var w = frame.clientWidth;
      var s = w / 713.338;
      el.style.transform = "scale(" + s + ")";
    });
  }
  if (scalers.length) {
    rescale();
    if ("ResizeObserver" in window) {
      var ro = new ResizeObserver(rescale);
      scalers.forEach(function (el) { ro.observe(el.parentElement); });
    } else {
      window.addEventListener("resize", rescale);
    }
  }
  /* no hero em telas pequenas, a altura do app acompanha a escala */
  function fitAppHeight() {
    $$(".app-frame[data-fit]").forEach(function (frame) {
      var s = frame.clientWidth / 713.338;
      frame.style.height = Math.round(383 * s + 4) + "px";
    });
  }
  if ($$(".app-frame[data-fit]").length) {
    fitAppHeight();
    window.addEventListener("resize", fitAppHeight);
  }

  /* ---------- estrelas do footer ---------- */
  $$(".stars").forEach(function (box) {
    var seed = 7;
    function rnd() { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; }
    var frag = document.createDocumentFragment();
    for (var i = 0; i < 90; i++) {
      var s = document.createElement("i");
      var size = rnd() < 0.18 ? 2.4 : 1.2;
      var top = Math.pow(rnd(), 1.4) * 82;
      s.style.cssText = "left:" + (rnd() * 100).toFixed(2) + "%;top:" + top.toFixed(2) + "%;width:" + size + "px;height:" + size + "px;opacity:" + (0.25 + rnd() * 0.6).toFixed(2);
      frag.appendChild(s);
    }
    box.appendChild(frag);
  });

  /* ---------- formulário de contato ---------- */
  var form = $("#contact-form");
  if (form) {
    var emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
    function validate(field) {
      var input = $("input, textarea, select", field);
      var v = input.value.trim();
      var ok = true;
      var msg = "";
      if (input.required && !v) { ok = false; msg = "Campo obrigatório."; }
      else if (input.type === "email" && v && !emailRe.test(v)) { ok = false; msg = "Informe um e-mail válido."; }
      else if (input.name === "message" && v && v.length < 10) { ok = false; msg = "Conte um pouco mais (mín. 10 caracteres)."; }
      field.classList.toggle("error", !ok);
      var m = $(".msg", field);
      if (m) m.textContent = msg;
      input.setAttribute("aria-invalid", String(!ok));
      return ok;
    }
    $$(".field", form).forEach(function (f) {
      var input = $("input, textarea, select", f);
      input.addEventListener(input.tagName === "SELECT" ? "change" : "blur", function () { if (input.value || f.classList.contains("error")) validate(f); });
      input.addEventListener("input", function () { if (f.classList.contains("error")) validate(f); });
    });
    var btn = $("button[type=submit]", form);
    var label = btn.querySelector("span");
    var labelText = label.textContent;
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var all = $$(".field", form).map(validate);
      if (all.indexOf(false) !== -1) {
        var bad = $(".field.error input, .field.error textarea, .field.error select", form);
        if (bad) bad.focus();
        return;
      }
      btn.disabled = true;
      label.textContent = "Enviando…";
      var endpoint = form.getAttribute("data-endpoint");
      var payload = {};
      $$("input, textarea, select", form).forEach(function (i) { payload[i.name] = i.value.trim(); });
      var done = function () {
        form.classList.add("sent");
        label.textContent = "Mensagem enviada";
        form.reset();
        setTimeout(function () { btn.disabled = false; label.textContent = labelText; }, 4000);
      };
      var fail = function () { btn.disabled = false; label.textContent = labelText; toast("Não foi possível enviar. Tente novamente."); };
      if (endpoint) {
        fetch(endpoint, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(payload) })
          .then(function (r) { if (!r.ok) throw new Error(r.status); done(); })
          .catch(fail);
      } else {
        /* sem backend: abre o WhatsApp com a mensagem pronta */
        var phone = form.getAttribute("data-whatsapp");
        var NL = String.fromCharCode(10);
        var lines = ["Olá! Quero aplicar ao Programa Kairos Cases.", ""];
        $$(".field", form).forEach(function (f) {
          var inp = $("input, textarea, select", f), lab = $("label", f);
          if (inp && lab && inp.value.trim()) lines.push(lab.textContent.replace("?", "") + ": " + inp.value.trim());
        });
        var text = lines.join(NL);
        var url = "https://wa.me/" + phone + "?text=" + encodeURIComponent(text);
        var w = window.open(url, "_blank", "noopener");
        if (!w) { window.location.href = url; }
        done();
      }
    });
  }


  /* ---------- entrada suave ao rolar ---------- */
  (function () {
    var els = $$("[data-reveal], [data-reveal-group] > *");
    if (!els.length) return;
    var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (reduce || !("IntersectionObserver" in window)) { els.forEach(function (e) { e.classList.add("in"); }); return; }
    $$("[data-reveal-group]").forEach(function (g) {
      Array.prototype.forEach.call(g.children, function (c, i) { c.setAttribute("data-reveal-i", i); c.style.setProperty("--d", (i * 90) + "ms"); });
    });
    els.forEach(function (e) { e.classList.add("reveal"); });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    els.forEach(function (e) { io.observe(e); });
  })();


  /* ---------- botão fixo de conversão ---------- */
  (function () {
    var btn = $(".sticky-cta");
    if (!btn) return;
    var form = $("#contact-form");
    var foot = $(".footer");
    function hit(el) { if (!el) return false; var r = el.getBoundingClientRect(); return r.top < window.innerHeight && r.bottom > 0; }
    function upd() {
      var show = window.scrollY > 700 && !hit(form) && !hit(foot) && !hit($("#aplicacao")) && !$$(".section-cta").some(hit);
      btn.classList.toggle("show", show);
      if ($("#aplicacao")) btn.setAttribute("href", "#aplicacao");
    }
    window.addEventListener("scroll", upd, { passive: true });
    window.addEventListener("resize", upd);
    upd();
  })();

  /* ---------- teste: quanto sua empresa depende de você ---------- */
  $$("[data-quiz]").forEach(function (box) {
    var qs = $$(".quiz__list li", box).map(function (li) { return li.getAttribute("data-q"); });
    var phone = box.getAttribute("data-whatsapp");
    var i = 0, score = 0;
    var bar = $(".quiz__bar i", box), count = $(".quiz__count", box), q = $(".quiz__q", box);
    var btns = $(".quiz__btns", box), res = $(".quiz__result", box);
    function render() {
      if (i >= qs.length) return finish();
      bar.style.width = (i / qs.length * 100) + "%";
      count.textContent = "Pergunta " + (i + 1) + " de " + qs.length;
      q.textContent = qs[i];
    }
    function finish() {
      bar.style.width = "100%";
      btns.hidden = true; q.hidden = true; count.hidden = true; res.hidden = false;
      var t, d;
      if (score <= 1) { t = "Você está no controle. Por enquanto."; d = "Poucos sinais de gargalo. Vale organizar antes que o acúmulo cresça."; }
      else if (score <= 3) { t = "Atenção: você já é parte do problema."; d = "A empresa depende de você em vários pontos. Cada semana de espera acumula mais."; }
      else { t = "Você é o arquivo vivo da empresa."; d = "Quase tudo passa por você. É exatamente o caso em que a Operação Mesa Limpa mais devolve tempo."; }
      $(".quiz__title", res).textContent = score + " de " + qs.length + " respostas \"sim\": " + t;
      $(".quiz__text", res).textContent = d;
      var NL = String.fromCharCode(10);
      var msg = "Olá! Fiz o teste no site da Kairos e tive " + score + " de " + qs.length + " respostas sim." + NL + "Quero saber se ainda há vaga neste mês.";
      var cta = $(".quiz__cta", res);
      cta.setAttribute("href", "https://wa.me/" + phone + "?text=" + encodeURIComponent(msg));
      cta.setAttribute("target", "_blank"); cta.setAttribute("rel", "noopener");
      cta.textContent = "Quero minha vaga pelo WhatsApp";
    }
    $$("[data-a]", box).forEach(function (b) {
      b.addEventListener("click", function () { score += Number(b.getAttribute("data-a")); i++; render(); });
    });
    $("[data-restart]", box).addEventListener("click", function () {
      i = 0; score = 0; btns.hidden = false; q.hidden = false; count.hidden = false; res.hidden = true; render();
    });
    render();
  });

  /* ---------- fallback de imagens ausentes ---------- */
  $$("img").forEach(function (img) {
    function miss() {
      img.style.visibility = "hidden";
      if (img.parentElement) img.parentElement.classList.add("img-missing");
      if (img.hasAttribute("data-logo-text")) {
        var span = document.createElement("span");
        span.className = "logo-fallback";
        span.textContent = img.getAttribute("data-logo-text");
        img.parentElement.appendChild(span);
      }
    }
    if (img.complete && img.naturalWidth === 0 && img.getAttribute("src")) miss();
    img.addEventListener("error", miss);
  });
})();
