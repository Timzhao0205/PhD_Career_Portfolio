#!/usr/bin/env python3
"""
md2html.py -- regenerate the reader-friendly HTML mirrors of the plan docs.

Each tracked markdown report gets a self-contained .html next to it
(sidebar table of contents, styled tables, dark-mode aware, printable),
plus a small reports_index.html at the research-folder root linking all
of them. Run from anywhere:

    pip install markdown          # one-time
    python3 tools/md2html.py

Re-run whenever one of the tracked .md files changes. To track a new
report, add it to DOCS below. The HTML is a MIRROR -- the markdown stays
the source of truth; never edit the .html by hand.
"""

import datetime
import html as html_mod
import os
import sys

try:
    import markdown
except ImportError:
    sys.exit("python-markdown missing -- run: pip install markdown")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (relative md path, short label used in nav, one-line description)
DOCS = [
    ("02_HSX_Hall_Sensor_Readout/docs/hsx_readout_bringup_and_calibration_plan.md",
     "Summer research plan",
     "Bring-up, verification & calibration of the spinning-current readout — the week-by-week summer plan (HSX install Aug 2026)."),
    ("02_HSX_Hall_Sensor_Readout/docs/second_test_setup_static_bias.md",
     "Second test setup",
     "Static DC bias p2 → p4, sense p1/p3 through the amp, Pico-ADC readout — scope-free health checks and raw-offset surveys."),
    ("03_HSX_Vector_Probe_RSI2026/docs/rsi_experiment_and_publication_plan.md",
     "RSI preparation",
     "Vector Hall probe, second HSX campaign, and the Review of Scientific Instruments paper plan (~Mar 2027)."),
    ("02_HSX_Hall_Sensor_Readout/journal/2026-07-08_spinning_emulator_20mA.md",
     "Journal 2026-07-08",
     "First dynamic spinning run on the emulator (20 kHz, 20 mA): offset cancellation works; absolute-magnitude anomaly open; plan comparison."),
]

INDEX = "reports_index.html"

CSS = """
:root{
  --bg:#f7f8fa; --panel:#ffffff; --ink:#1c2430; --muted:#5b6673;
  --accent:#1a56a7; --accent-soft:#e8f0fb; --border:#dde3ea;
  --code-bg:#f0f2f5; --th-bg:#eef2f7; --mark:#fff3c4;
}
@media (prefers-color-scheme: dark){
  :root{
    --bg:#12161c; --panel:#1a2029; --ink:#dfe6ee; --muted:#9aa7b5;
    --accent:#7db3f0; --accent-soft:#1f2c3f; --border:#2c3542;
    --code-bg:#232b36; --th-bg:#212936; --mark:#4a3f1a;
  }
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);
  font:16px/1.65 "Charter","Georgia","Times New Roman",serif}
.layout{display:flex;max-width:1240px;margin:0 auto;gap:0}
nav.side{position:sticky;top:0;align-self:flex-start;flex:0 0 290px;
  height:100vh;overflow-y:auto;padding:26px 20px 40px 24px;
  border-right:1px solid var(--border);
  font-family:"Avenir Next","Segoe UI",system-ui,sans-serif;font-size:13.5px}
nav.side .brand{font-weight:700;font-size:12px;letter-spacing:.14em;
  text-transform:uppercase;color:var(--muted);margin-bottom:4px}
nav.side .doctitle{font-weight:700;font-size:15px;line-height:1.35;
  color:var(--ink);margin-bottom:14px}
nav.side .siblings{margin:0 0 16px;padding:10px 12px;background:var(--accent-soft);
  border-radius:8px}
nav.side .siblings b{display:block;font-size:11px;letter-spacing:.1em;
  text-transform:uppercase;color:var(--muted);margin-bottom:6px}
nav.side .siblings a{display:block;padding:2px 0;color:var(--accent);
  text-decoration:none}
nav.side .siblings a.current{color:var(--ink);font-weight:700;cursor:default}
nav.side .toc-head{font-size:11px;letter-spacing:.1em;text-transform:uppercase;
  color:var(--muted);margin:14px 0 6px}
nav.side ul{list-style:none;margin:0;padding:0}
nav.side li a{display:block;padding:3px 8px;border-left:2px solid transparent;
  color:var(--muted);text-decoration:none;border-radius:0 6px 6px 0}
nav.side li a:hover{color:var(--accent);background:var(--accent-soft)}
nav.side li.lvl3 a{padding-left:22px;font-size:12.5px}
main{flex:1;min-width:0;padding:34px 44px 90px;background:var(--panel)}
main .meta{font-family:"Avenir Next","Segoe UI",system-ui,sans-serif;
  font-size:12.5px;color:var(--muted);border-bottom:1px solid var(--border);
  padding-bottom:10px;margin-bottom:6px}
h1,h2,h3,h4{font-family:"Avenir Next","Segoe UI",system-ui,sans-serif;
  line-height:1.25;scroll-margin-top:16px}
h1{font-size:29px;margin:14px 0 10px}
h2{font-size:21px;margin:40px 0 10px;padding-top:14px;
  border-top:1px solid var(--border)}
h3{font-size:17px;margin:28px 0 8px;color:var(--accent)}
a{color:var(--accent)}
p{margin:10px 0}
li{margin:4px 0}
strong{color:var(--ink)}
hr{border:none;border-top:1px solid var(--border);margin:30px 0}
code{font-family:"SF Mono","Cascadia Code",Consolas,monospace;
  font-size:.86em;background:var(--code-bg);padding:.12em .38em;
  border-radius:4px}
pre{background:var(--code-bg);border:1px solid var(--border);
  border-radius:8px;padding:14px 16px;overflow-x:auto;line-height:1.5}
pre code{background:none;padding:0;font-size:13px}
.tablewrap{overflow-x:auto;margin:14px 0;border:1px solid var(--border);
  border-radius:8px}
table{border-collapse:collapse;width:100%;
  font-family:"Avenir Next","Segoe UI",system-ui,sans-serif;font-size:13.5px}
th{background:var(--th-bg);text-align:left;font-weight:700}
th,td{padding:7px 12px;border-bottom:1px solid var(--border);
  vertical-align:top}
tr:last-child td{border-bottom:none}
tbody tr:nth-child(even){background:color-mix(in srgb,var(--th-bg) 45%,transparent)}
blockquote{margin:14px 0;padding:8px 18px;border-left:3px solid var(--accent);
  background:var(--accent-soft);border-radius:0 8px 8px 0;color:var(--muted)}
.backtop{position:fixed;right:22px;bottom:22px;
  font-family:system-ui,sans-serif;font-size:13px;text-decoration:none;
  background:var(--accent);color:#fff;padding:8px 12px;border-radius:20px;
  opacity:.85}
.backtop:hover{opacity:1}
@media (max-width:900px){
  .layout{flex-direction:column}
  nav.side{position:static;height:auto;flex:none;border-right:none;
    border-bottom:1px solid var(--border)}
  main{padding:24px 20px 70px}
}
@media print{
  nav.side,.backtop{display:none}
  main{padding:0}
  body{background:#fff;color:#000}
}
"""


def build_page(md_rel, label, all_docs):
    src = os.path.join(ROOT, md_rel)
    with open(src, encoding="utf-8") as fh:
        text = fh.read()

    md = markdown.Markdown(extensions=["tables", "fenced_code", "toc",
                                       "sane_lists"],
                           extension_configs={"toc": {"toc_depth": "2-3"}})
    body = md.convert(text)
    # wrap tables for horizontal scroll on narrow screens
    body = body.replace("<table>", '<div class="tablewrap"><table>')
    body = body.replace("</table>", "</table></div>")

    # sidebar TOC from the parsed heading tokens
    def clean(name):
        # toc token names arrive pre-escaped; unescape first to avoid &amp;amp;
        return html_mod.escape(html_mod.unescape(name))

    items = []
    for tok in md.toc_tokens:
        items.append('<li class="lvl2"><a href="#{id}">{name}</a></li>'
                     .format(id=tok["id"], name=clean(tok["name"])))
        for sub in tok.get("children", []):
            items.append('<li class="lvl3"><a href="#{id}">{name}</a></li>'
                         .format(id=sub["id"], name=clean(sub["name"])))
    toc_html = "<ul>{}</ul>".format("".join(items)) if items else ""

    here = os.path.dirname(md_rel)
    links = ['<a href="{}">Report index</a>'.format(
        html_mod.escape(os.path.relpath(INDEX, here)))]
    for other_rel, other_label, _ in all_docs:
        target = os.path.relpath(other_rel[:-3] + ".html", here)
        if other_rel == md_rel:
            links.append('<a class="current">{} (this doc)</a>'
                         .format(html_mod.escape(other_label)))
        else:
            links.append('<a href="{}">{}</a>'.format(
                html_mod.escape(target), html_mod.escape(other_label)))

    title = md_rel.rsplit("/", 1)[-1][:-3].replace("_", " ")
    for line in text.splitlines():
        if line.startswith("# "):
            title = line[2:].strip().replace("—", "-")
            break

    stamp = datetime.date.today().isoformat()
    page = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>{css}</style>
</head>
<body id="top">
<div class="layout">
<nav class="side">
  <div class="brand">01_PhD_Research · HSX GaN Hall sensing</div>
  <div class="doctitle">{label}</div>
  <div class="siblings"><b>Reports</b>{links}</div>
  <div class="toc-head">On this page</div>
  {toc}
</nav>
<main>
  <div class="meta">Reader view generated {stamp} from
  <code>{md_name}</code> — the markdown is the source of truth
  (regenerate with <code>python3 tools/md2html.py</code>).</div>
  {body}
</main>
</div>
<a class="backtop" href="#top">&uarr; top</a>
</body>
</html>
"""
    out = src[:-3] + ".html"
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(page.format(title=html_mod.escape(title), css=CSS,
                             label=html_mod.escape(label),
                             links="".join(links), toc=toc_html,
                             stamp=stamp, md_name=html_mod.escape(
                                 os.path.basename(src)),
                             body=body))
    return os.path.relpath(out, ROOT)


def build_index(all_docs):
    stamp = datetime.date.today().isoformat()
    cards = []
    for md_rel, label, desc in all_docs:
        cards.append("""
  <a class="card" href="{href}">
    <div class="card-label">{label}</div>
    <div class="card-desc">{desc}</div>
    <div class="card-path">{path}</div>
  </a>""".format(href=html_mod.escape(md_rel[:-3] + ".html"),
                 label=html_mod.escape(label), desc=html_mod.escape(desc),
                 path=html_mod.escape(md_rel)))
    page = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>PhD research reports — index</title>
<style>{css}
.wrap{{max-width:820px;margin:0 auto;padding:48px 24px}}
.card{{display:block;background:var(--panel);border:1px solid var(--border);
  border-radius:10px;padding:18px 22px;margin:14px 0;text-decoration:none;
  color:var(--ink)}}
.card:hover{{border-color:var(--accent)}}
.card-label{{font-family:"Avenir Next","Segoe UI",system-ui,sans-serif;
  font-weight:700;font-size:17px;color:var(--accent)}}
.card-desc{{margin:6px 0 8px;color:var(--ink)}}
.card-path{{font-family:monospace;font-size:12px;color:var(--muted)}}
</style>
</head>
<body>
<div class="wrap">
  <div class="meta" style="border:none">01_PhD_Research · reader-friendly
  report index · generated {stamp}</div>
  <h1>HSX GaN Hall-sensing — reports</h1>
  <p>Each card opens the styled reader view; the markdown next to it is
  the source of truth. Regenerate after edits:
  <code>python3 tools/md2html.py</code></p>
  {cards}
</div>
</body>
</html>
""".format(css=CSS, stamp=stamp, cards="".join(cards))
    out = os.path.join(ROOT, INDEX)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(page)
    return INDEX


def main():
    written = [build_page(md_rel, label, DOCS) for md_rel, label, _ in DOCS]
    written.append(build_index(DOCS))
    for w in written:
        print("wrote", w)


if __name__ == "__main__":
    main()
