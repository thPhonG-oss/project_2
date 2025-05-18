from utils import *
from itertools import combinations

def generate_cnf(grid):
    n_columns = len(grid[0])
    n_rows = len(grid)
    
    cnf = []
    for i in range(n_rows):
        for j in range(n_columns):
            cell = grid[i][j]
            if cell == 'T':
                cnf.append([get_var_id(i, j, n_columns)])
            elif cell == 'G':
                cnf.append([-get_var_id(i, j, n_columns)])
            elif isinstance(cell, int):
                cnt = int(cell)
                neighbors = list(get_neighbors(i, j, n_rows, n_columns))
                n_traps = [get_var_id(x, y, n_columns) for x, y in neighbors if grid[x][y] == 'T']
                unknown_neighbors = [get_var_id(x, y, n_columns) for x, y in neighbors if grid[x][y] == '_']
                remaining = cnt - len(n_traps)
                
                # if the number of traps is greater than the count, it's unsatisfiable
                if remaining < 0 or remaining > len(unknown_neighbors):
                    return None
                elif remaining == 0:
                    cnf.append([-x for x in unknown_neighbors])
                elif remaining == len(unknown_neighbors):
                    cnf.append(unknown_neighbors)
                
                # at least k true
                for combo in combinations(unknown_neighbors, len(unknown_neighbors) - remaining + 1):
                    cnf.append(list(combo))
                    
                # at most k true
                for combo in combinations(unknown_neighbors, remaining + 1):
                    cnf.append([-x for x in list(combo)])        
    return cnf