# AoC 2015 - Day14


from tqdm import tqdm 


def readInput(path): 
    with open(path) as f: 
        content = [line.rstrip().split(" ") for line in f.readlines()]
    return content


def formatInput(line): 
    return line[0], int(line[3]), int(line[6]), int(line[13])


def race(time, candidates, speed, duration, rest): 
    dist = [0]*len(candidates)
    counter = [0]*len(candidates)
    state = ['Run']*len(candidates)
    for _ in tqdm(iterable=range(1, time + 1), desc='Part1'):
        for i in range(0, len(candidates)): 
            if state[i] == 'Run':
                if counter[i] < duration[i]:
                    dist[i] += speed[i]
                if counter[i] == duration[i]: 
                    state[i] = 'Rest'
                    counter[i] = 0
                counter[i] += 1
            elif state[i] == 'Rest':
                if counter[i] == rest[i]: 
                    state[i] = 'Run'
                    dist[i] += speed[i]
                    counter[i] = 0
                counter[i] += 1
    # print(dist)
    return max(dist)


def runPart1(): 
    input = readInput("2015/data/input_day14.txt")
    # input = readInput("2015/data/input_test.txt")
    candidates, speed, duration, rest = [], [], [], []
    for line in input: 
        c, s, d, r = formatInput(line)
        candidates.append(c)
        speed.append(s)
        duration.append(d)
        rest.append(r)
    maxDist = race(2503, candidates, speed, duration, rest)
    print(maxDist)
    # 1120 Too low
    

def secondRace(time, candidates, speed, duration, rest): 
    dist = [0]*len(candidates)
    counter = [0]*len(candidates)
    points = [0]*len(candidates)
    state = ['Run']*len(candidates)
    for _ in tqdm(iterable=range(1, time + 1), desc='Part1'):
        for i in range(0, len(candidates)): 
            if state[i] == 'Run':
                if counter[i] < duration[i]:
                    dist[i] += speed[i]
                if counter[i] == duration[i]: 
                    state[i] = 'Rest'
                    counter[i] = 0
                counter[i] += 1
            elif state[i] == 'Rest':
                if counter[i] == rest[i]: 
                    state[i] = 'Run'
                    dist[i] += speed[i]
                    counter[i] = 0
                counter[i] += 1

        maxDist = max(dist)
        for i in range(0, len(dist)):
            if dist[i] == maxDist:  
                points[i] += 1
    # print(dist)
    return max(points)


def runPart2(): 
    input = readInput("2015/data/input_day14.txt")
    candidates, speed, duration, rest = [], [], [], []
    for line in input: 
        c, s, d, r = formatInput(line)
        candidates.append(c)
        speed.append(s)
        duration.append(d)
        rest.append(r)
    maxPoints = secondRace(2503, candidates, speed, duration, rest)
    print(maxPoints)


if __name__ == '__main__': 
    print('start')
    runPart1()
    runPart2()
    print('end')
