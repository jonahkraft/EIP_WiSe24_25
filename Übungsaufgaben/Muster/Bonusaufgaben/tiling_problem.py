import math
from typing import List


def tile(matrix: List[List[str]], m: int, x: int, y: int, counter: int) -> int:
    """
    :param matrix: die gesamte Matrix
    :param m: die Dimension der Teilmatrizen, die einzeln parkettiert werden
    :param x: die x-Koordinate des oberen linken Punkts
    :param y: die y-Koordinate des oberen linken Punkts
    :param counter: eine Zähler-Variable, die die Anzahl der Parkettierungen speichert
    :return: der Zählerstand nach der aktuellen Parkettierung
    """

    if m == 1:
        return counter

    max_x = x + m - 1
    max_y = y + m - 1
    mid_x = (max_x + x) // 2
    mid_y = (max_y + y) // 2

    # Wir wollen die aktuell betrachtete Teilmatrix in 4 neue Teilmatrizen aufteilen. In einem der 4 Teilmatrizen ist
    # bereits eine Zelle belegt.

    px = py = -1

    for i in range(x, max_x+1):
        for j in range(y, max_y+1):
            if matrix[j][i] != ".":
                px = i
                py = j
                break

    # Markierung der Punkte, mit dem aktuellen Counter, die an den inneren Zellen derjenigen Teilmatrizen sind,
    # in denen nichts markiert wurde.

    if not (x <= px <= mid_x and y <= py <= mid_y):
        matrix[mid_y][mid_x] = str(counter)
    if not (mid_x + 1 <= px <= max_x and y <= py <= mid_y):
        matrix[mid_y][mid_x + 1] = str(counter)
    if not(x <= px <= mid_x and mid_y + 1 <= py <= max_y):
        matrix[mid_y + 1][mid_x] = str(counter)
    if not (mid_x + 1 <= px <= max_x and mid_y + 1 <= py <= max_y):
        matrix[mid_y + 1][mid_x + 1] = str(counter)

    counter += 1

    # Rekursiv die 4 Quadranten parkettieren (gegen den Uhrzeigersinn, Start oben rechts)
    counter = tile(matrix, m // 2, mid_x + 1, y, counter)
    counter = tile(matrix, m // 2, x, y, counter)
    counter = tile(matrix, m // 2, x, mid_y + 1, counter)
    counter = tile(matrix, m // 2, mid_x + 1, mid_y + 1, counter)

    return counter


def main():
    n = 2 ** 6
    matrix = [["." for _ in range(n)] for _ in range(n)]
    matrix[2][n - 2] = "x"
    c = tile(matrix, n, 0, 0, 1)

    len_c = math.ceil(math.log10(c))  # Länge der höchsten Zahl in der Matrix

    for line in matrix:
        print("".join([f"{" " * (len_c-len(char))}{char} " for char in line]))


if __name__ == '__main__':
    main()
