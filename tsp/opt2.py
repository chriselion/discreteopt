from . import length, length_squared, Point, tour_length

def eval_2opt(points, path, start, end):
    # [1  2  3  4  5  6  7  8]
    #     i        j
    #  p1 p2       p3 p4
    # [1  5  4  3  2  6  7  8]
    #  p1 p3       p2 p4
    N = len(points)
    # Swap if we'd wrap around
    # TODO handle this
    if start > end:
        end, start = start, end
    before = (start + N - 1) % N
    after = (end+1) % N
    p1 = points[path[before]]
    p2 = points[path[start]]
    p3 = points[path[end]]
    p4 = points[path[after]]

    delta = length(p1, p3) + length(p2, p4) - length(p1, p2) - length(p3, p4)
    return delta

def perform_2opt(points, path, index1, index2):
    N = len(points)
    assert len(set(path)) == N
    path[index1:index2+1] = path[index1:index2+1][::-1]
    assert len(set(path)) == N

def solve_2opt_brute_force(points):
    # start with the naive solution
    N = len(points)
    path = range(0, len(points))
    path_cost = tour_length(path, points)

    changed = True
    while changed:
        changed = False
        for i in xrange(0, N):
            for j in xrange(i+1, N):
                if i == j:
                    continue
                if i == 0 and j == N-1:
                    continue
                delta_dist = eval_2opt(points, path, i, j)
                if delta_dist < -.001:
                    #print "before: %s" % path
                    #print "i=%d  j=%d" % (i,j)
                    perform_2opt(points, path, i, j)

                    #print "after: %s" % path
                    changed = True
                    #old_path_cost = path_cost
                    path_cost += delta_dist

        new_path_cost = tour_length(path, points)
        #print new_path_cost, path_cost
        #actual_delta = new_path_cost - old_path_cost
        #print "delta: expected: %f  actual: %f" % (delta_dist, actual_delta)
        assert abs(new_path_cost - path_cost) / float(N) < .01
        path_cost = new_path_cost
        #print "Total cost: %f" % path_cost

    return path, path_cost