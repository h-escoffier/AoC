# Day12 - AoC 2024 


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


def is_fence_here(all_fences, position):
    # part2 ? 
    pass 


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


def perimeter_from_region_advanced(data, region):
    line_of_fences = 0
    lines = [] # [position, direction]
    actual_letter = region[0]
    for pos in region[1]: 
        nb_neighbors = 4
        is_ok, _, actual_letter = check_above(data, pos, actual_letter)
        if not is_ok:
            nb_neighbors -= 1
        is_ok, _, actual_letter = check_below(data, pos, actual_letter)
        if not is_ok:
            nb_neighbors -= 1
        is_ok, _, actual_letter = check_left(data, pos, actual_letter)
        if not is_ok:
            nb_neighbors -= 1
        is_ok, _, actual_letter = check_right(data, pos, actual_letter)
        if not is_ok:
            not nb_neighbors -= 1
        fences += nb_neighbors
    return fences
def run_part1():
    data = load_data('data/day12_input.txt')
    sum = 0
    regions = identify_regions(data)
    for region in regions: 
        area = len(region[1])
        perimeter = perimeter_from_region(data, region)
        sum += area * perimeter
    print(sum)


if __name__ == '__main__':
    print('start')
    run_part1()
    print('end')