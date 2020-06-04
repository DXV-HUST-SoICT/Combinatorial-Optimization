from greedy import *
import numpy as np
from ortools.linear_solver import pywraplp
from copy import deepcopy

def localsearch(set_count, item_count, sets):
	opt, solution = greedy(set_count, item_count, deepcopy(sets))
	for it in range(1000):
		move = random_withdraw(set_count, min(100, sum(solution) * 4))
		tmp_sets = []
		items = set(range(item_count))
		for i in range(set_count):
			if i in move:
				tmp_sets.append(sets[i])
			elif solution[i] == 1:
				for j in sets[i].items:
					items.discard(j)
		# print(sum(solution))
		# print([i for i in range(len(solution)) if solution[i] == 1])
		# print(len(tmp_sets))
		# print([x.index for x in tmp_sets])
		# print(items)
		_, mini_batch_solution = mip_mini_batch(len(tmp_sets), tmp_sets, items)
		for i in range(len(tmp_sets)):
			solution[tmp_sets[i].index] = mini_batch_solution[i]
	return opt, solution

def random_withdraw(set_count, num_withdraw):
	x = np.random.uniform(0, 1, num_withdraw) * set_count
	x = [int(z) for z in x]
	return set(np.array(range(set_count))[x])

def mip_mini_batch(set_count, sets, items):
	solver = pywraplp.Solver("MIP", pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
	v = []
	for i in range(set_count):
		v.append(solver.IntVar(0, 1, 'v_%i' % i))
	for i in items:
		c = solver.Constraint(1, solver.infinity())
		for j in range(set_count):
			s = sets[j]
			if i in set(s.items):
				c.SetCoefficient(v[j], 1)
	objective = solver.Objective()
	for i in range(set_count):
		objective.SetCoefficient(v[i], sets[i].cost)
	objective.SetMinimization()
	status = solver.Solve()
	if status == solver.OPTIMAL:
		opt = 1
	else:
		opt = 0
	total_cost = 0
	solution = [0] * set_count
	for i in range(set_count):
		if int(v[i].solution_value()) == 1:
			solution[i] = 1
	return opt, solution