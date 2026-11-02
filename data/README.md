# Daten

Bilddaten werden nicht eingecheckt. Lokal diese Struktur anlegen:

```
data/
├── raw/
│   ├── ffhq/      # echte Gesichter
│   ├── sfhq/      # vollständig synthetische Gesichter
│   └── hidf/      # echte und Face-Swap-Fälschungen
├── subset/        # 100 echt + 100 synthetisch (von src/dataset.py erzeugt)
└── perturbed/     # JPEG-, Skalierungs- und Zuschnitt-Varianten
```

## Quellen

- FFHQ: https://github.com/NVlabs/ffhq-dataset
- SFHQ: https://github.com/SelfishGene/SFHQ-dataset
- HiDF: https://github.com/DSAIL-SKKU/HiDF

SFHQ (voll synthetisch) und HiDF (Face-Swap) werden getrennt ausgewertet.
Nutzungsbedingungen und Datenschutz vor dem Download prüfen und in `docs/lizenzen.md` festhalten.
