import sys
import threading
import time


import helperfn


def dfs(
    state: tuple[int, ...],
    depth: int,
    path: list[tuple[int, ...]],
    nodes_expandend: list[tuple[int, ...]],
    visited: dict,
    goal: tuple[int, ...] = (0, 1, 2, 3, 4, 5, 6, 7, 8),
    limit: int | None = None,
) -> bool:

    if state == goal:
        path.append(state)
        return True

    if limit is not None and depth == limit:
        return False

    visited[state] = depth
    nodes_expandend.append(state)

    children = helperfn.generate_neighbors(state)

    for child in children:
        if child in visited:

            if limit is None or visited[child] <= depth + 1:
                continue

        if dfs(child, depth + 1, path, nodes_expandend, visited, goal, limit):
            path.append(state)
            return True

    return False


def main():

    start = time.perf_counter_ns()
    grid = [[1, 0, 2], [3, 4, 5], [6, 7, 8]]
    flatted_grid = [item for row in grid for item in row]
    visited = {}
    path = []
    nodes_expandend = []
    dfs(tuple(flatted_grid), 0, path, nodes_expandend, visited)
    for state in reversed(path):
        for r in range(0, 9, 3):
            print(
                *state[r : r + 3]
            )  # Unpack the elements to print them separated by spaces without brackets
        print()

    print("moves:", len(path) - 1)
    print(
        "nodes:", len(nodes_expandend)
    )  # Note goal is not appended in nodes_expandend
    end = time.perf_counter_ns()
    print(end - start)


if __name__ == "__main__":
    # To prevent the stack overflow.
    # A second thread is started to operate with 512MB, and the main thread sleeps
    sys.setrecursionlimit(10**6)
    threading.stack_size(512 * 1024 * 1024)
    th = threading.Thread(target=main)
    th.start()
    th.join()
