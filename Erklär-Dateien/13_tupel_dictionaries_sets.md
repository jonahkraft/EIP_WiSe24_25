# Tupel, Dictionaries und Sets

Empfohlene Skills: [Datentypen und Operatoren](01_datentypen_operationen.md) und Grundkenntnisse in [Listen](04_listen.md)

---

In Python gibt es verschiedene Datentypen, die sich für unterschiedliche Aufgaben eignen. In diesem Abschnitt schauen
wir uns die **Tupel**, **Dictionaries** und **Sets** an.


## Tupel

Ein **Tupel** ist eine **unveränderliche** (immutable) Sequenz von Elementen. Das bedeutet, dass die Elemente eines
Tupels nach der Erstellung nicht mehr verändert werden können.

### Syntax:

```python
my_tuple = (1, 2, 3, 4)  # Ein Tupel mit vier Elementen
empty_tuple = ()  # Ein leeres Tupel
one_tuple = (42,)  # Ein Tupel mit einem Element
# Achtung: das Komma ist notwendig, da Python die Klammern sonst für redundant hält und one_tuple den Integerwert 42 zuweist
```

Die Klammern sind nicht notwendig, sofern man kein leeres Tupel erstellen möchte. Die folgenden Schreibweisen sind
daher äquivalent, da ausschließlich das Komma ausschlaggebend ist:

```python
my_tuple = (1, 2, 3)
my_other_tupel = 1, 2, 3
```

### Eigenschaften:

- **Unveränderlich**: Einmal erstellt, kann der Inhalt eines Tupels nicht mehr geändert werden.
- **Indexierbar**: Elemente können über ihre Indizes abgerufen werden.

### Beispiel:

```python
my_tuple = (10, 20, 30)
print(my_tuple[1])  

# Tupel sind unveränderlich, daher führt folgender Code zu einem Fehler:
# mein_tupel[1] = 25  
```

### Operationen mit Tupeln:

| Operation          | Beschreibung                            | Beispiel                           |
|--------------------|-----------------------------------------|------------------------------------|
| `len(tupel)`       | Gibt die Länge des Tupels zurück        | `len((1, 2, 3))` → 3               |
| `tupel[index]`     | Zugriff auf ein Element durch den Index | `(1, 2, 3)[1]` → 2                 |
| `tupel1 + tupel2`  | Verkettet zwei Tupel                    | `(1, 2) + (3, 4)` → `(1, 2, 3, 4)` |
| `tupel * n`        | Wiederholt das Tupel n-mal              | `(1, 2) * 2` → `(1, 2, 1, 2)`      |
| `element in tupel` | Prüft, ob ein Element im Tupel ist      | `2 in (1, 2, 3)` → `True`          |

Die + und * Operationen funktionieren, da nicht das ursprüngliche Tupel verändert wird, sondern es wird ein neues Tupel
erzeugt und zurückgegeben.


## Dictionaries

Ein **Dictionary** (Wörterbuch) in Python speichert **Schlüssel-Wert-Paare**. Es ist eine veränderliche (mutable)
Datenstruktur, in der jedes Element aus einem Schlüssel und einem dazugehörigen Wert besteht.

### Syntax:

```python
my_dict = {'name': 'Max', 'alter': 25}
empty_dict = {}  # Ein leeres Dictionary
```

### Eigenschaften:

- **Schlüssel** müssen unveränderlich sein (z. B. Strings, Zahlen, Tupel).
- **Werte** können beliebige Datentypen sein.
- Die Elemente sind **nicht geordnet**.

### Beispiel:

```python
person = {'name': 'Anna', 'alter': 30, 'stadt': 'Berlin'}
print(person['name'])  

# Wert ändern
person['alter'] = 31
print(person)  

# Neues Schlüssel-Wert-Paar hinzufügen
person['beruf'] = 'Ingenieurin'
```

### Operationen mit Dictionaries:

| Operation                | Beschreibung                                             | Beispiel                                           |
|--------------------------|----------------------------------------------------------|----------------------------------------------------|
| `dict[key]`              | Zugriff auf den Wert, der einem Schlüssel zugeordnet ist | `person['name']` → `'Anna'`                        |
| `dict[key] = value`      | Setzt einen neuen Wert für einen Schlüssel               | `person['alter'] = 31`                             |
| `len(dict)`              | Gibt die Anzahl der Schlüssel-Wert-Paare zurück          | `len(person)` → 3                                  |
| `key in dict`            | Prüft, ob ein Schlüssel im Dictionary vorhanden ist      | `'name' in person` → `True`                        |
| `dict.get(key, default)` | Gibt den Wert für den Schlüssel zurück, oder `default`   | `person.get('beruf', 'unbekannt')` → `'unbekannt'` |
| `dict.keys()`            | Gibt eine Liste aller Schlüssel zurück                   | `person.keys()` → `['name', 'alter', 'stadt']`     |
| `dict.values()`          | Gibt eine Liste aller Werte zurück                       | `person.values()` → `['Anna', 31, 'Berlin']`       |
| `dict.items()`           | Gibt eine Liste aller Schlüssel-Wert-Paare zurück        | `person.items()` → `[('name', 'Anna'), ...]`       |
| `dict.pop(key)`          | Entfernt das Element mit dem Schlüssel `key`             | `person.pop('alter')` → `31`                       |

Achtung: `dict[key]` wirft einen Fehler, wenn der key nicht enthalten ist. dict.get(key, default) ist sicherer.


## Sets

Ein **Set** ist eine ungeordnete Sammlung von **einzigartigen** Elementen. Sets können verwendet werden, um Duplikate zu
entfernen oder Schnittmengen und Vereinigungen von Mengen zu bilden.

### Syntax:

```python
my_set = {1, 2, 3, 4}  # Ein Set mit vier Elementen
empty_set = set()  # Ein leeres Set (Achtung: {} erzeugt ein leeres Dictionary!)
```

### Eigenschaften:

- Elemente in einem Set sind **einzigartig** (keine Duplikate).
- Sets sind **nicht geordnet**, es gibt also keine garantierte Reihenfolge der Elemente.

### Beispiel:

```python
digit_set = {1, 2, 3, 4, 4, 5}  # Doppelte 4 wird automatisch entfernt
print(digit_set) 

# Element hinzufügen
digit_set.add(6)
print(digit_set)

# Element entfernen
digit_set.remove(2)
```

### Operationen mit Sets:

| Operation                       | Beschreibung                                      | Beispiel                                |
|---------------------------------|---------------------------------------------------|-----------------------------------------|
| `len(set)`                      | Gibt die Anzahl der Elemente im Set zurück        | `len({1, 2, 3})` → 3                    |
| `element in set`                | Prüft, ob ein Element im Set ist                  | `2 in {1, 2, 3}` → `True`               |
| `set.add(element)`              | Fügt ein Element zum Set hinzu                    | `zahlen_set.add(6)`                     |
| `set.remove(element)`           | Entfernt ein Element aus dem Set                  | `zahlen_set.remove(2)`                  |
| `set.union(anderes_set)`        | Vereinigung zweier Sets                           | `{1, 2}.union({3, 4})` → `{1, 2, 3, 4}` |
| `set.intersection(anderes_set)` | Schnittmenge zweier Sets                          | `{1, 2}.intersection({2, 3})` → `{2}`   |
| `set.difference(anderes_set)`   | Gibt die Differenzmenge zwischen zwei Sets zurück | `{1, 2}.difference({2, 3})` → `{1}`     |


## Unterschiede zwischen Tupel, Dictionary und Set

| Eigenschaft            | Tupel                      | Dictionary                           | Set                          |
|------------------------|----------------------------|--------------------------------------|------------------------------|
| **Veränderbarkeit**    | Unveränderlich (immutable) | Veränderlich (mutable)               | Veränderlich (mutable)       |
| **Indexierung**        | Ja (über Indizes)          | Nein (Schlüssel)                     | Nein                         |
| **Doppelte Elemente**  | Erlaubt                    | Schlüssel sind eindeutig             | Nur einzigartige Elemente    |
| **Unveränderlichkeit** | Ja                         | Schlüssel müssen unveränderlich sein | Elemente sind unveränderlich |

---

[vorherige Seite](12_backtracking.md)  
[Zurück zum Inhaltsverzeichnis](00_inhaltsverzeichnis.md)  
[nächste Seite](14_dynamische_programmierung.md)