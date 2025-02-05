# Objektorientierte Programmierung (OOP)

Empfohlene Skills: [Datentypen und Operatoren](01_datentypen_operationen.md), [Kontrollstrukturen](02_kontrollstrukturen.md),
[Funktionen](09_funktionen.md)  
Kenntnisse in [Listen](04_listen.md) und [Tupeln, Dictionaries und Sets](13_tupel_dictionaries_sets.md) schaden nicht

---

Die objektorientierte Programmierung (OOP) ist ein Programmierparadigma, das auf dem Konzept von **Objekten** und **Klassen** 
basiert. In Python ist die OOP ein zentraler Bestandteil und bietet eine flexible und leistungsstarke Möglichkeit, 
komplexe Software zu entwickeln. Dieser Abschnitt führt in die Grundlagen der OOP ein, einschließlich magischer Methoden, Getter und Setter.


## Grundlagen der OOP

### Klassen und Objekte

- **Klassen** sind Blaupausen oder Vorlagen für Objekte.
- **Objekte** sind Instanzen von Klassen. Sie repräsentieren konkrete Dinge oder Konzepte.

Beispielweise werden Strings in Python durch die Klasse `str` repräsentiert und wenn man eine Variable vom Typ `str` 
verwendet, so ist diese eine Instanz der Klasse `str`.

Eine Klasse enthält **Attribute** (analog zu Variablen) und **Methoden** (analog zu Funktionen), die das Verhalten des Objekts beschreiben.

### Syntax für Klassen und Objekte:

```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand 
        self.color = color 

    def description(self):
        return f"Marke: {self.brand}, Farbe: {self.color}"

my_car = Car("BMW", "rot")
print(my_car.description())  
```

Der Konstruktor ist eine spezielle Methode, die beim Erstellen eines Objekts automatisch aufgerufen wird. In Python heißt 
der Konstruktor `__init__`. Er wird verwendet, um die Attribute eines Objekts zu initialisieren. In der Regel werden im Konstruktor
die Attribute der Klasse (hier brand und color) deklariert. 


## Die Rolle von `self` in Python-Klassen

In Python spielt der Parameter `self` eine zentrale Rolle in der objektorientierten Programmierung. Er ist erforderlich, 
um auf die Instanz einer Klasse zuzugreifen, in der eine Methode aufgerufen wird. Das bedeutet, `self` ermöglicht es Methoden, 
die Attribute und andere Methoden des aktuellen Objekts zu referenzieren.

Was ist `self`?

- `self` ist der erste Parameter jeder Instanzmethode einer Klasse.
- Es verweist immer auf das Objekt, das die Methode aufruft.


## Magische Methoden (Dunder-Methods)

**Magische Methoden** (auch **Dunder-Methods** genannt, wegen der doppelten Unterstriche) sind spezielle Methoden, 
die von Python vordefiniert sind. Sie erlauben es, das Verhalten von Objekten in bestimmten Situationen zu steuern, 
z. B. wie Objekte verglichen, dargestellt oder addiert werden. Dadurch kann man dann etwa die Operation `+` für die Klasse
verwenden. `__lt__` ermöglicht es, Objekte der Klasse mit `<` zu vergleichen und Listen, die diese Objekte enthalten, zu
sortieren.

### Wichtige magische Methoden:

- `__init__(self, ...)`: Initialisiert ein neues Objekt.
- `__str__(self)`: Wird verwendet, um eine "lesbare" String-Repräsentation des Objekts zurückzugeben.
- `__repr__(self)`: Liefert eine technische Repräsentation des Objekts, meist für Entwickler. Wird z.B. gebraucht, wenn eine List mit diesem Objekt geprintet wird
- `__eq__(self, other)`: Vergleicht zwei Objekte auf Gleichheit (`==`).
- `__add__(self, other)`: Definiert das Verhalten des `+`-Operators zwischen zwei Objekten.
- `__lt__(self, other)`: Definiert das Verhalten des `<`-Operators zwischen zwei Objekten. Notwendig für Sortierungen
  
### Beispiel für magische Methoden:

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return str(self)

    def __eq__(self, other_point):
        return self.x == other_point.x and self.y == other_point.y

    def __add__(self, other_point):
        return Vector(self.x + other_point.x, self.y + other_point.y)


v1 = Vector(1, 2)
v2 = Vector(1, 2)
v3 = Vector(3, 4)

# __str__
print(v1)

# __eq__ für Gleichheit
print(v1 == v2)
print(v1 == v3)

# __add__ für Addition
v4 = v1 + v3
print(v4)  
```


## Getter und Setter

In Python gibt es keine "echten" privaten Variablen. Daher verwendet man oft **Getter** und **Setter**, um 
den Zugriff auf Attribute eines Objekts zu kontrollieren. Dies ermöglicht es, Logik beim Abrufen oder Ändern eines Wertes einzubauen.
Getter und Setter machen Code lesbarer.


```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Lena", 25)
print(p.age) 
p.age = 30
```

- **Getter**: Liefert den Wert eines Attributs.
- **Setter**: Setzt den Wert eines Attributs und kann zusätzliche Validierungen durchführen.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_age(self):
        return self.age

    def set_age(self, value):
        self.age = value

p = Person("Lena", 25)
print(p.get_name())  
p.set_name("Anna")  
print(p.get_name())  
```


## Call by Reference

In Python werden **Objekte** stets **per Referenz** übergeben. Das bedeutet, dass wenn ein Objekt in eine Funktion 
übergeben wird, Änderungen an dem Objekt innerhalb der Funktion auch außerhalb der Funktion sichtbar sind.

### Beispiel:

```python
class Account:
    def __init__(self, balance):
        self.balance = balance

def deposit_money(account, amount):
    account.balance += amount

my_account = Account(100)
deposit_money(my_account, 50)

print(my_account.balance)  
```

In diesem Beispiel wird das Objekt `my_account` per Referenz übergeben, und Änderungen am Kontostand innerhalb der 
Funktion `desposit_money()` sind auch außerhalb der Funktion sichtbar. Dies sollte man sich im Hinterkopf behalten, weil
es sonst zu unerwartetem Verhalten führen kann. Man kann die Methode `__copy__` überladen und Kopien von Objekten übergeben,
wenn die Originale nicht verändert werden sollen.

---

[vorherige Seite](15_breitensuche.md)  
[Zurück zum Inhaltsverzeichnis](00_inhaltsverzeichnis.md)  
[nächste Seite](17_vererbung.md)