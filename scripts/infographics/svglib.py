"""Shared building blocks for the blog's SVG infographics and social cards.

Every piece of text is drawn with Cascadia Mono, embedded in the SVG as a
WOFF2 subset that only holds the glyphs in use, and every text run gets a
fixed `textLength`. Layout and highlights therefore look the same whatever
fonts the reader has installed.
"""
import base64
import html
import io
import os
import re

from fontTools import subset
from fontTools.ttLib import TTFont

FONT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")
FONT_REGULAR = os.path.join(FONT_DIR, "CascadiaMono-Regular.ttf")
FONT_BOLD = os.path.join(FONT_DIR, "CascadiaMono-Bold.ttf")
ADVANCE = 1200 / 2048  # Cascadia Mono glyph advance, in em

WIDTH, PAD = 800, 40
CONTENT_WIDTH = WIDTH - 2 * PAD

# Colours: dark terminal background, the site's dark-theme green for
# highlights and captions, blue for annotations that are not command output.
BG = "#0b0d10"
FG = "#c9d1d9"
WHITE = "#ffffff"
GREY = "#7d8792"
SUBTLE = "#9aa4ae"
RULE = "#2a3038"
GREEN = "#3a9657"
BLUE = "#58a6ff"
TRACK = "#1a1f26"

FONT_NOTICE = ("Font: Cascadia Mono, Copyright (c) 2019 - Present, Microsoft Corporation, "
               "SIL Open Font License 1.1 (https://scripts.sil.org/OFL)")


def escape(text):
    return html.escape(text, quote=False)


def wrap_words(text, columns):
    """Greedy word wrap to at most `columns` characters per line."""
    lines, current = [], ""
    for word in text.split(" "):
        if current and len(current) + 1 + len(word) > columns:
            lines.append(current)
            current = word
        else:
            current = f"{current} {word}" if current else word
    lines.append(current)
    return lines


def columns_for(size, width=CONTENT_WIDTH):
    return int(width // (size * ADVANCE))


class Canvas:
    """Collects SVG elements and the set of characters that need glyphs."""

    def __init__(self):
        self.items = []
        self.chars = set()

    def text(self, x, y, s, size, fill, bold=False, anchor="start", spacing=0.0):
        if not s.strip():
            return
        self.chars.update(s)
        length = len(s) * (size * ADVANCE + spacing) - (spacing if spacing else 0)
        weight = ' font-weight="700"' if bold else ""
        anchor_attr = f' text-anchor="{anchor}"' if anchor != "start" else ""
        self.items.append(
            f'<text x="{x:.2f}" y="{y:.2f}" font-size="{size}" fill="{fill}"{weight}{anchor_attr} '
            f'textLength="{length:.2f}" lengthAdjust="spacingAndGlyphs">{escape(s)}</text>')

    def rect(self, x, y, w, h, fill, radius=0, opacity=None):
        r = f' rx="{radius}"' if radius else ""
        o = f' opacity="{opacity}"' if opacity is not None else ""
        self.items.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}"{r} fill="{fill}"{o}/>')

    def circle(self, x, y, r, fill):
        self.items.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r}" fill="{fill}"/>')

    def rule(self, y, x=PAD, width=CONTENT_WIDTH):
        self.rect(x, y, width, 1, RULE)

    def svg(self, width, height, title):
        """Wraps the collected elements in a standalone SVG document."""
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height:.0f}" '
                f'width="{width}" height="{height:.0f}" role="img" aria-label="{html.escape(title)}" '
                f'xml:space="preserve"><!-- {FONT_NOTICE} --><title>{escape(title)}</title>'
                f'<style>{embedded_style(self.chars)}</style>'
                f'<rect width="100%" height="100%" fill="{BG}"/>' + "".join(self.items) + "</svg>")


def _font_face(chars, path, weight):
    font = TTFont(path)
    options = subset.Options()
    options.flavor = "woff2"
    options.layout_features = []
    # Keep the copyright notice, the licence and its URL, as the OFL requires.
    options.name_IDs = [0, 13, 14]
    options.notdef_outline = True
    subsetter = subset.Subsetter(options)
    subsetter.populate(text="".join(sorted(chars)))
    subsetter.subset(font)
    buffer = io.BytesIO()
    font.flavor = "woff2"
    font.save(buffer)
    data = base64.b64encode(buffer.getvalue()).decode()
    return (f"@font-face{{font-family:'BMono';font-weight:{weight};"
            f"src:url(data:font/woff2;base64,{data}) format('woff2')}}")


def embedded_style(chars):
    return (_font_face(chars, FONT_REGULAR, 400) + _font_face(chars, FONT_BOLD, 700)
            + "text{font-family:'BMono','Cascadia Mono',Consolas,Menlo,monospace;white-space:pre}")


def draw_heading(canvas, y, title, subtitle):
    """Title and subtitle at the top of an infographic; returns the new y."""
    for line in wrap_words(title, columns_for(40)):
        y += 40 * 0.92
        canvas.text(PAD, y, line, 40, WHITE, bold=True)
        y += 49 - 40 * 0.92
    y += 14
    for line in wrap_words(subtitle, columns_for(19)):
        y += 19 * 0.95
        canvas.text(PAD, y, line, 19, SUBTLE)
        y += 27.5 - 19 * 0.95
    return y


def draw_caption(canvas, y, text):
    canvas.text(PAD, y, text.upper(), 13, GREEN, spacing=1.5)


def draw_footer(canvas, y, sources):
    """Source lines on the left, site and author on the right; returns the page height."""
    canvas.rule(y)
    y += 18
    footer_y = y
    for line in sources:
        footer_y += 14 * 0.95 + 4
        canvas.text(PAD, footer_y, line, 14, GREY)
        footer_y += 22 - 14 * 0.95 - 4
    canvas.text(WIDTH - PAD, y + 26, "bortolin.io", 18, WHITE, bold=True, anchor="end")
    canvas.text(WIDTH - PAD, y + 50, "Simone Bortolin", 14, GREY, anchor="end")
    return max(footer_y, y + 56) + 30


# --- Terminal infographics -------------------------------------------------
#
# A block is a caption and the text of a terminal session. Lines starting
# with "$ " (or indented by six spaces, for continuations) are commands.
# In output lines, [[...]] marks a highlight and {{...}} an annotation that
# is not part of the output.

def _parse_line(line):
    if line.startswith("$ ") or line.startswith("      "):
        return [(line, "command")]
    segments, position = [], 0
    for match in re.finditer(r"\[\[(.+?)\]\]|\{\{(.+?)\}\}", line):
        if match.start() > position:
            segments.append((line[position:match.start()], "plain"))
        if match.group(1) is not None:
            segments.append((match.group(1), "highlight"))
        else:
            segments.append((match.group(2), "note"))
        position = match.end()
    if position < len(line):
        segments.append((line[position:], "plain"))
    return segments


def _wrap_segments(segments, columns):
    """Hard-wraps every `columns` characters, like CSS `word-break: break-all`."""
    lines, current, used = [], [], 0
    for text, kind in segments:
        while text:
            part, text = text[:columns - used], text[columns - used:]
            current.append((part, kind))
            used += len(part)
            if used >= columns and text:
                lines.append(current)
                current, used = [], 0
    lines.append(current)
    return lines


def terminal_infographic(title, subtitle, blocks, sources):
    """Builds a terminal-style infographic and returns the SVG source."""
    canvas = Canvas()
    y = draw_heading(canvas, 44, title, subtitle)
    size, line_height = 15.5, 24
    advance = size * ADVANCE
    columns = columns_for(size)
    colours = {"command": GREY, "note": BLUE, "plain": FG}
    for caption, session in blocks:
        y += 26
        canvas.rule(y)
        y += 33
        draw_caption(canvas, y, caption)
        y += 14
        for raw in session.split("\n"):
            for segments in _wrap_segments(_parse_line(raw), columns):
                baseline, column = y + 17.5, 0
                for part, kind in segments:
                    x = PAD + column * advance
                    if kind == "highlight":
                        canvas.rect(x - 3, y + 1, len(part) * advance + 6, line_height - 2, GREEN)
                        canvas.text(x, baseline, part, size, BG, bold=True)
                    else:
                        canvas.text(x, baseline, part, size, colours[kind])
                    column += len(part)
                y += line_height
    height = draw_footer(canvas, y + 30, sources)
    return canvas.svg(WIDTH, height, title)
