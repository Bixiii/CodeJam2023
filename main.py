import time

if __name__ == '__main__':

    # setup
    input_files = [
        'input_data/input.in',
    ]

    for input_file in input_files:

        # create name for output file
        output_file_name = 'output_data/' + input_file[input_file.find('/'):input_file.find('.')] + '.txt'  # add timestamp time.strftime('%H%M%S')

        # read input
        input_file = open(input_file)
        lines = input_file.readlines()

        # do something with the input
        for i, line in enumerate(lines):
            print(line.strip())

        # # write result to file
        output_file = open(output_file_name, 'w')
        for line in lines:
            output_file.writelines(line + '\n')
        output_file.close()
