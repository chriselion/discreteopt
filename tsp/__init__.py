import math
from collections import namedtuple

Point = namedtuple("Point", ['x', 'y'])

def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

def length_squared(point1, point2):
    return (point1.x - point2.x)**2 + (point1.y - point2.y)**2

def tour_length(path, points):
    # calculate the length of the tour
    node_count = len(path)
    obj = length(points[path[-1]], points[path[0]])
    for index in xrange(0, node_count-1):
        obj += length(points[path[index]], points[path[index+1]])
    return obj