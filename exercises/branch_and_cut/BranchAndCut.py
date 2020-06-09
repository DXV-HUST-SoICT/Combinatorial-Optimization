import os
import math
import numpy as np
from copy import deepcopy
from TwoPhaseSimplex import *
from Utils import *
from CuttingPlanes import *

def _try(tbl, bfs, c, best_value, best_solution):
	solvable, tbl, bfs = dual_twophase_simplex(tbl, bfs)
	if not solvable:
		return solvable, tbl, bfs
	x = get_solution(tbl, bfs)
	if (best_value != float('inf')) and (sum(c[0] * x[:c.shape[1]]) <= best_value):
		return False, best_value, best_solution
	k = check_solution(x)
	if k == -1:
		return True, sum(c[0] * x[:c.shape[1]]), x[:c.shape[1]]
	else:
		while True:
			num_cuts, tbl, bfs = add_cover_cut(tbl, bfs)
			if num_cuts == 0:
				break
			solvable, tbl, bfs = dual_twophase_simplex(tbl, bfs)
			if not solvable:
				return solvable, tbl, bfs
			x = get_solution(tbl, bfs)
			if (best_value != float('inf')) and (sum(c[0] * x[:c.shape[1]]) <= best_value):
				return False, best_value, best_solution
			k = check_solution(x)
			if k == -1:
				return True, sum(c[0] * x[:c.shape[1]]), x[:c.shape[1]]

		tbl1 = add_variables(tbl)
		m, n = get_shape(tbl1)
		bfs1 = np.concatenate((bfs, np.array([n - 1], dtype=int)), axis=0)
		c1 = np.concatenate((c, np.array([[frac(0)]], dtype=object)), axis=1)
		constraints = np.ndarray(shape=[1, n + 1], dtype=object)
		for j in range(n):
			constraints[0, j] = frac(0)
		constraints[0, k] = frac(1)
		constraints[0, n - 1] = frac(1)
		constraints[0, n] = frac(math.floor(x[k]))
		tbl1 = add_constraints(tbl1, constraints)
		solvable_1, best_value_1, best_solution_1 = _try(tbl1, bfs1, c1, best_value, best_solution)
		if (solvable_1) and (best_value_1 > best_value):
			solvable, best_value, best_solution = True, best_value_1, best_solution_1

		tbl2 = add_variables(tbl)
		m, n = get_shape(tbl1)
		bfs2 = np.concatenate((bfs, np.array([n - 1], dtype=int)), axis=0)
		c2 = np.concatenate((c, np.array([[frac(0)]], dtype=object)), axis=1)
		constraints = np.ndarray(shape=[1, n + 1], dtype=object)
		for j in range(n):
			constraints[0, j] = 0
		constraints[0, k] = frac(-1)
		constraints[0, n - 1] = frac(1)
		constraints[0, n] = -frac(math.ceil(x[k]))
		tbl2 = add_constraints(tbl2, constraints)
		solvable_2, best_value_2, best_solution_2 = _try(tbl2, bfs2, c2, best_value, best_solution)
		if (solvable_2) and (best_value_2 > best_value):
			solvable, best_value, best_solution = True, best_value_2, best_solution_2

		return solvable, best_value, best_solution

def branch_and_cut(a, b, c):
	tbl = create_tbl(a, b, c)
	best_value = -float('inf')
	best_solution = None
	solvable, tbl, bfs = twophase_simplex(tbl)
	if solvable:
		return _try(tbl, bfs, c, best_value, best_solution)
	else:
		return False, best_value, best_solution

if __name__ == '__main__':
	print('Branch and Cut')
	a, b, c = read_ilp_data('./data/mip_01')
	solvable, best_value, best_solution = branch_and_cut(a, b, c)
	if solvable:
		print("Result:")
		print('best_value:', best_value)
		print('best_solution:', best_solution.astype(float))
	else:
		print("can't find solution")