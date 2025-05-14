# Sudoku Solver 
Overview : 
This repository contains a simple yet effective Sudoku solver implemented in pure Python without any external dependencies. The solver uses a backtracking algorithm to find the correct solution for any valid 9×9 Sudoku puzzle.

Simple command-line interface
Handles standard 9×9 Sudoku puzzles
Backtracking algorithm for efficient solving

How to Use
Input Format - You can See in "input.txt"

Algorithm - 
The solver uses a backtracking algorithm which Finds the next empty cell and Tries valid numbers  (following Sudoku rules) from 1-9 in that cell, it recursively tries to solve the rest empty spaces and if it hits a dead end ( for an empty cell no valid entries are present) , it backtracks and tries the next number.

This approach guarantees a solution if one exists for the given puzzle.

I Hopes it will be helpful !

Thanks if you reaches till here reading this .
