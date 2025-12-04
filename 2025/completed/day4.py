# Day4 - AoC 2025 


def read_input(path): 
    with open(path, "r") as file:
        lines = file.readlines()
    content = []
    for line in lines:
        line = line.strip()
        content.append(list(line))
    return content


# Part1 
def parse_roll(content): 
    accesible = 0 
    for i in range(len(content)): 
        row = content[i]
        for j in range(len(row)): 
            elm = row[j]
            if elm == '@': 
                nb_adj = count_adj(i,j, len(content), len(row), content)
                if nb_adj < 4: 
                    accesible += 1 
    return accesible


def count_adj(i, j, max_i, max_j, content): 
    counter = 0 
    if i - 1 >= 0 and j - 1 >= 0: 
        if content[i - 1][j - 1] == '@': 
            counter += 1 
    if j - 1 >= 0: 
        if content[i][j - 1] == '@': 
            counter += 1 
    if i + 1 < max_i and j - 1 >= 0: 
        if content[i + 1][j - 1] == '@': 
            counter += 1 
    if i - 1 >= 0: 
        if content[i - 1][j] == '@': 
            counter += 1
    if i + 1 < max_i:
        if content[i + 1][j] == '@': 
            counter += 1
    if i - 1 >= 0 and j + 1 < max_j: 
        if content[i - 1][j + 1] == '@': 
            counter += 1 
    if j + 1 < max_j: 
        if content[i][j + 1] == '@': 
            counter += 1 
    if i + 1 < max_i and j + 1 < max_j:
        if content[i + 1][j + 1] == '@': 
            counter += 1 
    return counter


def run_part1(): 
    content = read_input('2025/data/input_day4.txt')
    # content = read_input('2025/data/input_test.txt')
    nb_accesible = parse_roll(content)
    print(nb_accesible)


# Part2 
def advanced_parse_roll(content, update_content): 
    accesible = 0 
    for i in range(len(content)): 
        row = content[i]
        for j in range(len(row)): 
            elm = row[j]
            if elm == '@': 
                nb_adj = count_adj(i,j, len(content), len(row), content)
                if nb_adj < 4: 
                    accesible += 1 
                    update_content[i][j] = '.'
    return accesible, update_content


def run_part2(): 
    content = read_input('2025/data/input_day4.txt')
    # content = read_input('2025/data/input_test.txt')
    total_accesible = 0 
    # Init while loop
    accesible = 1
    update_content = content
    while accesible != 0:
        accesible, update_content = advanced_parse_roll(content, update_content)
        content = update_content
        total_accesible += accesible
    print(total_accesible)


if __name__ == '__main__': 
    print('start')
    run_part1()
    run_part2()
    print('end')
