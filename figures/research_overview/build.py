#!/usr/bin/env python3
"""Research overview figure organised by the two directions
(causality for ML, ML for causality) and the three properties.

Pictures and icons are taken from the previous figure, so the look carries over.
Needs PyMuPDF and the macOS Times New Roman fonts.  Run:  python build.py
Writes research_overview.pdf here and static/images/research_overview.png for the site.
Citation numbers are typed by hand: keep them in step with data/publications.yml.
"""
from pathlib import Path
import pymupdf

HERE = Path(__file__).resolve().parent
SRC = HERE / "previous_figure.pdf"          # pictures and icons are read from the earlier figure
FD = Path("/System/Library/Fonts/Supplemental")
FILES = {"r": FD / "Times New Roman.ttf", "b": FD / "Times New Roman Bold.ttf",
         "i": FD / "Times New Roman Italic.ttf", "bi": FD / "Times New Roman Bold Italic.ttf"}
FONT = {k: pymupdf.Font(fontfile=str(v)) for k, v in FILES.items()}

BLACK, BLUE, GRAY = (0, 0, 0), (0.008, 0.004, 1.0), (0.498, 0.498, 0.498)
GREEN, PANEL, PINK = (0.851, 0.949, 0.816), (0.792, 0.933, 0.984), (0.949, 0.812, 0.933)
YELLOW, LIGHT = (1.0, 0.753, 0.0), (0.949, 0.949, 0.949)
W, H = 1020.78, 452.0

src = pymupdf.open(SRC)
IMG_BOX = {i["xref"]: pymupdf.Rect(i["bbox"]) for i in src[0].get_image_info(xrefs=True)}
doc = pymupdf.open()
page = doc.new_page(width=W, height=H)
for k, f in FILES.items():
    page.insert_font(fontname=k, fontfile=str(f))


def tw(text, font, size):
    return FONT[font].text_length(text, fontsize=size)


def put(x, y, text, font="r", size=15.9, color=BLACK):
    page.insert_text((x, y), text, fontname=font, fontsize=size, color=color)
    return x + tw(text, font, size)


def runs(x, y, parts, size=15.9):
    """parts: (text, font, color) tuples written one after another."""
    for text, font, color in parts:
        x = put(x, y, text, font, size, color)
    return x


def cited(x, y, text, nums, size=15.9):
    return runs(x, y, [(text + " [", "r", BLACK), (nums, "r", BLUE), ("]", "r", BLACK)], size)


def box(rect, fill, opacity=0.502, stroke=None, width=1.0, radius=0.1):
    sh = page.new_shape()
    sh.draw_rect(pymupdf.Rect(rect), radius=radius)
    sh.finish(fill=fill, color=stroke, width=width, fill_opacity=opacity)
    sh.commit()


def img(xref, x, y, scale=1.0):
    """Insert an original picture (with its transparency mask) at (x, y), scaled from its old size."""
    w, h = IMG_BOX[xref].width * scale, IMG_BOX[xref].height * scale
    pix = pymupdf.Pixmap(src, xref)
    if pix.colorspace is not None and pix.colorspace.n > 3:
        pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
    sm = src.xref_get_key(xref, "SMask")
    if sm[0] == "xref":
        pix = pymupdf.Pixmap(pix, pymupdf.Pixmap(src, int(sm[1].split()[0])))
    page.insert_image(pymupdf.Rect(x, y, x + w, y + h), pixmap=pix)
    return pymupdf.Rect(x, y, x + w, y + h)


def block_arrow(x, yc, w=19.0, h=20.0):
    """Outlined right-pointing block arrow, as in the previous figure."""
    t, head = h * 0.28, w * 0.5
    pts = [(x, yc - t), (x + w - head, yc - t), (x + w - head, yc - h / 2), (x + w, yc),
           (x + w - head, yc + h / 2), (x + w - head, yc + t), (x, yc + t), (x, yc - t)]
    sh = page.new_shape()
    sh.draw_polyline(pts)
    sh.finish(fill=LIGHT, color=GRAY, width=1.2)
    sh.commit()


def dashed(points, arrow=True):
    sh = page.new_shape()
    sh.draw_polyline([pymupdf.Point(p) for p in points])
    sh.finish(color=GRAY, width=1.5, dashes="[6 4.5] 0", closePath=False)
    if arrow:
        (x0, y0), (x1, y1) = points[-2], points[-1]
        dx, dy = (1, 0) if x1 > x0 else ((0, 1) if y1 > y0 else (0, -1))
        px, py = -dy, dx
        tip = (x1, y1)
        a = (x1 - 7 * dx + 4 * px, y1 - 7 * dy + 4 * py)
        b = (x1 - 7 * dx - 4 * px, y1 - 7 * dy - 4 * py)
        sh.draw_polyline([tip, a, b, tip])
        sh.finish(fill=GRAY, color=GRAY, width=0.5)
    sh.commit()


def underline(x0, x1, y):
    sh = page.new_shape()
    sh.draw_line((x0, y + 2.2), (x1, y + 2.2))
    sh.finish(color=BLACK, width=1.3)
    sh.commit()


# Pictures of the previous figure, by xref.
ICON = {"T": 8, "I": 13, "C": 16}
ICON_CAUSAL, ICON_GLOBE, ICON_SCI = 153, 143, 140
PIC_GENERALIZE, PIC_TREE, PIC_CYCLE, PIC_ROBOT = 164, 167, 170, 176
PIC_MODAL = (181, 184, 187)

X0, X1, XP1 = 238.6, 640.9, 1019.9          # green rows and blue panel
ROWS = {"T": (30.0, 124.0), "I": (131.6, 203.6), "C": (211.2, 283.2)}
TOP, BOTTOM = ROWS["T"][0], ROWS["C"][1]

# ---- band I: header, rows, panel -----------------------------------------------------
x = put(X0 + 2, 21.5, "I. Causality for Machine Learning", "b", 17.0)
put(x + 10, 21.5, "causal principles for models that go beyond prediction", "i", 12.0)

box((X1 - 2.4, TOP, XP1, BOTTOM), PANEL, radius=0.03)
TITLE = {"T": ("Transferability", "what carries over under change?"),
         "I": ("Interpretability", "what are the mechanisms?"),
         "C": ("Controllability", "what if a factor changes?")}
BULLETS = {
    "T": [("Adaptation across domains", "7"),
          ("Extrapolation [12] and composition", "21-23"),
          ("Exploration for missing evidence", "23,27")],
    "I": [("Concept learning theory", "10,13"),
          ("Understanding foundation models", "9,16,19,20")],
    "C": [("Controllable generation", "8,11,20,24"),
          ("Multimodal concept steering", "17")],
}
for k, (y0, y1) in ROWS.items():
    box((X0, y0, X1, y1), GREEN, radius=0.08 if k != "T" else 0.06)
    img(ICON[k], X0 + 6, y0 + 5.5, 0.72)
    title, question = TITLE[k]
    base = y0 + 21.0
    xt = X0 + 31
    xe = put(xt, base, title, "b", 17.0)
    underline(xt, xe, base)
    put(xe + 10, base, question, "i", 12.0)
    for n, (text, nums) in enumerate(BULLETS[k]):
        yb = base + 19.0 * (n + 1)
        put(X0 + 22, yb, "•", "r", 15.9)
        if "[12]" in text:
            a, b = text.split("[12]")
            xx = runs(X0 + 38, yb, [(a + "[", "r", BLACK), ("12", "r", BLUE), ("]" + b + " [", "r", BLACK),
                                    (nums, "r", BLUE), ("]", "r", BLACK)])
        else:
            cited(X0 + 38, yb, text, nums)
    block_arrow(605.0, (y0 + y1) / 2)

# panel pictures and application lists
img(PIC_GENERALIZE, 668.0, 34.0, 0.60)
# propose / verify / collect loop: cycle icon, three labels, robot photo
img(PIC_CYCLE, 648.0, 92.5, 0.9)
for n, lab in enumerate(("Propose", "Verify", "Collect")):
    put(668.0 + (37.0 - tw(lab, "r", 10.5)) / 2, 91.0 + 11.5 * n, lab, "r", 10.5)
img(PIC_ROBOT, 709.0, 81.5, 0.86)
img(PIC_TREE, 645.0, 138.5, 0.88)
ox, oy = IMG_BOX[181].x0, IMG_BOX[187].y0
for xr in PIC_MODAL:
    img(xr, 650.0 + IMG_BOX[xr].x0 - ox, 221.0 + IMG_BOX[xr].y0 - oy)
XT = 760.0
PANEL_LINES = {
    "T": [("- Domain adaptation", "", ""),
          ("- Compositional image generation", "", ""),
          ("- Robot world models (", "2× sample efficiency", ")"),
          ("- RL for LLM reasoning", "", "")],
    "I": [("- Interpreting foundation models", "", ""),
          ("- Vision-language alignment", "", ""),
          ("- Sparse-autoencoder features", "", "")],
    "C": [("- Concept steering & editing", "", ""),
          ("- Text & image generation", "", ""),
          ("- Image translation", "", "")],
}
for k, lines in PANEL_LINES.items():
    y0, y1 = ROWS[k]
    pitch = 16.6
    first = (y0 + y1) / 2 - pitch * (len(lines) - 1) / 2 + 4.6
    for n, (a, note, b) in enumerate(lines):
        yy = first + pitch * n
        xx = put(XT, yy, a, "r", 14.0)
        if note:
            xx = put(xx, yy, note, "i", 12.0)
            put(xx, yy, b, "r", 14.0)

# ---- strip: from principles to practice -----------------------------------------------
SY0, SY1 = BOTTOM + 8.0, BOTTOM + 31.0
box((X0 + 0.5, SY0, XP1 - 0.5, SY1), LIGHT, opacity=1.0, stroke=GRAY, width=1.0, radius=0.17)
parts = [("In practice:", "b", BLACK), (" mechanism-guided synthetic data for K2 [", "r", BLACK), ("28", "r", BLUE),
         ("]  ·  agent evaluation [", "r", BLACK), ("25,26", "r", BLUE),
         ("]  ·  multimodal world models", "r", BLACK)]
total = sum(tw(t, f, 14.0) for t, f, _ in parts)
runs((X0 + XP1) / 2 - total / 2, SY0 + 16.3, parts, 14.0)

# ---- left box: the two directions ------------------------------------------------------
PX0, PX1 = 16.7, 212.0
box((PX0, TOP + 14.6, PX1, BOTTOM - 14.4), PINK, radius=0.06)
cx = (PX0 + PX1) / 2
t = "Beyond Prediction"
put(cx - tw(t, "bi", 15.0) / 2, TOP + 44, t, "bi", 15.0)
t = "Causality"
xw = tw(t, "b", 17.0) + 6 + 24
img(ICON_CAUSAL, cx - xw / 2, TOP + 66, 0.83)
put(cx - xw / 2 + 30, TOP + 84, t, "b", 17.0)
t = "Machine Learning"
put(cx - tw(t, "b", 17.0) / 2, TOP + 178, t, "b", 17.0)
# two arrows between them: I goes down (causality -> ML), II goes up (ML -> causality)
for xa, up, lab, side in ((cx - 22, False, "I", -1), (cx + 22, True, "II", 1)):
    ya, yb = TOP + 98, TOP + 156
    sh = page.new_shape()
    sh.draw_line((xa, ya + (8 if up else 0)), (xa, yb - (0 if up else 8)))
    sh.finish(color=GRAY, width=3.0)
    tip = (xa, ya) if up else (xa, yb)
    d = 1 if up else -1
    sh.draw_polyline([tip, (xa - 6.5, tip[1] + 10 * d), (xa + 6.5, tip[1] + 10 * d), tip])
    sh.finish(fill=GRAY, color=GRAY, width=0.5)
    sh.commit()
    lw = tw(lab, "b", 14.0)
    put(xa + (side * 12) - (lw if side < 0 else 0), (ya + yb) / 2 + 5, lab, "b", 14.0)
t = "transferable · interpretable · controllable"
put(cx - tw(t, "i", 10.5) / 2, TOP + 205, t, "i", 10.5)

# connectors: left box -> the three rows, and down to band II
xs, xm = PX1 + 0.1, 224.7
ymid = (ROWS["I"][0] + ROWS["I"][1]) / 2
for k in "TIC":
    yt = ROWS[k][0] + 15.0
    if k == "I":
        dashed([(xs, yt), (X0 - 1.3, yt)])
    else:
        dashed([(xs, ROWS["I"][0] + 15.0), (xm, ROWS["I"][0] + 15.0), (xm, yt), (X0 - 1.3, yt)])

# ---- band II: machine learning for causality -------------------------------------------
BY = SY1 + 24.0
x = put(146.4, BY, "II. Machine Learning for Causality", "b", 17.0)
put(x + 10, BY, "scalable learning for causal discovery and inference", "i", 12.0)
B1 = (146.4, BY + 12, 443.8, BY + 44.3)
B2 = (146.4, BY + 60, 443.8, BY + 92.3)
for (bx, title) in ((B1, "Structure in Scientific Data"), (B2, "Mechanism Discovery for Science")):
    box(bx, YELLOW, opacity=0.2, radius=0.2)
    box(bx, None, opacity=1.0, stroke=BLACK, width=1.5, radius=0.2)
    put(bx[0] + 9, bx[1] + 22.5, title, "b", 18.1)
img(ICON_GLOBE, 96.0, B1[1] - 1, 0.95)
img(ICON_SCI, 92.0, B2[1] - 4, 0.95)
xtr = 66.8
dashed([(xtr, BOTTOM - 17.4), (xtr, B1[1] + 16), (90.0, B1[1] + 16)])
dashed([(xtr, B1[1] + 16), (xtr, B2[1] + 16), (88.0, B2[1] + 16)])
dashed([(295.0, B1[3] + 1), (295.0, B2[1] - 1)])
LISTS = [(B1, [("Latent hierarchies in psychometric data", "10"),
               ("Mechanisms in multimodal biomedical data", "15")]),
         (B2, [("Law discovery through experiment design (e.g., physics)", ""),
               ("Predicting interventions (e.g., gene perturbations)", ""),
               ("Principled black-box causal inference", "")])]
for bx, items in LISTS:
    mid = (bx[1] + bx[3]) / 2
    first = mid - 16.6 * (len(items) - 1) / 2 + 4.6
    sh = page.new_shape()                     # bracket
    xb = 452.0
    ya, yb = first - 12, first + 16.6 * (len(items) - 1) + 5
    sh.draw_polyline([(xb + 12, ya), (xb + 6, ya), (xb + 6, yb), (xb + 12, yb)])
    sh.draw_line((xb, mid), (xb + 6, mid))
    sh.finish(color=GRAY, width=1.2, closePath=False)
    sh.commit()
    for n, (text, nums) in enumerate(items):
        if nums:
            cited(470.0, first + 16.6 * n, text, nums, 14.0)
        else:
            put(470.0, first + 16.6 * n, text, "r", 14.0)

doc.save(HERE / "research_overview.pdf", garbage=3, deflate=True)
PNG = HERE.parent.parent / "static/images/research_overview.png"
zoom = 2411 / W
pix = doc[0].get_pixmap(matrix=pymupdf.Matrix(zoom, zoom), alpha=False)
pix.save(PNG)
print("ok", pix.width, pix.height, PNG)
