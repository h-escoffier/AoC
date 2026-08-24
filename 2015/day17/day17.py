# AoC 2015 - Day17


from tqdm import tqdm 
from itertools import combinations


def readInput(path): 
    with open(path) as f: 
        content = [int(line.rstrip()) for line in f.readlines()]
    return content


def is_valid_combination(input, target): 
    count = 0 
    for i in tqdm(iterable=range(1, len(input)), desc='part1'): 
        for comb in combinations(input, i): 
            if sum(comb) == target: 
                count += 1 
    return count


def runPart1(): 
    input = readInput("2015/data/input_day17.txt")
    target = 150
    nb_valid = is_valid_combination(input, target)
    print(nb_valid)


def is_valid_combination_advanced(input, target): 
    possible = False
    for i in tqdm(iterable=range(1, len(input)), desc='part2'): 
        count = 0 
        for comb in combinations(input, i): 
            if sum(comb) == target: 
                possible = True
                count += 1 
        if possible == True: 
            return count
    return count 


def runPart2(): 
    input = readInput("2015/data/input_day17.txt")
    target = 150 
    nb_valid = is_valid_combination_advanced(input, target)
    print(nb_valid)


if __name__ == '__main__': 
    print('start')
    runPart1()
    runPart2()
    print('end')
