import sys
import itertools


def get_input_form_stdin():
    contents = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        contents.append(line)
    return contents


def get_input_from_file(input_file_name):
    input_file = open(input_file_name)
    contents = input_file.readlines()
    return contents

##############################
# Implementation of Solution #
##############################

if __name__ == '__main__':

    with_files = True  # locally we can use files, when submitting we need to change it to False
    input_file_name = "input_data/test_input.txt"
    output_file_name = input_file_name.replace("input", "output")

    # get input
    if with_files:
        input_content = get_input_from_file(input_file_name)
    else:
        input_content = get_input_form_stdin()

    # create output solution
    output = ""
    num_test_cases = int(input_content[0])

    for line in input_content:
        print(line.strip())

    # write output
    if with_files:
        output_file = open(output_file_name, 'w')
        output_file.writelines(output)
        output_file.close()
        print(output)
    else:
        print(output)
