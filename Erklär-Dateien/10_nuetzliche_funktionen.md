# Nützliche eingebaute Funktionen

Empfohlene Skills: [Datentypen und Operatoren](01_datentypen_operationen.md), [Kontrollstrukturen](02_kontrollstrukturen.md),
[Listen](04_listen.md) und [Funktionen](09_funktionen.md)

---

Python bietet eine Vielzahl von nützlichen Funktionen, die die Programmierung effizienter gestalten. Hier sind einige der häufigsten und nützlichsten Funktionen:

## `sum()`

Die `sum()`-Funktion berechnet die Summe aller Elemente in einem iterierbaren Objekt (z.B. Liste, Tuple).

### Beispiel:

```python
digits = [1, 2, 3, 4, 5]
sum_of_digits = sum(digits)
print("Die Summe ist:", sum_of_digits)  
```


## `max()`

Die `max()`-Funktion gibt das größte Element in einem iterierbaren Objekt zurück. Bei mehreren Argumenten gibt sie das größte Argument zurück.

### Beispiel:

```python
digits = [1, 2, 3, 4, 5]
biggest_int = max(digits)
print("Die größte Zahl ist:", biggest_int)  
```


## `min()`

Die `min()`-Funktion gibt das kleinste Element in einem iterierbaren Objekt zurück. Bei mehreren Argumenten gibt sie das kleinste Argument zurück.

### Beispiel:

```python
digits = [1, 2, 3, 4, 5]
smallest_digit = min(digits)
print("Die kleinste Zahl ist:", smallest_digit)  
```


## `zip()`

Die `zip()`-Funktion kombiniert mehrere iterierbare Objekte und gibt ein Iterator von Tupeln zurück, wobei 
das i-te Tupel aus den i-ten Elementen der übergebenen iterierbaren Objekte besteht.
Was zunächst verwirrend klingen mag, ist in der Praxis sehr nützlich, um Daten zu kombinieren. In dem folgenden Beispiel
werden zwei Listen kombiniert. Die kombinierte Liste enthält die Tupel `(1, 'a')`, `(2, 'b')` und `(3, 'c')`. Dies
ist nützlich, wenn man beispielsweise eine Liste von Gegenständen und eine Liste von Preisen hat und diese kombinieren möchte.

### Beispiel:

```python
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combined = list(zip(list1, list2))
print("Kombinierte Liste:", combined)
```


## `enumerate()`

Die `enumerate()`-Funktion fügt einem iterierbaren Objekt einen Zähler hinzu und gibt ein Iterator von Tupeln zurück, 
wobei jedes Tupel den Index und das Element enthält. Hierbei handelt es sich um einen Spezialfall von `zip()`, bei dem
der Zähler als Index verwendet wird. `enumerate()` ist eine elegante Möglichkeit, über die Indizes und Elemente einer Liste zu iterieren.
Dadurch ist es nicht notwendig, über die Länge der Liste zu iterieren und manuell auf die Elemente zuzugreifen.

### Beispiel:

```python
my_list = ['a', 'b', 'c']
for index, element in enumerate(my_list):
    print(f"Index: {index}, Wert: {element}")
```


## `filter()`

Die `filter()`-Funktion filtert Elemente aus einem iterierbaren Objekt, basierend auf einer Funktion, die 
True oder False zurückgibt. Nur die Elemente, für die die Funktion True zurückgibt, werden zurückgegeben.

### Beispiel:

```python
digits = [1, 2, 3, 4, 5]
even_digits = list(filter(lambda x: x % 2 == 0, digits))
print("Gerade Zahlen:", even_digits)  
```

Man kann sich das so vorstellen, als ob die Funktion `filter()` die Elemente durchgeht und diejenigen, für die die Funktion `True` zurückgibt, in die neue Liste packt.


## `map()`

Die `map()`-Funktion wendet eine Funktion auf jedes Element eines iterierbaren Objekts an und gibt ein Iterator mit den 
Ergebnissen zurück. Man kann sich das so vorstellen, als ob die Funktion `map()` die Funktion auf jedes Element anwendet und die Ergebnisse in eine neue Liste packt.

### Beispiel:

```python
digits = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, digits))
print("Quadrate:", squares)  
```


## `sorted()`

Die `sorted()`-Funktion gibt eine sortierte Liste der angegebenen iterierbaren Objekte zurück, ohne das Original zu verändern.

### Beispiel:

```python
digits = [5, 2, 3, 1, 4]
sorted_digits = sorted(digits)
print("Sortierte Liste:", sorted_digits)  
```


## `any()`

Die `any()`-Funktion gibt True zurück, wenn mindestens eines der Elemente in einem iterierbaren Objekt True ist. 
Ansonsten gibt sie False zurück.

### Beispiel:

```python
my_list = [False, False, True]
print("Enthält die Liste True?", any(my_list))  
```


## `all()`

Die `all()`-Funktion gibt True zurück, wenn alle Elemente in einem iterierbaren Objekt True sind. Ansonsten gibt sie False zurück.

### Beispiel:

```python
my_list = [True, True, True]
print("Enthält die Liste nur True?", all(my_list))  
```

---

[vorherige Seite](09_funktionen.md)  
[Zurück zum Inhaltsverzeichnis](00_inhaltsverzeichnis.md)  
[nächste Seite](11_rekursion.md)