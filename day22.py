# Day22 - AoC 2024 


from math import * 
from tqdm import tqdm


def load_data(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    return [int(line.strip()) for line in lines if line.strip()]


def evolve(secret_nb, steps): 
    for _ in range(steps):
        # Step 1 
        result = int(secret_nb * 64)
        secret_nb = mix(secret_nb, result)
        secret_nb = prune(secret_nb)
        # Step 2
        result = int(floor(secret_nb / 32))
        secret_nb = mix(secret_nb, result)
        secret_nb = prune(secret_nb)
        # Step 3
        result = int(secret_nb * 2048)
        secret_nb = mix(secret_nb, result)
        secret_nb = prune(secret_nb)
    return secret_nb 


def mix(secret_nb, result): 
    return int(result ^ secret_nb)  # XOR operation 


def prune(secret_nb): 
    return int(secret_nb % 16777216)


def run_part1(): 
    # init_secret_nb = load_data('data/input_test.txt') 
    init_secret_nb = load_data('data/day22_input.txt') 
    # print(init_secret_nb)
    nb_step = 2000
    output = 0 
    for secret_nb in tqdm(init_secret_nb, desc='Progress Report - Part 1'):
        secret_nb = evolve(secret_nb, nb_step)
        output += secret_nb
    print(output)

if __name__ == "__main__":
    print('start')
    run_part1()
    print('end')


