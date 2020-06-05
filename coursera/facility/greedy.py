from copy import deepcopy
from utils import *

def naive(facilities, customers):
    solution = [-1]*len(customers)
    capacity_remaining = [f.capacity for f in facilities]

    facility_index = 0
    for customer in customers:
        if capacity_remaining[facility_index] >= customer.demand:
            solution[customer.index] = facility_index
            capacity_remaining[facility_index] -= customer.demand
        else:
            facility_index += 1
            assert capacity_remaining[facility_index] >= customer.demand
            solution[customer.index] = facility_index
            capacity_remaining[facility_index] -= customer.demand
    opt = 0
    return solution, opt

def greedy(facilities, customers):
    facilities.sort(key = lambda f: float("inf") if f.capacity == 0 else f.setup_cost / f.capacity)
    tmp_customers = deepcopy(customers)
    solution = [-1] * len(customers)
    opt = 0
    for i in range(len(facilities)):
        tmp_customers.sort(key = lambda c: length(facilities[i].location, c.location))
        tmp = 0
        while len(tmp_customers) > 0:
            tmp += tmp_customers[0].demand
            if tmp > facilities[i].capacity:
                break
            solution[tmp_customers[0].index] = facilities[i].index
            tmp_customers = tmp_customers[1:]
    return solution, opt