# AoC 2015 - Day11


ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def runPart1(): 
    password = "cqjxjnds"
    notSatisfy = True
    while notSatisfy:
        password = incrementString(password)
        if not conditionOne(password): 
            continue
        if not conditionTwo(password): 
            continue
        if conditionThree(password): 
            notSatisfy = False
    print(password)
    return password


def incrementString(password): 
    newPassword = ""
    nextLetter = True
    for letter in reversed(password):
        if nextLetter: 
            newLetter = incrementLetter(letter)
            increment = True
        else: 
            newLetter = letter
            increment = False        
        nextLetter = False
        if newLetter == 'a' and increment:
            nextLetter = True
        newPassword += newLetter
    return newPassword[::-1]


def incrementLetter(letter):
    return ALPHABET[(ALPHABET.index(letter) + 1) % 26]


def conditionOne(password): 
    idx = []
    i = 0 
    for letter in password: 
        idx.append(ALPHABET.index(letter)) 
        if len(idx) >= 3: 
            first = idx[i - 2]
            second = idx[i - 1]
            third = idx[i]
            if first + 1 == second: 
                if second + 1 == third: 
                    return True
        i += 1 
    return False


def conditionTwo(password): 
    forbiddenLetters = ['i', 'o', 'l']
    for f in forbiddenLetters: 
        if f in password: 
            return False
    return True 


def conditionThree(password): 
    counter = 0 
    idx, fIdx = [], []
    i = 0 
    for letter in password: 
        idx.append(ALPHABET.index(letter)) 
        if len(idx) >= 2: 
            first = idx[i-1]
            second = idx[i]
            if first == second and i-1 not in fIdx: 
                counter += 1
                fIdx = [i-1, i]
            if counter == 2: 
                return True
        i += 1 
    return False


def runPart2():
    password = runPart1()
    notSatisfy = True
    while notSatisfy:
        password = incrementString(password)
        if not conditionOne(password): 
            continue
        if not conditionTwo(password): 
            continue
        if conditionThree(password): 
            notSatisfy = False
            # pass
    print(password)


if __name__ == '__main__': 
    print('start')
    # runPart1()
    runPart2()
    print('end')