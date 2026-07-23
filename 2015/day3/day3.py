# Day3 - AoC 2015


def read_input(path): 
    with open(path) as f: 
        content = f.readline()
    return content


def coordinates(previous, move):
    x, y = previous
    if move == '^': 
        return (x, y + 1)
    if move == 'v': 
        return (x, y - 1)
    if move == '>': 
        return (x + 1, y)
    if move == '<': 
        return (x - 1, y)
    

def run_part1(): 
    content = read_input('2015/data/input_day3.txt')
    nb_house = 1
    visited = [(0, 0)]
    position = (0, 0)
    for move in content: 
        # print(move)
        # print(position)
        position = coordinates(position, move)
        if position not in visited:
            visited.append(position)
            nb_house += 1 
    print(nb_house)


def run_part2(): 
    content = read_input('2015/data/input_day3.txt')
    nb_house = 1
    visited = [(0, 0)]
    position_santa = (0, 0)
    position_robot = (0, 0)
    for i in range(0, len(content) - 1, 2):
        position_santa = coordinates(position_santa, content[i])
        position_robot = coordinates(position_robot, content[i + 1])
        if position_santa not in visited:
            visited.append(position_santa)
            nb_house += 1 
        if position_robot not in visited: 
            visited.append(position_robot)
            nb_house += 1 
    print(nb_house)


if __name__ == '__main__': 
    print('start')
    run_part1()
    run_part2()
    print('end')