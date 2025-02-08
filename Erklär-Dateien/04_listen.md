# Listen

Empfohlene Skills: [Datentypen und Operatoren](01_datentypen_operationen.md) und [Kontrollstrukturen](02_kontrollstrukturen.md)

---

## Einführung

Listen sind eine der grundlegenden Datentypen in Python. Sie sind geordnete Sammlungen von Elementen, die verschiedene
Datentypen enthalten können (wie Zahlen, Strings oder sogar andere Listen). Listen sind veränderbar (mutable), was
bedeutet, dass Sie ihre Inhalte nach der Erstellung ändern können.

Für Fortgeschrittene: Standardmäßig bietet Python nur dynamischen Listen und keine Arrays wie andere Programmiersprachen.

### Erstellen einer Liste:

```python
my_list = [1, 2, 3, "vier", 5.0]
```

Es ist möglich, Elemente von verschiedenen Datentypen in einer Liste zu haben. Dies ist jedoch nicht empfehlenswert, da
es die Lesbarkeit des Codes beeinträchtigen und zu unerwartetem Verhalten führen kann.

## Operationen mit Listen

Hier sind einige grundlegende Operationen, die Sie mit Listen durchführen können:

| Operation   | Beschreibung                                               | Beispiel                        |
|-------------|------------------------------------------------------------|---------------------------------|
| `append()`  | Fügt ein Element am Ende der Liste hinzu                   | `meine_liste.append(6)`         |
| `insert()`  | Fügt ein Element an einer bestimmten Position ein          | `meine_liste.insert(2, "zwei")` |
| `remove()`  | Entfernt ein Element aus der Liste                         | `meine_liste.remove(3)`         |
| `pop()`     | Entfernt und gibt ein Element an einem Index zurück        | `meine_liste.pop(1)`            |
| `extend()`  | Fügt mehrere Elemente am Ende der Liste hinzu              | `meine_liste.extend([7, 8])`    |
| `index()`   | Gibt den Index des ersten Vorkommens eines Elements zurück | `meine_liste.index("vier")`     |
| `count()`   | Zählt, wie oft ein Element in der Liste vorkommt           | `meine_liste.count(1)`          |
| `sort()`    | Sortiert die Liste in aufsteigender Reihenfolge            | `meine_liste.sort()`            |
| `reverse()` | Kehrt die Reihenfolge der Elemente um                      | `meine_liste.reverse()`         |

Außerdem gibt es die folgenden Funktionen, die im Kontext mit Listen hilfreich sind.

- `len(liste)`: Gibt die Anzahl der Elemente in der Liste zurück.
- `sum(liste)`: Gibt die Summe aller numerischen Elemente in der Liste zurück.

### Beispiel:

```python
digits = [1, 2, 3, 4, 5]
print(len(digits))  
print(sum(digits))  
```

## Indexierung

Listen sind indexiert, was bedeutet, dass man über Indizes auf Werte zugreifen kann. Bei einer Liste mit
n Elementen beginnt die Indexierung bei 0 und endet bei n-1. Man kann auch negative Indizes verwenden, zum Beispiel
liefert der Index -1 das letzte Element (auf negative Indizes wird implizit n addiert).

### Beispiel:

```python
digits = [1, 2, 3, 4, 5]

print(digits[0])
print(digits[-1])

digits[2] = 42
```

## Mit `for`-Schleifen über Listen iterieren

Sie können `for`-Schleifen verwenden, um über die Elemente einer Liste zu iterieren. Anstatt der range()-Funktion ist es
möglich, eine Liste anzugeben, über deren Elemente die Schleife iterieren soll.

### Beispiel:

```python
colors = ["red", "green", "blue"]

for color in colors:
    print(f"Die Farbe ist: {color}")
```

Was ist aber, wenn der Index und das Element an diesem Index benötigt werden?
Natürlich könnte man das mit einer range()-Funktion und dem Zugriff auf die Liste über den Index machen, aber es gibt
die Möglichkeit, das eleganter zu lösen. Die Funktion `enumerate()` löst dieses Problem:

```python
colors = ["red", "green", "blue"]

for index, element in enumerate(colors):
    print(index, element)
```

Man kann enumerate auch einen Startindex übergeben. Das kann so aussehen:

```python
colors = ["red", "green", "blue"]

for index, element in enumerate(colors, start=1):
    print(f"{index}. Farbe: {element}")
```

## Unterschied zwischen mutablen und nicht-mutablen Datentypen

- **Mutable Datentypen**: Diese können nach der Erstellung geändert werden, z.B. Listen. Später kommen noch mehr dazu
- **Immutable Datentypen**: Diese können nach der Erstellung nicht mehr verändert werden. Beispiele sind Strings, ints und floats

### Beispiel für mutablen und nicht-mutablen Datentyp:

```python
# Mutable Datentyp
my_list = [1, 2, 3]
my_list[0] = 100 
print(my_list)  

# Immutable Datentyp
my_string = "Hallo"
# my_string[0] = "h"  # Dies würde einen Fehler verursachen
print(my_string)  
```


## `copy()` und `deepcopy()`

- **`copy()`**: Erstellt eine flache Kopie einer Liste. Änderungen an der kopierten Liste beeinflussen die ursprüngliche
  Liste nicht, solange sich die Elemente in der Liste nicht ändern.

### Beispiel:

```python
original_list = [1, 2, [3, 4]]
flat_copy = original_list.copy()
flat_copy[0] = 100
print(original_list)
```

- **`deepcopy()`**: Erstellt eine tiefe Kopie einer Liste. Änderungen an der tiefen Kopie beeinflussen die ursprüngliche
  Liste nicht, auch wenn die Elemente in der Liste selbst Listen sind.

### Beispiel:

```python
import copy
original_list = [1, 2, [3, 4]]
deep_copy = copy.deepcopy(original_list)
deep_copy[2][0] = 300
print(original_list)
```


## Slicing

Slicing ermöglicht es Ihnen, Teile einer Liste auszuwählen, indem Sie einen bestimmten Bereich von Indizes angeben.

### Syntax:

```python
liste[start:stop:step]
```

### Beispiel:

```python
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Zugriff auf die Elemente von Index 2 bis 5 (5 ist ausgeschlossen)
short_list = digits[2:5]

# Zugriff auf alle Elemente mit Schrittweite 2
half_list = digits[::2]

# Zugriff auf die letzten 3 Elemente
last_elements = digits[-3:] 
```

---

[vorherige Seite](03_math_random_string_module.md)  
[Zurück zum Inhaltsverzeichnis](00_inhaltsverzeichnis.md)  
[nächste Seite](05_matrizen_2d_listen)