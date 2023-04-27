# Import the necessary libraries
from pyamaze import maze, agent, textLabel, COLOR
import heapq

# Define the UCS function
def UCS(m, start=None):
    """
    This function implements the Uniform Cost Search (UCS) algorithm.

    Args:
        m (maze): The maze object.
        start (tuple): The starting cell coordinates.

    Returns:
        ucs_Search (list): The list of cells visited during the search.
        ucs_path (dict): The dictionary of paths from each visited cell to its parent cell.
        forward_path (dict): The dictionary of paths from the starting cell to each visited cell.
    """
    
    # If the starting cell is not specified, set it to the bottom right cell of the maze
    if start is None:
        start = (m.rows, m.cols)
    
    # Initialize the list of explored cells and the heap of frontier cells with the starting cell
    explored = [start]
    frontier = [(0, start)]
    
    # Initialize the dictionaries for the paths from each visited cell to its parent and the path from the starting cell to each visited cell
    ucs_path = {}
    ucs_Search = []
    
    # Perform the UCS search
    while len(frontier) > 0:
        # Pop the cell with the lowest cost from the frontier heap
        current_cost, current_cell = heapq.heappop(frontier)
        ucs_Search.append(current_cell)
        
        # Check if the current cell is the goal cell, and break the loop if it is
        if current_cell == m._goal:
            break
        
        # Iterate over the four possible directions to move from the current cell
        for destination in 'ESNW':
            # If there is a wall in the direction
            if m.maze_map[current_cell][destination] == True:
            # Calculate the coordinates of the child cell based on the direction
                if destination == 'E':
                    child = (current_cell[0], current_cell[1] + 1)
                elif destination == 'W':
                    child = (current_cell[0], current_cell[1] - 1)
                elif destination == 'N':
                    child = (current_cell[0] - 1, current_cell[1])
                elif destination == 'S':
                    child = (current_cell[0] + 1, current_cell[1])
                
            # If the child cell has already been explored, skip it
                if child in explored:
                    continue
                    
                # Calculate the cost to move to the child cell
                child_cost = current_cost + 1
            
                # Add the child cell to the explored list, and update the ucs_path and frontier heap
                explored.append(child)
                ucs_path[child] = current_cell
                heapq.heappush(frontier, (child_cost, child))
        
    # Initialize the forward_path dictionary for tracing the path from the starting cell to each visited cell
    forward_path = {}
    cell = m._goal
    
    # Trace the path from the goal cell to the starting cell using the ucs_path dictionary
    while cell != start:
        forward_path[ucs_path[cell]] = cell
        cell = ucs_path[cell]
    
    # Return the ucs_Search list, ucs_path dictionary, and forward_path dictionary
    return ucs_Search, ucs_path, forward_path

# Main function
if __name__ == '__main__':
    # Create a maze object with dimensions 10x10
    maze_obj = maze(10, 10)
    # Create a maze with a starting point at (2,4) and a dark theme
    maze_obj.CreateMaze(loadMaze = 'Maze.csv', theme = COLOR.dark)

    # Add text labels to the maze object
    total_cells_label = textLabel(maze_obj, 'Total cells  ', maze_obj.rows * maze_obj.cols)
    created_by_label = textLabel(maze_obj, 'Created By ', 'MohamedIsmail, MohamedSamy, YassminAhmed, SalwaAhmed')
    label = textLabel(maze_obj,'and', 'ShaimaAbdelHamid')

    # Perform a depth-first search on the maze object starting at (10,10)
    ucs_Search, ucs_path, forward_path = UCS(maze_obj, start = (10, 10))

    # Create agents for the maze object
    agent_A = agent(maze_obj, 10, 10, goal=(1, 1), footprints=True, shape='arrow', color=COLOR.blue)
    agent_B = agent(maze_obj, 1, 1, goal=(10, 10), footprints=True, filled=True, color=COLOR.green)
    agent_C = agent(maze_obj, 10, 10, footprints=True, color=COLOR.yellow)

    # Trace the path of the agents on the maze object
    maze_obj.tracePath({agent_A: ucs_Search}, showMarked=True) # Show the path of agent A and mark decision points
    maze_obj.tracePath({agent_B: ucs_path}) # Show the path of agent B
    maze_obj.tracePath({agent_C: forward_path}) # Show the path of agent C

    # Run the maze
    maze_obj.run() 

    # Output: The agents navigate through the maze and reach their respective goals.
