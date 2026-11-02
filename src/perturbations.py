"""Bildmanipulationen: JPEG-Kompression, Skalierung, Zuschnitt."""
import argparse
from pathlib import Path

from PIL import Image

JPEG_QUALITIES = [90, 70, 50, 30]
SCALES = [0.75, 0.5, 0.25]
CROPS = [0.9, 0.75, 0.5]  # Anteil der Kantenlänge, zentriert


def jpeg(img: Image.Image, q: int, path: Path) -> None:
    img.convert("RGB").save(path.with_suffix(".jpg"), quality=q)


def scale(img: Image.Image, f: float, path: Path) -> None:
    img.resize((int(img.width * f), int(img.height * f)), Image.BICUBIC).save(path)


def crop(img: Image.Image, f: float, path: Path) -> None:
    w, h = img.size
    cw, ch = int(w * f), int(h * f)
    left, top = (w - cw) // 2, (h - ch) // 2
    img.crop((left, top, left + cw, top + ch)).save(path)


def run(src: Path, out: Path) -> None:
    for img_path in sorted(src.rglob("*")):
        if img_path.suffix.lower() not in {".png", ".jpg", ".jpeg"}:
            continue
        label = img_path.parent.name
        img = Image.open(img_path)
        variants = (
            [(f"jpeg_q{q}", lambda p, q=q: jpeg(img, q, p)) for q in JPEG_QUALITIES]
            + [(f"scale_{f}", lambda p, f=f: scale(img, f, p)) for f in SCALES]
            + [(f"crop_{f}", lambda p, f=f: crop(img, f, p)) for f in CROPS]
        )
        for name, fn in variants:
            target = out / name / label
            target.mkdir(parents=True, exist_ok=True)
            fn(target / img_path.name)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", type=Path, default=Path("data/subset"))
    ap.add_argument("--out", type=Path, default=Path("data/perturbed"))
    a = ap.parse_args()
    run(a.src, a.out)
