## Binario

[Binairo](https://de.puzzle-binairo.com) wird auf einem rechteckigem Feld gespielt. Einige Felder sind bereits mit schwarzen bzw. 
weißen Kreisen gefüllt, die restlichen sind leer. Das Ziel ist es alle Felder mit Kreisen zu befüllen, sodass:

1. jede Zeile/Spalte die gleiche Anzahl an schwarzen und weißen Kreisen enthält.
2. nie mehr als zwei Kreise derselben Farbe aufeinander folgen.
3. jede Zeile/Spalte einzigartig ist.

Wir gehen davon aus, dass Spielfelder quadratisch sind. Ignoriere die 3. Regel und löse Binario mit
Backtracking.

In der Datei [binario.py](../resources/binario.py) finden Sie bereits Spielfelder für Ihren Code.

[Hier](../Muster/Backtracking/backtracking_binario.py) finden Sie die Musterlösung.


## Quadrate

In der Liste [8, 1, 15, 10, 6, 3, 13, 12, 4, 5, 11, 14, 2, 7, 9] sind die Zahlen 1-15 so angeordnet, dass immer die 
Summe von 2 aufeinander folgende Zahlen eine Quadratzahl ist. Wir wollen jetzt eine Liste der Zahlen 7-31 so anordnen, 
dass hier diese Eigenschaft erfüllt ist.

Aufgabe 1: Eine naive Möglichkeit wäre es, alle Möglichkeiten auszuprobieren. 
Warum ist das kein sinnvoller Ansatz?

Aufgabe 2: Lösen Sie das Problem mit Backtracking, indem Sie die naive Idee so verändern, dass nicht mehr alle Möglichkeiten
geprüft werden müssen und Sie in Sekundenschnelle 2 Lösungen finden.

[Hier](../Muster/Backtracking/backtracking_squares.py) finden Sie die Musterlösung.
