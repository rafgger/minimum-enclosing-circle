# Architektura projektu Minimum Enclosing Circle (MEC)

Tento projekt slouží k nalezení minimálního kruhu, který obsahuje všechny zadané body v rovině. Je napsán v Pythonu a je vhodný i pro začátečníky.

## Struktura projektu

```
minimum_enclosing_circle/
├── __init__.py           # Označuje složku jako Python balíček
├── __main__.py           # Hlavní spustitelný skript (CLI rozhraní)
├── mec.py                # Výpočet minimálního kruhu a vizualizace
├── utils.py              # Načítání a ukládání dat (JSON, výstup)
├── test_input.json       # Ukázkový vstupní soubor
├── README.md             # Základní popis použití
├── ARCHITEKTURA.md       # Tento dokument
└── ...
pyproject.toml            # Konfigurační soubor pro instalaci
```

## Hlavní soubory a jejich role

### 1. `__main__.py`
- Umožňuje spustit projekt z příkazové řádky (`python -m minimum_enclosing_circle ...`).
- Načte vstupní body, spočítá kruh, uloží výsledek a případně vytvoří vizualizaci.
- Lze přidat argument `--plot` pro uložení grafu do HTML.

### 2. `mec.py`
- Obsahuje hlavní algoritmus pro výpočet minimálního opsaného kruhu (Welzlův algoritmus).
- Funkce `minimum_enclosing_circle(points)` vrací střed a poloměr kruhu.
- Funkce `plot_circle(points, center, radius, out_path)` vytvoří vizualizaci pomocí knihovny plotly.

### 3. `utils.py`
- Pomocné funkce pro načítání bodů ze vstupního JSON a ukládání výsledků do textového souboru.

### 4. `pyproject.toml`
- Umožňuje instalaci projektu přes pip a definuje závislosti (numpy, plotly).

## Jak to funguje krok za krokem

1. **Načtení bodů**: Ze zadaného JSON souboru se načtou souřadnice bodů.
2. **Výpočet kruhu**: Algoritmus najde nejmenší možný kruh, který všechny body obsahuje.
3. **Uložení výsledku**: Výsledek (střed a poloměr) se uloží do textového souboru.
4. **Vizualizace (volitelné)**: Pokud zadáte `--plot`, vytvoří se HTML s grafem bodů a kruhu.

## Jak projekt spustit

1. Vytvořte a aktivujte virtuální prostředí:
   ```
   python -m venv .venv
   .\.venv\Scripts\activate
   ```
2. Nainstalujte projekt:
   ```
   pip install .
   ```
3. Spusťte výpočet:
   ```
   python -m minimum_enclosing_circle minimum_enclosing_circle/test_input.json --plot
   ```
   Výsledky najdete v textovém souboru a vizualizaci v HTML.

## Proč je kód rozdělen takto?
- **Přehlednost**: Každý soubor má jasnou roli.
- **Znovupoužitelnost**: Algoritmus i vizualizace lze použít i v jiných projektech.
- **Snadné testování**: Funkce lze snadno otestovat samostatně.

## Co je Welzlův algoritmus?
Je to efektivní metoda pro nalezení minimálního kruhu obsahujícího všechny body. Pracuje rekurzivně a náhodně vybírá body, což zajišťuje rychlý výpočet i pro větší množství bodů.

## Závislosti
- `numpy` – rychlé výpočty s čísly
- `plotly` – interaktivní grafy (pouze pro vizualizaci)
- standardní knihovny Pythonu (json, sys, ...)

---

Pokud si s něčím nevíte rady, podívejte se do README nebo se ptejte!
