import numpy as np
from copy import deepcopy
from Simplex import *
from Pivot import *

def twophase_simplex(tbl):
	# print('2 phase input')
	# print(tbl.astype(str))

	tbl = standardize(tbl)

	# print('standard 1')
	# print(tbl.astype(str))

	m, n = get_shape(tbl)
	bfs = np.ndarray(shape=(m,), dtype=int)

	p1_tbl = deepcopy(tbl)
	for j in range(n):
		p1_tbl[m, j] = 0

	p1_tbl = add_variables(tbl, m)
	for i in range(m):
		p1_tbl[i, n+i] = frac(1) if p1_tbl[i, m+n] >= 0 else frac(-1)
		p1_tbl[m, n+i] = frac(-1)
	for j in range(n):
		p1_tbl[m, j] = frac(0)
	p1_tbl[m, m + n] = frac(0)
	p1_bfs = np.array([n + j for j in range(m)], dtype=int)

	# print('add slack')
	# print(p1_tbl.astype(str))

	solvable, p1_tbl, p1_bfs = primal_simplex(p1_tbl, p1_bfs)

	# print('after phase 1')
	# print(p1_tbl.astype(str))
	# print(p1_bfs)

	if solvable == False:
		return False, tbl, bfs

	tbl[:m, :] = np.concatenate((p1_tbl[:m, :n], p1_tbl[:m, (n+m):(n+m+1)]), axis = 1)
	for i in range(m):
		if p1_bfs[i] >= n:
			for j in range(n):
				if (j not in p1_bfs) and (tbl[i, j] != 0):
					p1_bfs[i] = j
					break
			if p1_bfs[i] >= n:
				return False, tbl, bfs
		bfs[i] = p1_bfs[i]
		tbl = pivot(tbl, i, bfs[i])

	# print('remove slack')
	# print(tbl.astype(str))
	# print(bfs)

	tbl = standardize(tbl, bfs)

	# print('standard 2')
	# print(tbl.astype(str))


	return primal_simplex(tbl, bfs)

def dual_twophase_simplex(tbl, bfs):
	solvable, tbl, bfs = dual_simplex(tbl, bfs)
	if not solvable:
		return solvable, tbl, bfs
	else:
		return primal_simplex(tbl, bfs)

if __name__ == '__main__':
	print('Two Phase Simplex')
	data = read_lp_data('./data/lp_02')
	assert len(data) >= 3
	a, b, c, bfs = data
	tbl = create_tbl(a, b, c)
	solvable, tbl, bfs = twophase_simplex(tbl)
	if solvable:
		x = get_solution(tbl, bfs)
		print(float(sum(c[0] * x)))
		print([float(k) for k in x])