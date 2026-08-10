# AoC 2015 - Day12


from tqdm import tqdm 
import json
import re


def readInput(path): 
    with open(path) as f: 
        content = f.readlines()
    return content


def readJson(path): 
    with open(path) as f: 
        content = json.load(f)
    return content


def runPart1(): 
    input = readInput("2015/data/input_day12.txt")
    match_all = re.findall(r'[0-9]+', input[0])
    match_negative = re.findall(r'\-[0-9]*', input[0])
    sum = 0 
    for number in match_all: 
        sum += int(number)
    for number in match_negative: 
        sum += int(number)*2
    print(sum)
    # 259908 Too high
    # 119433
    

def recursive(output): 
    # output 
    if isinstance(output, dict): 
        for _, v in output.items(): 
            print(v)
            recursive(v)
    else:
        pass


def detectRed(currentString): 
    newString = ""
    i = 0 
    for letter in currentString: 
        newString += letter
        if len(newString) >= 3: 
            first = newString[i - 2]
            second = newString[i - 1]
            third = newString[i]
            if first == 'r' and second == 'e' and third == 'd': 
                return True
        i += 1 
    return False


def identifyNumbers(currentString): 
    sum = 0 
    match_all = re.findall(r'[0-9]+', currentString)
    match_negative = re.findall(r'\-[0-9]*', currentString)
    for number in match_all: 
        sum += int(number)
    for number in match_negative: 
        sum += int(number)*2
    return sum 


def runTest(): 
    input = readJson("2015/data/input_day12.txt")
    recursive(input)


# def runPart2(): 
#     # input = readInput("2015/data/input_day12.txt")
#     input = readInput("2015/data/input_test.txt")
#     currentString = ""
#     nbOpen, nbClose = 0, 0 
#     totalSum = 0 
#     isRed = False
#     for character in input[0]: 
#         currentString += character
#         if character == '}':
#             nbClose += 1 
#             if nbOpen == nbClose: 
#                 isRed = detectRed(currentString) 
#                 # print(isRed)
#                 if not isRed: 
#                     totalSum += identifyNumbers(currentString)
#                     # print(currentString)
#                 # reset
#                 nbOpen = 0
#                 nbClose = 0 
#                 currentString = ""
#                 isRed = False
#         if character == '{': 
#             if nbOpen == 0: 
#                 totalSum += identifyNumbers(currentString)
#                 # print(currentString)
#                 currentString = ""
#                 isRed = False
#             nbOpen += 1
#             # totalSum += identifyNumbers(currentString)
#             # print(currentString)
#             # currentString = ""
#             # isRed = False
#     if not isRed: 
#         # print(currentString)
#         totalSum += identifyNumbers(currentString)
#     print(totalSum)
#     # 88462 Too high
      # 91945


def parseText(input, start, direction): 
    counter_bracket, counter_square = 0, 0
    idx = start 
    idx_square, idx_bracket = -1, -1
    square_found, bracket_found = False, False
    if direction == "forward": 
        for character in input[start:]:
            if character == '{':
                counter_bracket += 1
            elif character == '[': 
                counter_square += 1
            elif character == '}': 
                if bracket_found: 
                    continue
                if counter_bracket > 0: 
                    counter_bracket -= 1
                elif counter_bracket == 0: 
                    idx_bracket = idx
                    bracket_found = True 
                    
            elif character == ']':  
                if square_found: 
                    continue
                if counter_square > 0: 
                    counter_square -= 1
                elif counter_square == 0: 
                    idx_square = idx
                    square_found = True 

            if idx_bracket != -1 and idx_square != -1: 
                return idx_bracket, idx_square
            idx += 1
        return idx_bracket, idx_square # fallback
    
    elif direction == "reverse": 
        for character in reversed(input[:start]): 
            if character == '}':
                counter_bracket += 1
            elif character == ']': 
                counter_square += 1
            elif character == '{': 
                if bracket_found: 
                    continue
                elif counter_bracket > 0: 
                    counter_bracket -= 1
                elif counter_bracket == 0: 
                    idx_bracket = idx
                    bracket_found = True 

            elif character == '[':  
                if square_found: 
                    continue 
                elif counter_square > 0: 
                    counter_square -= 1
                elif counter_square == 0: 
                    idx_square = idx
                    square_found = True 

            if idx_bracket != -1 and idx_square != -1: 
                return idx_bracket, idx_square
            idx -= 1
        return idx_bracket, idx_square # fallback


def runPart2(): 
    input = readInput("2015/data/input_day12.txt")
    # input = readInput("2015/data/input_test.txt")
    stringInput = input[0]
    currentString = ''
    i = 0 
    forbidden = []
    for character in tqdm(iterable=stringInput, desc='Process Part2'): 
        currentString += character
        isRed = detectRed(currentString)
        if isRed: 
            # parse forward / backward
            idx_bracket_after, idx_square_after = parseText(stringInput, i+1, "forward")
            idx_bracket_before, idx_square_before = parseText(stringInput, i+1, "reverse")

            # print(idx_bracket_before, idx_bracket_after, stringInput[idx_bracket_before : idx_bracket_after])
            # print(idx_square_before, idx_square_after, stringInput[idx_square_before : idx_square_after])

            if idx_bracket_before == -1 or idx_bracket_after == -1: 
                bracket_interval = 99999 
            else: 
                bracket_interval = idx_bracket_after - idx_bracket_before

            if idx_square_before == -1 or idx_square_after == -1: 
                square_interval = 99999
            else: 
                square_interval = idx_square_after - idx_square_before
            
            if bracket_interval <= square_interval: 
                forbidden.append((idx_bracket_before, idx_bracket_after))

            # reset 
            currentString = ''
            isRed = False
        i += 1

    # generate forbidden idx
    forbidden_idx = []
    for inter in forbidden: 
        start, end = inter
        for i in range(start, end): 
            forbidden_idx.append(i)

    # generate output without forbidden intervals
    finalString = ''
    for i in range(0, len(stringInput)): 
        if i not in forbidden_idx: 
            finalString += stringInput[i]

    # sum 
    match_all = re.findall(r'[0-9]+', finalString)
    match_negative = re.findall(r'\-[0-9]*', finalString)
    sum = 0 
    for number in match_all: 
        sum += int(number)
    for number in match_negative: 
        sum += int(number)*2

    print('sum:', sum)



if __name__ == '__main__': 
    print('start')
    # runTest()
    runPart1()
    runPart2()
    print('end')
