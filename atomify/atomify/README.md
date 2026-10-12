# Kairos Consultoria — site estático (HTML/CSS/JS puro)

Sem framework e sem build no servidor: a pasta inteira é o site.

## Rodar localmente
```
npx http-server -p 8765 -c-1
```
Abra http://127.0.0.1:8765

## Subir na Vercel
**Pelo painel (recomendado, com GitHub):**
1. Suba esta pasta (`atomify`) em um repositório do GitHub.
2. Na Vercel: *Add New → Project* → importe o repositório.
3. Framework Preset: **Other**. Build Command e Output Directory: deixe em branco.
4. *Deploy*. Depois, em *Settings → Domains*, aponte o domínio.

**Pela linha de comando:**
```
cd atomify
vercel          # primeiro deploy (preview)
vercel --prod   # produção
```

`vercel.json` já liga URLs limpas (`/oferta` em vez de `/oferta.html`), cabeçalhos de segurança e cache.
`.vercelignore` deixa de fora `tools/` e as imagens que nenhuma página usa.

## Editar o conteúdo
Todo o texto está em `tools/build.py` (os `.html` são gerados). Depois de editar:
```
py tools/build.py
```
Dados de contato (e-mail, WhatsApp, Instagram) ficam no topo do arquivo.

## Depois de ter o domínio
```
KAIROS_SITE_URL=https://seudominio.com.br py tools/build.py
```
gera o `sitemap.xml` e liga o `robots.txt` a ele. Envie o sitemap no Google Search Console.

## Estrutura
- `index`, `oferta`, `ruraldocs`, `sobre`, `blog` + 5 artigos, `contato`, `termos`, `privacidade`, `404`
- `css/style.css`, `js/main.js` (menu, FAQ, animações, formulário que abre o WhatsApp)
- `assets/` imagens e logos

## Antes de publicar
- Revisar `termos.html` e `privacidade.html` com um advogado (texto-base).
- O formulário não tem servidor: ele abre o WhatsApp com a aplicação pronta. Para receber por e-mail/CRM, preencha `data-endpoint` no `<form id="contact-form">` (em `tools/build.py`).
- Não há imagem de compartilhamento (Open Graph). Se quiser prévia bonita no WhatsApp/LinkedIn, adicione `og:image`.
