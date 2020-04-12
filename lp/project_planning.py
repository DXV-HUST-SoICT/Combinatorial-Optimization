from __future__ import print_function
from ortools.linear_solver import pywraplp

solver = pywraplp.Solver("Project Planning", pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

A = "A"
B = "B"
C = "C"
D = "D"
E = "E"
F = "F"
G = "G"

d = dict()

d[A] = 4
d[B] = 3
d[C] = 5
d[D] = 2
d[E] = 10
d[F] = 10
d[G] = 1

task = [A, B, C, D, E, F, G]

maxLength = sum([d[key] for key in d])

s = dict()
for T in task:
	s[T] = solver.NumVar(0, maxLength, T)

c = []

c.append(solver.Constraint(-solver.infinity(), -d[A]))
c[-1].SetCoefficient(s[A], 1)
c[-1].SetCoefficient(s[G], -1)

c.append(solver.Constraint(-solver.infinity(), -d[A]))
c[-1].SetCoefficient(s[A], 1)
c[-1].SetCoefficient(s[D], -1)

c.append(solver.Constraint(-solver.infinity(), -d[E]))
c[-1].SetCoefficient(s[E], 1)
c[-1].SetCoefficient(s[F], -1)

c.append(solver.Constraint(-solver.infinity(), -d[G]))
c[-1].SetCoefficient(s[G], 1)
c[-1].SetCoefficient(s[F], -1)

c.append(solver.Constraint(-solver.infinity(), -d[D]))
c[-1].SetCoefficient(s[D], 1)
c[-1].SetCoefficient(s[C], -1)

c.append(solver.Constraint(-solver.infinity(), -d[F]))
c[-1].SetCoefficient(s[F], 1)
c[-1].SetCoefficient(s[C], -1)

c.append(solver.Constraint(-solver.infinity(), -d[F]))
c[-1].SetCoefficient(s[F], 1)
c[-1].SetCoefficient(s[B], -1)

Finish = solver.NumVar(0, maxLength, 'finish')

c.append(solver.Constraint(d[B], solver.infinity()))
c[-1].SetCoefficient(Finish, 1)
c[-1].SetCoefficient(s[B], -1)

c.append(solver.Constraint(d[C], solver.infinity()))
c[-1].SetCoefficient(Finish, 1)
c[-1].SetCoefficient(s[C], -1)

o = solver.Objective()
o.SetCoefficient(Finish, 1000)
o.SetCoefficient(s[B], 5000)
o.SetCoefficient(s[A], -5000)

solver.Solve()
opt = 1000 * Finish.solution_value() + 5000 * s[B].solution_value() - 5000 * s[A].solution_value() + 5000 * d[B]
print(opt)
for T in task:
	print(T + ':', s[T].solution_value(), s[T].solution_value() + d[T], end='; ')