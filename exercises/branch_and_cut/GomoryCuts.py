from Utils import *
from Simplex import *
from TwoPhaseSimplex import *
from CuttingPlanes import *

def gomory_cut_ilp(a, b, c):
	tbl = create_tbl(a, b, c)

	solvable, tbl, bfs = twophase_simplex(tbl)
	if not solvable:
		return solvable, tbl, bfs
	else:
		# x = get_solution(tbl, bfs)
		# print(sum(c[0, :] * x))
		# print(x.astype(float))
		pass

	x = get_solution(tbl, bfs)
	while check_solution(x) != -1:
		num_cuts, tbl, bfs = add_gomory_cut(tbl, bfs)
		solvable, tbl, bfs = dual_twophase_simplex(tbl, bfs)
		if not solvable:
			return solvable, tbl, bfs
		else:
			x = get_solution(tbl, bfs)
	return solvable, tbl, bfs

if __name__ == '__main__':
	print('Gomory Cuts')
	a, b, c = read_ilp_data('./data/mip_04')
	solvable, tbl, bfs = gomory_cut_ilp(a, b, c)
	best_solution = get_solution(tbl, bfs)[:c.shape[1]]
	best_value = sum(c[0, :] * best_solution)
	print("Final result:")
	print(float(best_value))
	print(best_solution.astype(float))