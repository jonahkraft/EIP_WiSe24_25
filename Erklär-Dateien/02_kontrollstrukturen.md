# Kontrollstrukturen

Empfohlene Skills: [Datentypen und Operatoren](01_datentypen_operationen.md)

---

## `if`-Statements

`if`-Anweisungen ermöglichen es Ihnen, Bedingungen zu überprüfen und entsprechend zu reagieren. Dadurch kann Ihr Programm
auf verschiedene Ereignisse reagieren. Die allgemeine Syntax ist:

```python
if bedingung:
   ...
    # Codeblock, der ausgeführt wird, wenn die Bedingung wahr ist
elif andere_bedingung:
   ...
    # Codeblock, der ausgeführt wird, wenn die andere Bedingung wahr ist
else:
   ...
    # Codeblock, der ausgeführt wird, wenn keine der Bedingungen wahr ist
```

Was passiert hier?  
Zuerst wird geprüft, ob der boolesche Wert `bedingung` wahr ist. Wenn das der Fall ist, wird der Code darunter
ausgeführt. Code aus `elif` oder `else` wird ignoriert. Wenn `bedingung` aber falsch ist, werden nacheinander alle
`elif`-Blöcke analog getestet. Wenn keine Bedingung True ist, wird der `else`-Block (falls vorhanden) ausgeführt.
Es ist möglich, beliebig viele elif-Statements zu verwenden. `elif` und `else` sind optional.

### Beispiel:

```python
x = 10

if x > 0:
    print("x ist positiv")
elif x < 0:
    print("x ist negativ")
else:
    print("x ist null")
```

## Pattern Matching

In einigen Fällen will man Zustände einer Variable abfragen. Hier kann man natürlich `if`-Statements verwenden,
aber diese haben einen recht hohen Schreibaufwand und der Code wird unübersichtlich.

### Beispiel:

```python
x = 5

if x == 0:
    ...
elif x == 1:
    ...
elif x == 2:
    ...
elif x == 3:
    ...
else:
    ...
```

Dies lässt sich mit dem `match`-`case`-Statement eleganter formulieren. Die allgemeine Syntax ist:

```python
match variable:
    case Muster1:
        # Aktion für Muster1
    case Muster2:
        # Aktion für Muster2
    case _:
        # Standardaktion, wenn kein Muster passt
```

Was passiert hier?

1. match variable:
   Hierbei wird die zu überprüfende Variable angegeben.

2. case Muster:
   Ein Fall, der mit der Variable verglichen wird. Wenn das Muster übereinstimmt, wird der zugehörige Codeblock ausgeführt.

3. Wildcard _:
   Ein Platzhalter, der immer übereinstimmt. Er dient als "default"-Fall, ähnlich wie ein else-Fall.

Nun wollen wir das auf unser Beispiel von oben übertragen, um dieses eleganter zu formulieren.

```python
x = 5

match x:
    case 0:
        ...
    case 1:
        ...
    case 2:
        ...
    case 3:
        ...
    case _:
        ...
```


## `while`-Schleifen

`while`-Schleifen führen einen Codeblock so lange aus, wie eine bestimmte Bedingung wahr ist. Die allgemeine Syntax ist:

```python
while bedingung:
   ...
    # Codeblock, der ausgeführt wird, solange die Bedingung wahr ist
```

Konkret wird erst die Bedingung wie bei einem if-Statement getestet. Wenn sie wahr ist, wird der Codeblock
ausgeführt. Dann wird die Bedingung wieder getestet und so weiter.  
Achtung: Dadurch können "infinite loops" entstehen, wenn die Bedingung immer wahr ist.

### Beispiel:

```python
count = 0

while count < 5:
    print(f"Count ist: {count}")
    count += 1  # analog zu x = x + 1
    # wenn man hier count += 1 vergisst, hat man einen infinite loop
```

Mit while-Schleifen und if-Statements können wir bereits ein einfaches Spiel programmieren.

```python
import random

secret_number = random.randint(1, 100)  # generiert eine zufällige Zahl zwischen 1 und 100
guessed = False
count = 0

while not guessed:  # solange guessed False ist...
    guess = int(input("Rate eine Zahl zwischen 1 und 100: "))
    count += 1

    if guess == secret_number:
        guessed = True
    elif guess < secret_number:
        print("Die gesuchte Zahl ist größer!")
    else:
        print("Die gesuchte Zahl ist kleiner!")

print(f"Sie haben die gesuchte Zahl {secret_number} in {count} Versuchen erraten.")
```

Bemerkung: Die beste Taktik des Spielers ist es, die Mitte des Intervalls zu raten. So wird das Intervall bei jedem
Schritt halbiert. Das ist der schnellste Weg, um die Zahl zu erraten. Diesen Algorithmus nennt man "binary search".


## `for`-Schleifen

Neben while-Schleifen gibt es noch for-Schleifen. Damit kann man unter anderem über eine range an Zahlen iterieren.

### Die `range()`-Funktion

Die `range()`-Funktion hat drei Hauptparameter:

1. **start** (optional): Die Zahl, bei der die Sequenz beginnt (Standardwert ist 0).
2. **stop**: Die Zahl, bei der die Sequenz endet (diese Zahl ist nicht in der Sequenz enthalten).
3. **step** (optional): Der Schrittwert, um den die Sequenz erhöht oder verringert wird (Standardwert ist 1).

### Syntax:

```python
range(start, stop, step)
```

Jetzt schauen wir uns an, was das bedeutet. Wenn man die Zahlen 0 bis 9 auf der Konsole ausgeben will, kann man das mit
einer while-Schleife machen, siehe oben.

```python
i = 0
while i < 10:
    print(i)
    i += 1
```

Eleganter geht es mit einer for-Schleife.

```python
for i in range(10):
    print(i)
```

Analog zur while-Schleife am Anfang dieser Datei gibt diese for-Schleife die Zahlen 0-9 aus. Was passiert hier?  
Hinter dem for wird die Laufvariable bestimmt. In diesem Fall ist das i, prinzipiell kann man die nennen, wie man
will.  
range(10) gibt alle Zahlen zwischen 0 und 9 zurück. In der ersten Iteration hat i dann den Wert 0, in der
zweiten 1 und so weiter. Die 10 ist exklusiv, wird also nicht mehr mitgezählt. Im Schleifenkörper kann man die
Laufvariable wie eine normale Variable verwenden; man kann z.B. mathematische Operationen damit ausführen.  
Man sollte nur davon absehen, den Wert der Laufvariable zu verändern, da dies zu unerwartetem Verhalten führen kann!

---

Wenn man range() zwei Werte übergibt, dann ist der erste Wert der Startwert (inklusiv) und der zweite der Endwert (exklusiv).

```python
for i in range(1, 10):
    print(i)
# Gibt dann die Zahlen 1-9 aus.
```

Wenn man range() noch eine dritte Zahl übergibt, dann gibt diese an, um wie viel hoch- oder runtergezählt werden soll.
Standardmäßig wird immer um 1 hochgezählt. Die folgende Schleife zählt um 2 hoch:

```python
for i in range(0, 10, 2):
    print(i)
```

Man kann dieses Verhalten der for-Schleifen natürlich auch mit while-Schleifen darstellen. for-Schleifen haben
aber einige Vorteile zum Beispiel um Umgang mit Listen (kommt später).


## Steueranweisungen: `break`, `continue` und `pass`

In Python gibt es verschiedene Steueranweisungen, die das Verhalten von Schleifen beeinflussen. Hier werden die Anweisungen 
`break`, `continue` und `pass` erklärt.

### `break`

Die `break`-Anweisung wird verwendet, um eine Schleife vorzeitig zu beenden. Wenn `break` in einer Schleife ausgeführt wird, 
wird die Schleife sofort verlassen, und das Programm fährt mit dem Code nach der Schleife fort.

### Beispiel:

```python
for i in range(5):
    if i == 3:
        break  # Beendet die Schleife, wenn i gleich 3 ist
    print(i)
```

**Ausgabe:**

```
0
1
2
```

### `continue`

Die `continue`-Anweisung überspringt den aktuellen Iterationsschritt einer Schleife und fährt mit der nächsten Iteration fort. 
Wenn `continue` ausgeführt wird, wird der Rest des Schleifenblocks für die aktuelle Iteration übersprungen, und die 
Schleife wird mit der nächsten Iteration fortgesetzt.

### Beispiel:

```python
for i in range(5):
    if i == 2:
        continue  # Überspringt den Rest des Codes in dieser Iteration, wenn i gleich 2 ist
    print(i)
```

**Ausgabe:**

```
0
1
3
4
```

In diesem Beispiel wird der Wert 2 übersprungen, und die Schleife gibt nur die Werte 0, 1, 3 und 4 aus.

### `pass`

Die `pass`-Anweisung ist ein Platzhalter, der nichts tut. Sie wird verwendet, wenn syntaktisch ein Codeblock 
erforderlich ist, Sie aber noch keinen Code schreiben möchten oder wenn ein Block absichtlich leer bleiben soll. 
`pass` kann bei jeder Art von Codeblock verwendet werden, z.B. auch in if-Statements.

### Beispiel:

```python
for i in range(5):
    if i == 2:
        pass  # Platzhalter, der nichts tut, wenn i gleich 2 ist
    print(i)
```

**Ausgabe:**

```
0
1
2
3
4
```

Im obigen Beispiel hat die `pass`-Anweisung keine Auswirkung auf die Schleife, sodass alle Werte von 0 bis 4 ausgegeben werden.

---

[vorherige Seite](01_datentypen_operationen.md)  
[Zurück zum Inhaltsverzeichnis](00_inhaltsverzeichnis.md)  
[nächste Seite](03_math_random_string_module.md)
