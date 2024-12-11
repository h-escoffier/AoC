# Day11 - AoC 2024 


from tqdm import tqdm
from collections import deque 
import cProfile


def load_data(file):
    with open(file, 'r') as file:
        data = [line.split() for line in file]
    return data[0]


def rules(stone):
    if stone == '0': 
        return ['1']
    elif len(stone) % 2 == 1: 
        return [str(int(stone)*2024)]
    else:
        where_split = len(stone) // 2 
        return stone[:where_split], stone[where_split:]
    

def blinck(data):
    new_data = []
    for stone in data:
        new_stone_s = rules(stone)
        if len(new_stone_s) == 1: 
            new_data.append(new_stone_s[0])
        else : 
            part1, part2 = new_stone_s
            new_data.append(part1)
            new_data.append(part2)
    return new_data


def blinck_advanced(data): 
    new_data = deque()
    for stone in data:
        new_stone_s = rules(stone)
        new_data.extend(new_stone_s)
    return new_data


def run_part1(): 
    blinck_data = load_data('data/day11_input.txt')
    for _ in tqdm(iterable=range(75), desc='Progress Report'): 
        blinck_data = blinck_advanced(blinck_data)
    print(len(blinck_data)) 


def run_part2():
    blinck_data = load_data('data/day11_input.txt')
    for i in tqdm(iterable=range(75), desc='Progress Report'): 
        blinck_data = blinck_advanced(blinck_data)
        if len(blinck_data) > 25000000:
            where_split = len(blinck_data) // 2 
            blinck_data_part1 = blinck_data[where_split:]
            blinck_data_part2 = blinck_data[:where_split]
            when = i
            break
    print('Break')
    for i in tqdm(range(when, 75)): 
        print(i)
        blinck_data_part1 = blinck_advanced(blinck_data_part1)
        blinck_data_part2 = blinck_advanced(blinck_data_part2)
        print(len(blinck_data_part1))
        print(len(blinck_data_part2))
    print(len(blinck_data))


if __name__ == '__main__': 
    print('start')
    # run_part1()
    run_part2()
    print('end')