# Detektoren

Jeder Detektor bekommt einen Unterordner mit einem Wrapper `predict.py`, der einheitlich arbeitet:

```python
def predict(image_paths: list[str]) -> list[float]:
    """Gibt pro Bild die Wahrscheinlichkeit zurück, dass es KI-generiert ist."""
```

| Ordner | Verfahren | Quelle |
| --- | --- | --- |
| `cnndetection/` | CNNDetection (2020) | https://github.com/PeterWang512/CNNDetection |
| `univfd/` | UniversalFakeDetect / UnivFD (2023) | https://github.com/lynote-ai/ai-image-detector |
| `dire/` | DIRE (2023) | https://github.com/ZhendongWang6/DIRE |

Gewichte gehören nach `detectors/<name>/weights/` und werden nicht eingecheckt.
Verwendete Version, Commit und Lizenz jedes Detektors in `docs/quellen.md` eintragen.
