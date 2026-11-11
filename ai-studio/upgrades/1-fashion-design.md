# Fashion, design & visual studios

## CoutureAI Atelier (was: CoutureAI Studio + "Fashion designer: bring concepts to life")
**What changes:**
- Goes from "type an idea, get one picture" to a full design workflow: brief → mood board → structured tech pack → flat sketch + editorial render → revisions.
- AI returns a structured tech pack (silhouette, fabrics, trims, construction, colorways, size range) that you can edit field by field, not a block of prose.
- Region-based edits ("make only the sleeves bishop sleeves") through image editing, with a version history you can browse and undo.
- Collections that save to your device (IndexedDB) and export to PDF line sheets and PNG files.

**How to compare:**
1. "Design a 4-look resort capsule inspired by Moroccan tilework." Winning: four looks that clearly belong together, each with an editable tech pack and consistent renders. A chat assistant gives text plus a few unrelated images.
2. Change one look's fabric to raw silk and lengthen the hem. Winning: only that look updates, the rest of the image stays the same, and the old version is still in history.
3. Export the capsule. Winning: a clean PDF line sheet with flats, swatches and specs, ready to send to a pattern maker.

**Paste into AI Studio Build:**
```
Rebuild this app as "CoutureAI Atelier", a professional fashion design studio for taking a garment concept from idea to tech pack.

Visual direction: an editorial atelier look. Warm ivory background (#F7F3EC), ink-black text, a single oxblood accent (#6B1E2A). Use a high-contrast serif (Cormorant Garamond) for headings and Inter for the interface. Generous whitespace, hairline 1px dividers, no gradients, small-caps section labels.

Screens:
1. Collections home: a grid of saved collections with cover images. Empty state shows "Start your first collection" with three example briefs the user can click.
2. Brief: a text field for the concept plus chips for season, customer, price tier and mood words; optional upload of up to 6 inspiration images.
3. Studio (three panels): a left rail of looks in the collection, a center canvas (toggle between flat sketch and editorial render), and a right tech-pack inspector.
4. Line sheet preview and export.

AI: use the newest Gemini Pro model in AI Studio for reasoning and the newest Gemini image model for image generation and editing. Generate tech packs as structured JSON against a schema: name, silhouette, fabrics[{name, weight, composition}], trims[], construction notes[], colorways[{name, hex}], size range, and a cost tier. Stream the design rationale text while the images render. Every field in the inspector is editable, and "Regenerate render" uses the edited spec. Support region edits: the user brushes a mask on the canvas and types an instruction, and only that area is edited. Keep looks within a collection consistent by passing the collection's palette and mood into every prompt.

Reliability: skeleton loaders that show the current step, clear error cards with Retry (automatic retry with backoff up to 3 times), and never lose the user's input after a failure. Keep the API key on AI Studio's built-in handling; never hard-code it.

Persistence: save collections, images and version history in IndexedDB. Undo/redo (Cmd/Ctrl+Z, Shift+Cmd/Ctrl+Z) for every spec edit and image version.

Export: PNG per look, a ZIP of the collection, and a PDF line sheet (flat, render, swatches, specs).

Mobile: panels collapse into tabs (Looks / Canvas / Specs) with a bottom action bar. Accessibility: full keyboard navigation, visible focus rings, alt text generated for every image, WCAG AA contrast.
```

## Modella Studio (was: Modella AI – High-End Virtual Modeling Studio + "Generate modeling photos from model, garments, pose, background, measurements")
**What changes:**
- A guided shoot builder (Model → Garments → Pose → Set → Measurements → Shoot) replaces one crowded form, with a live "shoot card" summary.
- Measurements and garment size feed a fit note, so the image shows realistic drape and the app explains how the garment would fit.
- Batch shoots: one outfit across 4 poses or backgrounds in one run, shown as a contact sheet you can compare.
- A consent and rights gate for every real-person photo, plus a visible "AI-generated" label option on exports.

**How to compare:**
1. Upload a model photo, a blazer and wide-leg trousers, then ask for a studio shot. Winning: the face and garment details (buttons, lapel, fabric texture) stay true. A chat assistant usually changes the face or invents details.
2. Run the same outfit in 4 poses on a concrete rooftop. Winning: a consistent contact sheet with the same person and outfit across all frames.
3. Enter measurements (bust 86, waist 68, hip 94, height 172) with garment size M. Winning: a fit note that makes sense ("slightly loose at the waist") and an image that matches it.

**Paste into AI Studio Build:**
```
Rebuild this app as "Modella Studio", a high-end virtual photo studio that produces on-model fashion images from a model photo, garment photos, a pose, a background and body measurements.

Visual direction: dark photo-studio look. Charcoal background (#121212), off-white text, brushed-silver accent (#C9C5BD), thin 1px borders. Use Didot-style display type (Bodoni Moda) for headings and IBM Plex Sans for the interface. The images are the hero: large and with little chrome around them.

Flow, as a stepper with a sticky "shoot card" summary on the right:
1. Model: upload a photo of the model. Before upload, show a required checkbox: "I own this photo or have the model's permission to use it for AI-generated images." Block generation until it is checked. Detect and warn about low-resolution or multi-person photos.
2. Garments: upload up to 4 garment photos (front and optional back), tag each as top, bottom, dress, outerwear, shoes or accessory, with size and fabric.
3. Pose: a gallery of pose presets (editorial stand, walk, seated, three-quarter turn, hands in pockets) plus a custom text pose.
4. Set: background presets (seamless white, concrete rooftop, Paris street, golden hour beach) or upload a background.
5. Measurements: height, bust, waist, hips, in cm or inches, with a unit toggle.
6. Shoot: choose 1, 2 or 4 variations, and an aspect ratio (4:5, 1:1, 9:16).

AI: use the newest Gemini Pro model in AI Studio for reasoning and the newest Gemini image model for image generation and editing. First call the reasoning model to return JSON against a schema: {fitNotes[], garmentDetailsToPreserve[], lightingPlan, promptForImage}. Then send the model photo, garment images and that prompt to the image model. Preserve identity and garment details. Show results as a contact sheet. Each frame has Star, Refine (text edit), Upscale and Download. Retry automatically with backoff on API errors, then show a friendly error card with Retry that keeps all inputs.

Keep the API key on AI Studio's built-in handling; never hard-code it.

Persistence: save shoots and starred frames in IndexedDB, with a Projects page. Undo/redo for edits.

Export: PNG/JPG per frame, ZIP of the contact sheet, and an option to stamp a small "AI-generated" mark.

Empty, loading and error states for every step. Mobile: the stepper becomes full-screen steps with a bottom Next button. Accessibility: keyboard reachable controls, labelled inputs, focus states and alt text for all results.
```

## FitForm Mannequin (was: "Dress up a mannequin with uploaded clothing photos, switch male/female")
**What changes:**
- Uploaded clothing photos are cut out automatically and become a reusable wardrobe of items, sorted by category.
- Clothes snap onto the right body zone and layer in the correct order (shirt under jacket), with drag, scale and nudge controls.
- Male/female/neutral mannequin switch keeps the outfit and re-fits it, instead of resetting everything.
- An optional "Make it photoreal" render, plus saved outfits, undo, and PNG export.

**How to compare:**
1. Upload a T-shirt, jeans and a coat, then dress the female mannequin. Winning: clean cutouts, correct layering, done in under a minute. A chat assistant cannot give you an interactive dressing canvas.
2. Switch to the male mannequin. Winning: the outfit stays on and re-fits; nothing is lost.
3. Save the look and export a photoreal render. Winning: a reusable saved outfit and a high-resolution image that matches the garments.

**Paste into AI Studio Build:**
```
Rebuild this app as "FitForm Mannequin", an interactive dressing tool where users upload clothing photos and dress a mannequin they can switch between female, male and neutral forms.

Visual direction: a clean showroom look. Pale stone background (#EDEBE6), graphite text (#2A2A2A), a muted sage accent (#7C8B74). Use Space Grotesk for headings and Inter for the interface. Soft shadows under the mannequin, rounded 12px cards, no gradients.

Layout:
- Left: Wardrobe panel with tabs (Tops, Bottoms, Dresses, Outerwear, Shoes, Accessories) and an upload drop zone. Empty state: "Drop clothing photos here" with tips (flat lay or hanger, plain background).
- Center: the mannequin canvas, shown as a clean SVG figure, with a Female / Male / Neutral segmented control and a skin-tone-neutral finish.
- Right: Layers panel listing worn items in order with drag-to-reorder, visibility toggle and remove.

Upload pipeline: when a photo is added, use the newest Gemini image model to remove the background and return a clean cutout, and use the newest Gemini Pro model in AI Studio to classify it with structured JSON against a schema: {category, subcategory, colors[], pattern, layerOrder, anchorZone}. Show a progress state on each wardrobe card and a Retry button if processing fails (automatic retry with backoff first).

Dressing: click or drag an item onto the mannequin and it snaps to its anchor zone (shoulders, waist, feet) at the right scale. Users can fine-tune with drag handles, arrow keys (Shift for bigger steps) and a scale slider. Switching body form keeps every item and re-fits it to the new anchor points.

"Make it photoreal": sends the composed outfit to the newest Gemini image model to render a realistic studio photo of a mannequin wearing it. Show a loading state and an error card with Retry.

Keep the API key on AI Studio's built-in handling; never hard-code it.

Persistence: store the wardrobe and saved outfits in IndexedDB. Undo/redo with Cmd/Ctrl+Z and on-screen buttons.

Export: PNG of the canvas (transparent or stone background) and of the photoreal render.

Mobile: the wardrobe becomes a bottom sheet and the layers panel a drawer, with large touch targets. Accessibility: every control keyboard-reachable, ARIA labels on canvas items, and visible focus outlines.
```

## Noir Wardrobe (was: Character dress-up website, black background, standing avatar in center — 3 versions)
**What changes:**
- One polished build replaces three rough versions: a black stage, a lit standing avatar in the center, and wardrobe rails around it.
- AI-generated clothing items in a consistent art style, so new pieces always match the avatar.
- Avatar customization (body type, skin tone, hair, face) with layered rendering and no clipping.
- Saved looks, random outfit, undo, and a shareable PNG "lookbook card".

**How to compare:**
1. "Give my character a cyberpunk streetwear outfit." Winning: new matching items show up in the wardrobe and on the avatar in the same art style. A chat assistant returns one image you cannot edit.
2. Mix 5 items, swap the hair, then undo three times. Winning: instant, correct layering and reliable undo.
3. Save three looks and export one as a card. Winning: the looks reload after refresh, and the card looks good enough to post.

**Paste into AI Studio Build:**
```
Rebuild this app as "Noir Wardrobe", a character dress-up website with a pure black stage and a standing avatar in the center.

Visual direction: theatrical and minimal. True black background (#000000), a soft spotlight glow behind the avatar, warm white text (#F2EFE9) and a champagne-gold accent (#C8A96A). Use Playfair Display for the title and DM Sans for the interface. Subtle motion only: items fade and slide in over 150ms. Respect prefers-reduced-motion.

Layout:
- Center: a full-height standing avatar on a faint reflective floor line.
- Left rail: category icons (Hair, Tops, Bottoms, Dresses, Outerwear, Shoes, Accessories, Background).
- Right rail: item grid for the selected category, with selected items outlined in gold.
- Top bar: Looks (saved), Randomize, Undo, Redo, Export.
- Avatar tab: body type, skin tone (wide inclusive range), hair style and color, eye color.

Rendering: build the avatar and items as layered transparent PNGs or SVGs on the same canvas size and anchor points, with a fixed z-order (body, bottoms, tops, outerwear, shoes, accessories, hair front). Ship a starter set of at least 6 items per category.

AI: "Design an item" box. The user describes a piece ("cropped holographic bomber"); use the newest Gemini Pro model in AI Studio to return structured JSON against a schema {name, category, colors[], style tags[], imagePrompt}, then the newest Gemini image model to generate it in the same flat illustration style as the starter set, as a transparent item that fits the avatar template. Also offer "Style me" where the user types a theme and the reasoning model picks a full outfit from existing items, returned as JSON item IDs. Show a shimmer placeholder while generating, and an error toast with Retry (automatic retry with backoff first).

Keep the API key on AI Studio's built-in handling; never hard-code it.

Persistence: save the avatar, generated items and looks in IndexedDB; restore the last look on load. Empty state on Looks: "No saved looks yet. Press S to save this one."

Export: PNG of the avatar alone (transparent) or a 1080x1350 lookbook card with the look name.

Keyboard: arrow keys move through items, Enter to wear, S to save, Cmd/Ctrl+Z to undo. Mobile: the avatar stays centered, and the rails become a bottom tab bar plus a swipeable item tray. All controls have ARIA labels and visible focus states.
```

## Concrete Studio Planner (was: "Interior design tool: visualize a one-bedroom concrete studio")
**What changes:**
- A real top-down floor plan editor with dimensions, rather than a single generated picture.
- Furniture snaps to walls, shows clearances, and warns about blocked walkways or doors.
- Photoreal renders of the room in the chosen style that match the layout you built.
- A budget and shopping list as structured data, plus version snapshots for comparing layouts.

**How to compare:**
1. "Plan a 38 m² concrete studio for one person who works from home." Winning: a dimensioned plan with zones (sleep, work, kitchen, lounge) and clearance checks. A chat assistant gives a description or one image that does not match any plan.
2. Move the bed to the window wall and re-render. Winning: the render follows the new layout.
3. Ask for a version under $3,000. Winning: an itemized list that adds up, with swaps that keep the style.

**Paste into AI Studio Build:**
```
Rebuild this app as "Concrete Studio Planner", a tool for designing and visualizing a one-bedroom concrete studio apartment.

Visual direction: architectural and calm. Warm concrete grey background (#D9D6D0), near-black text (#1C1C1C), a terracotta accent (#B4562F), blueprint-thin lines. Use Archivo for headings and JetBrains Mono for dimensions and numbers. Use a visible 8px spacing grid, square corners and no gradients.

Screens:
1. Setup: room size (width x length, m or ft toggle), ceiling height, window and door positions, occupant needs (work from home, guests, pets) and budget. Offer three starter templates.
2. Plan editor: a top-down SVG floor plan with a grid, wall dimensions and a furniture library (bed, sofa, desk, dining table, kitchen run, wardrobe, rug, plants, lighting). Drag, rotate (R), duplicate (D), delete (Backspace), with snap-to-wall and live clearance shading. Show warnings when a walkway is under 80cm or a door swing is blocked.
3. Visualize: choose a style (Brutalist warm, Japandi, Industrial loft, Mid-century) and a camera view (entry, window, corner), then render.
4. Budget: an itemized list with price ranges and totals.

AI: use the newest Gemini Pro model in AI Studio for reasoning and the newest Gemini image model for image generation and editing. "Auto-layout" sends room data and needs to the reasoning model and gets back JSON against a schema: {furniture[{type, x, y, width, depth, rotation}], zones[], rationale}. Place it on the plan so the user can edit it. Stream the rationale text. For renders, send a top-down plan snapshot plus a structured description of every item and its position so the image matches the layout. Support targeted edits ("swap the rug for jute") by image editing. Budget output is JSON {items[{name, category, priceLow, priceHigh}], total}. Retry with backoff on errors, then show an error card with Retry and keep the plan untouched.

Keep the API key on AI Studio's built-in handling; never hard-code it.

Persistence: autosave projects in IndexedDB; named snapshots ("Layout A", "Layout B") with a side-by-side compare. Undo/redo for every plan change.

Export: plan as PNG and SVG, renders as PNG, and a PDF board with plan, renders and budget.

Empty states for no furniture and no renders. Mobile: the plan supports pinch-zoom, and the library becomes a bottom sheet. Accessibility: furniture can be selected and moved with the keyboard, and all controls are labelled.
```

## Gambit Collage (was: "Chess background collage from uploaded photos")
**What changes:**
- A real chessboard layout engine: 8x8 (or custom) grid with each photo cropped into a square, alternating light and dark treatment for an actual board pattern.
- Smart cropping centers faces and subjects, and photos can be swapped or re-cropped per square.
- Optional chess piece overlays and AI-matched color grading so mixed photos look like one piece.
- Exports at wallpaper sizes (desktop, phone, 4K, print) instead of one fixed image.

**How to compare:**
1. Upload 20 mixed phone photos and make a chess wallpaper. Winning: a crisp board where faces are not cut off and the light/dark pattern reads clearly. A chat assistant gives either code or one generated image that does not use your real photos.
2. Swap two squares and recrop one. Winning: instant, precise, and undoable.
3. Export a 1170x2532 phone wallpaper and a 3840x2160 desktop one. Winning: correct sizes, sharp output, and the board stays centered.

**Paste into AI Studio Build:**
```
Rebuild this app as "Gambit Collage", a tool that turns uploaded photos into a chessboard-patterned background or wallpaper.

Visual direction: classic club elegance. Deep walnut background (#2B1D14), ivory text (#F4EBDD), brass accent (#B08D57). Use Libre Caslon for headings and Inter for the interface. Square tiles, thin brass dividers, no gradients except a subtle vignette option on the output.

Flow:
1. Upload: drag and drop or tap to add 1-64 photos. Show thumbnails with count. Empty state: a faded chessboard with "Add photos to fill the board." Reject non-images with a clear message. Downscale very large files in the browser.
2. Board: an 8x8 grid preview (options: 4x4, 6x6, 8x8, or custom). Light squares and dark squares get different treatments, chosen from presets: tint (ivory vs walnut), black-and-white vs color, or brightness. If there are fewer photos than squares, offer repeat, solid squares, or a mixed fill.
3. Edit: click a square to recrop (pan and zoom), replace, or clear it. Drag one square onto another to swap. Options for gap width, border, rank/file labels (a-h, 1-8), and chess piece overlays in the starting position.
4. Export: presets for phone (1170x2532), desktop (2560x1440), 4K (3840x2160), square (2048x2048) and print (A3 at 300dpi), rendered on an offscreen canvas as PNG or JPG.

AI: use the newest Gemini Pro model in AI Studio to look at each photo and return structured JSON against a schema: {focalPoint {x, y}, dominantColors[], brightness, suggestedSquare: "light" | "dark"}. Use the focal point for smart cropping, and "Auto-arrange" to place brighter photos on light squares and darker ones on dark squares. Optional "Harmonize" uses the newest Gemini image model to color-grade all photos to a shared look (sepia, film, monochrome). Show per-photo progress, retry with backoff on errors, and fall back to center cropping if analysis fails so the app still works.

Keep the API key on AI Studio's built-in handling; never hard-code it.

Persistence: save the current board and photos in IndexedDB so a refresh does not lose work. Undo/redo for every change (Cmd/Ctrl+Z).

Mobile: the board fits the screen width, tap a square to open an edit sheet. Accessibility: squares are keyboard-focusable (arrow keys to move, Enter to edit), and all controls are labelled.
```

## Gallery Wall (was: "Drag-and-drop artwork portfolio website (upload artwork by tapping anywhere)")
**What changes:**
- Tap or drop anywhere still works, and now it builds a real portfolio: a masonry wall with drag reordering, series grouping and a full-screen viewer.
- AI writes titles, descriptions, medium guesses and alt text as structured data that the artist can edit.
- A public "presentation mode" that looks like a gallery website, plus a separate edit mode.
- Export as a static website ZIP or a PDF portfolio, with backup and restore.

**How to compare:**
1. Drop 15 artworks onto the page. Winning: each one uploads in place with a progress state, and gets a draft title, medium and alt text within seconds. A chat assistant cannot give you a working, persistent portfolio.
2. Group them into two series and reorder by dragging. Winning: smooth, keyboard-accessible reordering that survives a refresh.
3. Export the portfolio. Winning: a downloadable site that works offline and a clean PDF you can send to a gallery.

**Paste into AI Studio Build:**
```
Rebuild this app as "Gallery Wall", a portfolio website builder for artists where you upload artwork by tapping or dropping anywhere on the page.

Visual direction: white-cube gallery. Off-white walls (#FAFAF7), charcoal text (#222222), one vermilion accent (#D9432B) used sparingly. Use Fraunces for the artist name and titles, and Inter for the interface. Wide margins, artworks floating with soft shadows, captions in small caps like gallery wall labels.

Modes:
- Edit mode: tapping any empty area or dropping files anywhere opens upload (a full-page drop overlay appears while dragging). Each new piece appears in place with a progress ring. Artworks sit in a masonry grid. Drag to reorder (with keyboard support: select, then arrow keys). Group into Series with collapsible headers.
- Presentation mode: a clean public portfolio with the artist name, a short bio, series sections and a full-screen lightbox (arrow keys, swipe, Esc to close, captions below).
- Toggle between modes with a button and the E key.

Empty state: a large, quiet prompt "Tap anywhere or drop your work here" with supported formats (JPG, PNG, WebP, HEIC converted in the browser).

AI: use the newest Gemini Pro model in AI Studio for reasoning. For each upload, return structured JSON against a schema: {title, medium, styleTags[], description (2 sentences), altText, dominantColors[], suggestedSeries}. Fill these into an editable caption card and mark AI text as "draft" until the artist confirms it. "Write my bio" streams a short artist statement from the artist's notes. Use the newest Gemini image model only for optional mockups ("show this piece framed on a wall"). Retry with backoff on errors; if analysis fails, the artwork still uploads with blank fields and a Retry link.

Keep the API key on AI Studio's built-in handling; never hard-code it.

Persistence: store images and metadata in IndexedDB, autosave, and offer "Back up" (download JSON plus images ZIP) and "Restore". Undo/redo for upload, delete, reorder and edits (Cmd/Ctrl+Z), with an undo toast after delete.

Export: a static website ZIP (index.html with the images) and a PDF portfolio with one work per page.

Mobile: single-column layout, a floating Add button in addition to tap-anywhere, and swipe in the lightbox. Accessibility: alt text on every image, focus rings, labelled controls and WCAG AA contrast.
```
