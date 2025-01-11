# Datentypen und Operationen

Empfohlene Skills: keine, aber es wird die Installation von Python und einem Texteditor / IDE vorausgesetzt

---

Traditionell beginnt man das Lernen einer neuen Programmiersprache, indem man "Hello world!" auf der Konsole ausgibt.
In Python geht das mit dem Befehl

```python
print("Hello world!")
```

\
Python unterstützt verschiedene grundlegende Datentypen, die in vielen Programmen häufig verwendet werden. Dazu gehören:

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


## `bool` (Boolesche Werte)

Boolesche Werte (`bool`) haben nur zwei mögliche Zustände: `True` (wahr) oder `False` (falsch). Sie werden häufig in
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

### Escape-Sequenzen für Strings

Eine **Escape-Sequenz** ist eine Kombination von Zeichen in einem String, die nicht als normale Textzeichen, sondern
als spezielle Anweisungen interpretiert wird. In Python (und vielen anderen Programmiersprachen) werden Escape-Sequenzen
verwendet, um Zeichen darzustellen, die sonst schwer oder gar nicht direkt eingegeben werden können, wie z.B. ein
Zeilenumbruch, ein Tab oder ein Anführungszeichen (da damit Strings umrandet sind).  
Escape-Sequenzen beginnen immer mit einem Backslash ( \ ), gefolgt von einem bestimmten Buchstaben oder einer Zahl, die
eine spezielle Bedeutung hat. Dadurch weiß Python, dass es dieses Zeichen anders interpretieren soll.  
Beispiel: Wenn du `\n` in einem String verwendest, bedeutet das **"neue Zeile"**, und Python wird an dieser Stelle einen
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

Probier die Escape-Sequenzen selbst aus. Unicode-Zeichen wie Emojis kann man übrigens auch einfach direkt in einen String einfügen, ohne die
Codierung anzugeben.

### f-Strings

Strings, bei denen vor dem ersten Hochkomma ein f steht, sind f-Strings. Diese haben die besondere Eigenschaft, dass
man andere Variablen in geschweiften Klammern einbinden kann.
Das kann so aussehen:

```python
x = 10
print(f"Der Wert von x ist {x}.")
# Ausgabe: Der Wert von x ist 10.
```


## `None`

In Python repräsentiert der NoneType den Typ von None, einem speziellen Wert, der verwendet wird, um das Fehlen eines 
Werts oder einen „leeren“ Zustand darzustellen. None ist also ein eigenständiges Objekt und wird häufig verwendet, um 
das Nichtvorhandensein eines gültigen Werts oder die Abwesenheit von Daten zu signalisieren.

### Beispiel

Für ein sinnvolles Beispiel braucht man bereits hier `if`-Anweisungen, die in der [Datei zu Kontrollstrukturen](02_kontrollstrukturen.md) erklärt werden.

```python
x = None
y = 5

if x is not None:  # für Abfragen auf None verwendet man das Schlüsselwort is. == geht auch, wird aber nicht empfohlen.
    # das setzt voraus, dass x entweder None oder eine Zahl ist.
    # Wenn x an dieser Stelle None wäre, würde das Programm einen Fehler werfen.
    print(x + y)
```

## Typehints

In Python ist es nicht erforderlich, den Typ einer Variable anzugeben. Man kann dies trotzdem tun, um die Lesbarkeit und 
Wartbarkeit des Codes zu verbessern. [Hier](20_typehints.md) wird das Thema ausführlicher erklärt. 


## Nutzereingaben

Man kann Nutzereingaben über die Konsole empfangen. Dazu gibt es die Funktion `input`. Diese kann man wie folgt
anwenden:

```python
name = input("Wie heißt du? ")
```

Die Nutzereingabe ist immer ein String. Wenn man einen int, float oder bool daraus machen will, geht das so:

```python
age = int(input("Wie alt bist du? "))
```

Für die anderen Datentypen funktioniert dies analog. Achtung: Wenn man bool verwendet, wird der Wert True, wenn der
String nicht leer ist und sonst False.


## Variablen benennen

Prinzipiell kann man Variablen beliebig benennen. Hier sind einige Ansätze für gute Variablennamen. 

1. Variablennamen sollten kurz und prägnant sein. Namen wie a, b, c sind nichtssagend und verwirren andere Leute, die
   deinen
   Code lesen (und dich nach 2 Wochen)

2. Variablennamen sollten immer kleingeschrieben werden. Wenn man mehrere Wörter nutzen will, kann man Unterstriche
   statt
   Leerzeichen nehmen, z.B.

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
