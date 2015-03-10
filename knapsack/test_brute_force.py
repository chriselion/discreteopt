from solver import parse_input
from brute_force import solve_brute_force
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
    print "BRUTE FORCE"
    value, taken = solve_brute_force(capacity, items)
    print value
    print taken

    print "GREEDY"
    value, taken = solve_greedy(capacity, items)
    print value
    print taken


if __name__ == '__main__':
    files = [
        './knapsack/data/ks_4_0',
        './knapsack/data/ks_19_0',
    ]

    for f in files:
        run_on_file(f)