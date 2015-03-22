from . import length, length_squared, Point, tour_length

from collections import namedtuple
PointIndex = namedtuple("PointIndex", ['x', 'y', 'i'])
from itertools import cycle, islice

#from https://docs.python.org/2/library/itertools.html#recipes
def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    # Recipe credited to George Sakkis
    pending = len(iterables)
    nexts = cycle(iter(it).next for it in iterables)
    while pending:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            pending -= 1
            nexts = cycle(islice(nexts, pending))


class SortedPoints(object):
    def __init__(self, points):
        self.points = points
        xyi = [PointIndex(p.x,p.y,i) for i,p in enumerate(self.points)]

        self.sorted = sorted(xyi, key=lambda p: p.x)
        self.original_to_sorted = [-1]*len(points)
        for i, p in enumerate(self.sorted):
            self.original_to_sorted[p[2]] = i

    def get_closest_point(self, orig, visited):
        point = self.points[orig]
        start_index = self.original_to_sorted[orig]

        # search left
        best_point = None
        best_dist_sq = float("inf")
        for i in xrange(start_index-1, -1, -1):
            potential = self.sorted[i]
            if potential.i in visited:
                continue

            dx = potential.x - point.x
            if dx*dx > best_dist_sq:
                break

            dist_sq = length_squared(point, potential)
            if dist_sq < best_dist_sq:
                best_dist_sq = dist_sq
                best_point = potential

        # search right
        for i in xrange(start_index+1, len(self.points)):
            potential = self.sorted[i]
            if potential.i in visited:
                continue

            dx = potential.x - point.x
            if dx*dx > best_dist_sq:
                break

            dist_sq = length_squared(point, potential)
            if dist_sq < best_dist_sq:
                best_dist_sq = dist_sq
                best_point = potential

        assert best_point is not None
        return best_point.i


def greedy_sub(sp, points, start_index):
    visited = set()
    path = [start_index]
    visited.add(start_index)

    prev = points[start_index]
    prev_index = start_index
    path_length = 0.0

    while len(visited) < len(points):
        # find the closest point
        # min_dist_sq = float("inf")
        # closest_index = -1
        # for i, point in enumerate(points):
        #     if i in visited:
        #         continue
        #     dist_sq = length_squared(prev, point)
        #     if dist_sq < min_dist_sq:
        #         min_dist_sq = dist_sq
        #         closest_index = i

        closest_index = sp.get_closest_point(prev_index, visited)

        #if cp != closest_index:
        #    print length(prev, points[closest_index])
        #    print length(prev, points[cp])
        #assert cp == closest_index
        #assert abs(length(prev, points[closest_index]) - length(prev, points[cp])) < .1

        path.append(closest_index)
        visited.add(closest_index)

        path_length += length(prev, points[closest_index])
        prev = points[closest_index]
        prev_index = closest_index

    path_length += length(points[closest_index], points[start_index])
    return path, path_length


def solve_greedy(points):
    sp = SortedPoints(points)
    best_path = None
    best_length = float("inf")
    k=10
    for i in xrange(0,k):
        path, path_length = greedy_sub(sp, points, i)
        if path_length < best_length:
            best_length = path_length
            best_path = path

    return best_path, best_length