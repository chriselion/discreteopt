from . import length, length_squared, Point, tour_length

def greedy_sub(points, start_index):
    visited = set()
    path = [start_index]
    visited.add(start_index)

    prev = points[start_index]
    path_length = 0.0

    while len(visited) < len(points):
        # find the closest point
        min_dist_sq = float("inf")
        closest_index = -1
        for i, point in enumerate(points):
            if i in visited:
                continue
            dist_sq = length_squared(prev, point)
            if dist_sq < min_dist_sq:
                min_dist_sq = dist_sq
                closest_index = i

        path.append(closest_index)
        visited.add(closest_index)

        path_length += length(prev, points[closest_index])
        prev = points[closest_index]

    return path, path_length


def solve_greedy(points):
    best_path = None
    best_length = float("inf")
    k=10
    for i in xrange(0,k):
        path, path_length = greedy_sub(points, i)
        if path_length < best_length:
            best_length = path_length
            best_path = path

    return best_path, best_length