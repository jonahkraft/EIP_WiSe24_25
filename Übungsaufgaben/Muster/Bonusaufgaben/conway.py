import copy
import time
from typing import List


def read_file(path: str) -> List[List[str]]:
    with open(path, "r") as file:
        return [[char for char in row.strip()] for row in file]


def print_matrix(matrix: List[List[str]]) -> None:
    time.sleep(0.5)

    for row in matrix:
        print("".join(row))
    print()


def main(cycles: int) -> None:
    matrix = read_file("../../resources/conway.txt")
    n = len(matrix)
    m = len(matrix[0])
    next_matrix = [["." for _ in range(m)] for _ in range(n)]

    for _ in range(cycles):
        print_matrix(matrix)

        for i, row in enumerate(matrix):
            for j, char in enumerate(row):

                alive = char == "o"

                neighbours = [matrix[i_][j_]
                              for i_ in range(max(0, i-1), min(i+2, n))
                              for j_ in range(max(0, j-1), min(j+2, m))
                              if not (i_ == i and j_ == j)]

                neighbours_alive = sum(1 for char in neighbours if char == "o")

                if alive:
                    if neighbours_alive in [2, 3]:
                        next_matrix[i][j] = "o"
                    else:
                        next_matrix[i][j] = "."
                else:
                    if neighbours_alive == 3:
                        next_matrix[i][j] = "o"
                    else:
                        next_matrix[i][j] = "."

        matrix = copy.deepcopy(next_matrix)

    print_matrix(matrix)


if __name__ == '__main__':
    main(100)
