# Day10 - AoC 2025 


# This is the first time I've used exec() - I've also learned the difference between exec() and eval() (a bit embarrassing...).
# The first part could have been much simpler. Thanks to Sebastien for pointing out that it was bound to be a combination of 1 and 0. 


import re
import highspy 
from tqdm import tqdm 
from highspy import HighsVarType


def read_input(path):
    with open(path) as f: 
        content = [line.strip() for line in f.readlines()]
    new_content = []
    for line in content: 
        splited= line.split(' ')
        pattern = splited[0]
        buttons = splited[1:len(splited) - 1]
        joltage = splited[len(splited) - 1]
        new_content.append([pattern, buttons, joltage])
    return new_content


# Part1
def translate_input(input): 
    configuration = []
    for elm in input: 
        if elm == '[' or elm == ']': 
            continue
        elif elm == '.': 
            configuration.append(0)
        else: 
            configuration.append(1)
    return configuration


def create_model(output, buttons): 
    h = highspy.Highs()
    h.setOptionValue("log_to_console", False)

    for i in range(len(buttons)): 
        var_string = f'x{i} = h.addVariable(lb = 0, ub = 1, type=HighsVarType.kInteger)' # 
        # print(var_string)
        exec(var_string)
    for j in range(len(output)): 
        var_string = f'k{j} = h.addVariable(lb = 0, type=HighsVarType.kInteger)'
        # print(var_string)
        exec(var_string)

    # Create constraints 
    for i in range(len(output)): 
        to_press = []
        for j in range(len(buttons)): 
            activators = list(map(int, re.findall(r'\d+', buttons[j])))
            if i in activators: 
                to_press.append(f'x{j}')
        
        # Create string and exec them
        all_to_press = '+'.join(to_press)
        if output[i] == 0: 
            condit_str = f'2*k{i}'
        else: 
            condit_str = f'2*k{i}+1'
        cnstr_string = f'h.addConstr({all_to_press} == {condit_str})'
        # print(cnstr_string)
        exec(cnstr_string)
    
    # Set objective 
    all_x_list = []
    for i in range(len(buttons)): 
        all_x_list.append(f'x{i}')
    all_x_list_string = '+'.join(all_x_list)
    obj_string = f'h.minimize({all_x_list_string})'
    # print(obj_string)
    exec(obj_string)

    h.getSolution()
    info = h.getInfo()
    return info.objective_function_value


def run_part1(): 
    content = read_input('2025/data/input_day10.txt')
    # content = read_input('2025/data/input_test.txt')
    nb_tap = 0 
    for row in tqdm(content): 
        output = translate_input(row[0])
        optimal = create_model(output, row[1])
        nb_tap += optimal
    print(int(nb_tap))


# Part2
def advanced_model(output, buttons, joltage): 
    h = highspy.Highs()
    h.setOptionValue("log_to_console", False)
    
    for i in range(len(buttons)): 
        var_string = f'x{i} = h.addVariable(lb = 0, type=HighsVarType.kInteger)'
        exec(var_string)

    # Add joltages
    joltages = list(map(int, re.findall(r'\d+', joltage)))

    for i in range(len(output)): 
        to_press = []
        for j in range(len(buttons)): 
            activators = list(map(int, re.findall(r'\d+', buttons[j])))
            if i in activators: 
                to_press.append(f'x{j}')

        all_to_press = '+'.join(to_press)
        joltage_str = f'h.addConstr({all_to_press} == {joltages[i]})'
        exec(joltage_str)
    
    # Set objective 
    all_x_list = []
    for i in range(len(buttons)): 
        all_x_list.append(f'x{i}')
    all_x_list_string = '+'.join(all_x_list)
    obj_string = f'h.minimize({all_x_list_string})'
    exec(obj_string)

    h.getSolution()
    info = h.getInfo()
    return info.objective_function_value


def run_part2(): 
    content = read_input('2025/data/input_day10.txt')
    # content = read_input('2025/data/input_test.txt')
    nb_tap = 0 
    for row in tqdm(content): 
        output = translate_input(row[0])
        optimal = advanced_model(output, row[1], row[2])
        nb_tap += optimal
    print(int(nb_tap))


if __name__ == '__main__': 
    print('start')
    run_part1()
    run_part2()
    print('end')