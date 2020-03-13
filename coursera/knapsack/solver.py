#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def naive(items, taken, capacity):
    value = 0
    weight = 0
    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight
    return value, weight, 0

def dynamic_programming(items, taken, capacity):
    best = [[0] * len(items)]
    for c in range(1, capacity + 1):
        for i in range(len(items)):
            if i == 0:
                best.append([0])
            elif (items[i].weight <= c) and (best[c - items[i].weight][i-1] + items[i].value > best[c][i-1]):
                best[c].append(best[c - items[i].weight][i-1] + items[i].value)
            else:
                best[c].append(best[c][i-1])

    tmp_capacity = capacity
    tmp_idx = 0
    for i in range(len(items)):
        if best[capacity][i] > best[capacity][tmp_idx]:
            tmp_idx = i


    value = 0
    weight = 0

    while tmp_capacity > 0 and tmp_idx >= 0:
        if best[tmp_capacity][tmp_idx] == best[tmp_capacity][tmp_idx-1]:
            taken[tmp_idx] = 0
        else:
            taken[tmp_idx] = 1
            value += items[tmp_idx].value
            weight += items[tmp_idx].weight
            tmp_capacity -= items[tmp_idx].weight
        tmp_idx -= 1

    return value, weight, 1

def greedy_by_avarage_value(items, taken, capacity):
    def key(item):
        return item.value / item.weight

    items.sort(key=key, reverse=True)

    value = 0
    weight = 0

    for i in range(len(items)):
        item = items[i]
        if weight + item.weight <= capacity:
            value += item.weight
            weight += item.weight
            taken[item.index] = 1

    return value, weight, 0

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0]*len(items)

    solver = naive
    if len(items) * capacity < pow(10, 8):
        solver = dynamic_programming
    else:
        solver = greedy_by_avarage_value
    value, weight, opt_flag = solver(items, taken, capacity)
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(opt_flag) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

