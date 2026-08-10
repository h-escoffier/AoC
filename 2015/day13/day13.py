# AoC 2015 - Day13


from itertools import permutations
from tqdm import tqdm 


def readInput(path): 
    with open(path) as f: 
        content = [line.rstrip().split(" ") for line in f.readlines()]
    return content


def formatInput(line): 
    return line[0], line[10][:-1], line[2], int(line[3])


def createAllPoss(persons): 
    allC = []
    for c in permutations(persons):
        allC.append(c)
    return allC


def calculateHappiness(possible, table): 

    bestScore = 0
    for possibility in tqdm(iterable=possible, desc='Part1'): 

        score = 0 

        # print(possibility)

        for i in range(0, len(possibility)): 

            pers1 = possibility[i]
            if i != len(possibility)-1: 
                pers2 = possibility[i+1]
            elif i == len(possibility)-1:
                pers2 = possibility[0] # cycle

            # print(pers1, pers2)
            
            # retrieve 
            for values in table: 
                if values[0] == pers1 and values[1] == pers2: 
                    
                    if values[2] == 'gain': 
                        score += values[3]
                    elif values[2] == 'lose': 
                        score -= values[3]

                elif values[1] == pers1 and values[0] == pers2: 
        
                    if values[2] == 'gain': 
                        score += values[3]
                    elif values[2] == 'lose': 
                        score -= values[3]

            # print(score)
            
        # break 
        if score >= bestScore: 
            bestScore = score 
    return bestScore


def runPart1(): 
    input = readInput("2015/data/input_day13.txt")
    # input = readInput("2015/data/input_test.txt")
    formatted = []
    participants = []
    for line in input: 
        person1, person2, change, value = formatInput(line)
        formatted.append([person1, person2, change, value])
        participants.append(person1)
    participants = list(set(participants))
    allC = createAllPoss(participants)
    bestScore = calculateHappiness(allC, formatted)
    print(bestScore)


def addMe(table, participants): 
    for participant in participants: 
        table.append([participant, 'ME', 'gain', 0])
        table.append(['ME', participant, 'gain', 0])
    participants.append('ME')
    return table, participants
    

def runPart2(): 
    input = readInput("2015/data/input_day13.txt")
    # input = readInput("2015/data/input_test.txt")
    formatted = []
    participants = []
    for line in input: 
        person1, person2, change, value = formatInput(line)
        formatted.append([person1, person2, change, value])
        participants.append(person1)
    participants = list(set(participants))
    formatted, participants = addMe(formatted, participants)
    allC = createAllPoss(participants)
    bestScore = calculateHappiness(allC, formatted)
    print(bestScore)



if __name__ == '__main__': 
    print('start')
    # runPart1()
    runPart2()
    print('end')
