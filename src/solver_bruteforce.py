from itertools import product
from utils import get_neighbors
import time

def is_valid_solution(grid):
    height, width = len(grid), len(grid[0])
    
    for i in range(height):
        for j in range(width):
            if isinstance(grid[i][j], int):
                neighbors = get_neighbors(i, j, height, width)
                trap_count = sum(1 for x, y in neighbors if grid[x][y] == 'T')
                if trap_count != grid[i][j]:
                    return False
    return True

def solve_bruteforce(grid):
    height, width = len(grid), len(grid[0])
    empty_cells = [(i, j) for i in range(height) for j in range(width)
                   if grid[i][j] == '_']
    
    test_grid = [row[:] for row in grid]
    start_time = time.time()
    timeout = 30  
    combinations_tried = 0
    total_combinations = 2 ** len(empty_cells)
    
    # try all combinations
    for combination in product(['T', 'G'], repeat=len(empty_cells)):
        combinations_tried += 1
        if combinations_tried % 10000 == 0:
                if time.time() - start_time > timeout:
                    elapsed = time.time() - start_time
                    print(f"\nTimeout after {elapsed:.2f} seconds:")
                    print(f"- Combinations tried: {combinations_tried:,}")
                    return None
        
        # apply combination to test grid
        for (i, j), val in zip(empty_cells, combination):
            test_grid[i][j] = val
            
        # check if this combination is valid
        if is_valid_solution(test_grid):
            return test_grid
            
        for i, j in empty_cells:
            test_grid[i][j] = '_'    
    return None