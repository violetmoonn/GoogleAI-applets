# Business, e-commerce & marketing

Fifteen upgrade prompts for the [YOUR BRAND] business and growth apps. Duplicate projects are merged. Each prompt stands alone: paste it into a new AI Studio Build project. Every prompt tells the app to use the newest Gemini Pro model in AI Studio and to get the API key from the environment, never hard-coded.

---

## [YOUR BRAND] Flagship Site (was: [YOUR BRAND] website replacement; Founder's note page; Website template)

**What changes:**
- Three separate drafts become one editorial brand site with a home page, a seasonal drop page, the founder's note, an archive since 2000 and a stockist/contact page.
- A built-in content editor stores pages as JSON, so the owner can change copy, drops and images without touching code.
- Shopify stays the checkout. Product cards link out with "Shop on Shopify" deep links, and an optional Buy Button embed snippet can be added.
- A restock countdown and a waitlist capture turn seasonal restocks into launch events.
- A Gemini copy assistant writes drop stories and alt text in the brand voice.

**How to compare:**
1. "Write a homepage for a fashion brand founded in 2000 with seasonal restocks." Winning: a working, navigable site with real sections and a countdown, against a static mockup or a block of text.
2. "Add a new Spring drop with 6 products." Winning: done in the editor in under 2 minutes, with alt text generated and no code edited.
3. "Make it work on a phone." Winning: a mobile layout that scores well in Lighthouse for accessibility and keeps the full-bleed imagery.

**Paste into AI Studio Build:**
```
Build "[YOUR BRAND]", an editorial flagship website for a fashion/lifestyle brand founded in 2000 that sells through seasonal restocks. Checkout stays on Shopify; this site tells the story and drives traffic there.

Visual direction: quiet-luxury editorial. Off-white (#F5F2EC) and ink black, one oxblood accent. A high-contrast serif for display type (e.g. Playfair Display or Cormorant) with a grotesk body font. Full-bleed imagery, generous whitespace, slow fade and parallax motion that respects prefers-reduced-motion.

Pages (hash router):
1. Home: hero video or image, current drop teaser with a live restock countdown, "Since 2000" timeline strip, newsletter/waitlist form.
2. Drop: product grid with lookbook toggle (grid / full-screen story). Each product has name, price, sizes, images, and a "Shop on Shopify" button linking to a configurable product URL.
3. Founder's Note: long-form letter layout with drop cap, pull quotes and signature image.
4. Archive: seasons since 2000 as a filterable masonry grid.
5. Contact & Stockists.

Admin mode (toggle at /#/admin, gated by a local passphrase): edit all content as forms backed by one JSON site config saved in localStorage. Import/export the config as JSON. Upload images as data URLs, with a warning when they get too large.

AI assistant in admin, using the newest Gemini Pro model in AI Studio (key from the environment, never hard-coded): "Write drop story", "Write product description", "Generate alt text from image", "Rewrite in brand voice". Return structured JSON {headline, body, bullets[], altText} that is validated before insertion. Show skeleton loaders, and on error show a retry toast that keeps the user's draft.

States: empty drop ("Next restock coming soon" with waitlist), image load fallbacks, offline banner.

Accessibility: semantic landmarks, focus-visible styles, AA contrast, keyboard-operable lookbook, alt text required before publishing.

Mobile: sticky bottom "Shop the drop" bar, swipeable lookbook, 44px tap targets.

Export: "Download static site" builds a zip of HTML/CSS plus the JSON config, ready for any static host. Include a README panel explaining how to point the domain at it while Shopify handles checkout.
```

---

## Shopify Growth Studio (was: Shopify store customizer with instructions; Shopify website assistant; Simple e-commerce store redesign; E-commerce store analyzer for conversion; "Guarantee 6 sales a day" planner)

**What changes:**
- Five tools become one workspace that runs Audit → Plan → Assets → Track.
- The app reads the store from a URL using Google Search grounding plus what the owner pastes in (theme screenshots, product copy, analytics numbers), then scores conversion across 8 categories with evidence.
- The "6 sales a day" idea becomes a target calculator. It works back from the goal through traffic, conversion rate and AOV to show the gap and the levers. It makes no promises.
- An asset generator writes product copy, a homepage hero, email flows and ad hooks, and gives step-by-step Shopify admin instructions for each change.
- A weekly tracker logs real numbers and compares them with the plan.

**How to compare:**
1. Paste a store URL and ask "Why isn't this converting?" Winning: a scored audit that cites specific pages and elements, ranked by impact and effort, instead of generic CRO tips.
2. "I want 6 sales a day, I get 400 visitors/day at 0.8% CVR and $85 AOV." Winning: exact gap math, scenarios and a 30-day plan with an honest confidence note.
3. "Rewrite my top product page." Winning: copy in the brand voice plus Shopify theme editor click-paths for each change.

**Paste into AI Studio Build:**
```
Build "Growth Studio", a Shopify conversion audit and action-plan workspace for a small fashion brand. It never promises sales outcomes. It shows the math, the evidence and the next actions.

Visual direction: dark "trading-floor calm". Charcoal (#111315) panels, mint (#3DDC97) for positive deltas, amber for warnings. Inter with tabular numerals and dense but airy cards.

Flow (left stepper; on mobile, a top segmented control):
1. Connect: enter a store URL and optionally paste product copy, upload theme screenshots, and enter metrics (sessions/day, conversion rate, AOV, add-to-cart rate, return rate). Show an empty state with a sample store so people can try it.
2. Audit: using the newest Gemini Pro model in AI Studio with Google Search grounding plus image understanding of screenshots, score 8 categories 0–100: first impression, navigation, product page, trust & social proof, pricing/offer, checkout friction, mobile UX, speed signals. Each finding: {category, severity, evidence, recommendation, impact 1–5, effort 1–5, sourceUrls[]}. Request JSON output with a response schema and validate it; show a radar chart and an impact/effort matrix.
3. Target Calculator: the user enters a daily orders goal. Compute the required sessions at the current CVR, the required CVR at current traffic, and blended scenarios. Show sliders and a gap bar. Display a permanent note: "Projections, not guarantees."
4. Action Plan: a 30-day kanban generated from the findings, each card with Shopify admin click-path instructions (Online Store → Themes → Customize …), a checklist and a status.
5. Assets: generate product descriptions, hero headline variants, a 3-email welcome flow, abandoned-cart copy and 10 ad hooks in a chosen brand voice. Show side-by-side variants with copy buttons.
6. Track: weekly log of real metrics with a line chart of plan vs actual.

Loading: streaming progress steps ("Reading homepage…"). Errors: per-section retry that keeps the other results. If grounding cannot reach the store, ask for screenshots instead.

Persistence: projects in IndexedDB; export the audit as PDF and the plan as CSV/Markdown. Key from the environment, never hard-coded.

Accessibility: charts have data-table alternatives, full keyboard support and AA contrast.
```

**Why reframed:** No tool can guarantee a set number of sales, so the planner now shows the traffic and conversion math needed to reach the goal, and makes no promise that it will be reached.

---

## Affiliate Outreach & Media Kit Studio (was: Affiliate/growth-expert outreach tool; Affiliate media pack download builder)

**What changes:**
- Outreach and the media kit become one pipeline: find partners, then pitch them, then send the kit.
- Partner discovery uses Search grounding and returns public profiles with source links, fit scores and reasons.
- Personalized pitch sequences come in 3 tones, with clear disclosure and opt-out lines.
- A media kit builder produces a branded PDF and a one-page web kit with commission terms, assets and brand guidelines.
- A simple CRM board tracks status and follow-up dates.

**How to compare:**
1. "Find 10 mid-tier fashion creators who'd fit a streetwear-luxe brand." Winning: real, cited public profiles with fit reasoning, not invented handles.
2. "Write a pitch to creator X." Winning: references their actual recent public content, with a follow-up sequence and a clear CTA.
3. "Make an affiliate media pack." Winning: a downloadable, designed PDF in minutes, against a text outline.

**Paste into AI Studio Build:**
```
Build "Partner Studio", an affiliate and creator outreach tool with a built-in media kit builder for a fashion/lifestyle brand.

Visual direction: glossy magazine meets CRM. Cream background, black type, hot-coral accent, rounded 20px cards, a condensed display font (e.g. Anton) for headers and DM Sans for body.

Screens:
1. Brand Profile: name, story, price range, audience, commission %, cookie window, discount code format. Saved locally.
2. Discover: the user describes the ideal partner (niche, platform, size, region). Use the newest Gemini Pro model in AI Studio with Google Search grounding to find publicly listed creators, blogs and affiliate publishers. Return JSON per schema {name, platform, publicUrl, audienceEstimate, niche, fitScore 0-100, fitReasons[], publicContactMethod, sources[]}. Show only items that have source URLs, and label estimates as estimates. Never invent emails; show "public contact method" only when it was found.
3. Pipeline: kanban (Prospect → Pitched → Replied → Negotiating → Active → Declined), cards with notes, next follow-up date and an overdue badge.
4. Pitch Composer: choose a partner and tone (warm, data-led, playful). Generate a subject line, a first email and 2 follow-ups that reference the partner's public work, include an honest opt-out line, and stay under 150 words each. One-click copy and "open in mail app" (mailto). The app never sends email itself.
5. Media Kit Builder: drag-and-drop sections (brand story, audience stats, commission table, product highlights, image grid, brand do's/don'ts, contact). Live preview, then export a PDF (print stylesheet) and a shareable single-file HTML kit. AI can draft each section.

States: empty pipeline with a "Discover your first partners" CTA; loading skeletons with progress text; when grounding returns nothing, suggest broadening the criteria; parse errors retry once and then show the raw text.

Persistence: IndexedDB; import/export pipeline CSV.

Accessibility: kanban is operable with the keyboard (move with arrow keys), ARIA live region for status changes.

Mobile: the pipeline becomes a stacked list with a status filter, and the composer is full-screen.

Key from the environment, never hard-coded.
```

---

## Talent Scout (was: Head-hunter tool for finding freelancers/affiliate marketers — 2 versions)

**What changes:**
- Both versions merge into one sourcing workspace for freelancers and affiliate marketers.
- It starts with a role brief builder that turns a vague need into a scored rubric.
- Grounded search covers public portfolios and marketplaces, and every result comes with sources.
- Side-by-side candidate comparison is scored against the rubric, with interview questions and a paid test-task generator.
- It uses only public data, and it drafts outreach without sending anything.

**How to compare:**
1. "I need a Shopify email-marketing freelancer, $40/hr max." Winning: a structured brief plus real, cited candidate profiles ranked by rubric.
2. "Compare these 3 portfolios." Winning: a scored matrix with evidence per criterion.
3. "Give me a test task." Winning: a scoped paid task with acceptance criteria and a grading guide.

**Paste into AI Studio Build:**
```
Build "Talent Scout", a sourcing assistant for finding freelancers and affiliate marketers from public information.

Visual direction: Scandinavian recruiting tool. Warm white, slate text, cobalt accent, soft shadows, Manrope font, generous 8px grid and pill tags.

Screens:
1. Brief Builder: chat-style wizard asking for role, outcomes, budget, timezone, must-haves and nice-to-haves. Using the newest Gemini Pro model in AI Studio, output JSON {roleTitle, summary, rubric:[{criterion, weight, whatGoodLooksLike}], redFlags[], suggestedRate}. Weights are editable and must sum to 100.
2. Search: with Google Search grounding, find publicly listed professionals (portfolio sites, marketplace profiles, published case studies). JSON per candidate {name, headline, publicProfileUrl, location, rateIfPublic, evidence:[{claim, sourceUrl}], rubricScores{}, overallScore}. Discard any candidate without a source URL. Add a "Paste a profile URL or text" option for manual candidates.
3. Shortlist: table and card toggle, sort by score, star, notes, status (Found → Contacted → Interviewing → Trial → Hired/Passed).
4. Compare: pick 2–4 candidates for a side-by-side rubric matrix with evidence tooltips and an AI summary of trade-offs.
5. Toolkit per candidate: tailored outreach message (copy only, nothing sent), 8 interview questions mapped to rubric criteria, and a paid test task with scope, deliverable, time box and grading rubric.

Ethics guardrails shown in the UI: public professional info only; no scraping of private data; respect platform terms; candidates are contacted through their published channels.

States: an empty state with an example brief; a progress list while searching; when results are thin, suggest relaxing criteria; on network or parse errors, show inline retry and keep the brief.

Persistence: IndexedDB. Export the shortlist to CSV and the brief to Markdown/PDF.

Accessibility: full keyboard nav, labelled controls, score bars with text values.

Mobile: single column, sticky "Compare (n)" tray.

Key from the environment, never hard-coded.
```

---

## Yes Deck (was: Pitch-deck builder — customizable PowerPoint to get a "yes")

**What changes:**
- A narrative-first flow: the app interviews the founder, builds a story arc, then lays out slides.
- Market data is researched with Search grounding and every number on a slide is cited.
- A real .pptx export (via PptxGenJS) gives editable slides, alongside PDF.
- A "Skeptical investor" review scores each slide and lists likely objections.
- Speaker notes come with a rehearsal timer.

**How to compare:**
1. "Make a seed pitch deck for a fashion brand going DTC-global." Winning: a downloadable, editable .pptx with designed slides and cited market sizes, against an outline.
2. "Critique my deck as a skeptical VC." Winning: a per-slide score, objections and suggested rewrites applied with one click.
3. "Change the theme and reorder slides." Winning: instant, with no lost content.

**Paste into AI Studio Build:**
```
Build "Yes Deck", a pitch deck builder that produces editable PowerPoint files designed to win a "yes".

Visual direction: Swiss-poster precision. Pure white canvas, jet black, one signal color the user chooses, a big grotesk type scale (e.g. Space Grotesk), hairline rules and an asymmetric grid. The app UI uses the same language.

Flow:
1. Interview: 10 focused questions (problem, customer, solution, traction, business model, market, competition, team, ask, use of funds). Accept pasted notes or uploaded docs/text.
2. Story Arc: the newest Gemini Pro model in AI Studio proposes a narrative (e.g. "insight → proof → scale") as JSON {slides:[{id, type, headline, bullets[], visual:{kind: chart|stat|quote|image|table, data}, speakerNotes, sources[]}]}, validated with a schema. Headlines are assertions, not labels.
3. Research: a "Fill market data" button uses Google Search grounding for TAM/SAM/SOM, comparables and trends; each figure carries a source footnote. Unsourced numbers get a yellow "verify" badge.
4. Editor: slide thumbnails in a left rail (drag to reorder), canvas in the center, inspector on the right (layout variants, theme, chart data). 6 themes. Inline editing.
5. Skeptic Review: an AI "skeptical investor" scores each slide 1–10 on clarity, evidence and ask, lists likely objections, and offers rewrites with Accept/Reject buttons.
6. Rehearse: presenter view with speaker notes, a per-slide timer and a total target time.

Export: .pptx using PptxGenJS with native text boxes, real charts and notes; PDF via print; JSON project file.

States: empty project with 3 sample decks; generation shows slide-by-slide progress; on failure keep partial slides and retry the missing ones.

Persistence: autosave to IndexedDB with version history (last 20 snapshots).

Accessibility: keyboard reordering, alt text for every image and chart, an AA contrast checker that warns on theme colors.

Mobile: review and rehearse modes; editing is simplified to text.

Key from the environment, never hard-coded.
```

---

## Term Sheet Match (was: "Dating app for venture capital")

**What changes:**
- The swipe idea is kept but backed by real thesis matching: stage, sector, check size, geography and portfolio conflicts.
- An investor list is researched from public sources with citations; it does not rely on a fabricated database.
- A match score with "why" explanations, plus a warm-intro path planner.
- A tailored teaser email and a meeting prep brief for each match.
- A founder pipeline CRM tracks every investor conversation.

**How to compare:**
1. "Find seed investors for a fashion-tech brand in Europe." Winning: real, cited funds with thesis fit and portfolio conflicts flagged.
2. "Why is this a match?" Winning: a criteria-level explanation with sources.
3. "Prep me for a call with fund X." Winning: a one-page brief on partner focus, recent deals and likely questions.

**Paste into AI Studio Build:**
```
Build "Term Sheet Match", a founder-investor matching app with a playful swipe interface backed by serious research.

Visual direction: late-night members' club. Deep navy (#0B1026), champagne gold accents, soft glassmorphism cards, a refined serif for names (e.g. Fraunces) and Inter for data. Card-swipe animations that respect reduced motion.

Screens:
1. Founder Profile: company, one-liner, stage, sector tags, raise amount, geography, traction metrics, deck link. Saved locally.
2. Discover: the newest Gemini Pro model in AI Studio with Google Search grounding finds investors (funds and angels) with public theses that match the profile. JSON schema per investor {name, firm, type, stages[], sectors[], checkSizeRange, geographies[], recentDeals:[{company, date, sourceUrl}], potentialConflicts[], matchScore 0-100, matchReasons[], sources[]}. Investors without sources are not shown. Data is labelled "from public sources as of <date>; verify before outreach".
3. Swipe Deck: cards show the score ring, top 3 reasons and a conflict warning. Swipe right to shortlist, left to pass, up to save for later. Buttons are provided for non-gesture and keyboard users (←/→/↑).
4. Matches: list with filters. Each match has a "Why" breakdown, a warm-intro planner (ask the user for mutual connections and suggest an intro request text), a teaser email draft (copy only), and a "Prep brief" (partner focus, recent deals, 8 likely questions with suggested answers).
5. Pipeline: Contacted → Meeting → Diligence → Term sheet → Closed/Passed, with dates and notes, plus a summary of the round total.

States: empty Discover with a "Complete your profile" checklist; a searching animation with real progress text; graceful fallback when grounding fails (manual add investor); schema-validation retry.

Persistence: IndexedDB. Export the pipeline to CSV and briefs to PDF.

Accessibility: everything that works by swiping also works with buttons, screen-reader announcements on decisions, AA contrast on gold.

Mobile-first: swipe deck full-screen, bottom tab bar.

Key from the environment, never hard-coded.
```

---

## Opt-In Talent Collective (was: In-house outsourcing agency that gathers people's data to build something bigger)

**What changes:**
- The app becomes a consent-first talent pool: people choose to join, choose what they share, and can export or delete their data at any time.
- Members build skills profiles with granular visibility toggles (public / collective only / private).
- AI turns a project brief into a team proposal from consenting members, with a skills-gap analysis.
- A transparent "how your data is used" page and a consent log are built in.
- A project board coordinates the assembled team.

**How to compare:**
1. "Assemble a team to launch a capsule collection in 8 weeks." Winning: roles, matched opted-in members, gaps and a timeline.
2. "Delete my data." Winning: a one-click export and delete with confirmation, which ChatGPT/Claude cannot demonstrate as a working app.
3. "Show what data is shared with project leads." Winning: per-field visibility shown clearly.

**Paste into AI Studio Build:**
```
Build "The Collective", a consent-based talent and skills pool where people opt in to be matched to projects. It is an in-house agency run on explicit consent.

Visual direction: warm co-op. Sand and terracotta palette with sage accents, a rounded humanist sans (e.g. Nunito) with an editorial serif for headings, illustrated avatars, soft paper texture.

Screens:
1. Join: a clear explainer of what is collected, why, and who sees it. Consent checkboxes are unchecked by default, one per purpose (matching, contact by project leads, inclusion in aggregate stats). Members can join without granting optional purposes.
2. My Profile: skills with proficiency levels, portfolio links, availability, rate range, location/timezone. Each field has a visibility toggle (Public / Collective / Private). Includes "Export my data (JSON)" and "Delete my profile" with a confirm dialog. Every consent change is recorded in a consent log the member can see.
3. Directory (for project leads): search and filter members by skill, availability and timezone, showing only fields visible to the viewer's role.
4. Project Brief → Team: a lead describes a project. The newest Gemini Pro model in AI Studio returns JSON {roles:[{title, skills[], hours}], proposedTeam:[{memberId, role, fitReasons[]}], gaps:[{skill, suggestion}], timeline:[{week, milestone}]}. It may only use members who granted matching consent. Invitations are sent as in-app requests that members accept or decline.
5. Project Board: tasks per role with statuses and a simple timeline.
6. Transparency: aggregate skill-coverage charts (only from members who consented to stats), plus a plain-language data policy.

Roles: member and lead (local role switcher for the demo). Data lives in IndexedDB on this device; explain that a real deployment needs a backend with authentication.

States: empty directory with "Invite your first members"; matching loader; when no matches, show the gap analysis instead; errors are recoverable without losing the brief.

Accessibility: every consent control is labelled and keyboard reachable, plus a plain-language summary.

Mobile: card-based directory, bottom sheet filters.

Key from the environment, never hard-coded.
```

**Why reframed:** Collecting people's data needs their knowledge and consent, so the app now runs on opt-in profiles with export and deletion controls instead of gathering data about people.

---

## Verity — Bulk Data Verifier (was: Large-scale data verification app)

**What changes:**
- Large CSV/XLSX files are processed in the browser using Web Workers and streamed parsing, so the UI does not freeze.
- Deterministic checks run first (formats, duplicates, ranges, referential checks), and AI is used only for fuzzy or factual checks.
- Search-grounded fact verification runs on sampled or selected rows, with citations and confidence.
- A rule builder plus a review queue with accept/fix/reject for each issue.
- The app exports a cleaned file plus an audit report.

**How to compare:**
1. Upload a 50k-row product or customer file. Winning: profiling in seconds with a column health dashboard, while a chatbot chokes on the size.
2. "Verify these 20 company addresses/websites are current." Winning: per-row verdicts with sources.
3. "Fix the inconsistent size labels." Winning: suggested normalization rules applied in bulk, with a before/after diff.

**Paste into AI Studio Build:**
```
Build "Verity", a large-scale data verification and cleaning app that runs in the browser.

Visual direction: precision lab instrument. Graphite UI, electric-blue focus color, green/amber/red status chips, JetBrains Mono for data and Inter for UI, dense virtualized tables.

Flow:
1. Import: drag-drop CSV, TSV, XLSX (SheetJS) or JSON, or paste text. Parse in a Web Worker with streaming (PapaParse) and a progress bar with row counts. Handles 500k+ rows using a virtualized grid.
2. Profile: per-column type inference, null %, unique %, pattern samples, outliers and a health score. Clicking a column filters the grid.
3. Rules: a no-code rule builder (required, regex, email/URL/phone format, numeric range, enum list, date format, uniqueness, cross-column conditions). An "Suggest rules" button sends the column profile and a 50-row sample to the newest Gemini Pro model in AI Studio and gets JSON {rules:[{column, type, params, rationale}]} back; the user approves each rule.
4. Verify: deterministic rules run locally in the worker. An optional "Fact check" mode verifies selected rows (e.g. business still operating, website live, address exists) with Google Search grounding, in batches of 10 with rate limiting, returning JSON {rowId, field, verdict: confirmed|contradicted|unverifiable, evidence, sourceUrls[], confidence}. Show a cost/time estimate before running.
5. Review Queue: issues grouped by rule, with bulk accept-fix, edit inline, ignore. AI normalization suggestions (e.g. "XL", "x-large" → "XL") are shown as a before/after diff.
6. Export: cleaned file (same format), issues CSV, and a PDF audit report (summary stats, rules applied, fact-check citations).

States: empty state with a sample dataset; cancelable long runs; partial results kept on error; retry failed batches only.

Persistence: datasets and sessions in IndexedDB, with a storage usage meter.

Accessibility: grid navigable with arrow keys, status conveyed by text plus color, announced progress.

Mobile: profile and review only (cards), with a note that large imports work best on desktop.

Privacy note in the UI: data stays local except for rows the user explicitly sends for AI checks.

Key from the environment, never hard-coded.
```

---

## Paper Desk — Market Research & Paper Trading (was: Stock prediction & trading helper)

**What changes:**
- Prediction becomes research: grounded news summaries, fundamentals snapshots, and bull/bear cases with sources.
- Paper trading uses a virtual portfolio with trade journaling. The app places no real-money trades and links to no broker.
- A trade journal records your reasoning, and the app reviews it for biases.
- Price data is user-supplied (CSV import) or grounded and timestamped, and labelled as possibly delayed.
- A persistent "Educational tool — not financial advice" frame appears throughout.

**How to compare:**
1. "Summarize what moved [ticker] this week." Winning: a dated, cited summary with a separate bull and bear case.
2. "Paper-buy 10 shares and track it." Winning: a working virtual portfolio with P&L and a journal entry.
3. "Review my last 10 paper trades." Winning: pattern analysis (e.g. selling winners early) using your own logged data.

**Paste into AI Studio Build:**
```
Build "Paper Desk", a market research and paper-trading dashboard for learning. It is educational only: no real-money trading, no brokerage connections, and no buy/sell recommendations.

Visual direction: Bloomberg-terminal-inspired but modern. Near-black background, amber and cyan data accents, IBM Plex Mono for numbers and IBM Plex Sans for text, tight grid panels with resizable splits.

A persistent banner: "Educational research and simulation. Not financial advice. Data may be delayed or incomplete."

Screens:
1. Watchlist: add tickers. Each row shows the last known price with a timestamp and source, the daily change and a sparkline. Prices come from Google Search grounding or from user-imported CSV price history; when data is stale, show it as stale.
2. Research: for a ticker, the newest Gemini Pro model in AI Studio with Google Search grounding returns JSON {asOf, summary, keyEvents:[{date, headline, sourceUrl}], fundamentalsSnapshot:{...}, bullCase[], bearCase[], risks[], openQuestions[]}. The schema forbids price targets and buy/sell ratings, and the app strips any that appear. Cards show citations.
3. Paper Portfolio: virtual cash (default $100,000). Place simulated market or limit orders at the last known price; positions, P&L, allocation donut and history. A reset button.
4. Journal: each paper trade requires a thesis, confidence level and exit plan. After it closes, record the outcome.
5. Coach: AI reviews the journal for behavioral patterns (overconfidence, holding losers, FOMO entries), citing the user's own entries. It does not suggest specific securities.
6. Learn: glossary tooltips on every metric.

States: empty watchlist with sample tickers; loading skeletons; grounding failures show "couldn't verify — try again or import CSV"; schema validation with one retry.

Persistence: IndexedDB. Export portfolio, trades and journal to CSV; research notes to Markdown.

Accessibility: charts include data tables, gains/losses use +/− signs plus color, keyboard shortcuts listed in a help sheet.

Mobile: tabbed panels, swipe between watchlist, portfolio and journal.

Key from the environment, never hard-coded.
```

**Why reframed:** No app can reliably predict stock prices, and personalized trading signals amount to financial advice, so the app now does sourced research and practice trading with virtual money only.

---

## EV Lab — Poker Equity & Decision Trainer (was: Poker best-move equation)

**What changes:**
- An exact and Monte Carlo equity engine runs in a Web Worker for hand vs hand and hand vs range.
- A visual 13×13 range editor with presets.
- EV math is shown step by step (pot odds, required equity, fold equity, EV of call/fold/raise), so the user learns the equation.
- Drill mode generates spots, scores your answers and tracks weak areas.
- AI explains the reasoning in plain language; the math engine is deterministic and does not depend on the AI.

**How to compare:**
1. "AKs vs QQ preflop — equity?" Winning: an exact answer (about 46/54) computed instantly, against an estimate.
2. "Should I call a pot-size river bet with a bluff-catcher?" Winning: the full EV breakdown with required equity, plus range-based equity.
3. "Train me on turn decisions." Winning: an adaptive drill with scoring and progress tracking.

**Paste into AI Studio Build:**
```
Build "EV Lab", a Texas Hold'em equity calculator, EV solver and decision trainer for study.

Visual direction: casino-noir precision. Deep green felt gradient, ivory cards with crisp suit glyphs, gold accents, Inter plus a monospace font for numbers, tactile chip and card animations (reduced-motion aware).

Core engine (pure TypeScript, in a Web Worker; no AI involved): a hand evaluator, exact enumeration when combinations ≤ 2M, otherwise Monte Carlo with a configurable number of iterations and a standard-error display. Supports 2–6 players, hand vs hand, hand vs range, dead cards and board cards.

Screens:
1. Calculator: card picker (tap a slot, then choose from a 52-card grid; used cards are disabled), board slots, per-player equity bars with win/tie %, and hand-class breakdown on the river.
2. Range Editor: 13×13 grid with drag-select, weight slider, presets (tight/loose open ranges by position), combo counter and % of hands; ranges are saved and named.
3. EV Solver: inputs for pot, bet size, stack sizes, villain range and fold-frequency estimate. Shows pot odds, required equity, actual equity, and EV(call), EV(fold), EV(raise) with each formula written out step by step. Highlights the highest-EV option with a sensitivity slider ("this changes if villain folds less than X%").
4. Explain: the newest Gemini Pro model in AI Studio turns the computed numbers into a plain-language explanation. It receives the numbers as structured input and must not change them. Response is JSON {summary, keyFactors[], commonMistake, ruleOfThumb}.
5. Trainer: random spots (preflop, flop, turn, river); the user picks an action or estimates equity; score by EV loss; spaced-repetition focus on weak spot types; streaks and an accuracy chart.

Note in the UI: "For study and training. Don't use during real-money online play where site rules prohibit assistance tools."

States: invalid input messages (duplicate cards, missing hands), progress for long simulations with a cancel button; when AI is unavailable, the math still works.

Persistence: saved ranges, spots and trainer stats in localStorage; export/import as JSON.

Accessibility: cards announced as "Ace of spades", keyboard card entry (type "As Kd"), colorblind four-color deck option.

Mobile: stacked calculator, bottom sheet card picker.

Key from the environment, never hard-coded.
```

---

## Vault Ledger — Subscriptions & Accounts Tracker (was: Subscription & login tracker)

**What changes:**
- Subscriptions are tracked with renewal dates, monthly cost normalization, annual totals and category breakdowns.
- Login details are never stored in plain text. The default is a deep link to the user's password manager entry. An optional encrypted notes vault uses Web Crypto (PBKDF2 + AES-GCM) and a master passphrase that is never saved.
- Renewal reminders via .ics export and browser notifications.
- AI pulls subscriptions out of pasted receipts or statements and suggests what to cancel.
- Encrypted backup export.

**How to compare:**
1. Paste 3 receipt emails. Winning: subscriptions extracted into structured entries with renewal dates, ready to confirm.
2. "What am I paying per year, and what can I cut?" Winning: totals by category plus specific, cost-ranked suggestions.
3. "Store my login." Winning: the app refuses to store it in plain text and shows a password-manager link or a passphrase-encrypted field, where a chatbot can only offer advice.

**Paste into AI Studio Build:**
```
Build "Vault Ledger", a private subscription and account tracker. Security rule: it never stores passwords or secrets in plain text.

Visual direction: Swiss-bank minimalism. Soft white and deep forest green, brass accents, a serif for figures (e.g. Libre Caslon) with Inter for UI, subtle embossed cards, a lock motif.

Screens:
1. Dashboard: monthly and annual spend (all amounts normalized to monthly), upcoming renewals in the next 30 days as a timeline, category donut, "free trial ending" alerts.
2. Subscriptions: list and card view with name, logo initial, plan, price, currency, billing cycle, next renewal, payment method label (e.g. "Visa ending ••42" typed by the user — never full numbers), category, status (active/trial/paused/cancelled), cancel URL, and account login reference.
3. Login reference: by default, a field for the password manager item link or name (e.g. "Open in 1Password/Bitwarden"). Optional "Secure note" encrypted client-side: derive a key from a master passphrase with Web Crypto PBKDF2 (≥310,000 iterations, random salt) and encrypt with AES-GCM (random IV). Never persist the passphrase or the derived key; auto-lock after 5 minutes idle. Show a clear warning that a forgotten passphrase means the data cannot be recovered.
4. Import: paste receipt or statement text. The newest Gemini Pro model in AI Studio extracts JSON {items:[{name, amount, currency, cycle, nextRenewal, category, confidence}]}. The prompt tells the model to ignore and never return any card numbers or passwords. The user confirms each item before it is saved. Never send encrypted fields to the AI.
5. Insights: AI cost-cutting suggestions (overlaps, unused services the user flags, cheaper annual plans), ranked by savings.
6. Reminders: browser notifications, plus .ics export of all renewal dates.

States: empty dashboard with "Add your first subscription" and "Import from receipts"; locked-vault state; wrong passphrase error with no hint leakage; extraction failure falls back to manual entry.

Persistence: IndexedDB. Export as CSV (no secrets) or as a fully encrypted backup file.

Accessibility: labelled currency inputs, keyboard-friendly date pickers, AA contrast.

Mobile: renewal timeline first, floating add button.

Key from the environment, never hard-coded.
```

**Why reframed:** Passwords stored in plain text can be stolen easily, so the app now links to a password manager or encrypts secrets on the device with a passphrase only the user knows.

---

## Inbox Architect — Branded Addresses & Email Writer (was: "Make as many business emails as I want without paying"; "Generate real emails" ×2)

**What changes:**
- Planning unlimited addresses on the owner's own domain (sales@, press@, restock@, per-campaign aliases) using free forwarding such as Cloudflare Email Routing, with no paid mailboxes.
- Step-by-step DNS/MX setup guides, plus "send as" setup in Gmail for replying from aliases.
- An alias map with routing rules, purpose tags and SPF/DKIM/DMARC checklist status.
- An AI email-writing assistant with brand voice and templates for wholesale, press, customer service and restock announcements.
- It creates no accounts at third-party providers and no fake identities.

**How to compare:**
1. "Set up 15 addresses on [yourbrand].com for free." Winning: an alias plan, a routing table and exact setup steps checked against current docs.
2. "Write a wholesale pitch from wholesale@." Winning: on-brand, sendable copy with a subject line and follow-ups, saved as a template.
3. "Why are my emails going to spam?" Winning: a personalized SPF/DKIM/DMARC checklist with grounded guidance.

**Paste into AI Studio Build:**
```
Build "Inbox Architect", a planner for unlimited branded email addresses on the user's own domain using free email forwarding, combined with an AI email-writing assistant. Scope: only the user's own domain. The app does not create accounts on any email provider and does not generate fake identities.

Visual direction: architectural blueprint. Deep blueprint blue with white line art, a grid-paper background, cyan highlights, IBM Plex Sans with a mono font for DNS records, diagram-style routing visuals.

Screens:
1. Domain Setup: the user enters their domain and current DNS host. A wizard explains forwarding options (e.g. Cloudflare Email Routing, or a registrar's free forwarding). The newest Gemini Pro model in AI Studio with Google Search grounding fetches current setup steps and cites them, with a "last checked" date. Shows the MX/TXT records to add in copyable code blocks and a checklist that the user ticks off.
2. Alias Planner: create addresses (sales@, press@, wholesale@, restock-spring26@…), each with a purpose, destination inbox and tags. A visual routing diagram shows alias → destination. Suggests a naming convention and campaign-specific aliases for tracking. Bulk-add from a list.
3. Reply-As Guide: steps to reply from an alias in Gmail ("Send mail as") or similar, with SMTP notes, sourced through grounding.
4. Deliverability: SPF, DKIM and DMARC checklist with explanations and example records for the chosen setup; status toggles set by the user.
5. Writer: choose sender alias, purpose (wholesale pitch, press release, customer service reply, restock announcement, partner follow-up), tone and key points. Gemini returns JSON {subjectOptions[3], body, followUps[], previewText}. Features: brand voice profile, saved templates, a spam-trigger word checker, and copy or mailto buttons. The app never sends email itself.

States: empty planner with suggested starter aliases; grounding failure falls back to general guidance marked "verify with your provider"; validation for domain and alias syntax.

Persistence: localStorage/IndexedDB. Export the alias table as CSV, the DNS checklist as PDF, and templates as JSON.

Accessibility: copy buttons announce success, diagrams have text equivalents, keyboard-complete wizard.

Mobile: wizard steps as full-screen cards.

Key from the environment, never hard-coded.
```

**Why reframed:** Creating accounts in bulk with third-party email providers breaks their terms and looks like fake identities, while forwarding aliases on your own domain give you as many branded addresses as you want, legitimately and for free.

---

## Deep Source — Cited Research Assistant (was: "Make something that outperforms Grok")

**What changes:**
- Every answer is grounded with Google Search, with inline numbered citations and a sources panel.
- A research plan step comes first: the question is broken into sub-questions you can see and edit.
- Claims are scored by how well they are supported, and conflicting sources are flagged.
- Answers come in modes: quick answer, deep report, compare, timeline.
- A saved research library, follow-up threads and export.

**How to compare:**
1. "What changed in Shopify's checkout extensibility this year?" Winning: dated, cited specifics, with conflicts noted.
2. "Compare 3 email platforms for a small fashion brand." Winning: a sourced comparison table plus a recommendation and caveats.
3. "Give me a timeline of [industry event]." Winning: a dated timeline with a source for every row.

**Paste into AI Studio Build:**
```
Build "Deep Source", a research assistant whose answers are always web-grounded and cited.

Visual direction: scholarly modern. Paper-white reading surface, ink-navy text, a highlighter-yellow accent for citations, Source Serif for answers and Inter for UI, a wide reading column with a sources sidebar.

Core: the newest Gemini Pro model in AI Studio with Google Search grounding on every request. Use the grounding metadata to attach numbered inline citations [1] to sentences, linked to the sources panel (title, domain, date if available, favicon initial).

Flow:
1. Ask: a large input with mode chips: Quick Answer, Deep Report, Compare, Timeline, Fact Check.
2. Plan (Deep/Compare/Timeline): show the generated sub-questions as editable chips; the user can approve, edit or add before running.
3. Run: a streaming progress list ("Searching: …", "Reading 7 sources…").
4. Answer: rendered Markdown with citations. Each paragraph has a support badge (well-supported / single-source / conflicting) computed from the grounding data. Conflicting claims open a side-by-side view of the sources. Compare mode renders a table; Timeline mode renders a vertical dated timeline. Request structured JSON where the output is parsed (e.g. {rows:[{item, criteria:{}, sources[]}]}) and validate it.
5. Follow-ups: 3 suggested next questions; threaded conversation keeps context.
6. Library: saved research with search, tags and pinned items.

Honesty rules in the system prompt: say "I couldn't find reliable sources" rather than guess; show the date of time-sensitive facts; distinguish fact from analysis.

States: empty home with example questions; no-results state with search refinement tips; rate-limit and network errors with retry and preserved question; partial answers kept.

Export: Markdown (with footnotes), PDF, and copy-with-citations.

Persistence: IndexedDB library.

Accessibility: citations reachable by keyboard and announced as "source 3: domain", adjustable reading size, high-contrast mode.

Mobile: sources open as a bottom sheet; mode chips scroll horizontally.

Key from the environment, never hard-coded.
```

---

## Live Lens Translator (was: Real-time page translation Chrome extension — 2 versions)

**What changes:**
- Both versions merge into one web app that translates pasted text, URLs (through grounding or fetched content) and screenshots/photos (OCR via Gemini vision).
- A side-by-side or overlay view keeps the layout, and a glossary keeps brand terms like [YOUR BRAND] untranslated.
- Translation streams in paragraph by paragraph, with a tone/formality setting.
- An appendix covers packaging the same core as a Chrome extension.
- History and saved glossaries per language pair.

**How to compare:**
1. Upload a screenshot of a Japanese product page. Winning: translated text overlaid in position, with the product names from the glossary preserved.
2. Paste a long article. Winning: streaming paragraph-aligned output you can toggle side by side.
3. "Translate my product descriptions into 5 languages." Winning: batch output with glossary consistency, exported as CSV.

**Paste into AI Studio Build:**
```
Build "Live Lens", a real-time translation web app for text, web pages and screenshots.

Visual direction: Tokyo transit signage. Crisp white and graphite, a vivid vermilion accent, bilingual-friendly fonts (Noto Sans family for wide script coverage), pill tabs, smooth split-pane transitions.

Inputs (tabs):
1. Text: paste or type; translation streams as you type (debounced 600ms), paragraph-aligned side by side.
2. URL: enter a URL. Use the newest Gemini Pro model in AI Studio with URL context/Google Search grounding to retrieve the readable content, then translate preserving headings, lists and links. If retrieval fails, ask the user to paste the page text.
3. Image: upload, paste or capture a screenshot. Gemini vision returns JSON {blocks:[{text, translated, bbox:{x,y,w,h}}]}, rendered as an overlay on the image (toggle original/translated/both) with text that can be selected and copied.
4. Batch: paste rows or upload CSV (e.g. product descriptions) and choose multiple target languages; returns a table.

Controls: auto-detect source language, target language, formality (casual/neutral/formal), domain (fashion retail, legal, casual chat), and a Glossary (term → fixed translation or "do not translate", e.g. brand names) that is injected into every request and checked after output, with violations highlighted.

Output features: hover a sentence to highlight its source; "explain this phrase" popover; copy; text-to-speech using the browser speechSynthesis API.

States: empty state with demo samples per tab; streaming progress; unsupported image or too-large file messages; partial output kept on error with "continue".

Persistence: history and glossaries in IndexedDB; export translations as TXT/Markdown/CSV and overlay images as PNG.

Accessibility: lang attributes set on output, screen-reader friendly side-by-side reading order, keyboard tab switching.

Mobile: camera capture for the Image tab, stacked panes with a swap toggle.

Key from the environment, never hard-coded.

Appendix: also create /extension with a Manifest V3 scaffold (content script that collects visible text nodes, a side panel showing translations, and a service worker calling a user-configured backend proxy so no API key ships in the extension), plus README steps to load it unpacked.
```

**Chrome extension appendix (for the owner):** AI Studio Build produces web apps, so treat the extension as a second step. Download the project, open the `/extension` folder, check `manifest.json` (Manifest V3, `sidePanel`, `activeTab`, `scripting` permissions), and keep the Gemini key on a small server proxy (for example a Cloud Run function), never inside the extension. Then go to `chrome://extensions`, turn on Developer mode, choose "Load unpacked", and select the folder. Publish to the Chrome Web Store only after adding a privacy policy that says which page text is sent for translation.

---

## Fair Floor — Meeting Talk-Time Balancer (was: "A tool that makes people shut up")

**What changes:**
- Tracks speaking time per participant with tap-to-switch, or optional on-device mic level detection, and shows a live balance chart.
- Gentle, neutral cues: a soft visual "wrap-up" glow and time-box chimes, with no shaming.
- Agenda time-boxing with a focus timer per item and a "parking lot" for tangents.
- An AI-written polite interruption phrase bank and a post-meeting summary of the talk-time balance.
- Works offline, and no audio is ever recorded or uploaded.

**How to compare:**
1. "Run a 30-min meeting with 5 people and 4 agenda items." Winning: a live working timer with per-person balance, not tips.
2. "Give me a polite way to cut off someone who's rambling in a client call." Winning: context-specific phrases saved to a quick-access deck.
3. "How balanced was today's meeting?" Winning: a per-person chart, the dominance share and suggestions for next time, exportable.

**Paste into AI Studio Build:**
```
Build "Fair Floor", a meeting talk-time balancer and focus timer that helps everyone get heard and politely keeps discussions on track.

Visual direction: calm studio. Soft dusk gradient (lavender to peach), each participant a distinct accessible color, large rounded type (e.g. Outfit), breathing-circle animations (reduced-motion aware), big touch targets suited to a shared screen.

Screens:
1. Setup: meeting name, participants (name plus color), agenda items with time boxes, and a fairness target (e.g. no one above 35%). Templates: standup, 1:1, client call, brainstorm.
2. Live Meeting:
   - Participant tiles; tap a tile to mark who is speaking (keyboard: number keys 1–9). Optional "auto-detect speech" uses the Web Audio API mic level on-device only to detect that someone is talking (the user still assigns who). Nothing is recorded, stored or uploaded, and this is explained in the UI.
   - A live donut of talk-time share; a tile glows amber when its speaker passes the target and pulses softly on long uninterrupted turns (configurable, e.g. 2 min).
   - Agenda timer for the current item, with a soft chime at 1 min left and an overtime indicator. "Parking lot" button captures tangents.
   - Phrase Deck: a drawer of polite interruption and redirection phrases.
3. Phrase Studio: the user describes the context (client, boss, peer; tone). The newest Gemini Pro model in AI Studio returns JSON {phrases:[{text, situation, tone}]}, saved into the deck.
4. Summary: per-person talk time, longest turns, agenda overruns, parking-lot items, and an AI recap with 3 neutral suggestions for next time (no blame language).
5. History: past meetings with trends.

Focus mode: Pomodoro-style solo timer with a "do not disturb" full-screen view.

States: empty history; mic permission denied falls back to tap mode; if AI fails, use the built-in default phrases.

Persistence: localStorage/IndexedDB. Export the summary as PDF/Markdown and data as CSV.

Accessibility: never color alone (names plus percentages), screen-reader announcements for time-box alerts, chimes with a visual equivalent, full keyboard control.

Mobile: grid of tiles fills the screen; landscape tablet layout for a meeting table.

Key from the environment, never hard-coded.
```

**Why reframed:** A tool built to silence people would cause friction, while a neutral talk-time balancer gets the same result (shorter monologues, more balanced meetings) in a way everyone in the room can accept.
