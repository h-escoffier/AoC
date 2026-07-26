# AoC 2015 - Day6


import numpy as np 


def readInput(path): 
    with open(path) as f: 
        content = [line.rstrip().split(" ") for line in f.readlines()]
    return content


# 123 -> x
# 456 -> y
# x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i

def readInstruction(line): 
    if len(line) == 3: # 19138 -> b 
        return 'ASSIGN', line[0], line[2]
    elif len(line) == 4: # NOT go -> gp
        return 'NOT', line[1], line[3]
    elif len(line) == 5: 
        return line[1], (line[0], line[2]), line[4]


def applyInstruction(gates, ope, inGate, outGate): 
    if ope == 'ASSIGN':
        if inGate.isdigit(): 
            inGate = int(inGate)
        else: 
            if inGate not in gates: 
                return gates, False
            inGate = gates[inGate] 
        gates.update({outGate: int(inGate)})
        return gates, True

    if ope == 'NOT': 
        if inGate not in gates: 
            return gates, False
        value = gates[inGate]
        value = np.uint16(value)
        gates.update({outGate: int(~value)})
        return gates, True

    # SetUp
    x, y = inGate
    if x.isdigit(): 
        valueX = int(x)
    else: 
        if x not in gates: 
            return gates, False
        valueX = gates[x] 
            
    if y.isdigit(): 
        valueY = int(y)
    else: 
        if y not in gates: 
            return gates, False
        valueY = gates[y] 

    if ope == 'AND': 
        gates.update({outGate: valueX & valueY})
        return gates, True
    
    if ope == 'OR': 
        gates.update({outGate: valueX | valueY})
        return gates, True

    if ope == 'LSHIFT': 
        gates.update({outGate: valueX << valueY})
        return gates, True

    if ope == 'RSHIFT': 
        gates.update({outGate: valueX >> valueY})
        return gates, True
    

def runPart1(): 
    lines = readInput('2015/data/input_day7.txt')
    gates = {}
    allProcess = False
    while not allProcess: 
        remainingLines = []
        for line in lines: 
            ope, inGate, outGate = readInstruction(line)
            gates, finsih = applyInstruction(gates, ope, inGate, outGate)
            if not finsih:
                remainingLines.append(line) 
        if len(remainingLines) == 0: 
            allProcess = True
        lines = remainingLines
    print(gates['a'])
    return gates['a']


def runPart2(): 
    lines = readInput('2015/data/input_day7.txt')
    gates = {'b': runPart1()} # c.f. part1
    allProcess = False
    while not allProcess: 
        remainingLines = []
        for line in lines: 
            ope, inGate, outGate = readInstruction(line)
            if ope == 'ASSIGN' and outGate == 'b': 
                continue
            gates, finsih = applyInstruction(gates, ope, inGate, outGate)
            if not finsih:
                remainingLines.append(line) 
        if len(remainingLines) == 0: 
            allProcess = True
        lines = remainingLines
    print(gates['a'])


if __name__ == '__main__': 
    print('start')
    # runPart1()
    runPart2()
    print('end')