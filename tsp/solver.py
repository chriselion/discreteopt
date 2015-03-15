#!/usr/bin/python
# -*- coding: utf-8 -*-

from . import length, Point, tour_length

def format_output(path, path_length, is_optimal=False):
    obj = path_length
    opt = "1" if is_optimal else "0"

    # prepare the solution in the specified output format
    output_data = str(obj) + ' ' + opt + '\n'
    output_data += ' '.join(map(str, path))

def solve_trivial(points):
    # build a trivial solution
    # visit the nodes in the order they appear in the file
    path =  range(0, len(points))
    path_length = tour_length(path, points)
    return path, path_length

def parse_input(input_data):
    lines = input_data.split('\n')

    nodeCount = int(lines[0])

    points = []
    for i in range(1, nodeCount+1):
        line = lines[i]
        parts = line.split()
        points.append(Point(float(parts[0]), float(parts[1])))
    return points


def solve_it(input_data):
    points = parse_input(input_data)

    path, path_length = solve_trivial(points)

    output_data = format_output(path, path_length)
    return output_data


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/tsp_51_1)'

