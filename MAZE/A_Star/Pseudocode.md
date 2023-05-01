### A* Pseudocode

1. Set the order of exploration to W, N, S, E.
2. Push the start cell into the Frontier with priority equal to its heuristic distance to the goal.
3. Initialize an empty Explored list.
4. Repeat until the goal is reached or the Frontier is empty:
    1. Pop the cell with the highest priority from the Frontier and set it as the current cell.
    2. If the current cell is the goal cell, return the path to the goal and the number of steps taken by the agent.
    3. Add the current cell to the Explored list.
    4. For each direction in the order of exploration (ESNW):
        1. Compute the child cell in that direction.
        2. If the child cell is a wall, skip to the next direction.
        3. If the child cell is already in the Explored list, skip to the next direction.
        4. Update the cost of the path from the start to the child cell as the cost of the path from the start to the current cell plus the cost of the step from the current cell to the child cell.
        5. Calculate the heuristic distance of the child cell to the goal using the Manhattan distance formula.
        6. Set the priority of the child cell in the Frontier to the sum of the cost and the heuristic distance.
        7. Update the parent of the child cell to the current cell.
5. Return the list of cells visited during the search, and the number of steps taken by the agent if the goal was not found.
