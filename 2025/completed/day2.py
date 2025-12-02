# Day2 - AoC 2025 


def read_input(path): 
    with open(path) as f: 
        content = [line.split(',') for line in f.readlines()][0]
    return content


# Part1
def identify_ranges(content): 
    pairs = []
    for pair in content: 
        lower_range = pair.split('-')[0]
        upper_range = pair.split('-')[1]
        pairs.append((lower_range, upper_range))
    return pairs


def check_range(lower, upper):
    sum_invalid = 0 
    for id in range(lower, upper + 1): 
        if check_invalid(id): 
            # print(id)
            sum_invalid += id
    return sum_invalid


def check_invalid(id): 
    id = str(id)
    if len(id) % 2 == 0: 
        middle = len(id) // 2 
        part1 = id[middle:]
        part2 = id[:middle]
        if part1 == part2: 
            return True
        return False 


def run_part1(): 
    content = read_input('2025/data/input_day2.txt')
    # content = read_input('2025/data/input_test.txt')
    pairs = identify_ranges(content)
    total_invalid = 0
    for pair in pairs: 
        lower, upper = pair
        sum_invalid = check_range(int(lower), int(upper))
        total_invalid += sum_invalid
    print(total_invalid)


# Part2
def advanced_check_range(lower, upper):
    sum_invalid = 0 
    for id in range(lower, upper + 1): 
        if advanced_check_invalid(id): 
            # print(id)
            sum_invalid += id
    return sum_invalid


def advanced_check_invalid(id): 
    id = str(id)
    for n in range(1, len(id)): 
        if len(id) % n == 0:     
            # https://stackoverflow.com/questions/22571259/split-a-string-into-n-equal-parts
            parts = [id[i:i+n] for i in range(0, len(id), n)]
            if len(list(set(parts))) == 1: 
                return True
    return False 


def run_part2(): 
    content = read_input('2025/data/input_day2.txt')
    # content = read_input('2025/data/input_test.txt')
    pairs = identify_ranges(content)
    total_invalid = 0
    for pair in pairs: 
        lower, upper = pair
        sum_invalid = advanced_check_range(int(lower), int(upper))
        total_invalid += sum_invalid
    print(total_invalid)


if __name__ == '__main__': 
    print('start')
    run_part1()
    run_part2()
    print('end')

