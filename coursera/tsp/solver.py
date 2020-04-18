#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
from utils import *
from dynamic_programming import *
from ortools_based_solver import *
from two_opt import *
from ortools_routing import *

Point = namedtuple("Point", ['x', 'y'])

def naive(points):
    nodeCount = len(points)
    solution = range(0, nodeCount)
    opt = 0
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
    solver = dynamic_programming
    solver = lip_ortools
    solver = cp_ortools
    solver = two_opt
    solver = ortools_routing
    print('solving...')
    
    solution, opt = solver(points)

    # calculate the length of the tour
    obj = length(points[solution[-1]], points[solution[0]])
    for index in range(0, nodeCount-1):
        obj += length(points[solution[index]], points[solution[index+1]])

    # prepare the solution in the specified output format
    output_data = '%.2f' % obj + ' ' + str(opt) + '\n'
    output_data += ' '.join(map(str, solution))

    # solver = TwoOptSolver(points)
    # output_data = solver.solve()

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

