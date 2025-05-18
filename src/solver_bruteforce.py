from itertools import product
import time

def solve_bruteforce(cnf):
    if not cnf:
        return None
    
    
    n_vars = max(abs(lit) for clause in cnf for lit in clause)
    max_combinations = 2 ** n_vars
    
    
    start_time = time.time()
    timeout = 30
    combinations_tried = 0
    
    def is_satisfied(assignment, clause):
        return any(
            (lit > 0 and assignment[abs(lit)-1]) or 
            (lit < 0 and not assignment[abs(lit)-1]) 
            for lit in clause
        )
    
    # try all possible combinations of True/False for n_vars
    for values in product([True, False], repeat=n_vars):
        combinations_tried += 1
        
        # check timeout after every 10000 combinations
        if combinations_tried % 10000 == 0:
            if time.time() - start_time > timeout:
                return None
        
        if all(is_satisfied(values, clause) for clause in cnf):
            return [i+1 for i, val in enumerate(values) if val]
    
    return None