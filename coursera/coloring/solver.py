#!/usr/bin/python
# -*- coding: utf-8 -*-

from greedy import *
from ortools_based_solver import *

def naive(node_count, edge_count, edges):
    solution = range(0, node_count)
    opt = 0
    return solution, opt

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])

    edges = []
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))

    # build a trivial solution
    # every node has its own color

    solver = naive
    solver = cp_ortools
    solver = greedy
    solver = cp_ortools_with_greedy
    solver = cp_ortools_wih_greedy_feasible_problem
    solver = greedy_by_max_deg
    solution, opt = solver(node_count, edge_count, edges)
    
    obj = len(set(solution))
    # prepare the solution in the specified output format
    output_data = str(obj) + ' ' + str(opt) + '\n'
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
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)')

