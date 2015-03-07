# BRUTE FORCE
# 19
# [0, 0, 1, 1]
# GREEDY
# 19
# [0, 0, 1, 1]

# ./knapsack/data/ks_19_0
# BRUTE FORCE
# 12248
# [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]
# GREEDY
# 12066
# [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]

from solver import parse_input
from branch_bound import solve_branch_bound
from greedy import solve_greedy

#copied from submit
def load_input_data(fileLocation):
    inputDataFile = open(fileLocation, 'r')
    inputData = ''.join(inputDataFile.readlines())
    inputDataFile.close()
    return inputData

def run_on_file(file_location):
    print file_location
    input_data = load_input_data(file_location)
    capacity, items = parse_input(input_data)

    print "GREEDY"
    value, taken = solve_greedy(capacity, items)
    print value
    print taken

    print "\nB&B"
    value, taken = solve_branch_bound(capacity, items)
    print value
    print taken


if __name__ == '__main__':
    files = [
        './knapsack/data/ks_4_0',
        './knapsack/data/ks_19_0',
        './knapsack/data/ks_30_0',
        './knapsack/data/ks_40_0',

    ]

    for f in files:
        run_on_file(f)