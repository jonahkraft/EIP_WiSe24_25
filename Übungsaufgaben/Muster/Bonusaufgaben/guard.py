import time
from typing import List, Tuple

def read_file(path: str) -> List[List[str]]:
    with open(path, "r") as file:
        return [[char for char in row.strip()] for row in file]


def print_matrix(matrix: List[List[str]]) -> None:
    time.sleep(0.5)
    for row in matrix:
        print("".join(row))
    print()


def is_in_bounds(matrix: List[List[str]], pos: Tuple[int, int]) -> bool:
    if pos[0] < 0 or pos[0] >= len(matrix):
        return False
    if pos[1] < 0 or pos[1] >= len(matrix[pos[0]]):
        return False
    return True


def get_nex_pos(pos: Tuple[int, int], direction: Tuple[int, int]) -> Tuple[int, int]:
    return pos[0] + direction[0], pos[1] + direction[1]


def update_matrix(matrix: List[List[str]], old_pos: Tuple[int, int], new_pos: Tuple[int, int], dir_symbol: str) -> None:
    set_cell(matrix, old_pos, ".")
    set_cell(matrix, new_pos, dir_symbol)


def change_direction(direction: Tuple[int, int]) -> Tuple[int, int]:
    match direction:
        case (-1, 0):  # top
            return 0, 1
        case (0, -1):  # left
            return -1, 0
        case (1, 0):  # bottom
            return 0, -1
        case (0, 1):  # right
            return 1, 0


def get_cell(matrix: List[List[str]], pos: Tuple[int, int]) -> str:
    return matrix[pos[0]][pos[1]]


def set_cell(matrix: List[List[str]], pos: Tuple[int, int], item: str) -> None:
    matrix[pos[0]][pos[1]] = item


def get_dir_symbol(direction: Tuple[int, int]) -> str:
    match direction:
        case (-1, 0):
            return "^"
        case (0, -1):
            return "<"
        case (1, 0):
            return "v"
        case (0, 1):
            return ">"


def teleport(matrix: List[List[str]], pos: Tuple[int, int]) -> Tuple[int, int]:
    i = pos[0]
    j = pos[1]

    if i == -1:
        i = len(matrix) - 1
    elif i == len(matrix):
        i = 0

    if j == -1:
        j = len(matrix[i]) - 1
    elif j == len(matrix[i]):
        j = 0

    return i, j


def main():
    matrix = read_file("../../resources/guard.txt")

    pos = (-1, -1)
    direction = (-1, 0)

    for i, line in enumerate(matrix):
        for j, char in enumerate(line):
            if char == "^":
                pos = i, j

    while True:
        next_pos = get_nex_pos(pos, direction)

        if not is_in_bounds(matrix, next_pos):
            next_pos = teleport(matrix, next_pos)

        if get_cell(matrix, next_pos) == "#":
            direction = change_direction(direction)
            update_matrix(matrix, pos, pos, get_dir_symbol(direction))
        else:
            update_matrix(matrix, pos, next_pos, get_dir_symbol(direction))
            pos = next_pos

        print_matrix(matrix)


if __name__ == '__main__':
    main()
