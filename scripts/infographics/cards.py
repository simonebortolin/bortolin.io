"""1200x630 social preview cards: publication date, title and byline."""
import os
import re

import svglib as L

WIDTH, HEIGHT, PAD = 1200, 630, 72
MONTHS_IT = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio",
             "agosto", "settembre", "ottobre", "novembre", "dicembre"]


def read_post(path):
    """Returns (title, date) from a post's frontmatter."""
    frontmatter = open(path, encoding="utf-8").read().split("---", 2)[1]

    def field(key):
        match = re.search(rf"^{key}:\s*(.+)$", frontmatter, re.M)
        return match.group(1).strip().strip("'\"") if match else ""

    return field("title"), field("date")


def list_posts(posts_dir):
    """Yields (slug, markdown path) for every post: folder/index.md or a single .md file."""
    for name in sorted(os.listdir(posts_dir)):
        path = os.path.join(posts_dir, name)
        if os.path.isdir(path) and os.path.exists(os.path.join(path, "index.md")):
            yield name, os.path.join(path, "index.md")
        elif name.endswith(".md"):
            yield name[:-3], path


def card_svg(title, date):
    canvas = L.Canvas()
    year, month, day = date.split("-")
    when = f"{int(day)} {MONTHS_IT[int(month) - 1]} {year}"
    canvas.rect(0, 0, 10, HEIGHT, L.GREEN)
    canvas.text(PAD, 104, when.upper(), 20, L.GREEN, spacing=2)

    # Largest size that fits the title in at most four lines and 330 px.
    width = WIDTH - 2 * PAD
    for size in (84, 76, 68, 62, 56, 50, 44):
        lines = L.wrap_words(title, L.columns_for(size, width))
        if len(lines) <= 4 and len(lines) * size * 1.2 <= 330:
            break
    line_height = size * 1.2
    block = (len(lines) - 1) * line_height + size * 0.92
    top, bottom = 140, HEIGHT - 130
    y = top + (bottom - top - block) / 2 + size * 0.92
    for line in lines:
        canvas.text(PAD, y, line, size, L.WHITE, bold=True)
        y += line_height

    canvas.rule(HEIGHT - 104, PAD, width)
    canvas.text(PAD, HEIGHT - 58, "Simone Bortolin", 24, L.SUBTLE)
    canvas.text(WIDTH - PAD, HEIGHT - 58, "bortolin.io", 28, L.WHITE, bold=True, anchor="end")
    return canvas.svg(WIDTH, HEIGHT, title)
