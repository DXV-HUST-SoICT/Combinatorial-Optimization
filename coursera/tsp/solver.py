#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
from collections import namedtuple

Point = namedtuple("Point", ['x', 'y'])

def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

def naive(points):
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

    solution, opt = dynamic_programming(points)

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

