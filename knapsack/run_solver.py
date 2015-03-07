from solver import solve_it_main

def run_on_file(file_location):
    input_data_file = open(file_location, 'r')
    input_data = ''.join(input_data_file.readlines())
    input_data_file.close()
    val, taken = solve_it_main(input_data)
    print val

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