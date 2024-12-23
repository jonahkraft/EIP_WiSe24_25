# Breitensuche (Breadth-First Search, BFS)

Empfohlene Skills: [Datentypen und Operatoren](01_datentypen_operationen.md), [Kontrollstrukturen](02_kontrollstrukturen.md),
[Listen](04_listen.md), [Funktionen](09_funktionen.md), [Sets und Dictionaries](13_tupel_dictionaries_sets.md)

---

Die Breitensuche ist ein Algorithmus zur Durchsuchung oder Traversierung von Graphen oder Baumstrukturen. 
Sie beginnt an einem Startknoten und erkundet alle benachbarten Knoten auf der gleichen Ebene, bevor sie in 
die nächste Ebene übergeht. In dieser Version speichern wir auch den Vorgänger jedes Knotens, um später den Pfad 
zurückverfolgen zu können.


## Algorithmus

1. **Initialisierung**: Erstelle eine Warteschlange und füge den Startknoten hinzu. Erstelle eine Menge für 
besuchte Knoten und ein Dictionary für Vorgänger.
2. **Schleife**: Solange die Warteschlange nicht leer ist:
   - Entferne den vordersten Knoten aus der Warteschlange.
   - Überprüfe, ob dieser Knoten bereits besucht wurde:
     - Wenn nicht, verarbeite ihn.
     - Markiere den Knoten als besucht.
     - Speichere den aktuellen Knoten als Vorgänger für alle unbesuchten Nachbarknoten und füge diese zur Warteschlange hinzu.


## Code

```python
def bfs(graph, start):
    visited = set()  
    queue = []  
    predecessors = {}  
    queue.append(start)  

    while queue:
        vertex = queue.pop(0)

        if vertex not in visited:
            visited.add(vertex)
            
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    predecessors[neighbor] = vertex

    return predecessors


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

predecessors = bfs(graph, 'A')
print("Vorgänger:", predecessors)
```

Mithilfe des predecessors-dicts kann man jetzt den kürzesten Weg zwischen dem Startknoten und einem beliebigen anderen
Knoten ermitteln.

---

[vorherige Seite](14_dynamische_programmierung.md)  
[Zurück zum Inhaltsverzeichnis](00_inhaltsverzeichnis.md)  
[nächste Seite](16_oop.md)