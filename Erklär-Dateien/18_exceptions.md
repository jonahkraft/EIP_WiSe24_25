# Exceptions

Empfohlene Skills: [Datentypen und Operatoren](01_datentypen_operationen.md) und [Kontrollstrukturen](02_kontrollstrukturen.md)  
Für eigene Exceptions: Grundlagen in [OOP](15_oop)

---

## Was sind Exceptions?

Exceptions sind Fehler, die während der Programmausführung auftreten. Sie unterbrechen den normalen Fluss eines Programms. 
Python bietet eine Möglichkeit, mit diesen Fehlern umzugehen, damit das Programm nicht abrupt beendet wird.


## Catching Exceptions

Um eine Exception zu fangen, verwendet man den `try`- und `except`-Block. Wenn der Code im `try`-Block einen Fehler verursacht, 
wird der Code im `except`-Block ausgeführt. Es ist wichtig, Exceptions, die möglicherweise auftreten können zu catchen, damit
das Programm nicht abstürzt. In vielen Fällen ist es aber sinnvoller, den Code so zu schreiben, dass eine Exception gar nicht
erst auftreten kann.

### Allgemeine Syntax für `try`-`except`-Blöcke

Die grundlegende Syntax für `try`-`except`-Blöcke in Python sieht folgendermaßen aus:

```python
try:
    # Code, der eine Exception verursachen könnte
    ...
except ExceptionType1:
    # Code für ExceptionType1
    ...
except ExceptionType2:
    # Code für ExceptionType2
    ...
else:
    # Code, der ausgeführt wird, wenn keine Exception auftritt
    ...
finally:
    # Code, der immer ausgeführt wird, unabhängig von einer Exception
    ...
```

### Beispiel:

```python
try:
    result = 10 / 0  # Division durch Null
except ZeroDivisionError:
    print("Fehler: Division durch Null!")
```

Es ist eine gute Praxis, den genauen Fehler anzugeben, z.B. `TypeError` oder `Value Error` und diese einzeln zu catchen.
Man sollte `except Exception` vermeiden!


## Eigene Exceptions erstellen

Man kann eigene Exception-Klassen erstellen, indem man eine Klasse erstellt, die von der `Exception`-Klasse erbt. Diese Klassen können dann wie 
jede andere Exception verwendet werden. Das ist nützlich, wenn man größere Projekte als die Übungsaufgaben entwickelt und
die Standard-Fehlermeldungen nicht ausreichen.

### Beispiel:

```python
class MyException(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return f"MyMessage: {self.message}"
```

---

[vorherige Seite](17_fortgeschrittene_oop)  
[Zurück zum Inhaltsverzeichnis](00_inhaltsverzeichnis.md)