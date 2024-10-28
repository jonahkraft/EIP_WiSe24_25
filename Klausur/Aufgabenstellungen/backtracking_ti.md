## Ein Problem aus der technischen Informatik

Gegeben seien k Listen der Länge n, die ausschließlich Nullen und Einsen enthalten. Gesucht ist eine
minimale Teilmenge der Listen, sodass an jedem Index in (mindestens) einer der gewählten Listen eine 1 steht.

Beispiel:

[0, 1, 1, 0]

[1, 0, 0, 0]

[1, 1, 1, 0]

[0, 0, 0, 1]

Aufgabe 1: Schreiben Sie zunächst einen Algorithmus, der irgendeine Teilmenge findet, die die Eigenschaft erfüllt.

Lösung: [[0, 1, 1, 0], [1, 0, 0, 0], [0, 0, 0, 1]]

[Hier](../Muster/backtracking_ti_muster1.py) finden Sie die Musterlösung.

---

Aufgabe 2: Modifizieren Sie Ihre Lösung aus Aufgabe 1, sodass tatsächlich die minimale Teilmenge gefunden wird.

Lösung: [[1, 1, 1, 0], [0, 0, 0, 1]]

[Hier](../Muster/backtracking_ti_muster_2.py) finden Sie die Musterlösung.
