# Music, video & animation

## AniGemini Studio — Multi-Layer Motion Editor (was: AniGemini – AI Animation Studio + Animation creating tool)

**What changes:**
- One shape and one AI-written @keyframes block becomes a real motion editor: multiple layers (shapes, text, SVG paths, uploaded images), a scrubbable timeline, and keyframes you can drag.
- A visual cubic-bezier easing editor with spring and step presets replaces the timing dropdown.
- The AI edits the timeline you already have ("make the star land 200ms later and overshoot") and returns a structured diff, not a fresh CSS string.
- Export goes past copied CSS to a CSS bundle, Lottie-style JSON, GIF, and WebM/MP4, plus a preset library and full undo/redo.

**How to compare:**
1. Ask: "Three dots bounce in sequence like a loading indicator, then merge into a circle." Winning: three editable layers with staggered keyframes on the timeline that play right away. ChatGPT or Claude will hand back one CSS snippet you have to paste somewhere else.
2. Follow up with "slow the second dot and add squash-and-stretch." Winning: only the dot-2 keyframes change, and one undo step reverts the edit.
3. Export a 3-second GIF and a Lottie-style JSON. Winning: you download real files in one click. A chat answer can only describe how to make them.

**Paste into AI Studio Build:**
```
Rebuild this app as "AniGemini Studio", a professional browser-based motion editor. React + Tailwind, single page.

LAYOUT (desktop): left Layers panel, center Stage (16:9, 1:1 or 9:16 artboard with checkerboard background), right Inspector, bottom Timeline. On mobile, the Stage sits on top and the Layers/Inspector/Timeline panels become a bottom sheet with tabs.

LAYERS: add shapes (circle, square, triangle, star, blob), text, SVG path (paste markup), and uploaded images. Layers can be reordered by drag, renamed, hidden, locked, and grouped.

TIMELINE: one track per layer with property rows (x, y, scale, rotate, opacity, fill, blur, border-radius). Diamond keyframes can be dragged in time, multi-selected with shift, copied and pasted. Playhead scrubbing, loop region, zoom, snap to 1/24 s. Space plays and pauses, K adds a keyframe, Delete removes one, Cmd/Ctrl+Z and Shift+Cmd/Ctrl+Z undo and redo (100-step history).

EASING: clicking a segment between two keyframes opens a cubic-bezier curve editor with draggable handles, a live preview dot, and presets (ease-out-expo, back-overshoot, spring, steps).

AI DIRECTOR: a prompt bar under the stage. Use the newest Gemini Pro model in AI Studio. Send the current timeline JSON plus the user request, and require structured JSON output against a schema: {operations:[{op:"addLayer"|"updateLayer"|"setKeyframe"|"deleteKeyframe"|"setEasing", layerId, property, time, value, easing}], summary}. Apply the operations as a single undoable step and show the summary as a toast with an Undo button. Add suggestion chips: "Make it bouncier", "Stagger these", "Add an intro". Validate the response; on a malformed reply or API error, retry once with backoff, then show an inline error with Retry. Use AI Studio's built-in API key handling.

PRESETS: a gallery of 12 animated thumbnails (pop-in, wiggle, orbit, typewriter, morph-pulse, and others) that apply to the selected layer.

EXPORT dialog: CSS (@keyframes + classes), Lottie-style JSON, GIF (render frames to canvas and encode in the browser), WebM via MediaRecorder on a canvas capture, and PNG sequence as a ZIP. Show a progress bar and a cancel button.

PERSISTENCE: autosave projects to IndexedDB, plus a project list with thumbnails, duplicate, and delete.

STATES: an empty stage invites the user to "Add a layer or describe a motion"; a skeleton shimmer shows while the AI works.

VISUAL DIRECTION: a dark editor in the spirit of a film-grading suite. Charcoal #111214 panels, a 1px #2A2C30 grid, signal-orange #FF6B2C as the only accent, Inter for UI, JetBrains Mono for values, tight 4px spacing rhythm. No gradients.

ACCESSIBILITY: every control keyboard reachable, ARIA labels on icons, reduced-motion toggle for the UI chrome.
```

## Veo Director — Shot-Based AI Video Studio (was: Use the Veo API)

**What changes:**
- A bare prompt box that calls Veo becomes a storyboard tool: a project holds shots, and each shot has its own prompt, reference image, aspect ratio, and duration.
- Gemini rewrites rough ideas into a cinematographer-grade shot list (lens, movement, lighting, mood) before anything is generated.
- Long-running generations are handled properly: a job queue, polling, progress, cancel, and a retry that keeps everything you set.
- Finished clips go into a gallery where you can compare takes side by side, trim them, play them in sequence, and download them.

**How to compare:**
1. Ask: "A 4-shot teaser for a cello recital at dusk." Winning: four structured shots with camera notes that you can edit and generate one by one. ChatGPT or Claude can write the shot list but can't produce any video.
2. Generate two takes of the same shot with one changed parameter. Winning: the takes play side by side and you can mark one as the keeper.
3. Kill the network while a generation is running. Winning: a clear error with a resume or retry option, and nothing in the project is lost.

**Paste into AI Studio Build:**
```
Rebuild this app as "Veo Director", a storyboard-first AI video studio. React + Tailwind.

SCREENS:
1. Projects: a grid of project cards with a poster frame, shot count, and last-edited date. "New project" asks for a title and a one-paragraph idea.
2. Storyboard: a horizontal strip of Shot cards (drag to reorder). Each card has a prompt, negative prompt, aspect ratio (16:9 / 9:16), duration, an optional reference image upload, and a status badge (Draft, Queued, Generating, Ready, Failed).
3. Shot detail drawer: prompt editor with token-style chips for Camera (dolly-in, handheld, drone, static), Lens (24mm, 50mm, 85mm), Lighting (golden hour, neon, overcast), and Mood. Chips insert phrases into the prompt.
4. Takes gallery: every generation for a shot, played in sync side by side, with a star to mark the keeper.
5. Sequence preview: plays the keepers back to back with a simple trim per clip.

AI:
- "Plan shots" uses the newest Gemini Pro model in AI Studio to turn the project idea into a shot list. Use structured JSON output with the schema {shots:[{title, prompt, camera, lens, lighting, mood, durationSec, aspect}]}.
- "Enhance prompt" rewrites one shot prompt in cinematic language and shows a diff with accept or reject.
- Generation uses the newest Veo model available in AI Studio. Treat it as a long-running operation: queue jobs, poll for status, and show elapsed time and a progress animation. Allow cancel. On failure or a safety block, show the reason in plain language and offer "Edit prompt" and "Retry" (exponential backoff, max 3 tries). Never hard-code keys; use AI Studio's built-in API key handling.

PERSISTENCE: store projects and shots in IndexedDB, with video blobs cached so a reload keeps everything. Undo/redo for storyboard edits.

EXPORT: download each clip as MP4, "Download keepers" as a ZIP, and a shot list as PDF/Markdown.

STATES: an empty storyboard shows three example idea chips; skeleton cards while planning; a mobile layout with a vertical shot list and full-width player.

VISUAL DIRECTION: cinema dark-room. Near-black #0B0B0C, warm paper-white text #EDE8DF, tungsten amber #E8A33D accent, Fraunces serif for titles, Inter for UI, letterboxed 2.39:1 hairline frames around players, generous 24px gutters.

ACCESSIBILITY: keyboard shortcuts (G generate, J/K/L playback, arrows move between shots), focus rings, and captions for status changes via aria-live.
```

## ReelPilot — Guided Reel Production Studio (was: Step-by-step tool that walks you through making and posting any type of video reel)

**What changes:**
- A generic checklist becomes a guided wizard that adapts to the reel type (tutorial, performance clip, behind-the-scenes, product, travel) and to the platform's specs.
- The AI writes a timed hook, beat-by-beat script, and shot list, then reads the user's uploaded clips and frames to suggest cuts and on-screen text.
- A light in-browser editor assembles the clips with captions, safe-zone overlays, and a 9:16 preview, and exports an MP4.
- A posting kit (caption, hashtags, cover frame, best-time checklist) is ready to copy. Nothing auto-posts.

**How to compare:**
1. Ask: "A 20-second reel of me practicing a Bach cello suite." Winning: a timed beat sheet, shot list, and on-screen text, all editable inside the project. A chatbot gives a prose list.
2. Upload three clips and ask for an edit. Winning: a rough cut you can preview in 9:16 with captions inside the safe zones.
3. Ask for a caption and 3 cover options. Winning: cover frames taken from your own footage and a caption already sized to the platform limit.

**Paste into AI Studio Build:**
```
Rebuild this app as "ReelPilot", a step-by-step reel production studio. React + Tailwind, mobile-first because most users will be on a phone.

FLOW (a stepper at the top with 6 steps; you can go back to any step and progress is saved):
1. Goal: pick a reel type (Tutorial, Performance, Behind the scenes, Product, Travel, Talking head, Custom) and a target platform (Reels, Shorts, TikTok, generic 9:16). Show that platform's spec card: length, safe zones, caption limit.
2. Plan: the newest Gemini Pro model in AI Studio writes a plan with structured JSON output against the schema {hook:{text,seconds}, beats:[{start,end,visual,onScreenText,voiceover}], shotList:[{shot,framing,tip}], musicMood}. Show it as an editable beat timeline with a "Regenerate this beat" action on each beat.
3. Shoot: a checklist made from the shot list, with framing tips and an optional camera recorder (getUserMedia) that saves takes.
4. Upload & cut: drop clips. Sample frames from each clip and send them to Gemini so it can suggest in/out points for each beat. Show a horizontal clip timeline with trim handles, reorder, and on-screen text blocks. A 9:16 preview shows platform safe-zone overlays you can toggle.
5. Polish: caption styles (3 tasteful presets), auto-generated captions from voiceover text, and an optional user-uploaded music track with a volume ducking slider (Web Audio).
6. Post kit: export the MP4 (canvas + MediaRecorder, with a progress bar), 3 cover frame candidates, a caption within the character limit, hashtags, and a pre-post checklist. Show copy buttons only; never post automatically.

DATA: projects and media live in IndexedDB; autosave on every change; undo/redo in the editor.

ERRORS: if the AI call fails, keep the user's edits, show an inline banner with Retry (with backoff), and offer a template-based fallback plan. Validate the AI JSON before rendering. Use AI Studio's built-in API key handling.

EMPTY STATES: the home screen shows "Start a reel" with type cards and a short 3-step explainer.

VISUAL DIRECTION: an editorial magazine feel. Off-white #F6F3EE background, ink #141414, a single tomato-red #E5482F accent, Söhne-like grotesk (use Inter Tight) for headings, large step numerals, 8px radius, thumb-reachable bottom action bar on mobile.

ACCESSIBILITY: all steps keyboard navigable, form labels on every input, captions on by default in the preview.
```

## Monolith — Monochrome Music Studio (was: Music studio tool + Music studio interface)

**What changes:**
- A mockup-style interface becomes a working browser studio: a multitrack arranger, a step sequencer, a piano roll, and a mixer, all running on the Web Audio API.
- Recording from the mic and importing the user's own audio files, with waveforms, per-track effects (EQ, compressor, reverb, delay), and live meters.
- An AI producer that reads the project state and returns structured edits: chord progressions, drum patterns, arrangement and mix notes. If music generation (Lyria) is available in AI Studio, it can also add generated stems.
- A built-in user manual and a references panel, so it's professional and learnable.

**How to compare:**
1. Ask: "A moody 90 BPM progression in D minor with a sparse drum groove." Winning: MIDI clips you can play right away in the piano roll and sequencer. A chatbot gives chord names as text.
2. Record 8 bars of cello and ask "how should I mix this against the pads?" Winning: concrete EQ and compressor settings that the app applies as one undoable step.
3. Export the mix. Winning: a WAV download plus a MIDI file per instrument track.

**Paste into AI Studio Build:**
```
Rebuild this app as "Monolith", a professional, strictly monochrome music studio in the browser. React + Tailwind + Web Audio API.

SCREENS (switched with a top bar; Tab cycles views):
1. Arrange: tracks stacked vertically (Audio, Instrument, Drum). Clips can be dragged, resized, split (S), duplicated (Cmd/Ctrl+D) and looped. A transport shows play/stop/record, BPM, time signature, metronome, loop range, and bar:beat:tick position.
2. Piano roll: draw, drag, and resize notes; velocity lane; quantize; scale highlighting.
3. Step sequencer: a 16-step grid per drum voice (synthesized kick/snare/hat/clap using Web Audio oscillators and noise; users may also load their own samples). Includes swing.
4. Mixer: channel strips with gain, pan, mute/solo, 3-band EQ, compressor, reverb/delay sends, and peak/RMS meters drawn on canvas.
5. Manual: searchable docs for every feature, a keyboard shortcut sheet, and a "References" page where users pin their own uploaded reference tracks for A/B against the mix (with loudness matching).

AUDIO SOURCES: only audio the user records (getUserMedia) or uploads, built-in synths, or audio generated in-app. No scraping or bundled commercial content. Draw waveforms from decoded buffers.

AI PRODUCER (side panel): use the newest Gemini Pro model in AI Studio. Send a compact JSON summary of the project (tempo, key, tracks, clip notes, mixer settings) and require structured JSON output against the schema {actions:[{type:"addMidiClip"|"setPattern"|"setMixer"|"addMarker", trackId, data}], explanation}. Show a preview list with checkboxes and apply the selected actions as one undoable step. If a music-generation model (Lyria) is available in AI Studio, add "Generate stem" that inserts the result as an audio clip; otherwise hide that button. On errors, retry with backoff and show a quiet inline message. Use AI Studio's built-in API key handling.

PERSISTENCE: projects in IndexedDB (audio buffers stored as blobs), autosave, 200-step undo/redo.

EXPORT: mixdown to WAV via OfflineAudioContext, stems as a ZIP, MIDI per track, and a project file (.monolith JSON + audio) for backup.

STATES: an empty project offers "Start from template" (Beat sketch, Singer-songwriter, String quartet sketch); audio permission denied gets a clear explanation.

VISUAL DIRECTION: pure monochrome, like high-end hardware. #000 / #0E0E0E / #1A1A1A surfaces, #FFFFFF and 60% grey text, no color at all. Selected states use inverted fills, meters are white bars. IBM Plex Mono for numbers, Neue Haas-style grotesk (Inter) for labels, 1px hairlines, square corners. Mobile: Arrange and Mixer collapse into a single-track focus view with large touch targets.

ACCESSIBILITY: full keyboard transport (Space, R, L, arrow nudges), ARIA on knobs (role=slider with value text).
```

## Vinyl Room — Personal Music Library & Player (was: Music app like Zora: hold songs, listen, create playlists)

**What changes:**
- Basic storage and playback becomes a polished personal library: drag-in uploads, automatic tag and duration reading, album art, and a smart search.
- Gapless queue, crossfade, a 10-band EQ, and a live spectrum visualizer through the Web Audio API.
- Gemini builds playlists from the user's own tracks by mood or description and writes liner notes for them. It never recommends or fetches outside catalog music.
- Offline-first storage in IndexedDB, with backup and restore, keyboard and media-key control, and a full mobile player.

**How to compare:**
1. Upload 30 of your own tracks and ask for "a calm Sunday-morning practice playlist." Winning: a playlist built only from your library, with a reason for each pick. A chatbot can't hear or see your files.
2. Ask: "Sort my recital recordings by key and tempo." Winning: tempo and key estimated in the app and shown as sortable columns.
3. Reload the page offline. Winning: the library, playlists, and playback position are all still there.

**Paste into AI Studio Build:**
```
Rebuild this app as "Vinyl Room", a beautiful personal music library and player for audio the user owns. React + Tailwind + Web Audio API.

SOURCES: only files the user uploads (MP3, WAV, FLAC, M4A, OGG) or audio they generate elsewhere and import. No streaming catalogs, scraping, or external track lookups.

SCREENS:
1. Library: drag-and-drop import with per-file progress. Read ID3/metadata where possible and fall back to the filename. Views: Songs (sortable table: title, artist, album, duration, BPM, key, plays), Albums (art grid), Artists. Fuzzy search with "/" to focus.
2. Track detail: waveform, editable tags, custom art upload, notes.
3. Playlists: create, rename, drag to reorder, cover collage, duplicate, delete with undo. Smart playlists by rules (genre, BPM range, recently added, most played).
4. Now Playing: full-screen view with large art, a real-time spectrum/radial visualizer (AnalyserNode on canvas), lyrics/notes pane, 10-band EQ with presets, crossfade 0-12 s, playback speed, A-B loop (useful for practicing).

AUDIO ANALYSIS: estimate BPM and loudness in the browser after import, in a Web Worker so the UI stays responsive.

AI (use the newest Gemini Pro model in AI Studio): a "Make a playlist" prompt. Send only the user's library metadata (titles, tags, BPM, key, notes), never audio, and require structured JSON output against the schema {name, description, trackIds:[...], reasons:{trackId:reason}}. Drop any trackId that isn't in the library. Also "Write liner notes" for a playlist. On failure, retry with backoff and fall back to a rules-based playlist. Use AI Studio's built-in API key handling.

PERSISTENCE: audio blobs and metadata in IndexedDB; remember the queue, position, volume, and EQ. Export/import a backup ZIP.

CONTROLS: Space play/pause, arrow keys seek, Shift+arrows next/previous, Media Session API for lock-screen and media keys.

STATES: an empty library shows a large drop zone ("Bring your music in"); unsupported files get an inline reason; a storage-quota warning shows usage.

MOBILE: bottom tab bar (Library, Playlists, Search), a mini-player that expands into Now Playing with swipe-down to close.

VISUAL DIRECTION: a warm listening room. Deep walnut #1C1612 background, cream #F2E8D5 text, brass #C9A45C accent, album art as the main source of color (extract a dominant color to tint Now Playing), Playfair Display for headings, Inter for lists, soft 12px radii.

ACCESSIBILITY: visible focus, a reduced-motion option for the visualizer, screen-reader labels on transport controls.
```

## [Your Name] — Cellist & Pianist (was: Musician portfolio website for [Your Name])

**What changes:**
- A static bio page becomes a concert-grade portfolio: a hero with self-hosted performance video, a repertoire database, a media player for recordings [Your Name] uploads, and an events calendar.
- An admin mode (local, no backend) lets [Your Name] edit every section in place, upload media, and reorder content. Content lives in IndexedDB and can be exported as a JSON bundle.
- Gemini helps write: polished bios at 50/150/400 words, program notes for a given piece, and press-kit text, all in [Your Name]'s voice from her own notes.
- Includes a downloadable EPK (electronic press kit) PDF and a booking inquiry form with validation, plus strong SEO and accessibility.

**How to compare:**
1. Ask for "a 150-word bio for a chamber festival program." Winning: it's generated from [Your Name]'s stored facts, saved as a version you can compare, and published to the site in one click.
2. Ask for "program notes for Elgar's Cello Concerto, 200 words." Winning: the notes attach to that repertoire entry and appear on the concert page.
3. Look at the site on a phone. Winning: fast load, smooth audio playback, an elegant layout, and a Lighthouse accessibility score of 95+. Chat tools only give you code to assemble yourself.

**Paste into AI Studio Build:**
```
Build "[Your Name] — Cellist & Pianist", an elegant portfolio website with a built-in editor. React + Tailwind, single page with hash routes.

PUBLIC SECTIONS:
1. Hero: full-bleed performance video or photo (user-uploaded), name in large serif, the line "Cellist · Pianist", buttons "Listen" and "Book".
2. About: bio with a toggle for short, medium, and long versions; a portrait; education and teachers.
3. Listen: a custom audio player for recordings [Your Name] uploads. Playlist by instrument (Cello / Piano / Chamber), waveform scrubber drawn with Web Audio, track notes. Only her own uploaded audio.
4. Watch: a video grid (uploaded files or YouTube links she provides) in a lightbox.
5. Repertoire: a filterable table (instrument, composer, era, solo/chamber/concerto) with search; each piece can have program notes.
6. Concerts: upcoming and past events with date, venue, program, and an add-to-calendar .ics download.
7. Press & EPK: quotes, high-res photo downloads, and a "Download EPK" PDF made from site content.
8. Contact/Booking: a form (name, email, event type, date, message) with validation and success and error states; it opens a pre-filled mailto, with no external form service.

ADMIN MODE (toggle with Shift+E, protected by a simple local PIN she sets): click any text to edit inline, drag to reorder sections and items, upload media, plus an undo/redo bar. Store content and media in IndexedDB. Export/import a site.json bundle.

AI WRITING ASSISTANT (admin only; use the newest Gemini Pro model in AI Studio): generate bios, program notes for a selected piece, and concert blurbs from her stored facts and tone notes. Use structured JSON output with the schema {short, medium, long} or {title, notes, wordCount}. Show a side-by-side diff before saving; keep version history. Retry with backoff on errors. Use AI Studio's built-in API key handling. Optionally use the newest Gemini image model to create abstract, non-photographic poster art for concerts.

VISUAL DIRECTION: a quiet concert hall. Ivory #FAF7F2 background, ink #1B1B1B text, a single rosewood #7A2E2E accent (the color of cello varnish), Cormorant Garamond for display and Inter for body text, wide margins, a 12-column grid, thin rules between sections, subtle fade-up on scroll (respecting prefers-reduced-motion).

MOBILE: sticky minimal nav that becomes a full-screen menu, a persistent mini audio player.

QUALITY: semantic HTML, alt text fields required on uploads, meta and Open Graph tags, lazy-loaded media, keyboard-accessible player.
```

## Mise — Script-to-Visual Recipe Storyboards (was: Recipe visualizer)

**What changes:**
- A text-in, pictures-out demo becomes a structured recipe engine: Gemini parses any written recipe or free-form script into ingredients, steps, timings, and techniques, then generates a consistent visual for each step.
- Visual consistency across steps comes from a shared style and kitchen "set" (same counter, cookware, lighting), with per-step regeneration and image editing.
- A cook mode with large type, step timers, voice read-aloud, and hands-free navigation.
- Exports to a printable recipe card PDF, a step carousel image set, and an optional short Veo clip for the hero step.

**How to compare:**
1. Paste a messy paragraph recipe for kimchi fried rice. Winning: a clean ingredient list with quantities, numbered steps with timers, and 8 coherent step images. A chatbot returns text or one image.
2. Ask: "Make step 4 show the pan from above." Winning: only that image changes, and the style stays consistent with the other steps.
3. Scale the recipe from 2 to 6 servings and switch to metric. Winning: everything recalculates right away and the steps update too.

**Paste into AI Studio Build:**
```
Rebuild this app as "Mise", which turns a written recipe or cooking script into an illustrated, cookable storyboard. React + Tailwind.

FLOW:
1. Write: a large editor where the user types or pastes any recipe, notes, or a spoken-style script. Sample chips: "Grandma's dumplings", "15-min pasta". Style picker: Editorial photo, Watercolor, Flat illustration, Claymation.
2. Parse: the newest Gemini Pro model in AI Studio converts the text with structured JSON output against the schema {title, servings, totalMinutes, ingredients:[{name, qty, unit, prep}], equipment:[...], steps:[{n, instruction, durationMin, technique, visualPrompt, ingredientsUsed:[...]}], tips:[...]}. Show the parsed result for review and editing before images are generated, with warnings for ambiguous quantities.
3. Visualize: generate one image per step with the newest Gemini image model. Prepend a shared "set bible" (counter surface, cookware, lighting, camera angle, chosen style) to every prompt so the steps look like one shoot. Steps render in parallel, max 3 at a time, with per-card skeletons. Each card has Regenerate, "Edit image" (a text instruction to the image model), and Lock.
4. Storyboard view: a vertical sequence of step cards on mobile and a 2-3 column board on desktop. Ingredient chips highlight in each step.
5. Cook mode: full-screen, one step at a time, huge type, a countdown timer per step with a chime (Web Audio), read-aloud via speechSynthesis, arrow keys or voice-free large tap zones, and screen wake lock.
6. Optional hero clip: with the newest Veo model, generate a short clip for one selected step, with polling and cancel.

TOOLS: a servings scaler and unit switcher (US/metric) that recalculate quantities; a shopping list grouped by aisle that you can copy.

ERRORS: validate AI JSON; on failure, retry with backoff, keep the user's text, and let them retry a single step image without redoing the rest. Use AI Studio's built-in API key handling.

PERSISTENCE: recipes and images in IndexedDB, a recipe library with search, undo/redo for edits.

EXPORT: printable recipe card PDF, step images as a ZIP, carousel-ready 4:5 images with step text overlaid.

VISUAL DIRECTION: a modern cookbook. Flour-white #FBF9F4 background, espresso #2B211C text, saffron #E3A018 accent, Recoleta-style soft serif (use Fraunces) for titles, Inter for body text, oversized step numerals, generous whitespace, photo cards with 6px radius.

ACCESSIBILITY: alt text on images from each step's instruction, focus order, high-contrast cook mode.
```

## Puppy — A Warm, Capable Personal AI Companion (was: Puppy)

**What changes:**
- A themed chatbot becomes a personal assistant with a consistent persona, an animated puppy avatar that reacts to state (listening, thinking, happy, confused), and voice input and output.
- Real memory: Puppy remembers facts the user approves, shows them on an editable "What Puppy knows" page, and forgets on request. Everything stays local.
- Built-in tools with structured actions: reminders, a to-do list, a daily check-in, practice logs (for a musician), and notes. Gemini returns JSON actions that the app runs and confirms.
- Mood-aware daily briefings, streaks, and gentle nudges, without being sycophantic.

**How to compare:**
1. Say: "Remind me to practice the Saint-Saëns at 7 and log 45 minutes of cello today." Winning: a reminder is scheduled and a log entry is created, each confirmed with an undo. A chatbot only acknowledges the request.
2. A week later, ask: "How has my practice been?" Winning: a chart and summary built from stored logs. A chat tool that has no memory of your logs can't do this.
3. Ask: "What do you know about me?" Winning: an editable list of memories, each with delete. That's transparent and under your control.

**Paste into AI Studio Build:**
```
Rebuild this app as "Puppy", a warm, capable personal AI assistant with a dog persona. React + Tailwind.

PERSONA: Puppy is cheerful, loyal, concise, and honest. Light dog flavor ("*tail wag*" at most once per conversation, never in serious moments). It drops the playfulness when the user is stressed, and it never flatters or invents facts.

SCREENS:
1. Home: an animated puppy avatar (SVG/CSS) with states: idle, listening, thinking, happy, confused, sleeping. A greeting with today's briefing (date, due tasks, reminders, practice streak) and quick chips: "Plan my day", "Log practice", "Remind me…", "Just chat".
2. Chat: a streaming conversation; a mic button for speech-to-text (Web Speech API) and an optional read-aloud reply (speechSynthesis) with a choice of voice. Markdown rendering.
3. Tasks & Reminders: a list with due times; browser notifications (ask permission with a clear explanation); snooze.
4. Practice Log: entries (date, instrument, piece, minutes, notes), a weekly bar chart, and streaks.
5. Memory: "What Puppy knows". Each memory card has the source message, date, an edit button, and a delete button. Includes "Forget everything" with confirmation.
6. Settings: persona intensity slider, voice, theme, export/import data.

AI: use the newest Gemini Pro model in AI Studio. Each turn sends the persona instructions, relevant memories, and today's state. Require structured JSON output against the schema {reply, actions:[{type:"addTask"|"addReminder"|"logPractice"|"addNote"|"proposeMemory", data}], mood:"idle"|"happy"|"thinking"|"confused"}. Execute actions locally and show a confirmation chip under the message with Undo. "proposeMemory" asks the user before saving. Stream the reply text. On errors, the avatar shows the confused state, with a friendly message and Retry (backoff). Use AI Studio's built-in API key handling; no hard-coded keys.

PERSISTENCE: everything in IndexedDB (chats, tasks, logs, memories); nothing leaves the device except the model calls. Global undo for the last 20 actions.

STATES: first run is a 3-step onboarding (name, what Puppy should help with, voice on/off); an empty task list shows a sleepy puppy.

VISUAL DIRECTION: soft and friendly but grown-up. Oat #F4EFE6 background, cocoa #3B2A20 text, a single collar-blue #2F6FED accent, Nunito for headings, Inter for body, rounded 20px cards, subtle paper grain, no neon or purple gradients. A dark mode with warm charcoal.

MOBILE: chat-first layout with a bottom tab bar (Home, Chat, Tasks, Practice, Me), large mic button.

ACCESSIBILITY: avatar state also announced via aria-live; all actions keyboard accessible; reduced-motion stills for the avatar.
```
