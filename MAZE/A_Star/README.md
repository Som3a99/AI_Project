# A* Search Algorithm

This is a Python program that implements the A* search algorithm on a maze. The program uses the pyamaze module to create and display the maze, the agent, and the text labels.

## How it works

The program defines a function called A_star that takes two arguments: a maze object and an optional starting cell coordinates. If the starting cell is not given, it defaults to the bottom-right corner of the maze.

The function uses two lists to keep track of the explored and frontier cells, and two dictionaries to store the paths from each visited cell to its parent cell and from the starting cell to each visited cell. The function also calculates the heuristic distance of each cell to the goal cell using the Manhattan distance formula.

The function iterates through the frontier cells using a priority queue data structure, sorted by the sum of the cost of the path from the start to the current cell and the estimated cost of the path from the current cell to the goal cell. If the current cell is the goal cell, the function returns the path from the start to the goal, and the number of steps taken by the agent. If not, it adds the adjacent cells that are not walls and not explored to the frontier and explored lists, and updates the path and heuristic dictionaries. The function returns the list of cells visited during the search, and the two path dictionaries.

you can run the program using:

```command
python3 A_star.py
```

The program will create a random maze of size 10x10 and display it on a window. The agent will start from the bottom-right corner and move towards the top-left corner using the A* search algorithm. The visited cells will be colored in blue, and the decision points will be marked with a yellow dot. The path from the start to the goal will be shown in green. A text label will show the number of steps taken by the agent.

You can change the size of the maze by modifying the 'rows' and 'cols' variables in line 4 of 'A_star.py'. You can also change the starting cell by passing a different tuple to the A_star function in line 67 of 'A_star.py'.
