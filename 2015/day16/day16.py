# AoC 2015 - Day16


from tqdm import tqdm 


def readInput(path): 
    with open(path) as f: 
        content = [line.rstrip().split(" ") for line in f.readlines()]
    return content


def formatInput(line): 
    sue = int(line[1][:-1])
    elm1 = (line[2][:-1], int(line[3][:-1]))
    elm2 = (line[4][:-1], int(line[5][:-1]))
    elm3 = (line[6][:-1], int(line[7]))
    return sue, [elm1, elm2, elm3]


def wrappingContent(): 
    return {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
        }


def runPart1(): 
    input = readInput("2015/data/input_day16.txt")
    allContent = []
    for line in input: 
        sue, content = formatInput(line)
        allContent.append(content)
    tickerTape = wrappingContent()
    for i in range(0, len(allContent)): 
        potential = True
        for k, v in tickerTape.items(): 
            for elm in allContent[i]: 
                # print(elm)
                k_c, v_c = elm 
                if k_c == k and v_c != v: 
                    potential = False 
        if potential: 
            print(i + 1)


def runPart2(): 
    input = readInput("2015/data/input_day16.txt")
    allContent = []
    for line in input: 
        sue, content = formatInput(line)
        allContent.append(content)
    tickerTape = wrappingContent()
    for i in range(0, len(allContent)): 
        potential = True
        for k, v in tickerTape.items(): 
            for elm in allContent[i]: 
                # print(elm)
                k_c, v_c = elm 
                if k_c == k:
                    if k_c == 'cats' or k_c =='trees':
                        if v_c <= v: 
                            potential = False 
                    elif k_c == 'pomeranians' or k_c =='goldfish': 
                        if v_c >= v:  
                            potential = False 
                    elif v_c != v: 
                        potential = False

        if potential: 
            print(i + 1)


if __name__ == '__main__': 
    print('start')
    # runPart1()
    runPart2()
    print('end')
