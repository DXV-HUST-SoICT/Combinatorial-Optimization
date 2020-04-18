from __future__ import print_function
import math
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
from utils import *
from collections import namedtuple

def ortools_routing(points):
	manager = pywrapcp.RoutingIndexManager(len(points), 1, 0)
	routing = pywrapcp.RoutingModel(manager)

	def distance_callback(from_index, to_index):
		from_node = manager.IndexToNode(from_index)
		to_node = manager.IndexToNode(to_index)
		return length(points[from_node], points[to_node])

	transit_callback_index = routing.RegisterTransitCallback(distance_callback)

	routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

	search_parameters = pywrapcp.DefaultRoutingSearchParameters()
	search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
	search_parameters.local_search_metaheuristic = (routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH)
	search_parameters.time_limit.seconds = 100 * 60
	search_parameters.log_search = True

	solution = routing.SolveWithParameters(search_parameters)
	if solution:
		print_solution(manager, routing, solution)
		routes = get_routes(solution, routing, manager)
		for i, route in enumerate(routes):
			print('Route', i, route)
		return routes[0][:-1], 0
	else:
		print("Can't solve!")
		return range(len(points)), 0

def get_routes(solution, routing, manager):
	routes = []
	for route_nbr in range(routing.vehicles()):
		index = routing.Start(route_nbr)
		route = [manager.IndexToNode(index)]
		while not routing.IsEnd(index):
			index = solution.Value(routing.NextVar(index))
			route.append(manager.IndexToNode(index))
		routes.append(route)
	return routes

def print_solution(manager, routing, solution):
	"""Prints solution on console."""
	print('Objective: {} miles'.format(solution.ObjectiveValue()))
	index = routing.Start(0)
	plan_output = 'Route for vehicle 0:\n'
	route_distance = 0
	while not routing.IsEnd(index):
		plan_output += ' {} ->'.format(manager.IndexToNode(index))
		previous_index = index
		index = solution.Value(routing.NextVar(index))
		route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
	plan_output += ' {}\n'.format(manager.IndexToNode(index))
	print(plan_output)
	plan_output += 'Route distance: {}miles\n'.format(route_distance)

if __name__ == '__main__':
	Point = namedtuple("Point", ['x', 'y'])

	input_data = open('./data/tsp_33810_1').read()

	lines = input_data.split('\n')

	nodeCount = int(lines[0])
	points = []
	for i in range(1, nodeCount+1):
		line = lines[i]
		parts = line.split()
		points.append(Point(float(parts[0]), float(parts[1])))
	ortools_routing(points)