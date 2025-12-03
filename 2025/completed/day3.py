# Day3 - AoC 2025 


def read_input(path): 
    with open(path) as f: 
        content = [line.strip() for line in f.readlines()]
    return content 


# Part1
def parse_banks(bank): 
    joltage = 0
    max_1, max_2 = 0, 0
    for i in range(len(bank) - 1):
        storage = int(bank[i])
        if storage > max_1: 
            max_1 = storage
            pos = i 
    for storage in bank[pos+1:]: 
        storage = int(storage)
        if storage > max_2:
            max_2 = storage 
    joltage = int(str(max_1) + str(max_2))
    return joltage


def run_part1(): 
    content = read_input('2025/data/input_day3.txt')
    # content = read_input('2025/data/input_test.txt')
    total_joltage = 0
    for bank in content: 
        joltage = parse_banks(bank)
        total_joltage += joltage
    print(total_joltage)


# Part2
def parse_banks_adv(bank): 
    joltage = 0
    max_1, max_2, max_3, max_4, max_5, max_6, = 0, 0, 0, 0, 0, 0
    max_7, max_8, max_9, max_10, max_11, max_12, = 0, 0, 0, 0, 0, 0
    for i in range(len(bank) - 11):
        storage = int(bank[i])
        if storage > max_1: 
            max_1 = storage
            pos = i 
    for i in range(pos + 1, len(bank) - 10):
        storage = int(bank[i])
        if storage > max_2: 
            max_2 = storage
            pos = i 
    for i in range(pos + 1, len(bank) - 9):
        storage = int(bank[i])
        if storage > max_3: 
            max_3 = storage
            pos = i 
    for i in range(pos + 1, len(bank) - 8):
        storage = int(bank[i])
        if storage > max_4: 
            max_4 = storage
            pos = i 
    for i in range(pos + 1, len(bank) - 7):
        storage = int(bank[i])
        if storage > max_5: 
            max_5 = storage
            pos = i 
    for i in range(pos + 1, len(bank) - 6):
        storage = int(bank[i])
        if storage > max_6: 
            max_6 = storage
            pos = i 
    for i in range(pos + 1, len(bank) - 5):
        storage = int(bank[i])
        if storage > max_7: 
            max_7 = storage
            pos = i
    for i in range(pos + 1, len(bank) - 4):
        storage = int(bank[i])
        if storage > max_8: 
            max_8 = storage
            pos = i
    for i in range(pos + 1, len(bank) - 3):
        storage = int(bank[i])
        if storage > max_9: 
            max_9 = storage
            pos = i
    for i in range(pos + 1, len(bank) - 2):
        storage = int(bank[i])
        if storage > max_10: 
            max_10 = storage
            pos = i
    for i in range(pos + 1, len(bank) - 1):
        storage = int(bank[i])
        if storage > max_11: 
            max_11 = storage
            pos = i
    for storage in bank[pos+1:]: 
        storage = int(storage)
        if storage > max_12:
            max_12 = storage 
    joltage = int(str(max_1) + str(max_2) + str(max_3) + str(max_4) + str(max_5) + str(max_6) + str(max_7) + str(max_8) + str(max_9) + str(max_10) + str(max_11) + str(max_12))
    return joltage


def run_part2():
    content = read_input('2025/data/input_day3.txt')
    # content = read_input('2025/data/input_test.txt')
    total_joltage = 0
    for bank in content: 
        joltage = parse_banks_adv(bank)
        total_joltage += joltage
    print(total_joltage)


if __name__ == '__main__': 
    print('start')
    run_part1()
    run_part2()
    print('end')
