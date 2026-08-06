# AoC 2015 - Day10


from tqdm import tqdm 
from itertools import groupby


def runPart1(): 
    input = "1321131112"
    # input = "21"
    for i in tqdm(range(0, 40)): 
    # for i in tqdm(range(0, 50)): 
        # dict = {}
        counter = 1 
        new_input = ""
        for i in range(0, len(input) - 1): 
            if input[i] == input[i+1]: 
                counter += 1
            else: 
                new_input = new_input + str(counter) + str(input[i])
                counter = 1 
        new_input = new_input + str(counter) + str(input[i + 1])
        counter = 1 
        input = new_input
        new_input = ""
    # print(input)
    print(len(input))


def runPart2():
    input = "1321131112"
    for _ in tqdm(range(0, 50)): # RLE
        output = ''
        for char, group in groupby(input):
            count = len(list(group)) 
            output += f"{count}{char}"
        input = output
    print(len(input))


if __name__ == '__main__': 
    print('start')
    # runPart1()
    runPart2()
    print('end')