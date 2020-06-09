from copy import deepcopy
import numpy as np
from fractions import Fraction as frac
from Utils import *

# Gaussian Elimination
def pivot(tbl, p, q, all=True, row=None):
	assert (all == True) or (row != None)
	m, n = get_shape(tbl)
	assert (m > 0) and (p < m) and (q < n)

	if all == True:
		row = list(range(m + 1))

	r = deepcopy(tbl)

	for i in row:
		if i == p:
			r[i] = tbl[i] / tbl[p, q]
		else:
			for j in range(n + 1):
					r[i, j] = tbl[i, j] - tbl[p, j] * tbl[i, q] / tbl[p, q]

	# print('pivot', row, p, q)
	# print(r.astype(str))
	
	return r

if __name__ == '__main__':
	print('Pivot')
	tbl = [[2, 3, 4, 5],
		[5, 2, 1, 3],
		[2, 4, 6, 2]]
	tbl = np.array(tbl, dtype=object)
	m, n = tbl.shape
	for i in range(m):
		for j in range(n):
			tbl[i, j] = frac(tbl[i, j])
	p, q = 1, 2
	r = pivot(tbl, p, q)
	print(r)
	print()

	p, q = 1, 1
	r = pivot(tbl, p, q)
	print(r)
	print()