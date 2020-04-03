from __future__ import print_function
from ortools.linear_solver import pywraplp

solver = pywraplp.Solver("Brewery", pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

tomato = solver.IntVar(0, solver.infinity(), 'tomato')
lettuce = solver.IntVar(0, solver.infinity(), 'lettuce')
spinach = solver.IntVar(0, solver.infinity(), 'spinach')
carrot = solver.IntVar(0, solver.infinity(), 'carrot')
oil = solver.IntVar(0, solver.infinity(), 'oil')

variables = [tomato, lettuce, spinach, carrot, oil]
protein = [0.85, 1.62, 12.78, 8.39, 0.00]
fat = [0.33, 0.20, 1.58, 1.39, 100]
carbohydrates = [4.64, 2.37, 74.69, 80.70, 0.00]
sodium = [9.00, 8.00, 7.00, 508.20, 0.00]
green_mass = [-1, 1, 1, -1, -1]
energy = [21, 16, 371, 346, 884]

protein = solver.Constraint(15, solver.infinity())
protein.SetCoefficient(tomato, 0.85)
protein.SetCoefficient(lettuce, 1.62)
protein.SetCoefficient(spinach, 12.78)
protein.SetCoefficient(carrot, 8.39)
protein.SetCoefficient(oil, 0.00)

fat = solver.Constraint(2, 6)
fat.SetCoefficient(tomato, 0.33)
fat.SetCoefficient(lettuce, 0.20)
fat.SetCoefficient(spinach, 1.58)
fat.SetCoefficient(carrot, 1.39)
fat.SetCoefficient(oil, 100)

carbohydrates = solver.Constraint(4, solver.infinity())
carbohydrates.SetCoefficient(tomato, 4.64)
carbohydrates.SetCoefficient(lettuce, 2.37)
carbohydrates.SetCoefficient(spinach, 74.69)
carbohydrates.SetCoefficient(carrot, 80.70)
carbohydrates.SetCoefficient(oil, 0.00)

sodium = solver.Constraint(0, 100)
sodium.SetCoefficient(tomato, 9.00)
sodium.SetCoefficient(lettuce, 8.00)
sodium.SetCoefficient(spinach, 7.00)
sodium.SetCoefficient(carrot, 508.20)
sodium.SetCoefficient(oil, 0.00)

green_mass = solver.Constraint(-solver.infinity(), 0)
green_mass.SetCoefficient(tomato, -1)
green_mass.SetCoefficient(lettuce, 1)
green_mass.SetCoefficient(spinach, 1)
green_mass.SetCoefficient(carrot, -1)
green_mass.SetCoefficient(oil, -1)

objective = solver.Objective()
objective.SetCoefficient(tomato, 21)
objective.SetCoefficient(lettuce, 16)
objective.SetCoefficient(spinach, 371)
objective.SetCoefficient(carrot, 346)
objective.SetCoefficient(oil, 884)

solver.Solve()
opt = 0
for i in range(len(variables)):
	v = variables[i]
	print(v.solution_value() * 100)
	opt += v.solution_value() * energy[i]
print(opt)