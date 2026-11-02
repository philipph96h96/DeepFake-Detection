"""Erzeugt Ergebnisgraphen aus den CSV-Dateien in results/."""
import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def plot_metric(df: pd.DataFrame, metric: str, out: Path) -> None:
    pivot = df.pivot(index="variant", columns="detector", values=metric)
    ax = pivot.plot(kind="bar", figsize=(9, 5))
    ax.set_ylabel(metric)
    ax.set_ylim(0, 1)
    ax.set_title(f"{metric} pro Detektor und Bildvariante")
    plt.tight_layout()
    plt.savefig(out / f"{metric}.png", dpi=200)
    plt.close()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", type=Path, default=Path("results/baseline.csv"))
    ap.add_argument("--out", type=Path, default=Path("results"))
    a = ap.parse_args()
    df = pd.read_csv(a.csv)
    for m in ("accuracy", "auc", "false_positive_rate", "false_negative_rate"):
        plot_metric(df, m, a.out)
