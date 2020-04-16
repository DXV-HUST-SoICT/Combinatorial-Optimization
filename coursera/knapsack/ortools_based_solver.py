from greedy import *
from ortools.sat.python import cp_model

def cp_ortools(items, taken, capacity):
    value = 0
    weight = 0
    opt = 1
    model = cp_model.CpModel()
    t = []
    w = []
    v = []
    for i in range(len(items)):
        item = items[i]
        t.append(model.NewIntVar(0, 1, 'taken_%i' % i))
        w.append(t[i] * item.weight)
        v.append(t[i] * item.value)
    model.Add(sum(w) <= capacity)
    model.Maximize(sum(v))
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    if status == cp_model.OPTIMAL:
        for i in range(len(t)):
            taken[i] = solver.Value(t[i])
        value = int(solver.ObjectiveValue())
    else:
        value, weight, opt = greedy_by_avarage_value(items, taken, capacity)
    return value, weight, opt