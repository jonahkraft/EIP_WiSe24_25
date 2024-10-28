# Nützliche eingebaute Funktionen

Empfohlene Skills: [Datentypen und Operatoren](01_datentypen_operationen.md), [Kontrollstrukturen](02_kontrollstrukturen.md),
[Listen](04_listen.md) und [Funktionen](09_funktionen.md)

---

Python bietet eine Vielzahl von nützlichen Funktionen, die die Programmierung effizienter gestalten. Hier sind einige der häufigsten und nützlichsten Funktionen:

## `sum()`

Die `sum()`-Funktion berechnet die Summe aller Elemente in einem iterierbaren Objekt (z.B. Liste, Tuple).

### Beispiel:

```python
zahlen = [1, 2, 3, 4, 5]
gesamt = sum(zahlen)
print("Die Summe ist:", gesamt)  # Ausgabe: 15
```


## `max()`

Die `max()`-Funktion gibt das größte Element in einem iterierbaren Objekt zurück. Bei mehreren Argumenten gibt sie das größte Argument zurück.

### Beispiel:

```python
zahlen = [1, 2, 3, 4, 5]
groesste_zahl = max(zahlen)
print("Die größte Zahl ist:", groesste_zahl)  # Ausgabe: 5
```


## `min()`

Die `min()`-Funktion gibt das kleinste Element in einem iterierbaren Objekt zurück. Bei mehreren Argumenten gibt sie das kleinste Argument zurück.

### Beispiel:

```python
digits = [1, 2, 3, 4, 5]
smallest_digit = min(digits)
print("Die kleinste Zahl ist:", smallest_digit)  # Ausgabe: 1
```


## `zip()`

Die `zip()`-Funktion kombiniert mehrere iterierbare Objekte und gibt ein Iterator von Tupeln zurück, wobei 
das i-te Tupel aus den i-ten Elementen der übergebenen iterierbaren Objekte besteht.

### Beispiel:

```python
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combined = list(zip(list1, list2))
print("Kombinierte Liste:", combined)  # Ausgabe: [(1, 'a'), (2, 'b'), (3, 'c')]
```


## `enumerate()`

Die `enumerate()`-Funktion fügt einem iterierbaren Objekt einen Zähler hinzu und gibt ein Iterator von Tupeln zurück, 
wobei jedes Tupel den Index und das Element enthält.

### Beispiel:

```python
my_list = ['a', 'b', 'c']
for index, element in enumerate(my_list):
    print(f"Index: {index}, Wert: {element}")
# Ausgabe: 
# Index: 0, Wert: a
# Index: 1, Wert: b
# Index: 2, Wert: c
```


## `filter()`

Die `filter()`-Funktion filtert Elemente aus einem iterierbaren Objekt, basierend auf einer Funktion, die 
True oder False zurückgibt. Nur die Elemente, für die die Funktion True zurückgibt, werden zurückgegeben.

### Beispiel:

```python
digits = [1, 2, 3, 4, 5]
even_digits = list(filter(lambda x: x % 2 == 0, digits))
print("Gerade Zahlen:", even_digits)  # Ausgabe: [2, 4]
```


## `map()`

Die `map()`-Funktion wendet eine Funktion auf jedes Element eines iterierbaren Objekts an und gibt ein Iterator mit den 
Ergebnissen zurück.

### Beispiel:

```python
digits = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, digits))
print("Quadrate:", squares)  # Ausgabe: [1, 4, 9, 16, 25]
```


## `sorted()`

Die `sorted()`-Funktion gibt eine sortierte Liste der angegebenen iterierbaren Objekte zurück, ohne das Original zu verändern.

### Beispiel:

```python
digits = [5, 2, 3, 1, 4]
sorted_digits = sorted(digits)
print("Sortierte Liste:", sorted_digits)  # Ausgabe: [1, 2, 3, 4, 5]
```


## `any()`

Die `any()`-Funktion gibt True zurück, wenn mindestens eines der Elemente in einem iterierbaren Objekt True ist. 
Ansonsten gibt sie False zurück.

### Beispiel:

```python
my_list = [False, False, True]
print("Enthält die Liste True?", any(my_list))  # Ausgabe: True
```


## `all()`

Die `all()`-Funktion gibt True zurück, wenn alle Elemente in einem iterierbaren Objekt True sind. Ansonsten gibt sie False zurück.

### Beispiel:

```python
my_list = [True, True, True]
print("Enthält die Liste nur True?", all(my_list))  # Ausgabe: True
```

---

[vorherige Seite](09_funktionen.md)  
[Zurück zum Inhaltsverzeichnis](00_inhaltsverzeichnis.md)  
[nächste Seite](11_rekursion.md)