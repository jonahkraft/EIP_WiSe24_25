# Vererbung

Empfohlene Skills: [Datentypen und Operatoren](01_datentypen_operationen.md), [Kontrollstrukturen](02_kontrollstrukturen.md),
[Funktionen](09_funktionen.md) und [OOP](15_oop)

---

Vererbung ist ein zentrales Konzept der objektorientierten Programmierung (OOP). Sie ermöglicht es, eine neue Klasse zu 
erstellen, die Eigenschaften und Methoden einer bestehenden Klasse erbt. Dies fördert die Wiederverwendbarkeit von 
Code und reduziert Redundanzen.


## Was ist Vererbung?

Vererbung bedeutet, dass eine Klasse (die **Kindklasse** oder **Unterklasse**) Eigenschaften (Attribute und Methoden) 
von einer anderen Klasse (der **Elternklasse** oder **Oberklasse**) übernimmt. Die Kindklasse kann die Eigenschaften der 
Elternklasse erweitern oder überschreiben.

### Syntax:

```python
class Elternklasse:
    ...
    # Methoden und Attribute der Elternklasse

class Kindklasse(Elternklasse):
    ...
    # Methoden und Attribute der Kindklasse
```

- Die Kindklasse erbt alle Eigenschaften und Methoden der Elternklasse.
- Sie kann eigene Methoden und Attribute hinzufügen oder geerbte Methoden überschreiben.


## Einfaches Beispiel:

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} is moving.")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} says: Woof!")


dog = Dog("Rex")
dog.move()
dog.bark()   
```

### Erklärung:
- `Dog` erbt von `Animal`. Das bedeutet, dass alle Hunde, die wir erstellen, die Methode `move()` und das Attribut `name` von der Klasse `Animal` haben.
- Die Methode `bark()` ist jedoch spezifisch für die Klasse `Dog`.


## Der `super()`-Befehl

Der `super()`-Befehl ermöglicht es, auf Methoden der Elternklasse aus der Kindklasse zuzugreifen. Dies ist besonders nützlich, 
wenn Sie in der Kindklasse eine Methode überschreiben und dennoch auf die Funktionalität der Elternklasse zugreifen möchten.
Im obigen Beispiel wurde der Konstruktor der Hund-Klasse weggelassen, da er identisch mit dem der Elternklasse ist. Daher
ist es ausreichend, den Konstruktor der Elternklasse aufzurufen, wenn ein Dog-Objekt erstellt wird.

### Beispiel mit `super()`:

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} is moving.")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def move(self):
        super().move()
        print(f"{self.name} is running fast.")


dog = Dog("Rex", "German Shepherd")
dog.move()
```

### Erklärung:
- `super().__init__(name)` ruft den Konstruktor der Elternklasse `Animal` auf, um das Attribut `name` zu initialisieren.
- Die Methode `move()` wird in der Kindklasse `Dog` überschrieben. Zuerst wird die Methode der Elternklasse aufgerufen 
- (`super().move()`), dann wird die zusätzliche Logik der Kindklasse hinzugefügt.


## Überschreiben von Methoden

Kindklassen können Methoden der Elternklasse **überschreiben**. Dadurch wird die Methode der Elternklasse in 
der Kindklasse durch eine neue Implementierung ersetzt.

### Beispiel:

```python
class Animal:
    def move(self):
        print("Das Tier bewegt sich.")


class Bird(Animal):
    def move(self):
        print("Der Vogel fliegt.")


animal = Animal()
bird = Bird()

animal.move()
bird.move()  
```

### Erklärung:
- Die Methode `move()` wurde in der Klasse `Bird` überschrieben. Wenn wir ein Objekt von `Bird` aufrufen, wird die 
- neue Implementierung verwendet, obwohl `Bird` von `Animal` erbt.


## Die `isinstance()`-Funktion

Mit der Funktion `isinstance()` kann man überprüfen, ob ein Objekt von einer bestimmten Klasse (oder einer abgeleiteten Klasse) ist.

### Beispiel:

```python
class Animal:
    pass


class Dog(Animal):
    pass


dog = Dog()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(isinstance(dog, object))  # True, da alle Klassen von object abstammen
```

### Erklärung:
- `isinstance()` gibt `True` zurück, wenn das Objekt von der angegebenen Klasse oder einer Unterklasse ist.
- Da `Dog` von `Animal` erbt, ist `dog1` auch eine Instanz von `Animal`.


## Die `issubclass()`-Funktion

Die Funktion `issubclass()` prüft, ob eine Klasse eine Unterklasse einer anderen ist.

### Beispiel:

```python
class Animal:
    pass

class Dog(Animal):
    pass

print(issubclass(Dog, Animal))  
print(issubclass(Dog, object))  # True, da alle Klassen von object abstammen
print(issubclass(Animal, Dog))  
```

---

[vorherige Seite](15_oop)  
[Zurück zum Inhaltsverzeichnis](00_inhaltsverzeichnis.md)  
[nächste Seite](17_fortgeschrittene_oop)