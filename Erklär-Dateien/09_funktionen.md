# Funktionen

Empfohlene Skills: [Datentypen und Operatoren](01_datentypen_operationen.md), [Kontrollstrukturen](02_kontrollstrukturen.md), [Listen](04_listen.md) und später (nicht zwingend erforderlich) [Tupel und Dictionaries](13_tupel_dictionaries_sets.md)

---

Funktionen sind in Python ein zentrales Konzept, um Code in wiederverwendbaren Blöcken zu organisieren. 
Eine Funktion kann Parameter annehmen, eine Aufgabe ausführen und einen Wert zurückgeben. Man kann sie sich wie eine
Fabrik vorstellen. Man gibt Ressourcen herein und bekommt ein Endprodukt.


## `return`

Das Schlüsselwort `return` wird verwendet, um das Ergebnis einer Funktion zurückzugeben. 
Wenn eine Funktion kein `return`-Statement enthält, gibt sie automatisch `None` zurück. Dabei handelt es sich um
einen besonderen Datentyp, der das Fehlen eines Wertes darstellt.

### Syntax:

```python
def function_name():
    # Code der Funktion
    return wert
```

### Beispiel:

```python
def add_digits(a, b):
    return a + b

result = add_digits(3, 4)
print(result)  
```

In diesem Beispiel nimmt die Funktion `add_digits` zwei Parameter (`a` und `b`), berechnet deren Summe und gibt 
das Ergebnis mit `return` zurück.

Mit `return` kann man ein Objekt zurückgeben. Daher stellt sich die Frage, wie man vorgehen kann, wenn man mehrere Objekte
wie etwa einen int und einen bool zurückgeben möchte. Dies lässt sich realisieren, indem man alle Werte, die zurückgegeben
werden sollen, in ein Tupel packt. Tupel sind vereinfacht gesagt unveränderliche Listen. [Hier](13_tupel_dictionaries_sets.md) können
Sie mehr darüber erfahren.

### Beispiel

```python
def func(a):
    even = a % 2 == 0
    half = a // 2
    return even, half

my_int = 10
is_even, half = func(my_int)
```

Hierbei werden die beiden Variablen beim `return` in ein Tupel verpackt, das in der untersten Zeile wieder entpackt wird.
Dabei bekommt `is_even` den Wert am Index 0 des Tupels und `half` den Wert am Index 1 des Tupels.

## Parameterliste

Funktionen können eine beliebige Anzahl von Parametern haben. Diese Parameter werden als Eingaben für die Funktion verwendet. 

### Syntax:

```python
def function_name(param1, param2, ...):
    ...
    # Code der Funktion
```

### Beispiel:

```python
def multiply(a, b, c):
    return a * b * c

result = multiply(2, 3, 4)
print(result)  
```

In diesem Beispiel nimmt die Funktion `multiply` drei Parameter (`a`, `b`, `c`) und multipliziert sie miteinander. Das
Ergebnis wird anschließend zurückgegeben.


## Call by Reference

Python verwendet für veränderbare (mutable) Objekte eine **Call by Reference**-Semantik, was bedeutet, dass 
Änderungen an Objekten innerhalb einer Funktion auch außerhalb der Funktion sichtbar sind. 
Für unveränderbare (immutable) Objekte wird **Call by Value**-ähnlich gearbeitet.

Zur Erinnerung:  
`int`, `float`, `str`, `bool` sind unveränderlich (auch die eben kurz erwähnten Tupel).  
Listen sind veränderlich.

### Beispiel (mit einer Liste, einem veränderbaren Datentyp):

```python
def append_element(a):
    a.append(4)

my_list = [1, 2, 3]
append_element(my_list)
print(my_list)  
```

In diesem Beispiel wird das Argument `my_list` als Referenz übergeben, und die Funktion `append_element` ändert die ursprüngliche Liste.

### Beispiel (mit einem unveränderbaren Datentyp):

```python
def add_one(x):
    x += 1

digit = 5
add_one(digit)
print(digit)
```

In diesem Beispiel wird `digit` nicht verändert, weil Ganzzahlen unveränderbare (immutable) Datentypen sind.


## Standardwerte für Parameter

Man kann Standardwerte für Funktionsparameter definieren. Wenn der Parameter beim Funktionsaufruf nicht angegeben wird, 
wird der Standardwert verwendet.

### Syntax:

```python
def function_name(param1=standardwert):
    ...
    # Code der Funktion
```

### Beispiel:

```python
def greeting(name="Welt"):
    print(f"Hallo, {name}!")


greeting("Rick Astley")
greeting()         
```

In diesem Beispiel hat der Parameter `name` einen Standardwert `"Welt"`. Wenn kein Argument übergeben wird, 
wird dieser Standardwert verwendet.


## Lambda-Funktionen

Lambda-Funktionen sind anonyme, kleine Funktionen, die mit dem Schlüsselwort `lambda` definiert werden. 
Sie sind nützlich für kurze, einmalige Operationen. Funktionen können auch Funktionen als Parameter übergeben bekommen.
Hier sind lambda-Funktionen sinnvoll. Sie können aber die Lesbarkeit des Codes einschränken, weshalb man sie nicht 
inflationär verwenden sollte.

### Syntax

```python
lambda argumente: ausdruck
```

### Beispiele

1. Einfache Addition:

```python
sum_ = lambda a, b: a + b
print(sum_(3, 5)) 
```

2. Mit `filter()`:

```python
digits = [1, 2, 3, 4, 5]
even_digits = list(filter(lambda x: x % 2 == 0, digits))
print(even_digits)  
```

In diesem Beispiel wird die Lambda-Funktion verwendet, um nur die geraden Zahlen aus der Liste `digits` zu filtern.
Wenn Ihnen filter() noch nicht bekannt ist, finden Sie eine Erklärung in der [Datei zu nützlichen Funktionen](10_nuetzliche_funktionen.md).


## `*args`

`*args` ermöglicht es, eine variable Anzahl von Positionsargumenten an eine Funktion zu übergeben. 
Die Argumente werden in einem Tupel [(siehe Datei zu Tupeln)](13_tupel_dictionaries_sets.md) gesammelt, das innerhalb der Funktion verwendet werden kann.

### Beispiel:

```python
def example_args(*args):
    print(args)

example_args(1, 2, 3, 4)
```

Hier nimmt die Funktion eine beliebige Anzahl von Argumenten an und gibt sie als Tupel aus.

### Beispiel mit Schleife:

```python
def calculate_sum(*args):
    return sum(args)

print(calculate_sum(1, 2, 3))
```


## `**kwargs`

`**kwargs` ermöglicht es, eine variable Anzahl von benannten Argumenten (Keyword Arguments) zu übergeben. 
Diese werden in einem Dictionary [(siehe Datei zu Dictionaries)](13_tupel_dictionaries_sets.md) gesammelt.

### Beispiel:

```python
def example_kwargs(**kwargs):
    print(kwargs)

example_kwargs(a=1, b=2, c=3)
```

In diesem Beispiel wird die Funktion `example_kwargs` mit drei benannten Argumenten aufgerufen. Das Dictionary `kwargs`
enthält die Schlüssel-Wert-Paare `{'a': 1, 'b': 2, 'c': 3}`.


### Beispiel mit Zugriff auf Schlüssel und Werte:

```python
def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(first_name="Max", last_name="Mustermann")
```

---

[vorherige Seite](08_os_modul.md)  
[Zurück zum Inhaltsverzeichnis](00_inhaltsverzeichnis.md)  
[nächste Seite](10_nuetzliche_funktionen.md)