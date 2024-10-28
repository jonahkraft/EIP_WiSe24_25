# Backtracking

Empfohlene Skills: [Datentypen und Operatoren](01_datentypen_operationen.md), [Kontrollstrukturen](02_kontrollstrukturen.md)
und [Funktionen](09_funktionen.md). Für das Beispiel zusätzlich [zweidimensionale Listen](05_2d_listen.md) und [List Comprehension](06_list_comprehension.md)

---

**Backtracking** ist eine allgemeine [rekursive](11_rekursion.md) Algorithmik, die zur Lösung von Problemen verwendet wird, bei denen eine 
inkrementelle Lösung aufgebaut wird und Schritte zurückgenommen werden, wenn eine Teillösung nicht zu einer 
gültigen Lösung führt. Das Verfahren durchsucht alle möglichen Lösungen eines Problems systematisch und nimmt 
dabei Rückschritte, um alternative Möglichkeiten zu testen.

Es wird häufig für Probleme verwendet, bei denen es viele mögliche Kombinationen gibt, wie z.B. in der Suche, 
beim Sortieren oder bei Entscheidungsproblemen. Klassische Beispiele für Backtracking sind **das N-Damen-Problem**, 
**das Rucksackproblem** und **Sudoku-Löser**.

---

## Aufbau eines Backtracking-Algorithmus

Ein Backtracking-Algorithmus besteht aus den folgenden Komponenten:

- **Basisfall (Abbruchbedingung)**: Wenn das Problem vollständig gelöst ist, endet der Algorithmus und gibt die Lösung zurück.
- **Rekursiver Fall**: Der Algorithmus versucht, eine Lösung Schritt für Schritt aufzubauen, indem er mögliche Entscheidungen 
- ausprobiert. Wenn eine Entscheidung zu keiner gültigen Lösung führt, wird ein Rückschritt gemacht (**Backtracking**), 
- und es wird eine alternative Entscheidung getroffen.

---

### Grundlegender Ablauf:

1. **Lösung Schritt für Schritt aufbauen**.
2. **Überprüfen, ob die aktuelle Lösung gültig ist** (Teillösung prüfen).
3. **Wenn eine ungültige Lösung gefunden wird**, einen Schritt zurückgehen und eine alternative Entscheidung treffen.
4. **Abbruch**: Wenn eine vollständige gültige Lösung gefunden wird, endet der Algorithmus.

---

#### Pseudocode:

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

---

## Beispiel: Das N-Damen-Problem

Beim **N-Damen-Problem** geht es darum, `N` Damen auf einem `N x N`-Schachbrett so zu platzieren, 
dass keine zwei Damen sich gegenseitig angreifen können (weder in derselben Zeile, Spalte noch Diagonale). 
Backtracking ist eine Methode, dieses Problem zu lösen.

```python
def is_safe(board, row, col, n):
    # Check if it's safe to place the queen at (row, col)

    # Check left side in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col, n):
    # Base case: If all queens are placed, return True
    if col >= n:
        return True

    # Try placing a queen in each row
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place the queen
            board[i][col] = 1

            # Recursion: Try to place the next queen
            if solve_n_queens(board, col + 1, n):
                return True

            # Backtracking: Remove the queen (as no solution was found)
            board[i][col] = 0

    # If no solution is found, return False
    return False

def n_queens_problem(n):
    # Create an N x N chessboard (initially empty, i.e., 0)
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_n_queens(board, 0, n):
        print("No solution exists")
        return False

    # Output the solution
    for row in board:
        print(row)
    return True

# Example: Solve the 4-Queens problem
n_queens_problem(4)
```

### Erklärung des Algorithmus:

1. Der Algorithmus platziert eine Dame in jeder Spalte, indem er in jeder Zeile prüft, ob die Position sicher ist.
2. Wenn eine Dame platziert wird, wird rekursiv versucht, die nächste Dame zu platzieren.
3. Wenn keine gültige Platzierung möglich ist, wird das Backtracking durchgeführt (die letzte Platzierung wird entfernt), und eine alternative Platzierung wird getestet.
4. Wenn alle Damen platziert sind, gibt der Algorithmus die Lösung zurück.

---

## Zusammenfassung

- **Backtracking** ist eine Methode zur systematischen Suche nach Lösungen, indem Entscheidungen getroffen und ggf. 
- rückgängig gemacht werden.
- Es wird häufig für Entscheidungsprobleme wie das N-Damen-Problem, Sudoku oder das Rucksackproblem verwendet.
- Backtracking basiert auf rekursiven Funktionsaufrufen, bei denen eine Lösung Schritt für Schritt aufgebaut und bei 
- ungültigen Schritten rückwärts gegangen wird.

---

[vorherige Seite](11_rekursion.md)  
[Zurück zum Inhaltsverzeichnis](00_inhaltsverzeichnis.md)  
[nächste Seite](13_tupel_dictionaries_sets.md)