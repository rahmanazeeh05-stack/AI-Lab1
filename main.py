# shouldn't stay for long, was just testing my bfs logic

import helperfn
import bfs

initial_state = (8, 6, 7, 2, 5, 4, 3, 0, 1)

goal_state = (0, 1, 2, 3, 4, 5, 6, 7, 8)

if helperfn.issolvable(initial_state):
    result = bfs.bfs(initial_state, goal_state)
    print("Expanded nodes:", result["node_count"])
    print("Search depth:", result["depth"])
else:
    print("unsolvable")
