import numpy as np
from fractions import Fraction as frac

def create_tbl(a, b, c):
	m = a.shape[0]
	n = a.shape[1]
	tbl = np.ndarray(shape=(m+1, n+1), dtype=object)
	tbl[:m, :n] = a[:m, :n]
	tbl[:m, n] = b[:m, 0]
	tbl[m, :n] = c[:n]
	tbl[m, n] = 0
	return tbl

def read_milp_data(file):
	data = open(file).read().split('\n')

	m, n = [int(x) for x in data[0].split(' ')]

	a = np.ndarray(shape=(m, n), dtype=object)
	b = np.ndarray(shape=(m, 1), dtype=object)
	c = np.ndarray(shape=(1, n), dtype=object)

	for i in range(m):
		data[i+1] = [int(x) for x in data[i+1].split(' ')]
		for j in range(n):
			a[i, j] = frac(data[i+1][j])
		b[i] = frac(data[i+1][n])

	data[m+1] = [int(x) for x in data[m+1].split(' ')]
	for j in range(n):
		c[0, j] = frac(data[m+1][j])
	l = int(data[m+2])
	ic = np.array([int(k) for k in data[m+3].split(' ')])
	return a, b, c, ic

def read_ilp_data(file):
	data = open(file).read().split('\n')

	m, n = [int(x) for x in data[0].split(' ')]

	a = np.ndarray(shape=(m, n), dtype=object)
	b = np.ndarray(shape=(m, 1), dtype=object)
	c = np.ndarray(shape=(1, n), dtype=object)

	for i in range(m):
		data[i+1] = [int(x) for x in data[i+1].split(' ')]
		for j in range(n):
			a[i, j] = frac(data[i+1][j])
		b[i] = frac(data[i+1][n])

	data[m+1] = [int(x) for x in data[m+1].split(' ')]
	for j in range(n):
		c[0, j] = frac(data[m+1][j])
	return a, b, c

def read_lp_data(file):
	data = open(file).read().split('\n')

	m, n = [int(x) for x in data[0].split(' ')]

	a = np.ndarray(shape=(m, n), dtype=object)
	b = np.ndarray(shape=(m, 1), dtype=object)
	c = np.ndarray(shape=(1, n), dtype=object)

	has_bfs = False
	if len(data[1].split(' ')) > n + 1:
		has_bfs = True
		bfs = np.ndarray(shape=(m), dtype=int)

	for i in range(m):
		data[i+1] = [int(x) for x in data[i+1].split(' ')]
		for j in range(n):
			a[i, j] = frac(data[i+1][j])
		b[i] = frac(data[i+1][n])
		if has_bfs:
			bfs[i] = data[i+1][n+1]

	data[m+1] = [int(x) for x in data[m+1].split(' ')]
	for j in range(n):
		c[0, j] = frac(data[m+1][j])

	data = [a, b, c]
	if has_bfs:
		data.append(bfs)
	return data

def get_solution(tbl, bfs):
	assert len(bfs) == len(set(bfs))
	m, n = get_shape(tbl)
	x = np.ndarray(shape=(n,), dtype=object)
	for j in range(n):
		x[j] = frac(0)
	for i in range(m):
		x[bfs[i]] = tbl[i, n] / tbl[i, bfs[i]]
	return x

def check_solution(x, ic=None):
	if type(ic) == type(None):
		ic = list(range(len(x)))
	for j, k in enumerate(x):
		if (j in ic) and (k.denominator != 1):
			return j
	return -1

def add_variables(tbl, num_vars=1):
	m, n = get_shape(tbl)

	new_vars = np.ndarray(shape=(m, num_vars), dtype=object)
	for i in range(m):
		for j in range(num_vars):
			new_vars[i, j] = frac(0)
	add_obj = np.array([[frac(0)] * num_vars])
	new_vars = np.concatenate([new_vars, add_obj])

	r = np.concatenate((tbl[:, :n], new_vars[:, :], tbl[:, n:(n+1)]), axis=1)
	return r

def add_constraints(tbl, constraints):
	m, n = get_shape(tbl)
	r = np.concatenate((tbl[:m, :], constraints[:, :], tbl[m:(m+1), :]), axis=0)
	return r

def get_shape(tbl):
	m, n = tbl.shape
	m, n = m - 1, n - 1
	return m, n

def get_cuts(tbl, bfs, ic=None):
	m, n = get_shape(tbl)
	assert len(bfs) == m
	if (type(ic) == type(None)):
		ic = list(range(n))
	cuts = []
	for i in range(m):
		if (bfs[i] in ic) and ((tbl[i, n] / tbl[i, bfs[i]]).denominator != 1):
			cuts.append(i)
	return cuts

if __name__ == '__main__':
	print('Utils')