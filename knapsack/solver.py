#!/usr/bin/python
# -*- coding: utf-8 -*-

from . import Item
from greedy import solve_greedy
from branch_bound import solve_branch_bound

def solve_it_main(capacity, items):
    return solve_branch_bound(capacity, items)

def parse_input(input_data):
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in xrange(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    return capacity, items

def format_output(value, taken, optimal=False):
    opt = "1" if optimal else "0"
    output_data = str(value) + ' ' + opt + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data

def solve_it(input_data):
    capacity, items = parse_input(input_data)
    value, taken = solve_it_main(capacity, items)

    # prepare the solution in the specified output format
    return format_output(value, taken, True)

import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

