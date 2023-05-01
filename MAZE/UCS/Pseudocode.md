### UCS Pseudocode

1. Initialize Frontier with the start cell and its path cost 0.
2. Initialize an empty Explored list.
3. While Frontier is not empty:
    a. current_cell, current_cost = Frontier.pop the cell with the lowest cost.
    b. If current_cell is the goal cell, return the path from the start to the goal.
    c. Add current_cell to the Explored list.
    d. For each direction (ESNW):
        i. child_cell = Next possible cell
        ii. child_cost = Cost to move from current_cell to child_cell
        iii. total_cost = current_cost + child_cost
        iv. If child_cell is already in the Explored list with a lower cost, do nothing.
        v. Otherwise, if child_cell is not in the Frontier or total_cost is lower than the stored cost for child_cell:
            1. Add child_cell to the Frontier with its total_cost.
            2. Update the path from the start to child_cell with the path from the start to current_cell plus the move from current_cell to child_cell.
4. Return None if no path is found.
