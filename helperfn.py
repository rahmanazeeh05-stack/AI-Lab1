def issolvable(intial_state):
    """
    this fun checks if the 8-puzzle is solvable

    """
    tiles = [tile for tile in intial_state]
    inversion = 0
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            if tiles[i] > tiles[j]:
                if tiles[i] != 0 and tiles[j] != 0:
                    inversion += 1

    return inversion % 2 == 0


def child(state, i, j):
    """
    helper function for swapping and generating the tuple

    """

    dir = list(state)
    dir[i], dir[j] = dir[j], dir[i]
    return tuple(dir)


def generate_neighbors(state):
    """
    this function validates and generates neighbors of
    a state and return list of tuples
    """

    neighbors = []
    x = state.index(0)
    if x not in (6, 7, 8):  # can move down
        neighbors.append(child(state, x, x + 3))

    if x not in (0, 1, 2):  # can move up
        neighbors.append(child(state, x, x - 3))
    if x not in (0, 3, 6):  # can move left
        neighbors.append(child(state, x, x - 1))
    if x not in (2, 5, 8):  # can move right
        neighbors.append(child(state, x, x + 1))
    return neighbors


def printing_path(path):
    for state in path:
        for r in range(0, 9, 3):
            print(*state[r : r + 3])
        print()


def result(result: dict):
    print("runtime: ", result["totaltime"], "seconds")
    print("path cost: ",result["pathcost"])
    print("Search depth:", result["depth"])
    print("Expanded nodes:", result["node_count"])
    printing_path(result["path"])
