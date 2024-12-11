# Day11 - AoC 2024 


from tqdm import tqdm


def load_data(file):
    with open(file, 'r') as file:
        data = [line.split() for line in file]
    return data[0]


def rules(stone):
    if stone == '0': 
        return ['1']
    elif len(stone) % 2 == 1: 
        return [str(int(stone)*2024)]
    else:
        where_split = len(stone) // 2 
        return stone[:where_split], str(int(stone[where_split:]))
    

def blinck(data):
    new_data = []
    for stone in data:
        new_stone_s = rules(stone)
        if len(new_stone_s) == 1: 
            new_data.append(new_stone_s[0])
        else : 
            part1, part2 = new_stone_s
            new_data.append(part1)
            new_data.append(part2)
    return new_data


def run_part1(): 
    blinck_data = load_data('data/day11_input.txt')
    for _ in tqdm(iterable=range(25), desc='Progress Report'): 
        # print(blinck_data)
        blinck_data = blinck(blinck_data)
    print(len(blinck_data)) 


def format_part2(data):
    data_dict = {}
    for stone in data: 
        if stone not in data_dict: 
            data_dict[stone] = 1
        else: 
            data_dict[stone] += 1
    return data_dict


def blinck_advanced(data_dict):
    new_dict = data_dict.copy()
    for stone in data_dict.keys():
        new_stone_s = rules(stone)
        if len(new_stone_s) == 1: 
            new_stone_s = new_stone_s[0]
            if new_stone_s in new_dict.keys(): 
                new_dict[new_stone_s] += data_dict[stone]
            else: 
                new_dict[new_stone_s] = data_dict[stone]
        else : 
            part1, part2 = new_stone_s
            if part1 in new_dict.keys(): 
                new_dict[part1] += data_dict[stone]
            else:
                new_dict[part1] = data_dict[stone]
            if part2 in new_dict.keys(): 
                new_dict[part2] += data_dict[stone]
            else:
                new_dict[part2] = data_dict[stone]
        new_dict[stone] -= data_dict[stone]
    return new_dict


def remove_all_zero(data_dict):
    new_dict = data_dict.copy()
    for stone in data_dict.keys():
        if data_dict[stone] == 0:
            del new_dict[stone]
    return new_dict


def run_part2():
    blinck_data = load_data('data/day11_input.txt')
    data_dict = format_part2(blinck_data)  
    for _ in tqdm(iterable=range(75), desc='Progress Report'): 
        data_dict = blinck_advanced(data_dict)
        data_dict = remove_all_zero(data_dict)
    print(sum(data_dict.values()))


if __name__ == '__main__': 
    print('start')
    run_part1()
    run_part2()
    print('end')
