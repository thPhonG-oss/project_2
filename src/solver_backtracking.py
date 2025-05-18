import time

def solve_backtracking(cnf, max_attempts=1000):
    if not cnf:
        return []  
        
    assignment = {}  
    start_time = time.time()
    timeout = 30
    
    def simplify_cnf(cnf, var, value):
        new_cnf = []
        for clause in cnf:
            if var in clause and value or -var in clause and not value:
                continue
            new_clause = [lit for lit in clause 
                         if abs(lit) != var]
            
            if not new_clause:
                return None
            new_cnf.append(new_clause)
            
        return new_cnf

    def backtrack(cnf, remaining_attempts):
        
        if time.time() - start_time > timeout:
            print("\nTimeout: Backtracking taking too long")
            return False
            
        if remaining_attempts <= 0:
            print("\nExceeded maximum attempts")
            return False
        
        
        if not cnf:
            return True
            
        
        used_vars = set(abs(lit) for clause in cnf for lit in clause)
        if not used_vars:  
            return False
            
        
        var = min(used_vars)
        
       
        simplified_cnf = simplify_cnf(cnf, var, True)
        if simplified_cnf is not None:
            assignment[var] = True
            if backtrack(simplified_cnf, remaining_attempts - 1):
                return True
                
        simplified_cnf = simplify_cnf(cnf, var, False)
        if simplified_cnf is not None:
            assignment[var] = False
            if backtrack(simplified_cnf, remaining_attempts - 1):
                return True
                
        # solution not found
        assignment.pop(var, None)
        return False

    if backtrack(cnf, max_attempts):
        n_vars = max(abs(lit) for clause in cnf for lit in clause)
        result = []
        for var in range(1, n_vars + 1):
            if assignment.get(var, False): 
                result.append(var)
        return result
    return None