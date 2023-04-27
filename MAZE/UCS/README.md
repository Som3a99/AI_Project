# Uniform-Cost Search Algorithm

This is a Python program that implements the Uniform-Cost Search (UCS) algorithm on a maze. The program uses the pyamaze module to create and display the maze, the agent, and the text labels.

## How it works

The program defines a function called UCS that takes two arguments: a maze object and an optional starting cell coordinates. If the starting cell is not given, it defaults to the bottom-right corner of the maze.

The function uses two lists to keep track of the explored and frontier cells, and two dictionaries to store the paths from each visited cell to its parent cell and the cost to reach the visited cell. The function also marks the cells that have more than one possible direction to go as decision points.

The function iterates through the frontier cells using a priority queue data structure, which sorts the cells by their accumulated cost. The accumulated cost of a cell is the cost to reach its parent cell plus the cost to move from the parent cell to the current cell. If a cell has already been visited and the new accumulated cost is lower than the stored cost, the function updates the path dictionary and the accumulated cost.

The function continues to explore the frontier cells until it reaches the goal cell or until there are no more cells to explore. The function returns the list of cells visited during the search, and the two path dictionaries.

you can run the program using:

```command
python3 UCS.py
```

The program will create a random maze of size 10x10 and display it on a window. The agent will start from the bottom-right corner and move towards the top-left corner using the UCS algorithm. The visited cells will be colored in blue, and the decision points will be marked with a yellow dot. The path from the start to the goal will be shown in green. A text label will show the number of steps taken by the agent.

You can change the size of the maze by modifying the 'rows' and 'cols' variables in line 4 of 'UCS.py'. You can also change the starting cell by passing a different tuple to the UCS function in line 67 of 'UCS.py'.
