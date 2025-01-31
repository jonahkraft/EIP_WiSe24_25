# Eine einfache Implementierung des Algorithmus "Tiefensuche"
# Tiefensuche ist nicht dazu geeignet, kürzeste Wege zu finden, dafür kann man Breitensuche verwenden (vgl. Bonusaufgaben)


def read_map(filename: str) -> list[list[str]]:
    maze = []

    with open(filename, 'r') as f:
        for line in f:
            maze.append([char for char in line][:-1])
        return maze


def find_cell(maze: list[list[str]], char: str) -> (int, int):
    # sucht ein Symbol in dem Labyrinth und gibt den Zeilen- und Spaltenindex als Tupel nicht negativer Zahlen zurück,
    # falls es vorhanden ist und sonst -1, -1
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == char:
                return i, j
    return -1, -1


def find_way(maze: list[list[str]], path: list[(int, int)]) -> list[(int, int)]:
    # um es gemäß den Vorgaben auf dem Blatt umzusetzen, erwartet die Funktion, dass der Pfad bereits den Startpunkt
    # enthält

    def is_valid(maze: list[list[str]], i: int, j: int) -> bool:
        # wir dürfen uns nicht außerhalb des Labyrinths bewegen und es dürfen nur Felder betreten werden, die
        # keine Wand sind und noch nicht besucht wurden.
        return 0 <= i < len(maze) and 0 <= j < len(maze[i]) and maze[i][j] in (" ", "A")

    current_i, current_j = path[-1]  # aktuelle Position

    if maze[current_i][current_j] == "A":
        # wenn das der Fall ist, sind wir am Ziel angekommen
        return path

    maze[current_i][current_j] = "B"  # wir markieren die aktuelle Zelle als besucht

    for direction_i, direction_j in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        # das sind alle möglichen Schritte, jeweils durch Richtungsvektoren dargestellt
        # wir berechnen die nächste Position
        next_i, next_j = current_i + direction_i, current_j + direction_j

        if is_valid(maze, next_i, next_j):
            path.append((next_i, next_j))

            # rekursiver Aufruf, um den Weg zu finden
            full_path = find_way(maze, path)

            if len(full_path) > 0:
                # dann wurde ein Weg basierend auf den aktuell besuchten Feldern gefunden und wir können ihn zurückgeben
                return full_path

            # Wenn wir hier ankommen, hat die aktuelle Konfiguration dazu geführt, dass kein Weg gefunden werden konnte.
            # Wir machen den Backtracking-Schritt und gehen ein Feld zurück.
            del path[-1]

    # wenn wir hier ankommen, wurde kein Weg gefunden
    return []


def main():
    maze = read_map('maze_big.txt')
    path = [find_cell(maze, 'E')]
    print(find_way(maze, path))

    for line in maze:
        print("".join(line))


if __name__ == '__main__':
    main()
