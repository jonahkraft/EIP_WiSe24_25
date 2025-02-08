# Datentypen und Operationen

Empfohlene Skills: keine, aber es wird die Installation von Python und einem Texteditor / IDE vorausgesetzt

---

Traditionell beginnt man das Lernen einer neuen Programmiersprache, indem man "Hello, world!" auf der Konsole ausgibt.
In Python geht das mit dem Befehl

```python
print("Hello, world!")
```

Python unterstützt verschiedene grundlegende Datentypen, die in den meisten Programmen verwendet werden. Dazu gehören:

- `int` (Ganzzahlen)
- `float` (Gleitkommazahlen)
- `bool` (Boolesche Werte)
- `str` (Zeichenketten, also Text)


## `int` (Ganzzahlen)

Ganzzahlen (`int`) sind Zahlen ohne Dezimalstellen. Sie können sowohl positiv als auch negativ sein.

### Beispiel:

```python
x = 42
y = -5
```

### Unterstützte Operationen mit `int`:

| Operation | Beschreibung              | Beispiel | Ergebnis |
|-----------|---------------------------|----------|----------|
| `+`       | Addition                  | `5 + 3`  | `8`      |
| `-`       | Subtraktion               | `5 - 3`  | `2`      |
| `*`       | Multiplikation            | `5 * 3`  | `15`     |
| `/`       | Division (float Ergebnis) | `5 / 2`  | `2.5`    |
| `//`      | Ganzzahl-Division         | `5 // 2` | `2`      |
| `%`       | Modulo (Restwert)         | `5 % 2`  | `1`      |
| `**`      | Potenzierung              | `5 ** 2` | `25`     |


## `float` (Gleitkommazahlen)

Gleitkommazahlen (`float`) sind Zahlen mit Dezimalstellen. Sie werden verwendet, wenn genauere Werte benötigt werden.

### Beispiel:

```python
x = 3.14
y = -0.5
```

### Unterstützte Operationen mit `float`:

| Operation | Beschreibung   | Beispiel    | Ergebnis |
|-----------|----------------|-------------|----------|
| `+`       | Addition       | `3.5 + 1.2` | `4.7`    |
| `-`       | Subtraktion    | `3.5 - 1.2` | `2.3`    |
| `*`       | Multiplikation | `3.5 * 2`   | `7.0`    |
| `/`       | Division       | `3.5 / 2`   | `1.75`   |
| `**`      | Potenzierung   | `3.5 ** 2`  | `12.25`  |

Warnung: Gleitkommazahlen sind nicht immer genau. Das liegt an der Art und Weise, wie sie im Computer gespeichert werden.  
Manchmal kann dies zu unerwarteten Ergebnissen führen. Zum Beispiel:

```python
print(0.1 + 0.2 == 0.3)  # False
```

## `bool` (Boolesche Werte)

Boolesche Werte (`bool`) haben nur zwei mögliche Zustände: `True` (wahr) oder `False` (falsch). Sie werden in
logischen Operationen und Bedingungen verwendet.

### Beispiel:

```python
x = True
y = False
# man muss True oder False nicht explizit zuweisen. Es geht auch so:
z = 3 < 4
# da 3 kleiner als 4 ist, bekommt z den Wert True zugewiesen.
```

### Unterstützte Operationen mit `bool`:

| Operation | Beschreibung         | Beispiel         | Ergebnis |
|-----------|----------------------|------------------|----------|
| `and`     | Logisches UND        | `True and False` | `False`  |
| `or`      | Logisches ODER       | `True or False`  | `True`   |
| `not`     | Logische Negation    | `not True`       | `False`  |
| `==`      | Vergleich (gleich)   | `True == False`  | `False`  |
| `!=`      | Vergleich (ungleich) | `True != False`  | `True`   |
| `<`       | Kleiner als          | `5 < 10`         | `True`   |
| `>`       | Größer als           | `5 > 10`         | `False`  |
| `<=`      | Kleiner oder gleich  | `5 <= 5`         | `True`   |
| `>=`      | Größer oder gleich   | `5 >= 10`        | `False`  |

Achtung: `=` und `==` haben eine andere Bedeutung! `=` ist eine Wertzuweisung und `==` ist ein Vergleich!

### Wahrheitstafel für logische Operatoren:

| `A`   | `B`   | `A and B` | `A or B` | `not A` |
|-------|-------|-----------|----------|---------|
| True  | True  | True      | True     | False   |
| True  | False | False     | True     | False   |
| False | True  | False     | True     | True    |
| False | False | False     | False    | True    |


## `str` (Strings)

Strings (`str`) sind Zeichenketten, die Text repräsentieren. Sie werden in Anführungszeichen geschrieben, entweder in
einfachen (`'`) oder doppelten (`"`).

Hinweis für Fortgeschrittene: In Python gibt es keinen Unterschied zwischen einfachen und doppelten Anführungszeichen,
da chars und strings in Python dasselbe sind.

### Beispiel:

```python
x = "Hallo"
y = 'Welt'
```

### Unterstützte Operationen mit `str`:

| Operation | Beschreibung               | Beispiel            | Ergebnis            |
|-----------|----------------------------|---------------------|---------------------|
| `+`       | Verkettung (Konkatenation) | `"Hallo" + " Welt"` | `"Hallo Welt"`      |
| `*`       | Wiederholung               | `"Hallo" * 3`       | `"HalloHalloHallo"` |
| `in`      | Überprüfung auf Teilstring | `'a' in "Hallo"`    | `True`              |

Man bemerkt, dass eine Operation wie `"Hallo" + 42` nicht funktioniert. Dies liegt daran, dass man in Python keine Strings
mit Zahlen addieren kann. Um dies zu tun, muss man die Zahl in einen String umwandeln, z.B. `"Hallo" + str(42)`.

### Indexierung und Slicing

Strings können indexiert und gesliced werden. Der Index eines Strings beginnt bei 0. Negative Indizes zählen von hinten
beginnend bei -1.

```python
s = "Hallo, Welt!"
print(s[0])    # H
print(s[-1])   # !
print(s[7:12]) # Welt!
```

Dies aber zunächst nur am Rande. Das Thema wird in der [Datei zu Listen](04_listen.md) ausführlich behandelt.

### Escape-Sequenzen für Strings

Eine **Escape-Sequenz** ist eine Kombination von Zeichen in einem String, die nicht als normale Textzeichen, sondern
als spezielle Anweisungen interpretiert wird. In Python (und vielen anderen Programmiersprachen) werden Escape-Sequenzen
verwendet, um Zeichen darzustellen, die sonst schwer oder gar nicht direkt eingegeben werden können, wie z.B. ein
Zeilenumbruch, ein Tab oder ein Anführungszeichen (da damit Strings umrandet sind).  
Escape-Sequenzen beginnen immer mit einem Backslash (`\`), gefolgt von einem bestimmten Buchstaben oder einer Zahl, die
eine spezielle Bedeutung hat. Dadurch weiß Python, dass es dieses Zeichen anders interpretieren soll.  
Beispiel: Wenn Sie `\n` in einem String verwenden, bedeutet das **"neue Zeile"**, und Python wird an dieser Stelle einen
Zeilenumbruch einfügen.  
Hier ist eine Liste der wichtigsten Escape-Sequenzen in Python:

| Escape-Sequenz | Beschreibung                                | Beispiel                 | Ausgabe                                 |
|----------------|---------------------------------------------|--------------------------|-----------------------------------------|
| `\\`           | Backslash (um einen Backslash darzustellen) | `"C:\\\\Users\\\\Jonah"` | `C:\\Users\\Jonah`                      |
| `\'`           | Einzelnes Anführungszeichen                 | `'It\'s a test.'`        | `It's a test.`                          |
| `\"`           | Doppelte Anführungszeichen                  | `"He said: \"Hello!\""`  | `He said: "Hello!"`                     |
| `\n`           | Neue Zeile (Zeilenumbruch)                  | `"Hello\nWorld"`         | `Hello`<br>`World`                      |
| `\t`           | Tab (horizontaler Tabulator)                | `"Hello\tWorld"`         | `Hello    World`                        |
| `\N{name}`     | Unicode-Zeichen durch Name                  | `"\N{COPYRIGHT SIGN}"`   | `©`                                     |
| `\uhhhh`       | 16-Bit Unicode-Zeichen                      | `"\u00A9"`               | `©`                                     |
| `\Uhhhhhhhh`   | 32-Bit Unicode-Zeichen                      | `"\U0001F600"`           | 😀                                      |

### f-Strings

Strings, bei denen vor dem ersten Hochkomma ein f steht, sind f-Strings. Diese haben die besondere Eigenschaft, dass
man andere Variablen in geschweiften Klammern einbinden kann.
Das kann so aussehen:

```python
x = 10
print(f"Der Wert von x ist {x}.")
```

## Typumwandlung

Manchmal muss man den Datentyp einer Variablen ändern. Wir haben im obigen Beispiel gesehen, wie man eine Zahl in einen
String umwandeln kann. Dies funktioniert für alle Datentypen, die bisher thematisiert wurden. Hier sind einige Beispiele:

```python
x = 42
y = str(x)  # y ist jetzt der String "42"

a = "3.14"
b = float(a)  # b ist jetzt die Gleitkommazahl 3.14

c = "42"
d = int(c)  # d ist jetzt die Ganzzahl 42
```

Warnung: Typumwandlungen können zu Fehlern führen, wenn die Umwandlung nicht möglich ist. Zum Beispiel kann 
`int("Hallo")` nicht funktionieren, da "Hallo" keine Zahl ist.


## Nutzereingaben

Man kann Nutzereingaben über die Konsole empfangen. Dazu gibt es die Funktion `input`. Diese kann man wie folgt
anwenden:

```python
name = input("Wie heißen Sie? ")
```

Die Nutzereingabe ist immer ein String. Wenn wir sie als Zahl verwenden wollen, müssen wir sie umwandeln. Das geht so:

```python
age = int(input("Wie alt sind Sie? "))
```

Für die anderen Datentypen funktioniert dies analog. Achtung: Wenn man bool verwendet, wird der Wert True, wenn der
String nicht leer ist und sonst False.


## Variablen benennen

Prinzipiell kann man Variablen beliebig benennen. Hier sind einige Ansätze für gute Variablennamen. 

1. Variablennamen sollten kurz und prägnant sein. Namen wie a, b, c sind nichtssagend und verwirren andere Leute, die
   Ihren Code lesen. Besser ist es, Namen zu wählen, die den Zweck der Variablen beschreiben, z.B. `age` statt `a`.

2. Variablennamen sollten immer kleingeschrieben werden. Wenn man mehrere Wörter nutzen will, kann man Unterstriche
   statt Leerzeichen nehmen, z.B.

```python
my_age = 20
```

3. Variablen, die ihren Wert nicht ändern, sind Konstanten. Es ist eine gute Praxis, diese in Großbuchstaben zu
   schreiben, z.B.

```python
MAXIMUM_LOGIN_ATTEMPTS = 5
```

4. Es ist eine gute Praxis, Variablen auf amerikanischem Englisch zu benennen.

---

[Zurück zum Inhaltsverzeichnis](00_inhaltsverzeichnis.md)  
[nächste Seite](02_kontrollstrukturen.md)
