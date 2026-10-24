from collections import deque
import helperfn
import time


def bfs(initial_state, goal_state):
    """
    implementing bfs on the states
    and should also have the reconstruction and rutime --->to do
    """
    start = time.perf_counter()
    frontier = deque()
    visited = set()
    parent = {}
    frontier.append(initial_state)
    visited.add(initial_state)
    parent[initial_state] = None
    node_count = 0
    while frontier:
        x = frontier.popleft()
        if x == goal_state:
            path = []

            current = x
            while current is not None:
                path.append(current)
                current = parent[current]
            totaltime = time.perf_counter() - start
            depth = len(path) - 1
            path.reverse()
            return {
                "depth": depth,
                "pathcost": depth,
                "node_count": node_count,
                "path": path,
                "totaltime": totaltime,
            }
        else:
            neighbors = helperfn.generate_neighbors(x)
            node_count += 1
            for neighbor in neighbors:
                if neighbor not in visited:
                    frontier.append(neighbor)
                    visited.add(neighbor)
                    parent[neighbor] = x
    return {
        "expanded_nodes": node_count,
        "search_depth": None,
        "path": None,
        "time": time.perf_counter() - start
    }
