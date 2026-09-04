# AoC 2015 - Day25


def convertValue(row, col): 
    find_row, find_col = False,  False
    i = 1
    nb_row, nb_col = 1, 1
    start_nb_row = 1  
    while not find_row and not find_col: 
        while nb_row >= 1: 
            if nb_row == row and nb_col == col: 
                return i
            i += 1
            nb_row -= 1 
            nb_col += 1
        start_nb_row += 1
        nb_row = start_nb_row
        nb_col = 1


def generateValue(nb): 
    start = 20151125
    for _ in range(2, nb + 1): 
        start *= 252533
        start = start % 33554393
    return start
        

def runPart1():
    # input: row 2978, column 3083
    nb_value = convertValue(2978, 3083)
    value = generateValue(nb_value)
    print(value)


# 17370278 too high 


if __name__ == '__main__': 
    print('start')
    runPart1()
    print('end')
