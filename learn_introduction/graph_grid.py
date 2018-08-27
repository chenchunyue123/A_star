#!/usr/bin/python3

from implementation import *

class GraphGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []

    def in_bound(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id):
        return id not in self.walls

    def neighbors(self, id):
        (x, y) = id
        result = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        if(x + y)%2 == 0: result.reverse()
        result = filter(self.in_bound(), result)
        result = filter(self.passable(), result)
        return result

# g = GraphGrid(30, 15)
#
# g.walls = DIAGRAM1_WALLS
#
# draw_grid(g)

def breadth_first_search_2(graph, start):
    # return "came_from"
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        current = frontier.get()
        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current

    return came_from

def breadth_first_search_3(graph, start, goal):
    frontier = Queue()
    frontier.put(start)
    come_from = {}
    come_from[start] = None

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            if next not in come_from:
                frontier.put(next)
                come_from[next] = current

    return come_from

g = SquareGrid(30, 15)
g.walls = DIAGRAM1_WALLS

parents = breadth_first_search_3(g, (8, 7), (17, 2))
draw_grid(g, width= 2, point_to = parents, start = (8, 7), goal = (17, 2))

came_from, cost_so_far = dijkstra_search(diagram4, (1, 4), (7, 8))
draw_grid(diagram4, width=3, point_to=came_from, start=(1, 4), goal=(7, 8))
print()
draw_grid(diagram4, width=3, number=cost_so_far, start=(1, 4), goal=(7, 8))
print()
draw_grid(diagram4, width=3, path=reconstruct_path(came_from, start=(1, 4), goal=(7, 8)))
