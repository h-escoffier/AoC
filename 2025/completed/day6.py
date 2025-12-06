# Day6 - AoC 2025 


import pandas as pd


# Part1
def read_input(path): 
    with open(path) as f: 
        content = [line.strip().split(' ') for line in f.readlines()]
        new_content = []
        for line in content: 
            new_line = []
            for elm in line: 
                if elm != ' ' and elm != '': 
                    new_line.append(elm)
            new_content.append(new_line)
    return new_content


def sum_cols(df): 
    total = 0 
    last_row = df.iloc[-1].to_list()
    df.drop(df.tail(1).index,inplace=True)
    for i in range(len(last_row)): 
        df.iloc[:,i] = pd.to_numeric(df.iloc[:,i] , downcast='integer', errors='coerce')
        if last_row[i] == '*': 
            total_row = df.iloc[:,i].prod()
            total += total_row
        else: 
            total_row = df.iloc[:,i].sum()
            total += total_row
    return total             


def run_part1(): 
    content = read_input('2025/data/input_day6.txt')
    # content = read_input('2025/data/input_test.txt')
    df = pd.DataFrame(content)
    total = sum_cols(df)
    print(total)


# Part2
def read_input_2(path): 
    with open(path) as f: 
        content = [line.strip('\n') for line in f.readlines()]
        new_content = [list(r) for r in content]
    return new_content


# def rereading(df, operators): 
#     total = 0 
#     all_cols = []
#     for i in range(len(df.columns)): 
#         total_row = df.iloc[:,i].sum()
#         if total_row != '    ': 
#             all_cols.append(int(total_row))
#     nb_rows = df.shape[0]
#     print(nb_rows)
#     chunks = [all_cols[i:i+nb_rows] for i in range(0, len(all_cols), nb_rows)]
#     print(len(chunks))
#     print(chunks[-1])
#     # print(chunks)
#     for i in range(len(operators)): 
#         if operators[i] == '*': 
#             row = chunks[i]
#             product = 1
#             for elm in row: 
#                 product *= elm
#             total += product
#         if operators[i] == '+': 
#             row = chunks[i]
#             sum_r = 0 
#             for elm in row: 
#                 sum_r += elm
#             total += sum_r
#     return total        


def rereading(df, operators): 
    total = 0 
    all_cols = []
    small_list = []
    for i in range(len(df.columns)): 
        total_row = df.iloc[:,i].sum()
        if total_row != '    ':  # change by '   ' for the input_test 
            small_list.append(int(total_row))
        else: 
            all_cols.append(small_list)
            small_list = []
    all_cols.append(small_list)
    for i in range(len(operators)): 
        if operators[i] == '*': 
            row = all_cols[i]
            product = 1
            for elm in row: 
                product *= elm
            total += product
        if operators[i] == '+': 
            row = all_cols[i]
            sum_r = 0 
            for elm in row: 
                sum_r += elm
            total += sum_r
    return total        


def run_part2(): 
    # content = read_input_2('2025/data/input_test.txt')
    # content_previous = read_input('2025/data/input_test.txt')
    content = read_input_2('2025/data/input_day6.txt')
    content_previous = read_input('2025/data/input_day6.txt')
    df_previous = pd.DataFrame(content_previous)
    last_row = df_previous.iloc[-1].to_list()
    df = pd.DataFrame(content)
    df.drop(df.tail(1).index,inplace=True)
    total = rereading(df, last_row)
    print(total)


if __name__ == '__main__': 
    print('start')
    run_part1()
    run_part2()
    print('end')
