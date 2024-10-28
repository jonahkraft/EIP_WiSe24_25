# Fortgeschrittene OOP

Empfohlene Skills: [Datentypen und Operatoren](01_datentypen_operationen.md), [Kontrollstrukturen](02_kontrollstrukturen.md),
[Funktionen](09_funktionen.md) und [OOP](16_oop.md)

---

## @staticmethod

Ein `@staticmethod` ist eine Methode, die innerhalb einer Klasse definiert ist, aber keinen Zugriff auf die Instanz (`self`) 
oder die Klasse (`cls`) hat. Sie verhält sich wie eine normale Funktion, die in den Namensraum der Klasse eingeschlossen ist.

### Syntax:

```python
class MyClass:
    @staticmethod
    def my_method(parameter):
        # Code hier
        ...
```

### Beispiel:

```python
class Math:
    @staticmethod
    def add(x, y):
        return x + y

print(Math.add(5, 3))  # Ausgabe: 8
```

---

## @classmethod

Ein `@classmethod` ist eine Methode, die Zugriff auf die Klasse (`cls`) hat, aber nicht auf die Instanz (`self`). 
Es wird häufig verwendet, um Fabrikmethoden zu erstellen oder den Zustand der Klasse zu verändern.

### Syntax:

```python
class MyClass:
    @classmethod
    def my_method(cls, parameter):
        # Code hier
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

---

# Abstrakte Klassen (ABC) und @abstractmethod

## Abstrakte Klassen

Eine abstrakte Klasse ist eine Klasse, die nicht instanziiert werden kann und dazu dient, eine Basis für andere Klassen 
zu schaffen. Abstrakte Klassen enthalten oft abstrakte Methoden, die in den abgeleiteten Klassen implementiert werden müssen.

## @abstractmethod

Ein `@abstractmethod` ist eine Methode, die in einer abstrakten Klasse definiert ist und keine Implementierung hat. 
Abgeleitete Klassen müssen diese Methode implementieren, um instanziiert werden zu können.

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

[vorherige Seite](17_vererbung.md)  
[Zurück zum Inhaltsverzeichnis](00_inhaltsverzeichnis.md)  
[nächste Seite](19_exceptions.md)