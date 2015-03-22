from . import length, length_squared, Point, tour_length
import math
import random
import time

time_eval = 0.0
time_perform = 0.0

def eval_2opt(points, path, start, end):
    start_time = time.time()
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
    end_time = time.time()
    global time_eval
    time_eval += end_time - start_time
    return delta

def perform_2opt(points, path, index1, index2):
    start_time = time.time()
    N = len(points)
    #assert len(set(path)) == N
    path[index1:index2+1] = path[index1:index2+1][::-1]
    #assert len(set(path)) == N
    end_time = time.time()
    global time_perform
    time_perform += end_time - start_time


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
                if i == 0 and j == N-1:
                    continue
                delta_dist = eval_2opt(points, path, i, j)
                if delta_dist < -.001:
                    perform_2opt(points, path, i, j)

                    changed = True
                    path_cost += delta_dist

        #new_path_cost = tour_length(path, points)
        #assert abs(new_path_cost - path_cost) / float(N) < .01
        #path_cost = new_path_cost

    path_cost = tour_length(path, points)
    return path, path_cost

def solve_2opt_rand(points):
    global time_eval, time_perform
    time_eval = 0.0
    time_perform = 0.0
    # start with the naive solution
    N = len(points)
    path = range(0, len(points))
    path_cost = tour_length(path, points)

    # set the seed for consistency
    random.seed(N)
    best_of = 5
    max_iter = 10*int(math.sqrt(N))

    for k in xrange(0, max_iter):
        for i in xrange(0, N-1):
            j = random.randint(i+1, N-1)
            ## if i = 7 and N = 10, xrange -> [8,9], so sample size is N-i-1
            #js = random.sample(xrange(i+1, N), min(best_of, N-i-1))
            js = [random.randint(i+1, N-1) for r in xrange(0, best_of)]
            #for j in xrange(i+1, N):
            best_delta = float("inf")
            best_j = -1
            for j in js:
                if i == 0 and j == N-1:
                    continue
                delta_dist = eval_2opt(points, path, i, j)
                if delta_dist < best_delta:
                    best_delta = delta_dist
                    best_j = j
            if best_delta < -.001:
                perform_2opt(points, path, i, best_j)

                path_cost += best_delta

        #new_path_cost = tour_length(path, points)
        #assert abs(new_path_cost - path_cost) / float(N) < .01
        #path_cost = new_path_cost

    print "Time spent: eval: %f seconds  perform: %f seconds" % (time_eval, time_perform)
    path_cost = tour_length(path, points)
    return path, path_cost