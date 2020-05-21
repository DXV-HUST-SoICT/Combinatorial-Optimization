#!/usr/bin/python
# -*- coding: utf-8 -*-

# The MIT License (MIT)
#
# Copyright (c) 2014 Carleton Coffrin
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


from collections import namedtuple
from ortools.linear_solver import pywraplp
from time import time


Set = namedtuple("Set", ['index', 'cost', 'items'])

def naive(set_count, item_count, sets):
    # build a trivial solution
    # pick add sets one-by-one until all the items are covered
    solution = [0]*set_count
    coverted = set()
    
    for s in sets:
        solution[s.index] = 1
        coverted |= set(s.items)
        if len(coverted) >= item_count:
            break
    return 0, solution

def mip(set_count, item_count, sets):
    
    solver = pywraplp.Solver("MIP", pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    v = []
    for i in range(set_count):
        v.append(solver.IntVar(0, 1, 'v_%i' % i))
    for i in range(item_count):
        c = solver.Constraint(1, solver.infinity())
        for j in range(set_count):
            s = sets[j]
            if i in set(s.items):
                c.SetCoefficient(v[j], 1)
    objective = solver.Objective()
    for i in range(set_count):
        objective.SetCoefficient(v[i], sets[i].cost)
    objective.SetMinimization()
    start = time()
    status = solver.Solve()
    end = time()
    if status == solver.OPTIMAL:
        opt = 1
    else:
        opt = 0
    total_cost = 0
    solution = [0] * set_count
    for i in range(set_count):
        if int(v[i].solution_value()) == 1:
            solution[i] = 1
    return opt, solution

def greedy(set_count, item_count, sets):
    covered = set()
    solution = [0] * set_count
    while len(covered) < item_count:
        m = float("inf")
        t = None
        for i in range(set_count):
            if (len(sets[i].items) != 0) and ((sets[i].cost / len(sets[i].items)) < m):
                m = sets[i].cost / len(sets[i].items)
                t = i
        solution[t] = 1
        for i in range(set_count):
            if i != t:
                for item in sets[t].items:
                    sets[i].items.discard(item)
        covered |= sets[t].items
        # print("length of covered set:", len(covered))
        sets[t].items.clear()
    return 0, solution


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    parts = lines[0].split()
    item_count = int(parts[0])
    set_count = int(parts[1])
    
    sets = []
    for i in range(1, set_count+1):
        parts = lines[i].split()
        sets.append(Set(i-1, float(parts[0]), set([int(x) for x in parts[1:]])))

    # solution here
    solver = mip
    opt, solution = solver(set_count, item_count, sets)
        
    # calculate the cost of the solution
    obj = sum([s.cost*solution[s.index] for s in sets])

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
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/sc_6_1)')

