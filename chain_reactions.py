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

class Module:
    def __init__(self, module_idx, fun_values, connection_vector):
        self.module_idx = module_idx + 1
        self.visited = False
        if self.module_idx in connection_vector:
            self.is_start_module = False
        else:
            self.is_start_module = True
        self.next_module = connection_vector[module_idx]
        if self.next_module == 0:
            self.has_void_ending = True
        else:
            self.has_void_ending = False
        self.fun_value = fun_values[module_idx]

    def reset_module(self):
        self.visited = False


def activate_module(modules, module_idx, max_fun):
    """
    Activates one module, sets the flag for all visited modules and returns the max_fun for the path
    Needs to be done for all start modules
    """
    modules[module_idx].visited = True
    if modules[module_idx].is_start_module:
        max_fun = 0  # I hate that python is not scoped
    max_fun = max(modules[module_idx].fun_value, max_fun)
    if modules[module_idx].has_void_ending:
        return max_fun
    if modules[modules[module_idx].next_module].visited:
        return max_fun
    return activate_module(modules, modules[module_idx].next_module, max_fun)


def get_all_start_modules(modules):
    start_module_idx = []
    for module in modules.values():
        if module.is_start_module:
            start_module_idx.append(module.module_idx)
    return start_module_idx


def reset_all_modules(modules):
    for module in modules.values():
        module.reset_module()



if __name__ == '__main__':

    with_files = True  # locally we can use files, when submitting we need to change it to False
    input_file_name = "input_data/chain_reactions_sample_ts1_input.txt"
    output_file_name = input_file_name.replace("input", "output")

    # get input
    if with_files:
        input_content = get_input_from_file(input_file_name)
    else:
        input_content = get_input_form_stdin()

    # create output solution
    output = ""
    num_test_cases = int(input_content[0])

    for i in range(1, len(input_content), 3):
        modules = {}
        num_modules = int(input_content[i])
        fun_factors = [int(num) for num in input_content[i + 1].split()]
        connection_vector = [int(num) for num in input_content[i + 2].split()]
        for module_idx in range(0, num_modules):
            modules[module_idx + 1] = Module(module_idx, fun_factors, connection_vector)
        start_modules = get_all_start_modules(modules)
        start_permutations = list(itertools.permutations(start_modules))

        absolut_max_fun = 0
        for permutation in start_permutations:
            current_max_fun = 0
            for module_idx in permutation:
                current_max_fun = current_max_fun + activate_module(modules, module_idx, current_max_fun)
            reset_all_modules(modules)
            absolut_max_fun = max(absolut_max_fun, current_max_fun)
        output = output + "Case #" + str(int(i/3)+1) + ": " + str(absolut_max_fun) + "\n"

    # write output
    if with_files:
        output_file = open(output_file_name, 'w')
        output_file.writelines(output)
        output_file.close()
    else:
        print(output)
