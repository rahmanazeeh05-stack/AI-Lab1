from math import hypot


def manhattan(state: tuple[int, ...]) -> int:
    h = 0
    for i, tile in enumerate(state):
        if tile == 0:  # Donot count it to aboid the overestimatetion
            continue

        current_row = i // 3
        current_col = i % 3

        target_row = tile // 3
        target_col = tile % 3

        h += abs(current_row - target_row) + abs(current_col - target_col)

    return h


def euclidean(state: tuple[int, ...]) -> float:
    h = 0
    for i, tile in enumerate(state):
        if tile == 0:
            continue

        current_row = i // 3
        current_col = i % 3

        target_row = tile // 3
        target_col = tile % 3

        h += hypot((current_row - target_row), (current_col - target_col))

    return h


def heuristic(state, mode):
    if mode:
        return manhattan(state)
    else:
        return euclidean(state)
