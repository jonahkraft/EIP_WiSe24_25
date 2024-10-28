# Rekursion

Empfohlene Skills: [Datentypen und Operatoren](01_datentypen_operationen.md), [Kontrollstrukturen](02_kontrollstrukturen.md)
und [Funktionen](09_funktionen.md)

---

Rekursion ist eine Technik, bei der eine Funktion sich selbst aufruft, um ein Problem zu lösen. 
Ein rekursiver Ansatz zerlegt ein Problem in kleinere Unterprobleme, bis eine bestimmte Bedingung erreicht ist (
die sogenannte **Basisbedingung**). Diese Methode eignet sich besonders für Probleme, die sich wiederholende Muster oder 
hierarchische Strukturen haben.

---

## Aufbau einer rekursiven Funktion

Eine rekursive Funktion besteht immer aus zwei Hauptbestandteilen:

- **Basisfall (Abbruchbedingung)**: Die Rekursion muss irgendwann enden. Hier wird eine Bedingung definiert, bei der die Rekursion aufhört.
- **Rekursiver Fall**: In diesem Teil ruft sich die Funktion selbst auf, um das Problem in kleinere Teile zu zerlegen.

### Syntax:

```python
def rekursive_funktion(parameter):
    if basisfall:
        return ergebnis
    else:
        # Ruft die Funktion erneut auf (rekursiver Fall)
        return rekursive_funktion(veränderte_parameter)
```

---

## Beispiel: Fakultät berechnen

Die Fakultät einer Zahl `n` (geschrieben `n!`) ist das Produkt aller positiven Ganzzahlen kleiner oder gleich `n`. Die Fakultät lässt sich rekursiv definieren:

- **Basisfall**: Wenn `n == 0`, dann ist `n! = 1`.
- **Rekursiver Fall**: Wenn `n > 0`, dann ist `n! = n * (n-1)!`.

### Beispiel:

```python
def factorial(n):
    if n == 0:
        return 1  # Basisfall
    else:
        return n * factorial(n - 1)  # Rekursiver Fall

ergebnis = factorial(5)
print(ergebnis)  # Ausgabe: 120

```

Die Berechnung erfolgt hier rekursiv:
- `fakultaet(5)` → `5 * fakultaet(4)`
- `fakultaet(4)` → `4 * fakultaet(3)`
- `fakultaet(3)` → `3 * fakultaet(2)`
- `fakultaet(2)` → `2 * fakultaet(1)`
- `fakultaet(1)` → `1 * fakultaet(0)`
- `fakultaet(0)` → `1`

---

## Beispiel: Fibonacci-Zahlen

Die Fibonacci-Zahlen sind eine Folge, in der jede Zahl die Summe der beiden vorhergehenden ist:
- **Basisfälle**: Die ersten beiden Fibonacci-Zahlen sind `0` und `1`.
- **Rekursiver Fall**: Jede nachfolgende Zahl ist die Summe der beiden vorhergehenden.

### Beispiel:

```python
def fibonacci(n):
    if n == 0:
        return 0  # Basisfall
    elif n == 1:
        return 1  # Basisfall
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Rekursiver Fall

result = fibonacci(6)
print(result)  # Ausgabe: 8

```

Die Berechnung erfolgt rekursiv:
- `fibonacci(6)` → `fibonacci(5)` + `fibonacci(4)`
- `fibonacci(5)` → `fibonacci(4)` + `fibonacci(3)`
- usw.

---

## Vorteile und Nachteile der Rekursion

### Vorteile:

- **Klarheit und Einfachheit**: Rekursive Lösungen sind oft kompakt und elegant, besonders bei Problemen, die sich natürlich rekursiv definieren lassen (wie die Fibonacci-Zahlen oder Baumstrukturen).

### Nachteile:

- **Leistung**: Rekursive Funktionen können speicherintensiv sein, da jeder Funktionsaufruf auf dem **Call-Stack** gespeichert wird. Bei sehr großen Rekursionstiefen kann es zu einem **Stack Overflow** kommen.
- **Effizienz**: Rekursive Lösungen können langsamer sein als iterative Ansätze, da viele Funktionsaufrufe nötig sind (z. B. in der Fibonacci-Funktion).

Eine der "bösartigsten" rekursiven Funktionen, wenn es um Leistung und Effizienz geht, ist übrigens die Ackermann-Funktion.

---

[vorherige Seite](10_nuetzliche_funktionen.md)  
[Zurück zum Inhaltsverzeichnis](00_inhaltsverzeichnis.md)  
[nächste Seite](12_backtracking.md)