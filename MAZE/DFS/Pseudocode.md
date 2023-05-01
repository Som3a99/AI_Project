## DFS Pseudocode
### Order = W -> N -> S -> E

1. Push the start cell onto the Frontier with a priority equal to the heuristic distance.
2. Initialize an empty Explored list.
3. Repeat until the goal is reached or the Frontier is empty:
   1. Pop the cell with the highest priority from the Frontier and set it as the current cell.
   2. If the current cell is the goal cell, return the path to the goal and the number of steps taken by the agent.
   3. Add the current cell to the Explored list.
   4. For each direction (ESNW):
      1. Compute the next possible cell in the given direction.
      2. If the next possible cell is a wall, skip to the next direction.
      3. If the next possible cell is already in the Explored list, skip to the next direction.
      4. Update the cost of the path from the start to the next possible cell.
      5. Calculate the heuristic distance of the next possible cell to the goal using the Manhattan distance formula.
      6. Set the priority of the next possible cell in the Frontier to the sum of the cost and the heuristic distance.
      7. Update the parent of the next possible cell to the current cell.
4. If the goal was not found, return the list of cells visited during the search and the number of steps taken by the agent.
