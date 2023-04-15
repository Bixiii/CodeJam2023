import sys
import itertools
from typing import List


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
def compare_char(a, b):
    if ord(a) == ord(b):
        return 0
    elif ord(a) < ord(b):
        return 1
    return -1


# def compare_string(a, b):
#     result = compare_char(a[0], b[0])
#     if result == 0:
#         result = compare_string(a[1:], b[1:])
#     return result
#

def least_char(input_string):
    # use enumerate to keep track of the index as
    # you are iterating over a list
    min_value = input_string[0]
    min_pos = 1
    for index, ch in enumerate(input_string, 1):
        # check to see if current char is closer to
        # front of alphabet than our current minimum
        if ch < min_value:
            # if so, keep track of the current pos/value
            # as the new minimum
            min_pos = index
            min_value = ch
            # pythonic: min_pos, min_value = index, ch
    return min_pos, min_value


def is_sorted(sub_string_list):
    sorted_list = sub_string_list.copy()
    sorted_list.sort()
    return sorted_list == sub_string_list


def increase_value(to_be_mod, increase_compare, index):
    # print("to_be_mod, increase_compare, index",to_be_mod, increase_compare, index)
    letters_bigger = (x for x in to_be_mod[index:] if ord(x) >= ord(increase_compare[index]))
    letters_bigger_array = []
    for x in letters_bigger:
        letters_bigger_array.append((x, to_be_mod.index(x)))
    if len(letters_bigger_array) == 0:
        # we dont have any candidates, impossible
        # print("no candidates for value increase")
        return False
    # print("letters bigger array",letters_bigger_array)
    candidate_index = letters_bigger_array[0][1]
    # splice the candidate to the front
    return to_be_mod[:index] + to_be_mod[candidate_index] + to_be_mod[index:candidate_index] + to_be_mod[
                                                                                               candidate_index + 1:]


def resolve_case(index, num_substrings: int, sub_string_list):
    # print(str(index) + "----num_sub: " + str(num_substrings) + " substrings " + str(sub_string_list))

    # is it already sorted, early exit
    if is_sorted(sub_string_list):
        # print("SORTED list", sub_string_list)
        return True, sub_string_list

    is_possible = False
    solution = sub_string_list

    # sort the first substring to ensure min value
    solution[0] = ''.join(sorted(solution[0]))
    # # print("sorted first substring: ", solution[0])

    # check in pairs
    index = 1
    while index < len(solution):
        # a is value minimized by the last operation
        a = solution[index - 1]
        solution[index] = ''.join(sorted(solution[index]))

        if is_sorted([a, solution[index]]):
            # that worked, both are value minimized and still sorted
            # print("SORTED pair", [a, solution[index]])
            index += 1
            continue

        # we value minimized both but now solution[index] is smaller, we need to try and modify solution[index]
        char_index = 0
        while char_index + 1 <= len(solution[index]) and not is_sorted([a, solution[index]]):
            inc = increase_value(solution[index], a, char_index)
            if inc == False:
                # no candidates found
                return False, []
            # print("modified:", solution[index], inc, char_index)
            solution[index] = inc
            char_index += 1
        index += 1
    is_possible = is_sorted(solution)
    # print("looks good", is_possible, solution)
    return is_possible, solution


if __name__ == '__main__':

    with_files = False  # locally we can use files, when submitting we need to change it to False
    input_file_name = "input_data/game_sort_part_1_sample_ts1_input.txt"
    output_file_name = input_file_name.replace("input", "output")

    # get input
    if with_files:
        input_content = get_input_from_file(input_file_name)
    else:
        input_content = get_input_form_stdin()

    # create output solution
    output = ""
    num_test_cases = int(input_content[0])

    for i in range(1, num_test_cases * 2, 2):
        index = int(((i + 1) / 2))
        num_substrings = int(input_content[i])
        sub_string_list = input_content[i + 1].split()
        is_possible, solution = resolve_case(index, num_substrings, sub_string_list)
        output += "Case #" + str(index) + ": "
        if is_possible:
            output += "POSSIBLE"
            output += "\n"
            output += str(solution)
        else:
            output += "IMPOSSIBLE"
        output += "\n"

    # write output
    if with_files:
        output_file = open(output_file_name, 'w')
        output_file.writelines(output)
        output_file.close()
        print(output)
    else:
        print(output)
