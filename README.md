Sudoku Solver - Python
Overview
This repository contains a simple yet effective Sudoku solver implemented in pure Python without any external dependencies. The solver uses a backtracking algorithm to find the correct solution for any valid 9×9 Sudoku puzzle.

Features
Pure Python implementation (no external libraries required)

Simple command-line interface

Handles standard 9×9 Sudoku puzzles

Backtracking algorithm for efficient solving

Clear input format for easy puzzle entry

How to Use
Input Format
You can input your Sudoku puzzle in two ways:

Direct Input: Enter each row of the Sudoku puzzle as a space-separated string of numbers (use 0 for empty cells)

Example input for a row:

5 3 0 0 7 0 0 0 0
File Input: Prepare a text file with each row on a separate line (see input.txt for an example)

Running the Solver
Clone the repository:

bash
git clone https://github.com/yourusername/Sudoku-Solver.git
cd Sudoku-Solver
Run the solver:

bash
python sudoku_solver.py
Follow the prompts to either:

Enter each row manually when prompted

Or specify an input file when asked

Example
Sample input (from input.txt):

5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
The solver will display the completed Sudoku puzzle.

Algorithm
The solver uses a backtracking algorithm which:

Finds the next empty cell

Tries numbers 1-9 in that cell

For each valid number (following Sudoku rules), it recursively tries to solve the rest

If it hits a dead end, it backtracks and tries the next number

This approach guarantees a solution if one exists for the given puzzle.
