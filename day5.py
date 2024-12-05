# Day5 - AoC 2024 


from tqdm import tqdm
import itertools


# 1st Part
def load_data(file):
    rules, updates = [], []
    # Open and read the file line by line
    with open(file, "r") as file: 
        for line in file:
            line = line.strip()
            if len(line) == 5:
                rules.append(line)
            elif line != '':
                updates.append(line)
    return rules, updates


def parser(rules, updates):
    # Updates 
    new_updates = [update.split(',') for update in updates]
    # Rules 
    new_rules = [rule.split('|') for rule in rules]
    return new_rules, new_updates


def int_converter(lst):
    new_lst = [[int(item) for item in sublist] for sublist in lst]
    return new_lst


def split_rules(rules):
    rules_before = [x[0] for x in rules]
    rules_after = [x[1] for x in rules]
    return rules_before, rules_after


def is_valid_ticket(rules_before, rules_after, update):
    i = 0
    for elm in update:
        if len(update) == i + 1:
            # print('Here1')
            return True
        indices = get_indices(rules_after, elm)
        # print(indices)
        values = get_values(rules_before, indices)
        # print(values)
        # if values in update[i:]:
        intersection = list(set(values) & set(update[i:]))
        if len(intersection) != 0:
            # print('Here2')
            return False
        i += 1


def get_indices(lst, value):
    indices = [i for i, x in enumerate(lst) if x == value]
    return indices


def get_values(lst, indices):
    values = [lst[i] for i in indices]
    return values

def get_middle_value(update): 
    middle_value = update[len(update) // 2]
    return middle_value


def run_part1():
    sum = 0 
    rules, updates = load_data("data/day5_input.txt")
    rules, updates = parser(rules, updates)
    rules = int_converter(rules)
    updates = int_converter(updates)   
    rules_before, rules_after = split_rules(rules)
    for update in tqdm(iterable=updates, desc='Progress Report - 1'):
        # print(update)
        is_valid = is_valid_ticket(rules_before, rules_after, update)
        if is_valid:
            middle_value = get_middle_value(update)
            sum += middle_value
        # break 
    print(sum)
            
        
# 2nd Part
def correct_update(): 
    pass 


def create_all_permutations(lst):
    perm = list(permutations(lst))
    return perm


def is_valid_ticket_advanced(rules_before, rules_after, update):
    i = 0
    for elm in update:
        if len(update) == i + 1:
            # print(update)
            # print('Here1')
            return True, update, []
        indices = get_indices(rules_after, elm)
        # print(indices)
        values = get_values(rules_before, indices)
        # print(values)
        # if values in update[i:]:
        intersection = list(set(values) & set(update[i:]))
        if len(intersection) != 0:
            # print('Here2')
            # print(i)
            # print(update)
            # print(update[i:])
            # print(update[:i])
            # exit()
            # update[i:]
            return False, update[i:], update[:i]
        i += 1


def is_valid_ticket_light(rules_before, rules_after, update):
    i = 0
    for elm in update:
        if len(update) == i + 1:
            # print('Here1')
            return True, update
        indices = get_indices(rules_after, elm)
        # print(indices)
        values = get_values(rules_before, indices)
        # print(values)
        # if values in update[i:]:
        intersection = list(set(values) & set(update[i:]))
        if len(intersection) != 0:
            # print('Here2')
            return False, []
        i += 1

def run_part2():
    sum = 0 
    sum_corrected_only = 0
    counter = 0
    # update_to_correct = []
    rules, updates = load_data("data/day5_input.txt")
    rules, updates = parser(rules, updates)
    rules = int_converter(rules)
    updates = int_converter(updates)   
    rules_before, rules_after = split_rules(rules)
    # for update in tqdm(iterable=updates, desc='Progress Report - 2 - Part 1'):
    for update in updates:

        counter += 1
        # print(update)
        is_valid, update_to_shuffle, update_ok = is_valid_ticket_advanced(rules_before, rules_after, update)
        if is_valid:
            # print(update_to_shuffle)
            middle_value = get_middle_value(update)
            sum += middle_value
        if not is_valid:
            print(counter)
            # update_to_correct.append(update)
            # perm = create_all_permutations(update_to_shuffle)
            # for p in tqdm(iterable=perm, desc='Progress Report - Perm'):
            for p in tqdm(itertools.permutations(update_to_shuffle), desc='Progress Report - Perm', leave=False):
            # for p in perm : 
                potential_update = update_ok + list(p)
                is_valid, update_good = is_valid_ticket_light(rules_before, rules_after, potential_update)
                if is_valid:
                    print(update_good)
                    middle_value = get_middle_value(update_good)
                    sum_corrected_only += middle_value
                    sum += middle_value
                    break
    # for update in tqdm(iterable=update_to_correct, desc='Progress Report - 2 - Part 2'):
    #     perm = create_all_permutations(update)
    #     for p in tqdm(iterable=perm, desc='Progress Report - Perm'):
    #         is_valid = is_valid_ticket(rules_before, rules_after, p)
    #         if is_valid:
    #             middle_value = get_middle_value(p)
    #             sum_corrected_only += middle_value
    #             sum += middle_value
    #             break      
    print(sum)
    print(sum_corrected_only)


if __name__ == '__main__': 
    print('start')
    # run_part1()
    run_part2()
    print('end')
