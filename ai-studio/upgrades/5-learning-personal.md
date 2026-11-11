# Learning, career & personal

Each section below has one paste-ready prompt. Open the existing project in AI Studio Build, paste the prompt (or start a new Build app with it), and let it regenerate. Every prompt stands alone. None of them contains an API key; AI Studio supplies the Gemini connection.

---

## Clausewise — Contract Drafting & Review Workbench (was: "Recreate Spellbook AI for legal professionals but make it better")

**What changes:**
- An original product with its own name and identity. It is a three-pane workbench (document, AI review, clause library) and not a chat box.
- Clause-level redlines with accept/reject per change and real tracked-change rendering. You can export them to .docx-compatible HTML and to Markdown.
- A playbook editor where a lawyer writes firm positions ("cap liability at 12 months' fees"). The AI then scores each clause against those positions with a risk level and cites the exact text.
- A persistent clause library with versions, tags and fallback positions, all stored locally in IndexedDB.
- A constant "for licensed legal professionals; not legal advice" framing, plus an audit trail of every AI suggestion.

**How to compare:**
1. Paste a 4-page vendor MSA and ask for a review against "customer-side, mid-market SaaS" positions. Winning means every risky clause is flagged with a severity, the quoted source text, the playbook rule it breaks, and a proposed redline you can accept in one click. ChatGPT or Claude would give back a prose summary.
2. Ask for a mutual NDA drafted from your library's preferred clauses. Winning means the draft is assembled from your saved clauses (the app shows which ones) and is not generic boilerplate.
3. Reject two redlines, accept three, then export. Winning means the exported document shows the tracked changes correctly and you can undo any decision.

**Paste into AI Studio Build:**
```
Build "Clausewise", an original AI contract drafting and review workbench for licensed lawyers and in-house counsel. It is not a clone of any existing product: use your own name, branding and layout. Show a persistent footer: "Assists legal professionals. Not legal advice. Verify all output."

VISUAL DIRECTION: quiet luxury legal. Ivory paper background (#FBF9F4), deep ink navy text, oxblood accent for high risk, brass accent for medium risk. Serif document font (Source Serif or similar), clean sans for UI. Generous margins. Documents look like real paper on a soft shadow.

SCREENS:
1. Matters dashboard: cards per matter (client, counterparty, contract type, status, risk score ring). Empty state shows an illustrated "Start your first review" with "Paste contract" and "Upload .txt/.docx/.pdf text" buttons.
2. Review workbench with 3 panes. Left: the document, with clauses auto-segmented and numbered. Center: an AI findings list grouped by severity (High/Medium/Low/OK). Right: tabs for Clause Library and Playbook. Clicking a finding scrolls to and highlights the clause.
3. Redline mode: inline tracked changes (strikethrough red, insertions underlined green). Accept/Reject per change, Accept All, and full undo/redo history (Ctrl+Z/Ctrl+Shift+Z).
4. Playbook editor: rules with a position, a fallback position, a walk-away point and a severity. Ship 3 sample playbooks (SaaS customer, SaaS vendor, Mutual NDA).
5. Drafting: pick a contract type and parties. The AI assembles a draft from the user's library clauses first and labels any newly generated clause "AI-drafted, review".

AI: use the newest Gemini Pro model in AI Studio. Request structured JSON with a response schema: findings[] {clauseId, quote, issue, playbookRuleId, severity, rationale, proposedRedline {deleteText, insertText}}. Validate the JSON. If parsing fails, retry once, then show a non-blocking error card with "Retry". Never invent quotes: discard any finding whose quote is not found verbatim in the document. Show a skeleton loader with the stage name ("Segmenting clauses", "Checking playbook").

PERSISTENCE: IndexedDB for matters, documents, library (with versions) and an audit log of each AI suggestion and the user's decision. Export a matter as a redlined HTML (Word-openable), Markdown, or a JSON backup. Import the JSON backup.

QUALITY: fully keyboard navigable (J/K to move between findings, A/R to accept/reject), ARIA labels, WCAG AA contrast, visible focus rings. Mobile: the panes become tabs with a sticky findings bar. Handle documents with more than 30 pages by chunking with a progress indicator.
```

---

## Earned — Honest Job-Landing Studio (was: Job interview tool: get any interview without lying on the resume)

**What changes:**
- One pipeline from target role → evidence bank → outreach → application → interview prep → follow-up. It replaces a set of disconnected generators.
- A "Truth Ledger": every claim the AI writes must link to a real item in your evidence bank. Unsupported claims are blocked and shown in red.
- Company research uses Search grounding with clickable sources, so outreach references real recent news.
- A mock interview mode with timed answers, STAR scoring and follow-up questions, plus a kanban tracker that persists locally.

**How to compare:**
1. Give a target posting and your real background, then ask for a LinkedIn message to the hiring manager. Winning means the message cites a sourced company fact, every claim about you maps to a ledger item, and there is no inflation.
2. Ask it to "make me sound more senior". Winning means it reframes impact honestly and refuses to fabricate titles or numbers, explaining why. A generic chatbot will often embellish.
3. Run a 5-question behavioral mock interview. Winning means per-answer STAR scores, a specific rewrite, and a saved session you can revisit.

**Paste into AI Studio Build:**
```
Build "Earned", an honest job-landing studio that takes a candidate from first outreach to interview-ready without ever fabricating experience.

VISUAL DIRECTION: confident editorial. Warm off-white with charcoal text, a single emerald accent for "verified", amber for "needs evidence". Display headings (e.g., Fraunces), Inter for UI, subtle grain, rounded cards.

CORE CONCEPT, the Truth Ledger: the user builds an Evidence Bank of real items (roles, projects, metrics, skills, certifications, links). Every sentence the AI writes about the candidate must cite one or more evidence IDs. Show citations as small chips. Any sentence the AI marks unsupported is highlighted amber, with "Add evidence" or "Remove".

SCREENS:
1. Onboarding: paste a resume or fill fields. The AI extracts evidence items into editable cards (JSON schema: items[] {id, type, title, detail, metric, dateRange}).
2. Targets: add a job by pasting the posting text or URL text. The AI maps requirements to evidence (match / partial / gap) in a visual matrix, with honest gap-bridging suggestions (courses, portfolio projects), never fake claims.
3. Company Intel: use Google Search grounding for recent company news, team and product facts. Display each fact with source link and date. If grounding returns nothing, say so.
4. Outreach: generate a LinkedIn note (<300 chars), a cold email and a referral ask in 3 tones. Each comes with a character count, citation chips and a copy button.
5. Tailored resume and cover letter: reorder and reword existing evidence only. Show a diff against the base resume. Export to PDF (print stylesheet) and Markdown.
6. Interview Prep: likely questions grounded in the posting, a STAR story builder, and a Mock Interview with timer and optional microphone input via the Web Speech API (text fallback). Scoring JSON: {situation, task, action, result, clarity, score1to5, rewrite}.
7. Pipeline: kanban (Researching, Reached out, Applied, Interviewing, Offer, Closed) with follow-up reminders.

AI: use the newest Gemini Pro model in AI Studio. Use Search grounding only for company facts. Use structured JSON output with schemas for everything parsed. On error, show an inline retry with a preserved draft. Refuse to invent titles, employers, degrees or numbers, and explain why.

PERSISTENCE: IndexedDB with undo for edits and deletions (a toast with Undo). Full JSON export/import.

QUALITY: mobile-first single-column layout with a bottom tab bar, skeleton loaders, empty states with a helpful next step, AA contrast, keyboard shortcuts, and screen-reader labels on all icon buttons.
```

---

## Propis — Russian Cursive Atelier (was: Learn Russian cursive)

**What changes:**
- A real stroke-order engine: every Cyrillic cursive letter, lowercase and uppercase, has stored vector strokes. They animate, and you trace them on a canvas with live feedback.
- Your tracing is scored for shape, direction and order with deterministic geometry, not the AI. The AI coaches on top of the scores and generates practice words.
- Connection drills for the joins that trip learners up (л, м, я connecting from the bottom of the stroke), plus look-alike drills (т/ш, и/п).
- Spaced repetition per letter, a streak calendar, and printable worksheets.

**How to compare:**
1. Ask how to write lowercase cursive "д". Winning means an animated stroke demo, then you trace it and get a score with the specific mistake ("started at top, should start at baseline loop"). A chatbot can only describe it.
2. Ask for a 10-minute practice session on your weakest letters. Winning means the app picks letters from your history and serves traced words that use them.
3. Print a worksheet for "ш, щ, ц". Winning means a clean A4/Letter PDF with guide lines, faded tracing glyphs and stroke arrows.

**Paste into AI Studio Build:**
```
Build "Propis", a Russian cursive handwriting trainer with stroke-order animation and canvas tracing.

VISUAL DIRECTION: Soviet-era school notebook reimagined as premium stationery. Cream paper with faint slanted ruling (the classic Russian "kosaya lineyka" guides), deep blue fountain-pen ink strokes, a red-pencil accent for corrections. A handwritten-style display font for headings and a clean sans for UI. Tactile paper texture and gentle ink-bleed animation.

DATA: hand-author an SVG path dataset for all 33 lowercase and 33 uppercase Russian cursive letters. Each letter has an ordered strokes[] array (SVG path, start point, direction) and entry/exit join points. Store it as a static TS module. Do not rely on the AI for letter shapes.

SCREENS:
1. Alphabet grid: 66 tiles with a mastery ring (0-100%). Filters: lowercase, uppercase, "tricky joins", look-alikes.
2. Letter studio: animated stroke order (play/pause/speed, numbered arrows), then Trace mode (faded guide), then Free-write mode (no guide). Draw with Pointer Events (mouse, touch, Apple Pencil pressure if available) and smooth the ink.
3. Scoring: deterministic, client-side. Resample the user stroke and the reference stroke, compare stroke count, order, direction and shape (e.g., Fréchet or DTW distance), and output 0-100 per stroke with a highlighted region of error.
4. Coach: send scores plus the letter to the newest Gemini Pro model in AI Studio. Get structured JSON {tip, commonMistake, nextDrill} and show it as a friendly note. If the AI fails, show stored default tips.
5. Words and joins: the AI generates practice words and short sentences that use the target letters at the learner's level (JSON {word, translation, stress, focusLetters[]}). Trace whole words with join checks.
6. Review: spaced repetition (SM-2) over letters and joins. Daily queue, streak calendar.
7. Worksheets: choose letters/words and generate printable pages (A4 and Letter) with guide ruling and faded glyphs. Export PDF via a print stylesheet.

PERSISTENCE: IndexedDB for progress, SRS state and saved attempts (thumbnails). Undo the last stroke (Ctrl+Z, plus an on-screen button) and Clear. JSON export/import of progress.

QUALITY: canvas fills the width on mobile with a landscape prompt, buttons have 44px hit targets, and a left-handed mode mirrors the toolbar. Include a reduced-motion setting, screen-reader text naming each letter and its transliteration, loading skeletons, and an empty state on first run with a 60-second guided tour.
```

---

## Repertoire — Chess Opening Memory Gym (was: Learn & memorize chess openings)

**What changes:**
- A real legal-move board (chess.js-style rules) with drag, click-to-move and premoves. It is not a static picture.
- Repertoire trees per color, with spaced repetition per move, not per opening. You drill the exact positions you keep forgetting.
- PGN import/export plus an explorer view of your own tree with mistake heatmaps.
- AI explains the idea behind a move in plain language, grounded in the move list. It never acts as the source of truth for which move is legal.

**How to compare:**
1. Import a PGN of the Italian Game with sidelines and start drilling. Winning means the board quizzes you move by move, schedules the misses for sooner review, and shows a due count tomorrow.
2. Ask "why 5.d3 here instead of d4?". Winning means an explanation tied to the actual position, with arrows drawn on the board.
3. Play a wrong move in a drill. Winning means instant feedback, the correct move animated, and the position flagged in a "leaks" list.

**Paste into AI Studio Build:**
```
Build "Repertoire", a chess opening trainer that makes openings stick with move-level spaced repetition.

VISUAL DIRECTION: walnut-and-felt club room. A deep green felt background, a board with warm wood squares (with alternate themes: marble, tournament green, high-contrast), elegant Staunton-style SVG pieces, gold accents, serif headings. Smooth piece animations (150ms) and a subtle move sound with a mute toggle.

ENGINE: implement full legal-move chess logic client-side (castling, en passant, promotion, check/mate/stalemate, FEN/PGN parsing). The board supports drag-and-drop, tap-tap moves, arrows (right-drag) and square highlights, and flips orientation.

SCREENS:
1. Library: repertoires by color. Starter sets: Italian, Queen's Gambit, Caro-Kann, Sicilian Najdorf basics, London. Empty state invites "Import PGN" or "Build by playing moves".
2. Builder: play moves on the board to grow a tree. Shows a variation tree with annotations, comments and NAGs. Undo/redo per move.
3. Drill: the app plays the opponent's moves and the user must find their repertoire move. SM-2 scheduling per position (FEN key). Modes: Due Today, Learn New, Weak Spots, Blitz (timed). On a miss, animate the correct move, show its comment, and re-queue it.
4. Explain: on any position, "Why this move?" sends FEN + move list + the repertoire move to the newest Gemini Pro model in AI Studio. Structured JSON {idea, plans[], typicalMistakes[], arrows[{from,to}]}. Draw the arrows on the board. Validate that every arrow square is a legal square name, and drop bad ones. Label the explanation "AI explanation; verify with an engine". On error, show a retry and keep the board usable.
5. Stats: retention curve, due forecast, a heatmap of the most-missed positions, and streak.

PERSISTENCE: IndexedDB for repertoires, SRS state and history. Export PGN (with comments) and a JSON backup. Import PGN, with clear error messages for malformed PGN showing the line number.

QUALITY: keyboard play (type moves in SAN, arrow keys step through history), screen-reader announcements of each move in words ("Knight to f3"), colorblind-safe highlight colors. Mobile: the board is full width with controls in a bottom sheet. Include loading and empty states, and a reduced-motion option.
```

---

## Gradebook Garden — Beautiful Classroom Checklist (was: Aesthetically pleasing classroom grades checklist)

**What changes:**
- A real teacher workflow: classes → roster → assignments grid with fast keyboard entry, status chips (Done, Late, Missing, Excused) and points/percent.
- Distinctive pastel-botanical design: a plant visibly grows as the class completes work. It is still dense and fast, not cute-but-slow.
- Category weighting, auto-calculated averages and a "who's missing what" view for parent emails.
- AI drafts parent/student notes and summarizes class trends from the grid only, with a review step before anything is copied.

**How to compare:**
1. Paste a roster of 28 names and create 6 assignments. Winning means you can mark the whole grid by keyboard in under 2 minutes, with averages updating live.
2. Ask "who is missing 2+ assignments, and draft a kind note to each family". Winning means accurate names drawn from your data and editable drafts. A chatbot needs you to re-paste everything.
3. Export to CSV and print a one-page class summary. Winning means a clean, attractive printout and a CSV that opens correctly in Sheets.

**Paste into AI Studio Build:**
```
Build "Gradebook Garden", a beautiful, fast classroom grades and assignment checklist for K-12 teachers.

VISUAL DIRECTION: modern botanical stationery. Soft sage, blush, butter yellow and cream, with a deep forest-green text color for contrast. Rounded cards, hand-drawn leaf illustrations, a playful rounded display font (e.g., Nunito/Recoleta) for headings and tabular numbers for grades. Each class has a "garden" illustration that grows (sprout → bloom) as its completion rate rises. It must still pass WCAG AA contrast.

SCREENS:
1. Classes home: class cards (name, period, color, garden stage, % complete, missing count). Empty state: "Plant your first class" with a quick-add form.
2. Roster: paste names (one per line or CSV) and the app parses them. Add student notes and accommodations flags. Bulk edit.
3. Grid: students × assignments. Each cell is a status chip (Done ✓, Late, Missing, Excused, Not yet) plus optional points. Keyboard entry: arrows to move, 1-5 for statuses, digits for points, Enter to go down. Sticky header and first column. Row/column averages. Category weights (Homework 20%, Tests 50%, etc.). Conditional colors that also carry text labels, not color alone.
4. Assignment detail: due date, category, max points, rubric checklist.
5. Insights: missing-work list, a grade distribution chart, and students trending down.
6. Notes: select students, and the newest Gemini Pro model in AI Studio drafts warm, specific parent/student messages using only that student's grid data. Structured JSON {studentId, subject, body, tone}. Show editable drafts with Copy and "Mark sent". No AI call happens without the teacher clicking Generate. On error, keep the selection and show a retry.

PERSISTENCE: IndexedDB with autosave and a "Saved" indicator. Full undo/redo history for grid edits (Ctrl+Z / Ctrl+Y) and a 10-second Undo toast for deletions. Export CSV per class, a JSON backup and import. A print view gives a one-page class summary and per-student progress slips.

PRIVACY: a note on the settings page saying data stays in this browser. An option to show initials only (privacy mode) when projecting.

QUALITY: mobile uses a per-student card view with swipe to set status. Tablet uses the grid. Include loading skeletons, an empty state per screen, and screen-reader labels like "Maria, Essay 2, Late, 8 of 10".
```

---

## Admit Atlas — Graduate Application Command Center (was: Graduate school application tracker)

**What changes:**
- Programs, deadlines, requirements, recommenders, essays and fees are tracked as linked records, with a timeline and a countdown view.
- Search-grounded program lookup pre-fills deadlines and requirements with sources and a "verify on official site" flag. Nothing is invented.
- An essay workspace with versioning, word-limit meters and AI feedback against each program's prompt.
- A recommender tracker with polite reminder drafts, plus a budget tracker for application fees and test costs.

**How to compare:**
1. Add 5 programs by name. Winning means deadlines and requirements are pre-filled with source links and dates checked, and each field is marked verified or unverified.
2. Ask "what's due in the next 14 days, and what am I blocked on?". Winning means one precise list from your own data, including recommenders who haven't submitted.
3. Paste a statement of purpose and target a program's prompt. Winning means line-level feedback, a word count against the limit, and a saved version you can diff.

**Paste into AI Studio Build:**
```
Build "Admit Atlas", a command center for graduate school applications (MS, PhD, MBA, law, med).

VISUAL DIRECTION: modern academic atlas. Deep midnight-blue sidebar, parchment content area, copper accents, and fine topographic-line patterns. Serif headings (e.g., Newsreader) and geometric sans for data. Each program gets a university-style color chip. Calm, precise, premium.

SCREENS:
1. Dashboard: next-deadline countdown, a progress ring per program, a "Blocked" list (missing recs, unsent scores), and a 30-day timeline. Empty state: "Add your first program" with search.
2. Add Program: type a program and university. Use the newest Gemini Pro model in AI Studio with Google Search grounding to find the deadline(s), required materials, fee, GRE/GMAT policy, essay prompts and word limits. Return structured JSON with a sourceUrl and retrievedDate per field. Show every field as editable, with source links and a "Verify on official site" badge. If a value isn't found, leave it blank and say "Not found". Never guess.
3. Program detail: a requirements checklist, essays, recommenders, portal login reminder (just a URL and a note, never store passwords), fee, status (Researching → In progress → Submitted → Interview → Decision) and decision outcome.
4. Essays: a rich-text editor with a word/character limit meter, version history with a diff view, and reuse of a base essay across programs. "Get feedback" sends the essay plus that program's prompt to the newest Gemini Pro model and returns JSON {overall, strengths[], issues[{quote, suggestion}], promptFit1to5}. Quotes are highlighted in the editor.
5. Recommenders: who, which programs, request date, status, and a polite reminder email draft (copy only).
6. Calendar: a month view of all deadlines. Export .ics.
7. Budget: fees, tests, score reports, totals, and fee waivers.

PERSISTENCE: IndexedDB, autosave, undo toasts for deletions, and full undo in essays. Export JSON backup, CSV of programs, and a printable summary PDF via a print stylesheet. Import backup.

ERRORS: if grounding fails or times out, show "Couldn't look this up. Enter manually or retry" and keep partial data. Loading states name the step.

QUALITY: mobile bottom navigation, cards instead of tables on small screens, AA contrast, keyboard shortcuts (N = new program, / = search), and ARIA labels.
```

---

## Room Radar — Month-to-Month Rentals, Cheapest First (was: Month-to-month rent finder near [your neighborhood])

**What changes:**
- Every listing comes from Google Search grounding, with its source link, the date found, and the posted date when available. Without a source there is no card, and the app says so openly.
- Results are sorted cheapest first, filtered for one person and month-to-month or flexible terms, and plotted by distance from [your neighborhood].
- Shortlist, notes, "contacted" status and a scam-check checklist, all saved locally.
- A re-search that marks new and possibly-stale listings, compared against what you already saved.

**How to compare:**
1. Run the default search. Winning means a sorted list where each item has a price, type (room/studio/ADU), term, a clickable source and dates, with an explicit "Found N results; M lacked price and are listed separately".
2. Ask ChatGPT/Claude the same. Winning means fewer hallucinated or undated listings. Click 5 links in each and count how many are real and current.
3. Shortlist 3, add notes, reload the next day and re-search. Winning means your notes persist and new or changed listings are badged.

**Paste into AI Studio Build:**
```
Build "Room Radar", a finder for month-to-month rentals for ONE person near [your neighborhood], sorted cheapest first.

NON-NEGOTIABLE: never invent listings, prices, addresses or links. Every listing must come from Google Search grounding results with a real source URL. If nothing is found, show an honest empty state. Display each listing's source link, "found on" date (today) and posted date if the source shows one, otherwise "posted date unknown".

VISUAL DIRECTION: sunny California modern. Warm sand background, terracotta and sage accents, rounded cards, a bold condensed display font for prices (e.g., Barlow Condensed) and Inter for body. A clean map-like distance strip instead of a heavy map. Friendly, trustworthy, fast.

SEARCH: use the newest Gemini Pro model in AI Studio with Google Search grounding. Run several queries (e.g., "month to month room for rent near [your neighborhood]", "furnished room monthly West [your city]", studio, sublet, near Valley Fair / Santana Row / Winchester), then de-duplicate by URL. Ask for structured JSON: listings[] {title, priceMonthly (number or null), type (room/studio/ADU/apartment/sublet), term (month-to-month/flexible/unknown), neighborhood, approxAddressOrCrossStreets, sourceUrl, sourceName, postedDate|null, notes}. Cross-check every sourceUrl against the grounding metadata URLs and drop any listing not backed by a grounding source. Show "N dropped as unverifiable".

SCREENS:
1. Search home: preset filters (max budget slider, room/studio, furnished, utilities included, pets, parking, radius 1/3/5 mi) and a big "Find listings" button. Loading shows the query steps.
2. Results: cheapest first. Listings with an unknown price are in a separate section at the bottom. Each card has the price, type, term badge, distance estimate, source chip and dates. Sort options: price, newest, distance.
3. Listing detail: summary, the source link (opens a new tab), my notes, status (New, Contacted, Touring, Applied, Passed), and a scam checklist (never wire deposits, see the place first, verify the owner).
4. Shortlist: compare up to 4 side by side.
5. Re-search: marks listings "New since last search" and flags saved ones not found again as "May be gone".

PERSISTENCE: localStorage/IndexedDB for searches, shortlist, notes and status. Undo for removal. Export the shortlist as CSV and Markdown.

ERRORS: if grounding fails, rate-limits or returns zero, explain that and offer a retry plus direct links to search manually on major rental sites. Never fill gaps with made-up data.

QUALITY: mobile-first, one-thumb layout, AA contrast, every link labeled with its source, keyboard navigable.
```

---

## Keepsake Vault — Labeled Memory Organizer with Encrypted Passwords (was: Organizer for photos, notes and important info with labels — and passwords)

**What changes:**
- One labeled library for photos, notes and important info (IDs, warranties, contacts), with fast search, smart collections and a timeline.
- A separate Password Vault encrypted client-side with Web Crypto: PBKDF2/Argon2-style key derivation from a master passphrase and AES-GCM. It auto-locks, and vault contents are never sent to the AI.
- AI auto-labels photos and summarizes notes only for non-vault items, and only when you opt in per item.
- An encrypted backup export, with honest messaging that a forgotten passphrase cannot be recovered.

**How to compare:**
1. Add 20 photos and 10 notes, then ask "show receipts from last spring". Winning means AI-suggested labels and a correct filtered result in a polished gallery.
2. Create a vault entry, reload, and inspect localStorage/IndexedDB in DevTools. Winning means you only see ciphertext, and the network tab shows no vault data leaving the browser.
3. Export a backup and re-import it in a fresh browser. Winning means everything restores, and the vault still requires the passphrase.

**Paste into AI Studio Build:**
```
Build "Keepsake Vault", a personal organizer for photos, notes and important info with labels, plus a separately encrypted password vault.

VISUAL DIRECTION: museum archive meets modern app. Deep charcoal and warm linen, an antique-gold accent, archival label tags styled like museum placards, and a masonry photo gallery with soft depth. Serif display (e.g., Cormorant) with a clean sans. The vault area shifts to a darker, steel-blue "safe room" theme with a lock animation.

LIBRARY (not encrypted by default, stored in IndexedDB):
1. Home: a search bar, smart collections (Recent, Documents, Receipts, People, Places, Unlabeled) and a label cloud. Empty state with drag-and-drop.
2. Items: Photo (with caption and EXIF date), Note (Markdown), Info Card (templates: ID document details, warranty, medical info, emergency contacts, Wi-Fi), all with labels, color and pinned state.
3. Labels: create, rename, merge and nest. Bulk-label with multi-select.
4. AI assist (opt-in per action): "Suggest labels" sends a downscaled photo or a note to the newest Gemini Pro model in AI Studio and returns JSON {labels[], title, summary}. Show the suggestions as chips to accept. Never auto-send anything.

PASSWORD VAULT (strict rules):
- Encrypt client-side with the Web Crypto API: derive a key from the master passphrase with PBKDF2-SHA256 (≥600,000 iterations, random 16-byte salt) and encrypt each entry with AES-GCM (random 12-byte IV). Store only ciphertext, salt and IV.
- The passphrase and key live only in memory. Auto-lock after 5 minutes idle and on tab hide (configurable). Lock button always visible.
- Vault data is NEVER sent to the AI or any network endpoint. Hide AI buttons inside the vault.
- Entries: site, username, password (hidden, reveal-on-hold, copy that clears the clipboard after 30s), notes, and a password generator with a strength meter.
- Clear warning at setup: a forgotten passphrase cannot be recovered.

EXPORT: an encrypted backup (.json, vault ciphertext included as-is) and an import with a validation report. Library export to a ZIP of files plus metadata JSON.

UNDO: deletions go to Trash for 30 days with Restore. Undo toast on edits.

QUALITY: mobile bottom tabs and a full-screen photo viewer with swipe, AA contrast, keyboard shortcuts, ARIA labels, loading skeletons for thumbnails, and clear error messages for storage quota or a wrong passphrase.
```

---

## Blue Team: Night Shift — Incident Response Simulator (was: Cybersecurity breach simulation game)

**What changes:**
- An exciting narrative game at a fictional company (Halcyon Freight): you are the on-call analyst over one tense night.
- Three gameplay loops: phishing inbox triage, a SIEM alert queue with true/false-positive decisions, and incident containment on a network map. A clock and a business-impact meter run throughout.
- AI generates fresh, realistic but fictional emails, logs and attacker moves within a strict JSON schema. It is defensive-only, with no real exploit code, and all domains are fictional (.example).
- An end-of-shift debrief maps your decisions to real-world frameworks (MITRE ATT&CK technique names, NIST IR phases) with a score and replays.

**How to compare:**
1. Play a 10-minute shift. Winning means it feels like a game (timer, tension, consequences) while you learn red flags. A chatbot gives you a quiz.
2. Mis-triage a phishing email on purpose. Winning means the consequence shows up later in the story (a compromised account appears in alerts) and the debrief explains the missed cues.
3. Replay on "Hard". Winning means new scenario content each run, with no repeats.

**Paste into AI Studio Build:**
```
Build "Blue Team: Night Shift", an exciting, educational defensive cybersecurity game. The player is the on-call security analyst at a fictional company, "Halcyon Freight", during one night. Defensive skills only: no real exploit code, no real malware, no real company names. All domains and IPs use reserved example ranges (example.com, 203.0.113.0/24, 10.x).

VISUAL DIRECTION: cinematic SOC at 3 a.m. Near-black navy, neon cyan and amber UI, red alarms, monospace data (JetBrains Mono) with a condensed display font. Subtle scanlines, a pulsing threat meter, satisfying sounds (mutable). It should feel like a thriller, not a worksheet.

GAME STRUCTURE: a shift with a 20-minute in-game clock (real time about 10 min). A Business Impact meter and an Analyst Reputation score. Difficulty: Trainee, Analyst, Lead.

SCREENS:
1. Title and briefing: story intro, choose difficulty, and a tutorial overlay.
2. Inbox: suspicious emails with full headers. The player flags red cues (lookalike domain, urgency, mismatched link on hover) and decides Report / Safe / Escalate.
3. Alert Queue: SIEM-style alerts with log snippets. Triage each as True Positive, False Positive or Needs Investigation, then pivot to related logs.
4. Network Map: an SVG of company hosts. Contain incidents by isolating hosts, disabling accounts, blocking domains or resetting credentials. Each action has business tradeoffs (isolating the dispatch server stops shipping).
5. Comms: write a short status update to the fictional CISO. The AI grades it for clarity.
6. Debrief: timeline replay, every decision with a correct/incorrect explanation, mapped MITRE ATT&CK technique names and NIST incident response phases, a score, and badges.

AI: use the newest Gemini Pro model in AI Studio to generate scenario content each run, using structured JSON with a schema: emails[] {from, subject, body, headers, isPhish, cues[]}, alerts[] {id, source, severity, log, truth, explanation}, attackerSteps[] {time, technique, effect}. Validate it. If invalid, retry once, then fall back to 3 built-in handcrafted scenarios so the game always works. Keep generated content free of real organizations and of working malicious code. Show a "Generating your shift…" loader with flavor text.

PERSISTENCE: localStorage for progress, badges, best scores and settings. Save/resume a shift. Undo the last containment action once per shift (a "rollback" mechanic). Export the debrief as Markdown/PDF.

QUALITY: mobile layout uses tabs (Inbox / Alerts / Map) with a sticky clock. Keyboard shortcuts, screen-reader text for map nodes, a no-flashing mode and a reduced-motion mode, colorblind-safe severity icons with labels.
```

---

## Mirror Me — Consent-First Personal AI Twin (was: "Build a clone of myself from photos and videos")

**What changes:**
- A persona studio that learns your voice from your own writing and notes. You review an explicit "Persona Card" (tone, values, phrases, topics, boundaries) instead of a hidden prompt.
- An avatar generated only from your own uploaded photos, with an image model producing stylized portraits. A permanent "AI" badge shows on every avatar and message.
- Consent gates: you confirm ownership of every upload, and there is no option to clone other people. A one-click "Delete everything" is included.
- Twin chat with "how confident am I this sounds like me" ratings and feedback that refines the persona over time.

**How to compare:**
1. Upload 10 of your own writing samples and ask the twin "what should I do this weekend?". Winning means it sounds recognizably like you, and its Persona Card shows why.
2. Ask a chatbot to "be me" from the same samples. Winning means the app keeps the persona, memories and corrections across sessions, while the chatbot forgets.
3. Try to upload a celebrity photo, or ask it to impersonate someone else. Winning means a clear refusal and the consent rules shown.

**Paste into AI Studio Build:**
```
Build "Mirror Me", a consent-first personal AI twin. The owner creates a chat persona from their OWN writing and notes, and an avatar from their OWN photos. Every twin output is visibly labeled "AI".

ETHICS RULES (enforce in UI and logic):
- Onboarding requires checking "These are my own photos and writing, and I consent to creating an AI version of myself."
- Every upload asks for ownership confirmation. Refuse requests to imitate any other real person.
- A permanent "AI twin" badge appears on avatar images (burned into exports as a corner watermark) and on every chat message.
- Settings has "Delete everything" (wipes IndexedDB) with a typed confirmation.

VISUAL DIRECTION: soft futurist mirror. Pearl-white and lavender gradients, iridescent holographic accents, high-contrast glass panels, an elegant sans (e.g., Satoshi), and a slow shimmer on the avatar.

SCREENS:
1. Welcome and consent.
2. Voice Studio: paste or upload text (journals, emails, posts, notes; .txt/.md). The newest Gemini Pro model in AI Studio analyzes them and returns a Persona Card as JSON {tone[], signaturePhrases[], values[], interests[], writingStyle {sentenceLength, emoji, humor}, boundaries[], sampleReplies[]}. The owner edits every field. Version the card.
3. Avatar Studio: upload 3-10 of your own photos. Use the AI Studio image model to generate stylized portrait avatars (illustrated, watercolor, 3D clay) that resemble the owner. Each carries the "AI" watermark. The owner picks a default. Note that photos stay local except when sent for generation.
4. Twin Chat: chat with your twin. Responses use the Persona Card plus relevant memory snippets from your notes (simple local keyword/embedding retrieval) and cite which notes informed them. Per-message rating "Sounds like me? 👍/👎 + fix". Corrections are saved as persona rules.
5. Memory: browse, edit and delete the notes and facts the twin knows.
6. Share card: export a labeled persona summary image or PDF with "AI twin of [name]".

AI DETAILS: structured JSON with schemas for the persona and ratings. Streaming chat with a typing indicator. On error, show an inline retry with the message preserved. If image generation fails or is blocked, explain why and offer a different style.

PERSISTENCE: IndexedDB for samples, photos (compressed), persona versions, chat history and memory. Undo for edits and deletions. Export a full encrypted-optional JSON backup and import it.

QUALITY: mobile chat-first layout, AA contrast on all glass panels, alt text for avatars, keyboard navigation, reduced-motion support, and empty states on every screen.
```

---

## Lanternfen — Original Retro Creature-Collecting RPG (was: Pokémon Soul Silver website & mobile version)

**What changes:**
- An entirely original game: its own world (the river-delta region of Lanternfen), its own 24-creature roster with original names, types, art and music. It uses no names, creatures, maps, art or audio from any existing franchise.
- A playable top-down 2D tile engine on canvas with turn-based battles, a type chart, catching, a party/storage box and a journal. Keyboard on desktop, a touch D-pad on mobile.
- Procedural pixel art (drawn in code) and chiptune made with WebAudio, so there is no copyrighted asset risk.
- AI adds flavor through NPC dialogue and journal entries via schema-checked JSON. Core gameplay is deterministic and works offline.

**How to compare:**
1. Play 15 minutes on your phone: pick a starter, explore, battle, and catch two creatures. Winning means smooth controls, saving, and a game that feels finished.
2. Ask ChatGPT/Claude for "a creature-collecting RPG in one file". Winning means Lanternfen has multiple maps, a balanced type chart, catching, saving and audio, while theirs is a demo.
3. Close the tab mid-route and reopen. Winning means you resume exactly where you were, with the party intact.

**Paste into AI Studio Build:**
```
Build "Lanternfen", an ORIGINAL retro 2D creature-collecting RPG playable in desktop and mobile browsers. Do NOT use any names, creatures, characters, moves, items, maps, art, music or UI from Pokémon or any other existing franchise. Everything below is original.

WORLD: Lanternfen is a misty river-delta region of stilt villages, glowing reed marshes, tide caves and a lighthouse city. The player is a new "Wickkeeper" who befriends "Glimmerlings", creatures drawn to lantern light. Create 24 original Glimmerlings across 8 original types (Ember, Tide, Moss, Gale, Stone, Spark, Dusk, Bloom) with an original type-effectiveness chart, 2-stage evolutions, stats and 4 moves each. Write the data as a static TS module.

VISUAL DIRECTION: GBA-era pixel art with a modern touch. A 16×16 tileset and creature sprites drawn procedurally in code (pixel arrays rendered to canvas), with a limited warm-dusk palette, soft bloom on lanterns, day/night tint, and crisp integer scaling. Chiptune music and SFX synthesized with the WebAudio API (original melodies), with a volume and mute control.

GAMEPLAY:
1. Title: New Game / Continue / Settings.
2. Overworld: tile-based movement, collision, NPCs, signs, tall-reed encounter zones, 4 maps (Ferrow Village, Reedlight Marsh, Tidehollow Cave, Beacon City), and doors/transitions with fades.
3. Battle: turn-based with HP/XP bars, type effectiveness messages, status effects, a catch mechanic using "Wick Jars", run, switch, items. Trainer battles plus one gym-style "Beacon Trial".
4. Menus: party (6), storage box, bag, Glimmerdex journal with seen/caught, save.
5. Optional AI flavor: the newest Gemini Pro model in AI Studio writes NPC small-talk and journal entries as JSON {speaker, lines[]} within the Lanternfen lore. Validate them. Fall back to built-in dialogue if offline or on error. AI never changes stats or rules.

CONTROLS: keyboard (arrows/WASD, Z/Enter = A, X/Esc = B), gamepad API, and on mobile a translucent on-screen D-pad plus A/B buttons with haptics where supported. Landscape and portrait layouts.

PERSISTENCE: autosave to localStorage on map change plus a manual save with 3 slots. Export/import a save file (JSON).

QUALITY: 60fps game loop with requestAnimationFrame, pause on tab hide, adjustable text speed, a colorblind-friendly type icon set with labels, a reduced-flash option, a loading screen, and graceful errors if audio is blocked ("Tap to enable sound").
```

---

## Untitled projects ("Build this", "Do this", "Code Assistant history" ×2, "Retain features from previous edits")

These five projects have no descriptive title, so their content is unknown. For each one:

1. Open it in AI Studio Build and click through the preview for two minutes. Write down in one line what it does and what's broken or ugly.
2. Rename the project to something descriptive so you can find it later.
3. If it's a duplicate of an app above (for example, an earlier version of the rent finder), archive it and use that app's prompt instead.
4. Otherwise, paste the generic prompt below into that project's Build chat. Fill in the bracketed line at the top with your one-line description. Run it, check the preview, then ask for any specific fixes in a follow-up message.

**Paste into AI Studio Build (any existing project):**
```
This app currently does: [one line describing what the app is for]. Upgrade it to a polished, production-quality app WITHOUT removing or breaking any existing feature, screen, or saved data.

STEP 1, AUDIT FIRST: before changing code, list every existing feature, screen, data field and AI call you find, plus every bug, console error, broken flow and missing state. Keep this list in a FEATURES.md file in the project and confirm that each item still works after your changes.

STEP 2, FIX: fix every bug and console error. Remove any hard-coded API keys and use AI Studio's built-in Gemini connection. Where AI output is parsed, switch to structured JSON output with a response schema, validate it, retry once on failure, then show a friendly error card with a Retry button. Use the newest Gemini Pro model in AI Studio (an image model for images, Google Search grounding for any current facts, with source links shown). Never invent facts or data.

STEP 3, STATES: every screen gets a designed empty state (with a clear next action), a loading state (skeletons or named progress steps), an error state (a plain-language message plus retry) and a success feedback toast.

STEP 4, PERSISTENCE AND UNDO: save user data locally (localStorage for settings, IndexedDB for larger data), autosave with a "Saved" indicator, an Undo toast for deletions and major edits, and export/import of a JSON backup. Add CSV/Markdown/PDF export where it makes sense.

STEP 5, DESIGN: give the app a distinctive, cohesive, high-end visual identity that fits its purpose. Choose one: a custom color palette defined as CSS variables (light and dark mode), a paired display and body font, consistent 8px spacing, a refined component style and tasteful micro-animations. Avoid the generic default look. Make every screen fully responsive: mobile-first, no horizontal scroll, 44px touch targets, bottom navigation on phones.

STEP 6, ACCESSIBILITY: WCAG AA contrast, semantic HTML, labels on all inputs and icon buttons, full keyboard navigation with visible focus rings, reduced-motion support, and never color alone to convey meaning.

STEP 7, VERIFY: re-check every item in FEATURES.md, then summarize what you changed, what you fixed, and anything you could not complete.
```
