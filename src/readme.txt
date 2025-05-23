Gem Hunter Puzzle Solver
Overview
This project implements a solver for the Gem Hunter puzzle, a grid-based game where players identify gems (G) and traps (T) based on numerical clues indicating the number of surrounding traps. The solver uses Conjunctive Normal Form (CNF) constraints and provides three solving approaches: PySAT (using the python-sat library), backtracking, and brute-force.
Features

CNF Generation: Automatically generates CNF clauses based on the puzzle grid.
PySAT Solver: Uses the python-sat library to solve CNF constraints efficiently.
Backtracking Algorithm: Implements a backtracking approach to explore valid solutions.
Brute-Force Algorithm: Tests all possible combinations for small grids, with a timeout mechanism.
Performance Comparison: Measures and compares execution times across solvers.
Test Cases: Includes 9 test cases (3 each for 5x5, 11x11, and 20x20 grids) in the testcases directory.

Installation

Clone the Repository:
git clone https://github.com/thPhonG-oss/project_2
cd src

Install Dependencies:
pip install -r requirements.txt

The requirements.txt includes:

python-sat>=1.8.dev16: For CNF solving with the Glucose3 solver.

Usage

Run the Program:
python main.py

Select a Solver:

1: PySAT (uses CNF and Glucose3 solver)
2: Backtracking
3: Brute-force
0: Exit

Select a Test Case:

1-3: 5x5 grids
4-6: 11x11 grids
7-9: 20x20 grids
0: Back to solver menu

View Results:

The solution (if found) is printed to the console and appended to the corresponding testcases/output/output_x.txt file.
Execution time and solver name are included in the output.

Test Cases
The testcases directory contains 9 solvable test cases:

5x5 Grids: input_1.txt, input_2.txt, input_3.txt
11x11 Grids: input_4.txt, input_5.txt, input_6.txt
20x20 Grids: input_7.txt, input_8.txt, input_9.txt

Each input file uses the format:

T: Trap
G: Gem
Number: Clue indicating the number of surrounding traps
_: Empty cell

Output files (output_x.txt) contain:

Solver name
Solution grid (with T or G for empty cells)
Execution time