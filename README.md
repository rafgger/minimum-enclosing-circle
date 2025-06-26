# Minimum Enclosing Circle (MEC)

Projekt v Pythonu pro výpočet minimálního kruhu opsaného zadaným bodům.

<p align="left">
  <img src="https://github.com/user-attachments/assets/569a85f3-3843-417f-9fc9-746ee79bcad6" alt="Minimum Enclosing Circle" width="500"/>
</p>


## Spuštění

`python -m venv .venv`

`.\.venv\Scripts\activate`

1. Instalace: `pip install .`
2. Spuštění: `python -m minimum_enclosing_circle minimum_enclosing_circle/test_input.json`

volitelny parametr
--plot

## Vstup
JSON soubor s body:
```
{"pnt 1": {"x": 20.4, "y": 12.3}, ...}
```

## Výstup
Textový soubor s poloměrem a středem kruhu.

## Implementace
- Vlastní algoritmus (Welzl)
- Používá numpy, plotly
