import math
import math
from queue import PriorityQueue
from helpers import Map

def shortest_path(M: Map, start, goal):
    if start == goal:
        return [start]

    intersections_count = len(M.intersections)
    is_frontier = [False for _ in range(intersections_count)]
    is_explored = [False for _ in range(intersections_count)]
    g_distance = [math.inf for _ in range(intersections_count)]
    h_distance = [euclidean_distance(M, i, goal) for i in range(intersections_count)]

    priority_queue = PriorityQueue()
    priority_queue.put_nowait((0, start))
    is_frontier[start] = True
    g_distance[start] = 0

    parent = {start: None}
    while priority_queue.qsize() > 0:
        node_f, node = priority_queue.get_nowait()
        if is_explored[node]:
            continue

        is_explored[node] = True
        if node == goal:
            path = build_path(parent, start, goal)
            return path

        # add neighbors to frontiers
        add_frontiers(M, node, g_distance, h_distance, is_frontier, is_explored, priority_queue, parent)


def add_frontiers(M: Map, node, g_distance, h_distance, is_frontier, is_explored, priority_queue, parent):
    for neighbor in M.roads[node]:
        # ignore explored nodes
        if is_explored[neighbor]:
            continue

        # calculate cost of path from start to this neighbor
        g_distance_of_neighbor = g_distance[node] + euclidean_distance(M, node, neighbor)
        # now use heuristic estimation and path of covered cost to get an idea of path cost to goal
        f = g_distance_of_neighbor + h_distance[neighbor]

        if not is_frontier[neighbor]:
            is_frontier[neighbor] = True
            g_distance[neighbor] = g_distance_of_neighbor
            # neighbor has not be visited before
            priority_queue.put_nowait((f, neighbor))
            # keep track of it's parent
            parent[neighbor] = node
        else:
            # neighbor has been visited before, check if new path is low cost
            if g_distance_of_neighbor < g_distance[neighbor]:
                g_distance[neighbor] = g_distance_of_neighbor
                parent[neighbor] = node
                priority_queue.put_nowait((f, neighbor))


def build_path(parent, start, goal):
    path = [goal]
    current_parent = parent[goal]
    while current_parent != start:
        path.append(current_parent)
        current_parent = parent[current_parent]

    path.append(start)
    path.reverse()
    return path


def euclidean_distance(M: Map, p1: int, p2: int):
    x1, y1 = M.intersections[p1]
    x2, y2 = M.intersections[p2]
    return math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))