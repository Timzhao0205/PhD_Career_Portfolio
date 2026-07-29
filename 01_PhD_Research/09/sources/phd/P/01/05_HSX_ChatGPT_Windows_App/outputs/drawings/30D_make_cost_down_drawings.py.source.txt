"""Generate the Stage-30 cost-down concept and selected-package drawings."""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Polygon, Rectangle

OUT = Path(__file__).resolve().parent

TI = "#9aa9b8"
TI_DARK = "#4f6476"
CER = "#f1cf77"
SENSOR = "#d86b55"
HARNESS = "#2c7fb8"
HOLD = "#b4332a"
INK = "#1f2937"
GREEN = "#1b7f5a"


def setup(ax, title):
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title, fontsize=12, weight="bold", color=INK, pad=8)


def folded_icon(ax, origin=(0, 0), scale=1.0, cartridges=True):
    x, y = origin
    base = Polygon(
        [(x, y), (x + 4.4 * scale, y + 1.8 * scale), (x + 2.1 * scale, y + 3.0 * scale), (x - 2.3 * scale, y + 1.2 * scale)],
        closed=True,
        facecolor=TI,
        edgecolor=TI_DARK,
        lw=1.3,
    )
    left = Polygon(
        [(x - 2.3 * scale, y + 1.2 * scale), (x, y), (x, y + 4.7 * scale), (x - 2.3 * scale, y + 5.9 * scale)],
        closed=True,
        facecolor="#8799aa",
        edgecolor=TI_DARK,
        lw=1.3,
    )
    right = Polygon(
        [(x + 4.4 * scale, y + 1.8 * scale), (x, y), (x, y + 4.7 * scale), (x + 4.4 * scale, y + 6.5 * scale)],
        closed=True,
        facecolor="#aebac5",
        edgecolor=TI_DARK,
        lw=1.3,
    )
    ax.add_patch(base)
    ax.add_patch(left)
    ax.add_patch(right)
    for px, py in ((x - 2.0, y - 1.5), (x + 3.8, y - 0.8), (x - 0.2, y - 2.0), (x + 5.0, y + 0.3)):
        ax.add_patch(Rectangle((px * scale, py * scale), 0.55 * scale, 2.2 * scale, facecolor=TI_DARK, edgecolor=INK, lw=0.7))
    if cartridges:
        ax.add_patch(Polygon([(x - 1.8 * scale, y + 2.0 * scale), (x - 0.25 * scale, y + 1.2 * scale), (x - 0.25 * scale, y + 3.6 * scale), (x - 1.8 * scale, y + 4.4 * scale)], facecolor=CER, edgecolor=INK, lw=1.0))
        ax.add_patch(Polygon([(x + 0.55 * scale, y + 1.1 * scale), (x + 3.6 * scale, y + 2.4 * scale), (x + 3.6 * scale, y + 4.7 * scale), (x + 0.55 * scale, y + 3.4 * scale)], facecolor=CER, edgecolor=INK, lw=1.0))
        ax.add_patch(Polygon([(x - 0.9 * scale, y + 1.25 * scale), (x + 2.4 * scale, y + 2.55 * scale), (x + 1.05 * scale, y + 3.25 * scale), (x - 2.1 * scale, y + 1.9 * scale)], facecolor=CER, edgecolor=INK, lw=1.0))


def concepts():
    fig, axes = plt.subplots(1, 4, figsize=(17, 5.6), dpi=150)
    fig.patch.set_facecolor("white")

    setup(axes[0], "D1 — SELECTED\nfolded trihedral")
    folded_icon(axes[0], (0, 0), 0.72)
    axes[0].set_xlim(-3.0, 5.0)
    axes[0].set_ylim(-2.4, 6.0)
    axes[0].text(-2.7, -1.5, "one laser-cut blank\ntwo main bends\n0 fixed ceramic seats\n3 flat ceramic guards\n3 face screws", fontsize=9.3, color=INK)
    axes[0].text(-2.7, -2.15, "hard gates: PASS / conditional", fontsize=9.5, color=GREEN, weight="bold")

    setup(axes[1], "D2 — RUNNER-UP\nthree face modules")
    for dx, dy, rot in ((0, 0, 0), (2.1, 1.0, 15), (0.7, 2.4, -10)):
        axes[1].add_patch(Rectangle((dx, dy), 3.1, 3.1, angle=rot, facecolor=TI, edgecolor=INK, lw=1.2))
        axes[1].add_patch(Rectangle((dx + 0.6, dy + 0.6), 1.9, 1.9, angle=rot, facecolor=CER, edgecolor=INK, lw=0.9))
    axes[1].set_xlim(-1.0, 6.0)
    axes[1].set_ylim(-2.3, 6.4)
    axes[1].text(-0.8, -1.45, "three identical bent Ti faces\nsimple single bends\nmore joints and datum stack\n6–9 extra fasteners", fontsize=9.3, color=INK)
    axes[1].text(-0.8, -2.08, "hard gates: PASS / conditional", fontsize=9.5, color=GREEN, weight="bold")

    setup(axes[2], "D3 — REJECT\ndirect metal clip")
    axes[2].add_patch(Rectangle((0, 0.6), 4.6, 4.6, facecolor=TI, edgecolor=INK, lw=1.3))
    axes[2].add_patch(Rectangle((0.85, 1.45), 2.9, 2.9, facecolor="#ece7d6", edgecolor=INK, lw=1.0))
    axes[2].add_patch(Circle((2.3, 2.9), 0.55, facecolor=SENSOR, edgecolor=INK, lw=0.8))
    axes[2].plot([0.4, 4.2], [5.0, 0.8], color=HOLD, lw=3)
    axes[2].plot([0.4, 4.2], [0.8, 5.0], color=HOLD, lw=3)
    axes[2].set_xlim(-0.9, 5.5)
    axes[2].set_ylim(-2.3, 6.4)
    axes[2].text(-0.7, -1.45, "no custom guard ceramic\nbut metal near active area\nshorting and bond exposure\nmagnetic error unbounded", fontsize=9.3, color=INK)
    axes[2].text(-0.7, -2.08, "hard gates: FAIL", fontsize=9.5, color=HOLD, weight="bold")

    setup(axes[3], "OLD A — SUPERSEDED\nfixed zirconia seats")
    folded_icon(axes[3], (0, 0), 0.72)
    for px, py in ((-1.45, 2.0), (1.75, 2.5), (0.0, 1.6)):
        axes[3].add_patch(Rectangle((px, py), 2.7, 0.28, facecolor="#f5f5f5", edgecolor=HOLD, lw=1.2))
    axes[3].set_xlim(-3.0, 5.0)
    axes[3].set_ylim(-2.4, 6.0)
    axes[3].text(-2.7, -1.5, "3 fixed zirconia seats\n3 guarded cartridges\n6 face screws + 6 keepers\npost-fire ceramic DFM", fontsize=9.3, color=INK)
    axes[3].text(-2.7, -2.15, "passes fit; loses cost decision", fontsize=9.5, color=HOLD, weight="bold")

    fig.suptitle("HSX 250 °C UHV package cost-down concepts — NOT FOR FABRICATION", fontsize=15, weight="bold", color=INK)
    fig.tight_layout(rect=(0, 0, 1, 0.92))
    for ext in ("svg", "png"):
        fig.savefig(OUT / f"30D_cost_down_concepts.{ext}", bbox_inches="tight")
    plt.close(fig)


def selected():
    fig, axes = plt.subplots(2, 2, figsize=(15, 11), dpi=150)
    fig.patch.set_facecolor("white")

    setup(axes[0, 0], "A. selected folded assembly")
    folded_icon(axes[0, 0], (0, 0), 0.88)
    axes[0, 0].text(-3.0, 6.1, "flat ceramic guard travels with each protected cartridge", fontsize=9.3, color=INK)
    axes[0, 0].text(-3.0, 5.6, "folded CP-Ti bracket: one flat blank, two main 90° bends", fontsize=9.3, color=INK)
    axes[0, 0].set_xlim(-3.6, 6.1)
    axes[0, 0].set_ylim(-2.6, 7.0)

    setup(axes[0, 1], "B. top envelope check")
    axes[0, 1].add_patch(Circle((0, 0), 15.875, fill=False, edgecolor=HOLD, lw=2.0, ls="--"))
    axes[0, 1].add_patch(Rectangle((-10.15, -10.15), 20.60, 20.60, fill=False, edgecolor=TI_DARK, lw=1.6))
    axes[0, 1].add_patch(Rectangle((-6.8, -6.8), 13.6, 13.6, facecolor=TI, edgecolor=INK, lw=1.0, alpha=0.85))
    axes[0, 1].add_patch(Rectangle((7.3, -5.45), 3.15, 10.9, facecolor=CER, edgecolor=INK, lw=1.0))
    axes[0, 1].add_patch(Rectangle((-5.45, 7.3), 10.9, 3.15, facecolor=CER, edgecolor=INK, lw=1.0))
    for px in (-9, 9):
        for py in (-9, 9):
            axes[0, 1].add_patch(Circle((px, py), 1.15, facecolor=TI_DARK, edgecolor=INK, lw=0.7))
    axes[0, 1].plot([0, 14.779], [0, 0], color=HARNESS, lw=1.8)
    axes[0, 1].text(2.3, 0.8, "R = 14.779 mm", color=HARNESS, fontsize=9.5, weight="bold")
    axes[0, 1].text(-15.2, -17.3, "hard radius 15.875 mm  |  radial margin 1.096 mm\nphysical height 26.250 mm  |  height margin 1.250 mm", fontsize=9.5, color=INK)
    axes[0, 1].set_xlim(-18, 18)
    axes[0, 1].set_ylim(-18, 18)

    setup(axes[1, 0], "C. one-face section and load path")
    axes[1, 0].add_patch(Rectangle((0, 0), 0.5, 6.2, facecolor=TI, edgecolor=INK, lw=1.0))
    axes[1, 0].add_patch(Rectangle((0.5, 1.0), 2.4, 4.2, facecolor=CER, edgecolor=INK, lw=1.0))
    axes[1, 0].add_patch(Rectangle((2.9, 0.4), 0.4, 5.4, facecolor=TI_DARK, edgecolor=INK, lw=1.0))
    axes[1, 0].add_patch(Rectangle((-0.7, -0.2), 0.7, 1.5, facecolor=TI_DARK, edgecolor=INK, lw=1.0))
    axes[1, 0].plot([-0.7, 3.5], [0.55, 0.55], color=INK, lw=2.0)
    axes[1, 0].add_patch(Circle((3.5, 0.55), 0.5, facecolor=TI_DARK, edgecolor=INK, lw=1.0))
    axes[1, 0].add_patch(Rectangle((-0.6, 4.7), 0.6, 0.5, facecolor=TI_DARK, edgecolor=INK, lw=1.0))
    axes[1, 0].plot([-0.3, 3.0], [4.95, 4.95], color=TI_DARK, lw=2.5)
    axes[1, 0].add_patch(FancyArrowPatch((3.8, 3.1), (0.15, 3.1), arrowstyle="-|>", mutation_scale=15, lw=2, color=GREEN))
    axes[1, 0].text(0.8, 3.35, "clamp load → guard hard stops → bracket", fontsize=9.3, color=GREEN, weight="bold")
    axes[1, 0].text(-0.8, 6.4, "two open hooks + one screw; nut plate reacts on Ti only", fontsize=9.3, color=INK)
    axes[1, 0].text(-0.8, -1.1, "0.50 sheet   2.40 cartridge envelope   0.40 clamp\nno die/bond/fanout/electrical joint in retention load path", fontsize=9.3, color=INK)
    axes[1, 0].set_xlim(-1.5, 5.3)
    axes[1, 0].set_ylim(-1.7, 7.2)

    setup(axes[1, 1], "D. independent one-axis service")
    steps = [
        ("1", "support handling jig\nand disconnect only\nthat remote pigtail"),
        ("2", "remove one external\nface screw"),
        ("3", "slide 0.8 mm to\ndisengage two\nopen-edge hooks"),
        ("4", "withdraw protected\ncartridge normal\nto its face"),
    ]
    for i, (num, text) in enumerate(steps):
        x = i * 3.2
        axes[1, 1].add_patch(Circle((x, 2.8), 0.55, facecolor=HARNESS, edgecolor=INK, lw=1.0))
        axes[1, 1].text(x, 2.8, num, ha="center", va="center", color="white", fontsize=12, weight="bold")
        axes[1, 1].text(x, 1.8, text, ha="center", va="top", fontsize=9.0, color=INK)
        if i < 3:
            axes[1, 1].add_patch(FancyArrowPatch((x + 0.7, 2.8), (x + 2.5, 2.8), arrowstyle="-|>", mutation_scale=14, lw=1.6, color=TI_DARK))
    axes[1, 1].text(0, -0.9, "X/Y/Z neighbours remain installed; reinstallation ends with identity, isolation, polarity and vector-calibration checks.", fontsize=9.0, color=GREEN, weight="bold")
    axes[1, 1].text(0, -1.55, "HOLD: hook strength, captive-lance retention, preload and hot-UHV service-cycle test.", fontsize=9.0, color=HOLD, weight="bold")
    axes[1, 1].set_xlim(-1.2, 11.2)
    axes[1, 1].set_ylim(-2.1, 4.4)

    fig.suptitle("HSX cost-down package — selected architecture — NOT FOR FABRICATION", fontsize=16, weight="bold", color=INK)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    for ext in ("svg", "png"):
        fig.savefig(OUT / f"30D_cost_down_selected.{ext}", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    concepts()
    selected()
    print(OUT / "30D_cost_down_concepts.svg")
    print(OUT / "30D_cost_down_selected.svg")
