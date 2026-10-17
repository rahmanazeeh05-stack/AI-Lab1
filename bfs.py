from collections import deque
import helperfn


def bfs(initial_state, goal_state):
    """
    implementing bfs on the states
    and should also have the reconstruction and rutime --->to do
    """

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
            depth = 0
            current = x
            while current is not None:
                depth += 1
                current = parent[current]
            return {"depth": depth, "node_count": node_count}
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
    }
