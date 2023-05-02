## BFS Pseudocode

### Order = W -> N -> S -> E

1. Add the start cell to the Frontier queue.
2. Initialize an empty Explored set.
3. Repeat until the goal is reached or the Frontier is empty:
   1. Dequeue the first cell in the Frontier and set it as the current cell.
   2. If the current cell is the goal cell, return the path to the goal and the number of steps taken by the agent.
   3. Add the current cell to the Explored set.
   4. For each direction (ESNW):
      1. Compute the next possible cell in the given direction.
      2. If the next possible cell is a wall, skip to the next direction.
      3. If the next possible cell is already in the Explored set, skip to the next direction.
      4. If the next possible cell is not in the Frontier queue, add it to the Frontier queue.
      5. Update the parent of the next possible cell to the current cell.
4. If the goal was not found, return the list of cells visited during the search and the number of steps taken by the agent.
