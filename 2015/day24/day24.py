# AoC 2015 - Day24


from itertools import permutations, combinations
from tqdm import tqdm
from math import prod


def readInput(path): 
    with open(path) as f: 
        content = [int(line)for line in f.readlines()]
    return content


def splitThree(perm, sum_total): 
    split1, split2, split3 = [], [], []
    for elm in perm: 
        if sum(split1) < sum_total // 3: 
            split1.append(elm)
        elif sum(split1) > sum_total // 3: 
            return False, split1, split2, split3
        elif sum(split2) < sum_total // 3: 
            split2.append(elm)
        elif sum(split2) > sum_total // 3: 
            return False, split1, split2, split3
        elif sum(split3) < sum_total // 3: 
            split3.append(elm)
        elif sum(split3) > sum_total // 3: 
            return False, split1, split2, split3
    return True, split1, split2, split3


def createCombi(weights): # Too slow
    min_lenght_s1, min_quantum = 99999999999, 9999999999999
    for perm in tqdm(iterable=permutations(weights), desc='run1'): 
        condi, stock1, _, _ = splitThree(perm, sum(perm))
        if condi: 
            if len(stock1) < min_lenght_s1: 
                min_lenght_s1 = len(stock1)
                min_quantum = prod(stock1)
                print(min_quantum)
            elif len(stock1) == min_lenght_s1: 
                if prod(stock1) < min_quantum: 
                    min_quantum = prod(stock1)
                    print(min_quantum)
    return min_quantum


def lowestSum(weights, nb_split): 
    solution_found = False
    prod_min = 99999999999999999999
    limit = len(weights) // nb_split
    for i in range(limit + 1): 
        if solution_found: 
            break 
        for combi in combinations(weights, i):
            if sum(combi) == sum(weights) // nb_split: 
                solution_found = True 
                if prod(combi) <= prod_min: 
                    prod_min = prod(combi)
    return prod_min


def runPart1(path):
    weights = readInput(path)
    prod_min = lowestSum(weights, 3)
    print(prod_min)
    

def runPart2(path): 
    weights = readInput(path)
    prod_min = lowestSum(weights, 4)
    print(prod_min)


if __name__ == '__main__': 
    print('start')
    input_path = "2015/data/input_day24.txt"
    # input_path = "2015/data/input_test.txt"
    runPart1(input_path)
    runPart2(input_path)
    print('end')
