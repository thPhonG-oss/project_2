from utils import get_neighbors

def is_valid(grid, i, j, val):
    height, width = len(grid), len(grid[0])
    neighbors = get_neighbors(i, j, height, width)
    
    for ni, nj in neighbors:
        if isinstance(grid[ni][nj], int):
            count = grid[ni][nj]
            neighbor_traps = sum(1 for x, y in get_neighbors(ni, nj, height, width)
                               if (x == i and y == j and val == 'T') or
                                  (grid[x][y] == 'T'))
            if neighbor_traps > count:
                return False
    return True

def solve_backtracking(grid):
    def solve(pos=0):
        if pos == len(empty_cells):
            return True
        
        i, j = empty_cells[pos]
        for val in ['T', 'G']:
            if is_valid(grid, i, j, val):
                grid[i][j] = val
                if solve(pos + 1):
                    return True
                grid[i][j] = '_'  # backtrack
        return False

    height, width = len(grid), len(grid[0])
    empty_cells = [(i, j) for i in range(height) for j in range(width)
                   if grid[i][j] == '_']
    if solve():
        return grid
    return None