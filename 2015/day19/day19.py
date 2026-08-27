# AoC 2015 - Day19

import re
import functools  # for memoization

def readInput(path): 
    with open(path) as f: 
        content = [line.rstrip().split(" ") for line in f.readlines()]
    return content

def formatRules(rules): 
    new_rules = []
    for line in rules:
        x, _, y = line
        new_rules.append((x, y))
    return new_rules


def createNewString(input_string, rules): 
    new_strings = []
    for rule in rules: 
        old, new = rule 
        pattern = re.compile(old)
        r = pattern.search(input_string)
        all_pos = []
        while r:
            start, end = r.start(), r.end() - 1
            r = pattern.search(input_string,r.start() + 1)
            all_pos.append((start, end))
        for pos in all_pos: 
            s, e = pos
            new_string = ""
            for i in range(len(input_string)): 
                if s == i: 
                    new_string += new
                elif i >= s and i <= e: 
                    continue
                else: 
                    new_string += input_string[i]
            new_strings.append(new_string)
    return new_strings


def runPart1(): 
    input = readInput("2015/data/input_day19.txt")
    # input = readInput("2015/data/input_test.txt")
    rules = input[:-2]
    input_string = input[-1][0]
    rules = formatRules(rules)
    new_strings = createNewString(input_string, rules)
    print(len(list(set(new_strings))))


# @functools.cache
# def createRecursiveMolecules(mol, rules, all_mols, all_steps, target, steps):
#     steps += 1 
#     all_mols = createNewString(mol, rules) 
#     uq_mols = tuple(list(set(all_mols)))
#     for new_mol in uq_mols: 
#         # print(mol, "->", new_mol)
#         print(len(new_mol))
#         if new_mol == target:
#             all_steps += (steps,)
#             return steps
#         elif len(new_mol) >= len(target): 
#             pass
#         else:
#             all_steps = createRecursiveMolecules(new_mol, rules, tuple(all_mols), all_steps, target, steps)
#     return all_steps


def createOldString(input_string, rules): 
    new_strings = []
    for rule in rules: 
        old, new = rule 
        pattern = re.compile(new)
        r = pattern.search(input_string)
        all_pos = []
        while r:
            start, end = r.start(), r.end() - 1
            r = pattern.search(input_string,r.start() + 1)
            all_pos.append((start, end))
        for pos in all_pos: 
            s, e = pos
            new_string = ""
            for i in range(len(input_string)): 
                if s == i: 
                    new_string += old
                elif i >= s and i <= e: 
                    continue
                else: 
                    new_string += input_string[i]
            new_strings.append(new_string)
    return new_strings


# @functools.cache
def createOppositeRecursiveMolecules(mol, rules, all_mols, all_steps, target, steps):
    steps += 1 
    all_mols = createOldString(mol, rules) 
    uq_mols = tuple(list(sorted(set(all_mols))))
    for new_mol in uq_mols: 
        # print(mol, "->", new_mol)
        # print(len(mol))
        if 'e' in new_mol and len(new_mol) > 1: 
            continue
        if new_mol == target:
            all_steps += (steps,)
            print(steps)
            # return steps
        elif len(new_mol) < len(target): 
            continue
        else: 
            all_steps = createOppositeRecursiveMolecules(new_mol, rules, tuple(all_mols), all_steps, target, steps)
    return all_steps


# def runPart2(): 
#     input = readInput("2015/data/input_day19.txt")
#     # input = readInput("2015/data/input_test.txt")
#     rules = input[:-2]
#     input_string = input[-1][0]
#     rules = formatRules(rules)
#     molecule = "e"
#     all_steps = createRecursiveMolecules(molecule, tuple(rules), (), (), input_string, 0)
#     print(min(all_steps))


# def runPart2(): 
#     input = readInput("2015/data/input_day19.txt")
#     # input = readInput("2015/data/input_test.txt")
#     rules = input[:-2]
#     input_string = input[-1][0]
#     rules = formatRules(rules)
#     # molecule = "e"
#     value = createOppositeRecursiveMolecules(input_string, tuple(rules), (), (), 'e', 0)
#     print(value)


from collections import deque

def solve_part2(molecule, rules):

    queue = deque([(molecule, 0)])
    visited = {molecule}

    while queue:

        mol, steps = queue.popleft()

        if mol == 'e':
            return steps

        for new_mol in set(createOldString(mol, rules)):

            if new_mol in visited:
                continue

            if 'e' in new_mol and new_mol != 'e':
                continue

            visited.add(new_mol)
            queue.append((new_mol, steps + 1))


def runPart2():

    input = readInput("2015/data/input_day19.txt")

    rules = input[:-2]
    input_string = input[-1][0]

    rules = formatRules(rules)

    result = solve_part2(input_string, tuple(rules))

    print(result)


if __name__ == '__main__': 
    print('start')
    # runPart1()
    runPart2()
    print('end')
