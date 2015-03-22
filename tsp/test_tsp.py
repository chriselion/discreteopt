import time
from solver import parse_input, solve_trivial
from greedy import solve_greedy
from opt2 import solve_2opt_brute_force, solve_2opt_rand
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
    points = parse_input(input_data)

    start_time = time.time()
    path, path_length = eval("solve_%s(points)" % args.method)
    end_time = time.time()

    print "%s solver for %s took %f seconds. path length is %f" % \
          (args.method, file_location, end_time-start_time, path_length)


if __name__ == '__main__':
    test_files = [
        #'./tsp/data/tsp_5_1',
        #'./tsp/data/tsp_10_1',
        #'./tsp/data/tsp_51_1',
        # './tsp/data/tsp_100_3',
        # './tsp/data/tsp_200_2',
         './tsp/data/tsp_574_1',
         './tsp/data/tsp_1889_1',
         './tsp/data/tsp_2319_1',
        # './tsp/data/tsp_33810_1'
    ]

    submit_files = [
        './tsp/data/tsp_51_1',
        './tsp/data/tsp_100_3',
        './tsp/data/tsp_200_2',
        './tsp/data/tsp_574_1',
        './tsp/data/tsp_1889_1',
        './tsp/data/tsp_33810_1'
    ]

    parser = argparse.ArgumentParser()
    parser.add_argument("--method", default="trivial", choices=["trivial", "greedy", "2opt_brute_force", "2opt_rand"])
    parser.add_argument("--files", default="test", choices=["test", "submit",])
    args = parser.parse_args()

    files = {"test": test_files, "submit": submit_files}

    for f in files[args.files]:
        run_on_file(f, args)