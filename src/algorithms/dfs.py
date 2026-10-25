import utils.helperfn as helperfn


def dfs_logic(
    state: tuple[int, ...],
    depth: int,
    path: list[tuple[int, ...]],
    nodes_expandend: list[tuple[int, ...]],
    visited: dict,
    goal: tuple[int, ...] = (0, 1, 2, 3, 4, 5, 6, 7, 8),
    limit: int | None = None,
) -> bool:

    if state == goal:
        visited[state] = depth  # Includeing the goal state in the depth
        path.append(state)
        nodes_expandend.append(state)
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

        if dfs_logic(child, depth + 1, path, nodes_expandend, visited, goal, limit):
            path.append(state)
            return True

    return False
