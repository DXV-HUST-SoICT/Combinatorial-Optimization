from ortools.sat.python import cp_model
from copy import deepcopy as cp

# Define input data
ll = [
    [0, 2, 4, 1],
    [2, 0, 3, 7],
    [4, 3, 0, 8],
    [1, 7, 8, 0]
    ]
n = len(ll)

def main():

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
        print('Length: ', solver.ObjectiveValue())
        for v in p:
            print(solver.Value(v), end = ' ')
    else:
        print("Not found any solution")

if __name__ == "__main__":
    main()