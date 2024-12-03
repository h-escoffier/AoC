# Day2 - AoC 2024 


import re 
from tqdm import tqdm


# 1st Part
def load_data(file):
    with open(file) as f:
        data = f.readlines()
        data = [x.strip() for x in data]
    return data


def find_pattern(data): 
    pattern = r"mul\((\d+),(\d+)\)"
    finded_pattern = re.findall(pattern, data)
    return finded_pattern


def multiply(a, b):
    a = int(a)
    b = int(b)
    return a * b


def run_part1():
    all_pattern = []
    sum = 0 
    data = load_data('data/day3_input.txt')
    for i in tqdm(iterable=range(len(data)), desc='Progress Report - 1'):
        finded_pattern = find_pattern(data[i])
        print(finded_pattern)
        all_pattern += finded_pattern
    for a, b in all_pattern:
        sum += multiply(a, b)
    print(sum)


# 2nd Part
def one_str(data):
    return "".join(data)


def find_pattern_advanced(data):
    pattern = r"mul\((\d+),(\d+)\)"
    all_pattern = [(finded_pattern.group(1, 2), finded_pattern.start()) for finded_pattern in re.finditer(pattern, data)]
    return all_pattern


def find_pattern_do_dont(data): 
    pattern = r"do\(\)"
    start_do = [finded_pattern.start() for finded_pattern in re.finditer(pattern, data)]
    pattern = r"don't\(\)"
    start_dont = [finded_pattern.start() for finded_pattern in re.finditer(pattern, data)]
    return start_do, start_dont


def closest_inferior_idx(list_do_or_dont, idx_mul):
    filtered_idx = [idx for idx in list_do_or_dont if idx < idx_mul]
    return max(filtered_idx, default=0)


def run_part2():
    sum = 0
    data = load_data('data/day3_input.txt')
    data = one_str(data)
    all_pattern = find_pattern_advanced(data)
    start_do, start_dont = find_pattern_do_dont(data)
    for pattern in tqdm(iterable=all_pattern, desc='Progress Report - 2'):
        filtered_idx_do = closest_inferior_idx(start_do, pattern[1])
        filtered_idx_dont = closest_inferior_idx(start_dont, pattern[1])
        if filtered_idx_do == 0 and filtered_idx_dont == 0:
            sum += multiply(pattern[0][0], pattern[0][1])    
        elif filtered_idx_do > filtered_idx_dont:
            sum += multiply(pattern[0][0], pattern[0][1])
    print(sum)
        

if __name__ == '__main__': 
    print('start')
    run_part2()
    print('end')