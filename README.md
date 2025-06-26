# Minimum Enclosing Circle (MEC)

Projekt v Pythonu pro výpočet minimálního kruhu opsaného zadaným bodům.


[![Minimum Enclosing Circle](https://img.youtube.com/vi/1UKnY7uTvOI/0.jpg)](https://www.youtube.com/watch?v=1UKnY7uTvOI)





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
