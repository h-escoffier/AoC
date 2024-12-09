# Day9 - AoC 2024 


from tqdm import tqdm


def load_data(file): 
    with open(file, 'r') as file:
        data = [line.strip() for line in file]
        data = data[0]
    return data


def create_one_line(data): 
    new_line = []
    idx_no_free_space = 0 
    for i in range(len(data)): 
        if i % 2 == 0: 
            new_line += [idx_no_free_space] * int(data[i])
            idx_no_free_space += 1 
        else:
            new_line += ['.'] * int(data[i])
    return new_line


# def permutation(lst, number_position, free_space_position):  # Too slow = 350 Perm/s
#     new_lst = []
#     for i in range(len(lst)): 
#         if i == number_position: 
#             new_lst.append(lst[free_space_position])
#         elif i == free_space_position: 
#             new_lst.append(lst[number_position])
#         else: 
#             new_lst.append(lst[i])
#     return new_lst


def permutation(lst, number_position, free_space_position):  # 2000 Perm/s
    lst[number_position], lst[free_space_position] = lst[free_space_position], lst[number_position]
    return lst


# def move_to_top_left_recursive(line, nb_permutation, nb_permutation_max, idx_to_move):
#     # new_line = []
#     # print(nb_permutation)
#     for i in tqdm(range(len(line)), desc='Progress Report - 1'): 
#         if line[i] != '.':
#             pass
#         else : 
#             if nb_permutation == nb_permutation_max : 
#                 print('Return')
#                 return line
#             new_line = permutation(line, i, len(line) - idx_to_move - 1)
#             nb_permutation += 1
#             idx_to_move += 1
#             # print(new_line)
#             return move_to_top_left(new_line, nb_permutation, nb_permutation_max, idx_to_move)
#     return new_line


def move_to_top_left_iterative(line, nb_permutation_max):
    nb_permutation = 0
    idx_to_move = 0
    with tqdm(desc="Progress Report - 1", unit=" Perm") as pbar:
        while nb_permutation < nb_permutation_max:
            # print(line)
            for i in range(len(line)): 
                if line[i] == '.':
                    free_space_position = len(line) - idx_to_move - 1
                    line = permutation(line, i, free_space_position)
                    nb_permutation += 1
                    idx_to_move += 1
                    break 
            pbar.update(1)
    return line


def sum_lst(lst): 
    sum_lst = 0
    # for i in tqdm(iterable=range(len(lst)), desc='Progress Report - 1'):
    for i in range(len(lst)): 
        if lst[i] == '.':
            return sum_lst
        sum_lst += i*lst[i]


def run_part1(): 
    data = load_data('data/day9_input.txt')
    one_line = create_one_line(data)
    nb_perm = one_line.count('.')
    new_line = move_to_top_left_iterative(one_line, nb_perm)
    sum = sum_lst(new_line)
    # print("OK") 
    print(sum)


def create_one_line_advanced(line):
    new_line = []
    same_elm = str(10000)
    inside_lst = []
    for elm in line:
        if elm == same_elm:
            inside_lst.append(elm)
        else:
            new_line.append(inside_lst)
            inside_lst = [elm]
            same_elm = elm
    new_line.append(inside_lst)
    new_line.pop(0)
    return new_line


def sum_lst_advanced(lst): 
    sum_lst = 0
    for i in range(len(lst)): 
        if lst[i] != '.':
            sum_lst += i*lst[i]
    return sum_lst


def reorganize(line): 
    # print(line)
    new_line = []
    idx_at_the_end = 1
    for elm in line: 
        # print(new_line)
        # print(elm[0])
        if elm[0] == '.':
            # print(len(elm))
            # print(len(line[-idx_at_the_end]))
            if len(elm) >= len(line[-idx_at_the_end]):
                new_line.append(line[-idx_at_the_end])
                # print(line[-idx_at_the_end])
                new_line.append(['.']*(len(elm)-len(line[-idx_at_the_end])))
                # print(new_line)
                # exit()
            idx_at_the_end += 1
        else:
            new_line.append(elm)
    print(new_line)    



def run_part2(): 
    data = load_data('data/day9_input_test.txt')
    one_line = create_one_line(data)
    print(one_line)
    nb_perm = one_line.count('.')
    one_line_advanced = create_one_line_advanced(one_line)
    # print(one_line_advanced)
    reorganize(one_line_advanced)


if __name__ == '__main__': 
    print('start')
    # run_part1()
    run_part2()
    print('end')
