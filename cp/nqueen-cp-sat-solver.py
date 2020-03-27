from ortools.sat.python import cp_model
from copy import deepcopy as cp
import time

start = time.time()

N = 200

model = cp_model.CpModel()
cVar = [model.NewIntVar(0, N - 1, 'Q%i' % i) for i in range(N)]
model.AddAllDifferent(cVar)
model.Add(cVar[0] <= (N // 2))
model.Add(cVar[-1] > (N // 2))

diag1 = []
diag2 = []
for i in range(N):
	q1 = model.NewIntVar(i, N + i, 'diag1_%i' % i)
	diag1.append(q1)
	model.Add(q1 == cVar[i] + i)
	q2 = model.NewIntVar(-i, -i + N, 'diag2_%i' % i)
	diag2.append(q2)
	model.Add(q2 == cVar[i] - i)
model.AddAllDifferent(diag1)
model.AddAllDifferent(diag2)

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.FEASIBLE:
	print('ok')
else:
	print("Can't find solution")

finish = time.time()
print(finish - start)