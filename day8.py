# Day8 - AoC 2024 


from tqdm import tqdm
from itertools import combinations
import math


# 1st Part
def load_data(file): 
    with open(file, 'r') as file:
        data = [line.strip() for line in file]
    return data


def find_frequencies(data): 
    frequencies = []
    frequencies_positions = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] != '.':
                if data[y][x] not in frequencies: 
                    frequencies.append(data[y][x])
                    frequencies_positions.append([(y, x)])
                else: 
                    idx = frequencies.index(data[y][x]) 
                    frequencies_positions[idx].append((y, x))
    return frequencies, frequencies_positions


def find_antinodes(data, p1, p2): 
    antinodes = []
    y1, x1 = p1
    y2, x2 = p2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    delta_x = (x2 - x1) / distance
    delta_y = (y2 - y1) / distance
    # Before
    xb = x1 - distance * delta_x
    yb = y1 - distance * delta_y
    pb = (yb, xb)
    # After 
    xa = x2 + distance * delta_x
    ya = y2 + distance * delta_y
    pa = (ya, xa)
    if 0 <= xa < len(data[0]) and 0 <= ya < len(data):
        antinodes.append(pa) 
    if 0 <= xb < len(data[0]) and 0 <= yb < len(data):
        antinodes.append(pb) 
    return antinodes


def run_part1(): 
    data = load_data('data/day8_input.txt')
    frequencies, frequencies_positions = find_frequencies(data)
    print('Nb_of_diff_freq ' + str(len(frequencies))) 
    # print(frequencies_positions)
    all_antinodes = []
    for i in tqdm(iterable=range(len(frequencies)), desc='Progress Report - 1'): 
        positions = combinations(frequencies_positions[i], 2)
        for duo in positions: 
            antinodes = find_antinodes(data, duo[0], duo[1])
            all_antinodes += antinodes
    all_antinodes = list(set(all_antinodes))
    print(len(all_antinodes))


# 2nd Part
def find_antinodes_advanced(data, p1, p2): 
    # Add antinodes at the position of p1 and p2
    antinodes = [p1, p2]
    is_outside = 0
    is_before_outside = False
    is_after_outside = False
    i = 0
    y1, x1 = p1
    y2, x2 = p2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    delta_x = (x2 - x1) / distance
    delta_y = (y2 - y1) / distance
    while is_outside != 2: 
        i += 1
        # print('i ' + str(i))
        if is_before_outside == False: 
            xb = x1 - i * distance * delta_x
            yb = y1 - i * distance * delta_y
            pb = (int(round(yb, 1)), int(round(xb, 1))) 
            # pb = (yb, xb)
            if 0 <= xb < len(data[0]) and 0 <= yb < len(data):
                antinodes.append(pb) 
            else:
                # print('Here before')
                is_before_outside = True
                is_outside += 1
        if is_after_outside == False:
                xa = x2 + i * distance * delta_x
                ya = y2 + i * distance * delta_y
                pa = (int(round(ya, 1)), int(round(xa, 1))) 
                # pa = (ya, xa)
                if 0 <= xa < len(data[0]) and 0 <= ya < len(data):
                    antinodes.append(pa) 
                else:
                    # print('Here after')
                    is_after_outside = True
                    is_outside += 1
    return antinodes    


def run_part2(): 
    data = load_data('data/day8_input_test.txt')
    frequencies, frequencies_positions = find_frequencies(data)
    # print('Nb_of_diff_freq ' + str(len(frequencies))) 
    all_antinodes = []
    for i in tqdm(iterable=range(len(frequencies)), desc='Progress Report - 2'): 
        positions = combinations(frequencies_positions[i], 2)
        for duo in positions: 
            antinodes = find_antinodes_advanced(data, duo[0], duo[1])
            all_antinodes += antinodes
    all_antinodes = list(set(all_antinodes))
    print(all_antinodes)
    print(len(all_antinodes))


if __name__ == '__main__': 
    print('start')
    # run_part1()
    run_part2()
    print('end')