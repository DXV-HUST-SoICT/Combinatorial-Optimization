from ortools.sat.python import cp_model
from SolutionPrinter import SolutionPrinter

def main(n, k, E, c):
	model = cp_model.CpModel()

	cVar = [model.NewIntVar(0, k-1, c[i]) for i in range(n)]
	for p in E:
		model.Add(cVar[p[0]] != cVar[p[1]])
		
	solver = cp_model.CpSolver()
	solution_printer = SolutionPrinter(cVar, c)
	status = solver.SearchForAllSolutions(model, solution_printer)
	print()
	print('Solutions found : %i' % solution_printer.SolutionCount())

if __name__ == "__main__":
	c = ['Belgium', 'Denmark', 'France', 'Germany', 'Netherlands', 'Luxembourg']
	numV = len(c)
	n = [('Belgium', 'France'), ('Belgium', 'Germany'), ('Belgium', 'Netherlands'), ('Belgium', 'Luxembourg'),
		('Denmark', 'Germany'), ('France', 'Germany'), ('France', 'Luxembourg'), ('Germany', 'Netherlands'), ('Germany', 'Luxembourg')]
	k = 4
	listE = []
	for i in n:
		listE.append((c.index(i[0]), c.index(i[1])))
	main(numV, k, listE, c)