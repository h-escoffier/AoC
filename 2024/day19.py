# Day19 - AoC 2024 


from tqdm import tqdm


def load_data(file):
    with open(file, 'r') as file:
        lines = file.readlines()
    towels = [item.strip() for item in lines[0].split(',')]
    patterns = [line.strip() for line in lines[1:] if line.strip()]
    return towels, patterns


def is_possible_combination(pattern, towels):
    def backtrack(remaining, memo):
        if remaining in memo:
            return memo[remaining]
        if not remaining:
            memo[remaining] = True
            return True
        for towel in towels:
            if remaining.startswith(towel):
                if backtrack(remaining[len(towel):], memo):
                    memo[remaining] = True
                    return True
        memo[remaining] = False
        return False
    memo = {}
    return backtrack(pattern, memo)



def run_part1(): 
    nb_possible_pattern = 0
    towels, patterns = load_data('data/day19_input.txt')
    for pattern in tqdm(iterable=patterns, desc='Progress Report - 1'):
        if is_possible_combination(pattern, towels):
            nb_possible_pattern += 1
    print(nb_possible_pattern)
            


if __name__ == "__main__":
    print('start')
    run_part1()
    print('end')