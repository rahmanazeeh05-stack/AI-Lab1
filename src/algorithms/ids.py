import time
import utils.helperfn as helperfn
import algorithms.dfs as dfs


def ids(initial_state, goal):
    start = time.perf_counter()
    limit = 0
    nodes = []
    while True:
        visited = {}
        path = []

        found = dfs.dfs_logic(initial_state, 0, path, nodes, visited, goal, limit)
        totalnodes = len(nodes)
        if found:
            path.reverse()
            return {
                "path": path,
                "pathcost": len(path) - 1,
                "depth": len(path) - 1,
                "totaltime": time.perf_counter() - start,
                "node_count": totalnodes,
            }

        limit += 1
