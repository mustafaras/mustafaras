#!/usr/bin/env python3
"""Generate custom SVG artwork for the mustafaras profile README.
Deterministic (seeded) — regenerate any time with: python3 scripts/generate_assets.py
"""
import math
import os
import random

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
os.makedirs(OUT, exist_ok=True)
random.seed(42)

# ── palette ──────────────────────────────────────────────────────────────────
BG0, BG1, BG2 = "#050810", "#0B1120", "#0E1A2B"
INK, SUBTLE, FAINT = "#F1F5F9", "#94A3B8", "#64748B"
CYAN, VIOLET, EMERALD = "#22D3EE", "#A78BFA", "#34D399"
AMBER, ROSE, SKY = "#FBBF24", "#F472B6", "#38BDF8"
LINE = "#1E293B"

SERIF = "Georgia, 'Times New Roman', serif"
MONO = "ui-monospace, 'JetBrains Mono', Menlo, Consolas, monospace"


def w(name, svg):
    path = os.path.join(OUT, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"  ✓ {name}  ({os.path.getsize(path)} B)")


# ══════════════════════════════════════════════════════════════════════════════
# HERO — instrument-panel banner: grid, particle network, skyline, serif name
# ══════════════════════════════════════════════════════════════════════════════
def hero():
    W, H = 1000, 340
    p = []
    p.append(f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Mustafa Raşit Şahin — research profile banner">')
    p.append("""<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0" stop-color="#050810"/><stop offset="0.55" stop-color="#0B1120"/><stop offset="1" stop-color="#0E1A2B"/>
</linearGradient>
<linearGradient id="namegrad" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0" stop-color="#E2E8F0"/><stop offset="0.5" stop-color="#F8FAFC"/><stop offset="1" stop-color="#A5B4CF"/>
</linearGradient>
<linearGradient id="rule" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0" stop-color="#22D3EE" stop-opacity="0"/><stop offset="0.5" stop-color="#22D3EE"/><stop offset="1" stop-color="#A78BFA" stop-opacity="0"/>
</linearGradient>
<radialGradient id="glow" cx="0.5" cy="0.5" r="0.5">
  <stop offset="0" stop-color="#22D3EE" stop-opacity="0.10"/><stop offset="1" stop-color="#22D3EE" stop-opacity="0"/>
</radialGradient>
<linearGradient id="sky1" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#0D1526"/><stop offset="1" stop-color="#0A1120"/>
</linearGradient>
<linearGradient id="sky2" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#121D33"/><stop offset="1" stop-color="#0B1322"/>
</linearGradient>
<style>
  .n { animation: pulse 4.2s ease-in-out infinite; }
  .n2 { animation: pulse 5.6s ease-in-out 1.1s infinite; }
  .n3 { animation: pulse 3.4s ease-in-out 2.2s infinite; }
  .e { stroke-dasharray: 3 6; animation: flow 9s linear infinite; }
  @keyframes pulse { 0%,100% { opacity: 0.25; } 50% { opacity: 0.95; } }
  @keyframes flow { to { stroke-dashoffset: -90; } }
</style>
</defs>""")
    p.append(f'<rect width="{W}" height="{H}" fill="url(#bg)"/>')

    # faint blueprint grid
    for x in range(0, W + 1, 80):
        p.append(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}" stroke="#38BDF8" stroke-opacity="0.035" stroke-width="1"/>')
    for y in range(0, H + 1, 40):
        p.append(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="#38BDF8" stroke-opacity="0.028" stroke-width="1"/>')

    # glow behind name
    p.append(f'<ellipse cx="500" cy="150" rx="330" ry="95" fill="url(#glow)"/>')

    # particle network (upper band)
    nodes = [(random.randint(60, 940), random.randint(28, 118)) for _ in range(16)]
    edges = []
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            d = math.dist(nodes[i], nodes[j])
            if d < 185:
                edges.append((i, j))
    for i, j in edges[:22]:
        p.append(f'<line class="e" x1="{nodes[i][0]}" y1="{nodes[i][1]}" x2="{nodes[j][0]}" y2="{nodes[j][1]}" stroke="#22D3EE" stroke-opacity="0.16" stroke-width="1"/>')
    for k, (x, y) in enumerate(nodes):
        cls = "n" if k % 3 == 0 else ("n2" if k % 3 == 1 else "n3")
        c = CYAN if k % 2 == 0 else VIOLET
        p.append(f'<circle class="{cls}" cx="{x}" cy="{y}" r="{random.choice([1.8, 2.2, 2.8])}" fill="{c}"/>')

    # skyline — back layer
    x = -6
    while x < W:
        bw = random.randint(22, 46)
        bh = random.randint(26, 58)
        p.append(f'<rect x="{x}" y="{H - bh}" width="{bw}" height="{bh}" fill="url(#sky1)"/>')
        x += bw + random.randint(1, 5)
    # skyline — front layer with lit windows
    x = -10
    while x < W:
        bw = random.randint(18, 40)
        bh = random.randint(34, 92)
        top = H - bh
        p.append(f'<rect x="{x}" y="{top}" width="{bw}" height="{bh}" fill="url(#sky2)"/>')
        for wx in range(x + 4, x + bw - 4, 7):
            for wy in range(top + 6, H - 6, 10):
                r = random.random()
                if r < 0.14:
                    p.append(f'<rect x="{wx}" y="{wy}" width="2.6" height="3.6" fill="#F59E0B" fill-opacity="0.55"/>')
                elif r < 0.24:
                    p.append(f'<rect x="{wx}" y="{wy}" width="2.6" height="3.6" fill="#22D3EE" fill-opacity="0.38"/>')
        x += bw + random.randint(2, 7)

    # corner ticks (instrument frame)
    t, m = 14, 16
    for cx, cy, dx, dy in [(m, m, 1, 1), (W - m, m, -1, 1), (m, H - m, 1, -1), (W - m, H - m, -1, -1)]:
        p.append(f'<path d="M {cx} {cy + dy * t} L {cx} {cy} L {cx + dx * t} {cy}" stroke="#22D3EE" stroke-opacity="0.5" stroke-width="1.4" fill="none"/>')

    # top labels
    p.append(f'<text x="{m + 10}" y="34" font-family="{MONO}" font-size="10" letter-spacing="2.5" fill="#475569">M. R. ŞAHİN — RESEARCH PROFILE</text>')
    p.append(f'<text x="{W - m - 10}" y="34" text-anchor="end" font-family="{MONO}" font-size="10" letter-spacing="2.5" fill="#475569">ANKARA · 39.9334°N 32.8597°E</text>')

    # name + rule + taglines
    p.append(f'<text x="500" y="152" text-anchor="middle" font-family="{SERIF}" font-size="46" letter-spacing="7" fill="url(#namegrad)">Mustafa Raşit Şahin</text>')
    p.append(f'<rect x="300" y="176" width="400" height="1.4" fill="url(#rule)"/>')
    p.append(f'<text x="500" y="208" text-anchor="middle" font-family="{MONO}" font-size="15" letter-spacing="3.5" fill="#7DD3FC">URBAN MORPHOLOGY · SPATIAL COMPLEXITY · AI FOR CITIES</text>')
    p.append(f'<text x="500" y="234" text-anchor="middle" font-family="{MONO}" font-size="12" letter-spacing="1.5" fill="#64748B">PhD — City &amp; Regional Planning, METU · Instructor · Ankara</text>')

    p.append("</svg>")
    w("hero.svg", "\n".join(p))


# ══════════════════════════════════════════════════════════════════════════════
# DIVIDER — gradient hairline with center diamond
# ══════════════════════════════════════════════════════════════════════════════
def divider():
    p = [f'<svg width="1000" height="16" viewBox="0 0 1000 16" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="divider">',
         """<defs><linearGradient id="dg" x1="0" y1="0" x2="1" y2="0">
<stop offset="0" stop-color="#22D3EE" stop-opacity="0"/><stop offset="0.35" stop-color="#22D3EE"/><stop offset="0.65" stop-color="#A78BFA"/><stop offset="1" stop-color="#A78BFA" stop-opacity="0"/>
</linearGradient></defs>""",
         '<rect x="60" y="7.2" width="880" height="1.3" fill="url(#dg)"/>',
         '<rect x="496" y="2" width="8" height="8" transform="rotate(45 500 6)" fill="#22D3EE" fill-opacity="0.9"/>',
         '<circle cx="60" cy="7.8" r="1.6" fill="#22D3EE" fill-opacity="0.5"/>',
         '<circle cx="940" cy="7.8" r="1.6" fill="#A78BFA" fill-opacity="0.5"/>',
         "</svg>"]
    w("divider.svg", "\n".join(p))


# ══════════════════════════════════════════════════════════════════════════════
# PILLAR ICONS — Sierpinski / contours / neural graph (72×72)
# ══════════════════════════════════════════════════════════════════════════════
def icon_sierpinski():
    tris = []

    def rec(cx, cy, s, depth):
        if depth == 0:
            h = s * 0.8660254
            tris.append(f"M {cx:.1f} {cy:.1f} L {cx - s / 2:.1f} {cy + h:.1f} L {cx + s / 2:.1f} {cy + h:.1f} Z")
            return
        h = s * 0.8660254
        rec(cx, cy, s / 2, depth - 1)
        rec(cx - s / 4, cy + h / 2, s / 2, depth - 1)
        rec(cx + s / 4, cy + h / 2, s / 2, depth - 1)

    rec(36, 7, 56, 4)
    p = [f'<svg width="72" height="72" viewBox="0 0 72 72" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="urban complexity">',
         """<defs><linearGradient id="sg" x1="0" y1="0" x2="1" y2="1">
<stop offset="0" stop-color="#22D3EE"/><stop offset="1" stop-color="#A78BFA"/></linearGradient></defs>""",
         f'<path d="{" ".join(tris)}" fill="none" stroke="url(#sg)" stroke-width="0.9" stroke-opacity="0.9"/>',
         "</svg>"]
    w("icon-urban.svg", "\n".join(p))


def icon_contours():
    p = [f'<svg width="72" height="72" viewBox="0 0 72 72" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="spatial intelligence">']
    for k, r in enumerate([9, 15, 21, 27]):
        ph1, ph2 = k * 1.3, k * 0.7
        pts = []
        for i in range(49):
            th = i / 48 * 2 * math.pi
            rr = r * (1 + 0.16 * math.sin(3 * th + ph1) + 0.09 * math.sin(5 * th + ph2))
            pts.append(f"{36 + rr * math.cos(th):.1f},{36 + rr * math.sin(th):.1f}")
        op = 0.85 - k * 0.14
        p.append(f'<polygon points="{" ".join(pts)}" fill="none" stroke="#A78BFA" stroke-width="1.1" stroke-opacity="{op:.2f}"/>')
    p.append('<circle cx="36" cy="36" r="2.2" fill="#FBBF24"/>')
    p.append('<line x1="36" y1="4" x2="36" y2="14" stroke="#A78BFA" stroke-opacity="0.5" stroke-width="1"/>')
    p.append('<line x1="36" y1="58" x2="36" y2="68" stroke="#A78BFA" stroke-opacity="0.5" stroke-width="1"/>')
    p.append('<line x1="4" y1="36" x2="14" y2="36" stroke="#A78BFA" stroke-opacity="0.5" stroke-width="1"/>')
    p.append('<line x1="58" y1="36" x2="68" y2="36" stroke="#A78BFA" stroke-opacity="0.5" stroke-width="1"/>')
    p.append("</svg>")
    w("icon-spatial.svg", "\n".join(p))


def icon_neural():
    layers = [(14, [18, 36, 54]), (36, [12, 26, 40, 54]), (58, [22, 44])]
    p = [f'<svg width="72" height="72" viewBox="0 0 72 72" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="agentic systems">']
    for i in range(len(layers) - 1):
        x1, ys1 = layers[i]
        x2, ys2 = layers[i + 1]
        for y1 in ys1:
            for y2 in ys2:
                p.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#34D399" stroke-opacity="0.35" stroke-width="0.9"/>')
    for li, (x, ys) in enumerate(layers):
        for y in ys:
            c = EMERALD if li == 1 else CYAN
            p.append(f'<circle cx="{x}" cy="{y}" r="3.4" fill="#0B1120" stroke="{c}" stroke-width="1.6"/>')
    p.append("</svg>")
    w("icon-agentic.svg", "\n".join(p))


# ══════════════════════════════════════════════════════════════════════════════
# REPO CARDS — journal-cover thumbnails (460×150)
# ══════════════════════════════════════════════════════════════════════════════
CARDS = [
    ("card-urban-analytics.svg", "URBAN · GIS", "Synapse IDE — Urban Analytics",
     ["Tri-modal spatial intelligence platform for urban",
      "science, planning, risk and evidence-based decisions."],
     ["TypeScript", "GIS", "Spatial ML"], CYAN),
    ("card-quantum-gravity.svg", "SCIENTIFIC ATLAS", "Horizon — Quantum Gravity Atlas",
     ["Interactive quantum-gravity atlas: black-hole",
      "thermodynamics, QFT scattering, holography."],
     ["JavaScript", "WebGL", "Physics"], VIOLET),
    ("card-belief-emergence.svg", "RESEARCH", "Belief Emergence",
     ["Reproducible study of bounded nonlinear response",
      "surfaces for macro-urban belief emergence."],
     ["TypeScript", "LaTeX", "Visual Analytics"], AMBER),
    ("card-synapse-ide.svg", "PLATFORM", "Synapse IDE",
     ["Browser IDE with a streaming AI assistant and a safe",
      "apply-plan pipeline that turns model output into edits."],
     ["React", "Monaco", "LLM"], EMERALD),
    ("card-moodforge.svg", "SIMULATION", "MoodForge Advanced",
     ["Multimodal engine simulating synthetic patients with",
      "longitudinal psychological profiles and metrics."],
     ["Python", "NLP", "Psychometrics"], ROSE),
    ("card-flux2.svg", "GENERATIVE", "FLUX.2 — Architectural Studio",
     ["Generative environment for architectural and urban",
      "design exploration, iteration and form-finding."],
     ["Python", "Streamlit", "Diffusion"], SKY),
]


def card(fname, domain, name, desc_lines, chips, accent):
    W, H = 460, 150
    p = [f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{name}">']
    p.append(f'<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="10" fill="#0B1120" stroke="{LINE}"/>')
    p.append(f'<rect x="6" y="12" width="3" height="126" rx="1.5" fill="{accent}"/>')
    p.append(f'<text x="436" y="26" text-anchor="end" font-family="{MONO}" font-size="9.5" letter-spacing="2" fill="{accent}" fill-opacity="0.85">{domain}</text>')
    p.append(f'<text x="24" y="52" font-family="{SERIF}" font-size="19" font-weight="bold" fill="#F1F5F9">{name}</text>')
    for i, line in enumerate(desc_lines):
        p.append(f'<text x="24" y="{76 + i * 17}" font-family="{MONO}" font-size="11" fill="#94A3B8">{line}</text>')
    # chips
    cx = 24
    for chip in chips:
        cw = 7 * len(chip) + 16
        p.append(f'<rect x="{cx}" y="116" width="{cw}" height="19" rx="9.5" fill="#1E293B" fill-opacity="0.8" stroke="#334155"/>')
        p.append(f'<text x="{cx + cw / 2}" y="129.5" text-anchor="middle" font-family="{MONO}" font-size="9.5" fill="#CBD5E1">{chip}</text>')
        cx += cw + 8
    p.append(f'<text x="436" y="140" text-anchor="end" font-family="{MONO}" font-size="8.5" letter-spacing="1.5" fill="#475569">GITHUB ↗</text>')
    # corner tick
    p.append(f'<path d="M {W - 18} {H - 10} L {W - 10} {H - 10} L {W - 10} {H - 18}" stroke="{accent}" stroke-opacity="0.4" stroke-width="1.2" fill="none"/>')
    p.append("</svg>")
    w(fname, "\n".join(p))


# ══════════════════════════════════════════════════════════════════════════════
# FOOTER — wave, tagline, contact line
# ══════════════════════════════════════════════════════════════════════════════
def footer():
    p = ['<svg width="1000" height="150" viewBox="0 0 1000 150" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="footer">',
         """<defs>
<linearGradient id="fbg" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#0E1A2B"/><stop offset="1" stop-color="#050810"/>
</linearGradient>
<linearGradient id="fline" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0" stop-color="#22D3EE" stop-opacity="0"/><stop offset="0.5" stop-color="#22D3EE"/><stop offset="1" stop-color="#A78BFA" stop-opacity="0"/>
</linearGradient>
</defs>""",
         '<path d="M0,42 C 220,8 480,66 720,34 C 850,18 940,30 1000,24 L1000,150 L0,150 Z" fill="url(#fbg)"/>',
         '<path d="M0,42 C 220,8 480,66 720,34 C 850,18 940,30 1000,24" fill="none" stroke="url(#fline)" stroke-width="1.4"/>',
         '<text x="500" y="92" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-size="26" fill="#E2E8F0">Let&#8217;s build cities that learn.</text>',
         '<text x="500" y="122" text-anchor="middle" font-family="ui-monospace, Menlo, monospace" font-size="11.5" letter-spacing="1.5" fill="#64748B">Ankara · mustafarasit@gmail.com · ORCID 0009-0001-4809-3950</text>',
         "</svg>"]
    w("footer.svg", "\n".join(p))


if __name__ == "__main__":
    print("Generating profile assets →", OUT)
    hero()
    divider()
    icon_sierpinski()
    icon_contours()
    icon_neural()
    for c in CARDS:
        card(*c)
    footer()
    print("done.")