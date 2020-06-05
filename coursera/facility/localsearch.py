from greedy import *
import numpy as np
from ortools.linear_solver import pywraplp
from copy import deepcopy
from utils import *
from collections import namedtuple

Point = namedtuple("Point", ['x', 'y'])
Facility = namedtuple("Facility", ['index', 'setup_cost', 'capacity', 'location'])
Customer = namedtuple("Customer", ['index', 'demand', 'location'])

def localsearch(facilities, customers):
	solution, opt = greedy(deepcopy(facilities), deepcopy(customers))
	for it in range(10000):
		print(it)
		facilities_batch = random_withdraw(len(facilities), min(20, len(facilities)))
		print(facilities_batch)
		customers_batch = set(range(len(customers)))
		for i in range(len(customers)):
			if solution[i] not in facilities_batch:
				customers_batch.discard(i)
		tmp_facilities = []
		tmp_customers = []
		for i in facilities_batch:
			tmp_facilities.append(deepcopy(facilities[i]))
		for i in customers_batch:
			tmp_customers.append(deepcopy(customers[i]))
		tmp_solution, _ = mip_mini_batch(tmp_facilities, tmp_customers)
		for i in range(len(tmp_solution)):
			solution[tmp_customers[i].index] = tmp_solution[i]
		used = [0]*len(facilities)
		for facility_index in solution:
			used[facility_index] = 1
		obj = sum([f.setup_cost*used[f.index] for f in facilities])
		for customer in customers:
			obj += length(customer.location, facilities[solution[customer.index]].location)
		print(obj)
	return solution, opt

def random_withdraw(num_facilities, num_withdraw):
	facilities_batch = set()
	remain = list(range(num_facilities))
	while (len(remain) > 0) and (len(facilities_batch) < num_withdraw):
		i = int(np.random.uniform(0, 1) * len(remain))
		facilities_batch.add(remain[i])
		remain.remove(remain[i])
	return facilities_batch

def mip_mini_batch(facilities, customers):
	solver = pywraplp.Solver("MIP", pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
	v = []
	for i in range(len(customers)):
		v.append([])
		c = solver.Constraint(1, 1)
		for j in range(len(facilities)):
			v[i].append(solver.IntVar(0, 1, "v_%i_%i" % (i, j)))
			c.SetCoefficient(v[i][j], 1)
	for j in range(len(facilities)):
		c = solver.Constraint(0, facilities[j].capacity)
		for i in range(len(customers)):
			c.SetCoefficient(v[i][j], customers[i].demand)
	u = []
	for j in range(len(facilities)):
		u.append(solver.IntVar(0, 1, "u_%i" % j))
		c = solver.Constraint(0, solver.Infinity())
		c.SetCoefficient(u[j], 1)
		for i in range(len(customers)):
			c.SetCoefficient(v[i][j],
				0 if facilities[j].capacity == 0 else -(customers[i].demand / facilities[j].capacity))
	o = solver.Objective()
	for j in range(len(facilities)):
		o.SetCoefficient(u[j], facilities[j].setup_cost)
	for i in range(len(customers)):
		for j in range(len(facilities)):
			o.SetCoefficient(v[i][j], length(customers[i].location, facilities[j].location))
	o.SetMinimization()
	solver.SetTimeLimit(600000)
	status = solver.Solve()
	if status == solver.OPTIMAL:
		opt = 1
	else:
		opt = 0
	solution = [0] * len(customers)
	for i in range(len(customers)):
		for j in range(len(facilities)):
			if v[i][j].solution_value() == 1:
				solution[i] = facilities[j].index
				break
	return solution, opt