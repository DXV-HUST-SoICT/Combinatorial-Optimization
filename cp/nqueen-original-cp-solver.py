"""
  OR-tools solution to the N-queens problem.
"""
from __future__ import print_function
import sys
from ortools.constraint_solver import pywrapcp

def main(board_size):
  # Creates the solver.
  solver = pywrapcp.Solver("n-queens")
  # Creates the variables.
  # The array index is the column, and the value is the row.
  queens = [solver.IntVar(0, board_size - 1, "x%i" % i) for i in range(board_size)]
  # Creates the constraints.

  # All rows must be different.
  solver.Add(solver.AllDifferent(queens))

  # All columns must be different because the indices of queens are all different.

  # No two queens can be on the same diagonal.
  solver.Add(solver.AllDifferent([queens[i] + i for i in range(board_size)]))
  solver.Add(solver.AllDifferent([queens[i] - i for i in range(board_size)]))

  db = solver.Phase(queens,
                    solver.CHOOSE_FIRST_UNBOUND,
                    solver.ASSIGN_MIN_VALUE)
  solver.NewSearch(db)

  # Iterates through the solutions, displaying each.
  num_solutions = 0

  while solver.NextSolution():
    # Displays the solution just computed.
    for i in range(board_size):
      for j in range(board_size):
        if queens[j].Value() == i:
          # There is a queen in column j, row i.
          print("Q", end=" ")
        else:
          print("_", end=" ")
      print()
    print()
    num_solutions += 1
    break

  solver.EndSearch()

  print()
  print("Solutions found:", num_solutions)
  print("Time:", solver.WallTime(), "ms")

# By default, solve the 8x8 problem.
board_size = 50

if __name__ == "__main__":
  if len(sys.argv) > 1:
    board_size = int(sys.argv[1])
  main(board_size)