# Day10 - AoC 2024 


from tqdm import tqdm


def load_data(file): 
    with open(file, 'r') as file:
        data = [line.strip() for line in file]
    return data


def find__all_start(data):
    all_start = []
    for y in range(len(data)): 
        for x in range(len(data[0])): 
            if data[y][x] == '0': 
                all_start.append((y, x))
    return all_start


def check_above(data, pos, actual_height): 
    y, x = pos
    x = int(x)
    y = int(y)
    if y - 1 >= 0: 
        if int(data[y - 1][x]) == int(actual_height) + 1: 
            new_pos = (y - 1, x)
            return True, new_pos, int(actual_height) + 1
    return False, pos, int(actual_height)


def check_below(data, pos, actual_height):
    y, x = pos
    x = int(x)
    y = int(y)
    if y + 1 < len(data): 
        if int(data[y + 1][x]) == int(actual_height) + 1: 
            new_pos = (y + 1, x)
            return True, new_pos, int(actual_height) + 1
    return False, pos, int(actual_height)


def check_left(data, pos, actual_height):
    y, x = pos
    x = int(x)
    y = int(y)
    if x - 1 >= 0: 
        if int(data[y][x - 1]) == int(actual_height) + 1: 
            new_pos = (y, x - 1)
            return True, new_pos, int(actual_height) + 1
    return False, pos, int(actual_height) 


def check_right(data, pos, actual_height):
    y, x = pos
    x = int(x)
    y = int(y)
    if x + 1 < len(data[0]): 
        if int(data[y][x + 1]) == int(actual_height) + 1: 
            new_pos = (y, x + 1)
            return True, new_pos, int(actual_height) + 1
    return False, pos, int(actual_height)


def check_complete_path(data, start, part): 
    actual_height = 0
    valid_path = 0
    pos = start
    all_positions_possible = [[pos, actual_height]]
    for pos in all_positions_possible: 
        pos_block = 0
        if check_above(data, pos[0], pos[1])[0]:
            all_positions_possible.append([check_above(data, pos[0], pos[1])[1], check_above(data, pos[0], pos[1])[2]])
        else: 
            pos_block += 1 
        if check_below(data, pos[0], pos[1])[0]:
            all_positions_possible.append([check_below(data, pos[0], pos[1])[1], check_below(data, pos[0], pos[1])[2]])
        else: 
            pos_block += 1
        if check_left(data, pos[0], pos[1])[0]:
            all_positions_possible.append([check_left(data, pos[0], pos[1])[1], check_left(data, pos[0], pos[1])[2]])
        else: 
            pos_block += 1
        if check_right(data, pos[0], pos[1])[0]:
            all_positions_possible.append([check_right(data, pos[0], pos[1])[1], check_right(data, pos[0], pos[1])[2]])
        else:
            pos_block += 1
    if part == 1:
        all_positions_possible_no_duplicate = []
        for all_pos in all_positions_possible: 
            if all_pos not in all_positions_possible_no_duplicate and all_pos[1] == 9: 
                all_positions_possible_no_duplicate.append(all_pos)
                valid_path += 1
    if part == 2:
        for all_pos in all_positions_possible: 
            if all_pos[1] == 9: 
                valid_path += 1
    return valid_path
        
    
def run_part1_and2(part): 
    data = load_data('data/day10_input.txt')
    all_start = find__all_start(data)
    all_valid_path = 0
    for start in all_start:
        valid_path = check_complete_path(data, start, part)
        all_valid_path += valid_path
    print(all_valid_path)


if __name__ == '__main__': 
    print('start')
    run_part1_and2(1)
    run_part1_and2(2)
    print('end')
