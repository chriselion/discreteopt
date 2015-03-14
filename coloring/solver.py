#!/usr/bin/python
# -*- coding: utf-8 -*-

from greedy import solve_greedy
from dsatur import solve_dsatur
from iter_greedy import solve_iter_greedy

def parse_input(input_data):
    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])

    edges = []
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))
    return node_count, edges

def format_output(num_colors, is_optimal, solution):
    # prepare the solution in the specified output format
    opt = '1' if is_optimal else '0'
    output_data = str(num_colors) + ' ' + opt + '\n'
    output_data += ' '.join(map(str, solution))

    return output_data

def solve_trivial(node_count, edges):
    # build a trivial solution
    # every node has its own color
    solution = range(0, node_count)
    num_colors = node_count

    return num_colors, solution


def solve_it(input_data):
    node_count, edges = parse_input(input_data)
    num_colors, solution = solve_iter_greedy(node_count, edges)
    return format_output(num_colors, False, solution)

import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)'

