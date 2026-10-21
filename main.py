# shouldn't stay for long, was just testing my bfs/ids logic
import helperfn
import bfs
import ids

initial_state = (1, 2, 3, 4, 0, 5, 6, 7, 8)

goal_state = (0, 1, 2, 3, 4, 5, 6, 7, 8)

# if helperfn.issolvable(initial_state):
#   result = bfs.bfs(initial_state, goal_state)
#  helperfn.result_bfs(result)
# else:
#   print("unsolvable")

if helperfn.issolvable(initial_state):
    result = ids.ids(initial_state, goal_state)
    helperfn.result(result)
else:
    print("unsolvable")
