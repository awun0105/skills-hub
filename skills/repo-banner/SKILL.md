---
name: repo-banner
description: Create a polished header banner image for a repository README (big project name, small tagline, real screenshots / code / shapes on the right), built as an HTML file and rendered to PNG with headless Chrome. Use when the user asks for a README banner, header or hero image, a cover or social-preview image for a repo, or "an image with the project name at the top of the README".
---

# Repo banner

Builds a wide README header like this: the project name huge on the left (one word in an accent colour), a short rule, a small spaced-out uppercase tagline, and on the right a visual made of the project's **real** artefacts — screenshots fanned like cards, a terminal + code snippet, or soft shapes. The banner is an HTML page (kept in the repo so it can be edited later) rendered to PNG by headless Chrome. No npm packages needed.

Files in this skill:
- `template.html` — the layout, colours as CSS variables, three visual variants (A screenshots, B terminal + code, C shapes).
- `render.sh` — `render.sh banner.html banner.png [width=1600] [height=500] [scale=1.5]`; finds Chrome / Chromium (or `CHROME_PATH`).

## Steps

1. **Get the words.** Project name (as the user wants it written — they may want spaces or a different case than the repo slug) and a tagline of 3–6 words. If the user didn't give a tagline, take it from the README's first sentence or the package description and confirm it in your reply.
2. **Pick the look from the project itself** (this is what makes it look designed, not generic):
   - If the repo has a design system — CSS variables, a Tailwind config, a theme file, a logo, an existing site or templates — reuse its **fonts and colours**.
   - Otherwise pick a mood that fits the project and one font pairing from Google Fonts, e.g. editorial serif (Cormorant Garamond / Fraunces / Instrument Serif + Work Sans), technical (Space Grotesk / JetBrains Mono), friendly (Bricolage Grotesque / Syne + DM Sans), bold (Archivo Black / Bebas Neue + Inter Tight).
   - **One** accent colour for the highlighted word, a second for the short rule, a warm or cool near-black (or a light paper colour) for the background. Check the tagline is readable (contrast ≥ 4.5:1).
   - Avoid the generic AI look: no purple-to-blue gradient, no plain Inter on white, no stock icons or emoji as the visual.
3. **Pick the visual (right side)** — real content beats decoration:
   - **A. Screenshots** — apps, websites, UI kits, templates, dashboards: 3–4 screenshots that look different from each other (colours, layouts), fanned with small rotations (−7° … +5°), overlapping. Take them yourself with headless Chrome if the repo has none (`render.sh page.html shot.png 1920 1080 1`).
   - **B. Terminal + code** — CLIs, libraries, SDKs: the real install / run command with its output, and a real 2–4 line usage snippet from the README. Keep lines short (≤ 38 characters) so nothing is cut off.
   - **C. Shapes** — only when there is nothing to show; overlapping circles in the palette.
4. **Build it.** Copy `template.html` to `assets/banner.html` in the target repo (create `assets/` if needed; follow the repo's own convention if it has a `docs/` or `.github/` images folder). Fill in fonts, `:root` colours, title (`<h1>name <em>accent</em></h1>` — put the most meaningful word in `<em>`), tagline, and keep **one** visual variant, deleting the others. Image paths are relative to the HTML file. If the name is long, lower the `h1` font-size until it fits in about half the width.
5. **Render:** `~/.agents/skills/repo-banner/render.sh assets/banner.html assets/banner.png` (defaults 1600×500 at 1.5× → 2400×750 px, sharp on retina screens).
6. **Look at the PNG** (open / read the image) and fix before showing it to the user:
   - nothing touches or crosses the edges (cards often clip at the top or bottom — shrink them or move them in);
   - the title doesn't run into the visual; the text block and the visual feel balanced;
   - web fonts actually loaded (a Georgia / Times fallback means the font link is wrong);
   - file size under about 1.5 MB (lower the scale to 1.25, or use fewer / smaller screenshots).
   Re-render after each change.
7. **Put it in the README**, at the very top:
   ```html
   <p align="center"><img src="./assets/banner.png" alt="<name> — <tagline>" /></p>
   ```
   If the README has a language switch or badges, put them centred right under the banner. Mention in your reply how to re-render it: edit `assets/banner.html`, then run the render command.

## Variations

- **GitHub social preview** (the image shown when the repo link is shared): render a second file at 1280×640 (`render.sh assets/banner.html assets/social.png 1280 640 1` after setting `--W: 1280px; --H: 640px;` in a copy). Tell the user to upload it in the repo's Settings → Social preview; it can't be set from git.
- **Light version:** swap the background to a paper colour (`--bg-*` around `#F4F0E6`), ink to near-black, drop the grain or keep it at `.05` with a dark dot.
- **No web fonts allowed / offline:** use system stacks (`Georgia`, `ui-monospace`) and remove the `<link>`.

## Troubleshooting

| Problem | Fix |
|---|---|
| `Chrome/Chromium not found` | Install Chrome or set `CHROME_PATH=/path/to/chrome` |
| Fonts fall back to Times / Arial | The Google Fonts `<link>` family name or weights don't match the CSS; check spelling and that the weight is in the URL |
| Screenshot images missing | Paths in `src` are relative to the banner HTML file, not to the repo root |
| Blank or partial PNG | Something slow to load: raise `--virtual-time-budget` in `render.sh` |
| Image blurry on GitHub | Render at scale 1.5 or 2; GitHub scales it down to the column width |
