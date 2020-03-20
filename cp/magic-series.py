from ortools.sat.python import cp_model

N = 100

model = cp_model.CpModel()

series = [model.NewIntVar(0, N - 1, 'e%i' % i) for i in range(N)]
model.Add(sum(series) == N)

p = []
for i in range(N):
	eq = []
	for j in range(N):
		e = series[j]
		tmp = model.NewBoolVar('eq_%i_%i' % (i, j))
		model.Add(e == i).OnlyEnforceIf(tmp)
		model.Add(e != i).OnlyEnforceIf(tmp.Not())
		eq.append(tmp)
	model.Add(sum(eq) == series[i])

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.FEASIBLE:
	print(' '.join([str(solver.Value(series[i])) for i in range(N)]))