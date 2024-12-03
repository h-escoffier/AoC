# Day1 - AoC 2024 


from tqdm import tqdm


def load_data(file):
    with open(file) as f:
        data = f.readlines()
        data = [x.strip().split() for x in data]
        data = [[int(x) for x in y] for y in data]
    return data

def split_list(data): 
    first_column = []
    second_column = []
    for pair in data: 
        first_column.append(pair[0])
        second_column.append(pair[1])
    return first_column, second_column
        

def rank_list(lst):
    return sorted(lst)


def difference(x, y):
    return x - y

def run_part1():
    total_difference = 0
    data = load_data('data/day1_input.txt')
    first_column, second_column = split_list(data)
    first_column = rank_list(first_column)
    second_column = rank_list(second_column) 
    for i in range(len(first_column)): 
        total_difference += abs(difference(first_column[i], second_column[i]))
    print(total_difference)


def how_many_times(lst, n): 
    return lst.count(n)


def run_part2(): 
    similarity_score = 0 
    data = load_data('data/day1_input.txt')
    first_column, second_column = split_list(data)
    first_column = rank_list(first_column)
    second_column = rank_list(second_column) 
    for elm in tqdm(iterable=first_column, desc='Progress report'): 
        count = how_many_times(second_column, elm) 
        similarity_score += count*elm
    print(similarity_score)


if __name__ == '__main__': 
    print('start')
    run_part1()
    run_part2()
    print('end')