# AoC 2015 - Day15


from tqdm import tqdm 


def readInput(path): 
    with open(path) as f: 
        content = [line.rstrip().split(" ") for line in f.readlines()]
    return content


def formatInput(line): 
    return line[0][:-1], int(line[2][:-1]), int(line[4][:-1]), int(line[6][:-1]), int(line[8][:-1]), int(line[10])


def findSum(n, total, seq=()):
    # Adapted from https://stackoverflow.com/questions/67646991/generate-combinations-such-that-the-total-is-always-100-and-uses-a-defined-jump
    if n == 0:
        if total == 0: yield seq
        return
    for i in range(1, total+1):
        yield from findSum(n - 1, total - i, seq + (i,))


def runPart1(): 
    input = readInput("2015/data/input_day15.txt")
    # input = readInput("2015/data/input_test.txt")
    capacities, durabilities, flavors, textures = [], [], [], []
    for line in input: 
        _, capacity, durability, flavor, texture, _ = formatInput(line)
        capacities.append(capacity)
        durabilities.append(durability)
        flavors.append(flavor)
        textures.append(texture)
        properties = [capacities, durabilities, flavors, textures]

    maxSum = -1 
    # for seq in findSum(2, 100, 1):
    for seq in tqdm(iterable=findSum(4, 100), desc='Part1'):
        # print(seq)
        # a, b = seq
        a, b, c, d = seq
        sumTot = 1 
        for property in properties: 
            # sumProp = a*property[0] + b*property[1] 
            sumProp = a*property[0] + b*property[1] + c*property[2] + d*property[3]
            if sumProp <= 0: 
                sumProp = 0  
            sumTot *= sumProp
        if sumTot >= maxSum:
            maxSum = sumTot
    print(maxSum)

        
def caloriesControl(seq, calories): 
    a, b, c, d = seq 
    if a*calories[0] + b*calories[1] + c*calories[2] + d*calories[3] == 500: 
        return True 
    return False


def runPart2(): 
    input = readInput("2015/data/input_day15.txt")
    # input = readInput("2015/data/input_test.txt")
    capacities, durabilities, flavors, textures, calories = [], [], [], [], []
    for line in input: 
        _, capacity, durability, flavor, texture, calorie = formatInput(line)
        capacities.append(capacity)
        durabilities.append(durability)
        flavors.append(flavor)
        textures.append(texture)
        calories.append(calorie)
        properties = [capacities, durabilities, flavors, textures]

    maxSum = -1 
    # for seq in findSum(2, 100, 1):
    for seq in tqdm(iterable=findSum(4, 100), desc='Part2'):
        # print(seq)
        # a, b = seq
        a, b, c, d = seq
        sumTot = 1 
        if not caloriesControl(seq, calories): 
            continue
        for property in properties: 
            # sumProp = a*property[0] + b*property[1] 
            sumProp = a*property[0] + b*property[1] + c*property[2] + d*property[3]
            if sumProp <= 0: 
                sumProp = 0  
            sumTot *= sumProp
        if sumTot >= maxSum:
            maxSum = sumTot
    print(maxSum)


if __name__ == '__main__': 
    print('start')
    # runPart1()
    runPart2()
    print('end')
