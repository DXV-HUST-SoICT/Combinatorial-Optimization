from greedy import *

def cp_ortools(node_count, edge_count, edges):
    from ortools.sat.python import cp_model
    model = cp_model.CpModel()
    color = [model.NewIntVar(0, node_count, 'color_%i' % i) for i in range(node_count)]
    for i in range(edge_count):
        model.Add(color[edges[i][0]] != color[edges[i][1]])
    model.Minimize(sum(color))
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    opt = 1
    if status == cp_model.OPTIMAL:
        solution = [solver.Value(color[i]) for i in range(node_count)]
        return solution, opt
    else:
        return naive(node_count, edge_count, edges)

def cp_ortools_with_greedy(node_count, edge_count, edges):
    solution, opt = greedy(node_count, edge_count, edges)
    max_num_color = max(solution)
    from ortools.sat.python import cp_model
    model = cp_model.CpModel()
    color = [model.NewIntVar(0, max_num_color, 'color_%i' % i) for i in range(node_count)]
    for i in range(edge_count):
        model.Add(color[edges[i][0]] != color[edges[i][1]])
    model.Minimize(sum(color))
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    opt = 1
    if status == cp_model.OPTIMAL:
        solution = [solver.Value(color[i]) for i in range(node_count)]
        return solution, opt
    else:
        return naive(node_count, edge_count, edges)

def cp_ortools_wih_greedy_feasible_problem(node_count, edge_count, edges):
    solution, opt = greedy(node_count, edge_count, edges)
    max_num_color = max(solution)
    from ortools.sat.python import cp_model
    while True:
        max_num_color -= 1
        model = cp_model.CpModel()
        color = [model.NewIntVar(0, max_num_color, 'color_%i' % i) for i in range(node_count)]
        for i in range(edge_count):
            model.Add(color[edges[i][0]] != color[edges[i][1]])
        solver = cp_model.CpSolver()
        status = solver.Solve(model)
        if status == cp_model.FEASIBLE:
            solution = [solver.Value(color[i]) for i in range(node_count)]
        else:
            break
    opt = 1
    return solution, opt