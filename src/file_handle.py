import os
from utils import *

def read_input(filename: str):
    if not os.path.exists(filename):
        print("File", filename, "does not exist\n")
        return None
    
    grid = []
    with open(filename, 'r') as file:
        for line in file:
            row = line.strip().split(', ')
            grid.append([int(cell) if cell.isdigit() else cell for cell in row])
    return grid

def write_output(solution, grid, filename, executed_time, solver_name):
    n_rows = len(grid)
    n_columns = len(grid[0])
    result_grid = []
    
    for i in range(n_rows):
        row = []
        for j in range(n_columns):
            var_id = get_var_id(i, j, n_columns)
            if isinstance(grid[i][j], int):
                row.append(str(grid[i][j]))
            else:
                row.append('T' if var_id in solution else 'G')
        result_grid.append(row)
    
    with open(filename, 'a') as file:
        file.write(f"Solution name: {solver_name}\n")
        file.write("Result:\n")
        
        for row in result_grid:
            file.write(', '.join(row) + '\n')
        
        file.write(f"\nExecution time: {executed_time:.4f} seconds\n")
        file.write("\n")  
    # rrint to console
    print(f"\nSolution for {solver_name}:")
    for row in result_grid:
        print(', '.join(row))
    print(f"Execution time: {executed_time:.4f} seconds")