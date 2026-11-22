#!/usr/bin/env python3
"""Builds the blog's infographics and social preview cards.

    python3 scripts/infographics/build.py infographics [name ...]
    python3 scripts/infographics/build.py cards [slug ...]
    python3 scripts/infographics/build.py all

Outputs (generated files, not committed; the site build creates them):
  docs/public/post/<slug>/<name>.svg    infographic shown in the article
  docs/public/post/<slug>/<name>.png    1600 px PNG of it, for sharing
  docs/public/og/<slug>.png             1200x630 card used as og:image

PNGs are rendered with Playwright (render.cjs) and reduced to a 256-colour
palette, which keeps them sharp at a third of the size.
"""
import argparse
import importlib
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
POSTS = os.path.join(ROOT, "docs", "post")
PUBLIC = os.path.join(ROOT, "docs", "public")
sys.path.insert(0, HERE)

import cards  # noqa: E402
import svglib  # noqa: E402

PAGE_MODULES = ["ont", "php2shell", "nextjs", "usb_c"]


def collect_infographics():
    """Returns {name: (post slug, function returning the SVG source)}."""
    found = {}
    for module_name in PAGE_MODULES:
        module = importlib.import_module(f"pages.{module_name}")
        for spec in getattr(module, "INFOGRAPHICS", []):
            build = (lambda s=spec: svglib.terminal_infographic(
                s["title"], s["subtitle"], s["blocks"], s["sources"]))
            found[spec["name"]] = (module.POST, build)
        for spec in getattr(module, "CUSTOM", []):
            found[spec["name"]] = (module.POST, spec["build"])
    return found


def render_png(jobs, css_width, scale):
    """jobs: list of (svg path, png path)."""
    if not jobs:
        return
    args = [str(css_width), str(scale)] + [p for job in jobs for p in job]
    subprocess.run(["node", os.path.join(HERE, "render.cjs"), *args], check=True)
    from PIL import Image
    for _, png in jobs:
        image = Image.open(png).convert("RGB")
        image.quantize(colors=256, method=Image.Quantize.MEDIANCUT,
                       dither=Image.Dither.NONE).save(png, optimize=True)


def build_infographics(names):
    available = collect_infographics()
    unknown = set(names) - set(available)
    if unknown:
        sys.exit(f"Unknown infographics: {', '.join(sorted(unknown))}. "
                 f"Available: {', '.join(sorted(available))}")
    jobs = []
    for name in names or sorted(available):
        slug, build = available[name]
        out_dir = os.path.join(PUBLIC, "post", slug)
        os.makedirs(out_dir, exist_ok=True)
        svg_path = os.path.join(out_dir, f"{name}.svg")
        with open(svg_path, "w", encoding="utf-8") as f:
            f.write(build())
        jobs.append((svg_path, os.path.join(out_dir, f"{name}.png")))
        print(f"infographic  post/{slug}/{name}.svg")
    render_png(jobs, 800, 2)


def build_cards(slugs):
    posts = dict(cards.list_posts(POSTS))
    unknown = set(slugs) - set(posts)
    if unknown:
        sys.exit(f"Unknown posts: {', '.join(sorted(unknown))}")
    out_dir = os.path.join(PUBLIC, "og")
    os.makedirs(out_dir, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        jobs = []
        for slug in slugs or sorted(posts):
            title, date = cards.read_post(posts[slug])
            if not title or not date:
                print(f"skipped      {slug}: missing title or date in the frontmatter")
                continue
            svg_path = os.path.join(tmp, f"{len(jobs)}.svg")
            with open(svg_path, "w", encoding="utf-8") as f:
                f.write(cards.card_svg(title, date))
            jobs.append((svg_path, os.path.join(out_dir, f"{slug}.png")))
            print(f"card         og/{slug}.png")
        render_png(jobs, cards.WIDTH, 1)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("target", choices=["infographics", "cards", "all"])
    parser.add_argument("names", nargs="*", help="infographic names or post slugs (default: all)")
    args = parser.parse_args()
    if args.target in ("infographics", "all"):
        build_infographics(args.names if args.target == "infographics" else [])
    if args.target in ("cards", "all"):
        build_cards(args.names if args.target == "cards" else [])


if __name__ == "__main__":
    main()
