# Import the necessary libraries
from pyamaze import maze, agent, textLabel, COLOR

# Define the BFS function
def BFS(m):
    """
    This function implements the Breadth-First Search (BFS) algorithm.
    Args:
        m (maze): The maze object.
        start (tuple): The starting cell coordinates.
    Returns:
        explored (list): The list of cells visited during the search.
        forward_path (dict): The dictionary of paths from the starting cell to ending cell.
    """
    start = (m.rows, m.cols)

    # Initialize the list of explored cells and the list of frontier cells with the starting cell
    frontier = [start]
    explored = [start]

    # Initialize the dictionaries for the paths from each visited cell to its parent and the path from the starting cell to each visited cell
    bfsPath = {}

  # Perform the BFS search
    while len(frontier) > 0:
        # Pop the first cell in the frontier list
        currCell = frontier.pop(0)

        # Check if the current cell is the goal cell, and break the loop if it is
        if currCell == (1, 1):
            break

        # Iterate over the four possible directions to move from the current cell
        for d in 'ESNW':

            # If there is a wall in the direction
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1]+1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1]-1)
                elif d == 'S':
                    childCell = (currCell[0]+1, currCell[1])
                elif d == 'N':
                    childCell = (currCell[0]-1, currCell[1])

                # If the child cell has already been explored, skip it
                if childCell in explored:
                    continue

                # Add the child cell to the explored and frontier lists, and update the bfs_path dictionary
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell] = currCell

    # Initialize the forward_path dictionary for tracing the path from the starting cell to each visited cell
    fwdPath = {}
    cell = (1, 1)

    # Trace the path from the goal cell to the starting cell using the bfs_path dictionary
    while cell != start:
        fwdPath[bfsPath[cell]] = cell
        cell = bfsPath[cell]

    # Return the bfs_Search list[explored] and forward_path dictionary
    return explored, fwdPath


# Main function
if __name__ == '__main__':
    # Create a maze object with dimensions 10x10
    maze_obj = maze(10, 10)

    # Create a maze with a dark theme
    maze_obj.CreateMaze(loadMaze='Maze.csv', theme=COLOR.dark)

    # Add text labels to the maze object
    total_cells_label = textLabel(
        maze_obj, 'Total cells  ', maze_obj.rows * maze_obj.cols)
    created_by_label = textLabel(
        maze_obj, 'Created By ', 'MohamedIsmail, MohamedSamy, YassminAhmed, SalwaAhmed')
    label = textLabel(maze_obj, 'and', 'ShaimaAbdelHamid')

    # Perform a depth-first search on the maze object starting at (10,10)
    dfs_Search, forward_path = BFS(maze_obj)

    # Create agents for the maze object
    agent_A = agent(maze_obj, 10, 10, goal=(1, 1),footprints=True, shape='arrow', color=COLOR.blue)
    agent_B = agent(maze_obj, 10, 10, footprints=True,color=COLOR.yellow, filled=True)
    agent_C = agent(maze_obj, 10, 10, footprints=True, color=COLOR.red)
    # Trace the path of the agents on the maze object
    # Show the path of agent A and mark decision points
    maze_obj.tracePath({agent_A: dfs_Search}, showMarked=True)
    maze_obj.tracePath({agent_B: forward_path})  # Show the path of agent B
    maze_obj.tracePath({agent_C: forward_path}) # Show the path of agent C

    # Run the maze
    maze_obj.run()

    # Output: The agents navigate through the maze and reach their respective goals.
