# Sudoku-Solver

## Introduction

Two things I am passionate about today are computer science and sudoku, so it made sense to me
to combine these two and tackle an interesting project. I have always enjoyed leveraging the power
of computers as a means of solving problems, and solving a sudoku puzzle is no exception. It also
gives me the opportunity to puts the different skills I've learned into practice, from algorithm design
to clean code principals. I hope for this project to evolve like the knowledge I've gained in CS also.

## Instructions for use

After downloading the source files (must be in the same directory), run sudokuGrid.py. The gui will pop
up and you can select a sudoku file for the solver to solve. There are two button options that can be used to solve
the puzzle. First is solve pass, where the solver will pass through the grid once with each technique. This
is useful if you don't want to solve the puzzle completely and just need a hint. If the entire puzzle needs
to be solved in one sweep, clicking solve all will attempt to solve the entire puzzle. 

For now, the puzzle will stop when it can no longer solve any empty cells, either because the puzzle has been solved
or there is not enough information for the current techniques to work with. To reset the puzzle, exit the solver and
run the program again.

## What I have accomplished so far

* I created a basic GUI using tkinter from python. I went for a clean, minimal design that is (hopefully)
simple and easy to use
* The solver so far can solve easy puzzles that use basic elimination techniques in it's algorithms. One could
go online and find and easy sudoku puzzle, upload it to the solver and likely have a solution returned.
* The solver uses custom .sudoku files that are easy to create for personal testing. Each row represents a
row on the sudoku grid and has nine values for each column. A blank space is represented by a zero.

## What is to come

* In order to solve every puzzle (that has a possible solution), I want to create algorithms for the more
advanced techniques (such as swordfish and X-wing)
* It would be useful to have a visual that shows each step that the solver uses to solve the puzzle. This
could be color coded to each algorithm and could be a way to help learn those techniques.
* A brute force algorithm is possible for solving a sudoku puzzle using a computer, so I want to create 
a backtracking branching algorithm that can find a solution. This would be helpful for a puzzle that cannot
be solved using common techniques
* Quality of life improvements for the UI (such as a reset button to continuously solve puzzles without 
exiting the program). 
* I have recently learned about algorithm design and can work to optimize the algorithms I have implemented
already, helping the overall speed and resource usage.
