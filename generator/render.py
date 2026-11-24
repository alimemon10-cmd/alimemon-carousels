import base64, html, io, json, os, sys
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright
import art

HERE = Path(__file__).parent
A = HERE / "assets"
OUT = Path(sys.argv[1])  # repo root
ONLY = sys.argv[2:]  # optional folder filter


def b64(p, mime):
    return f"data:{mime};base64," + base64.b64encode(Path(p).read_bytes()).decode()


FONTS = "".join(
    f"@font-face{{font-family:'{fam}';font-weight:{w};src:url({b64(A/f'{file}-latin-{w}-normal.woff2','font/woff2')})}}"
    for fam, file, ws in [("Inter", "inter", [400, 500, 600, 700, 800, 900]), ("Playfair Display", "playfair-display", [600, 700])]
    for w in ws)
HEADSHOT = b64(A / "headshot.png", "image/png")

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;overflow:hidden;font-family:Inter;color:#fff;background:#1b2838}
.s{position:relative;width:1080px;height:1350px;overflow:hidden}
.bg{position:absolute;inset:0}
.bg svg{width:1080px;height:1350px;display:block}
.blur{opacity:.55}.blur svg{filter:blur(28px) saturate(.6);transform:scale(1.15)}
.veil{position:absolute;inset:0;background:linear-gradient(180deg,rgba(27,40,56,.80),rgba(24,36,51,.86) 50%,rgba(18,28,41,.94))}
.cveil{position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,30,44,0) 30%,rgba(18,28,41,.75) 62%,rgba(15,24,36,.97) 100%)}
.top{position:absolute;top:72px;left:80px;right:80px;display:flex;justify-content:space-between;font-size:23px;font-weight:700;letter-spacing:.5px}
.top .h{color:#D9AE57}.top .n{color:#c9d1db;font-weight:600}
.foot{position:absolute;bottom:52px;left:80px;right:80px;height:30px}
.dots{position:absolute;left:50%;transform:translateX(-50%);top:8px;display:flex;gap:11px}
.dots i{width:10px;height:10px;border-radius:50%;background:#5d6b7b;display:block}
.dots i.on{background:#D9AE57}
.swipe{position:absolute;right:0;top:0;font-size:21px;font-weight:700;letter-spacing:1px;color:#dfe5ec}
.body{position:absolute;left:80px;right:80px;top:170px}
.num{font-family:'Playfair Display';font-weight:700;color:#D9AE57;font-size:200px;line-height:1;letter-spacing:-2px}
.num.sm{font-size:150px}
.lab{margin-top:44px;color:#D9AE57;font-weight:700;font-size:27px;letter-spacing:1px;text-transform:uppercase}
h2{font-weight:800;font-size:64px;line-height:1.1;margin-top:18px;letter-spacing:-.5px}
ul{list-style:none;margin-top:30px}
li{position:relative;padding-left:48px;font-size:35px;line-height:1.38;font-weight:500;color:#eef1f5;margin-bottom:20px}
li:before{content:"";position:absolute;left:4px;top:19px;width:14px;height:14px;border-radius:50%;background:#D9AE57}
.cov{position:absolute;left:80px;right:70px;bottom:190px}
.pill{display:inline-block;background:#D9AE57;color:#1b2838;font-weight:800;font-size:27px;padding:10px 22px;border-radius:40px;letter-spacing:.5px}
h1{font-weight:900;font-size:92px;line-height:1.04;margin-top:30px;letter-spacing:-1.5px;text-shadow:0 4px 30px rgba(0,0,0,.45)}
h1 em{font-style:normal;color:#D9AE57;display:block}
.sub{margin-top:26px;font-size:35px;color:#dbe2ea;font-weight:500}
.close{position:absolute;top:135px;left:0;right:0;text-align:center}
.hs{width:480px;height:480px;border-radius:50%;border:9px solid #D9AE57;margin:0 auto;background:url(HS) center/cover}
.nm{font-family:'Playfair Display';font-weight:600;font-size:78px;margin-top:34px}
.role{color:#D9AE57;font-weight:700;font-size:25px;letter-spacing:1px;margin-top:10px}
.ct{font-size:35px;line-height:1.42;color:#eef1f5;margin:30px auto 0;width:820px;font-weight:500}
.btn{display:inline-block;margin-top:38px;background:#D9AE57;color:#1b2838;font-weight:800;font-size:40px;padding:26px 0;width:760px;border-radius:70px}
.contact{margin-top:36px;font-size:28px;color:#dfe5ec;font-weight:500}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:40px}
.card{background:rgba(255,255,255,.06);border:1px solid rgba(217,174,87,.35);border-radius:22px;padding:26px}
.card svg{display:block;border-radius:4px;box-shadow:0 6px 18px rgba(0,0,0,.35)}
.card .em{color:#D9AE57;font-weight:800;font-size:25px;letter-spacing:1px;margin-top:20px;text-transform:uppercase}
.card .rn{font-weight:700;font-size:31px;line-height:1.25;margin-top:8px}
.card .since{font-size:25px;color:#c9d1db;margin-top:8px;font-weight:500}
.chips{display:flex;flex-wrap:wrap;gap:18px;margin-top:44px}
.chip{border:2px solid #D9AE57;border-radius:50px;padding:16px 30px;font-size:33px;font-weight:700}
.bars{margin-top:44px}
.bar{margin-bottom:30px}
.bar .t{display:flex;justify-content:space-between;font-size:33px;font-weight:600}
.bar .t b{color:#D9AE57;font-weight:800}
.bar .tr{height:20px;background:rgba(255,255,255,.08);border-radius:10px;margin-top:12px}
.bar .f{height:20px;background:#D9AE57;border-radius:10px}
.cal{margin-top:44px}
.cal .r{display:flex;align-items:center;gap:30px;margin-bottom:26px;background:rgba(255,255,255,.06);border-radius:22px;padding:22px 28px}
.cal .d{width:150px;text-align:center;border-right:2px solid rgba(217,174,87,.5);padding-right:24px}
.cal .d b{display:block;font-family:'Playfair Display';color:#D9AE57;font-size:66px;line-height:1}
.cal .d span{font-size:22px;font-weight:700;letter-spacing:2px;color:#c9d1db}
.cal .x{font-size:32px;line-height:1.3;font-weight:600}
.cal .x small{display:block;font-size:26px;color:#c9d1db;font-weight:500;margin-top:4px}
.flagbig{margin-top:40px;display:flex;gap:30px;align-items:stretch}
.sw{flex:1;border-radius:18px;padding:22px 20px;font-size:27px;font-weight:700;line-height:1.3}
.sw small{display:block;font-weight:500;font-size:24px;margin-top:8px;opacity:.9}
.note{margin-top:26px;font-size:25px;color:#aab5c2;font-weight:500;line-height:1.4}
"""


def dots(i, n):
    return "".join(f'<i class="{"on" if k == i else ""}"></i>' for k in range(n))


def esc(s):
    return html.escape(s, quote=False)


def page(inner, bgsvg, i, n, cover=False, last=False):
    bg = f'<div class="bg">{bgsvg}</div>' if cover else f'<div class="bg blur">{bgsvg}</div>'
    veil = '<div class="cveil"></div>' if cover else '<div class="veil"></div>'
    swipe = "" if last else '<div class="swipe">SWIPE &rarr;</div>'
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}{CSS.replace('HS', HEADSHOT)}</style></head>
<body><div class="s">{bg}{veil}
<div class="top"><span class="h">@ALIMEMON_REALESTATE</span><span class="n">{i+1}/{n}</span></div>
{inner}
<div class="foot"><div class="dots">{dots(i,n)}</div>{swipe}</div></div></body></html>"""


def render_slide(sl):
    t = sl["t"]
    if t == "cover":
        return f'<div class="cov"><span class="pill">{esc(sl["tag"])}</span><h1>{esc(sl["title"])}<em>{esc(sl["gold"])}</em></h1><div class="sub">{esc(sl["sub"])}</div></div>'
    if t == "stat":
        cls = "num sm" if len(sl["num"]) > 5 else "num"
        lis = "".join(f"<li>{esc(b)}</li>" for b in sl["bullets"])
        return f'<div class="body"><div class="{cls}">{esc(sl["num"])}</div><div class="lab">{esc(sl["label"])}</div><h2>{esc(sl["head"])}</h2><ul>{lis}</ul></div>'
    if t == "rulers":
        cards = []
        for e in sl["items"]:
            fl = f'<svg width="200" height="100" viewBox="0 0 200 100">{art.emirate_flag(e["flag"], 200)}</svg>'
            cards.append(f'<div class="card">{fl}<div class="em">{esc(e["emirate"])}</div><div class="rn">{esc(e["name"])}</div><div class="since">{esc(e["since"])}</div></div>')
        note = f'<div class="note">{esc(sl["note"])}</div>' if sl.get("note") else ""
        return f'<div class="body" style="top:150px"><div class="lab" style="margin-top:0">{esc(sl["label"])}</div><h2>{esc(sl["head"])}</h2><div class="grid">{"".join(cards)}</div>{note}</div>'
    if t == "chips":
        ch = "".join(f'<span class="chip">{esc(c)}</span>' for c in sl["chips"])
        note = f'<div class="note">{esc(sl["note"])}</div>' if sl.get("note") else ""
        return f'<div class="body"><div class="lab" style="margin-top:0">{esc(sl["label"])}</div><h2>{esc(sl["head"])}</h2><div class="chips">{ch}</div>{note}</div>'
    if t == "bars":
        mx = max(v for _, v, _ in sl["bars"])
        bs = "".join(f'<div class="bar"><div class="t"><span>{esc(k)}</span><b>{esc(lbl)}</b></div><div class="tr"><div class="f" style="width:{v/mx*100:.1f}%"></div></div></div>' for k, v, lbl in sl["bars"])
        note = f'<div class="note">{esc(sl["note"])}</div>' if sl.get("note") else ""
        return f'<div class="body"><div class="lab" style="margin-top:0">{esc(sl["label"])}</div><h2>{esc(sl["head"])}</h2><div class="bars">{bs}</div>{note}</div>'
    if t == "cal":
        rows = "".join(f'<div class="r"><div class="d"><b>{esc(d)}</b><span>{esc(m)}</span></div><div class="x">{esc(x)}<small>{esc(s)}</small></div></div>' for d, m, x, s in sl["rows"])
        return f'<div class="body"><div class="lab" style="margin-top:0">{esc(sl["label"])}</div><h2>{esc(sl["head"])}</h2><div class="cal">{rows}</div></div>'
    if t == "flag":
        fl = f'<svg width="920" height="460" viewBox="0 0 920 460" style="display:block;margin-top:40px;border-radius:8px;box-shadow:0 10px 30px rgba(0,0,0,.4)">{art.emirate_flag("fujairah", 920)}</svg>'
        sw = "".join(f'<div class="sw" style="background:{bg};color:{fg}">{esc(n)}<small>{esc(m)}</small></div>' for bg, fg, n, m in sl["swatches"])
        note = f'<div class="note">{esc(sl["note"])}</div>' if sl.get("note") else ""
        return f'<div class="body" style="top:150px"><div class="lab" style="margin-top:0">{esc(sl["label"])}</div><h2>{esc(sl["head"])}</h2>{fl}<div class="flagbig">{sw}</div>{note}</div>'
    if t == "list":
        lis = "".join(f"<li>{esc(b)}</li>" for b in sl["bullets"])
        return f'<div class="body"><div class="lab" style="margin-top:0">{esc(sl["label"])}</div><h2>{esc(sl["head"])}</h2><ul style="margin-top:40px">{lis}</ul></div>'
    if t == "close":
        return f'''<div class="close"><div class="hs"></div><div class="nm">Ali Memon</div><div class="role">LUXURY PROPERTY CONSULTANT &middot; DUBAI</div>
<div class="ct">{esc(sl["text"])}</div><div class="btn">{esc(sl["btn"])}</div><div class="contact">+971 56 387 0124 &nbsp;&middot;&nbsp; alimemonrealestate.com</div></div>'''
    raise ValueError(t)


def main():
    days = json.loads((HERE / "content.json").read_text())
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        for d in days:
            if ONLY and d["folder"] not in ONLY:
                continue
            folder = OUT / d["folder"]; folder.mkdir(exist_ok=True)
            bgsvg = art.cover(d["art"])
            n = len(d["slides"]); imgs = []
            for i, sl in enumerate(d["slides"]):
                htm = page(render_slide(sl), bgsvg, i, n, cover=sl["t"] == "cover", last=i == n - 1)
                pg.set_content(htm); pg.wait_for_timeout(150)
                png = pg.screenshot(type="png")
                im = Image.open(io.BytesIO(png)).convert("RGB")
                im.save(folder / f"{i+1:02d}.jpg", quality=90, optimize=True)
                imgs.append(im)
            imgs[0].save(folder / "carousel.pdf", save_all=True, append_images=imgs[1:], resolution=150)
            print(d["folder"], n)
        b.close()


if __name__ == "__main__":
    main()
