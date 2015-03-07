from . import Item

def eval_greedy(items, item_count, capacity):
    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0]*item_count

    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight

    return value, taken

def solve_greedy(capacity, items):
    item_count = len(items)

    solns = []
    solns.append(eval_greedy(items, item_count, capacity))
    solns.append(eval_greedy(reversed(items), item_count, capacity))

    sorted_by_weight = sorted(items, key=lambda it: it.weight)
    solns.append(eval_greedy(sorted_by_weight, item_count, capacity))

    sorted_by_value = sorted(items, reverse=True, key=lambda it: it.value )
    solns.append(eval_greedy(sorted_by_value, item_count, capacity))

    sorted_by_density = sorted(items, reverse=True, key=lambda it: float(it.value) / float(it.weight) )
    solns.append(eval_greedy(sorted_by_density, item_count, capacity))

    sorted_soln = sorted(solns, reverse=True, key=lambda s: s[0])

    return sorted_soln[0]