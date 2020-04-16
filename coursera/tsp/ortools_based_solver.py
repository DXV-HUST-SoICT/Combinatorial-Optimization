from utils import *

from ortools.sat.python import cp_model

def lip_ortools(points):
    def find_cycle(solver, d):
        s = [0]
        for i in range(len(d)):
            if solver.Value(d[s[-1]][i]) == 1:
                s.append(i)
                break
        while s[-1] != s[0]:
            for i in range(len(d)):
                if solver.Value(d[s[-1]][i]) == 1:
                    s.append(i)
                    break
        return s

    # Calculate distance
    l = []
    for i in range(len(points)):
        l.append([])
        for j in range(len(points)):
            val = int(1000000 * length(points[i], points[j]))
            l[i].append(val)
    n = len(l)

    # Initialize model
    model = cp_model.CpModel()
    d = []

    # Define variables
    for i in range(n):
        d.append([])
        for j in range(n):
            d[i].append(model.NewIntVar(0, 1, 'd_%i_%i' %(i, j)))

    # Define constraints
    for i in range(n):
        ouE = []
        inE = []
        for j in range(n):
            ouE.append(d[i][j])
            inE.append(d[j][i])
        model.Add(d[i][i] == 0)
        model.Add(sum(ouE) == 1)
        model.Add(sum(inE) == 1)

    # Define objective function
    model.Minimize(sum([d[i][j] * l[i][j] for i in range(n) for j in range(n)]))

    # Initialize solver
    solver = cp_model.CpSolver()

    while True:
        status = solver.Solve(model)
        if status == cp_model.OPTIMAL:
            cycle = find_cycle(solver, d)
            cycle = cycle[:-1]
            if len(cycle) == n:
                return cycle, 1
            else:
                subtour = []
                for i in cycle:
                    for j in cycle:
                        subtour.append(d[i][j])
                model.Add(sum(subtour) < len(cycle))
        else:
            return(naive(points))
            break

def cp_ortools(points):
    def appendEdgeValue(model, n, d, s, edge_idx):
        i = edge_idx
        j = (i + 1) % n
        u = model.NewIntVar(0, n - 1, 'u_%i' % i)
        model.Add(u == p[i])
        v = model.NewIntVar(0, n - 1, 'v_%i' % i)
        model.Add(v == p[j])
        z = model.NewIntVar(0, n * n - 1, 'z_%i' % i)
        model.Add(z == u * n + v)
        tmp = model.NewIntVar(min(d), max(d), 'tmp_%i' % i)
        model.AddElement(z, d, tmp)
        s.append(tmp)

    # Calculate distance
    l = []
    for i in range(len(points)):
        l.append([])
        for j in range(len(points)):
            val = int(1000000 * length(points[i], points[j]))
            l[i].append(val)
    n = len(l)

    d = []
    for i in range(n):
        for j in range(n):
            d.append(l[i][j])

    # Initialize model
    model = cp_model.CpModel()
    p = []

    # Define variables
    for i in range(n):
        p.append(model.NewIntVar(0, n - 1, 'p_%i' % i))

    model.AddAllDifferent(p)

    s = []
    for i in range(n):
        appendEdgeValue(model, n, d, s, i)

    # Define objective function
    model.Minimize(sum(s))

    # Initialize solver
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL:
        solution = []
        opt = 1
        for v in p:
            solution.append(solver.Value(v))
        return solution, opt
    else:
        return naive(points)