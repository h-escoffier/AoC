# Day5 - AoC 2024 


from tqdm import tqdm
import itertools
import sys


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
# Approache 1 
def is_valid_ticket_advanced(rules_before, rules_after, update):
    i = 0
    for elm in update:
        if len(update) == i + 1:
            return True, update, []
        indices = get_indices(rules_after, elm)
        values = get_values(rules_before, indices)
        intersection = list(set(values) & set(update[i:]))
        if len(intersection) != 0:
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


# Is valid but too long 
def run_part2_long():  # 2 long = too long :D 
    sum = 0 
    sum_corrected_only = 0
    counter = 0
    rules, updates = load_data("data/day5_input.txt")
    rules, updates = parser(rules, updates)
    rules = int_converter(rules)
    updates = int_converter(updates)   
    rules_before, rules_after = split_rules(rules)
    for update in updates:
        counter += 1
        is_valid, update_to_shuffle, update_ok = is_valid_ticket_advanced(rules_before, rules_after, update)
        if is_valid:
            middle_value = get_middle_value(update)
            sum += middle_value
        if not is_valid:
            # print(counter)
            for p in tqdm(itertools.permutations(update_to_shuffle), desc='Progress Report - Perm', leave=False):
                potential_update = update_ok + list(p)
                is_valid, update_good = is_valid_ticket_light(rules_before, rules_after, potential_update)
                if is_valid:
                    print(update_good)
                    middle_value = get_middle_value(update_good)
                    sum_corrected_only += middle_value
                    sum += middle_value
                    break
    print(sum)
    print(sum_corrected_only)


# Approach 2
def is_valid_ticket_advanced_2(rules_before, rules_after, update):
    i = 0
    for elm in update:
        if len(update) == i + 1:
            return True, update
        indices = get_indices(rules_after, elm)
        values = get_values(rules_before, indices)
        intersection = list(set(values) & set(update[i:]))
        if len(intersection) != 0:
            return False, update
        i += 1    

def fix_invalid_ticket(rules_before, rules_after, update):
    i = 0
    for elm in update:
        if len(update) == i + 1:
            return True, update
        indices = get_indices(rules_after, elm)
        values = get_values(rules_before, indices)
        intersection = list(set(values) & set(update[i:]))
        if len(intersection) != 0:
            idx = [update.index(value) for value in intersection]
            max_index = max(idx)
            new_update = []
            # Permutation 
            for i in range(len(update)):
                if update[i] == elm: 
                    new_update.append(update[max_index])
                elif update[i] == update[max_index]:
                    new_update.append(elm)  
                else: 
                    new_update.append(update[i])
            if len(intersection) != 0:
                return fix_invalid_ticket(rules_before, rules_after, new_update)  # Recursion time 
        i += 1  


def run_part2(): 
    sum = 0 
    sum_corrected_only = 0
    to_fix = []
    rules, updates = load_data("data/day5_input.txt")
    rules, updates = parser(rules, updates)
    rules = int_converter(rules)
    updates = int_converter(updates)   
    rules_before, rules_after = split_rules(rules)
    for update in tqdm(iterable=updates, desc='Progress Report - 2 - Part 1'):
        is_valid, invalid_update = is_valid_ticket_advanced_2(rules_before, rules_after, update)
        if is_valid:
            middle_value = get_middle_value(update)
            sum += middle_value
        else: 
            to_fix.append(invalid_update)
    for update in tqdm(iterable=to_fix, desc='Progress Report - 2 - Part 2'):     
            is_valid, fix_update = fix_invalid_ticket(rules_before, rules_after, update) 
            if is_valid: 
                middle_value = get_middle_value(fix_update)
                sum_corrected_only += middle_value
    # print(sum)
    print(sum_corrected_only)


# Try to redo the pop 'bug'
def is_valid_optimize(rules_before, rules_after, update, is_blocked):
    print(update)
    print(is_blocked)
    i = 0
    is_blocked += 1
    if is_blocked == 500: 
        print('HERE')
        return False, update
    for elm in update:
        if len(update) == i + 1:
            print(update)
            return True, update
        indices = get_indices(rules_after, elm)
        values = get_values(rules_before, indices)
        intersection = list(set(values) & set(update[i:]))
        if len(intersection) != 0:
            print('HERE1')
            # n = len(intersection)
            elm = update.pop(i)
            # update.insert(i + n, elm)
            # new_list = update[:i] + [elm] + update[i+1:i+n] + update[i+n+1:]
            new_list = update[:i+1]  # Take everything before index 'i'
            new_list.append(elm)   # Add the new element 'elm'
            new_list.extend(update[i+1:]) 
            print(new_list)
            is_valid_optimize(rules_before, rules_after, new_list, is_blocked)
            # return False, update
        i += 1


def run_pop(): 
    sum = 0 
    sum_corrected_only = 0
    to_fix = []
    rules, updates = load_data("data/day5_input.txt")
    rules, updates = parser(rules, updates)
    rules = int_converter(rules)
    updates = int_converter(updates)   
    rules_before, rules_after = split_rules(rules)
    for update in tqdm(iterable=updates, desc='Progress Report - 2 - Part 1'):
        is_valid, invalid_update = is_valid_optimize(rules_before, rules_after, update, 0)
        exit()
        if is_valid:
            middle_value = get_middle_value(update)
            sum += middle_value
        else: 
            to_fix.append(invalid_update)
    for update in tqdm(iterable=to_fix, desc='Progress Report - 2 - Part 2'):     
            is_valid, fix_update = fix_invalid_ticket(rules_before, rules_after, update) 
            if is_valid: 
                middle_value = get_middle_value(fix_update)
                sum_corrected_only += middle_value
    # print(sum)
    print(sum_corrected_only)



if __name__ == '__main__': 
    print('start')
    # run_part1()
    # run_part2()
    run_pop()
    print('end')
