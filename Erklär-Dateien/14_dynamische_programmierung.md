## Dynamische Programmierung

Empfohlene Skills: [Datentypen und Operatoren](01_datentypen_operationen.md), [Kontrollstrukturen](02_kontrollstrukturen.md),
[Funktionen](09_funktionen.md), [Rekursion](11_rekursion.md) und [Dictionaries](13_tupel_dictionaries_sets.md)

---

Die Idee der dynamischen Programmierung ist es, Zwischenergebnisse zu speichern und redundante Rechnungen zu sparen.
Kurz gesagt wird ein Memory angelegt, also ein Dictionary, das als Keys jeweils n und als Values den Funktionswert von n
speichert.

---

## Beispiel: Fibonacci


```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

Die Fibonacci-Funktion ist recht ineffizient, da der Rechenaufwand mit steigendem n explodiert.
Beheben wir das!

```python
def dynamic_fibonacci(n, mem={}):
    if n in mem:
        # wenn der Wert bereits bekannt ist, gib ihn zurück
        return mem[n]
    
    # berechne Wert, schreibe ins Memory
    if n <= 1:
        mem[n] = n
    else:
        mem[n] = dynamic_fibonacci(n-1, mem) + dynamic_fibonacci(n-2, mem)
        
    return mem[n]
```

Wenn Funktionswerte bereits bekannt sind, werden sie aus dem Memory gelesen. Ansonsten werden sie berechnet und dann
ins Memory geschrieben. Da Dictionaries mutable sind, greift jeder Rekursionsaufruf auf dasselbe Dictionary zu und es muss
nicht returned werden!

---

## Ein weiterer Anwendungsfall

```python
def func(n):
    if n <= 1:
        return 42
    else:
        return max(func(n-2) + 1, func(n-1) + 2)
```

Diese Funktion hat keinen tieferen Sinn, aber sie hat offensichtlich Potenzial, verbessert zu werden. Machen wir also
auch das mit einem Memory.

```python
def dynamic_func(n, mem={}):
    # Es gibt jetzt einen neuen Basisfall für die Funktion, und zwar, dass der Wert bereits berechnet wurde.

    if n in mem:
        return mem[n]

    # Der bereits bestehende Basisfall wird darum ergänzt, dass das Ergebnis ins Memory geschrieben wird.
    # Ansonsten geht man analog zu Fibonacci vor

    if n <= 1:
        mem[n] = 42
    else:
        mem[n] = max(dynamic_func(n-2, mem) + 1, dynamic_func(n-1, mem) + 2)
        
    return mem[n]
```

---
[vorherige Seite](13_tupel_dictionaries_sets.md)  
[Zurück zum Inhaltsverzeichnis](00_inhaltsverzeichnis.md)  
[nächste Seite](15_breitensuche.md)