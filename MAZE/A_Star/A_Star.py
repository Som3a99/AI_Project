from pyamaze import maze, agent, COLOR, textLabel
from queue import PriorityQueue

def h(cell1, cell2):

    """
    Calculates the Manhattan distance between two cells.

    Args:
        cell1 (tuple): The coordinates of the first cell.
        cell2 (tuple): The coordinates of the second cell.

    Returns:
        (int): The Manhattan distance between the two cells.
    """

    x1, y1 = cell1
    x2, y2 = cell2
    return (abs(x1 - x2) + abs(y1 - y2))

def aStar(m, start=None):

    """
    Implements the A* search algorithm.

    Args:
        m (maze): The maze object.
        start (tuple): The starting cell coordinates.

    Returns:
        searchPath (list): The list of cells visited during the search.
        aPath (dict): The dictionary of paths from each visited cell to its parent cell.
        fwdPath (dict): The dictionary of paths from the starting cell to each visited cell.
    """

   # If no starting point is given, use the bottom-right corner of the maze
    if start is None:
        start = (m.rows, m.cols)
    
    # Create a priority queue and add the starting point to it
    open = PriorityQueue()
    open.put((h(start, m._goal), h(start, m._goal), start))
    
    # Initialize the dictionaries for the path and the scores
    aPath = {}
    g_score = {row: float("inf") for row in m.grid}
    g_score[start] = 0
    f_score = {row: float("inf") for row in m.grid}
    f_score[start] = h(start, m._goal)
    
    # Initialize the list for the search path
    searchPath = [start]
    
    # Run the main loop
    while not open.empty():
        # Get the cell with the lowest f-score from the priority queue
        currCell = open.get()[2]
        searchPath.append(currCell)
        
        # If we've reached the goal, exit the loop
        if currCell == m._goal:
            break
        
        # Loop through the neighbors of the current cell
        for d in 'ESNW':
            if m.maze_map[currCell][d]:
                if d == 'E':
                    childCell = (currCell[0], currCell[1]+1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1]-1)
                elif d == 'N':
                    childCell = (currCell[0]-1, currCell[1])
                elif d == 'S':
                    childCell = (currCell[0]+1, currCell[1])
                
                # Calculate the scores for the neighbor
                temp_g_score = g_score[currCell] + 1
                temp_f_score = temp_g_score + h(childCell, m._goal)
                
                # If the neighbor has not been evaluated before, or if the new score is better,
                # update the dictionaries and add the neighbor to the priority queue
                if temp_f_score < f_score[childCell]:   
                    aPath[childCell] = currCell
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_g_score + h(childCell, m._goal)
                    open.put((f_score[childCell], h(childCell, m._goal), childCell))
    
    # Reconstruct the forward and backward paths
    fwdPath = {}
    cell = m._goal
    while cell != start:
        fwdPath[aPath[cell]] = cell
        cell = aPath[cell]
    
    # Return the search path, the forward path, and the backward path
    return searchPath, aPath, fwdPath

# If the script is run directly, create a maze and run the A* algorithm on it
if __name__ == '__main__':
    # Create the maze object and load the maze from a file
    m = maze()
    # Load the maze from a csv file
    m.CreateMaze(loadMaze = 'Maze.csv')

    # Run the A* algorithm on the maze
searchPath,aPath,fwdPath=aStar(m)

# Create three agents with different colors and settings
a = agent(m, footprints = True, color = COLOR.blue, filled = True, shape = 'arrow')
b = agent(m, 1, 1, footprints = True, color = COLOR.yellow, filled = True, goal = (m.rows, m.cols))
c=agent(m,footprints=True,color=COLOR.red)

# Trace the search path of agent a on the maze with a delay of 300ms and show marked cells
m.tracePath({a:searchPath},delay = 300, showMarked = True)
# Trace the path of agent b using the A* path calculated earlier with a delay of 300ms
m.tracePath({b:aPath},delay = 300)
# Trace the reverse path of agent c from the goal to the start using the A* path calculated earlier with a delay of 300ms
m.tracePath({c:fwdPath},delay = 300)

# Add two text labels to the maze object with the path length and search length of A* algorithm
l = textLabel(m,'A Star Path Length', len(fwdPath)+1)
l = textLabel(m,'A Star Search Length', len(searchPath))

# Add text labels to the maze object with the names of the creators
created_by_label = textLabel(m, 'Created By ', 'MohamedIsmail, MohamedSamy, YassminAhmed, SalwaAhmed')
label = textLabel(m,'and', 'ShaimaAbdelHamid')

# Run the maze object to start the visualization
m.run()
