from . import Item
from itertools import combinations, chain

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def solve_brute_force(capacity, items):
    N = len(items)
    best_val, best_set = 0, None
    for t in powerset(items):
        weight = sum(i.weight for i in t)
        if weight > capacity:
            continue
        val = sum(i.value for i in t)
        if val > best_val:
            best_val = val
            best_set = t

    taken = [0]*N
    for i in best_set:
        taken[i.index] = 1

    return best_val, taken
