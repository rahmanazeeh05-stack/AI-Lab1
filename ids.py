import time
import helperfn


def ids_helper(state, limit, depth, path, visited, goal_state):
    """
    this function helps ids and preforms dfs on every iteration

    """

    if state == goal_state:
        path.append(state)
        return True
    if depth == limit:
        return False
    visited[state] = True
    neighbors = helperfn.generate_neighbors(state)

    for neighbor in neighbors:
        if neighbor in visited:
            continue
        path.append(state)
        if ids_helper(neighbor, limit, depth + 1, path, visited, goal_state):
            return True
        path.pop()
    return False


def ids(initial_state, goal):
    start = time.perf_counter()
    limit = 0
    nodes = 0
    while True:
        visited = {}
        path = []

        if ids_helper(initial_state, limit, 0, path, visited, goal):

            return {
                "path": path,
                "depth": len(path) - 1,
                "totaltime": time.perf_counter() - start,
                "node_count": nodes,
            }
        nodes += len(visited)
        limit += 1


# to do: if found less depth-->replace
# total nodes?
