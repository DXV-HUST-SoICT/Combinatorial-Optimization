

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

def greedy_by_max_deg(node_count, edge_count, edges):
    solution = [-1] * node_count
    opt = 0
    d = []
    c = []
    for i in range(node_count):
        d.append(set())
        c.append(set(range(node_count)))
    for e in edges:
        d[e[0]].add(e[1])
        d[e[1]].add(e[0])
    for i in range(node_count):
        idx = -1
        for j in range(node_count):
            if solution[j] == -1:
                if idx == -1:
                    idx = j
                elif len(d[j]) > len(d[idx]):
                    idx = j
        if idx != -1:
            solution[idx] = min(c[idx])
            for j in d[idx]:
                d[j].discard(idx)
                c[j].discard(solution[idx])
            print(idx, solution[idx])
    return solution, opt