from utils import *
from copy import deepcopy

def two_opt(points):
    n = len(points)
    def two_opt_swap(route, i, k):
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
                    best_move = two_opt_swap(route, i, k)
                    start_again = True
        if not start_again:
            break
        else:
            route = best_move
            best_distance = best_move_distance
            print(x, ":", best_distance)
    return route, opt

def two_opt_first_improvement(points):
    n = len(points)
    def two_opt_swap(route, i, k):
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
                    best_move = two_opt_swap(route, i, k)
                    start_again = True
                    break
        if not start_again:
            break
        else:
            route = best_move
            best_distance = best_move_distance
            print(x, ":", best_distance)
    return route, opt