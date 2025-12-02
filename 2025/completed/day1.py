# Day1 - AoC 2025 


from statistics import mode


def read_input(path): 
    with open(path) as f: 
        content = [line.strip() for line in f.readlines()]
    return content


# Part1
def main(content, position): 
    positions = [position]
    for elm in content: 
        if elm[0] == 'L': 
            position = (position - int(elm[1:])) % 100
            positions.append(position)
        else: 
            position = (position + int(elm[1:])) % 100
            positions.append(position)
    return positions


def count_mode(positions):
    counter = 0  
    lst_mode = mode(positions)
    for elm in positions: 
        if elm == lst_mode: 
            counter +=1
    return counter

def run_part1(): 
    content = read_input('2025/data/input_day1.txt')
    # content = read_input('2025/data/input_test.txt')
    start_position = 50 
    positions = main(content, start_position)
    counter = count_mode(positions)
    print(counter)
    

# Part2
def main2(content, position): # Work on the example but not on the real data
    counter = 0 
    for elm in content: 
        if elm[0] == 'L': 
            quotient = (position - int(elm[1:])) // 100
            if (position == 0 and quotient != 0) or ((position - int(elm[1:])) % 100 == 0 and quotient != 0):
                quotient = abs(quotient) 
                quotient -= 1
            counter += abs(quotient)
            print(elm[0], position, int(elm[1:]), quotient, (position - int(elm[1:])) % 100)
            position = (position - int(elm[1:])) % 100
            if position == 0: 
                counter +=1
        else: 
            quotient = (position + int(elm[1:])) // 100
            if (position == 0 and quotient != 0) or ((position + int(elm[1:])) % 100 == 0 and quotient != 0):
                quotient = abs(quotient) 
                quotient -= 1
            counter += abs(quotient) 
            print(elm[0], position, int(elm[1:]), quotient, (position + int(elm[1:])) % 100)
            position = (position + int(elm[1:])) % 100
            if position == 0: 
                # print('here')
                counter +=1
        # print(counter)
    return counter


def brute_force(content, start_position):    
    """
    Thanks to Vanille Lejal for the idea. 
    """
    total_counter = 0  
    position = start_position
    for elm in content: 
        number = int(elm[1:])
        direction = elm[0]
        position, counter = move(position, direction, number)
        total_counter += counter
    return total_counter 


def move(position, direction, number): 
    counter = 0 
    for _ in range(number): 
        if direction == 'L': 
            position -= 1 
        else: 
            position += 1 
        if position == -1: 
            position = 99 
        elif position == 100: 
            position = 0 
        if position == 0: 
            counter +=1
    return position, counter


def run_part2(): 
    content = read_input('2025/data/input_day1.txt')
    # content = read_input('2025/data/input_test.txt')
    start_position = 50 
    counter = brute_force(content, start_position)
    print(counter)


if __name__ == '__main__': 
    print('start')
    run_part1()
    run_part2()
    print('end')


# 5968 Too low
# 6195 Too high 
# 6459 Too high 
