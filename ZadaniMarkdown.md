# Zadání

## Vytvořte projekt, jehož hlavní funkcionalitou je výpočet souřadnic středu a poloměru kruhu, který obsahuje všechny

## body ze vstupního seznamu tak, že ze všech možných má minimální poloměr (minimum enclosing circle - MEC).

## Inspiraci možných řešení lze získat např. na wikipedii.

# Vstupy

## Vstupem je soubor ve formátu JSON, obsahující jednotlivé body. Příklad vstupu:

## Počet bodů ve vstupním souboru není shora ani zdola omezen.

# Výstup

## Formátovaný textový soubor obsahující požadované výpočtené prvky k danému vstupnímu souboru. Příklad

## výstupu

# Omezení

## Implementace výpočtu parametrů MEC musí být vaše vlastní. Je dovoleno využívat knihovny na numerické

## výpočty (jádrová funkcionalita Maltab bez toolboxů, v Pythonu numpy), stejně jako knihovny na práci se soubory a

## tak podobně.

# Hodnocené aspekty implementace

## Ne všechny z těchto aspektů musí úspěšné řešení úlohy splňovat najednou. Pokud jste se v implementaci

## soustředili pouze na některé, uveďte je společně s odevzdáním.

### {

```
"pnt 1 ":{
"x": 20. 4 ,
"y": 12. 3
},
"pnt 2 ":{
"x": 1. 123 ,
"y": 2. 32
},
"pnt 3 ":{
"x": 12. 3 ,
"y": 32. 27
},
"pnt 4 ":{
"x": 0. 987 ,
"y": 87. 43
}
}
```
```
Enclosing circle radius: 12. 123
Enclosing circle center: 3. 23 , 4. 45
```
## korektnost výpočtu, numerická efektivita, ošetření okrajových případů,

## dokumentace, přehlednost a čistota,

## architektura kódu (ať už funkcionálně nebo objektově pojatá),

## otestovanost.


# Jazyk implementace

## Úloha může být řešena v jazyce Matlab nebo Python. Tuto volbu uveďte společně s odevzdáním.

## Matlab

## Výstupem jsou zdrojové kódy ve složce, zahrnuté v projektu po jehož otevření bude veškerá potřebná

## funkcionalita v cestách. Název hlavního spouštěcího skriptu je main.m. Projekt nesmí být závislý na žádném z

## Matlab toolboxů, jinak řečeno musí být využita pouze základní funkcionalita jazyka Matlab. S odevzdáním uveďte

## verzi Matlabu, pod kterou jste vývoj prováděli (např. R2025a).

## V případě potřeby vykreslení bude použita Matlab grafika s využítím doporučené tečkové notace.

## Python

## Výstupem jsou zdrojové kódy ve složce, přičemž projekt musí být instalovatelný pomocí pip podle specifikace v

## souboru pyproject.toml. V ideálním případe by modul s implementací měl být spustitelný z příkazové řádky

## (přepínač -m) s jedním vstupním argumentem, a to cestou ke vstupnímu JSON souboru.

## Je možné využít standardní knihovnu. Z knihoven třetích stran lze využít numpy, scipy a v případě

## implementace vykreslení plotly.

# Očekávaná náročnost

## Tvorba implementace by neměla zabrat více než jedno odpoledne. S touto časovou dotací se počítá, dle toho je

## také očekávaný rozsah a hloubka implementace. Projekt nemusí být kompletní, nicméně musí obsahovat alespoň

## některé funkční dílčí části.

## Pokud uznáte za vhodné, můžete k odevzdání připojit stručný (do rozsahu jedné A4 strany) popis procesu

## implementace, např. které části byly náročné nebo zabraly velké množství času a proč.


