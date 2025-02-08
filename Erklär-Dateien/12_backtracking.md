# Backtracking

Empfohlene Skills: [Datentypen und Operatoren](01_datentypen_operationen.md), [Kontrollstrukturen](02_kontrollstrukturen.md)
und [Funktionen](09_funktionen.md). Für das Beispiel zusätzlich [zweidimensionale Listen](05_matrizen_2d_listen) und [List Comprehension](06_list_comprehension.md)

---

**Backtracking** ist eine allgemeine [rekursive](11_rekursion.md) Algorithmik, die zur Lösung von Problemen verwendet wird, bei denen eine 
inkrementelle Lösung aufgebaut wird und Schritte zurückgenommen werden, wenn eine Teillösung nicht zu einer 
gültigen Lösung führt. Das Verfahren durchsucht alle möglichen Lösungen eines Problems systematisch und nimmt 
dabei Rückschritte, um alternative Möglichkeiten zu testen.

Es wird häufig für Probleme verwendet, bei denen es viele mögliche Kombinationen gibt, wie z.B. in der Suche, 
beim Sortieren oder bei Entscheidungsproblemen. Klassische Beispiele für Backtracking sind **das N-Damen-Problem**, 
**das Rucksackproblem** und **Sudoku-Löser**.


## Aufbau eines Backtracking-Algorithmus

Ein Backtracking-Algorithmus besteht aus den folgenden Komponenten:

- **Basisfall**: Wenn das Problem vollständig gelöst ist, endet der Algorithmus und gibt die Lösung zurück.
- **Rekursiver Fall**: Der Algorithmus versucht, eine Lösung Schritt für Schritt aufzubauen, indem er mögliche Entscheidungen 
ausprobiert. Wenn eine Entscheidung zu keiner gültigen Lösung führt, wird ein Rückschritt gemacht (**Backtracking**), 
und es wird eine alternative Entscheidung getroffen.


### Grundlegender Ablauf:

1. **Lösung Schritt für Schritt aufbauen**.
2. **Überprüfen, ob die aktuelle Lösung gültig ist** (Teillösung prüfen).
3. **Wenn eine ungültige Lösung gefunden wird**, einen Schritt zurückgehen und eine alternative Entscheidung treffen.
4. **Abbruch**: Wenn eine vollständige gültige Lösung gefunden wird, endet der Algorithmus.

In Pseudocode sieht das so aus:

```
def vervollständige(Konfiguration K):
    if vollständig(K) then
        return True
    end

    for each Erweiterungsmöglichkeit E do
        erweitere (K, E)
        if zulässig(K) then
            if vervollständige(K) then
                return True
            end
        end
        mache rückgängig(K, E)
    end
    return False

```

## Beispiel: Tiefensuche (Depth-First Search)

Ein einfaches Beispiel für Backtracking ist die **Tiefensuche** (Depth-First Search, DFS) in einem gerichteten Graphen. 
Falls Sie sich nicht sicher sind, was ein gerichteter Graph ist, können Sie [hier](https://de.wikipedia.org/wiki/Gerichteter_Graph) mehr darüber erfahren.
Die Tiefensuche beginnt bei einem Startknoten und besucht alle benachbarten Knoten rekursiv, bevor sie sich weiterbewegt. 
Im folgenden Beispiel verwenden wir Tiefensuche, um zu prüfen, ob es einen Weg von einem Startknoten zu einem Zielknoten in einem gerichteten Graphen gibt.
Den Graphen repräsentieren wir als **Adjazenzliste**, wobei jeder Knoten eine Liste seiner Nachbarn hat. Als Datenstruktur
verwenden wir ein **Dictionary** in Python. [Hier](13_tupel_dictionaries_sets.md) können Sie mehr über Dictionaries erfahren.


```python
def dfs(graph, current, target, visited=None):
    if visited is None:
        visited = set()

    print(f"Besuche {current}")

    # zuerst prüfen wir, ob wir am Ziel sind. Das entspricht dem "if vollständig(K) then" im Pseudocode
    if current == target:
        return True

    # sicherstellen, dass jeder Knoten nur einmal besucht wird
    if current not in visited:
        visited.add(current)

        # rekursiv alle Nachbarn besuchen. Das entspricht dem "for each Erweiterungsmöglichkeit E do" im Pseudocode
        for neighbor in graph.get(current, []):
            # nur Nachbarn besuchen, die noch nicht besucht wurden. Das entspricht dem "if zulässig(K) then" im Pseudocode
            if neighbor not in visited:
                # rekursiver Aufruf für den Nachbarn. Das entspricht dem "vervollständige(K)" im Pseudocode
                if dfs(graph, neighbor, target, visited):
                    return True
        
        # Ein expliziter Rückgabewert False ist notwendig, wenn kein Weg gefunden wurde. Dies liegt daran, dass wir automatisch
        # zum vorherigen Knoten zurückkehren, wenn der rekursive Aufruf False zurückgibt. Ein etwaiger Backtracking-Schritt
        # entspricht dem "mache rückgängig(K, E)" im Pseudocode

    return False


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['B'],
    'D': ['C'],
    'E': ['F'],
    'F': ['A']
}

print(dfs(graph, 'A', 'F'))
```

---

[vorherige Seite](11_rekursion.md)  
[Zurück zum Inhaltsverzeichnis](00_inhaltsverzeichnis.md)  
[nächste Seite](13_tupel_dictionaries_sets.md)