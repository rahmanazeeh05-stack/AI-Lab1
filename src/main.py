import utils.helperfn as helperfn
from algorithms.bfs import bfs
from algorithms.ids import ids
from algorithms.graph_search import dfs, astar

goal = (0, 1, 2, 3, 4, 5, 6, 7, 8)

algorithms = {
    1: "bfs",
    2: "dfs",
    3: "ids",
    4: "a* (Manhattan)",
    5: "a* (Euclidean)",
}


def solve(state, choice):
    """do the chosen search algorithm and return the result dictionary"""
    if choice == 1:
        return bfs(state, goal)
    if choice == 2:
        return dfs(state, goal)
    if choice == 3:
        return ids(state, goal)
    if choice == 4:
        return astar(state, True, goal)
    return astar(state, False, goal)


def read_state(text):
    """convert state into a tuple. if invalid raise error"""
    state = tuple(int(x) for x in text.replace(",", " ").split())
    if sorted(state) != list(range(9)):
        raise ValueError("Enter each number from 0 to 8 exactly once.")
    if not helperfn.issolvable(state):
        raise ValueError("This puzzle is not solvable.")
    return state


def print_board(state):
    for r in range(0, 9, 3):
        print(" ".join(str(t) for t in state[r : r + 3]))


def main():

    while True:
        try:
            state = read_state(input("enter initial state (ex: 1,2,5,3,4,0,6,7,8: "))
            break
        except ValueError as e:
            print("Error:", e)

    for k, name in algorithms.items():
        print(f"{k}. {name}")
    choice = 0
    while choice not in algorithms:
        text = input("Choose algorithm (1-5): ")
        choice = int(text) if text.isdigit() else 0

    result = solve(state, choice)
    print(f"\n{algorithms[choice]} - path to goal:\n")
    for i, step in enumerate(result["path"]):
        print("Initial state:" if i == 0 else f"Step {i}:")
        print_board(step)
        print()

    print("path cost     :", result["pathcost"])
    print("nodes expanded:", result["node_count"])
    print("search depth  :", result["depth"])
    print("running time  :", result["totaltime"], "seconds")


if __name__ == "__main__":
    main()
