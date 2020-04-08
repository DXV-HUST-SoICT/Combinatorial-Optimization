#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
from collections import namedtuple
from ortools.sat.python import cp_model
from copy import deepcopy

Point = namedtuple("Point", ['x', 'y'])

def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

def naive(points):
    nodeCount = len(points)
    solution = range(0, nodeCount)
    opt = 0
    return solution, opt

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

def _2opt(points):
    n = len(points)
    def _2opt_swap(route, i, k):
        new_route = deepcopy(route)
        new_route[i:(k+1)] = reversed(new_route[i:(k+1)])
        return new_route
    def calculate_distance(route):
        distance = 0
        for i in range(n - 1):
            distance += length(points[route[i]], points[route[i + 1]])
        return distance + length(points[route[-1]], points[route[0]])
    route = list(range(n))
    best_distance = calculate_distance(route)
    print(0, ":", best_distance)
    opt = 0
    x = 0
    while (x <= 1000):
        x += 1
        start_again = False
        best_move = deepcopy(route)
        best_move_distance = best_distance
        for i in range(1, n - 1):
            for k in range(i + 1, n):
                new_distance = best_distance - (length(points[route[i-1]], points[route[i]])\
                    + length(points[route[k]], points[route[(k+1)%n]])) \
                    + (length(points[route[i-1]], points[route[k]]) \
                    + length(points[route[i]], points[route[(k+1)%n]]))
                if (new_distance < best_move_distance):
                    best_move_distance = new_distance
                    best_move = _2opt_swap(route, i, k)
                    start_again = True
        if not start_again:
            break
        else:
            route = best_move
            best_distance = best_move_distance
            print(x, ":", best_distance)
    return route, opt

def _2opt_first_improvement(points):
    n = len(points)
    def _2opt_swap(route, i, k):
        new_route = deepcopy(route)
        new_route[i:(k+1)] = reversed(new_route[i:(k+1)])
        return new_route
    def calculate_distance(route):
        distance = 0
        for i in range(n - 1):
            distance += length(points[route[i]], points[route[i + 1]])
        return distance + length(points[route[-1]], points[route[0]])
    route = list(range(n))
    best_distance = calculate_distance(route)
    print(0, ":", best_distance)
    opt = 0
    x = 0
    while (x <= 1000):
        x += 1
        start_again = False
        best_move = deepcopy(route)
        best_move_distance = best_distance
        for i in range(1, n - 1):
            for k in range(i + 1, n):
                new_distance = best_distance - (length(points[route[i-1]], points[route[i]])\
                    + length(points[route[k]], points[route[(k+1)%n]])) \
                    + (length(points[route[i-1]], points[route[k]]) \
                    + length(points[route[i]], points[route[(k+1)%n]]))
                if (new_distance < best_move_distance):
                    best_move_distance = new_distance
                    best_move = _2opt_swap(route, i, k)
                    start_again = True
                    break
        if not start_again:
            break
        else:
            route = best_move
            best_distance = best_move_distance
            print(x, ":", best_distance)
    return route, opt


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    nodeCount = int(lines[0])

    points = []
    for i in range(1, nodeCount+1):
        line = lines[i]
        parts = line.split()
        points.append(Point(float(parts[0]), float(parts[1])))

    # build a trivial solution
    # visit the nodes in the order they appear in the file

    solver = naive
    if len(points) <= 20:
        solver = dynamic_programming
    else:
        solver = cp_ortools
    solver = _2opt
    solver = _2opt_first_improvement
    # if len(points) >= 300:
    #     solver = naive
    solution, opt = solver(points)

    # calculate the length of the tour
    obj = length(points[solution[-1]], points[solution[0]])
    for index in range(0, nodeCount-1):
        obj += length(points[solution[index]], points[solution[index+1]])

    # prepare the solution in the specified output format
    output_data = '%.2f' % obj + ' ' + str(opt) + '\n'
    output_data += ' '.join(map(str, solution))

    return output_data


import sys

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/tsp_51_1)')

