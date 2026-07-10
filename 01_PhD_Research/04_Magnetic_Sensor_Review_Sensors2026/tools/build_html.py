#!/usr/bin/env python3
"""
build_html.py -- reader-friendly .html mirrors of the review-paper outputs.

Auto-discovers every outputs/*.md, renders a self-contained styled .html next to
it (sidebar table of contents from the headings, styled tables, dark-mode aware,
printable), and writes outputs/index.html linking them all. The markdown stays
the source of truth; never hand-edit the .html.

    pip install markdown        # one-time
    python tools/build_html.py

Run from the review-paper folder (run.ps1 does this for you). Non-fatal: if the
markdown package is missing it prints a hint and exits 3 so the pipeline keeps
going.
"""
import datetime
import glob
import html as html_mod
import os
import re
import sys

try:
    import markdown
except ImportError:
    print("python-markdown not installed -- run: pip install markdown "
          "(HTML mirrors skipped; the .md files are unaffected)", file=sys.stderr)
    sys.exit(3)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                 # the review-paper folder
OUT = os.path.join(ROOT, "outputs")
INDEX = os.path.join(OUT, "index.html")

CSS = """
:root{--bg:#ffffff;--fg:#1a1a1a;--muted:#6b7280;--accent:#2563eb;--line:#e5e7eb;--code:#f3f4f6;}
@media(prefers-color-scheme:dark){:root{--bg:#0f1115;--fg:#e6e6e6;--muted:#9aa4b2;--accent:#6ea8fe;--line:#262b33;--code:#171a21;}}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.6 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif}
.wrap{display:grid;grid-template-columns:260px 1fr;max-width:1200px;margin:0 auto;min-height:100vh}
nav{position:sticky;top:0;align-self:start;height:100vh;overflow:auto;padding:24px 16px;border-right:1px solid var(--line);font-size:14px}
nav .home{display:inline-block;margin-bottom:12px;color:var(--muted);text-decoration:none}
nav a{display:block;color:var(--fg);text-decoration:none;padding:3px 6px;border-radius:6px}
nav a:hover{background:var(--code)}
nav a.h3{padding-left:18px;color:var(--muted)}
main{padding:40px 48px;max-width:820px}
main h1{font-size:1.9rem;margin-top:.2em;border-bottom:2px solid var(--line);padding-bottom:.3em}
main h2{margin-top:1.8em;border-bottom:1px solid var(--line);padding-bottom:.2em}
a{color:var(--accent)}
code{background:var(--code);padding:.12em .35em;border-radius:5px;font-size:.9em}
pre{background:var(--code);padding:14px;border-radius:10px;overflow:auto}
pre code{background:none;padding:0}
table{border-collapse:collapse;width:100%;margin:1em 0;font-size:.94em;display:block;overflow:auto}
th,td{border:1px solid var(--line);padding:7px 10px;text-align:left;vertical-align:top}
th{background:var(--code)}
blockquote{border-left:3px solid var(--accent);margin:1em 0;padding:.2em 1em;color:var(--muted)}
.meta{color:var(--muted);font-size:13px;margin-bottom:24px}
@media(max-width:820px){.wrap{grid-template-columns:1fr}nav{position:static;height:auto;border-right:none;border-bottom:1px solid var(--line)}main{padding:24px}}
@media print{nav{display:none}.wrap{display:block}main{max-width:none}}
"""

def render(md_path):
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    md = markdown.Markdown(extensions=["extra", "tables", "sane_lists", "toc"])
    body = md.convert(text)
    toc = re.findall(r'<h([23]) id="([^"]+)">(.*?)</h[23]>', body)
    nav = ['<a class="home" href="index.html">&larr; all outputs</a>']
    for lvl, hid, htxt in toc:
        cls = "h3" if lvl == "3" else "h2"
        nav.append(f'<a class="{cls}" href="#{hid}">{re.sub(r"<[^>]+>","",htxt)}</a>')
    title = os.path.basename(md_path)[:-3]
    mtime = datetime.datetime.fromtimestamp(os.path.getmtime(md_path)).strftime("%Y-%m-%d %H:%M")
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html_mod.escape(title)}</title><style>{CSS}</style></head>
<body><div class="wrap"><nav>{''.join(nav)}</nav>
<main><div class="meta">Mirror of <code>outputs/{html_mod.escape(os.path.basename(md_path))}</code> &middot; generated {mtime} &middot; markdown is the source of truth</div>
{body}</main></div></body></html>"""
    out = md_path[:-3] + ".html"
    with open(out, "w", encoding="utf-8") as f:
        f.write(page)
    return out, title

def main():
    if not os.path.isdir(OUT):
        print("no outputs/ folder yet -- nothing to mirror", file=sys.stderr)
        return
    mds = sorted(glob.glob(os.path.join(OUT, "*.md")))
    if not mds:
        print("no outputs/*.md yet -- nothing to mirror", file=sys.stderr)
        return
    made = [render(p) for p in mds]
    links = "".join(
        f'<li><a href="{html_mod.escape(os.path.basename(p))}">{html_mod.escape(t)}</a></li>'
        for p, t in made
    )
    stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    idx = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Magnetic-sensor review - outputs</title><style>{CSS}</style></head>
<body><div class="wrap"><nav><a class="home" href="index.html">outputs index</a></nav>
<main><h1>Magnetic-sensor review &mdash; outputs</h1>
<div class="meta">generated {stamp}</div>
<p>Reader-friendly mirrors of the pipeline outputs. Open
<code>00_DELIVERABLE_paper_plan.html</code> first.</p>
<ul>{links}</ul></main></div></body></html>"""
    with open(INDEX, "w", encoding="utf-8") as f:
        f.write(idx)
    print(f"wrote {len(made)} html mirror(s) + index.html")

if __name__ == "__main__":
    main()
