# Die Module math, random und string

Empfohlene Skills: [Datentypen und Operatoren](01_datentypen_operationen.md) und Grundkenntnisse in [Listen](04_listen.md)

---

## Einführung in das `math`-Modul

Das `math`-Modul bietet eine Vielzahl von mathematischen Funktionen und Konstanten, die häufig in wissenschaftlichen und mathematischen Berechnungen verwendet werden.

### Wichtige Funktionen und Konstanten:

- **`math.pi`**: Die Konstante π
- **`math.e`**: Die eulersche Zahl e, etwa 2.71828
- **`math.sqrt(x)`**: Gibt die Quadratwurzel von x zurück.
- **`math.factorial(x)`**: Gibt die Fakultät von x zurück (x!).
- **`math.sin(x)`**, **`math.cos(x)`**, **`math.tan(x)`**: Trigonometrische Funktionen, die den Sinus, Kosinus und Tangens eines Winkels in Bogenmaß berechnen.
- **`math.log(x, base)`**: Gibt den Logarithmus von x zur angegebenen Basis zurück (Basis ist optional, Standard ist e).
- **`math.floor(x)`**: Rundet x auf die nächste ganze Zahl nach unten.
- **`math.ceil(x)`**: Rundet x auf die nächste ganze Zahl nach oben.

### Beispiel:

```python
import math

# Berechnung der Quadratwurzel
angle = math.sqrt(16)
print("Die Quadratwurzel von 16 ist:", angle)

# Berechnung des Sinus eines Winkels
angle = math.radians(30)  # Umwandlung von Grad in Bogenmaß
sinus = math.sin(angle)
print("Der Sinus von 30 Grad ist:", sinus) 

# Berechnung der Fakultät
factorial = math.factorial(5)
print("Die Fakultät von 5 ist:", factorial)  
```


## Einführung in das `random`-Modul

Das `random`-Modul bietet Funktionen zur Erzeugung von Zufallszahlen und ist nützlich für Simulationen, Spiele und andere Anwendungen, bei denen Zufälligkeit erforderlich ist.

### Wichtige Funktionen:

- **`random.random()`**: Gibt eine zufällige Fließkommazahl zwischen 0.0 und 1.0 zurück.
- **`random.randint(a, b)`**: Gibt eine zufällige Ganzzahl zwischen a und b (inklusive) zurück.
- **`random.choice(seq)`**: Wählt ein zufälliges Element aus einer nicht leeren Sequenz (z.B. Liste oder Tuple) aus.
- **`random.shuffle(lst)`**: Mischt die Elemente einer Liste in zufälliger Reihenfolge.
- **`random.sample(population, k)`**: Wählt eine zufällige Teilmenge der Größe k aus einer Population aus.

### Beispiel:

```python
import random

# Zufällige Fließkommazahl zwischen 0 und 1
random_float = random.random()
print("Eine zufällige Fließkommazahl zwischen 0 und 1:", random_float)

# Zufällige Ganzzahl zwischen 1 und 10
random_digit = random.randint(1, 10)
print("Eine zufällige Ganzzahl zwischen 1 und 10:", random_digit)

# Zufälliges Element aus einer Liste auswählen. Wie genau Listen funktionieren, folgt
colors = ['red', 'green', 'blue', 'yellow']
random_color = random.choice(colors)
print("Eine zufällige Farbe:", random_color)

# Elemente einer Liste mischen
digits = [1, 2, 3, 4, 5]
random.shuffle(digits)
print("Gemischte Liste:", digits)
```


## Einführung in das `string`-Modul

Das `string`-Modul enthält Funktionen und Konstanten, die mit Zeichenfolgen arbeiten und nützliche Werkzeuge für die Textmanipulation bereitstellen.

### Wichtige Konstanten:

- **`string.ascii_letters`**: Alle Buchstaben des Alphabets (sowohl klein als auch groß).
- **`string.ascii_lowercase`**: Alle Kleinbuchstaben (a-z).
- **`string.ascii_uppercase`**: Alle Großbuchstaben (A-Z).
- **`string.digits`**: Alle Ziffern (0-9).
- **`string.punctuation`**: Alle Satzzeichen.
- **`string.printable`**: Alle druckbaren Zeichen (Buchstaben, Ziffern, Satzzeichen und Leerzeichen).
- **`string.whitespace`**: Alle Whitespace-Zeichen (z.B. Leerzeichen, Tabulatoren).

### Nützliche Funktionen:

- **`string.capwords(s)`**: Gibt die Zeichenfolge s zurück, wobei jedes Wort mit einem Großbuchstaben beginnt.
- **`string.replace(s, old, new)`**: Ersetzt alle Vorkommen von `old` in der Zeichenfolge `s` durch `new`. Gibt es aber auch als Methode der String-Klasse

### Beispiel:

```python
import string

# Verwendung von string.ascii_letters
char = 'A'
if char in string.ascii_letters:
    print(f"{char} ist ein Buchstabe.")

# Nutzung von string.capwords
text = "hallo welt"
text_with_capwords = string.capwords(text)
print("Mit Großbuchstaben:", text_with_capwords)  

# Ersetzen von Zeichen in einer Zeichenfolge
original = "Ich liebe Python!"
replaced = original.replace("liebe", "mag")
print("Ersetzter Text:", replaced)  
```

---

[vorherige Seite](02_kontrollstrukturen.md)  
[Zurück zum Inhaltsverzeichnis](00_inhaltsverzeichnis.md)  
[nächste Seite](04_listen.md)