# AoC 2015 - Day8


def readInput(path): 
    with open(path) as f: 
        content = [line.rstrip().split(" ") for line in f.readlines()]
    return content


def runPart1(): 
    # lines = readInput('2015/data/input_day8.txt')
    lines = readInput('2015/data/input_test.txt')
    sumTotal = 0 
    sumString = 0 
    for line in lines: 
        print('int:', line[0], len(line[0]))
        print('out:', eval(line[0]), len(eval(line[0])))
        sumTotal += len(line[0])
        sumString += len(eval(line[0]))
    print(sumTotal - sumString)
    

def modifyLine(line):
    new_line = ''
    idx = 0
    for letter in line: 
        if letter == '"': 
            new_line += r'\"'
        elif letter == "\\": 
            new_line += r'\\'
        else: 
            new_line += letter 
        idx += 1 
    return new_line


def runPart2(): 
    lines = readInput('2015/data/input_day8.txt')
    sumTotal = 0 
    sumModify = 0 
    for line in lines: 
        sumTotal += len(line[0])
        line = modifyLine(line[0])
        sumModify += len(line) + 2 
    print(sumModify - sumTotal)


if __name__ == '__main__': 
    print('start')
    runPart1()
    # runPart2()
    print('end')