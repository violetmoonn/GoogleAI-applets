# Healthcare

Every app in this group is for training and demos only. Each prompt below requires synthetic data, a persistent "Not for clinical use — training only" banner, blocking of obvious real identifiers, and no diagnosis or treatment advice. Paste each prompt into a fresh AI Studio Build session.

---

## FrontDesk Studio — Allergy & Asthma Practice Simulator (was: Doctor's office new system idea; [practice name] website info)

**What changes:**
- Merges the scheduling idea and the website info into one front-desk command center: a day board, check-in, a patient-facing kiosk view and an editable practice profile.
- Adds allergy-specific visit types (new consult, skin testing, allergy-shot build-up and maintenance, spirometry, biologic injection) with realistic slot lengths and prep rules, such as holding antihistamines before skin testing as a configurable note.
- Gemini creates synthetic patient days and answers "how do I…" questions using only the practice profile you entered, and it cites which field each answer came from.
- Adds PHI guardrails, tablet-first layout, CSV/JSON export, and local persistence that survives a refresh.

**How to compare:**
1. "Generate a busy Monday with 3 shot patients, 2 skin tests and a no-show." Winning: a schedule you can tap and edit, with conflicts flagged and the 30-minute post-shot wait tracked, where ChatGPT or Claude gives a static table.
2. Type a fake SSN like 123-45-6789 into a name field. Winning: the input is blocked with an inline explanation, and nothing is saved.
3. Ask the kiosk "What should I bring to my first visit?" Winning: an answer drawn only from your practice profile with the source shown, and "I don't know — ask the front desk" when the profile is blank, not invented office details.

**Paste into AI Studio Build:**
```
Build "FrontDesk Studio," a tablet-first React + Tailwind training simulator for the front desk of an allergy & asthma practice. Training/demo only: show a fixed top banner "Not for clinical use — training only" on every screen. Use synthetic patients only.

Visual direction: calm clinical-premium. Warm white (#FAFAF7) background, deep teal primary, soft sage accents, one serif display face for headings with Inter for UI, generous 16px+ body text, 48px minimum tap targets, WCAG AA contrast, visible focus rings, reduced-motion support.

Screens:
1. Today Board: a timeline of rooms and providers in columns. Visit types: New Consult (60m), Skin Testing (90m), Allergy Shot Build-up / Maintenance (15m + 30m observation timer), Spirometry (30m), Biologic Injection (30m + observation). Drag to reschedule. Conflicts and overbooked observation chairs are flagged in amber.
2. Check-in drawer: confirm demographics, insurance card placeholder, intake checklist, and prep reminders (an editable rule like "hold antihistamines before skin testing per practice policy").
3. Kiosk Mode: a large-type, patient-facing view with check-in and an FAQ assistant.
4. Practice Profile: editable locations, hours, phone, parking, new-patient instructions and policies. Ship it with clearly marked placeholders. Never invent real practice details.
5. Settings: export day as CSV/JSON, import JSON, reset demo.

AI: use the newest Gemini Pro model available in AI Studio through the built-in SDK. Never hard-code an API key. Two features:
(a) "Generate synthetic day": returns JSON matching a declared schema {appointments:[{id, patientAlias, age, visitType, start, durationMin, provider, room, notes}]}. Validate it before rendering, and on a parse failure retry once, then show a friendly error with a Retry button.
(b) Kiosk FAQ: answers ONLY from the Practice Profile JSON passed as context. Return {answer, sourceField|null}. If sourceField is null, say "Please ask the front desk." Never give medical advice. Refuse symptom or dosing questions politely.

Guardrails: reject inputs that match a full SSN pattern, a 16-digit card number or an MRN-like long numeric ID, with an inline message. Names must use the "Demo-" prefix or be generated.

States: empty board with a "Generate a sample day" CTA, skeleton loaders during AI calls, toast errors, offline notice.
Persist everything in localStorage. Responsive: two-pane on a landscape tablet, stacked on a phone.
```

---

## IntakeCoach — Voice Role-Play for New-Patient Check-in (was: New-patient station / practice voice acting)

**What changes:**
- Changes a static script into live voice role-play: the AI plays a synthetic new patient (rushed parent, hard-of-hearing senior, Spanish-preferring caller, frustrated insurance case) while you practice collecting intake information.
- A live checklist ticks off each required field as you capture it, with a timer for efficiency.
- After each call, a scorecard covers completeness, time, empathy phrases, and whether you read back the information to confirm it.
- A script library with branching "if the patient says X" cards that you can edit and export.

**How to compare:**
1. Start a "rushed parent, child with new asthma referral" call and talk through it. Winning: a natural spoken back-and-forth with interruptions, where ChatGPT or Claude gives a typed dialogue.
2. Skip asking about the insurance subscriber. Winning: the scorecard names the missed field and suggests one exact phrasing to use next time.
3. Run the same scenario three times. Winning: a progress chart that shows time-to-complete and completeness trending, saved locally.

**Paste into AI Studio Build:**
```
Build "IntakeCoach," a voice role-play trainer for front-desk staff practicing new-patient intake at an allergy & asthma clinic. Show a persistent banner: "Not for clinical use — training only. All patients are fictional."

Visual direction: quiet and focused. Charcoal-on-ivory, a single coral accent for "live" states, rounded 20px cards, a large circular mic button (min 72px), Inter for UI. WCAG AA, full keyboard support, captions always on.

Screens:
1. Scenario Picker: cards for persona (rushed parent, hard-of-hearing senior, Spanish-preferring caller, anxious first-timer, insurance mix-up), difficulty and target time. Includes a "Custom persona" form.
2. Live Call: a big mic button, a live transcript with speaker labels, and a right-side Intake Checklist (legal name, DOB, callback number, referral source, reason for visit, insurance carrier/member ID/subscriber, preferred pharmacy, allergies-to-medication question, preferred language, emergency contact) that auto-checks as each item is captured. Also an elapsed timer, a "Hint" button and an End Call button.
3. Debrief: a score out of 100 with sub-scores (completeness, efficiency, empathy, read-back confirmation), missed items, 3 suggested phrasings and the replayable transcript.
4. Script Library: branching cards ("If the caller says they don't have their card…"), editable, export as Markdown/JSON.
5. Progress: a chart of past sessions from localStorage.

AI: use the newest Gemini Live / native-audio model available in AI Studio for real-time two-way voice role-play. If it is unavailable or mic permission is denied, fall back to text chat with the newest Gemini Pro model and tell the user why. Never hard-code an API key. The patient persona invents synthetic details only and never gives or asks for medical advice.
For the debrief and checklist, call the newest Gemini Pro model with structured JSON output: {capturedFields:[{field, value, turnIndex}], missedFields:[], scores:{completeness, efficiency, empathy, readBack}, suggestions:[string]}. Validate it, and on failure show "Couldn't score this call — retry" without losing the transcript.

Guardrails: if the trainee speaks or types something resembling a real full SSN or card number, mask it in the transcript and show a warning.
States: mic permission prompt explainer, connecting spinner, reconnect on drop, empty library state.
Tablet-first landscape layout. On a phone the checklist becomes a bottom sheet. Persist sessions and scripts locally, and export the debrief as PDF via print.
```

---

## VitalSign Lab — Vitals & Auscultation Trainer (was: Vitals & stethoscope simulation)

**What changes:**
- An interactive torso diagram with tappable auscultation points. Each point plays synthesized heart or lung sound patterns (normal, wheeze, crackles, murmur-like) generated with Web Audio, labeled as approximations.
- A vitals monitor that animates HR, BP, RR, SpO2 and temperature for synthetic cases. The learner records readings and gets graded against the case.
- Peak-flow and spirometry-style practice cards relevant to asthma training.
- AI case generation with quiz-style "what would you note and escalate?" feedback, without treatment instructions.

**How to compare:**
1. "Give me an asthma-flare training case." Winning: a playable case with an animated monitor, tappable lung sounds and a scored entry form, where ChatGPT or Claude gives a paragraph.
2. Enter a wrong respiratory rate. Winning: specific feedback with the correct range and the counting technique tip.
3. Turn on Quiz mode and identify 5 sounds. Winning: a randomized audio quiz with a streak counter and the score stored locally.

**Paste into AI Studio Build:**
```
Build "VitalSign Lab," a training simulator for measuring vitals and practicing auscultation, aimed at medical assistants and students at an allergy & asthma clinic. Always show the banner "Not for clinical use — training only. Sounds are synthesized approximations." Use synthetic cases only.

Visual direction: dark clinical-monitor aesthetic softened for long use. Deep navy (#0E1A2B) canvas, monitor-green and amber waveform accents, white cards for forms, tabular numerals, 48px+ tap targets, WCAG AA (never color alone, so pair color with icons and text).

Screens:
1. Case Library: synthetic cases (well check, mild asthma flare, post-shot observation, anxious child, elderly with COPD history). Includes a "Generate new case" button.
2. Monitor: animated SVG/canvas ECG-style trace, pleth wave, and numeric HR, BP, RR, SpO2 and temperature that drift realistically. Pause/resume controls.
3. Auscultation: a front/back torso SVG with labeled tappable points (aortic, pulmonic, tricuspid, mitral, and lung fields L/R upper/lower). Tapping plays a Web Audio–synthesized pattern (normal S1/S2, wheeze, crackles, diminished sounds, murmur-like) with a volume control and a visual waveform. Include captions describing each sound for deaf or hard-of-hearing users.
4. Record & Grade: a form where the learner enters vitals and selects sound findings, then sees a graded comparison with tips (e.g., count RR for 30s x2).
5. Quiz Mode: random sound identification with a streak counter and spaced review of missed items.
6. Progress: a history chart, plus CSV export.

AI: use the newest Gemini Pro model available in AI Studio. Never hard-code an API key. "Generate case" returns JSON matching the schema {title, age, sex, context, vitals:{hr, sbp, dbp, rr, spo2, tempC}, drift:{...}, soundsByPoint:{pointId: soundType}, learningObjectives:[], debriefQuestions:[]}. Only allow soundType values from the app's sound enum. Validate the response; on failure, fall back to a built-in case and show a toast.
The AI explains and quizzes only. It frames findings as "what you would document and report to the supervising clinician" and never gives treatment advice.

Guardrails: the case notes field blocks SSN-like and card-number patterns.
States: the empty library loads 5 seeded cases, a loader while generating, and a gate that starts audio only after a user tap.
Responsive: side-by-side monitor and torso on a landscape tablet, tabs on a phone. Persist progress in localStorage.
```

---

## ChartSandbox — EHR Practice Environment (was: Epic practice tool)

**What changes:**
- A generic, unbranded EHR practice environment: patient search, chart summary, an allergy list, a medication list, an immunotherapy (shot) record, orders, notes and messages. No vendor names, logos or look-alike screens.
- Guided "missions" (e.g., "Document a reaction observed after an allergy shot," "Reconcile a med list," "Route a refill request") with step checking.
- A Gemini coach that explains why each workflow step matters and grades your documentation for completeness.
- Resets to a clean synthetic panel in one tap, with an audit trail of trainee actions you can export.

**How to compare:**
1. "Teach me to update an allergy list in an EHR." Winning: you actually click through a working chart and the mission auto-verifies, where ChatGPT or Claude gives steps in prose.
2. Write a sloppy post-shot observation note. Winning: field-level feedback listing missing elements (time, site, observation duration, vitals), without clinical advice.
3. Reset the sandbox, then export your audit trail. Winning: a clean reset plus a timestamped JSON/CSV log of your actions.

**Paste into AI Studio Build:**
```
Build "ChartSandbox," a generic EHR practice environment for training front-desk staff and medical assistants at an allergy & asthma clinic. Do NOT use any EHR vendor's name, logo, color scheme, or screen layouts. This is an original, unbranded design. Persistent banner: "Not for clinical use — training only. Synthetic patients."

Visual direction: crisp, information-dense but calm. Cool gray (#F4F6F8) background, slate text, indigo primary, a red reserved only for allergy alerts, compact data tables with 44px+ row tap targets in "tablet mode", IBM Plex Sans. WCAG AA, screen-reader labels on every table.

Layout: a left patient list/search, a center chart with tabs (Summary, Allergies, Medications, Immunotherapy Log, Vitals, Notes, Orders, Messages), and a right "Mission" panel.

Features:
1. Synthetic panel of 25 patients seeded on first load (Demo- prefixed names, fake MRNs starting with "TRN-").
2. Allergies: add/edit with reaction and severity; an allergy banner at the top of the chart.
3. Immunotherapy Log: vial, dilution, dose, site, time given, 30-min observation timer, reaction field.
4. Notes: templates (Check-in, Post-injection observation, Phone message) with required-field hints.
5. Orders & Messages: mock inbox with route/complete actions.
6. Missions: 10 guided tasks with step checklists that auto-verify against app state, a timer and a score.
7. Audit Trail: every trainee action logged, exportable as CSV/JSON. "Reset sandbox" restores the seed after confirmation.

AI: use the newest Gemini Pro model available in AI Studio. Never hard-code an API key. (a) "Coach" explains the purpose of the current step in plain language. (b) "Review my note" returns JSON {missingElements:[], clarityIssues:[], score:0-100, exemplar:string}. Validate against the schema, and on error show a retry option while keeping the note intact. (c) "Generate patient" returns schema-validated synthetic chart JSON. The AI never recommends doses or treatment. It refers clinical decisions to "the supervising provider."

Guardrails: block SSN-, card-, and real-MRN-like patterns. Names without the "Demo-" prefix trigger a confirm dialog.
States: empty search results, skeleton chart while loading, a "mission complete" celebration that respects reduced motion.
Persist in IndexedDB/localStorage. On a phone the panels collapse into a bottom tab bar.
```

---

## ProtoBench — Collaborative Medical Device Concept Studio (was: Medical device prototyping tool; real-time collaboration feature)

**What changes:**
- Merges both apps into one workspace: concept canvas, requirements, user-needs and risk table (an FMEA-style practice table), plus a sketch board, with live multi-tab collaboration.
- Real-time co-editing between browser tabs or devices on the same browser profile via BroadcastChannel, plus a shareable session file for teammates. Presence avatars and comment pins.
- Gemini turns a rough idea (e.g., "a kid-friendly spacer that counts inhaler puffs") into structured user needs, a requirements trace and a risk brainstorm, all editable.
- One-click export of a concept brief (print-to-PDF) and the JSON project.

**How to compare:**
1. "Develop a concept for a smart peak-flow meter for kids." Winning: populated, linked user-needs → requirements → risks tables you can edit, where ChatGPT or Claude gives a wall of bullets.
2. Open the app in two tabs and edit a requirement in one. Winning: it updates live in the other, with a presence indicator.
3. Export the concept brief. Winning: a clean, printable multi-section PDF with a traceability table.

**Paste into AI Studio Build:**
```
Build "ProtoBench," a collaborative concept studio for early-stage medical device ideas (educational/prototyping practice only). Persistent banner: "Not for clinical use — training and concept exploration only. No real patient data." Never claim regulatory compliance. Label risk analysis as a "practice exercise."

Visual direction: engineering-premium. Off-white drafting-paper background with a subtle grid, graphite text, electric-blue primary, mustard for comments, JetBrains Mono for IDs and Inter for UI. Cards have 1px hairline borders. Tap targets 48px+, WCAG AA.

Screens:
1. Projects: list, create, duplicate, import/export JSON. The empty state offers 3 sample projects (inhaler puff counter spacer, kid-friendly peak-flow meter, epinephrine auto-injector trainer).
2. Concept Canvas: freeform sticky notes, a simple pen sketch layer (pointer events, works with stylus), image upload for reference photos, and comment pins.
3. Needs → Requirements → Verification: three linked tables with IDs (UN-1, RQ-1, VR-1) and a traceability matrix view that highlights gaps.
4. Risk Table: hazard, cause, harm, severity 1-5, likelihood 1-5, computed score with a heat color plus a text label, and mitigation linked to a requirement.
5. Brief: an auto-assembled printable concept brief that exports via the print dialog.

Collaboration: real-time sync across tabs and windows using BroadcastChannel, with presence (name plus color avatar), live cursors on the canvas and last-writer-wins per field with a small conflict toast. "Share session" exports a .json snapshot that teammates import. Show a clear note that cross-device live sync requires a backend.

AI: use the newest Gemini Pro model available in AI Studio. Never hard-code an API key. "Expand idea" returns JSON matching the schema {userNeeds:[{id,text,user}], requirements:[{id,text,needId,verificationIdea}], risks:[{id,hazard,cause,harm,severity,likelihood,mitigationReqId}]}. Validate it and merge as suggestions the user accepts or rejects one by one. On a malformed response, retry once, then show an error and leave the data unchanged. Also include "Critique my requirement" (testability, ambiguity), returned as JSON.

States: loading shimmer on AI suggestions, an offline badge, undo/redo.
Persist in IndexedDB with autosave. On a tablet the canvas goes full-screen with a floating toolbar; on a phone the tables become cards.
```

---

## Retain MD — Evidence-Based Medical Study Engine (was: Medical student study tool using cognitive science)

**What changes:**
- A real spaced-repetition scheduler (an SM-2-style algorithm with ease and interval shown) instead of static flashcards, plus interleaved retrieval-practice sessions.
- Gemini turns pasted lecture notes into cloze cards, vignette-style MCQs and "explain why" prompts. It flags low-confidence items for the learner to verify against course material.
- Confidence-rating, elaborative-interrogation follow-ups, and a "teach it back" mode where the AI grades the learner's explanation.
- Includes an allergy/immunology starter deck (hypersensitivity types, asthma control concepts, immunotherapy basics) framed as study material, not clinical guidance.

**How to compare:**
1. Paste a page of notes and generate cards. Winning: editable cloze and MCQ cards that land in a scheduled queue with due dates, where ChatGPT or Claude gives a list.
2. Do a 20-card session and rate your confidence. Winning: a calibration chart (confidence vs. correct) and tomorrow's due count.
3. Use "Teach it back" on type I hypersensitivity. Winning: a rubric score, the specific missing concept, and a follow-up question.

**Paste into AI Studio Build:**
```
Build "Retain MD," a study engine for medical students grounded in cognitive science: spaced repetition, retrieval practice, interleaving, elaboration and calibration. Banner on every screen: "Educational use only — not for clinical decisions. Verify AI-generated content against your course materials."

Visual direction: scholarly calm. Paper-cream background (#FBF8F1), ink-navy text, muted plum accent, a serif (Source Serif) for card content and Inter for UI. Large readable card text (20px+), focus mode that hides all chrome, 48px tap targets, WCAG AA, and a dark mode.

Screens:
1. Today: due count, new-card cap, streak, an estimated session length and a "Start session" button.
2. Session: card front, then reveal, then confidence (1-4), then grade (Again/Hard/Good/Easy). Interleaves decks. Keyboard shortcuts 1-4 and space. Shows the next interval on each grade button.
3. Create: paste notes or upload a .txt/.md file, then "Generate" produces cloze, MCQ (vignette-style with 4-5 options and explanations) and "Why?" prompts, reviewed in a staging list where each card can be accepted, edited or discarded.
4. Teach-It-Back: the learner explains a concept by typing or voice dictation; the AI grades it with a rubric and asks one follow-up.
5. Insights: a retention forecast, a calibration plot (confidence vs. accuracy), weakest tags and a heatmap of review days.
6. Decks: tags, search, import/export (JSON and Anki-compatible CSV). Includes a seeded "Allergy & Immunology basics" deck.

Scheduling: implement SM-2-style intervals with ease factor, lapses and a learning step, all computed locally and deterministically.

AI: use the newest Gemini Pro model available in AI Studio. Never hard-code an API key. Generation returns JSON matching the schema {cards:[{type:"cloze"|"mcq"|"why", front, back, options?:[], answerIndex?, explanation, tags:[], confidence:"high"|"low"}]}. Flag low-confidence cards for verification. Teach-back returns {score:0-10, missingConcepts:[], misconceptions:[], followUpQuestion}. Validate everything, retry once, then show an error without losing the pasted notes. The AI explains and quizzes only and never gives advice about real patients.

Guardrails: warn if pasted notes contain SSN-like or patient-identifier patterns, and require removal before generating.
States: empty deck onboarding, a generation progress indicator, an offline review mode (works without AI).
Persist in IndexedDB. The phone layout is single-column with swipe-to-grade.
```
