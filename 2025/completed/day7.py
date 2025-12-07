# Day7 - AoC 2025 


# from helpers import print_maze


def read_input(path):
    with open(path, "r") as file:
        lines = file.readlines()
    maze = []
    for line in lines:
        line = line.strip()
        maze.append(list(line))
    return maze


# Part1
def found_start(content): 
    for row in range(len(content)):
        for col in range(len(content[0])):
            if content[row][col] == "S":
                start_pt = (col, row)
                break 
    return start_pt


def all_path(content, start): 
    init_x, init_y = start
    x = init_x
    y = init_y
    x_list = [x]
    finish = False
    total_split = 0 
    while not finish: 
        y, x_list, split, finish = walk(content, x_list, y)
        total_split += split
    return x_list, total_split


def walk(content, x_list, y): 
    y += 1 
    counter = 0 
    if y == len(content) - 1: 
        return y, len(x_list), 0, True
    else:
        new_x_list = []
        for x in x_list: 
            if content[y][x] == '.': 
                new_x_list.append(x)
            else: # == '^'
                counter += 1
                new_x_list.append(x-1)
                new_x_list.append(x+1)
        new_x_list = list(set(new_x_list))
        return y, new_x_list, counter, False
    

def run_part1(): 
    content = read_input('2025/data/input_day7.txt')
    # content = read_input('2025/data/input_test.txt')
    start = found_start(content)
    _, total = all_path(content, start)
    print(total)


# Part2
def advanced_all_path(content, start): 
    init_x, init_y = start
    x = init_x
    y = init_y
    x_dict = {
        x: 1
        }
    finish = False
    while not finish: 
        y, x_dict, finish = advanced_walk(content, x_dict, y)
    return x_dict


def advanced_walk(content, x_dict, y): 
    y += 1 
    if y == len(content) - 1: 
        return y, x_dict, True
    else:
        new_x_dict = dict()
        for x in x_dict.keys(): 
            if content[y][x] == '.': 
                    if x in new_x_dict.keys(): 
                        new_x_dict[x] += 1 * x_dict[x]
                    else:
                        new_x_dict[x] = x_dict[x]      
            else: # == '^'
                if x+1 in new_x_dict.keys(): 
                    new_x_dict[x+1] += 1 * x_dict[x]
                else: 
                    new_x_dict[x+1] = x_dict[x]   
                
                if x-1 in new_x_dict.keys(): 
                    new_x_dict[x-1] += 1 * x_dict[x]
                else: 
                    new_x_dict[x-1] = x_dict[x]
        return y, new_x_dict, False


def run_part2(): 
    content = read_input('2025/data/input_day7.txt')
    # content = read_input('2025/data/input_test.txt')
    start = found_start(content)
    all_path = advanced_all_path(content, start)
    sum = 0
    for elm in all_path.values(): 
        sum += elm 
    print(sum)


if __name__ == '__main__': 
    print('start')
    run_part1()
    run_part2()
    print('end')
