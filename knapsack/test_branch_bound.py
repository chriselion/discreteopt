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
from branch_bound import solve_branch_bound, solve_branch_a_star
from greedy import solve_greedy

#copied from submit
def load_input_data(fileLocation):
    inputDataFile = open(fileLocation, 'r')
    inputData = ''.join(inputDataFile.readlines())
    inputDataFile.close()
    return inputData

def run_on_file(file_location):
    print "\n" + file_location
    input_data = load_input_data(file_location)
    capacity, items = parse_input(input_data)

    value, taken = solve_branch_bound(capacity, items)
    print "B&B: %s" % value
#    print taken


if __name__ == '__main__':
    test_files = [
        './knapsack/data/ks_4_0',
        './knapsack/data/ks_19_0',
        './knapsack/data/ks_30_0',
        './knapsack/data/ks_40_0',
        './knapsack/data/ks_50_0',
    ]

    submit_files = [
        './knapsack/data/ks_30_0',
        './knapsack/data/ks_50_0',
        './knapsack/data/ks_200_0',
        './knapsack/data/ks_400_0',
        './knapsack/data/ks_1000_0',
        './knapsack/data/ks_10000_0',
    ]

    for f in submit_files:
        run_on_file(f)