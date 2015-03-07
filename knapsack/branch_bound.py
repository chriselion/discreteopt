from . import Item
import time

class State:
    def __init__(self):
        self.index = -1
        self.knapsack = set()
        self.total_value = 0
        self.total_weight = 0

    def is_valid(self, best_val, capacity, items):
        if self.total_weight > capacity:
            return False
        best_case = self.get_best_case(items)
        #print "Optimistic: %d  current best: %d" % (best_case, best_val)
        if best_case <= best_val:
            return False
        return True

    def get_value(self):
        return self.total_value

    def get_best_case(self, items):
        # Naive approach - best case is current value plus everything not tried yet
        current_value = self.get_value()
        for i in xrange(self.index, len(items)):
            current_value += items[i].value
        return current_value

def get_taken(knapsack, items):
    taken = [0] * len(items)
    for i in knapsack:
        taken[i.index] = 1
    return taken

def solve_branch_bound(capacity, items):
    start_time = time.time()
    best_val = 0
    best_set = set()

    current_state = State()
    current_state.index = 0
    stack = []

    num_steps = 0

    while True:
        num_steps += 1
        # get "left" state using item
        # get "right" state not using item
        # if left is valid and right is valid
            # stack.push(right)
            # current state = left
        # else if left is valid
            # current state = left
        # else if right if valid
            # current state = right
        # else
            # current state = stack.pop()

        #print "Current state: " + str( get_taken(current_state.knapsack, items) )

        current_value = current_state.get_value()
        if current_value > best_val:
            best_val = current_value
            best_set = current_state.knapsack

        #print "Index: %d  num items: %d" % (current_state.index, len(items))
        if current_state.index >= len(items):
            if stack:
                current_state = stack.pop()
                continue
            else:
                break

        #print "Adding nodes"
        l = State()
        l.index = current_state.index+1
        l.knapsack = current_state.knapsack.copy()
        l.knapsack.add(items[current_state.index])
        l.total_value = current_state.total_value + items[current_state.index].value
        l.total_weight = current_state.total_weight + items[current_state.index].weight

        r = State()
        r.index = current_state.index+1
        r.knapsack = current_state.knapsack.copy()
        r.total_value = current_state.total_value
        r.total_weight = current_state.total_weight

        l_ok = l.is_valid(best_val, capacity, items)
        r_ok = r.is_valid(best_val, capacity, items)

        if l_ok and r_ok:
            stack.append(r)
            current_state = l
        elif l_ok:
            current_state = l
        elif r_ok:
            current_state = r
        else:
            if stack:
                current_state = stack.pop()
            else:
                break

    end_time = time.time();
    print "Branch and Bound for %d items searched %d nodes in %f seconds" % (len(items), num_steps, end_time - start_time)
    taken = get_taken(best_set, items)

    return best_val, taken