"""Render the cost-down STL for visual QA; not an engineering calculator."""

from __future__ import annotations

import struct
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

HERE = Path(__file__).resolve().parent
STL = HERE / "30D_NFF.stl"
PNG = HERE.parent / "drawings" / "30D_cad_visual_QA.png"


def read_binary_stl(path: Path):
    data = path.read_bytes()
    count = struct.unpack_from("<I", data, 80)[0]
    expected = 84 + count * 50
    if len(data) != expected:
        raise RuntimeError(f"binary STL length mismatch: {len(data)} != {expected}")
    dtype = np.dtype(
        [("normal", "<f4", (3,)), ("vertices", "<f4", (3, 3)), ("attribute", "<u2")]
    )
    return np.frombuffer(data, dtype=dtype, count=count, offset=84)["vertices"]


def equal_axes(ax, vertices):
    low = vertices.reshape(-1, 3).min(axis=0)
    high = vertices.reshape(-1, 3).max(axis=0)
    center = (low + high) / 2
    span = (high - low).max() / 2 * 1.08
    ax.set_xlim(center[0] - span, center[0] + span)
    ax.set_ylim(center[1] - span, center[1] + span)
    ax.set_zlim(max(0, center[2] - span), center[2] + span)
    ax.set_box_aspect((1, 1, 1))


def add_mesh(ax, triangles):
    mesh = Poly3DCollection(
        triangles,
        facecolor="#bcc8d6",
        edgecolor="#27384b",
        linewidth=0.035,
        alpha=0.98,
    )
    ax.add_collection3d(mesh)
    equal_axes(ax, triangles)
    ax.set_xlabel("X mm", labelpad=2)
    ax.set_ylabel("Y mm", labelpad=2)
    ax.set_zlabel("Z mm", labelpad=2)
    ax.grid(False)


def main():
    triangles = read_binary_stl(STL)
    fig = plt.figure(figsize=(16, 6), dpi=160, facecolor="white")
    views = ((24, -52, "isometric"), (90, -90, "top / envelope footprint"), (5, -90, "side"))
    for i, (elev, azim, title) in enumerate(views, 1):
        ax = fig.add_subplot(1, 3, i, projection="3d")
        add_mesh(ax, triangles)
        ax.view_init(elev=elev, azim=azim)
        ax.set_title(title, fontsize=11, weight="bold")
    fig.suptitle(
        "HSX cost-down folded trihedral package — visual QA only — NOT FOR FABRICATION",
        fontsize=14,
        weight="bold",
    )
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    PNG.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(PNG, bbox_inches="tight")
    print(PNG)


if __name__ == "__main__":
    main()
