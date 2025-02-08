# Fortgeschrittene OOP

Empfohlene Skills: [Datentypen und Operatoren](01_datentypen_operationen.md), [Kontrollstrukturen](02_kontrollstrukturen.md),
[Funktionen](09_funktionen.md) und [OOP](15_oop)

---

## @staticmethod

Eine `@staticmethod` ist eine Methode, die innerhalb einer Klasse definiert ist, aber keinen Zugriff auf die Instanz (`self`) 
oder die Klasse (`cls`) hat. Sie verhält sich wie eine normale Funktion, die in den Namensraum der Klasse eingeschlossen ist.

### Syntax:

```python
class MyClass:
    @staticmethod
    def my_method(parameter):
        ...
```

### Beispiel:

```python
class Math:
    @staticmethod
    def add(x, y):
        return x + y

print(Math.add(5, 3))  
```


## @classmethod

Eine `@classmethod` ist eine Methode, die Zugriff auf die Klasse (`cls`) hat, aber nicht auf die Instanz (`self`). 
Sie kann beispielsweise verwendet werden, um auf Klassenattribute zuzugreifen oder diese zu verändern.

### Syntax:

```python
class MyClass:
    @classmethod
    def my_method(cls, parameter):
        ...
```

### Beispiel:

```python
class Circle:
    pi = 3.14

    @classmethod
    def calculate_area(cls, radius):
        return cls.pi * (radius ** 2)
```

Bemerkung: pi ist ein Klassenattribut, das von allen Instanzen der Klasse Circle geteilt wird. Daher wird es nicht
über `self` sondern über `cls` aufgerufen.

## Abstrakte Klassen

Eine abstrakte Klasse ist eine Klasse, die nicht instanziiert werden kann und dazu dient, eine Basis für andere Klassen 
zu schaffen. Abstrakte Klassen enthalten oft abstrakte Methoden, die in den abgeleiteten Klassen implementiert werden müssen.
Sie dienen dazu, sicherzustellen, dass bestimmte Funktionalitäten in den Unterklassen vorhanden sind.

## @abstractmethod

Eine `@abstractmethod` ist eine Methode, die in einer abstrakten Klasse definiert ist und keine Implementierung hat. 
Abgeleitete Klassen müssen diese Methode implementieren, um instanziiert werden zu können. Wie eben bereits erwähnt, wird
dadurch sichergestellt, dass alle benötigten Methoden existieren, beispielsweise `__lt__`, um die Objekte sortieren zu können.

### Syntax:

```python
from abc import ABC, abstractmethod

class AbstractBaseClass(ABC):
    @abstractmethod
    def my_abstract_method(self):
        pass
```

### Beispiel:

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def move(self):
        return "Dog moves."

class Cat(Animal):
    def move(self):
        return "Cat moves!"
```

---

[vorherige Seite](16_vererbung)  
[Zurück zum Inhaltsverzeichnis](00_inhaltsverzeichnis.md)  
[nächste Seite](18_exceptions)