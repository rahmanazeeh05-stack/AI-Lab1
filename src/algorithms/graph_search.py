import time
import threading
import sys
from algorithms.dfs import dfs_logic
from algorithms.astar import astar_logic


def dfs(
    state: tuple[int, ...], goal: tuple[int, ...] = (0, 1, 2, 3, 4, 5, 6, 7, 8)
) -> dict:
    nodes = []
    visited = {}
    path = []

    def worker():
        dfs_logic(state, 0, path, nodes, visited, goal, None)

    sys.setrecursionlimit(200_000)
    old_size = 0
    for mb in (256, 128, 64, 32, 16):  # try smaller sizes until one is accepted
        try:
            old_size = threading.stack_size(mb * 1024 * 1024)
            break
        except ValueError:
            continue
    start = time.perf_counter()
    try:
        th = threading.Thread(target=worker)
        th.start()
        th.join()
    finally:
        threading.stack_size(old_size)
    total_time = time.perf_counter() - start
    path.reverse()

    return {
        "path": path,
        "pathcost": len(path) - 1,
        "depth": max(visited.values(), default=0),
        "totaltime": total_time,
        "node_count": len(nodes),
    }


def astar(
    state: tuple[int, ...],
    mode: bool,
    goal: tuple[int, ...] = (0, 1, 2, 3, 4, 5, 6, 7, 8),
) -> dict:
    path = []
    node_info = {}
    node_count = 0

    start = time.perf_counter()
    node_count, depth = astar_logic(state, mode, path, node_info, goal, node_count)
    total_time = time.perf_counter() - start

    return {
        "path": path,
        "pathcost": node_info[goal]["g"],
        "depth": depth,  # Max depth is always where i found the goal
        "totaltime": total_time,
        "node_count": node_count,
    }
