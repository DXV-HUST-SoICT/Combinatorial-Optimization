import numpy as np
from fractions import Fraction as frac
from Pivot import *
from Utils import *

# Solve Linear Programming Problem in canonical form (equality constraints) and know a BFS
def primal_simplex(tbl, bfs):
	m, n = get_shape(tbl)
	assert len(bfs) == m
	assert len(bfs) == len(set(bfs))

	tbl = standardize(tbl, bfs)
	
	while True:
		q = n
		for j in range(n):
			if tbl[m, j] > 0:
				q = j
				break
		if q == n:
			return True, tbl, bfs

		p = m
		for i in range(m):
			if tbl[i, q] > 0:
				p = i
				break
		if p == m:
			return False, tbl, bfs

		for i in range(p + 1, m):
			if (tbl[i, q] > 0) and ((tbl[i, n] / tbl[i, q]) < (tbl[p, n] / tbl[p, q])):
				p = i
		bfs[p] = q
		tbl = pivot(tbl, p, q)

def dual_simplex(tbl, bfs):
	m, n = get_shape(tbl)
	assert len(bfs) == m
	assert len(bfs) == len(set(bfs))
	
	tbl = standardize(tbl, bfs)

	while True:
		p = m
		for i in range(m):
			if tbl[i, n] < 0:
				p = i
				break
		if p == m:
			return True, tbl, bfs

		q = n
		for j in range(n):
			if tbl[p, j] < 0:
				q = j
				break
		if q == n:
			return False, tbl, bfs

		for j in range(q + 1, n):
			if (tbl[p, j] < 0) and (tbl[m, j] / tbl[p, j] < tbl[m, q] / tbl[p, q]):
				q = j
		bfs[p] = q
		tbl = pivot(tbl, p, q)

def standardize(tbl, bfs=[]):
	# Standardize
	m, n = get_shape(tbl)
	for p, q in enumerate(bfs):
		tbl = pivot(tbl, p, q)
	for i in range(len(bfs)):
		tbl[i, :] /= tbl[i, bfs[i]]
	return tbl


if __name__ == '__main__':
	print('Simplex')
	np.set_printoptions(precision=3, suppress=True)
	data = read_lp_data('./data/lp_01')
	assert len(data) == 4
	a, b, c, bfs = data
	tbl = create_tbl(a, b, c)
	solvable, tbl, bfs = primal_simplex(tbl, bfs)
	if solvable:
		print(tbl.astype(str))
		x = get_solution(tbl, bfs)
		print(float(sum(c[0] * x)))
		print([float(k) for k in x])
	else:
		print("Can't find primal solution!")