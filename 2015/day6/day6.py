# AoC 2015 - Day6


def readInput(path): 
    with open(path) as f: 
        content = [line.rstrip().split(" ") for line in f.readlines()]
    return content


def createGrid(size): 
    grid = []
    for _ in range(0, size): 
        line = []
        for _ in range(0, size): 
            line.append(-1)
        grid.append(line)
    return grid 


def readInstruction(line): 
    if len(line) == 5: 
        type = line[1] # On/Off
        start = line[2].split(',')
        end = line[4].split(',')
    else:
        type = line[0]
        start = line[1].split(',')
        end = line[3].split(',')
    start = (int(start[0]), int(start[1]))
    end = (int(end[0]), int(end[1]))
    return type, start, end


def toChange(type, value): 
    if type == 'toggle': 
        return value * -1
    elif type == 'on': 
        return 1
    elif type == 'off': 
        return -1


def applyInstruction(grid, type, start, end): 
    xStart,yStart = start
    xEnd, yEnd = end
    for i in range(xStart, xEnd + 1): 
        for j in range(yStart, yEnd + 1):
            grid[i][j] = toChange(type, grid[i][j])
    # print(grid)
    return grid 


def lightOn(grid): 
    count = 0 
    for row in grid: 
        for elm in row: 
            if elm == 1: 
                count += 1
    return count 


def runPart1(): 
    lines = readInput('2015/data/input_day6.txt')
    grid = createGrid(1000)
    for line in lines: 
        type, start, end = readInstruction(line)
        grid = applyInstruction(grid, type, start, end)
    print(lightOn(grid))


def createNewGrid(size): 
    grid = []
    for _ in range(0, size): 
        line = []
        for _ in range(0, size): 
            line.append(0)
        grid.append(line)
    return grid 


def newToChange(type, value): 
    if type == 'toggle': 
        return value + 2
    elif type == 'on': 
        return value + 1
    elif type == 'off': 
        if value == 0: 
            return value 
        else: 
            return value - 1


def applyNewInstruction(grid, type, start, end): 
    xStart,yStart = start
    xEnd, yEnd = end
    for i in range(xStart, xEnd + 1): 
        for j in range(yStart, yEnd + 1):
            grid[i][j] = newToChange(type, grid[i][j])
    # print(grid)
    return grid 


def brightness(grid): 
    count = 0 
    for row in grid: 
        for elm in row: 
            count += elm
    return count 


def runPart2(): 
    lines = readInput('2015/data/input_day6.txt')
    grid = createNewGrid(1000)
    for line in lines: 
        type, start, end = readInstruction(line)
        grid = applyNewInstruction(grid, type, start, end)
    print(brightness(grid))


if __name__ == '__main__': 
    print('start')
    runPart1()
    runPart2()
    print('end')