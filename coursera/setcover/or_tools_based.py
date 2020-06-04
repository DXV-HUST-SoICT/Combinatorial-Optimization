
from ortools.linear_solver import pywraplp
from time import time

def mip(set_count, item_count, sets):
    solver = pywraplp.Solver("MIP", pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    v = []
    for i in range(set_count):
        v.append(solver.IntVar(0, 1, 'v_%i' % i))
    for i in range(item_count):
        c = solver.Constraint(1, solver.infinity())
        for j in range(set_count):
            s = sets[j]
            if i in set(s.items):
                c.SetCoefficient(v[j], 1)
    objective = solver.Objective()
    for i in range(set_count):
        objective.SetCoefficient(v[i], sets[i].cost)
    objective.SetMinimization()
    start = time()
    status = solver.Solve()
    end = time()
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
