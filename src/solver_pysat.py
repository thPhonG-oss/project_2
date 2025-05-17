from pysat.solvers import Glucose3
from utils import *

def solve_cnf(cnf):
    solver = Glucose3()
    
    for clause in cnf:
        solver.add_clause(clause)
    
    if solver.solve():
        model = solver.get_model()
        return model  # Return the model if a solution is found
    else:
        return None  # No solution found