# Day 25 - AoC 2025 

from tqdm import tqdm
import pandas as pd


def load_data(file): 
    with open(file, 'r') as file:
        data = file.readlines()
        data = [line.strip() for line in data]
    return data


def indentify_block(data): 
    all_blocks = []
    block = []
    for line in data: 
        if line == '': 
            all_blocks.append(block)
            block = []
        else:
            block.append(line)
    all_blocks.append(block)
    return all_blocks


def convert_block_to_key(block): 
    # Convert block to matrix 
    if block[0] == '.....': 
        is_lock = False
    else:
        is_lock = True
    block_for_matrix = [list(row) for row in block[1:-1]]
    df = pd.DataFrame(block_for_matrix)
    # Convert to binary (1 = # and 0 = .)
    df = df.map(lambda x: 1 if x == '#' else 0)
    sum_columns = df.sum()
    heights = []
    for _, value in sum_columns.items():
        heights.append(value)
    return heights, is_lock


def is_overlapping(heights_lock, heights_key):
    for i in range(len(heights_lock)):
        if heights_lock[i] + heights_key[i] > 5:
            return False
    return True


def run(): 
    data = load_data('data/day25_input.txt') 
    # data = load_data('data/input_test.txt') 
    all_blocks = indentify_block(data)
    heights_lock = []
    heights_key = []
    for block in all_blocks: 
        heights, is_lock = convert_block_to_key(block)
        if is_lock:
            heights_lock.append(heights)
        else:
            heights_key.append(heights)

    nb_pairs = []    
    for lock in tqdm(iterable=heights_lock, desc='Progress Report - 1'):
        for key in heights_key: 
            # print(lock, key)
            if is_overlapping(lock, key):
                if (lock, key) not in nb_pairs:
                    nb_pairs.append((lock, key))
    print(len(nb_pairs))
    # print(nb_pairs)


if __name__ == "__main__":
    print('start')
    run()
    print('end')
