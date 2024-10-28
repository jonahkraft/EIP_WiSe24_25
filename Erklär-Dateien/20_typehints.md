# Eine Einführung zu Typehints

Empfohlene Skills: [Datentypen und Operatoren](01_datentypen_operationen.md) und für komplexere Typehints
[Listen](04_listen.md), [Funktionen](09_funktionen.md) und [Tupel, Dictionaries und Sets](13_tupel_dictionaries_sets.md).

---

## Einführung

Typehints oder Typ-Annotationen sind Verweise im Code, die angeben, welchen Typ eine Variable hat, also ob sie beispielsweise
ein Integer oder ein String ist. Man kann diese Typehints machen, wenn man eine Variable deklariert, in unserem Fall ist das
der Zeitpunkt, an dem ihr zum ersten Mal ein Wert zugewiesen wird. In Python sind Typehints völlig optional,
während es in anderen Programmiersprachen üblich ist, dass diese zwingend erforderlich sind.

Wenn eine Variable deklariert wird, kann man hinter den Variablennamen einen Doppelpunkt und dann den Typ schreiben, bevor
das Gleichheitszeichen folgt.

---

## Typehints für primitive Datentypen

Fangen wir mit den grundlegenden Datentypen an.

```python
my_string: str = ""
my_int: int = 42
my_float: float = 3.14
my_bool: bool = True
```

In der einführenden Datei zu [Datentypen und Operatoren](01_datentypen_operationen.md) wurde auch der None-Type genannt.
Hier funktioniert ein Typehint anders. Normalerweise ist eine Variable, die None sein kann, entweder None oder eine Instanz
von einem bestimmten anderen Typ. Beispielsweise könnte eine Variable entweder None oder ein int sein. Um auszudrücken,
dass die Variable einen von beiden Typen hat, kann man einen Hochstrich verwenden. Das geht so:

```python
my_optional_float: None | float = None
```

Wenn man die Hochstrich-Syntax vermeiden will, kann man auch mit Optional aus dem Typing-Modul arbeiten. Das würde dann
so aussehen und ist die Syntax, die ich bevorzuge.

```python
from typing import Optional

my_optional_float: Optional[float] = None
```

---

## Typehints für Listen

Bei Listen gibt man zunächst an, dass es sich bei der Variable um eine Liste handelt. Weiter kann man aber auch
angeben, welchen Typ die Elemente der Liste haben. Es ist sinnvoll, dass alle Elemente denselben Typ haben, aber in
Python nicht zwingend erforderlich. Wenn eine Liste verschiedene Datentypen enthält, kann man das mit dem Hochstrich angeben.
Normalerweise schreibt man "list" klein. Wenn man es lieber großschreiben will, kann man List aus dem Typing-Modul importieren.

```python
from typing import List

my_list: list = []
my_int_list: List[int] = [1, 2, 3, 4]
my_mixed_list: List[int | float] = [1, 2, 3.14, 4]
```

---

## Typehints für Funktionen

Bei Funktionen kann man angeben, welchen Typen die Parameter haben und welcher Datentyp zurückgegeben wird. Bei den
Parametern geht man wie bei normalen Variablen vor und der Rückgabetyp wird mit einem Pfeil versehen. Nehmen wir als 
Beispiel einen naiven Primzahl-Test.

```python
import math

def is_prime(n: int) -> bool:
    # die Funktion erhält als Parametern n einen Integer und gibt einen booleschen Wert zurück
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

```

---

## Typehints für Tupel

Hier geht man analog zu den Listen vor. Auch hier kann man optional "Tuple" aus dem Typing-Modul importieren, um es
großzuschreiben. Im Gegensatz zu den Listen muss man aber für jedes Element den Typ angeben, um einen "sauberen" Typehint
zu machen.

```python
from typing import Tuple

my_tuple: Tuple[int, int, int] = (1, 2, 3)
```

---

## Typehints für Sets

Auch hier geht man analog zu den Listen vor und kann wahlweise "Set" aus dem Typing-Modul importieren.
Da Sets nicht indiziert sind und keine feste Länge haben, kann man im Gegensatz zu den Tupeln nicht für jedes
Element den Typ einzeln angeben.

```python
from typing import Set

my_set: Set[int] = {1, 2, 3}
```

---

## Typehints für Dictionaries

Hier gibt man an, welchen Typen die Keys haben (es sollte immer derselbe Datentyp sein, etwas anderes wäre keine gute Praxis)
und welchen die Values. Hier kann der Wert abweichen. Im Typing-Modul gibt es "Dict".

```python
from typing import Dict

my_dict: Dict[int, str] = {0: "Hello", 1: "World"}
# der erste Typ in den eckigen Klammern ist für die Keys und der zweite für die Values.
```

---

## Probleme mit Typehints

Im Kontext der OOP kann es zu Problemen mit Typehints kommen. Ein Beispiel:

```python
class MyClass:
    def __init__(self, x: int):  # für self macht man gewöhnlich keinen Typehint
        self.x: int = x
    
    def __eq__(self, other: MyClass) -> bool:
        return self.x == other.x
```

Hier würde es zur Laufzeit einen Fehler geben, weil ich einen Typehint der Klasse MyClass verwendet habe,
während ich mich in deren Scope befinde. Dieses Problem lässt sich lösen, indem man in die erste Zeile der
Datei den folgenden Import ergänzt.

```python
from __future__ import annotations
```

Dies sorgt dafür, dass die Typehints intern als Strings betrachtet und deswegen vollständig ignoriert werden.

---

## Wann Typehints verwenden?

Da Typehints optional sind, kann man sie nach Belieben verwenden oder es lassen. Es ist sinnvoll Typehints
zu verwenden, wenn der Typ einer Variable nicht offensichtlich ist. Darüber hinaus empfiehlt es sich, Typehints
bei Funktionen (siehe oben) anzugeben, insbesondere, wenn diese viele Parameter übergeben bekommen.

---

[vorherige Seite](19_exceptions.md)  
[Zurück zum Inhaltsverzeichnis](00_inhaltsverzeichnis.md)  
