from solver import solve_it_main, parse_input

#copied from submit
def load_input_data(fileLocation):
    inputDataFile = open(fileLocation, 'r')
    inputData = ''.join(inputDataFile.readlines())
    inputDataFile.close()
    return inputData

def run_on_file(file_location):
    input_data = load_input_data(file_location)
    capacity, items = parse_input(input_data)
    value, taken = solve_it_main(capacity, items)
    print value

if __name__ == '__main__':
    files = [
        './data/ks_30_0',
        './data/ks_50_0',
        './data/ks_200_0',
        './data/ks_400_0',
        './data/ks_1000_0',
        './data/ks_10000_0'
    ]

    for f in files:
        run_on_file(f)