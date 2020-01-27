
"""
Author: Ramiz Raja
Created on: 27/01/2020
"""
import math


def shortest_path(M,start,goal):
    print(euclidean_distance(M, start, goal))
    print("shortest path called")
    return


def euclidean_distance(M, p1: int, p2: int):
    x1, y1 = M.intersections[p1]
    x2, y2 = M.intersections[p2]
    return math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))