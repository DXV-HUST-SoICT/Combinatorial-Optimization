from ortools.linear_solver import pywraplp

def main():
	data = './data/gc_20_7'
	N, edge = read_data(data)
	solver = big_M_transform
	# solver = binary_mip
	solver(N, edge)

def big_M_transform(N, edge):
	solver = pywraplp.Solver('graph coloring', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
	color = [solver.IntVar(0, N - 1, 'color_%i' % i) for i in range(N)]
	b = []
	for i in range(N):
		b.append([])
		for j in range(N):
			b[-1].append(solver.IntVar(0, 1, 'b_%i_%i' % (i, j)))
	M = N
	obj = solver.IntVar(0, N - 1, 'objective')
	for e in edge:
		c1 = e[0]
		c2 = e[1]
		constraint = solver.Constraint(-solver.infinity(), -1)
		constraint.SetCoefficient(color[c1], 1)
		constraint.SetCoefficient(color[c2], -1)
		constraint.SetCoefficient(b[c1][c2], -M)

		constraint = solver.Constraint(1 - M, solver.infinity())
		constraint.SetCoefficient(color[c1], 1)
		constraint.SetCoefficient(color[c2], -1)
		constraint.SetCoefficient(b[c1][c2], -M)

	for i in range(N):
		constraint = solver.Constraint(0, solver.infinity())
		constraint.SetCoefficient(obj, 1)
		constraint.SetCoefficient(color[i], -1)
	objective = solver.Objective()
	objective.SetCoefficient(obj, 1)
	objective.SetMinimization()

	solver.Solve()
	print(int(obj.solution_value() + 1))

def binary_mip(N, edge):
	solver = pywraplp.Solver('graph coloring', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
	
	color = []
	for i in range(N):
		color.append([])
		for j in range(N):
			color[-1].append(solver.IntVar(0, 1, 'color_%i_%i' % (i, j)))
	

	# objective = solver.Objective()
	# objective.SetCoefficient(obj, 1)
	# objective.SetMinimization()

	# solver.Solve()
	# print(int(obj.solution_value() + 1))

def read_data(data):
	f = open(data).read().split('\n')
	f[0] = f[0].split(' ')
	N = int(f[0][0])
	M = int(f[0][1])
	edge = []
	for i in range(1, M + 1):
		edge.append([int(node) for node in f[i].split(' ')])
	return N, edge

if __name__ == '__main__':
	main()