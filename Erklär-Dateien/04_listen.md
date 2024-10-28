# Listen

Empfohlene Skills: [Datentypen und Operatoren](01_datentypen_operationen.md) und [Kontrollstrukturen](02_kontrollstrukturen.md)

---

## Einführung

Listen sind eine der grundlegenden Datentypen in Python. Sie sind geordnete Sammlungen von Elementen, die verschiedene
Datentypen enthalten können (wie Zahlen, Strings oder sogar andere Listen). Listen sind veränderbar (mutable), was
bedeutet, dass du ihre Inhalte nach der Erstellung ändern kannst.

### Erstellen einer Liste:

```python
my_list = [1, 2, 3, "vier", 5.0]
```


## Operationen mit Listen

Hier sind einige grundlegende Operationen, die du mit Listen durchführen kannst:

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
print(len(digits))  # Ausgabe: 5
print(sum(digits))  # Ausgabe: 15
```


## Mit `for`-Schleifen über Listen iterieren

Du kannst `for`-Schleifen verwenden, um über die Elemente einer Liste zu iterieren. Anstatt der range()-Funktion kannst
du auch eine Liste angeben, über deren Elemente die Schleife iterieren soll.

### Beispiel:

```python
colors = ["red", "green", "blue"]

for color in colors:
    print(f"Die Farbe ist: {color}")
```

Was ist aber, wenn ich den Index und das Element an diesem Index brauche?
Die Funktion enumerate löst dieses Problem. Sie lässt sich folgendermaßen benutzen:

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
my_list[0] = 100  # Änderungen sind erlaubt
print(my_list)  # Ausgabe: [100, 2, 3]

# Immutable Datentyp
my_string = "Hallo"
# my_string[0] = "h"  # Dies würde einen Fehler verursachen
print(my_string)  # Ausgabe: "Hallo"
```


## `copy()` und `deepcopy()`

- **`copy()`**: Erstellt eine flache Kopie einer Liste. Änderungen an der kopierten Liste beeinflussen die ursprüngliche
  Liste nicht, solange sich die Elemente in der Liste nicht ändern.

### Beispiel:

```python
original_list = [1, 2, [3, 4]]
flat_copy = original_list.copy()
flat_copy[0] = 100
print(original_list)  # Ausgabe: [1, 2, [3, 4]]
```

- **`deepcopy()`**: Erstellt eine tiefe Kopie einer Liste. Änderungen an der tiefen Kopie beeinflussen die ursprüngliche
  Liste nicht, auch wenn die Elemente in der Liste selbst Listen sind.

### Beispiel:

```python
import copy
original_list = [1, 2, [3, 4]]
deep_copy = copy.deepcopy(original_list)
deep_copy[2][0] = 300
print(original_list)  # Ausgabe: [1, 2, [3, 4]]
```


## Slicing

Slicing ermöglicht es dir, Teile einer Liste auszuwählen, indem du einen bestimmten Bereich von Indizes angibst.

### Syntax:

```python
liste[start:stop:step]
```

### Beispiel:

```python
zahlen = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Zugriff auf die Elemente von Index 2 bis 5 (5 ist ausgeschlossen)
short_list = zahlen[2:5]  # Ausgabe: [2, 3, 4]

# Zugriff auf alle Elemente mit Schrittweite 2
half_list = zahlen[::2]  # Ausgabe: [0, 2, 4, 6, 8]

# Zugriff auf die letzten 3 Elemente
last_elements = zahlen[-3:]  # Ausgabe: [7, 8, 9]
```

---

[vorherige Seite](03_math_random_string_module.md)  
[Zurück zum Inhaltsverzeichnis](00_inhaltsverzeichnis.md)  
[nächste Seite](05_2d_listen.md)