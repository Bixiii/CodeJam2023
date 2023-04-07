import sys


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

def create_asci_drawing(rows: int, cols: int):
    asci_drawing = ""
    for row in range(rows):
        if row == 0:
            asci_drawing = asci_drawing + ".." + "+-" * (cols - 1) + "+\n"
            asci_drawing = asci_drawing + ".." + "|." * (cols - 1) + "|\n"
        else:
            asci_drawing = asci_drawing + "+-" * cols + "+\n"
            asci_drawing = asci_drawing + "|." * cols + "|\n"

    asci_drawing = asci_drawing + "+-" * cols + "+"
    return asci_drawing


if __name__ == '__main__':

    with_files = False

    if with_files:
        input_file_name = "input_data/sample_ts1_input.txt"
        output_file_name = input_file_name.replace("input", "output")
        input_content = get_input_from_file(input_file_name)
    else:
        input_content = get_input_form_stdin()

    # create output solution
    output = ""
    number_graphics = 0
    for i, line in enumerate(input_content):
        if i == 0:
            number_graphics = int(line)
            continue
        [rows, cols] = line.split()
        output = output + "Case #" + str(i) + ":\n"
        output = output + create_asci_drawing(int(rows), int(cols)) + "\n"

    if with_files:
        output_file = open(output_file_name, 'w')
        output_file.writelines(output)
        output_file.close()
    else:
        print(output)
