#!/usr/bin/env python3
"""
Gerador estático do site da Kairos Consultoria.

Roda com:  py tools/build.py   (ou python3 tools/build.py)
Escreve os arquivos .html na raiz do projeto (HTML puro, sem dependências em runtime).
Existe só para não repetir navbar / footer / CTA / sprite de ícones em cada página.
"""
import os
from html import escape
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --------------------------------------------------------------------------
# Dados da empresa
# --------------------------------------------------------------------------
SITE = "Kairos"
EMAIL = "therafadourado@gmail.com"
PHONE_DISPLAY = "+55 95 98410-4479"
PHONE_E164 = "5595984104479"
INSTAGRAM_USER = "orafaeldourado"
INSTAGRAM_URL = f"https://instagram.com/{INSTAGRAM_USER}"
WA_TEXT = "Olá! Vim pelo site da Kairos e quero ver o que podem automatizar na minha empresa."
WA_URL = f"https://wa.me/{PHONE_E164}?text={quote(WA_TEXT)}"
EXT = 'target="_blank" rel="noopener"'
# Endereço público do site (sem barra no final). Quando definido, o build gera sitemap.xml.
# Ex.: KAIROS_SITE_URL=https://kairos.com.br py tools/build.py
SITE_URL = os.environ.get("KAIROS_SITE_URL", "").rstrip("/")

# --------------------------------------------------------------------------
# Ícones (sprite SVG, stroke = currentColor)
# --------------------------------------------------------------------------
ICONS = {
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3.5 7 8.5 6 8.5-6"/>',
    "inbox": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 13h5l1.2 2.2h5.6L16 13h5"/><path d="M8 8.5h8"/>',
    "headphones": '<path d="M4 15v-3a8 8 0 0 1 16 0v3"/><rect x="3" y="14" width="4.5" height="6.5" rx="1.8"/><rect x="16.5" y="14" width="4.5" height="6.5" rx="1.8"/>',
    "pin": '<path d="M12 21.5s-7-6-7-11.3a7 7 0 0 1 14 0c0 5.3-7 11.3-7 11.3z"/><circle cx="12" cy="10.2" r="2.6"/>',
    "chat-q": '<path d="M12 3.2a8.8 8.8 0 1 0 4.4 16.4L21 21l-1.3-4.5A8.8 8.8 0 0 0 12 3.2z"/><path d="M9.6 9.6a2.5 2.5 0 1 1 3.6 2.2c-.8.4-1.2 1-1.2 1.8"/><path d="M12 16.6h.01"/>',
    "code": '<path d="m8 8-4 4 4 4"/><path d="m16 8 4 4-4 4"/><path d="m13.5 5-3 14"/>',
    "scale": '<rect x="3" y="3" width="18" height="18" rx="2.5"/><path d="M13.5 10.5 19 5"/><path d="M14.5 5H19v4.5"/><path d="M10.5 13.5 5 19"/><path d="M9.5 19H5v-4.5"/>',
    "share": '<circle cx="6" cy="12" r="2.6"/><circle cx="18" cy="6" r="2.6"/><circle cx="18" cy="18" r="2.6"/><path d="m8.3 10.8 7.4-3.6"/><path d="m8.3 13.2 7.4 3.6"/>',
    "stopwatch": '<circle cx="12" cy="13.5" r="7.5"/><path d="M12 9.5v4l2.5 1.5"/><path d="M9.5 2.8h5"/>',
    "wifi": '<path d="M3.5 9.3a12 12 0 0 1 17 0"/><path d="M6.8 12.6a7.3 7.3 0 0 1 10.4 0"/><path d="M9.8 15.7a3 3 0 0 1 4.4 0"/><path d="M12 19h.01"/>',
    "user-sq": '<rect x="3" y="3" width="18" height="18" rx="3"/><circle cx="12" cy="10" r="2.6"/><path d="M6.8 18c.7-2.5 2.7-3.7 5.2-3.7s4.5 1.2 5.2 3.7"/>',
    "check-circle": '<circle cx="12" cy="12" r="9.5"/><path d="m8 12.3 2.8 2.8L16.2 9.5"/>',
    "chev-down": '<path d="m6 9 6 6 6-6"/>',
    "chev-up": '<path d="m18 15-6-6-6 6"/>',
    "chev-left": '<path d="m15 6-6 6 6 6"/>',
    "chev-right": '<path d="m9 6 6 6-6 6"/>',
    "arrow-right": '<path d="M5 12h14"/><path d="m13 6 6 6-6 6"/>',
    "bolt": '<path d="M13 2.5 4.5 13.5H11l-1 8 8.5-11H12l1-8z"/>',
    "download": '<circle cx="12" cy="12" r="9.5"/><path d="M12 7.5v8"/><path d="m8.5 12.5 3.5 3.5 3.5-3.5"/>',
    "chat-oval": '<ellipse cx="12" cy="11" rx="8.5" ry="7.2"/><path d="m8.5 17.5-1 3.5 4-2.4"/>',
    "arrow-bl": '<circle cx="12" cy="12" r="9.5"/><path d="m15.5 8.5-7 7"/><path d="M9 9.5v6h6"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "x": '<path d="m6 6 12 12M18 6 6 18"/>',
    "play": '<path d="M7 4.5v15a.8.8 0 0 0 1.2.7l12.3-7.5a.8.8 0 0 0 0-1.4L8.2 3.8A.8.8 0 0 0 7 4.5z" fill="currentColor" stroke="none"/>',
    "instagram": '<rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17 7h.01"/>',
}


def sprite():
    out = ['<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><defs>']
    for name, body in ICONS.items():
        out.append(f'<symbol id="i-{name}" viewBox="0 0 24 24">{body}</symbol>')
    out.append("</defs></svg>")
    return "".join(out)


def icon(name, cls="", extra=""):
    c = f"icon {cls}".strip()
    return f'<svg class="{c}" aria-hidden="true" focusable="false" {extra}><use href="#i-{name}"/></svg>'


# --------------------------------------------------------------------------
# Peças compartilhadas
# --------------------------------------------------------------------------
ORG_JSONLD = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"ProfessionalService","name":"Kairos Consultoria","description":"Automação de rotinas administrativas e processamento de documentos com inteligência artificial, com conferência humana e acompanhamento direto.","areaServed":{"@type":"City","name":"Boa Vista, Roraima"},"address":{"@type":"PostalAddress","addressLocality":"Boa Vista","addressRegion":"RR","addressCountry":"BR"},"email":"therafadourado@gmail.com","telephone":"+55 95 98410-4479","sameAs":["https://instagram.com/orafaeldourado"],"knowsLanguage":"pt-BR"}
</script>
"""


def head(title, desc, page_class="", extra_head=""):
    t, d = escape(title), escape(desc)
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<meta name="theme-color" content="#e0e3e8">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="Kairos Consultoria">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Instrument+Sans:wght@500;600&family=Geist:wght@400;500;600&family=Michroma&family=Poppins:wght@700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css?v=21">
<script>document.documentElement.className+=" js"</script>
{extra_head}</head>
<body class="{page_class}">
<a class="skip-link" href="#main">Ir para o conteúdo</a>
{sprite()}
<div class="page">
"""


def tail():
    return """</div>
<a class="sticky-cta" href="contato.html#aplicacao" aria-label="Aplicar agora">Aplicar agora <span>· 4 vagas por mês</span></a>
<script src="js/main.js?v=5"></script>
</body>
</html>
"""


def logomark(dark=False):
    return '<img class="brandmark brandmark--lg" src="assets/kairos.svg" alt="Kairos" width="142" height="28">'


NAV_COMPANY = [
    ("Sobre a Kairos", "sobre.html", "Quem somos e como trabalhamos"),
    ("Blog", "blog.html", "Conteúdo sobre automação administrativa"),
    ("Contato", "contato.html", "Fale com a gente"),
]


def nav(active="", light=False):
    cls = "nav nav--light" if light else "nav"

    def menu(items, label, mid, cur):
        links = "".join(
            f'<a href="{h}"{" aria-current=\"page\"" if h.split("#")[0] == cur else ""}>{escape(t)}<small>{escape(s)}</small></a>'
            for t, h, s in items
        )
        return (
            f'<div class="nav__item"><button class="nav__trigger" type="button" aria-expanded="false" aria-haspopup="true" aria-controls="{mid}">'
            f'{label}{icon("chev-down", "icon--16")}</button><div class="nav__menu" id="{mid}">{links}</div></div>'
        )

    def link(href, label, key):
        cur = ' aria-current="page"' if active == key else ""
        return f'<a class="nav__link" href="{href}"{cur}>{label}</a>'

    company_active = active if active in ("sobre.html", "blog.html", "contato.html") or active.startswith("blog-") else ""
    if active.startswith("blog-"):
        company_active = "blog.html"
    return f"""  <header class="{cls}" id="nav">
    <a class="logo" href="index.html" aria-label="Kairos — página inicial"><img class="brandmark" src="assets/kairos.svg" alt="Kairos" width="122" height="24"></a>
    <nav class="nav__links" aria-label="Principal">
      {link("index.html", "Início", "index.html")}
      {link("index.html#areas", "Áreas", "#areas")}
      {link("ruraldocs.html", "RuralDocs", "ruraldocs.html")}
      {link("oferta.html", "Programa", "oferta.html")}
      {menu(NAV_COMPANY, "Empresa", "menu-empresa", company_active)}
      <a class="btn nav__panel-cta" href="contato.html#aplicacao">Aplicar agora</a>
    </nav>
    <a class="btn nav__cta" href="contato.html#aplicacao">Aplicar agora</a>
    <button class="nav__burger" type="button" aria-label="Abrir menu" aria-expanded="false">{icon("menu")}</button>
  </header>
"""


def footer():
    return f"""  <footer class="footer">
    <img class="footer__art" src="assets/footer-art.svg?v=2" alt="" aria-hidden="true">
    <div class="footer__in">
      <div class="footer__brand">
        <strong>KAIROS</strong>
        <p>Automação de rotinas administrativas e de documentos com inteligência artificial, com conferência humana e acompanhamento direto. Atuação inicial em Boa Vista, Roraima.</p>
        <small>© 2026 Kairos Consultoria. Todos os direitos reservados.</small>
      </div>
      <nav class="footer__nav" aria-label="Rodapé">
        <div class="footer__col"><h4>Navegação</h4>
          <a href="index.html#areas">Áreas</a><a href="ruraldocs.html">RuralDocs</a><a href="oferta.html">Programa</a><a href="blog.html">Blog</a></div>
        <div class="footer__col"><h4>Contato</h4>
          <a href="{WA_URL}" {EXT}>WhatsApp</a><a href="mailto:{EMAIL}">E-mail</a><a href="{INSTAGRAM_URL}" {EXT}>Instagram</a><a href="contato.html">Formulário</a></div>
        <div class="footer__col"><h4>Legal</h4>
          <a href="termos.html">Termos de uso</a><a href="privacidade.html">Privacidade</a><a href="privacidade.html#cookies">Cookies</a></div>
      </nav>
    </div>
  </footer>
"""


def cta(title="Quer ser um dos nossos cases?", text="4 vagas por mês. Implementação sem custo para quem se encaixa."):
    return f"""  <section class="section cta" aria-labelledby="cta-title">
    <div class="cta__in">
      <div class="cta__txt">
        {logomark(dark=True)}
        <h2 id="cta-title">{title}</h2>
        <p>{text}</p>
      </div>
      <div class="btn-row">
        <a class="btn btn--dark" href="contato.html#aplicacao">Aplicar agora {icon("bolt", "icon--16")}</a>
        <a class="btn btn--light" href="{WA_URL}" {EXT}>Falar no WhatsApp</a>
      </div>
    </div>
  </section>
"""


def page_head(h1, p=None, with_logo=False):
    logo = logomark(dark=True) if with_logo else ""
    sub = f'<p class="lead">{p}</p>' if p else ""
    return f"""      <div class="text-block">
        {logo}
        <h1 class="h-lg">{h1}</h1>
        {sub}
      </div>
"""


def sub_section_open(nav_html, extra_class=""):
    return f"""  <main id="main">
  <section class="section section--page {extra_class}">
    <div class="mask-grid" aria-hidden="true"></div>
{nav_html}
    <div class="content stack-64">
"""


def sub_section_close():
    return """    </div>
  </section>
"""


def write(name, content):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("ok", name)


# --------------------------------------------------------------------------
# Cards reutilizáveis
# --------------------------------------------------------------------------
def tile(name=None, emoji=None):
    if emoji:
        return f'<span class="icon-tile"><span class="emoji" aria-hidden="true">{emoji}</span></span>'
    return f'<span class="icon-tile"><span>{icon(name)}</span></span>'


def info_card(icon_name, title, text_html, emoji=None):
    return f"""<article class="card"><div class="card__inner">
  <div class="card__head">{tile(icon_name, emoji)}<h3 class="card__title">{title}</h3></div>
  <p class="card__text">{text_html}</p>
</div></article>"""


# --------------------------------------------------------------------------
# Mockups em HTML/CSS (ilustrativos; sem dados reais de clientes)
# --------------------------------------------------------------------------
def dash(dark=False):
    bars = [(72.57, 9.97), (4.68, 17.48), (67.24, 24.98), (60.27, 32.49), (15.78, 39.99), (46.07, 47.5),
            (43.84, 55.01), (28.72, 62.51), (47.15, 70.02), (75.05, 77.52), (24.84, 85.03), (44.03, 92.54)]
    labels = [f"L{i}" for i in range(1, 13)]
    plot = []
    for i, (top, left) in enumerate(bars):
        plot.append(f'<b style="left:{left}%;height:{90 - top:.2f}%"></b>')
        plot.append(f'<i class="m" style="left:{left + 2.98:.2f}%">{labels[i]}</i>')
    for k, lab in enumerate(["0", "20", "40", "60", "80"]):
        plot.append(f'<i class="y" style="top:{90 - k * 22.35:.2f}%">{lab}</i>')
    recent = [("NF", "Nota fiscal (DANFE)", "Fornecedor lido · aguardando", "Revisar"),
              ("CP", "Cupom fiscal", "Itens extraídos · aguardando", "Revisar"),
              ("RC", "Recibo de serviço", "Conferido por você", "Confirmado"),
              ("PG", "Comprovante de pagamento", "Vinculado à despesa", "Vinculado"),
              ("AM", "Anotação manuscrita", "Campos ilegíveis em branco", "Revisar")]
    recent_html = "".join(
        f'<li><span class="av">{a}</span><div class="who">{n}<small>{e}</small></div><span>{v}</span></li>'
        for a, n, e, v in recent
    )
    stats = [
        ("Importados", "128", "originais preservados", '<path d="M6 1.5v6.5M3.5 5.5 6 8l2.5-2.5M2 10.5h8"/>'),
        ("Lidos pela IA", "96", "regiões separadas por documento", '<circle cx="6" cy="6" r="4"/><circle cx="6" cy="6" r="1.4"/>'),
        ("Em revisão", "41", "aguardando conferência humana", '<circle cx="4" cy="3.6" r="1.9"/><path d="M0.8 10c.3-1.7 1.5-2.6 3.2-2.6s2.9.9 3.2 2.6"/><path d="M8.2 2a1.9 1.9 0 0 1 0 3.6M9.4 7.6c.9.4 1.4 1.2 1.6 2.4"/>'),
        ("Confirmados", "55", "prontos para virar despesa", '<path d="m2 6.3 2.6 2.6L10 3.4"/>'),
    ]
    stats_html = "".join(
        f'<div class="dash__card dash__stat"><div class="dash__stat-h"><span>{t}</span><svg viewBox="0 0 12 12">{ic}</svg></div>'
        f'<div class="dash__stat-b"><strong>{v}</strong><small>{c}</small></div></div>'
        for t, v, c, ic in stats
    )
    cls = "dash dash--dark" if dark else "dash"
    return f"""<div class="{cls}" aria-hidden="true">
<div class="dash__bar"><div class="dash__combo"><span class="dash__dot"></span><span>RuralDocs</span><svg width="7" height="7" viewBox="0 0 8 8" fill="none" stroke="currentColor" stroke-width="1" stroke-linecap="round"><path d="m2 3 2-1.6L6 3M2 5l2 1.6L6 5"/></svg></div>
<div class="dash__nav"><span class="on">Painel</span><span>Lotes</span><span>Revisão</span><span>Despesas</span></div>
<div class="dash__tools"><div class="dash__search">Buscar...</div><div class="dash__avatar">KA</div></div></div>
<div class="dash__body">
<div class="dash__title"><h3>Painel</h3><div class="dash__title-r"><div class="dash__date"><svg viewBox="0 0 8 8" fill="none" stroke="currentColor" stroke-width=".7"><rect x="1" y="1.5" width="6" height="5.5" rx=".8"/><path d="M1 3.4h6M2.8 .8v1.2M5.2 .8v1.2"/></svg>Tela ilustrativa</div><div class="dash__btn">Ver lotes</div></div></div>
<div class="dash__tabs"><button type="button" class="dash__tab on" tabindex="-1">Visão geral</button><button type="button" class="dash__tab" tabindex="-1">Lotes</button><button type="button" class="dash__tab" tabindex="-1">Revisão</button><button type="button" class="dash__tab" tabindex="-1">Despesas</button></div>
<div class="dash__stats">{stats_html}</div>
<div class="dash__row">
<div class="dash__card dash__chart"><h4>Documentos por lote</h4><div class="dash__plot">{"".join(plot)}</div></div>
<div class="dash__card dash__sales"><header><h4>Documentos recentes</h4><p>Você tem a palavra final.</p></header><ul>{recent_html}</ul></div>
</div></div></div>"""


def revisao():
    """Mockup da tela de conferência humana (usa a estrutura visual do antigo mockup de e-mail)."""
    nav1 = [("Lotes", "", False, '<path d="M3 3h6v4.5H7.8L7 9H5l-.8-1.5H3z"/>'), ("Documentos", "", False, '<path d="M3 3h6v6H3z"/>'),
            ("Revisão", "41", True, '<circle cx="6" cy="6" r="4"/><circle cx="6" cy="6" r="1.4"/>'), ("Despesas", "", False, '<rect x="1.5" y="3" width="9" height="6" rx="1"/>'),
            ("Fornecedores", "", False, '<circle cx="6" cy="4" r="2"/><path d="M2 10c.5-2 2-3 4-3s3.5 1 4 3"/>')]

    def row(t, c, on, svg='<circle cx="6" cy="6" r="3.6"/>'):
        return (f'<a href="#" tabindex="-1" class="{"on" if on else ""}"><svg viewBox="0 0 12 12">{svg}</svg><span>{t}</span>{f"<b>{c}</b>" if c else ""}</a>')

    side = "".join(row(t, c, on, s) for t, c, on, s in nav1)
    items = [("Nota fiscal (DANFE)", "Revisar", "Fornecedor, datas, valores e itens já preenchidos para você.", ["pendente*", "nota de origem"]),
             ("Cupom fiscal", "Revisar", "Soma dos itens conferida com o total do documento.", ["pendente*", "cupom"]),
             ("Comprovante de pagamento", "Vincular", "Ligado à despesa certa, sem contar duas vezes.", ["comprovante"]),
             ("Recibo de serviço", "Confirmado", "Sua correção guardada ao lado da leitura original.", ["confirmado"])]

    def item(n, s, b, tags):
        t = "".join(f'<span class="{"dk" if x.endswith("*") else ""}">{x.rstrip("*")}</span>' for x in tags)
        return f'<div class="mail__item"><div>{n}<em>{s}</em></div><strong>Documento {escape(n.split(" ")[0].lower())}</strong><p>{b}</p><div class="mail__tags">{t}</div></div>'

    return f"""<div class="mail" aria-hidden="true">
<div class="mail__side"><div class="mail__acct"><i></i><span>RuralDocs</span><svg width="7" height="7" viewBox="0 0 8 8" fill="none" stroke="currentColor" stroke-width="1" stroke-linecap="round"><path d="m2 3 2-1.6L6 3M2 5l2 1.6L6 5"/></svg></div><div class="mail__nav">{side}</div></div>
<div class="mail__list"><div class="mail__list-h"><h4>Revisão</h4><div class="mail__seg"><span class="on">Pendentes</span><span>Todos</span></div></div>
<div class="mail__search">Buscar documento</div><div class="mail__items">{"".join(item(*i) for i in items)}</div></div>
<div class="mail__view"><div class="mail__tools"><svg viewBox="0 0 12 12"><path d="m2 6.3 2.6 2.6L10 3.4"/></svg><svg viewBox="0 0 12 12"><circle cx="6" cy="6" r="4"/></svg><svg viewBox="0 0 12 12"><path d="M3 4h6l-.6 6H3.6zM2.5 3h7"/></svg></div>
<div class="mail__from"><i></i><div><strong>Nota fiscal (DANFE)</strong><small>Recorte ampliado + leitura da IA</small><small>Campos editáveis · histórico preservado</small></div></div>
<div class="mail__body"><p>Tudo já vem preenchido: confirme ou ajuste fornecedor, datas, valores e itens.</p><p>Alertas de CPF/CNPJ e de soma aparecem na hora.</p><p>O original fica sempre guardado.</p></div></div></div>"""


# --------------------------------------------------------------------------
# Seções reutilizáveis
# --------------------------------------------------------------------------
PROGRAM = [
    "Um especialista da Kairos só seu, começando pelo diagnóstico da operação",
    "Roadmap com o que dá mais retorno primeiro",
    "Imersão presencial: a gente trabalha junto com o seu time",
    "Automações, agentes e ferramentas rodando nas suas áreas",
    "Acompanhamento por 12 meses: toda semana no 1º mês, a cada 15 dias nos meses 2 e 3, uma vez por mês depois",
    "Grupo direto com o especialista e com o sócio da Kairos",
    "Treinamento gravado e materiais para o seu time",
    "Infraestrutura de IA e backup conferido",
]

PREREQ = [
    ("scale", "Faturamento de R$ 2 milhões por ano ou mais", "Abaixo disso, ainda não compensa o nível de trabalho que a gente coloca."),
    ("user-sq", "Pelo menos 5 pessoas no escritório", "É onde a IA mais economiza tempo e dinheiro."),
    ("code", "Sócio ou CEO acompanhando o projeto", "A gente vai mexer em processo antigo. Precisa de quem decide."),
    ("share", "Autorizar o case", "Contamos a história do projeto. O que for sensível ou estratégico fica de fora."),
    ("download", "Contrato de 12 meses", "R$ 5.000 por mês para pagar a IA, R$ 60 mil no total, fechado de uma vez."),
]

AREAS = [
    ("inbox", "Administrativo e documentos", "Nota, recibo e comprovante viram dado organizado, ligado ao original."),
    ("scale", "Financeiro", "Lançamento e conferência sem digitar nada."),
    ("bolt", "Comercial", "A IA ajuda a qualificar contato, fazer follow-up e montar proposta."),
    ("chat-oval", "Atendimento", "A IA responde o básico e o seu time cuida do que precisa de gente."),
    ("user-sq", "Pessoas e rotinas internas", "Admissão, pedidos internos e a papelada do dia a dia."),
    ("share", "Operações", "Liga sistemas e planilhas para o processo andar sozinho."),
]


def program_card(button_href="contato.html#aplicacao", button_label="Aplicar agora"):
    lis = "".join(f'<li>{icon("check-circle")}<span>{escape(i)}</span></li>' for i in PROGRAM)
    return f"""<div class="tiers tiers--single"><article class="tier tier--pop tier--offer">
  <div class="tier__head">
    <div class="tier__title"><div><h3>Programa Kairos Cases</h3><span class="pill">4 vagas por mês</span></div><p>IA na empresa toda, sem cobrar a implementação. Contrato de 12 meses, fechado de uma vez.</p></div>
  </div>
  <div class="price-cards">
    <div class="price-card price-card--free"><span>Implementação</span><strong>R$ 0</strong><em>Por nossa conta</em></div>
    <div class="price-card price-card--paid"><span>Contrato de 12 meses</span><strong>R$ 5.000<small>/mês</small></strong><em>R$ 60 mil no total</em></div>
  </div>
  <p class="price-note"><strong>Os R$ 5.000 por mês pagam o custo da inteligência artificial</strong> que vai rodar na sua empresa: o consumo de IA e a infraestrutura.</p>
  <div class="tier__body">
    <div><h4>TUDO QUE VOCÊ RECEBE</h4><p>Infraestrutura de IA, automações rodando e acompanhamento direto durante os 12 meses.</p></div>
    <ul class="checks">{lis}</ul>
  </div>
  <div class="tier__foot"><a class="btn btn--dark btn--block" href="{button_href}">{button_label}</a></div>
</article></div>
<p class="fine-print">Deslocamento e hospedagem, se fora de Boa Vista, ficam por conta do cliente.</p>"""


def prereq_cards():
    return "".join(info_card(i, t, d) for i, t, d in PREREQ)


def scarcity():
    return f"""<aside class="promo" aria-label="Escassez">
        <div><h3>Só 4 vagas por mês</h3><p>Cada projeto tem um especialista só dele, por isso são só 4 por mês. Quando as vagas do programa acabarem, a implementação passa a ser cobrada, e bem mais cara.</p></div>
        <a class="btn btn--light" href="contato.html#aplicacao">Aplicar agora {icon("arrow-right", "icon--16")}</a>
      </aside>"""


FAQS = [
    ("Por que a implementação é de graça?", "Porque a gente quer o case. Preferimos ter uma base de resultados reais a cobrar a implementação agora."),
    ("Quanto custa e por quanto tempo?", "A implementação não custa nada. O contrato é de 12 meses, fechado de uma vez: R$ 5.000 por mês, R$ 60 mil no total. Esse valor paga o custo da inteligência artificial que vai rodar na sua empresa, o consumo de IA e a infraestrutura."),
    ("Aplicar é o mesmo que contratar?", "Não. A gente analisa a sua aplicação e, se fizer sentido, liga para conversar sobre o seu negócio. Só depois decidimos juntos."),
    ("Que áreas vocês automatizam?", "O administrativo é onde a gente já tem resultado: documentos, notas e lançamentos. Na conversa a gente descobre onde está o maior ganho: financeiro, comercial, atendimento, operações."),
    ("O que é documentar o case?", "Contar a história: qual era o problema, o que foi feito e qual foi o resultado. O que for sensível ou estratégico fica protegido, e combinamos tudo antes."),
    ("E se minha empresa não se encaixa?", 'Hoje o programa é para empresas a partir de R$ 2 milhões por ano e com pelo menos 5 pessoas no escritório. Se ainda não é o seu caso, <a href="contato.html" style="text-decoration:underline">fale com a gente</a> e avisamos quando abrirmos outras vagas.'),
]


def faq(title="Perguntas frequentes", lead=None):
    lead = lead or 'Mais dúvidas? <a href="contato.html" style="text-decoration:underline">Fale com a gente</a>.'
    items = []
    for i, (q, a) in enumerate(FAQS):
        op = " open" if i == 0 else ""
        items.append(f"""<div class="faq__item{op}"><button class="faq__q" type="button" id="faq-q{i}" aria-expanded="{"true" if i == 0 else "false"}" aria-controls="faq-a{i}"><span>{q}</span>{icon("chev-down")}</button>
<div class="faq__a" id="faq-a{i}" role="region" aria-labelledby="faq-q{i}"><div><p>{a}</p></div></div></div>""")
    return f"""  <section class="section section--pad" id="faq" aria-labelledby="faq-title">
    <div class="stack-64 content">
      <div class="text-block"><h2 class="h-lg" id="faq-title">{title}</h2>
        <p class="lead">{lead}</p></div>
      <div class="faq"><div class="faq__inner">{"".join(items)}</div></div>
    </div>
  </section>
"""


# --------------------------------------------------------------------------
# PÁGINAS
# --------------------------------------------------------------------------
def mini_members(rows):
    out = ""
    for title, sub, tag in rows:
        out += f'<div class="mini__member"><span class="av"></span><div><strong>{title}</strong><span>{sub}</span></div><div class="mini__select">{tag}</div></div>\n'
    return f'<div class="mini__members">{out}</div>'


def page_index():
    h = head("Kairos — Entramos na sua operação e automatizamos com IA",
             "A Kairos coloca o time dentro da sua operação para automatizar processos com IA, sem cobrar a implementação. Para empresas a partir de R$ 2 milhões por ano. Boa Vista, Roraima.",
             "home", extra_head=ORG_JSONLD)
    tickers = ["Administrativo", "Financeiro", "Comercial", "Atendimento", "Operações", "Documentos", "Rotinas internas", "Relatórios"]
    tick = "".join(f"<span>{t}</span><i aria-hidden='true'></i>" for t in tickers)
    areas = "".join(info_card(i, t, d) for i, t, d in AREAS)
    steps = (
        info_card("chat-q", "1. Diagnóstico no caos", "A gente ouve você e mapeia a rotina.")
        + info_card("bolt", "2. Prova ao vivo", "Você vê funcionando com os seus dados.")
        + info_card("code", "3. Execução sob medida", "Montamos o fluxo para as suas regras.")
        + info_card("check-circle", "4. Estrutura que fica", "Interface pronta para a sua equipe usar.")
    )
    sc = lambda label="Aplicar agora": f'<div class="section-cta" data-reveal><a class="btn btn--dark" href="#aplicacao">{label} {icon("arrow-right", "icon--16")}</a></div>'
    h += f"""  <main id="main">
  <section class="section hero hero--vsl" id="top">
    <div class="mask-grid mask-grid--dark" aria-hidden="true"></div>
{nav("index.html", light=True)}
    <div class="hero__content content">
      <div class="hero__frame">
        <div class="hero__head">
          <span class="badge badge--live">Para empresas de R$ 2 mi+ por ano</span>
          <div class="hero__text">
            <h1 class="h-xl" style="color:#fff;text-align:center">Sua empresa depende de você para tudo?</h1>
            <p style="text-align:center">A gente entra na sua empresa, descobre o que dá para automatizar e coloca a IA para trabalhar. A implementação não custa nada. São 4 vagas por mês.</p>
          </div>
        </div>
        <div class="btn-row">
          <a class="btn btn--light" href="#aplicacao">Aplicar agora {icon("arrow-right", "icon--16")}</a>
          <a class="btn btn--gray" href="{WA_URL}" {EXT}>Falar no WhatsApp</a>
        </div>
        <ul class="trust" aria-label="Destaques">
          <li>{icon("check-circle", "icon--16")}Implementação sem custo</li>
          <li>{icon("check-circle", "icon--16")}4 vagas por mês</li>
          <li>{icon("check-circle", "icon--16")}Case real: Fazenda Cajazeira</li>
        </ul>
      </div>
      <div class="hero__app">
        <div class="app-frame app-frame--hero" data-fit><div class="app-frame__scale">{dash(dark=True)}</div></div>
      </div>
    </div>
  </section>

  <div class="ticker" aria-hidden="true"><div class="ticker__in">{tick}{tick}</div></div>

  <section class="section section--case section--pad" id="caso" aria-labelledby="caso-title">
    <div class="case" data-reveal>
      <span class="pill">Resultado real</span>
      <h2 id="caso-title">Fazenda Cajazeira</h2>
      <p class="case__big">Centenas de documentos organizados em cerca de uma semana e meia.</p>
      <p class="case__small">À mão, levaria de 30 a 45 dias. O dono voltou a ver o fundo da própria mesa.</p>
      <a class="btn btn--light" href="ruraldocs.html">Veja como funciona {icon("arrow-right", "icon--16")}</a>
    </div>
  </section>

  <section class="section section--pad" id="tese" aria-labelledby="tese-title">
    <div class="stack-64 content">
      <div class="text-block" data-reveal><h2 class="h-lg" id="tese-title">Colocar ChatGPT em processo velho não resolve</h2>
        <p class="lead">Com a eletricidade foi assim: o salto de produtividade só veio quando as fábricas mudaram o jeito de trabalhar. Com IA é igual.</p></div>
      <div class="compare" data-reveal-group>
        <article class="compare__col compare__col--old"><h3>O que a maioria faz</h3><p>Paga uma conta de ChatGPT para cada funcionário e espera a empresa render mais.</p></article>
        <article class="compare__col compare__col--new"><h3>O que a gente faz</h3><p>Pega o processo, pergunta como ele seria se fosse criado hoje, com IA ligada o dia inteiro, e refaz do zero.</p></article>
      </div>
      {sc()}
    </div>
  </section>

  <section class="section section--pad" id="operar" aria-labelledby="operar-title">
    <div class="stack-64 content">
      <div class="text-block" data-reveal><h2 class="h-lg" id="operar-title">Usar IA é uma coisa. Operar com IA é outra.</h2>
        <p class="lead">ChatGPT na mão de cada um dá ganho individual. A empresa só muda quando o processo muda.</p></div>
      <div class="compare" data-reveal-group>
        <article class="compare__col compare__col--old"><h3>Usar IA</h3><p>Cada um com a sua conta e o seu jeito. O ganho é pequeno e o conhecimento fica espalhado.</p></article>
        <article class="compare__col compare__col--new"><h3>Operar com IA</h3><p>O processo é refeito, a IA conhece a empresa e a automação roda todo dia. Dá para medir o resultado.</p></article>
      </div>
      <p class="fine-print">O problema quase nunca é a ferramenta. É ter alguém que entre na empresa, converse com o time e refaça o processo.</p>
    </div>
  </section>

  <section class="section section--pad" id="areas" aria-labelledby="areas-title">
    <div class="stack-64 content">
      <div class="text-block" data-reveal><h2 class="h-lg" id="areas-title">Qualquer área pode rodar sem você</h2>
        <p class="lead">A gente começa pelo que dá mais retorno.</p></div>
      <div class="card-grid card-grid--3" data-reveal-group>{areas}</div>
      {sc()}
    </div>
  </section>

  <section class="section section--pad" id="metodo" aria-labelledby="metodo-title">
    <div class="stack-64 content">
      <div class="text-block" data-reveal><h2 class="h-lg" id="metodo-title">O método Raio X da Bagunça</h2>
        <p class="lead">Quatro etapas, com você junto do começo ao fim.</p></div>
      <div class="media-card media-card--short" data-reveal>
        <img src="assets/img/careers-hero.png" alt="" width="1188" height="763" loading="lazy">
        <div class="media-card__ov" style="top:30%"></div>
        <div class="media-card__cap"><div style="max-width:620px"><h3>Uma conversa direta com você</h3><p>É assim que tudo começa.</p></div></div>
      </div>
      <div class="card-grid card-grid--4" data-reveal-group>{steps}</div>
      {sc()}
    </div>
  </section>

  <section class="section section--dark section--pad" id="porque" aria-labelledby="porque-title">
    <div class="prose-block" data-reveal>
      <div class="tx"><h2 id="porque-title">Por que a implementação não custa nada?</h2>
        <p>Porque o seu resultado vira a nossa vitrine. Cada empresa que a gente transforma vira um case, com o antes, o depois e os números. Isso vale mais para a gente do que cobrar a implementação. E para você também compensa: sua empresa passa a ser referência em IA no seu mercado.</p></div>
    </div>
  </section>

  <section class="section section--pad" id="criterios" aria-labelledby="criterios-title">
    <div class="stack-64 content">
      <div class="text-block" data-reveal><h2 class="h-lg" id="criterios-title">Só 4 empresas por mês entram</h2>
        <p class="lead">Não é para todo mundo. Se você não se encaixa nos cinco pontos abaixo, o programa não é para você.</p></div>
      <div class="card-grid card-grid--3" data-reveal-group>{prereq_cards()}</div>
    </div>
  </section>

  <section class="section section--pad" id="programa" aria-labelledby="programa-title">
    <div class="stack-64 content">
      <div class="text-block" data-reveal><h2 class="h-lg" id="programa-title">Um time dentro da sua operação. Implementação sem custo.</h2>
        <p class="lead">Diagnóstico, roadmap, implementação, acompanhamento e treinamento. Contrato de 12 meses: R$ 5.000 por mês para pagar a IA, R$ 60 mil no total.</p></div>
      {program_card(button_href="#aplicacao")}
      {scarcity()}
    </div>
  </section>

{faq()}
  <section class="section section--pad" id="aplicacao" aria-labelledby="aplicacao-title">
    <div class="stack-64 content">
      <div class="text-block" data-reveal><h2 class="h-lg" id="aplicacao-title">Aplique para ser um dos 4 cases do mês</h2>
        <p class="lead">Aplicar não é contratar. A gente analisa e, se fizer sentido, liga para você.</p></div>
      {form_card()}
    </div>
  </section>
  </main>
{footer()}"""
    h += tail()
    write("index.html", h)


def page_oferta():
    h = head("Programa Kairos Cases — implementação de IA sem custo | Kairos", "Programa Kairos Cases: a Kairos implementa IA na sua operação sem cobrar a implementação. Contrato de 12 meses, R$ 5.000 por mês (R$ 60 mil). Para empresas a partir de R$ 2 milhões por ano. 4 vagas por mês.", "pricing")
    h += sub_section_open(nav("oferta.html")) + f"""{page_head("IA na empresa toda, sem custo de implementação.", "A gente entra na sua operação, constrói as soluções junto com o seu time e acompanha por 12 meses. Em troca, precisamos do seu case e do contrato de 12 meses.")}
      <div class="media-card media-card--short" data-reveal>
        <img src="assets/img/careers-hero.png" alt="" width="1188" height="763" loading="lazy">
        <div class="media-card__ov" style="top:30%"></div>
        <div class="media-card__cap"><div style="max-width:620px"><h3>Um time dentro da sua operação</h3><p>Do diagnóstico ao acompanhamento de 12 meses.</p></div></div>
      </div>
      {program_card()}
      <div class="text-block"><h2 class="h-md">Quem pode aplicar</h2></div>
      <div class="card-grid card-grid--3">{prereq_cards()}</div>
      {scarcity()}
""" + sub_section_close() + "\n" + faq() + "\n" + cta() + "  </main>\n" + footer() + tail()
    write("oferta.html", h)


RURAL = [
    ("inbox", "Despeje o acúmulo de uma vez", "Fotos e arquivos em lote. Originais guardados, duplicados avisados."),
    ("share", "Uma foto, vários documentos", "A IA separa cada nota e comprovante da mesma foto."),
    ("stopwatch", "Trabalha enquanto você trabalha", "Processa em lote e retoma sozinho se algo falhar."),
    ("user-sq", "Você confere em segundos", "Recorte ampliado, campos preenchidos, tudo editável."),
    ("check-circle", "Alertas na hora", "CPF, CNPJ, valores e itens conferidos automaticamente."),
    ("scale", "Dinheiro sob controle", "Só o que você confirma vira despesa. Sem contar duas vezes."),
    ("code", "Encontre qualquer coisa", "Busca por período, fornecedor, categoria e texto."),
    ("download", "Seus dados com você", "Armazenamento local e backup completo conferido."),
]


def page_ruraldocs():
    cards = "".join(info_card(i, t, d) for i, t, d in RURAL)
    h = head("RuralDocs — do monte de papel ao dado na ponta dos dedos | Kairos", "RuralDocs: importe fotos de notas e recibos, deixe a IA ler e organizar, confira em segundos e saiba para onde foi cada real. Solução da Kairos já em uso em um cliente real.", "integrations")
    h += sub_section_open(nav("ruraldocs.html")) + f"""      <div class="text-block">{logomark(dark=True)}
        <h1 class="h-lg">RuralDocs: do monte de papel ao dado na ponta dos dedos</h1>
        <p class="lead">Você fotografa, a IA organiza, você confere em segundos.</p></div>
      <div class="card-grid card-grid--wide">
{cards}      </div>
      <article class="feature feature-wide" style="width:100%">
        <div class="feature__text"><h3>Tudo num painel só</h3><p class="lead2">O que entrou, o que foi lido e o que falta conferir.</p>
          <ul class="checklist">
            <li>{icon("arrow-bl")}Lotes e documentos em um lugar</li>
            <li>{icon("arrow-bl")}Busca por fornecedor, período e categoria</li>
            <li>{icon("arrow-bl")}Cada dado ligado ao documento original</li>
          </ul></div>
        <div class="feature__media">{dash()}</div>
      </article>
      <article class="feature feature-wide" style="width:100%">
        <div class="feature__media">{revisao()}</div>
        <div class="feature__text"><h3>Você tem a palavra final</h3><p class="lead2">A IA preenche. Você confere e confirma.</p>
          <ul class="checklist">
            <li>{icon("arrow-bl")}Recorte ampliado ao lado dos campos</li>
            <li>{icon("arrow-bl")}Alerta de CPF, CNPJ e valores</li>
            <li>{icon("arrow-bl")}Histórico de tudo que foi alterado</li>
          </ul></div>
      </article>
""" + sub_section_close() + "\n" + cta("Quer algo assim na sua empresa?", "O RuralDocs mostra o que a gente faz. Aplique e veja o que dá para automatizar na sua operação.") + "  </main>\n" + footer() + tail()
    write("ruraldocs.html", h)


# --------------------------------------------------------------------------
# Blog
# --------------------------------------------------------------------------
def _li(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


ARTICLES = [
    dict(
        slug="blog-organizar-notas-fiscais-fazenda.html",
        img="blog-2", date="12 de outubro de 2026", iso="2026-10-12",
        title="Como organizar notas fiscais acumuladas da fazenda sem se perder em planilhas",
        desc="Passo a passo para organizar notas fiscais, recibos e comprovantes acumulados: digitalizar, padronizar campos, separar comprovantes e conferir antes de lançar.",
        excerpt="Um passo a passo para transformar uma pilha de notas, recibos e comprovantes em informação que o dono consegue consultar.",
        body=[
            ("Por que o acúmulo vira um problema", [
                "Em fazendas e pequenas indústrias, as notas fiscais, os recibos e os comprovantes se acumulam em gavetas, pastas e galerias de celular. Enquanto tudo está espalhado, ninguém consegue responder perguntas simples: quanto foi gasto no mês, com quem, e quanto cada sócio desembolsou.",
                "O custo aparece na hora de fechar as contas, de conversar com o contador ou de tomar uma decisão de investimento. Quanto mais tempo passa, mais difícil fica reconstruir o histórico."]),
            ("Passo 1: junte tudo e separe por origem", [
                "Reúna os papéis e as fotos em um só lugar e separe o que é documento de compra (nota fiscal, cupom, recibo) do que é comprovante de pagamento (transferência, boleto pago). Essa distinção é importante: o comprovante prova que a compra foi paga, mas não é uma segunda compra."]),
            ("Passo 2: digitalize com um padrão", [
                "Fotografe com boa luz, sem cortar as bordas e sem sombra sobre os números. Se várias notas aparecerem na mesma foto, tudo bem, desde que cada uma esteja inteira. O mais importante é guardar sempre o original digital, sem editar a imagem."]),
            ("Passo 3: padronize os campos", [
                "Defina o que você precisa saber de cada documento e registre sempre do mesmo jeito:",
                _li(["fornecedor e CPF ou CNPJ", "número e data do documento", "valores, descontos e total", "itens comprados, com quantidade e preço"])]),
            ("Passo 4: confira antes de lançar", [
                "Compare a soma dos itens com o total e valide CPF e CNPJ antes de tratar o dado como pronto. Esse cuidado simples deixa o seu histórico confiável para decidir e para conversar com o contador."]),
            ("Por que só uma planilha costuma não resolver", [
                "Digitar documento por documento consome semanas, e a planilha perde a ligação com o papel original. Quando surge uma dúvida, ninguém sabe de qual nota veio aquele valor. O ideal é que cada linha de dado continue ligada ao documento de origem."]),
            ("Onde a inteligência artificial entra", [
                "A IA faz o trabalho pesado: lê, separa e preenche os dados dos documentos, inclusive de várias notas na mesma foto. Você só confere e confirma, e o original continua guardado.",
                "Foi esse o caminho de um projeto real da Kairos: documentos acumulados por cerca de um ano e meio a dois anos em uma fazenda, uma tentativa inicial em Excel e, depois, uma aplicação com processamento em lote e revisão humana."]),
        ]),
    dict(
        slug="blog-empresa-depende-do-dono.html",
        img="blog-1", date="8 de outubro de 2026", iso="2026-10-08",
        title="Sua empresa depende de você para tudo? 5 sinais de que o dono virou gargalo",
        desc="Cinco sinais de que o dono concentra informação e decisões demais, e como começar a tirar o peso do administrativo para sobrar tempo de crescer.",
        excerpt="Cinco sinais de que a empresa só funciona se o dono estiver por perto, e por onde começar a mudar isso.",
        body=[
            ("O dono que sabe de tudo", [
                "É comum, em empresas que cresceram a partir do trabalho do dono, que as informações importantes morem na cabeça dele. Isso funciona enquanto a operação é pequena, mas passa a travar o crescimento quando tudo precisa passar por uma única pessoa."]),
            ("Os 5 sinais", [
                _li([
                    "<strong>Funcionários procuram você para resolver tudo.</strong> Perguntas simples sobre fornecedor, valor ou documento acabam na sua mesa.",
                    "<strong>Documentos se acumulam.</strong> Notas, recibos e comprovantes ficam para depois, e o depois nunca chega.",
                    "<strong>Você não sabe quanto cada sócio gastou.</strong> Sem dados organizados, a resposta exige uma investigação.",
                    "<strong>Sobra pouco tempo para o que faz o negócio crescer.</strong> O administrativo consome o espaço de vender, negociar e planejar.",
                    "<strong>Sair de férias vira um risco.</strong> Quando você se ausenta, a rotina trava ou acumula."])]),
            ("Por que isso acontece", [
                "Não é falta de esforço. A rotina administrativa cresce junto com a empresa e raramente é desenhada: ela vai sendo improvisada. Cada solução provisória (uma planilha, um caderno, uma pasta no celular) resolve o dia, mas aumenta o custo de organizar depois."]),
            ("Como começar a sair desse lugar", [
                _li(["Escolha uma rotina que consome tempo e se repete, como lançar documentos ou conferir gastos.",
                     "Descreva como ela funciona hoje: o que chega, quem faz, onde trava e o que precisa sair no final.",
                     "Defina o que continua sendo decisão sua e o que pode ser executado por um fluxo organizado.",
                     "Automatize primeiro a parte mecânica, mantendo uma conferência humana nos pontos que envolvem dinheiro."])]),
            ("O papel da automação", [
                "Automatizar não é tirar o dono do negócio, é tirar do dono o que não precisa ser dele. A ideia é aliviar o peso de ter que saber e resolver tudo, para que o tempo volte para as atividades produtivas e para o crescimento.",
                "É exatamente essa a proposta da Kairos: mapear a rotina manual, construir o fluxo com IA e entregar uma estrutura que a empresa consiga usar sem depender de você."]),
        ]),
    dict(
        slug="blog-ia-le-notas-e-recibos.html",
        img="blog-3", date="5 de outubro de 2026", iso="2026-10-05",
        title="Como a IA lê notas, recibos e comprovantes em segundos (e você continua no controle)",
        desc="Entenda como a inteligência artificial identifica e extrai dados de notas fiscais, cupons e recibos, e como você mantém o controle de tudo o que vira registro.",
        excerpt="O que a IA consegue fazer com uma foto de nota fiscal e como você mantém a palavra final sobre cada registro.",
        body=[
            ("O que a IA faz com uma foto de documento", [
                "Em um fluxo bem desenhado, a leitura acontece em etapas. Primeiro, a IA identifica quais documentos financeiros aparecem na imagem e define a região de cada um. Depois, cada região é recortada a partir do original e lida separadamente, para que os dados de uma nota não se misturem com os da nota vizinha.",
                "Uma foto com duas notas e dois comprovantes, por exemplo, gera quatro resultados independentes."]),
            ("Que tipos de documento entram", [
                "DANFE, nota, cupom, recibo, recibo de serviço, comprovante de pagamento e anotação financeira manuscrita. O que não dá para ler com segurança fica em branco, para você preencher em vez de herdar um valor inventado."]),
            ("Alertas que trabalham por você", [
                _li(["CPF e CNPJ verificados um a um.",
                     "Valor bruto, desconto, juros e líquido comparados quando há dados suficientes.",
                     "Soma dos itens conferida com os totais do documento.",
                     "Nota de origem separada de comprovante de pagamento, para não contar o mesmo gasto duas vezes."])]),
            ("Por que você continua com a palavra final", [
                "A IA propõe, você decide. Cada documento chega com o recorte ampliado e os campos preenchidos, e você confirma ou ajusta em segundos. Só depois disso o dado vira registro. Assim você ganha a velocidade da automação sem abrir mão do controle."]),
            ("Boas práticas para um fluxo confiável", [
                _li(["Guarde sempre o arquivo original, sem substituí-lo.",
                     "Mantenha a leitura da IA separada do dado conferido, para poder comparar.",
                     "Registre quem criou, editou e aprovou cada despesa.",
                     "Deixe as diferenças de valores visíveis para você decidir, em vez de corrigir nos bastidores."])]),
        ]),
    dict(
        slug="blog-automacao-administrativa-roraima.html",
        img="blog-4", date="1 de outubro de 2026", iso="2026-10-01",
        title="Automação administrativa para empresas em Roraima: por onde começar",
        desc="Guia para donos de empresas do agronegócio e da pequena indústria em Boa Vista e Roraima sobre como escolher a primeira rotina administrativa para automatizar com IA.",
        excerpt="Como escolher a primeira rotina administrativa da sua empresa para automatizar, e o que perguntar antes de contratar.",
        body=[
            ("Quem mais ganha com automação administrativa", [
                "Empresas físicas que já operam e crescem, especialmente no agronegócio e na pequena indústria, tendem a acumular uma rotina administrativa pesada: notas fiscais, recibos, comprovantes, controle de materiais e de gastos por sócio. Quando o dono concentra tudo isso, a empresa depende dele para andar."]),
            ("Como escolher a primeira rotina", [
                "Procure uma tarefa que reúna quatro características:",
                _li(["se repete com frequência;", "tem volume suficiente para consumir horas;", "segue regras razoavelmente claras;", "causa uma dor real, como atraso, erro ou falta de informação."])]),
            ("Exemplos de rotinas candidatas", [
                _li(["organizar e lançar notas fiscais, recibos e comprovantes acumulados;",
                     "descobrir quanto cada sócio gastou em um período;",
                     "conferir informações de documentos antes de enviá-las ao contador;",
                     "montar uma base de consulta por fornecedor, categoria e período."])]),
            ("O que perguntar antes de contratar", [
                _li(["Quem confere os dados no fim, e como essa conferência acontece?",
                     "Onde os meus documentos ficam guardados e quem tem acesso?",
                     "Como e quando é feita a cobrança?",
                     "Haverá acompanhamento direto durante e depois da implementação?"])]),
            ("Atendimento perto de você", [
                "A Kairos atua inicialmente em Boa Vista, Roraima, com acompanhamento direto. O primeiro passo é uma conversa para entender a rotina da empresa e indicar, com honestidade, se faz sentido automatizá-la e por onde começar."]),
        ]),
    dict(
        slug="blog-raio-x-da-bagunca.html",
        img="blog-5", date="28 de setembro de 2026", iso="2026-09-28",
        title="Raio X da Bagunça: como mapear uma rotina manual antes de automatizar",
        desc="Conheça as quatro etapas do método Raio X da Bagunça, da conversa de diagnóstico à estrutura final de consulta, e as perguntas que ajudam a mapear uma rotina.",
        excerpt="As quatro etapas do método que usamos para sair do caos administrativo e chegar a uma estrutura que fica.",
        body=[
            ("Por que mapear antes de automatizar", [
                "Automatizar uma rotina mal compreendida só acelera a bagunça. O método Raio X da Bagunça existe para evitar isso: primeiro entender a rotina específica, depois construir o fluxo."]),
            ("Etapa 1: diagnóstico no caos", [
                "Uma conversa com o empresário para mapear a rotina que precisa ser organizada. Algumas perguntas ajudam:",
                _li(["O que chega, em que formato e com que frequência?", "Quem trata isso hoje?", "Onde trava ou se perde informação?", "O que precisa existir no final para você tomar decisões?", "Quais regras definem o que está certo ou errado?"])]),
            ("Etapa 2: prova ao vivo", [
                "Em vez de apresentar uma promessa, mostramos uma parte da solução funcionando com o problema real da empresa. Isso permite validar cedo se o caminho faz sentido."]),
            ("Etapa 3: execução sob medida", [
                "Construímos e ajustamos o fluxo aos documentos e às regras daquela empresa. Aqui entram a digitalização, a leitura por IA, a conferência dos dados e os ajustes combinados com o dono."]),
            ("Etapa 4: estrutura que fica", [
                "A entrega é uma interface e informações organizadas, pensadas para uso depois que o projeto termina. O objetivo é que a empresa continue consultando e usando a estrutura sem depender de você para tudo.",
                "Esse é o método por trás do Programa Kairos Cases: entramos na operação, mapeamos, provamos e entregamos uma estrutura que fica."]),
        ]),
]


def _article_html(a):
    out = ""
    for heading, parts in a["body"]:
        paras = "".join(p if p.startswith("<ul>") else f"<p>{p}</p>" for p in parts)
        out += f"        <section><h2>{heading}</h2>{paras}</section>\n"
    return out


def page_blog():
    feat, rest = ARTICLES[0], ARTICLES[1:]
    cards = ""
    for a in rest:
        cards += f"""<article class="blog-card">
  <a class="shot shot--link" href="{a['slug']}" aria-label="{escape(a['title'])}"><div class="shot__img"><img src="assets/img/{a['img']}.png" alt="" loading="lazy" width="485" height="244"></div></a>
  <div class="post-meta"><p class="post-date"><time datetime="{a['iso']}">{a['date']}</time></p><div><h2 class="post-title">{a['title']}</h2><p class="post-excerpt">{a['excerpt']}</p></div>
  <a class="btn btn--light post-link" href="{a['slug']}">Ler artigo</a></div>
</article>
"""
    h = head("Blog — Kairos | Automação administrativa com IA", "Conteúdo prático sobre organização de documentos, rotina administrativa e automação com inteligência artificial para empresas do agronegócio e da pequena indústria.", "blog")
    h += sub_section_open(nav("blog.html")) + f"""      <div class="text-block"><h1 class="h-lg">Blog da Kairos</h1>
        <p class="lead">Conteúdo prático sobre organização de documentos, rotina administrativa e automação com inteligência artificial, para donos de empresas que querem recuperar o tempo.</p></div>
      <article class="blog-feat">
        <a class="shot shot--link" href="{feat['slug']}" aria-label="{escape(feat['title'])}"><div class="shot__img"><img src="assets/img/{feat['img']}.png" alt="" width="485" height="244"></div></a>
        <div class="post-meta"><p class="post-date"><time datetime="{feat['iso']}">{feat['date']}</time></p>
          <div><h2 class="post-title post-title--lg">{feat['title']}</h2>
          <p class="post-excerpt post-excerpt--lg" style="margin-top:12px">{feat['excerpt']}</p></div>
          <a class="btn btn--light post-link" href="{feat['slug']}">Ler artigo</a></div>
      </article>
      <div class="blog-grid">
{cards}      </div>
""" + sub_section_close() + "\n" + cta() + "  </main>\n" + footer() + tail()
    write("blog.html", h)


def page_articles():
    for a in ARTICLES:
        ld = (f'<script type="application/ld+json">\n{{"@context":"https://schema.org","@type":"BlogPosting","headline":{_js(a["title"])},"datePublished":"{a["iso"]}",'
              f'"inLanguage":"pt-BR","author":{{"@type":"Organization","name":"Kairos Consultoria"}},"publisher":{{"@type":"Organization","name":"Kairos Consultoria"}},"description":{_js(a["desc"])}}}\n</script>\n')
        h = head(f"{a['title']} — Blog Kairos", a["desc"], "blog-detail", extra_head=ld)
        h += sub_section_open(nav("blog-" + a["slug"])) + f"""      <div class="text-block text-block--left" style="max-width:1188px">
        <a class="btn btn--light" href="blog.html">{icon("chev-left", "icon--16")}Voltar ao blog</a>
        <h1 class="h-lg">{a['title']}</h1>
        <p class="lead"><time datetime="{a['iso']}">{a['date']}</time></p>
      </div>
      <div class="shot shot--full" style="width:100%"><div class="shot__img"><img src="assets/img/{a['img']}.png" alt="" width="1170" height="535"></div></div>
      <div class="article">
{_article_html(a)}      </div>
""" + sub_section_close() + "\n" + cta() + "  </main>\n" + footer() + tail()
        write(a["slug"], h)


def _js(s):
    import json
    return json.dumps(s, ensure_ascii=False)


# --------------------------------------------------------------------------
# Contato
# --------------------------------------------------------------------------
def form_card():
    def select(label, name, options, req=True):
        opts = '<option value="">Selecione</option>' + "".join(f'<option>{o}</option>' for o in options)
        return f'<div class="field"><label for="f-{name}">{label}</label><select id="f-{name}" name="{name}" {"required" if req else ""}>{opts}</select><span class="msg" role="alert"></span></div>'

    def field(label, name, ph, typ="text", req=True, area=False, auto=""):
        ctl = (f'<textarea id="f-{name}" name="{name}" placeholder="{ph}" {"required" if req else ""}></textarea>' if area else
               f'<input id="f-{name}" name="{name}" type="{typ}" placeholder="{ph}" {"required" if req else ""} {auto}>')
        return f'<div class="field"><label for="f-{name}">{label}</label>{ctl}<span class="msg" role="alert"></span></div>'

    return f"""<form class="card form" id="contact-form" novalidate data-endpoint="" data-whatsapp="{PHONE_E164}">
        <div class="card__inner">
          {field("Nome", "name", "Seu nome", auto='autocomplete="name"')}
          {field("Cargo", "role", "Ex.: sócio, CEO, diretor", auto='autocomplete="organization-title"')}
          {field("E-mail", "email", "voce@empresa.com.br", "email", auto='autocomplete="email"')}
          {field("WhatsApp", "phone", "(95) 90000-0000", "tel", auto='autocomplete="tel"')}
          {field("Empresa", "company", "Nome da empresa", auto='autocomplete="organization"')}
          {select("Faturamento anual", "revenue", ["Abaixo de R$ 2 milhões", "De R$ 2 a 5 milhões", "De R$ 5 a 20 milhões", "Acima de R$ 20 milhões"])}
          {select("Pessoas em funções de escritório", "staff", ["Até 4", "De 5 a 10", "De 11 a 30", "Mais de 30"])}
          {select("Área prioritária para automatizar", "area", ["Administrativo e documentos", "Financeiro", "Comercial", "Atendimento", "Operações", "Pessoas e rotinas internas", "Outra"])}
          {select("Você é sócio ou CEO, ou decide o projeto?", "decision", ["Sim", "Decido junto com sócio(s)", "Não, preciso consultar alguém"])}
          {select("Autoriza documentarmos o case (dados sensíveis protegidos)?", "case", ["Sim", "Quero conversar antes"])}
          {field("Qual processo mais pesa hoje? (opcional)", "message", "Conte em poucas linhas.", req=False, area=True)}
          <p class="form__legal">Aplicar não é contratar. Ao enviar, abriremos o WhatsApp com a sua aplicação pronta. Veja a <a href="privacidade.html">Política de Privacidade</a>.</p>
          <div class="form__ok" role="status">{icon("check-circle", "icon--16")}<span>Aplicação pronta! Abrimos o WhatsApp para você enviar. Se preferir, escreva para {EMAIL}.</span></div>
          <button class="btn btn--dark btn--block" type="submit"><span>Enviar aplicação</span></button>
          <p class="form__trust">{icon("check-circle", "icon--14")} Aplicar não é contratar &nbsp; {icon("check-circle", "icon--14")} 4 vagas por mês &nbsp; {icon("check-circle", "icon--14")} Retorno pelo WhatsApp</p>
        </div>
      </form>"""


def page_contato():
    cards = (
        info_card("chat-oval", "WhatsApp", f'O caminho mais rápido: <a href="{WA_URL}" {EXT}>{PHONE_DISPLAY}</a>')
        + info_card("mail", "E-mail", f'<a href="mailto:{EMAIL}">{EMAIL}</a>')
        + info_card("instagram", "Instagram", f'<a href="{INSTAGRAM_URL}" {EXT}>@{INSTAGRAM_USER}</a>')
        + info_card("pin", "Onde atuamos", "Boa Vista, Roraima, com acompanhamento direto.")
    )
    h = head("Aplicação — Programa Kairos Cases | Kairos", "Aplique para o Programa Kairos Cases: implementação de IA na sua operação sem custo de implementação. 4 vagas por mês. Boa Vista, Roraima.", "contact")
    h += sub_section_open(nav("contato.html")) + f"""      <div class="text-block"><h1 class="h-lg">Aplique para ser um case</h1>
        <p class="lead">Aplicar não é contratar. A gente analisa e, se fizer sentido, liga para você.</p></div>
      <div class="media-card media-card--short" data-reveal>
        <img src="assets/img/about-hero.png" alt="" width="1188" height="763" loading="lazy">
        <div class="media-card__ov" style="top:35%"></div>
        <div class="media-card__cap"><div style="max-width:620px"><h3>Vamos conversar sobre a sua operação</h3><p>Boa Vista, Roraima.</p></div></div>
      </div>
      <div id="aplicacao" class="anchor"></div>
      {form_card()}
      <div class="card-grid card-grid--4" style="max-width:1100px">{cards}</div>
""" + sub_section_close() + "  </main>\n" + footer() + tail()
    write("contato.html", h)


# --------------------------------------------------------------------------
# Sobre
# --------------------------------------------------------------------------
def page_sobre():
    h = head("Sobre a Kairos — automação administrativa com IA em Boa Vista", "Conheça a Kairos Consultoria: mapeamos rotinas administrativas feitas à mão e implementamos soluções com IA, com conferência humana e acompanhamento direto.", "about")
    h += sub_section_open(nav("sobre.html")) + f"""      <div class="text-block"><h1 class="h-lg">Entramos na operação para tirar o peso das suas costas</h1></div>
      <div class="media-card">
        <img src="assets/img/about-hero.png" alt="" width="1188" height="763">
        <div class="media-card__ov"></div>
        <div class="media-card__cap"><div style="max-width:620px"><h3>Kairos Consultoria</h3><p>Automação administrativa com IA · Boa Vista, Roraima</p></div></div>
      </div>
""" + sub_section_close() + f"""
  <section class="section section--dark section--pad" aria-labelledby="mission-title">
    <div class="prose-block">
      <div class="tx"><h2 id="mission-title">O que nos move</h2><p>Devolver ao dono o tempo que a operação consome, redesenhando processos com IA.</p></div>
      <div class="tx"><h2>Como trabalhamos</h2><p>Entramos na operação, mapeamos os processos, construímos as soluções com o seu time e acompanhamos de perto.</p></div>
    </div>
  </section>

  <section class="section section--pad" aria-labelledby="who-title">
    <div class="prose-block" style="max-width:none">
      <div class="tx" style="max-width:720px;margin:0 auto"><h2 id="who-title">Quem somos</h2><p>A Kairos é feita por Rafael e sua parceira de negócio, em Boa Vista, Roraima, para donos de empresas do agronegócio e da pequena indústria.</p></div>
      <div class="who-cards">
        {info_card("share", "Rotina real, não teoria.", "Cada fluxo nasce dos seus documentos e regras.")}
        {info_card("scale", "A IA trabalha, você decide.", "A tecnologia trabalha, você tem a palavra final.")}
        {info_card("code", "Estrutura que fica.", "Interface pronta para a equipe usar depois.")}
      </div>
    </div>
  </section>
  </main>
{cta()}
{footer()}""" + tail()
    write("sobre.html", h)


# --------------------------------------------------------------------------
# Legais
# --------------------------------------------------------------------------
def legal(blocks):
    out = ""
    for sid, heading, body in blocks:
        out += f'<section{f" id=\"{sid}\"" if sid else ""}><h2>{heading}</h2>{body}</section>\n'
    return out


P = lambda t: f"<p>{t}</p>"


def page_termos():
    blocks = [
        (None, "Quem somos", P("Estes termos regulam o uso do site e a contratação de serviços da Kairos Consultoria (“Kairos”), com atuação inicial em Boa Vista, Roraima. Ao usar o site ou participar de um projeto, você declara que leu e concorda com eles.")),
        (None, "O que oferecemos", P("A Kairos mapeia rotinas administrativas feitas manualmente e implementa soluções com inteligência artificial para executá-las, incluindo, conforme cada projeto, diagnóstico, digitalização, validação de dados e interface de consulta. O escopo de cada projeto é combinado com o cliente antes do início.")),
        (None, "Programa Kairos Cases", P("No Programa Kairos Cases, a Kairos realiza a implementação sem cobrar por ela. Em contrapartida, o cliente fecha um contrato de 12 meses, de uma só vez, com mensalidade de R$ 5.000 (total de R$ 60.000), que paga o custo da inteligência artificial usada na operação do cliente (consumo de IA e infraestrutura) durante todo o período, e autoriza a documentação do case. A forma de pagamento e as demais condições são definidas por escrito antes do início.")),
        (None, "Critérios de seleção", P("A participação depende de aprovação. Os critérios atuais são faturamento de R$ 2 milhões por ano ou mais, pelo menos 5 pessoas em funções de escritório, sócio ou CEO envolvido no projeto, autorização para documentar o case e contrato de 12 meses. Enviar a aplicação não significa contratar.")),
        (None, "Documentação do case", P("A Kairos poderá divulgar a história do projeto (problema, solução e resultado) após combinar o que será publicado. Dados sensíveis, informações confidenciais e questões estratégicas do cliente permanecem protegidos.")),
        (None, "Deslocamento", P("Quando as visitas presenciais ocorrerem fora de Boa Vista, as despesas de deslocamento e hospedagem ficam por conta do cliente.")),
        (None, "Conferência humana e limites da IA", P("A leitura por inteligência artificial pode conter erros. Verificações automáticas ajudam, mas não garantem que um documento foi lido corretamente. Por isso, a conferência humana faz parte do serviço, e o cliente é responsável por confirmar os dados antes de utilizá-los para fins financeiros, fiscais ou contábeis.")),
        (None, "Responsabilidades do cliente", P("O cliente se compromete a fornecer documentos e informações verdadeiros e obtidos de forma legítima, a indicar uma pessoa responsável pela conferência e a comunicar ajustes necessários durante o projeto.")),
        (None, "Dados e documentos", P("Os documentos e dados enviados pelo cliente continuam sendo do cliente. Os arquivos originais são preservados e não são substituídos por versões tratadas. O tratamento de dados pessoais está descrito na <a href=\"privacidade.html\">Política de Privacidade</a>.")),
        (None, "Confidencialidade", P("A Kairos trata como confidenciais as informações e os documentos a que tiver acesso para executar o projeto e não os utiliza para outras finalidades.")),
        (None, "Propriedade intelectual", P("Marca, textos, layout e materiais do site pertencem à Kairos ou são utilizados com autorização, e não podem ser reproduzidos sem permissão.")),
        (None, "Limitação de responsabilidade", P("A Kairos não responde por decisões tomadas com base em dados não conferidos pelo cliente, nem por indisponibilidades de serviços de terceiros, como provedores de IA, fora do seu controle razoável.")),
        (None, "Alterações destes termos", P("Podemos atualizar estes termos. A versão vigente é sempre a publicada nesta página, com a data de atualização indicada.")),
        (None, "Lei aplicável e contato", P("Aplica-se a legislação brasileira. Dúvidas podem ser enviadas para <a href=\"mailto:" + EMAIL + "\">" + EMAIL + "</a>.")),
    ]
    h = head("Termos de uso — Kairos", "Termos de uso do site e da contratação de serviços da Kairos Consultoria. Atualizado em 12 de outubro de 2026.", "terms")
    h += "<!-- Texto-base elaborado a partir do posicionamento da empresa; recomenda-se revisão jurídica antes da publicação. -->\n"
    h += sub_section_open(nav("")) + f"""      <div class="text-block"><h1 class="h-lg">Termos de uso</h1><p class="lead">Atualizado em 12 de outubro de 2026</p></div>
      <div class="legal">
{legal(blocks)}      </div>
""" + sub_section_close() + "  </main>\n" + footer() + tail()
    write("termos.html", h)


def page_privacidade():
    blocks = [
        (None, "Quem é o responsável", P("A Kairos Consultoria, com atuação inicial em Boa Vista, Roraima, é a responsável pelo tratamento dos dados descritos aqui, nos termos da Lei Geral de Proteção de Dados (LGPD, Lei nº 13.709/2018). Contato: <a href=\"mailto:" + EMAIL + "\">" + EMAIL + "</a>.")),
        (None, "Dados que coletamos no site", P("Quando você envia a aplicação ou usa o formulário, podemos receber nome, cargo, e-mail, telefone/WhatsApp, empresa, faturamento anual, tamanho da equipe e o conteúdo da sua mensagem. Esses dados são fornecidos por você. O site não exige cadastro.")),
        (None, "Dados de projetos contratados", P("Na execução de um projeto, tratamos documentos enviados pelo cliente, como notas fiscais, recibos e comprovantes, que podem conter dados pessoais (por exemplo, nomes e CPF/CNPJ). Esses dados são usados apenas para executar o projeto contratado.")),
        (None, "Para que usamos os dados", P("Responder ao seu contato, elaborar o diagnóstico e a proposta, executar e acompanhar o projeto e cumprir obrigações legais. Não vendemos dados pessoais.")),
        (None, "Como os documentos são tratados", P("Os arquivos originais ficam armazenados localmente, com identificação individual e verificação de integridade, e não são alterados. Para a leitura de imagens, um provedor externo de inteligência artificial é utilizado, e as credenciais de acesso ficam na configuração do servidor. Os resultados da leitura passam por conferência humana.")),
        (None, "Compartilhamento", P("Compartilhamos dados apenas com prestadores necessários à execução do serviço (como o provedor de IA e o WhatsApp, quando você opta por falar por lá) e quando exigido por lei.")),
        (None, "Por quanto tempo guardamos", P("Mantemos os dados pelo tempo necessário para a finalidade para a qual foram coletados, para o cumprimento de obrigações legais e para o exercício regular de direitos. Contatos sem andamento podem ser excluídos a seu pedido.")),
        (None, "Seus direitos", P("Você pode solicitar confirmação de tratamento, acesso, correção, anonimização ou eliminação de dados, portabilidade, informação sobre compartilhamento e revogação de consentimento, escrevendo para <a href=\"mailto:" + EMAIL + "\">" + EMAIL + "</a>.")),
        (None, "Segurança", P("Adotamos medidas razoáveis para proteger os dados, como controle de acesso e armazenamento local dos originais. Nenhum sistema é totalmente livre de riscos, e por isso a conferência e o acompanhamento são parte do serviço.")),
        ("cookies", "Cookies e serviços de terceiros", P("Este site não usa cookies de rastreamento ou publicidade. As fontes de texto são carregadas do Google Fonts, o que pode envolver o envio do seu endereço IP a esse serviço. Ao clicar nos links para WhatsApp ou Instagram, você passa a se submeter às políticas dessas plataformas.")),
        (None, "Alterações", P("Podemos atualizar esta política. A versão vigente é sempre a publicada nesta página.")),
    ]
    h = head("Política de Privacidade — Kairos", "Como a Kairos Consultoria trata dados pessoais do site e de projetos, de acordo com a LGPD. Atualizado em 12 de outubro de 2026.", "privacy")
    h += "<!-- Texto-base elaborado a partir do posicionamento da empresa; recomenda-se revisão jurídica antes da publicação. -->\n"
    h += sub_section_open(nav("")) + f"""      <div class="text-block"><h1 class="h-lg">Política de Privacidade</h1><p class="lead">Atualizado em 12 de outubro de 2026</p></div>
      <div class="legal">
{legal(blocks)}      </div>
""" + sub_section_close() + "  </main>\n" + footer() + tail()
    write("privacidade.html", h)


def page_404():
    h = head("Página não encontrada — Kairos", "A página que você procura não existe. Volte para a página inicial da Kairos.", "nf-page")
    h = h.replace('<link rel="icon"', '<base href="/"><link rel="icon"', 1)  # a 404 é servida em qualquer URL
    h += sub_section_open(nav("")) + f"""      <div class="nf">
        <div class="nf-art" aria-hidden="true"><div class="shadow"></div><div class="base"></div><div class="paper"></div><div class="code">404</div><div class="scrap"></div></div>
        <div class="text-block"><h1 class="h-lg">Ops! Página não encontrada</h1>
          <p class="lead">Sem problema: o que você procura provavelmente está na página inicial.</p></div>
        <a class="btn btn--dark" href="index.html">{icon("chev-left", "icon--16")}VOLTAR AO INÍCIO</a>
      </div>
""" + sub_section_close() + "  </main>\n" + footer() + tail()
    write("404.html", h)


OLD_FILES = ["about.html", "blog-detail.html", "careers.html", "contact-form.html", "contact.html", "download.html",
             "integrations.html", "pricing.html", "privacy.html", "terms.html"]

def write_seo_files():
    pages = ["", "oferta", "ruraldocs", "sobre", "blog", "contato", "termos", "privacidade"] + [a["slug"][:-5] for a in ARTICLES]
    robots = "User-agent: *\nAllow: /\n"
    if SITE_URL:
        robots += f"\nSitemap: {SITE_URL}/sitemap.xml\n"
        urls = "".join(f"  <url><loc>{SITE_URL}/{p}</loc></url>\n" for p in pages)
        write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n")
    elif os.path.exists(os.path.join(ROOT, "sitemap.xml")):
        os.remove(os.path.join(ROOT, "sitemap.xml"))
    write("robots.txt", robots)


if __name__ == "__main__":
    for f in OLD_FILES:
        p = os.path.join(ROOT, f)
        if os.path.exists(p):
            os.remove(p)
            print("removido", f)
    page_index()
    page_oferta()
    page_ruraldocs()
    page_sobre()
    page_blog()
    page_articles()
    page_contato()
    page_termos()
    page_privacidade()
    page_404()
    write_seo_files()
