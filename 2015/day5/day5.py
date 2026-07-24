# AoC 2015 - Day5


import re


def read_input(path): 
    with open(path) as f: 
        content = [line.rstrip() for line in f.readlines()]
    return content


def run_part1(): 
    lines = read_input('2015/data/input_day5.txt')
    count = 0 
    for line in lines: 
        if conditions(line): 
            count += 1 
    print(count)        


def conditions(string): 
    # Condition 3 
    if re.match('^.*ab', string) or re.match('^.*cd', string) or re.match('^.*pq', string) or re.match('^.*xy', string): 
        return False
    # if re.match(r'(\w+)+\1', string): 
    vowels = ['a', 'e', 'i', 'o', 'u']
    condition_vowels, condition_in_a_row = False, False
    count_vowel = 0
    previous_letter = '0'
    for letter in string: 
        if letter == previous_letter:
            condition_in_a_row = True
        previous_letter = letter
        if letter in vowels and letter:
            count_vowel += 1
            if count_vowel == 3: 
                condition_vowels = True
        if condition_in_a_row and condition_vowels: 
            return True
    return False


def run_part2(): 
    lines = read_input('2015/data/input_day5.txt')
    count = 0

    for line in lines: 
        if new_conditions(line): 
            count += 1 
    print(count)  

def new_conditions(string): 

    twice_split_by_one, two_pattern = False, False

    small_pattern = []
    previous_letter = '0'
    previous_previous_letter = '0'

    for letter in string: 
        if previous_previous_letter == letter: 
            twice_split_by_one = True

        if previous_letter + letter in small_pattern :
            nb_pattern = 0 
            for pattern in small_pattern: 
                if previous_letter + letter == pattern: 
                    nb_pattern += 1 
            if nb_pattern > 1 or (nb_pattern == 1 and small_pattern[-1] != previous_letter + letter):
                two_pattern = True
                
        small_pattern.append(previous_letter + letter)
        previous_previous_letter = previous_letter
        previous_letter = letter

        if twice_split_by_one and two_pattern: 
            return True

    return False


if __name__ == '__main__': 
    print('start')
    # run_part1()
    run_part2()
    print('end')