import copy

def spread_fire(grid):
    """
    Update the forest grid based on fire spreading rules.
    - 0: Empty
    - 1: Tree
    - 2: Fire
    """
    grid_size = len(grid)
    update_grid = copy.deepcopy(grid)
    
    for i in range(grid_size):
        for j in range(grid_size):
            # Skip if the cell is not a tree (1)
            if grid[i][j] != 1:
                continue
            
            # Check neighbors
            neighbors = []
            if i > 0:  # Above
                neighbors.append(grid[i-1][j])
            if i < grid_size - 1:  # Below
                neighbors.append(grid[i+1][j])
            if j > 0:  # Left
                neighbors.append(grid[i][j-1])
            if j < grid_size - 1:  # Right
                neighbors.append(grid[i][j+1])
            
            # If any neighbor is on fire, the current tree catches fire
            if 2 in neighbors:
                update_grid[i][j] = 2

    return update_grid
