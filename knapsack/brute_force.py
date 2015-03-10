from . import Item
import time
from itertools import combinations, chain

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def solve_brute_force(capacity, items):
    start_time = time.time()
    num_steps = 0
    N = len(items)
    best_val, best_set = 0, None
    for t in powerset(items):
        num_steps += 1
        weight = sum(i.weight for i in t)
        if weight > capacity:
            continue
        val = sum(i.value for i in t)
        if val > best_val:
            best_val = val
            best_set = t

    end_time = time.time()
    taken = [0]*N
    for i in best_set:
        taken[i.index] = 1

    print "Branch and Bound for %d items searched %d nodes in %f seconds" % (len(items), num_steps, end_time - start_time)

    return best_val, taken
