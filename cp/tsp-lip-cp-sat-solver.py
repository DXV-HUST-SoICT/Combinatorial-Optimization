from ortools.sat.python import cp_model
from copy import deepcopy as cp

# Define input data
l = [
    [0, 2, 4, 1],
    [2, 0, 3, 7],
    [4, 3, 0, 8],
    [1, 7, 8, 0]
    ]
n = len(l)

def main():

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
                print("Found optimal solution")
                for i in range(n):
                    for j in range(n):
                        if solver.Value(d[i][j]) == 1:
                            print(i, j)
                break
            else:
                print("Solution has subtour")
                print(cycle)
                subtour = []
                for i in cycle:
                    for j in cycle:
                        subtour.append(d[i][j])
                model.Add(sum(subtour) < len(cycle))
        else:
            print("Not found any solution")
            break

if __name__ == "__main__":
    main()