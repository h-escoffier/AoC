# AoC 2015 - Day18


from tqdm import tqdm 
from itertools import combinations


def readInput(path): 
    with open(path, "r") as file:
        lines = file.readlines()
    content = []
    for line in lines:
        line = line.strip()
        content.append(list(line))
    return content


def printGrid(grid): 
    for line in grid: 
        print(line, '\n')


def identifyNeighbours(pos, grid): 
    neighs = []
    i, j = pos
    # top 
    if j > 0:
        top = grid[j - 1][i]
        neighs.append(top)
    # bottom 
    if j != len(grid) - 1: 
        bottom = grid[j + 1][i]
        neighs.append(bottom)
    # left 
    if i > 0: 
        left = grid[j][i - 1]
        neighs.append(left)
    # right 
    if i != len(grid) - 1: 
        right = grid[j][i + 1]
        neighs.append(right)
    # diag 
    if j > 0 and i > 0:
        diag_top_left = grid[j - 1][i - 1]
        neighs.append(diag_top_left)
    if j != len(grid) - 1 and i > 0:
        diag_bottom_left = grid[j + 1][i - 1]
        neighs.append(diag_bottom_left)
    if j > 0 and i != len(grid) - 1:
        diag_top_right = grid[j - 1][i + 1]
        neighs.append(diag_top_right)
    if j != len(grid) - 1 and i != len(grid) - 1:
        diag_bottom_right = grid[j + 1][i + 1]
        neighs.append(diag_bottom_right)
    return neighs


def modify(pos, neighs, grid): 
    i, j = pos
    value = grid[j][i]
    if value == '#': # on 
        count = 0 
        for neig in neighs: 
            if neig == '#': 
                count += 1 
        if count == 2 or count == 3: 
            return '#'
        return '.'
    elif value == '.': # off
        count = 0 
        for neig in neighs: 
            if neig == '#': 
                count += 1 
        if count == 3: 
            return '#'
        return '.'

def countOn(grid): 
    count = 0
    for line in grid: 
        for elm in line: 
            if elm == '#': 
                count += 1
    return count


def runPart1(): 
    grid = readInput("2015/data/input_day18.txt")
    # grid = readInput("2015/data/input_test.txt")
    for i in range(100): 
        new_grid = []
        for j in range(len(grid)): 
            new_line = []
            for i in range(len(grid[0])):
                pos = (i, j)
                neighs = identifyNeighbours(pos, grid) 
                new_value = modify(pos, neighs, grid)
                new_line.append(new_value)
            new_grid.append(new_line)
        grid = new_grid
    print(countOn(grid))
    # printGrid(grid)


def runPart2(): 
    grid = readInput("2015/data/input_day18.txt")
    # grid = readInput("2015/data/input_test.txt")
    exceptions = [(0, 0), (0, len(grid) - 1), (len(grid) - 1, 0), (len(grid) - 1, len(grid) - 1)]
    # modify inital state
    new_grid = []
    for j in range(len(grid)): 
        new_line = []
        for i in range(len(grid[0])): 
            pos = (i, j)
            if pos not in exceptions: 
                new_line.append(grid[j][i])
            else: 
                new_line.append('#')
        new_grid.append(new_line)
    grid = new_grid
    # run
    for i in range(100): 
    # for i in range(5): 
        new_grid = []
        for j in range(len(grid)): 
            new_line = []
            for i in range(len(grid[0])):
                pos = (i, j)
                neighs = identifyNeighbours(pos, grid) 
                if pos not in exceptions: 
                    new_value = modify(pos, neighs, grid)
                else: 
                    new_value = '#'
                new_line.append(new_value)
            new_grid.append(new_line)
        grid = new_grid
    print(countOn(grid))


if __name__ == '__main__': 
    print('start')
    runPart1()
    runPart2()
    print('end')
