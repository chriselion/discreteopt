from . import Item
import time

class State:
    def __init__(self):
        self.index = -1
        self.knapsack = set()

    def is_valid(self, capacity):
        weight = sum(i.weight for i in self.knapsack)
        return weight <= capacity

    def get_value(self):
        return sum(i.value for i in self.knapsack)

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

        r = State()
        r.index = current_state.index+1
        r.knapsack = current_state.knapsack.copy()

        l_ok = l.is_valid(capacity)
        r_ok = r.is_valid(capacity)

        if l_ok and r_ok:
            # Push both
            # TODO queue R and update current
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