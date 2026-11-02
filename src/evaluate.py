"""Lässt jeden Detektor über Original und Varianten laufen und berechnet Kennzahlen."""
import argparse
import importlib
from pathlib import Path

import pandas as pd
import yaml
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score

IMG_EXT = {".png", ".jpg", ".jpeg"}


def collect(folder: Path) -> tuple[list[str], list[int]]:
    paths, labels = [], []
    for label_name, y in (("real", 0), ("fake", 1)):
        for p in sorted((folder / label_name).glob("*")):
            if p.suffix.lower() in IMG_EXT:
                paths.append(str(p))
                labels.append(y)
    return paths, labels


def metrics(y_true: list[int], scores: list[float], threshold: float = 0.5) -> dict:
    y_pred = [int(s >= threshold) for s in scores]
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred, labels=[0, 1]).ravel()
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "auc": roc_auc_score(y_true, scores),
        "false_positive_rate": fp / (fp + tn) if (fp + tn) else float("nan"),
        "false_negative_rate": fn / (fn + tp) if (fn + tp) else float("nan"),
    }


def main(config_path: Path) -> None:
    cfg = yaml.safe_load(config_path.read_text())
    rows = []
    for det in cfg["detectors"]:
        predict = importlib.import_module(f"detectors.{det}.predict").predict
        for variant in ["original"] + cfg["variants"]:
            folder = Path(cfg["subset_dir"]) if variant == "original" else Path(cfg["perturbed_dir"]) / variant
            paths, y = collect(folder)
            rows.append({"detector": det, "variant": variant, **metrics(y, predict(paths))})
    out = Path(cfg["results_dir"])
    out.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(out / f"{cfg['name']}.csv", index=False)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", type=Path, default=Path("experiments/baseline.yaml"))
    main(ap.parse_args().config)
