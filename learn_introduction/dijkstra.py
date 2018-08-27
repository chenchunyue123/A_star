#!/usr/bin/python3

class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.wall = []

    def in_bound(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id):
        return  id not in self.wall

    def neighbors(self, id):
        (x, y) = id
        result = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        if(x + y) % 2 == 0: result.reverse()
        result = filter(in_bound, result)
        result = filter(passable, result)
        return  result


class GridWithWeight(SquareGrid):
    def __init__(self, width, height):
        super.__init__(width, height)
        self.weight = {}

    def cost(self, from_node, to_node):
        return self.weight.get(to_node, 1)


import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

def dijkstra_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                came_from[next] = current
    return came_from, cost_so_far

def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

from implementation import draw_tile, draw_grid, diagram4

# from implementation import *

came_from, cost_so_far = dijkstra_search(diagram4, (1, 4), (7, 8))
draw_grid(diagram4, width=3, point_to=came_from, start=(1, 4), goal=(7, 8))
print()
draw_grid(diagram4, width=3, number=cost_so_far, start=(1, 4), goal=(7, 8))
print()
draw_grid(diagram4, width=3, path=reconstruct_path(came_from, start=(1, 4), goal=(7, 8)))