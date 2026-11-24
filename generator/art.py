"""SVG cover illustrations (1080x1350), navy + gold palette."""
GOLD = "#D9AE57"
RED = "#C8102E"; GREEN = "#00843D"; BLACK = "#111"; WHITE = "#fff"


def svg(body, extra_defs=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1080 1350" width="1080" height="1350">
<defs>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2c4660"/><stop offset=".55" stop-color="#1d2e42"/><stop offset="1" stop-color="#121c29"/></linearGradient>
<radialGradient id="sun" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#f3d28b" stop-opacity=".9"/><stop offset=".4" stop-color="{GOLD}" stop-opacity=".35"/><stop offset="1" stop-color="{GOLD}" stop-opacity="0"/></radialGradient>
{extra_defs}
</defs>
<rect width="1080" height="1350" fill="url(#sky)"/>
{body}
</svg>'''


def skyline(y=820, seed=1, color="#0f1824", h=1.0):
    import random
    r = random.Random(seed)
    x = -20; parts = []
    while x < 1100:
        w = r.randint(40, 95); th = int(r.randint(120, 430) * h)
        parts.append(f'<rect x="{x}" y="{y-th}" width="{w}" height="{1350-y+th}" fill="{color}"/>')
        # windows
        for wy in range(y - th + 20, y, 34):
            for wx in range(x + 10, x + w - 10, 18):
                if r.random() < .22:
                    parts.append(f'<rect x="{wx}" y="{wy}" width="7" height="12" fill="{GOLD}" opacity=".35"/>')
        x += w + r.randint(4, 14)
    return "".join(parts)


def flag_uae(x, y, w, wave=False):
    h = w / 2
    return (f'<g transform="translate({x},{y})">'
            f'<rect width="{w}" height="{h/3}" fill="{GREEN}" x="0"/>'
            f'<rect y="{h/3}" width="{w}" height="{h/3}" fill="{WHITE}"/>'
            f'<rect y="{2*h/3}" width="{w}" height="{h/3}" fill="{BLACK}"/>'
            f'<rect width="{w/4}" height="{h}" fill="{RED}"/></g>')


def emirate_flag(kind, w):
    """Return inner svg markup for an emirate flag of width w (ratio 2:1)."""
    h = w / 2
    if kind == "abudhabi":
        return f'<rect width="{w}" height="{h}" fill="{RED}"/><rect width="{w*0.25}" height="{h*0.25}" fill="#fff"/>'
    if kind in ("dubai", "ajman"):
        return f'<rect width="{w}" height="{h}" fill="{RED}"/><rect width="{w*0.25}" height="{h}" fill="#fff"/>'
    if kind in ("sharjah", "rak"):
        b = h * 0.25
        return f'<rect width="{w}" height="{h}" fill="#fff"/><rect x="{b}" y="{b}" width="{w-2*b}" height="{h-2*b}" fill="{RED}"/>'
    if kind == "uaq":
        cx = w * 0.55; cy = h / 2; r = h * 0.3
        return (f'<rect width="{w}" height="{h}" fill="{RED}"/><rect width="{w*0.25}" height="{h}" fill="#fff"/>'
                f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff"/><circle cx="{cx+r*0.35}" cy="{cy}" r="{r*0.85}" fill="{RED}"/>'
                f'<polygon points="{star(cx+r*1.45, cy, r*0.38)}" fill="#fff"/>')
    if kind == "fujairah":  # uses UAE flag
        return (f'<rect width="{w}" height="{h/3}" fill="{GREEN}"/><rect y="{h/3}" width="{w}" height="{h/3}" fill="#fff"/>'
                f'<rect y="{2*h/3}" width="{w}" height="{h/3}" fill="{BLACK}"/><rect width="{w/4}" height="{h}" fill="{RED}"/>')
    raise ValueError(kind)


def star(cx, cy, r):
    import math
    pts = []
    for i in range(10):
        a = -math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.42
        pts.append(f"{cx+rr*math.cos(a):.1f},{cy+rr*math.sin(a):.1f}")
    return " ".join(pts)


def cover(kind):
    if kind == "history":
        dots = "".join(f'<circle cx="{170+i*123}" cy="560" r="16" fill="{GOLD}"/>' for i in range(7))
        return svg(f'''<circle cx="540" cy="420" r="420" fill="url(#sun)"/>
<text x="540" y="470" text-anchor="middle" font-family="Playfair Display" font-weight="700" font-size="330" fill="none" stroke="{GOLD}" stroke-width="3" opacity=".55">1971</text>
<line x1="170" y1="560" x2="908" y2="560" stroke="{GOLD}" stroke-width="3" opacity=".6"/>{dots}
<path d="M0 760 Q 270 720 540 760 T 1080 760 V1350 H0Z" fill="#0f1824" opacity=".8"/>''')
    if kind == "rehistory":
        return svg(f'''<circle cx="800" cy="330" r="330" fill="url(#sun)"/>
{skyline(1000, seed=7, color="#14202f", h=1.4)}{skyline(1080, seed=3, color="#0c141e", h=1.0)}
<polyline points="80,900 260,760 420,820 600,560 760,640 980,300" fill="none" stroke="{GOLD}" stroke-width="10" stroke-linejoin="round" stroke-linecap="round"/>
<circle cx="980" cy="300" r="20" fill="{GOLD}"/>''')
    if kind == "metro":
        return svg(f'''<g fill="none" stroke-width="26" stroke-linecap="round" stroke-linejoin="round">
<path d="M-40 260 L380 260 Q470 260 520 330 L760 660 Q810 730 900 730 L1120 730" stroke="#E21836"/>
<path d="M-40 540 L300 540 Q380 540 430 470 L560 300 Q610 230 700 230 L1120 230" stroke="#4CA64C"/>
<path d="M200 -40 L200 120 Q200 200 280 230 L960 470 Q1040 500 1040 580 L1040 900" stroke="#2E7FD9"/>
<path d="M-40 840 L240 840 Q320 840 370 780 L620 470 Q670 410 750 410 L1120 410" stroke="{GOLD}"/>
</g>
<g fill="#fff" stroke="#16212e" stroke-width="8">
<circle cx="520" cy="330" r="22"/><circle cx="640" cy="495" r="22"/><circle cx="430" cy="470" r="22"/><circle cx="560" cy="300" r="22"/><circle cx="280" cy="230" r="22"/><circle cx="960" cy="470" r="22"/><circle cx="620" cy="470" r="22"/><circle cx="750" cy="410" r="22"/><circle cx="370" cy="780" r="22"/><circle cx="900" cy="730" r="22"/><circle cx="700" cy="230" r="22"/><circle cx="1040" cy="580" r="22"/>
</g>''')
    if kind == "rail":
        rails = "".join(f'<line x1="{540-25-i*95}" y1="{620+i*120}" x2="{540+25+i*95}" y2="{620+i*120}" stroke="#3a4a5c" stroke-width="{6+i*3}"/>' for i in range(7))
        return svg(f'''<circle cx="540" cy="560" r="380" fill="url(#sun)"/>
<path d="M0 640 Q 300 600 540 620 T 1080 640 V1350 H0Z" fill="#162333"/>
<path d="M0 700 L 260 610 L 400 640 L 520 600 L 700 650 L 860 610 L1080 680 V720 H0Z" fill="#1b2a3b"/>
{rails}
<line x1="515" y1="620" x2="-60" y2="1400" stroke="{GOLD}" stroke-width="10"/><line x1="565" y1="620" x2="1140" y2="1400" stroke="{GOLD}" stroke-width="10"/>
<g transform="translate(470,500)"><path d="M10 120 Q10 20 70 10 Q130 20 130 120Z" fill="#e9e3d4"/><rect x="25" y="45" width="90" height="34" rx="10" fill="#1d2e42"/><circle cx="40" cy="105" r="8" fill="{GOLD}"/><circle cx="100" cy="105" r="8" fill="{GOLD}"/></g>''')
    if kind == "abudhabi":
        return svg(f'''<circle cx="300" cy="380" r="300" fill="url(#sun)"/>
{skyline(900, seed=11, color="#16222f", h=1.5)}
<path d="M0 960 Q 540 900 1080 960 V1350 H0Z" fill="#0e1824"/>
<path d="M0 990 Q 540 940 1080 990" stroke="{GOLD}" stroke-width="3" fill="none" opacity=".5"/>''')
    if kind == "culture":
        rings = "".join(f'<ellipse cx="540" cy="700" rx="{460-i*44}" ry="{150-i*14}" fill="none" stroke="{GOLD}" stroke-width="2" opacity="{.25+i*.05:.2f}"/>' for i in range(8))
        cones = "".join(f'<polygon points="{x},{760} {x+w/2},{760-hh} {x+w},{760}" fill="#e7e1d3" opacity="{op}"/>' for x, w, hh, op in [(140,120,260,.55),(250,90,190,.4),(780,140,300,.55),(900,90,170,.4)])
        return svg(f'''<circle cx="540" cy="520" r="420" fill="url(#sun)"/>
<path d="M120 760 Q540 330 960 760Z" fill="#101a26"/>{rings}{cones}
<path d="M0 760 H1080 V1350 H0Z" fill="#0d1622"/>
<path d="M0 800 Q 540 770 1080 800" stroke="{GOLD}" stroke-width="3" fill="none" opacity=".4"/>''')
    if kind == "rulers":
        order = ["abudhabi", "dubai", "sharjah", "ajman", "uaq", "rak", "fujairah"]
        g = []
        for i, k in enumerate(order):
            col, row = i % 4, i // 4
            w = 200
            x = 70 + col * 245 + (122 if row == 1 else 0)
            y = 250 + row * 170
            g.append(f'<g transform="translate({x},{y})">{emirate_flag(k, w)}<rect width="{w}" height="{w/2}" fill="none" stroke="#000" stroke-opacity=".25"/></g>')
        return svg(f'<circle cx="540" cy="380" r="420" fill="url(#sun)"/>' + "".join(g))
    if kind == "national":
        return svg(f'''<circle cx="540" cy="460" r="460" fill="url(#sun)"/>
<g transform="translate(130,220) skewY(-4)">{flag_uae(0,0,820)}</g>
{sparkles()}''')
    if kind == "adgm":
        bars = "".join(f'<rect x="{110+i*112}" y="{900-hh}" width="78" height="{hh}" fill="#1a2a3c" stroke="{GOLD}" stroke-opacity=".35" stroke-width="2"/>' for i, hh in enumerate([180,240,220,320,380,360,470,560]))
        return svg(f'''<circle cx="820" cy="300" r="320" fill="url(#sun)"/>{bars}
<polyline points="150,700 262,640 374,660 486,560 598,500 710,520 822,410 934,320" fill="none" stroke="{GOLD}" stroke-width="9" stroke-linejoin="round"/>
<path d="M0 900 Q 540 860 1080 900 V1350 H0Z" fill="#0e1824"/>
<path d="M0 930 Q 540 900 1080 930" stroke="{GOLD}" stroke-width="3" fill="none" opacity=".5"/>''')
    if kind == "difc":
        return svg(f'''<circle cx="540" cy="380" r="380" fill="url(#sun)"/>
{skyline(880, seed=23, color="#16222f", h=1.3)}
<g transform="translate(390,250)"><rect x="0" y="120" width="300" height="520" fill="#0f1925" stroke="{GOLD}" stroke-width="3"/><rect x="60" y="0" width="180" height="160" fill="none" stroke="{GOLD}" stroke-width="8"/><rect x="100" y="160" width="100" height="480" fill="#0b131d"/></g>
<path d="M0 880 Q 540 840 1080 880 V1350 H0Z" fill="#0e1824"/>''')
    raise ValueError(kind)


def sparkles(n=36, seed=5):
    import random
    r = random.Random(seed); out = []
    for _ in range(n):
        x = r.randint(20, 1060); y = r.randint(40, 820)
        if 110 < x < 970 and 160 < y < 700:
            continue
        out.append(f'<circle cx="{x}" cy="{y}" r="{r.choice([3,4,6])}" fill="{GOLD}" opacity="{r.uniform(.4,.9):.2f}"/>')
    return "".join(out)
