# hormozi-gtm

**Alex Hormozi's complete go-to-market methodology — $100M Offers, $100M Leads, $100M Money Models — distilled into an AI-ready playbook. Works with Claude, ChatGPT, Gemini, Cursor, any LLM — or your own eyes.**

Not a summary. Not a chatbot that quotes the books. A working operator: give your AI this playbook plus your offer, your funnel, or your pricing, and it either **builds** using Hormozi's frameworks or **audits** against his checklists — with his actual numbers, thresholds, and decision rules.

> "Make people an offer so good they would feel stupid saying no" — now enforceable by your AI, on every offer you write.

## Who this is for

- **Founders & solopreneurs** — pressure-test your offer and pricing before you spend a dollar on ads.
- **Marketers & growth teams** — audit funnels and ad copy against the Core Four and the Value Equation instead of vibes.
- **Sales teams** — structured upsell/downsell sequences (never discount the same thing — change what they get or how they pay).
- **Agencies & consultants** — run client offers through a consistent, named methodology with scored checklists.
- **Anyone using an AI assistant for business** — turn a generic chatbot into a blunt, numbers-driven GTM operator.
- **Readers of the books** — the fastest reference to every framework, threshold, and checklist in one place.

## What it does

Three books, operationalized as one chained system:

| Module | Book | Job |
|---|---|---|
| **Offers** | $100M Offers (2021) | Make the thing worth buying — Value Equation, Grand Slam Offers, premium pricing, scarcity/urgency/bonuses/guarantees, MAGIC naming |
| **Leads** | $100M Leads (2023) | Get strangers to want it — the Core Four (warm/cold × 1-to-1/1-to-many), lead magnets, Rule of 100, the four Lead Getters (referrals, employees, agencies, affiliates) |
| **Money Models** | $100M Money Models (2025) | Get paid fast enough that growth self-finances — Client-Financed Acquisition, attraction/upsell/downsell/continuity offers sequenced in three stages |

They chain deliberately: a Grand Slam Offer is what your lead engine advertises, and the money model sequences that offer over time so acquisition pays for itself. Weakness in any one caps the other two — and the playbook tells your AI to identify which one is your constraint before optimizing anything.

## Two modes

**APPLY** — build or improve something:
> "Build me an offer for my B2B consulting service"
> "Design a lead engine for my agency"
> "How should I structure upsells for my gym?"

Produces concrete, usable output for *your* business — a stacked offer with named components and dollar values, a sequenced money model, a channel plan — not book advice.

**REVIEW** — audit existing work:
> "Here's my landing page offer — what's wrong with it?"
> "Audit my funnel"
> "Run my pricing past Hormozi"

Runs the matching checklist, scores each item pass/fail/partial, and gives a specific before→after fix for every gap.

## What makes it useful

- **Quantitative.** It uses Hormozi's actual rules: LTGP:CAC ≥ 3:1, 30-day payback (Client-Financed Acquisition), anchor at 5–10×, rollover ≥ 4× credit, Rule of 100, give:ask ≥ 3:1, churn-by-billing-cadence data, refund red-lines. Give it real numbers and it does the math.
- **Blunt.** It instructs the AI to push back on weak offers, price-cutting, vanity fears, and optimizing the wrong lever — the way the books do.
- **Layered.** `SKILL.md` is the compact working method (~200 lines — fits any context window). The `references/` files hold the full distilled methodology per book — frameworks, step-by-step procedures, decision rules, review checklists, common mistakes, glossaries — loaded only when depth is needed.
- **Model-agnostic.** It's plain markdown. Nothing here is tied to one AI vendor.

## Structure

```
hormozi-gtm/
├── SKILL.md                  # working playbook: modes, modules, thresholds, checklists
└── references/
    ├── offers.md             # $100M Offers — full method
    ├── leads.md              # $100M Leads — full method
    └── money-models.md       # $100M Money Models — full method
```

## Use it with…

### Claude (Claude Code)
```bash
mkdir -p ~/.claude/skills/hormozi-gtm
cp -r SKILL.md references ~/.claude/skills/hormozi-gtm/
```
Claude triggers it automatically on offer / lead-gen / monetization tasks.

### Claude (Desktop / Cowork / claude.ai)
Package and install as a custom skill:
```bash
zip -r hormozi-gtm.skill SKILL.md references/
```
Install the `.skill` file via the skills menu — or just attach the four files to a Project.

### ChatGPT
- **Custom GPT:** create a GPT, paste `SKILL.md` into Instructions, upload the three `references/` files into Knowledge.
- **Quick use:** paste `SKILL.md` at the start of a conversation, attach references as files.

### Gemini
Create a **Gem** with `SKILL.md` as the instruction and the references as attached knowledge — or paste inline.

### Cursor / Windsurf / IDE agents
Drop the folder into your project and reference it as a rules/context file (e.g. `.cursor/rules/`) — useful when building landing pages, pricing pages, and checkout flows: the agent critiques the copy as it writes it.

### Any other LLM / your own app
It's plain markdown. Load `SKILL.md` as the system prompt; retrieve `references/*.md` on demand (they're structured for RAG — each has a contents line, numbered sections, and a glossary).

### No AI at all
Read it as a condensed operator's manual. The checklists in each reference file work fine on paper: print the Offer audit, score your current offer, fix what fails.

## Example session

> **You:** Here's my offer: "Personal training, $80/session, book online." What's wrong?
>
> **AI (with this playbook):** Running the Offer audit… You're selling a commodity by the hour — price-comparable in one glance, which is the race to the bottom. Scored against the checklist: no dream outcome (you sell sessions, not a transformation), no risk reversal, no scarcity, no stack, hourly pricing caps your LTGP… Here's the rebuild: a 12-week named program with an outcome guarantee, priced 4× your current monthly revenue per client, with a payment-plan downsell — and the math on why your LTGP:CAC now clears 3:1…

## The venture trilogy

Three sibling playbooks form a pipeline:

1. **[thiel-zero-to-one](https://github.com/wowsergei/thiel-zero-to-one)** — *what to build*: the 7 Questions scorecard, monopoly vs competition, secrets.
2. **hormozi-gtm** (this repo) — *how it makes money*: Grand Slam Offers, lead engines, money models.
3. **[get-backed](https://github.com/wowsergei/get-backed)** — *how to package it and raise*: pitch decks, investor pipelines, asks, closing.

They hand off: pass Thiel's 7 Questions first (no offer fixes a commodity business), build the Grand Slam Offer and money model here, then let get-backed turn the numbers into a deck and a raise.

## Scope & honest limits

- The frameworks are US-sales-culture native. The playbook explicitly tells the AI to adapt tone and tactics to the user's market and legal context (guarantees, giveaways/sweepstakes are regulated differently across jurisdictions).
- It's a methodology tool, not business or legal advice. Numbers in the references are Hormozi's published claims, reproduced as method inputs.
- Public edition: the reference files restate the methodology in original wording and contain no book excerpts.

## Attribution & copyright

This is an original distillation of the *methodology* taught in Alex Hormozi's books — frameworks, procedures, and decision rules restated in original wording. It is **not** a reproduction of the books and contains no substantial excerpts. Ideas and methods are not subject to copyright; the books' text is © Alex Hormozi / Acquisition.com. The books go far deeper than any distillation — stories, proofs, worked examples — and are free/cheap. Buy them:

- [$100M Offers](https://www.acquisition.com/books) (2021)
- [$100M Leads](https://www.acquisition.com/books) (2023)
- [$100M Money Models](https://www.acquisition.com/books) (2025)

This project is not affiliated with or endorsed by Alex Hormozi or Acquisition.com.

## Contributing

PRs welcome — especially: corrections where the distillation misstates the method, checklist improvements from real-world use, and worked examples (your offer before → after, with the audit that got you there).

## License

Methodology distillation and playbook text: MIT. Underlying frameworks remain the intellectual work of their author — see attribution above.
