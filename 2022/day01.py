# Day1 - AoC 2022


def read_input(path): 
    with open(path) as f: 
        content = [line.rstrip() for line in f.readlines()]
    return content


def run_part1(input_path):
    content = read_input(input_path)
    maxElf = 0 
    actualElf = 0 
    for snack in content: 
        if snack == '': 
            if actualElf >= maxElf: 
                maxElf = actualElf
            actualElf = 0 
        else: 
            actualElf += int(snack)
    print(maxElf)


def run_part2(input_path): 
    content = read_input(input_path)
    allSnacks = []
    actualElf = 0 
    for snack in content: 
        if snack == '': 
            allSnacks.append(actualElf)
            actualElf = 0 
        else: 
            actualElf += int(snack)
    allSnacks.sort(reverse=True)
    print(sum(allSnacks[:3]))


if __name__ == '__main__': 
    print('start')
    input_path = '2022/data/input_day01.txt'
    # input_path = '2022/data/input_test.txt'
    
    run_part1(input_path)
    run_part2(input_path)
    print('end')