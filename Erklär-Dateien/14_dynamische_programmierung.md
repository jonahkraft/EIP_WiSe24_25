## Dynamische Programmierung

Empfohlene Skills: [Datentypen und Operatoren](01_datentypen_operationen.md), [Kontrollstrukturen](02_kontrollstrukturen.md),
[Funktionen](09_funktionen.md), [Rekursion](11_rekursion.md) und [Dictionaries](13_tupel_dictionaries_sets.md)

---

Die Idee der dynamischen Programmierung ist es, Zwischenergebnisse zu speichern und redundante Rechnungen zu sparen.
Kurz gesagt wird ein Memory angelegt, also beispielsweise ein Dictionary, das als Keys jeweils n und als Values den Funktionswert von n
speichert. Neben Dictionaries sind auch Listen und Matrizen gängig. Durch das Speichern von Zwischenergebnissen müssen
wir dann in den Rekursionsaufrufen lediglich fragen, ob wir den Wert bereits berechnet haben, um die Laufzeit erheblich zu
beschleunigen.


## Beispiel: Fibonacci


```python
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
```

Die obige Implementierung der Fibonacci-Funktion sollte Ihnen bekannt sein. Ein Nachteil, der bei steigenden Werten für
n schnell auffällt, ist die Tatsache, dass die Laufzeit sehr schnell wächst. Konkret lässt sie sich durch 2^n abschätzen.
Wir wollen den Algorithmus jetzt so verbessern, dass er eine Laufzeit hat, die nur linear in n ist (und damit deutlich schneller).
Wie oben bereits angedeutet, erstellen wir ein Memory, in unserem Fall als ein Dictionary. Am Anfang fragen wir, ob wir
den Wert bereits berechnet haben. Wenn ja, geben wir ihn direkt zurück und können uns weitere Rekursionsaufrufe sparen.
Alle anderen Ergebnisse, die wir berechnen müssen, speichern wir im Memory. Dadurch wir für ein gegebenes n für alle i aus 0...n-1
fibonacci(i) nur exakt einmal rekursiv berechnet.

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

## Beispiel: Einbrecher

Ein Einbrecher möchte in ein Haus einbrechen und hat eine Liste von Werten, die die Beute in jedem Raum repräsentieren.
Er darf jedoch nicht in zwei benachbarte Räume einbrechen. Wie kann er die maximale Beute erzielen?

Für das Problem lässt sich die folgende Rekursion formulieren:

```python
def max_loot(house, n):
    if n == 0:
        return house[0]
    if n == 1:
        return max(house[0], house[1])
    
    # entweder wir nehmen den Raum n nicht oder wir nehmen ihn und müssen den Raum n-1 überspringen
    return max(max_loot(house, n-1), house[n] + max_loot(house, n-2))
```

Die Laufzeit des obigen Algorithmus ist exponentiell in n, da wir für jedes n zwei Rekursionsaufrufe machen. Wir können
das Problem jedoch auch mit dynamischer Programmierung lösen. Dazu erstellen wir ein Memory, in dem wir die maximalen
Beuten für die Räume speichern. Wir können dann in jedem Schritt fragen, ob wir den Wert bereits berechnet haben und
ihn direkt zurückgeben.

```python
def dynamic_max_loot(house, n, mem={}):
    if n in mem:
        return mem[n]
    
    if n == 0:
        mem[n] = house[0]
    elif n == 1:
        mem[n] = max(house[0], house[1])
    else:
        mem[n] = max(dynamic_max_loot(house, n-1, mem), house[n] + dynamic_max_loot(house, n-2, mem))
    
    return mem[n]
```

---
[vorherige Seite](13_tupel_dictionaries_sets.md)  
[Zurück zum Inhaltsverzeichnis](00_inhaltsverzeichnis.md)  
[nächste Seite](15_oop.md)