"""Generate Stage-30 concept drawings as precise, editable SVG.

These are concept/clearance drawings, not released manufacturing drawings.
All dimensions are fired/finished millimetres unless marked otherwise.
"""

from pathlib import Path

OUT = Path(__file__).resolve().parent

COL = {
    "ink": "#172033", "muted": "#5c667a", "grid": "#d8dee9",
    "zr": "#6dc5c1", "zr_dark": "#277d7a", "ti": "#d7a85e",
    "ti_dark": "#8a5d20", "lcc": "#d97745", "harness": "#7b61b8",
    "danger": "#c94141", "ok": "#258552", "paper": "#fbfcfe",
}


def start(title, subtitle):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="560" viewBox="0 0 800 560">
<defs>
  <marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="{COL['ink']}"/></marker>
  <marker id="arrowRed" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="{COL['danger']}"/></marker>
  <pattern id="hatch" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="8" stroke="#b7c0cf" stroke-width="2"/></pattern>
  <style>
    text {{ font-family: Segoe UI, Arial, sans-serif; fill:{COL['ink']}; }}
    .t {{ font-size:22px; font-weight:700; }} .s {{ font-size:12px; fill:{COL['muted']}; }}
    .l {{ font-size:13px; }} .sm {{ font-size:11px; }} .dim {{ font-size:11px; fill:{COL['muted']}; }}
    .outline {{ stroke:{COL['ink']}; stroke-width:1.5; fill:none; }}
    .thin {{ stroke:{COL['muted']}; stroke-width:1; fill:none; }}
    .dash {{ stroke:{COL['danger']}; stroke-width:1.5; stroke-dasharray:7 5; fill:none; }}
    .axis {{ stroke:{COL['ink']}; stroke-width:1.5; marker-end:url(#arrow); fill:none; }}
  </style>
</defs>
<rect width="800" height="560" fill="{COL['paper']}"/>
<text x="32" y="38" class="t">{title}</text>
<text x="32" y="59" class="s">{subtitle}</text>
<rect x="621" y="22" width="147" height="28" rx="5" fill="#fff0d6" stroke="#d8841c"/>
<text x="694.5" y="41" class="sm" text-anchor="middle" fill="#8b4d00">NOT FOR FABRICATION</text>
<line x1="32" y1="72" x2="768" y2="72" stroke="{COL['grid']}"/>
'''


def end(note="All dimensions mm. Geometry is conceptual pending Stage-40 red team and vendor DFM."):
    return f'''<line x1="32" y1="526" x2="768" y2="526" stroke="{COL['grid']}"/>
<text x="32" y="546" class="s">{note}</text></svg>'''


def legend():
    return f'''<g transform="translate(555 86)">
<rect width="210" height="75" rx="6" fill="white" stroke="{COL['grid']}"/>
<rect x="12" y="12" width="15" height="10" fill="{COL['zr']}"/><text x="35" y="21" class="sm">zirconia / ceramic datum</text>
<rect x="12" y="31" width="15" height="10" fill="{COL['ti']}"/><text x="35" y="40" class="sm">CP-Ti frame / retention</text>
<rect x="12" y="50" width="15" height="10" fill="{COL['lcc']}"/><text x="35" y="59" class="sm">bonded LCC cartridge</text></g>'''


def iso(concept):
    cfg = {
        "A": ("Concept A — exploded tri-plate cage", "Three identical 9.60 × 9.60 × 1.00 zirconia seats; external CP-Ti cage", "three identical flat seats"),
        "B": ("Concept B — exploded monolithic core", "One 11.30 mm zirconia core; external face clamps and nut pads", "one monolithic zirconia core"),
        "C": ("Concept C — exploded split cassettes", "10.50 mm core; zirconia rear datum + LCC + 0.50 mm Ti front guard", "three independently pinned cassettes"),
    }[concept]
    out = start(cfg[0], cfg[1]) + legend()
    # common isometric base and posts
    out += f'''<g transform="translate(85 70)">
<polygon points="170,270 300,205 430,270 300,335" fill="{COL['ti']}" fill-opacity=".35" stroke="{COL['ti_dark']}" stroke-width="2"/>
<polygon points="170,270 170,286 300,352 300,335" fill="{COL['ti']}" stroke="{COL['ti_dark']}"/>
<polygon points="300,335 430,270 430,286 300,352" fill="#ba8439" stroke="{COL['ti_dark']}"/>
<g fill="{COL['ti']}" stroke="{COL['ti_dark']}" stroke-width="1.5">
<rect x="185" y="285" width="13" height="92"/><rect x="397" y="285" width="13" height="92"/>
<rect x="255" y="327" width="13" height="78"/><rect x="330" y="327" width="13" height="78"/>
</g>
<text x="300" y="420" class="l" text-anchor="middle">connected CP-Ti base frame + four posts</text>
'''
    if concept == "A":
        out += f'''<polygon points="255,165 335,125 415,165 335,205" fill="none" stroke="{COL['ti_dark']}" stroke-width="5"/>
<polygon points="255,165 255,245 335,285 335,205" fill="{COL['zr']}" fill-opacity=".9" stroke="{COL['zr_dark']}" stroke-width="2"/>
<polygon points="335,205 415,165 415,245 335,285" fill="{COL['zr']}" fill-opacity=".75" stroke="{COL['zr_dark']}" stroke-width="2"/>
<polygon points="267,155 335,121 403,155 335,189" fill="{COL['zr']}" stroke="{COL['zr_dark']}" stroke-width="2"/>
<path d="M220 210 L174 190" class="axis"/><path d="M410 208 L466 181" class="axis"/><path d="M335 126 L335 82" class="axis"/>
<g fill="{COL['lcc']}" stroke="#8e3f1d" stroke-width="1.5"><rect x="134" y="168" width="45" height="45"/><rect x="462" y="157" width="45" height="45"/><rect x="313" y="62" width="45" height="45"/></g>
<text x="153" y="160" class="sm">X cartridge</text><text x="463" y="149" class="sm">Y cartridge</text><text x="366" y="89" class="sm">Z cartridge</text>'''
    elif concept == "B":
        out += f'''<polygon points="255,150 335,110 415,150 335,190" fill="{COL['zr']}" stroke="{COL['zr_dark']}" stroke-width="2"/>
<polygon points="255,150 255,250 335,290 335,190" fill="#58aaa7" stroke="{COL['zr_dark']}" stroke-width="2"/>
<polygon points="335,190 415,150 415,250 335,290" fill="#87d4d0" stroke="{COL['zr_dark']}" stroke-width="2"/>
<path d="M251 208 L184 208" class="axis"/><path d="M419 207 L486 207" class="axis"/><path d="M335 111 L335 55" class="axis"/>
<g fill="{COL['lcc']}" stroke="#8e3f1d" stroke-width="1.5"><rect x="137" y="185" width="48" height="48"/><rect x="485" y="184" width="48" height="48"/><rect x="311" y="39" width="48" height="48"/></g>
<text x="270" y="315" class="l">open-bottom core; 1.65 mm minimum side web</text>'''
    else:
        out += f'''<polygon points="263,157 335,121 407,157 335,193" fill="{COL['zr']}" stroke="{COL['zr_dark']}" stroke-width="2"/>
<polygon points="263,157 263,247 335,283 335,193" fill="#58aaa7" stroke="{COL['zr_dark']}" stroke-width="2"/>
<polygon points="335,193 407,157 407,247 335,283" fill="#87d4d0" stroke="{COL['zr_dark']}" stroke-width="2"/>
<g stroke-width="1.5"><path d="M255 205 L158 205" class="axis"/><rect x="129" y="179" width="24" height="52" fill="{COL['ti']}" stroke="{COL['ti_dark']}"/><rect x="99" y="179" width="24" height="52" fill="{COL['lcc']}" stroke="#8e3f1d"/><rect x="69" y="179" width="24" height="52" fill="{COL['zr']}" stroke="{COL['zr_dark']}"/>
<path d="M415 205 L512 205" class="axis"/><rect x="517" y="179" width="24" height="52" fill="{COL['zr']}" stroke="{COL['zr_dark']}"/><rect x="547" y="179" width="24" height="52" fill="{COL['lcc']}" stroke="#8e3f1d"/><rect x="577" y="179" width="24" height="52" fill="{COL['ti']}" stroke="{COL['ti_dark']}"/>
<path d="M335 120 L335 45" class="axis"/><rect x="309" y="13" width="52" height="18" fill="{COL['ti']}" stroke="{COL['ti_dark']}"/></g>
<text x="68" y="247" class="sm">rear / LCC / guard</text><text x="480" y="247" class="sm">shared Ti rail cage</text>'''
    out += f'''<text x="300" y="440" class="l" text-anchor="middle">{cfg[2]}</text></g>'''
    return out + end()


def top(concept):
    names = {"A":"Concept A — top envelope", "B":"Concept B — top envelope", "C":"Concept C — top envelope"}
    out = start(names[concept], "Conservative installed fastener + reserved harness envelope") + legend()
    cx, cy, sc = 330, 300, 13.5
    r = 15.875 * sc
    out += f'''<circle cx="{cx}" cy="{cy}" r="{r:.1f}" fill="none" stroke="{COL['danger']}" stroke-width="2" stroke-dasharray="8 5"/>
<text x="{cx}" y="{cy-r-10:.1f}" class="l" text-anchor="middle">Ø31.75 hard envelope</text>
<line x1="{cx-r:.1f}" y1="{cy}" x2="{cx+r:.1f}" y2="{cy}" class="thin"/><line x1="{cx}" y1="{cy-r:.1f}" x2="{cx}" y2="{cy+r:.1f}" class="thin"/>
'''
    # posts and harness corridors
    for x in (-9, 9):
        for y in (-9, 9):
            out += f'<circle cx="{cx+x*sc:.1f}" cy="{cy-y*sc:.1f}" r="{1.15*sc:.1f}" fill="{COL["ti"]}" stroke="{COL["ti_dark"]}"/>'
    for x, y in ((-6.3,3.8),(3.8,-6.3),(-6.3,-3.8)):
        out += f'<rect x="{cx+(x-1.5)*sc:.1f}" y="{cy-(y+1.5)*sc:.1f}" width="{3*sc:.1f}" height="{3*sc:.1f}" fill="{COL["harness"]}" fill-opacity=".35" stroke="{COL["harness"]}"/>'
    if concept in "AB":
        side = 15.6 * sc
        out += f'<rect x="{cx-side/2:.1f}" y="{cy-side/2:.1f}" width="{side:.1f}" height="{side:.1f}" fill="{COL["ti"]}" fill-opacity=".25" stroke="{COL["ti_dark"]}" stroke-width="2"/>'
        inner = (10.0 if concept == "A" else 11.3) * sc
        out += f'<rect x="{cx-inner/2:.1f}" y="{cy-inner/2:.1f}" width="{inner:.1f}" height="{inner:.1f}" fill="{COL["zr"]}" fill-opacity=".65" stroke="{COL["zr_dark"]}"/>'
    else:
        inner = 10.5 * sc
        out += f'<rect x="{cx-inner/2:.1f}" y="{cy-inner/2:.1f}" width="{inner:.1f}" height="{inner:.1f}" fill="{COL["zr"]}" fill-opacity=".65" stroke="{COL["zr_dark"]}"/>'
        for u in (-5.7,5.7):
            out += f'<rect x="{cx+(u-.5)*sc:.1f}" y="{cy-5.3*sc:.1f}" width="{sc:.1f}" height="{10.6*sc:.1f}" fill="{COL["ti"]}" stroke="{COL["ti_dark"]}"/>'
    out += f'''<circle cx="{cx}" cy="{cy}" r="{14.354*sc:.1f}" fill="none" stroke="{COL['ok']}" stroke-dasharray="3 4"/>
<line x1="{cx}" y1="{cy}" x2="{cx+14.354*sc:.1f}" y2="{cy}" stroke="{COL['ok']}" marker-end="url(#arrow)"/>
<text x="555" y="205" class="l">Kernel result</text><text x="555" y="228" class="sm">conservative radius 14.354</text>
<text x="555" y="247" class="sm" fill="{COL['ok']}">radial margin 1.521 PASS</text>
<text x="555" y="280" class="l">Installed reservations</text><text x="555" y="303" class="sm">4 posts: centers ±9.0, r 1.15</text>
<text x="555" y="322" class="sm">3 harness corridors: 3.0 × 3.0</text><text x="555" y="341" class="sm">fastener heads included in CAD</text>
<text x="555" y="376" class="l">HOLD</text><text x="555" y="399" class="sm">actual wire OD and bend radius</text><text x="555" y="418" class="sm">mated 19C datum confirmation</text>'''
    return out + end("Bounding-box radius combines independent X/Y extrema and is conservative; all installed modeled solids pass.")


def section(concept):
    cfg = {
        "A": ("Concept A — axial section", 26.70, "10.00 Ti cage + 1.00 seat", "+ 2.40 cartridge + 0.50 clamp + 0.30 head"),
        "B": ("Concept B — axial section", 27.00, "11.30 core + 2.40 cartridge", "+ 0.50 clamp + 0.30 head"),
        "C": ("Concept C — axial section", 26.55, "10.50 core + 3.25 cassette", "+ 0.30 pin projection"),
    }[concept]
    out = start(cfg[0], "Flange datum z = 0; full height includes feedthrough keep-out, hardware, and retention projection")
    y0, sc, x0 = 495, 12.2, 280
    yy = lambda z: y0 - z*sc
    out += f'''<rect x="105" y="{yy(10.41):.1f}" width="{22.1*sc:.1f}" height="{10.41*sc:.1f}" fill="#f8dddd" stroke="{COL['danger']}" stroke-dasharray="6 4"/>
<text x="115" y="{yy(5):.1f}" class="sm" fill="{COL['danger']}">conservative 19C keep-out</text>
<rect x="{x0-7.5*sc:.1f}" y="{yy(12.5):.1f}" width="{15*sc:.1f}" height="{1*sc:.1f}" fill="{COL['ti']}" stroke="{COL['ti_dark']}"/>
<rect x="{x0-9*sc-1.15*sc:.1f}" y="{yy(11.5):.1f}" width="{2.3*sc:.1f}" height="{11.5*sc:.1f}" fill="{COL['ti']}" stroke="{COL['ti_dark']}"/>
<rect x="{x0+9*sc-1.15*sc:.1f}" y="{yy(11.5):.1f}" width="{2.3*sc:.1f}" height="{11.5*sc:.1f}" fill="{COL['ti']}" stroke="{COL['ti_dark']}"/>
'''
    if concept == "A":
        out += f'''<rect x="{x0-5*sc:.1f}" y="{yy(22.5):.1f}" width="{10*sc:.1f}" height="{10*sc:.1f}" fill="none" stroke="{COL['ti_dark']}" stroke-width="3"/>
<rect x="{x0-4.8*sc:.1f}" y="{yy(23.5):.1f}" width="{9.6*sc:.1f}" height="{1*sc:.1f}" fill="{COL['zr']}" stroke="{COL['zr_dark']}"/>
<rect x="{x0-5.45*sc:.1f}" y="{yy(25.9):.1f}" width="{10.9*sc:.1f}" height="{2.4*sc:.1f}" fill="{COL['lcc']}" stroke="#8e3f1d"/>
<rect x="{x0-7.8*sc:.1f}" y="{yy(26.4):.1f}" width="{15.6*sc:.1f}" height="{.5*sc:.1f}" fill="{COL['ti']}" stroke="{COL['ti_dark']}"/>'''
    elif concept == "B":
        out += f'''<rect x="{x0-5.65*sc:.1f}" y="{yy(23.8):.1f}" width="{11.3*sc:.1f}" height="{11.3*sc:.1f}" fill="{COL['zr']}" stroke="{COL['zr_dark']}"/>
<rect x="{x0-4*sc:.1f}" y="{yy(19.3):.1f}" width="{8*sc:.1f}" height="{6.8*sc:.1f}" fill="url(#hatch)" stroke="{COL['zr_dark']}"/>
<rect x="{x0-5.45*sc:.1f}" y="{yy(26.2):.1f}" width="{10.9*sc:.1f}" height="{2.4*sc:.1f}" fill="{COL['lcc']}" stroke="#8e3f1d"/>
<rect x="{x0-7.8*sc:.1f}" y="{yy(26.7):.1f}" width="{15.6*sc:.1f}" height="{.5*sc:.1f}" fill="{COL['ti']}" stroke="{COL['ti_dark']}"/>'''
    else:
        out += f'''<rect x="{x0-5.25*sc:.1f}" y="{yy(23.0):.1f}" width="{10.5*sc:.1f}" height="{10.5*sc:.1f}" fill="{COL['zr']}" stroke="{COL['zr_dark']}"/>
<rect x="{x0-3.25*sc:.1f}" y="{yy(20):.1f}" width="{6.5*sc:.1f}" height="{7.5*sc:.1f}" fill="url(#hatch)" stroke="{COL['zr_dark']}"/>
<rect x="{x0-4.9*sc:.1f}" y="{yy(24):.1f}" width="{9.8*sc:.1f}" height="{1*sc:.1f}" fill="{COL['zr']}" stroke="{COL['zr_dark']}"/>
<rect x="{x0-4.445*sc:.1f}" y="{yy(25.65):.1f}" width="{8.89*sc:.1f}" height="{1.65*sc:.1f}" fill="{COL['lcc']}" stroke="#8e3f1d"/>
<rect x="{x0-4.9*sc:.1f}" y="{yy(26.25):.1f}" width="{9.8*sc:.1f}" height="{.5*sc:.1f}" fill="{COL['ti']}" stroke="{COL['ti_dark']}"/>'''
    out += f'''<line x1="595" y1="{yy(0):.1f}" x2="595" y2="{yy(cfg[1]):.1f}" class="axis"/>
<text x="611" y="{(yy(0)+yy(cfg[1]))/2:.1f}" class="l">{cfg[1]:.2f} nominal</text>
<line x1="635" y1="{yy(27.5):.1f}" x2="635" y2="{yy(0):.1f}" class="dash"/>
<text x="650" y="{yy(27.5)+4:.1f}" class="sm" fill="{COL['danger']}">27.50 limit</text>
<text x="535" y="405" class="l">Stack</text><text x="535" y="426" class="sm">{cfg[2]}</text><text x="535" y="444" class="sm">{cfg[3]}</text>
<text x="535" y="466" class="sm">Worst-case height remains ≤27.36</text><text x="535" y="484" class="sm">using proposed tolerance ledger.</text>
<text x="535" y="498" class="sm" fill="{COL['danger']}">HOLD: verify true mated 19C height.</text>'''
    return out + end()


def contact(concept):
    title = {"A":"Concept A — cartridge contact detail", "B":"Concept B — cartridge contact detail", "C":"Concept C — split-cassette contact detail"}[concept]
    out = start(title, "Mechanical preload bypasses all electrical joints; bond-wire guard remains installed during service")
    out += f'''<g transform="translate(70 105)"><rect x="0" y="0" width="660" height="340" rx="8" fill="white" stroke="{COL['grid']}"/>
<rect x="55" y="225" width="520" height="36" fill="{COL['zr']}" stroke="{COL['zr_dark']}" stroke-width="2"/>
<text x="65" y="250" class="l">zirconia hard-stop datum</text>
'''
    if concept in "AB":
        out += f'''<rect x="185" y="150" width="260" height="75" fill="{COL['lcc']}" stroke="#8e3f1d" stroke-width="2"/>
<rect x="165" y="105" width="300" height="120" fill="none" stroke="{COL['zr_dark']}" stroke-width="8"/>
<path d="M235 158 Q270 98 305 158 Q340 98 375 158" fill="none" stroke="#c5c9d0" stroke-width="2"/>
<rect x="145" y="70" width="340" height="24" fill="{COL['ti']}" stroke="{COL['ti_dark']}" stroke-width="2"/>
<path d="M260 94 q20 55 40 0 M330 94 q20 55 40 0" fill="none" stroke="{COL['ti_dark']}" stroke-width="5"/>
<path d="M215 187 L105 187" stroke="{COL['harness']}" stroke-width="5"/><path d="M105 187 L70 205" stroke="{COL['harness']}" stroke-width="5"/>
<text x="500" y="84" class="sm">formed CP-Ti flexure tabs</text><text x="500" y="104" class="sm">δ20 = 0.10…0.26</text><text x="500" y="124" class="sm">δ250 ≈ 0.1005…0.2605</text>
<text x="500" y="158" class="sm">k target 1–2 N/mm</text><text x="500" y="178" class="sm">F = kδ = 0.10…0.52 N</text>
<text x="206" y="181" class="sm" fill="white">LCC02046</text><text x="220" y="132" class="sm">measured bond-loop keep-out + 0.30 min</text>
<text x="65" y="175" class="sm" fill="{COL['harness']}">qualified tongue + pigtail</text>'''
    else:
        out += f'''<rect x="180" y="195" width="270" height="30" fill="{COL['zr']}" stroke="{COL['zr_dark']}" stroke-width="2"/>
<rect x="200" y="130" width="230" height="65" fill="{COL['lcc']}" stroke="#8e3f1d" stroke-width="2"/>
<path d="M240 137 Q275 82 310 137 Q345 82 380 137" fill="none" stroke="#c5c9d0" stroke-width="2"/>
<rect x="170" y="78" width="290" height="18" fill="{COL['ti']}" stroke="{COL['ti_dark']}" stroke-width="2"/>
<rect x="135" y="70" width="16" height="165" fill="{COL['ti']}" stroke="{COL['ti_dark']}"/><circle cx="143" cy="112" r="8" fill="white" stroke="{COL['ti_dark']}" stroke-width="3"/>
<path d="M210 164 L95 164 L70 186" stroke="{COL['harness']}" stroke-width="5" fill="none"/>
<text x="480" y="88" class="sm">0.50 Ti front guard</text><text x="480" y="112" class="sm">1.00 zirconia rear datum</text><text x="480" y="136" class="sm">1.65 LCC + 0.10 axial clearance</text><text x="480" y="168" class="sm">pin captures external rail only</text><text x="480" y="188" class="sm">no pin through ceramic</text>'''
    out += f'''<path d="M515 215 L515 262" stroke="{COL['ok']}" stroke-width="5" marker-end="url(#arrow)"/><text x="535" y="244" class="sm" fill="{COL['ok']}">load path to hard stop</text>
<path d="M105 300 L520 300" stroke="{COL['harness']}" stroke-width="4" marker-end="url(#arrow)"/><text x="312" y="324" class="sm" text-anchor="middle" fill="{COL['harness']}">electrical path is strain-relieved separately; zero retention load</text></g>
<text x="70" y="475" class="l">Release tests</text><text x="70" y="497" class="sm">formed-flexure force at 20/250 °C after dwell • 25 service cycles • loop/guard optical clearance • hot contact resistance</text>'''
    return out + end("All force limits are ENGINEERING PROPOSAL - VALIDATE; CP-Ti creep/relaxation coupon is mandatory.")


def axes(concept):
    title = {"A":"Concept A — fastener and tool axes", "B":"Concept B — fastener and tool axes", "C":"Concept C — pin and tool axes"}[concept]
    out = start(title, "All retention axes are external; no crossed bolts, hidden nuts, or zirconia threads")
    out += f'''<g transform="translate(55 105)"><rect width="410" height="350" rx="8" fill="white" stroke="{COL['grid']}"/>
<rect x="140" y="95" width="150" height="150" fill="{COL['zr']}" fill-opacity=".6" stroke="{COL['zr_dark']}" stroke-width="2"/>
<rect x="130" y="85" width="170" height="170" fill="none" stroke="{COL['ti_dark']}" stroke-width="5"/>
<text x="215" y="175" class="l" text-anchor="middle">+Z face</text><text x="310" y="177" class="sm">+X sensor</text><text x="185" y="74" class="sm">+Y sensor</text>
'''
    if concept in "AB":
        out += f'''<circle cx="143" cy="170" r="8" fill="white" stroke="{COL['danger']}" stroke-width="3"/><circle cx="215" cy="242" r="8" fill="white" stroke="{COL['danger']}" stroke-width="3"/>
<path d="M143 170 L78 170" stroke="{COL['danger']}" stroke-width="2" marker-end="url(#arrowRed)"/><path d="M215 242 L215 315" stroke="{COL['danger']}" stroke-width="2" marker-end="url(#arrowRed)"/>
<text x="54" y="161" class="sm">Z-F1</text><text x="224" y="318" class="sm">Z-F2</text>
<text x="45" y="340" class="sm">Top fasteners occupy only −X and −Y edges.</text>'''
        table = "X-F1/F2: u=−6.50, z=cz±2.00 | Y-F1/F2: u=−6.50, z=cz∓2.00 | Z-F1: (−6.50,0) | Z-F2: (0,−6.50)"
    else:
        out += f'''<circle cx="143" cy="170" r="8" fill="white" stroke="{COL['danger']}" stroke-width="3"/><circle cx="215" cy="242" r="8" fill="white" stroke="{COL['danger']}" stroke-width="3"/>
<path d="M143 170 L78 170" stroke="{COL['danger']}" stroke-width="2" marker-end="url(#arrowRed)"/><path d="M215 242 L215 315" stroke="{COL['danger']}" stroke-width="2" marker-end="url(#arrowRed)"/>
<text x="42" y="161" class="sm">Z-P1</text><text x="224" y="318" class="sm">Z-P2</text><text x="45" y="340" class="sm">Pins engage the external rail cage; none pierces ceramic.</text>'''
        table = "X pins: u=−6.10, z=cz−3.00/−1.50 | Y pins: u=−6.10, z=cz+0.50/+2.00 | Z pins: (−6.10,0)/(0,−6.10)"
    out += f'''</g><g transform="translate(500 105)"><rect width="245" height="350" rx="8" fill="white" stroke="{COL['grid']}"/>
<text x="18" y="30" class="l">Straight tool access</text><rect x="62" y="85" width="95" height="145" fill="{COL['zr']}" fill-opacity=".55" stroke="{COL['zr_dark']}"/>
<path d="M158 130 L225 130" class="axis"/><path d="M158 180 L225 180" class="axis"/><path d="M98 85 L98 44" class="axis"/>
<text x="169" y="120" class="sm">+X</text><text x="169" y="170" class="sm">+Y</text><text x="108" y="54" class="sm">+Z</text>
<text x="18" y="264" class="sm">Ø3.0 driver/pull corridor</text><text x="18" y="284" class="sm">ENGINEERING PROPOSAL - VALIDATE</text>
<text x="18" y="316" class="sm" fill="{COL['ok']}">Kernel pairwise overlap: 0.000000 mm³</text><text x="18" y="336" class="sm">X/Y axis levels are staggered.</text></g>
<text x="55" y="486" class="sm">{table}</text><text x="55" y="509" class="sm">Assembly order: base frame → ceramic/core → guarded cartridges → external retainers → pigtail strain relief; removal reverses one branch only.</text>'''
    return out + end()


def main():
    for concept in "ABC":
        files = {
            f"30{concept}_isometric_exploded.svg": iso(concept),
            f"30{concept}_top_envelope.svg": top(concept),
            f"30{concept}_section.svg": section(concept),
            f"30{concept}_contact_detail.svg": contact(concept),
            f"30{concept}_fastener_axes.svg": axes(concept),
        }
        for name, data in files.items():
            (OUT / name).write_text(data, encoding="utf-8")
    print("generated 15 Stage-30 SVG drawings")


if __name__ == "__main__":
    main()
