from typing import List, Tuple

b1 = [[0, 0, 0, 2, 0, 0],
      [1, 0, 1, 0, 0, 0],
      [0, 2, 0, 2, 0, 2],
      [0, 0, 0, 0, 0, 0],
      [1, 0, 0, 2, 0, 0],
      [0, 0, 1, 0, 0, 0]]

b2 = [[0, 1, 2, 0, 0, 2, 1, 1, 0, 1],
      [0, 2, 1, 2, 0, 0, 1, 0, 1, 1],
      [1, 2, 0, 0, 0, 0, 2, 1, 0, 2],
      [0, 1, 2, 0, 0, 1, 0, 0, 2, 0],
      [2, 0, 0, 0, 2, 0, 1, 2, 1, 0],
      [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 1, 0, 1, 1, 0],
      [0, 1, 1, 0, 1, 1, 0, 0, 0, 0],
      [1, 0, 1, 0, 0, 0, 0, 0, 2, 1],
      [1, 0, 2, 1, 0, 2, 2, 0, 2, 0]]

b3 = [[2, 1, 0, 0, 1, 0, 1, 1, 0, 1],
      [2, 0, 1, 2, 0, 0, 1, 0, 0, 0],
      [0, 2, 0, 0, 2, 0, 0, 0, 0, 2],
      [2, 0, 1, 0, 0, 0, 0, 0, 2, 0],
      [0, 0, 2, 0, 2, 1, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 0, 1, 0, 1, 0],
      [0, 0, 0, 0, 2, 0, 0, 0, 1, 2],
      [0, 0, 2, 0, 2, 0, 0, 0, 0, 0],
      [0, 2, 0, 0, 0, 0, 2, 0, 1, 0],
      [1, 1, 0, 1, 0, 2, 0, 0, 0, 2]]


def empty_cell(matrix: List[List[int]]) -> Tuple[int, int]:
    # sucht die erste leere Zelle und gibt die Koordinaten zurück.
    # Gibt -1, -1 zurück, wenn keine leere Zelle gefunden wurde
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                return i, j
    return -1, -1


def allowed(matrix: List[List[int]], r: int, c: int) -> bool:
    # Prüft, ob es einen Konflikt mit den Regeln aus der Aufgabenstellung gibt, siehe Bemerkungen bei den
    # Bedingungen.

    row = matrix[r]
    col = [matrix[i][c] for i in range(len(matrix))]

    def cond1(rc):
        # Checke, ob in einer Zeile oder Spalte die Zahl 1 oder 2 mehr als zweimal hintereinander vorkommt.
        for i in range(len(rc)-2):
            if rc[i] == rc[i+1] == rc[i+2] and rc[i] != 0:
                return False
        return True

    def cond2(rc):
        # Checke, ob in einer Zeile oder Spalte mehr als die Hälfte der Einträge 1 oder 2 sind.
        return rc.count(1) <= len(rc) // 2 and rc.count(2) <= len(rc) // 2

    return all([cond1(row), cond2(row), cond1(col), cond2(col)])


def complete_field(matrix: List[List[int]]) -> bool:

    y, x = empty_cell(matrix)
    if y == -1:
        # wenn keine leere Zelle mehr gefunden wird, ist das Spielfeld vollständig
        return True

    for stone in [1, 2]: # wir probieren beide Steine aus
        matrix[y][x] = stone

        # prüfen, ob die Bedingungen erfüllt sind und sich das Spielfeld rekursiv vervollständigen lässt
        if allowed(matrix, y, x):
            if complete_field(matrix):
                return True
        matrix[y][x] = 0  # Backtracking
    return False


for playing_field in [b1, b2, b3]:
    complete_field(playing_field)
    for line in playing_field:
        print(line)
    print()
