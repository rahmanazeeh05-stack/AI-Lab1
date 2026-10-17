import sys
import threading
import time


import helperfn

goal = (0, 1, 2, 3, 4, 5, 6, 7, 8)

ans = []


def dfs(grid: tuple[int, ...], visited: dict) -> bool:

    if grid == goal:
        ans.append(grid)
        return True

    visited[grid] = True

    children = helperfn.generate_neighbors(grid)

    for child in children:
        if child in visited:
            continue

        if dfs(child, visited):
            ans.append(grid)
            return True

    return False


def main():

    start = time.perf_counter_ns()
    grid = [[1, 0, 2], [3, 4, 5], [6, 7, 8]]
    flatted_grid = [item for row in grid for item in row]
    visited = {}

    dfs(tuple(flatted_grid), visited)
    for state in reversed(ans):
        for r in range(0, 9, 3):
            print(
                *state[r : r + 3]
            )  # Unpack the elements to print them separated by spaces without brackets
        print()

    print("moves:", len(ans) - 1)
    end = time.perf_counter_ns()
    print(end - start)


if __name__ == "__main__":
    """
    To prevent the stack overflow.
    A second thread is started to operate with 512MB, and the main thread sleeps
    """
    sys.setrecursionlimit(10**6)
    threading.stack_size(512 * 1024 * 1024)
    th = threading.Thread(target=main)
    th.start()
    th.join()
