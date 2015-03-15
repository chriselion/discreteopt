import time
from solver import parse_input
from greedy import solve_greedy
from min_conflict import solve_min_conflict
from dsatur import solve_dsatur
from iter_greedy import solve_iter_greedy
import argparse

#copied from submit
def load_input_data(fileLocation):
    inputDataFile = open(fileLocation, 'r')
    inputData = ''.join(inputDataFile.readlines())
    inputDataFile.close()
    return inputData

def run_on_file(file_location, args):
    #print "\n" + file_location
    input_data = load_input_data(file_location)
    num_nodes, edges = parse_input(input_data)

    start_time = time.time()
    #num_colors, coloring = solve_min_conflict(num_nodes, edges)
    num_colors, coloring = eval("solve_%s(num_nodes, edges)" % args.method)
    end_time = time.time()

    print "%s solver for %s took %f seconds. Best coloring is %d colors" % \
          (args.method, file_location, end_time-start_time, num_colors)


if __name__ == '__main__':
    test_files = [
        './coloring/data/gc_50_3',
        './coloring/data/gc_70_7',
        './coloring/data/gc_100_5',
        './coloring/data/gc_250_9',
        './coloring/data/gc_500_1',
        #'./coloring/data/gc_1000_5'
    ]

    submit_files = [
        './coloring/data/gc_50_3',
        './coloring/data/gc_70_7',
        './coloring/data/gc_100_5',
        './coloring/data/gc_250_9',
        './coloring/data/gc_500_1',
        './coloring/data/gc_1000_5'
    ]

    parser = argparse.ArgumentParser()
    parser.add_argument("--method", default="greedy", choices=["greedy", "min_conflict", "dsatur", "iter_greedy"])
    args = parser.parse_args()

    for f in submit_files:
        run_on_file(f, args)