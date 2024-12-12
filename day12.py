# Day12 - AoC 2024 

# Many thanks to Léonie for the help on this one 


def load_data(file):
    with open(file, "r") as file:
        data = [list(line.strip()) for line in file]
    return data


def identify_regions(data):
    all_regions = []
    actual_region = []
    # actual_letter = 'A'
    for y in range(len(data)): 
        for x in range(len(data[0])): 
            # print(data[y][x])
            # print(data[y][x])
            # print(actual_letter)
            # if data[y][x] != actual_letter and len(actual_region) > 0: 
            #     all_regions.append([actual_letter, list(actual_region)]) 
            #     actual_region = []
            #     actual_letter = data[y][x]
            # # elif data[y][x] == actual_letter: 
            # else: 
            actual_region = [(y, x)]
            all_connections, letter = is_connection(data, (y, x), data[y][x])  
            actual_region.extend(all_connections)
            # print(actual_region)
            all_regions.append([data[y][x], list(actual_region)]) 
            # print(all_regions)
                # exit()
    # print(all_regions)
    one_overlapping = True
    while one_overlapping:
        all_regions, one_overlapping = merge_regions(all_regions, one_overlapping)
        # print(len(all_regions))
    # print(len(all_regions))
    return all_regions


def merge_regions(data, one_overlapping):
    one_overlapping = False
    merged = {}
    for letter, positions in data:
        positions_set = set(positions)
        if letter not in merged:
            merged[letter] = [positions_set]
        else:
            found_overlap = False
            for group in merged[letter]:
                if group & positions_set:  # Check for intersection
                    group |= positions_set  # Merge the positions
                    found_overlap = True
                    one_overlapping = True
                    break
            if not found_overlap:
                merged[letter].append(positions_set)
    result = []
    for letter, groups in merged.items():
        for group in groups:
            result.append([letter, sorted(group)])
    return result, one_overlapping


def is_connection(data, position, actual_letter):
    all_connections = []
    is_ok, new_pos, actual_letter = check_above(data, position, actual_letter)
    # print(is_ok)
    if is_ok: 
        all_connections.append(new_pos)
    is_ok, new_pos, actual_letter = check_below(data, position, actual_letter)
    # print(is_ok)
    if is_ok: 
        all_connections.append(new_pos)
    is_ok, new_pos, actual_letter = check_left(data, position, actual_letter)
    # print(is_ok)
    if is_ok: 
        all_connections.append(new_pos)
    is_ok, new_pos, actual_letter = check_right(data, position, actual_letter)
    # print(is_ok)
    if is_ok: 
        all_connections.append(new_pos)
    return all_connections, actual_letter


def perimeter_from_region(data, region):
    fences = 0
    actual_letter = region[0]
    for pos in region[1]: 
        nb_neighbors = 4
        is_ok, _, actual_letter = check_above(data, pos, actual_letter)
        if is_ok:
            nb_neighbors -= 1
        is_ok, _, actual_letter = check_below(data, pos, actual_letter)
        if is_ok:
            nb_neighbors -= 1
        is_ok, _, actual_letter = check_left(data, pos, actual_letter)
        if is_ok:
            nb_neighbors -= 1
        is_ok, _, actual_letter = check_right(data, pos, actual_letter)
        if is_ok:
            nb_neighbors -= 1
        fences += nb_neighbors
    return fences


def check_above(data, pos, actual_letter): 
    y, x = pos
    x = int(x)
    y = int(y)
    if y - 1 >= 0: 
        if str(data[y - 1][x]) == actual_letter: 
            new_pos = (y - 1, x)
            return True, new_pos, actual_letter
    return False, pos, actual_letter


def check_below(data, pos, actual_letter):
    y, x = pos
    x = int(x)
    y = int(y)
    if y + 1 < len(data): 
        if str(data[y + 1][x]) == actual_letter: 
            new_pos = (y + 1, x)
            return True, new_pos, actual_letter
    return False, pos, actual_letter


def check_left(data, pos, actual_letter):
    y, x = pos
    x = int(x)
    y = int(y)
    if x - 1 >= 0: 
        if str(data[y][x - 1]) == actual_letter: 
            new_pos = (y, x - 1)
            return True, new_pos, actual_letter
    return False, pos, actual_letter


def check_right(data, pos, actual_letter):
    y, x = pos
    x = int(x)
    y = int(y)
    if x + 1 < len(data[0]): 
        if str(data[y][x + 1]) == actual_letter: 
            new_pos = (y, x + 1)
            return True, new_pos, actual_letter
    return False, pos, actual_letter


def process_all_possible_corners(data):
    all_possible_corners = []
    for y in range(len(data)): 
        for x in range(len(data[0])): 
            corners = corners_of_position((y, x))
            all_possible_corners.extend(corners)
    return all_possible_corners

def perimeter_from_region_advanced(data, region):
    all_possible_corners = process_all_possible_corners(data)
    line_of_fences = 0
    corner_that_i_hate = []
    lines = [] # [position, direction]
    all_corners = []
    remaining_corners = []
    for pos in region[1]: 
        corners = corners_of_position(pos)
        all_corners.extend(corners)
    for corner in all_corners:
        # print(corner)
        # print(all_corners.count(corner))
        if all_corners.count(corner) % 2 == 1:
            remaining_corners.append(corner)
        elif all_corners.count(corner) == 2:
            # Check if it the corner in the center of a square
            square_corners = calcul_the_square(corner)
            # print(square_corners[0])
            # print(square_corners[3])
            # print()
            if (square_corners[0] in all_corners) and (square_corners[3] in all_corners):
                corner_that_i_hate.append(corner)
            elif (square_corners[1] in all_corners) and (square_corners[2] in all_corners): 
            # elif (square_corners[1] and square_corners[2]) in all_corners:
                corner_that_i_hate.append(corner)
                # remaining_corners.append(corner) 
    line_of_fences = len(list(set(remaining_corners)))
    # final = list(set(all_possible_corners).intersection(set(corner_that_i_hate)))
    # print(list(set(final)))
    yeah = len(list(set(corner_that_i_hate))) // 9 
    return line_of_fences, yeah


def calcul_the_square(corner):
    y, x = corner
    corner1 =  (y - 1, x - 1)
    corner2 =  (y + 1, x - 1)
    corner3 =  (y - 1, x + 1)
    corner4 =  (y + 1, x + 1)
    square_corners = [corner1, corner2, corner3, corner4]
    return square_corners



def corners_of_position(position):
    y, x = position
    upper_left = (y - 0.5, x - 0.5)
    upper_right = (y + 0.5, x - 0.5)
    lower_left = (y - 0.5, x + 0.5)
    lower_right = (y + 0.5, x + 0.5)
    corners = [upper_left, upper_right, lower_left, lower_right]
    return corners


def run_part1():
    data = load_data('data/day12_input.txt')
    sum = 0
    regions = identify_regions(data)
    for region in regions: 
        area = len(region[1])
        perimeter = perimeter_from_region(data, region)
        sum += area * perimeter
    print(sum)


def run_part2(): 
    data = load_data('data/day12_input.txt')
    sum = 0
    regions = identify_regions(data)
    for region in regions: 
        area = len(region[1])
        yeah = 0
        # print(region[0])
        line_of_fences, yeah = perimeter_from_region_advanced(data, region)
        # print(line_of_fences)
        yeah = yeah * 2 
        sum += area * (line_of_fences + yeah)
    print(sum)


if __name__ == '__main__':
    print('start')
    # run_part1()
    run_part2()
    print('end')