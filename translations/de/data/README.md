# data/
 
> [English (primary)](../../../data/README.md) · [Русский](../../ru/data/README.md) · Deutsch

Rohmessungsprotokolle: CSV- und PNG-Ausgaben von `software/sweep-map/sweep_map.py`.

- Dateinamen enthalten einen UTC-Timestamp: `sweep_25000-45000_20260801T120000Z.csv`.
- CSV/PNG-Dateien bleiben aus git heraus (siehe `.gitignore`) — sie sind groß und reproduzierbar; nur die kuratierten Plots werden in git aufgenommen und in das entsprechende Experimentverzeichnis `experiments/NNN-*/` kopiert.

Mock-Modus-Läufe (`sweep_map.py --mock`) schreiben hier auch hin — diese Dateien können jederzeit gelöscht werden.
