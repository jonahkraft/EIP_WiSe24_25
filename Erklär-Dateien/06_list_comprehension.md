# List Comprehension

Empfohlene Skills: [Datentypen und Operatoren](01_datentypen_operationen.md), [Kontrollstrukturen](02_kontrollstrukturen.md) und [Listen](04_listen.md)

---

Beginnen wir mit einem Beispiel.
Wenn ich eine Liste haben will, in der zehnmal die Zahl 0 steht, kann ich das so machen.

## Herleitung

```python
list1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

Das ist insbesondere bei grossen Listen nervig und dauert lang, weil hardgecoded.
Es gibt aber auch die folgende Möglichkeit:

```python
list2 = []
for _ in range(10):
    list2.append(0)
```

Das ist schon cooler, aber ich wuerde es gerne noch besser machen. Man kann dasselbe auch in einer Zeile schreiben.

```python
list3 = [0 for _ in range(10)]
```

Das ist dann List Comprehension. Was passiert hier? Bei einer "normalen" for-Schleife wie oben, schreibt man erst
den Schleifenkopf "for _ in range(10):" und dann, was passieren soll. Wenn man eine for-Schleife in eine Liste packt,
schreibt man zuerst, was man hinzufügen will - in dem Fall die Zahl 0 - und dann den Schleifenkopf, aber ohne den
Doppelpunkt. Das ist schon die ganze Magie.

---

## Einige Beispiele

### Ein komplexeres Beispiel

Zuerst erstelle ich eine Liste, in der ich 10 zufaellige Zahlen zwischen 1 und 10 haben will. Mit List Comprehension
geht das so:

```python
import random
random_numbers = [random.randint(1, 10) for _ in range(10)]
```

Jetzt wuerde ich gerne alle Zahlen aus random_numbers, die groesser als 5 sind, in eine neue Liste packen.
Ohne List Comprehension geht das so:

```python
big_numbers1 = []

for i in random_numbers:
    if i > 5:
        big_numbers1.append(i)
```

Man kann auch if-Statements in List Comprehensions packen. Das geht analog zu den for-Schleifen.

```python
big_numbers2 = [i for i in random_numbers if i > 5]
```

---

### Verschachtelte Schleifen

Probieren wir etwas anderes aus. Man kann auch mehrere Schleifen ineinander verschachteln.
Dieses Beispiel erstellt eine 5 x 5 Matrix, bei der in jedem Eintrag 0 steht.

```python
matrix = [[0 for _ in range(5)] for _ in range(5)]
```

Probieren wir etwas anderes aus. Ich hätte gerne eine 5 x 5 Matrix, bei der in jedem Eintrag steht, ob die Summe aus
Zeilen- und Spaltenindex gerade ist.

```python
matrix2 = [[(i+j) % 2 == 0 for i in range(5)] for j in range(5)]
# (i+j) % 2 == 0 ist bereits ein boolescher Wert
```

Zum Schluss kommt noch ein komplexeres Beispiel. Zuerst erstelle ich 2 Listen mit je 10 zufälligen Zahlen wie oben.
Dann möchte ich eine neue Liste haben, die alle geordneten Paare von Zahlen aus den beiden Listen enthaelt, deren
Summe durch drei teilbar ist.

```python
import random
random_numbers1 = [random.randint(1, 10) for _ in range(10)]
random_numbers2 = [random.randint(1, 10) for _ in range(10)]

result = [(i, j)
          for i in random_numbers1
          for j in random_numbers2
          if (i+j) % 3 == 0
          ]
```

---

[vorherige Seite](05_2d_listen.md)  
[Zurück zum Inhaltsverzeichnis](00_inhaltsverzeichnis.md)  
[nächste Seite](07_dateien.md)