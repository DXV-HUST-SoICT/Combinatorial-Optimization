from Utils import *
from fractions import Fraction as frac
import numpy as np
import math
from copy import deepcopy
from OrTools import *

def add_gomory_cut(tbl, bfs, all=True, cuts=None):
	assert (all == True) or (cuts != None)
	tbl = deepcopy(tbl)
	bfs = deepcopy(bfs)
	m, n = get_shape(tbl)
	if all == True:
		cuts = get_cuts(tbl, bfs)
	num_cuts = 0
	for i in cuts:
		num_cuts += 1
		tbl = add_variables(tbl)
		m, n = get_shape(tbl)
		new_constraint = np.ndarray(shape=(1, n + 1), dtype=object)
		tbl = add_constraints(tbl, new_constraint)
		bfs = np.append(bfs, n - 1)
		m, n = get_shape(tbl)
		for j in range(n + 1):
			if j == n - 1:
				tbl[m - 1, j] = frac(1)
			else:
				tbl[m - 1, j] = -(tbl[i, j] - math.floor(tbl[i, j]))

	return num_cuts, tbl, bfs

def add_cover_cut(tbl, bfs, all=True, cuts=None):
	assert (all == True) or (cuts != None)
	tbl = deepcopy(tbl)
	bfs = deepcopy(bfs)
	m, n = get_shape(tbl)
	if all == True:
		cuts = get_cuts(tbl, bfs)
	num_cuts = 0
	x = get_solution(tbl, bfs)
	for i in cuts:
		profits = 1 - x
		weights = tbl[i, :x.shape[0]]
		capacities = sum(tbl[i, :n]) - tbl[i, n]
		cover_set, value = solve_knapsack(profits, weights, capacities)
		if sum(profits) - value >= 1:
			continue
		num_cuts += 1
		constraints = np.ndarray(shape=(1, n + 1), dtype=object)
		cover_set_size = 0
		for j in range(n):
			if cover_set[j]:
				constraints[0, j] = frac(1)
				cover_set_size += 1
			else:
				constraints[0, j] = frac(0)
		constraints[0, n] = cover_set_size - 1
		tbl = add_constraints(tbl, constraints)
	for i in range(num_cuts):
		tbl = add_variables(tbl)
		tbl[m + i, n + i] = frac(1)
		bfs = np.append(bfs, n + i)
	return num_cuts, tbl, bfs

def add_gomory_milp_cut(tbl, bfs, ic, all=True, cuts=None):
	pass