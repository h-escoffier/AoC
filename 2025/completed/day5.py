# Day5 - AoC 2025 


def read_input(path): 
    with open(path) as f: 
        content = [line.strip() for line in f.readlines()]
    id_ranges, avail = [], []
    is_break = False
    for elm in content: 
        if elm == '': 
            is_break = True
            continue
        if is_break: 
            avail.append(int(elm))
        else: 
            lower_range = elm.split('-')[0]
            upper_range = elm.split('-')[1]
            id_ranges.append((int(lower_range), int(upper_range)))
    return id_ranges, avail


# Part1
def is_in(id, id_ranges): 
    for lower_range, upper_range in id_ranges: 
        if lower_range <= id <= upper_range:    
            return True
    return False
        

def run_part1():
    id_ranges, avail = read_input('2025/data/input_day5.txt')
    # id_ranges, avail = read_input('2025/data/input_test.txt')
    counter = 0 
    for id in avail: 
        pres = is_in(id, id_ranges)
        if pres: 
            counter += 1 
    print(counter)


# Part2 
def sort_id_ranges(id_ranges): 
    lower_only, sort_id_ranges = [], []
    for lower, _ in id_ranges: 
        lower_only.append(lower)
    lower_only.sort()
    for value in lower_only: 
        for lower, upper in id_ranges: 
            if lower == value: 
                sort_id_ranges.append((lower, upper))
    return sort_id_ranges
        

def merge_ranges(id_ranges): 
    new_id_ranges = []
    for i in range(len(id_ranges) - 1): 
        lower1, upper1 = id_ranges[i]
        lower2, upper2 = id_ranges[i + 1]
        if upper1 >= lower2 and upper1 <= upper2: 
            new_id_ranges.append((lower1, upper2)) 
            before = id_ranges[:i]
            after = id_ranges[i+2:]
            new_id_ranges = before + [(lower1, upper2)] + after
            return new_id_ranges, False
        elif upper1 >= upper2: 
            new_id_ranges.append((lower1, upper1))
            before = id_ranges[:i]
            after = id_ranges[i+2:]
            new_id_ranges = before + [(lower1, upper1)] + after
            return new_id_ranges, False
    return id_ranges, True 
        

def calcul_in_range(lower, upper): 
    return upper - lower + 1 


def run_part2(): 
    id_ranges, _ = read_input('2025/data/input_day5.txt')
    # id_ranges, _ = read_input('2025/data/input_test.txt')
    sort_id = sort_id_ranges(id_ranges)
    finish = False 
    while not finish:
        sort_id, finish = merge_ranges(sort_id)
    total_fresh = 0 
    for lower, upper in sort_id: 
        fresh = calcul_in_range(lower, upper)
        total_fresh += fresh
    print(total_fresh)


if __name__ == '__main__': 
    print('start')
    run_part1()
    run_part2()
    print('end')
