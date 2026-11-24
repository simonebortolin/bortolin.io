# Infographics and social cards

Generates the blog's infographics and the 1200×630 preview cards used for
link previews on social networks.

## What it produces

| Output | Where | Used for |
|---|---|---|
| Infographic, SVG | `docs/public/post/<slug>/<name>.svg` | shown in the article |
| Infographic, PNG (1600 px) | `docs/public/post/<slug>/<name>.png` | sharing; the SVG in the article links to it |
| Preview card, PNG (1200×630) | `docs/public/og/<slug>.png` | `og:image` / `twitter:image` |

These files are **generated, not committed**: `docs/public/post/` and
`docs/public/og/` are in `.gitignore`, and the deploy workflow
(`.github/workflows/vitepress.yml`) runs `npm run infographics` before
`vitepress build`. Only the data in `pages/` and the scripts live in git.

In an article, reference an infographic by its absolute public path, linked
to its PNG:

```md
[![Alt text describing the data](/post/<slug>/<name>.svg)](/post/<slug>/<name>.png)
```

The site picks up `docs/public/og/<slug>.png` automatically for every post that
does not set `image` in its frontmatter (see `transformHead` in
`docs/.vitepress/config.mts`).

## Requirements

- Python 3.10+ with the packages in `requirements.txt`:
  `pip install -r scripts/infographics/requirements.txt`
- Node.js with Playwright and its Chromium, used to render SVG to PNG; the
  workflow pins the version:
  `npm install --no-save playwright@1.63.0 && npx playwright install chromium`

## Usage

For a local preview with the images, generate them first, then start VitePress:

```sh
npm run infographics && npm run docs:dev
```

Run from the repository root:

```sh
python3 scripts/infographics/build.py all                     # everything
python3 scripts/infographics/build.py infographics            # all infographics
python3 scripts/infographics/build.py infographics usb-c-mestieri
python3 scripts/infographics/build.py cards                   # all cards
python3 scripts/infographics/build.py cards 2026-10-25-php-nel-2026-php2shell
```

New posts get their preview card automatically at the next deploy.

## Adding an infographic

Infographics are defined in `pages/`, one module per article. Each module sets
`POST` (the post slug) and either:

- `INFOGRAPHICS`: terminal-style infographics, a list of dicts with `name`,
  `title`, `subtitle`, `blocks` and `sources`. A block is a caption and a
  terminal session: lines starting with `$ ` are commands, `[[...]]` marks a
  highlight and `{{...}}` an annotation that is not command output.
- `CUSTOM`: infographics with their own layout, a list of dicts with `name`
  and a `build()` function returning the SVG source (see `pages/usb_c.py`).

Then add the module to `PAGE_MODULES` in `build.py`.

The text of the infographics is in Italian, like the blog. Terminal
infographics must only show real output of the commands they display: keep
the data that produced them, or the command, reproducible.

## How it works

- `svglib.py` draws text, rectangles and highlights. Every text run has a
  fixed `textLength` and the font is embedded as a WOFF2 subset holding only
  the glyphs in use, so the result does not depend on the reader's fonts.
- `cards.py` reads title and date from each post's frontmatter.
- `render.cjs` renders each SVG in an `<img>` with Chromium and saves a PNG;
  `build.py` then reduces it to a 256-colour palette.

## Font

[Cascadia Mono](https://github.com/microsoft/cascadia-code) by Microsoft,
release 2407.24, under the SIL Open Font License 1.1 (`fonts/OFL.txt`). The
embedded subsets keep the font's copyright and licence name records, and each
SVG carries the notice in a comment.

## Related

`scripts/kernel-cves/cve_open.py` produces the kernel CVE counts shown in the
`ont-cve-rami` infographic, from the kernel's
[vulns.git](https://git.kernel.org/pub/scm/linux/security/vulns.git) records.
