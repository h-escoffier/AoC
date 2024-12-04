# Day4 - AoC 2024 

# 1st Part 
def load_data(file):
    with open(file, "r") as file:
        data = [list(line.strip()) for line in file]
    return data


def horizontal_string(data):
    return ["".join(line) for line in data]


def vertical_string(data):
    vertical_data = ["".join([line[i] for line in data]) for i in range(len(data[0]))]
    return vertical_data


def diagonal_upper_right_string(data):  # Backward = Lower Right
    all_diagonals = []
    for nb_diag in range(len(data) + len(data[0]) - 1):  
        idx_col = nb_diag
        is_padding = False
        if nb_diag > len(data): 
            padding_col = nb_diag - len(data) + 1
            padding_line = nb_diag - len(data) 
            is_padding = True
        diagonal = []
        for z in range(nb_diag + 1):
            if idx_col < len(data) and not is_padding:  
                diagonal.append(data[idx_col][z]) 
                idx_col -= 1
            elif is_padding and (z + padding_line) < len(data):
                diagonal.append(data[idx_col - padding_col][z + padding_line])
                idx_col -= 1
        if diagonal != []:
            all_diagonals.append("".join(diagonal))
    return all_diagonals


def diagonal_upper_left_string(data): # Backward = Lower Left
    all_diagonals = []
    for nb_diag in range(len(data) + len(data[0]) - 1):
        idx_col = nb_diag
        is_padding = False
        if nb_diag > len(data): 
            padding_col = nb_diag - len(data) + 1
            padding_line = nb_diag - len(data) 
            is_padding = True
        diagonal = []
        for z in range(nb_diag + 1):
            if idx_col < len(data) and not is_padding:  
                diagonal.append(data[idx_col][len(data[0]) - z - 1]) 
                idx_col -= 1
            elif is_padding and (z + padding_line) < len(data):
                diagonal.append(data[idx_col - padding_col][len(data[0]) - (z + padding_line) - 1])
                idx_col -= 1
        if diagonal != []:
            all_diagonals.append("".join(diagonal))
    return all_diagonals 


def backward(data): 
    reversed_data = [line[::-1] for line in data]
    return reversed_data


def run_part1():
    data = load_data('data/day4_input.txt')
    count = 0
    horizontal_data = horizontal_string(data)
    vertical_data = vertical_string(data)
    diagonal_ur = diagonal_upper_right_string(data)
    diagonal_ul = diagonal_upper_left_string(data)
    for line in horizontal_data:             
        count += line.count('XMAS') 
    for line in vertical_data:             
        count += line.count('XMAS') 
    for line in diagonal_ur:             
        count += line.count('XMAS')
    for line in diagonal_ul:             
        count += line.count('XMAS')
    # Backward
    for line in backward(horizontal_data):             
        count += line.count('XMAS') 
    for line in backward(vertical_data):             
        count += line.count('XMAS') 
    for line in backward(diagonal_ur):             
        count += line.count('XMAS') 
    for line in backward(diagonal_ul):             
        count += line.count('XMAS') 
    print(count)
    
    
# 2nd Part
def coord_a(data): 
    coord = []
    for line in range(len(data)):
        for col in range(len(data[0])):
            if data[line][col] == 'A':
                coord.append((line, col))
    return coord


def remove_coord(coord): 
    # Remove first and last column 
    filtered_coord = [(x, y) for x, y in coord if x != 0 and x != 140]
    return filtered_coord


def check_diag(coord_a, data):
    count = 0
    for coord in coord_a:
        is_ok = 0
        try: 
            # check first diagonal
            if (data[coord[0] - 1][coord[1] - 1] == 'M' and data[coord[0] + 1][coord[1] + 1] == 'S') or (data[coord[0] - 1][coord[1] - 1] == 'S' and data[coord[0] + 1][coord[1] + 1] == 'M'):
                is_ok += 1
            # check second diagonal
            if (data[coord[0] - 1][coord[1] + 1] == 'M' and data[coord[0] + 1][coord[1] - 1] == 'S') or (data[coord[0] - 1][coord[1] + 1] == 'S' and data[coord[0] + 1][coord[1] - 1] == 'M'):
                is_ok += 1
            if is_ok == 2:
                count += 1
        except: 
            pass
    return count


def run_part2():
    data = load_data('data/day4_input.txt')
    # data = [['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M'],
    #         ['M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A'],
    #         ['A', 'M', 'X', 'S', 'X', 'M', 'A', 'A', 'M', 'M'],
    #         ['M', 'S', 'A', 'M', 'A', 'S', 'M', 'S', 'M', 'X'],
    #         ['X', 'M', 'A', 'S', 'A', 'M', 'X', 'A', 'M', 'M'],
    #         ['X', 'X', 'A', 'M', 'M', 'X', 'X', 'A', 'M', 'A'],
    #         ['S', 'M', 'S', 'M', 'S', 'A', 'S', 'X', 'S', 'S'],
    #         ['S', 'A', 'X', 'A', 'M', 'A', 'S', 'A', 'A', 'A'],
    #         ['M', 'A', 'M', 'M', 'M', 'X', 'M', 'M', 'M', 'M'],
    #         ['M', 'X', 'M', 'X', 'A', 'X', 'M', 'A', 'S', 'X']]
    coord = coord_a(data)
    print(coord)
    coord = remove_coord(coord)
    print(coord)
    count = check_diag(coord, data)
    print(count)


if __name__ == '__main__': 
    print('start')
    run_part1()
    run_part2()
    print('end')