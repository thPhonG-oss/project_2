from file_handle import read_input, write_output
from cnf_generator import generate_cnf
from solver_pysat import solve_cnf
from solver_backtracking import solve_backtracking
from solver_bruteforce import solve_bruteforce
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_solver_menu():
    print("╔════╤══════════════════╗")
    print("║ 1  │ PySAT            ║")
    print("║ 2  │ Backtracking     ║")
    print("║ 3  │ Bruteforce       ║")
    print("║ 0  │ Exit             ║")
    print("╚════╧══════════════════╝")

def display_testcase_menu():
    print("\nSelect test case:")
    print(" 1  │ 5x5")
    print(" 2  │ 5x5")
    print(" 3  │ 5x5")
    print(" 4  │ 11x11")
    print(" 5  │ 11x11")
    print(" 6  │ 11x11")
    print(" 7  │ 20x20")
    print(" 8  │ 20x20")
    print(" 9  │ 20x20")
    print(" 0  │ Back")

def solve_puzzle(grid, solver_type):
    start_time = time.time()
    solution = None
    
    # Chuyển grid thành CNF một lần
    cnf = generate_cnf(grid)
    if not cnf:
        return None, time.time() - start_time
    
    solvers = {
        1: solve_cnf,  # PySAT solver
        2: solve_backtracking,  # Backtracking solver
        3: solve_bruteforce  # Bruteforce solver
    }
    
    solution = solvers.get(solver_type)(cnf)
    return solution, time.time() - start_time

def main():
    while True:
        clear_screen()
        display_solver_menu()
        
        solver_choice = input("\nEnter your choice (0-3): ")
        if solver_choice == '0':
            print("\nThank you for using Gem Hunter Solver!")
            break
            
        if solver_choice not in ['1', '2', '3']:
            input("Invalid choice! Press Enter to continue...")
            continue
            
        while True:
            clear_screen()
            display_testcase_menu()
            
            testcase = input("\nEnter test case (0-9): ")
            if testcase == '0':
                break
                
            if testcase not in [str(i) for i in range(1, 10)]:
                input("Invalid test case! Press Enter to continue...")
                continue
                
            input_file = f"./testcases/input/input_{testcase}.txt"
            output_file = f"./testcases/output/output_{testcase}.txt"
            
            print("\nSolving puzzle...")
            grid = read_input(input_file)
            if not grid:
                input("Failed to read input file! Press Enter to continue...")
                continue
            
            # Single solver mode for all choices
            solver_names = {1: 'PySAT', 2: 'Backtracking', 3: 'Bruteforce'}
            solution, solve_time = solve_puzzle(grid, int(solver_choice))
            
            if solution:
                # Remove the file clear operation
                write_output(solution, grid, output_file, solve_time, solver_names[int(solver_choice)])
                print(f"\nSolution found in {solve_time:.4f} seconds!")
                print(f"Result appended to: {output_file}")
            else:
                print("\nNo solution found!")
                with open(output_file, 'a') as f:
                    f.write(f"\nSolution name: {solver_names[int(solver_choice)]}\n")
                    f.write("No solution found!\n")
                    f.write(f"Execution time: {solve_time:.4f} seconds\n\n")
            
            input("\nPress Enter to continue...")
            
if __name__ == "__main__":
    main()