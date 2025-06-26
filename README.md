# Minimum Enclosing Circle (MEC)

Projekt v Pythonu pro výpočet minimálního kruhu opsaného zadaným bodům.

<a href="https://www.youtube.com/watch?v=1UKnY7uTvOI" target="_blank">
  <img src="https://github.com/user-attachments/assets/83f5c01c-4030-4c8a-ab0e-48c14f00c891" alt="Minimum Enclosing Circle" width="500"/>
</a>

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
