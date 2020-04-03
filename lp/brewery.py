from __future__ import print_function
from ortools.linear_solver import pywraplp

solver = pywraplp.Solver("Brewery", pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

a = solver.IntVar(0, solver.infinity(), 'a')
b = solver.IntVar(0, solver.infinity(), 'b')

c0 = solver.Constraint(0, 480)
c0.SetCoefficient(a, 5)
c0.SetCoefficient(b, 15)

c1 = solver.Constraint(0, 160)
c1.SetCoefficient(a, 4)
c1.SetCoefficient(b, 4)

c2 = solver.Constraint(0, 1190)
c2.SetCoefficient(a, 35)
c2.SetCoefficient(b, 20)

o = solver.Objective()
o.SetCoefficient(a, 13)
o.SetCoefficient(b, 23)
o.SetMaximization()

solver.Solve()
opt = 13 * a.solution_value() + 23 * b.solution_value()
print(opt, a.solution_value(), b.solution_value())