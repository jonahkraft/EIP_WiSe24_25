from typing import List, Tuple


def read_maze(path: str) -> List[List[str]]:
    with open(path, 'r') as file:
        return [list(line.strip()) for line in file]


def draw_maze(maze: List[List[str]]) -> None:
    for line in maze:
        print("".join(line))


def find(maze: List[List[str]], s: str) -> tuple[int, int]:
    for i, line in enumerate(maze):
        for j, char in enumerate(line):
            if char == s:
                return i, j
    return -1, -1


def bfs(maze: List[List[str]], start: Tuple[int, int], dest: Tuple[int, int]) -> List[Tuple[int, int]] | None:
    n = len(maze)
    m = len(maze[0])
    queue = [start]
    visited = [[False for _ in range(m)] for _ in range(n)]  # ein Set wäre effizienter
    pred = [[(-1, -1) for _ in range(m)] for _ in range(n)]  # ein Dictionary wäre effizienter

    while len(queue) > 0:
        px, py = queue.pop(0)
        visited[px][py] = True

        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nx, ny = px + dx, py + dy

            if not visited[nx][ny] and maze[nx][ny] != "█":
                queue.append((nx, ny))
                pred[nx][ny] = (px, py)

    if not visited[dest[0]][dest[1]]:
        return None

    path = [dest]
    current_point = dest

    while True:
        pred_point = pred[current_point[0]][current_point[1]]
        path.append(pred_point)
        current_point = pred_point

        if current_point == start:
            break

    return path[::-1]


def draw_maze_with_path(maze: List[List[str]], path: List[Tuple[int, int]]) -> None:
    for px, py in path:
        if maze[px][py] not in ["S", "Z"]:
            maze[px][py] = "x"

    draw_maze(maze)


def main():
    m = read_maze("../../resources/maze.txt")
    path = bfs(m, find(m, "S"), find(m, "Z"))

    if path is not None:
        draw_maze_with_path(m, path)
    else:
        print("Kein Pfad gefunden")


if __name__ == '__main__':
    main()
