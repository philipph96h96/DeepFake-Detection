# Deepfake Detection – Sicherheitsanalyse KI-generierter Gesichtsbilder

Experimentelle Untersuchung, wie zuverlässig bestehende KI-Detektoren echte von KI-generierten Gesichtsbildern unterscheiden und wie JPEG-Kompression, Skalierung und Zuschnitt die Erkennung beeinflussen.

**Projektplanung, Team-Einteilung, Aufgaben und Hintergrund** liegen in Notion (dort pflegen, nicht hier duplizieren):
[Projektseite in Notion](https://app.notion.com/p/3fe47c72611980998addd532ea6e39df)

Dieses Repository enthält nur Code, Konfigurationen, Ergebnisse und den Bericht.

## Struktur

| Ordner | Inhalt |
| --- | --- |
| `data/` | Lokale Bilddaten (nicht versioniert), siehe `data/README.md` |
| `detectors/` | Anbindung der drei Detektoren (CNNDetection, UnivFD, DIRE) |
| `src/` | Datensatz-Auswahl, Bildmanipulationen, Auswertung, Diagramme |
| `experiments/` | Konfiguration pro Versuchslauf |
| `results/` | Tabellen und Diagramme der Läufe |
| `report/` | Bericht und Präsentation |
| `docs/` | Entscheidungen, Quellen, Lizenzen |

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ablauf der Experimente

1. `python -m src.dataset` wählt 100 echte und 100 synthetische Bilder aus (fester Seed).
2. `python -m src.perturbations` erzeugt JPEG-, Skalierungs- und Zuschnitt-Varianten.
3. `python -m src.evaluate` lässt jeden Detektor über Original und Varianten laufen.
4. `python -m src.plots` erzeugt die Ergebnisgraphen in `results/`.

Alle Läufe sind über Seed und Konfiguration in `experiments/` reproduzierbar.

## Konventionen

- Branch pro Aufgabe, Änderungen per Pull Request.
- Jede Entscheidung und jede übernommene Quelle wird in `docs/` festgehalten.
- Keine Bilddaten und keine Modellgewichte einchecken.
