from ortools.linear_solver import pywraplp
from ortools.algorithms import pywrapknapsack_solver
from Utils import *

def solve_knapsack(profits, weights, capacities):
	solver = pywrapknapsack_solver.KnapsackSolver(pywrapknapsack_solver.KnapsackSolver.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, '.')
	solver.Init(list(profits.astype(float)), [list(weights.astype(float))], [float(capacities)])
	value = solver.Solve()
	res = []
	for i in range(len(profits)):
		res.append(solver.BestSolutionContains(i))
	return res, value

def lp_solve(a, b, c):
	m, n = a.shape

	solver = pywraplp.Solver('tester', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

	x = []
	for j in range(n):
		x.append(solver.NumVar(0, solver.infinity(), 'x_%i' % j))

	return solve(a, b, c, x, solver)

def mip_solve(a, b, c, ic):
	m, n = a.shape

	solver = pywraplp.Solver('tester', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

	x = []
	for j in range(n):
		if j not in ic:
			x.append(solver.NumVar(0, solver.infinity(), 'x_%i' % j))
		else:
			x.append(solver.IntVar(0, solver.infinity(), 'x_%i' % j))

	return solve(a, b, c, x, solver)

def solve(a, b, c, x, solver):
	m, n = a.shape
	for i in range(m):
		ct = solver.Constraint(float(b[i, 0]), float(b[i, 0]))
		for j in range(n):
			ct.SetCoefficient(x[j], float(a[i, j]))

	o = solver.Objective()
	for j in range(n):
		o.SetCoefficient(x[j], float(c[0, j]))
	o.SetMaximization()

	solver.Solve()

	return solver.Objective().Value(), [k.solution_value() for k in x]


if __name__ == '__main__':
	print('OrTools')
	a, b, c, ic = read_milp_data('./data/mip_04')
	obj_value, sol = mip_solve(a, b, c, ic)
	print(obj_value)
	print(sol)
