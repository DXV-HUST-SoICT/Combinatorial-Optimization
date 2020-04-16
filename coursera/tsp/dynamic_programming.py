from utils import *

def dynamic_programming(points):
    n = len(points)
    N = 1 << n
    inf = float("inf")
    c = []
    p = []

    def minCost(mask, last, p, c):
        if not ((mask >> last) & 1):
            return inf
        if (mask != 1) and (last == 0):
            return inf
        if (c[mask][last] == inf):
            tmpMask = mask & ~(1 << last)
            for i in range(n):
                if (i != last) and ((tmpMask >> i) & 1):
                    tmp = minCost(tmpMask, i, p, c) + length(points[i], points[last])
                    if tmp < c[mask][last]:
                        c[mask][last] = tmp
                        p[mask][last] = i
        return c[mask][last]

    for i in range(N):
        c.append([])
        p.append([])
        for j in range(n):
            c[i].append(inf)
            p[i].append(-1)
    c[1][0] = 0
    res = inf
    solution = [-1] * n
    for i in range(n):
        tmp = minCost(N - 1, i, p, c) + length(points[i], points[0])
        if tmp < res:
            res = tmp
            solution[-1] = i
    
    tmp_l = solution[-1]
    tmp_m = N - 1
    idx = n - 2
    while (idx >= 0):
        tmp = p[tmp_m][tmp_l]
        if tmp == -1:
            break
        solution[idx] = tmp
        tmp_m = tmp_m & ~(1 << tmp_l)
        tmp_l = tmp
        idx -= 1

    opt = 1
    return solution, opt