from __future__ import print_function
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
from utils import *
from naive import *

def ortools_routing(customers, depot, customer_count, vehicle_count, vehicle_capacity):

	# Create the routing index manager.
	manager = pywrapcp.RoutingIndexManager(len(customers), vehicle_count, 0)

	# Create Routing Model.
	routing = pywrapcp.RoutingModel(manager)


	# Create and register a transit callback.
	def distance_callback(from_index, to_index):
		"""Returns the distance between the two nodes."""
		# Convert from routing variable Index to distance matrix NodeIndex.
		from_node = manager.IndexToNode(from_index)
		to_node = manager.IndexToNode(to_index)
		return length(customers[from_node], customers[to_node])

	transit_callback_index = routing.RegisterTransitCallback(distance_callback)

	# Define cost of each arc.
	routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)


	# Add Capacity constraint.
	def demand_callback(from_index):
		"""Returns the demand of the node."""
		# Convert from routing variable Index to demands NodeIndex.
		from_node = manager.IndexToNode(from_index)
		return customers[from_node].demand

	demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
	routing.AddDimensionWithVehicleCapacity(
		demand_callback_index,
		0,  # null capacity slack
		[vehicle_capacity] * vehicle_count,  # vehicle maximum capacities
		True,  # start cumul to zero
		'Capacity')

	# Setting first solution heuristic.
	search_parameters = pywrapcp.DefaultRoutingSearchParameters()
	search_parameters.first_solution_strategy = (
		routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
	search_parameters.local_search_metaheuristic = (
		routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH)
	search_parameters.time_limit.seconds = 120 * 60
	search_parameters.log_search = True

	# Solve the problem.
	solution = routing.SolveWithParameters(search_parameters)

	# Print solution on console.
	if solution:
		all_routes = []
		total_distance = 0
		total_load = 0
		for vehicle_id in range(vehicle_count):
			index = routing.Start(vehicle_id)
			plan_output = 'Route for vehicle {}:\n'.format(vehicle_id)
			route = []
			route_distance = 0
			route_load = 0
			while not routing.IsEnd(index):
				node_index = manager.IndexToNode(index)
				route.append(customers[node_index])
				route_load += customers[node_index].demand
				plan_output += '{0} Load({1}) -> '.format(node_index, route_load)
				previous_index = index
				index = solution.Value(routing.NextVar(index))
				route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
				plan_output += ' {0} Load({1})\n'.format(manager.IndexToNode(index), route_load)
				plan_output += 'Distance of the route: {}m\n'.format(route_distance)
				plan_output += 'Load of the route: {}\n'.format(route_load)
				print(plan_output)
				total_distance += route_distance
				total_load += route_load
			route.append(customers[0])
			all_routes.append(route[1:-1])
		print('Total distance of all routes: {}m'.format(total_distance))
		print('Total load of all routes: {}'.format(total_load))
		print(all_routes)
		return all_routes, 0
	else:
		return naive(customers, depot, customer_count, vehicle_count, vehicle_capacity)


if __name__ == '__main__':
	from collections import namedtuple
	Customer = namedtuple("Customer", ['index', 'demand', 'x', 'y'])
	input_data = open('./data/vrp_16_5_1').read()
	lines = input_data.split('\n')

	parts = lines[0].split()
	customer_count = int(parts[0])
	vehicle_count = int(parts[1])
	vehicle_capacity = int(parts[2])
	
	customers = []
	for i in range(1, customer_count+1):
		line = lines[i]
		parts = line.split()
		customers.append(Customer(i-1, int(parts[0]), float(parts[1]), float(parts[2])))

	#the depot is always the first customer in the input
	depot = customers[0] 
	ortools_routing(customers, depot, customer_count, vehicle_count, vehicle_capacity)