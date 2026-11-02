"""Stellt das Testset zusammen: n echte und n synthetische Bilder (fester Seed)."""
import argparse
import random
import shutil
from pathlib import Path

IMG_EXT = {".png", ".jpg", ".jpeg"}


def list_images(folder: Path) -> list[Path]:
    return sorted(p for p in folder.rglob("*") if p.suffix.lower() in IMG_EXT)


def build_subset(real_dir: Path, fake_dir: Path, out_dir: Path, n: int, seed: int) -> None:
    rng = random.Random(seed)
    for label, src in (("real", real_dir), ("fake", fake_dir)):
        images = list_images(src)
        if len(images) < n:
            raise ValueError(f"{src}: nur {len(images)} Bilder, benötigt {n}")
        target = out_dir / label
        target.mkdir(parents=True, exist_ok=True)
        for img in rng.sample(images, n):
            shutil.copy2(img, target / img.name)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--real", type=Path, default=Path("data/raw/ffhq"))
    ap.add_argument("--fake", type=Path, default=Path("data/raw/sfhq"))
    ap.add_argument("--out", type=Path, default=Path("data/subset"))
    ap.add_argument("--n", type=int, default=100)
    ap.add_argument("--seed", type=int, default=42)
    a = ap.parse_args()
    build_subset(a.real, a.fake, a.out, a.n, a.seed)
