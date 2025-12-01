# Day23 - AoC 2024 


from tqdm import tqdm


def load_data(file):
    all_connections = []
    with open(file, 'r') as f:
        lines = f.readlines()
    for line in lines:
        parts = line.strip().split('-')
        all_connections.append((parts[0], parts[1]))
    return all_connections


def find_triport(all_co): 
    triport = []
    for port1, port2 in tqdm(iterable=all_co, desc='Progress Report - Part 1'):
        for i in range(len(all_co)): 
            if port1 == all_co[i][0] and port2 == all_co[i][1]:
                continue
            if port1 == all_co[i][0]:
                if (port2, all_co[i][1]) in all_co:
                    triport.append((port1, port2, all_co[i][1]))
                elif (all_co[i][1], port2) in all_co:
                    triport.append((port1, port2, all_co[i][1]))
            elif port1 == all_co[i][1]:
                if (port2, all_co[i][0]) in all_co:
                    triport.append((port1, port2, all_co[i][0]))
                elif (all_co[i][0], port2) in all_co:
                    triport.append((port1, port2, all_co[i][0]))
            elif port2 == all_co[i][0]:
                if (port1, all_co[i][1]) in all_co:
                    triport.append((port2, port1, all_co[i][1]))
                elif (all_co[i][1], port1) in all_co:
                    triport.append((port2, port1, all_co[i][1]))
            elif port2 == all_co[i][1]:
                if (port1, all_co[i][0]) in all_co:
                    triport.append((port2, port1, all_co[i][0]))
                elif (all_co[i][0], port1) in all_co:
                    triport.append((port2, port1, all_co[i][0]))
    triport = remove_duplicates(triport)
    return triport


def remove_duplicates(sets_of_three):
    unique_sets = []
    for s in sets_of_three:
        if sorted(s) not in unique_sets:
            unique_sets.append(sorted(s))
    return unique_sets


def is_t_in_set(tri): 
    if tri[0].startswith('t'):
        return True
    elif tri[1].startswith('t'):
        return True
    elif tri[2].startswith('t'):
        return True
    return False


def count_t_in_sets(triports):
    count = 0
    for tri in triports:
        if is_t_in_set(tri):
            count += 1
    return count


def run_part1(): 
    # all_co = load_data('data/input_test.txt')
    all_co = load_data('data/day23_input.txt')
    triports = find_triport(all_co)
    print(count_t_in_sets(triports))


if __name__ == "__main__":
    print('start')
    run_part1()
    print('end')
