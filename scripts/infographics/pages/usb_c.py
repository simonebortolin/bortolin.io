"""Custom-layout infographic for the USB-C article.

Data checked on 22 November 2026 against usb.org (USB 3.2, USB4 and USB
Charger pages) and the text of Directive (EU) 2022/2380 on EUR-Lex.
Text is in Italian, like the article.
"""
import math

import svglib as L

POST = "2021-01-20-la-rivoluzione-dell-usb-c"

TITLE = "USB-C: un connettore, tanti mestieri."
SUBTITLE = ("La forma è sempre la stessa. Quello che passa dal cavo dipende dalla "
            "specifica supportata da porta, dispositivo e cavo.")

# (label, note, value, unit)
DATA_RATES = [
    ("USB 3.2 Gen 1", "1 linea", 5, "Gbps"),
    ("USB 3.2 Gen 2", "1 linea", 10, "Gbps"),
    ("USB 3.2 Gen 2×2", "2 linee da 10 Gbps", 20, "Gbps"),
    ("USB4", "con cavi certificati 80 Gbps", 80, "Gbps"),
]
POWER = [
    ("USB PD fino al 2021", "20 V × 5 A", 100, "W"),
    ("USB PD 3.1", "annunciata nel 2021", 240, "W"),
]
ALT_MODES = ["DisplayPort", "Thunderbolt", "più monitor in cascata (MST)"]
EU_DEADLINES = [
    ("28 dicembre 2024", "Telefoni, tablet, fotocamere, cuffie, console portatili, altoparlanti "
                         "portatili, e-reader, tastiere, mouse, navigatori portatili, auricolari."),
    ("28 aprile 2026", "Laptop."),
]
SOURCES = ["Dati: usb.org (USB 3.2, USB4, USB Charger),", "EUR-Lex, Direttiva (UE) 2022/2380."]

LABEL_WIDTH = 230
BAR_X = L.PAD + LABEL_WIDTH
BAR_MAX = L.CONTENT_WIDTH - LABEL_WIDTH - 120


def _section(canvas, y, caption):
    y += 20
    canvas.rule(y)
    y += 33
    L.draw_caption(canvas, y, caption)
    return y


def _bars(canvas, y, rows, scale):
    for label, note, value, unit in rows:
        y += 12
        canvas.text(L.PAD, y + 20, label, 15.5, L.FG, bold=True)
        if note:
            canvas.text(L.PAD, y + 40, note, 12.5, L.GREY)
        canvas.rect(BAR_X, y + 6, BAR_MAX, 20, L.TRACK, radius=4)
        width = max(6, BAR_MAX * scale(value))
        canvas.rect(BAR_X, y + 6, width, 20, L.GREEN, radius=4)
        canvas.text(BAR_X + width + 12, y + 22, f"{value:g} {unit}".replace(".", ","), 17, L.WHITE, bold=True)
        y += 46
    return y


def build():
    canvas = L.Canvas()
    y = L.draw_heading(canvas, 44, TITLE, SUBTITLE)

    y = _section(canvas, y + 6, "Dati · velocità massima") + 8
    y = _bars(canvas, y, DATA_RATES, lambda v: math.log10(v) / math.log10(80))
    canvas.text(L.PAD, y + 18, "Scala logaritmica.", 12.5, L.GREY)
    y += 24

    y = _section(canvas, y, "Energia · USB Power Delivery") + 8
    y = _bars(canvas, y, POWER, lambda v: v / 240)

    y = _section(canvas, y, "Video e altri protocolli · modalità alternative") + 18
    x = L.PAD
    for chip in ALT_MODES:
        width = len(chip) * 15 * L.ADVANCE + 24
        canvas.rect(x, y, width, 32, L.TRACK, radius=16)
        canvas.text(x + 12, y + 21, chip, 15, L.FG)
        x += width + 10
    y += 32

    y = _section(canvas, y + 6, "Caricatore unico · Direttiva (UE) 2022/2380") + 24
    timeline_x, top = L.PAD + 10, y
    for date, devices in EU_DEADLINES:
        canvas.circle(timeline_x, y + 9, 7, L.GREEN)
        canvas.text(timeline_x + 24, y + 15, date, 17, L.WHITE, bold=True)
        line_y = y + 22
        for line in L.wrap_words(devices, L.columns_for(14.5, L.CONTENT_WIDTH - 34)):
            line_y += 21
            canvas.text(timeline_x + 24, line_y, line, 14.5, L.FG)
        y = line_y + 22
    canvas.rect(timeline_x - 1, top + 16, 2, y - top - 60, L.GREEN, opacity=0.5)

    height = L.draw_footer(canvas, y + 6, SOURCES)
    return canvas.svg(L.WIDTH, height, TITLE)


CUSTOM = [dict(name="usb-c-mestieri", build=build)]
