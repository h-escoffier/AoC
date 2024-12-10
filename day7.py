# Day7 - AoC 2024 


from itertools import product
from tqdm import tqdm


# 1st Part
def load_data(file):
    all_output = []
    all_values = []
    with open(file, 'r') as file:
        for line in file:
            before, after = line.strip().split(':')
            all_output.append(int(before.strip()))
            all_values.append(list(map(int, after.strip().split())))
    
    return all_output, all_values


def create_combination(output, values): 
    for combination in product(['+', 'x'], repeat=len(values) - 1):
        print(combination)
        is_ok = calculate_combinations(values, combination, output)
        if is_ok:
            return True
    return False


def calculate_combinations(values, calcul, output):
    # print(values, calcul)
    total = values[0]
    for i in range(len(calcul)): 
        if calcul[i] == '+':
            total += values[i + 1]
        else:
            total *= values[i + 1]
        if total > output:
            return False
    if total == output:
        return True
    return False


def run_part1():
    sum = 0
    all_output, all_values = load_data('data/day7_input.txt')
    for output, values in tqdm(zip(all_output, all_values), desc='Progress Report - 1'):
        is_valid = create_combination(output, values)
        if is_valid:
            sum += output
    print(sum)


# 2nd Part
def create_combination_advanced(output, values):
    for combination in product(['+', 'x', '||'], repeat=len(values) - 1):
        is_ok = calculate_combinations_advanced(values, combination, output)
        if is_ok:
            return True
    return False


def calculate_combinations_advanced(values, calcul, output):
    total = values[0]
    for i in range(len(calcul)): 
        if calcul[i] == '+':
            total += values[i + 1]
        elif calcul[i] == 'x':
            total *= values[i + 1]
        else:
            total = int(str(total) + str(values[i + 1]))
        if total > output:
            return False
    if total == output:
        return True
    return False


def run_part2():
    sum = 0
    all_output, all_values = load_data('data/day7_input.txt')
    for output, values in tqdm(zip(all_output, all_values), desc='Progress Report - 2'):
        is_valid = create_combination_advanced(output, values)
        if is_valid:
            sum += output
    print(sum)


if __name__ == '__main__': 
    print('start')
    run_part1()
    run_part2()
    print('end')