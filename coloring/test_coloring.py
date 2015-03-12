import time
from solver import parse_input
from greedy import solve_greedy

#copied from submit
def load_input_data(fileLocation):
    inputDataFile = open(fileLocation, 'r')
    inputData = ''.join(inputDataFile.readlines())
    inputDataFile.close()
    return inputData

def run_on_file(file_location):
    #print "\n" + file_location
    input_data = load_input_data(file_location)
    num_nodes, edges = parse_input(input_data)

    start_time = time.time()
    num_colors, coloring = solve_greedy(num_nodes, edges)
    end_time = time.time()

    print "Greedy solver for %s took %f seconds. Best coloring is %d colors" % (file_location, end_time-start_time, num_colors)


if __name__ == '__main__':
    test_files = [
        './coloring/data/gc_4_1',
        './coloring/data/gc_20_1',
        './coloring/data/gc_50_3',
    ]

    submit_files = [
        './coloring/data/gc_50_3',
        './coloring/data/gc_70_7',
        './coloring/data/gc_100_5',
        './coloring/data/gc_250_9',
        './coloring/data/gc_500_1',
        './coloring/data/gc_1000_5'
    ]

    for f in submit_files:
        run_on_file(f)