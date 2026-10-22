from heuristic import heuristic
import helperfn
import heapq


def astar(
    initial_state: tuple[int, ...],
    mode: bool,
    goal: tuple[int, ...] = (0, 1, 2, 3, 4, 5, 6, 7, 8),
) -> tuple[list[tuple[int, ...]], list[tuple[int, ...]]]:
    node_info = {}

    nodes_expanded = []
    h = heuristic(initial_state, mode)

    node_info[initial_state] = {"g": 0, "parent": None}

    frontier = []

    heapq.heappush(frontier, (h, 0, initial_state))

    while frontier:

        _, g, current_state = heapq.heappop(frontier)
        if (
            g > node_info[current_state]["g"]
        ):  # Take alawys the smaller and ignore the bigger
            # You can compere the f but for the same state the h is constant so the g has all the information about the state
            continue
        nodes_expanded.append(current_state)
        if current_state == goal:
            break

        children = helperfn.generate_neighbors(current_state)

        for child in children:

            new_g = g + 1
            if (
                child in node_info and new_g >= node_info[child]["g"]
            ):  # Take the smallest g
                continue

            h = heuristic(child, mode)
            f = h + new_g

            heapq.heappush(frontier, (f, new_g, child))
            node_info[child] = {"g": new_g, "parent": current_state}

    path = []
    trace = goal
    while trace is not None:
        path.append(trace)
        trace = node_info[trace]["parent"]

    path.reverse()
    return path, nodes_expanded
