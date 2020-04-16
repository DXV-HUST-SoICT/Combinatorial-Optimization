

def greedy(node_count, edge_count, edges):
    solution = []
    opt = 0
    d = []
    for i in range(node_count):
        d.append([0] * node_count)
    for i in range(edge_count):
        d[edges[i][0]][edges[i][1]] = d[edges[i][1]][edges[i][0]] = 1
    for i in range(node_count):
        sol = set(range(node_count))
        for j in range(i):
            if d[i][j] == 1 and solution[j] in sol:
                sol.remove(solution[j])
        solution.append(min(sol))
    return solution, opt
