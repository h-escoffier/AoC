# AoC 2015 - Day20


from itertools import combinations
import functools


# Thanks to Aurélien for the idea of the decomposition 
# PartOne and PartTwo each run for about 1 minute


# def runPart1(): # Too slow
#     input = 36000000
#     i = 1
#     # house = {}
#     at_least = False
#     while not at_least: 
#         # print('house ', i)
#         still_elfs = True
#         elfs = []
#         elf_nb = 1
#         gift_nb = 0
#         while still_elfs: 
#             # Init
#             elfs.append(elf_nb)
#             # print(elfs)
            
#             # print('elf', elf_nb)
#             if i % elf_nb == 0: 
#                 # print(elf_nb, 'add', 10*elf_nb)
#                     # print(elf * elf_nb)
#                     # house = deliver(elf, house, i)
#                     # print(house)
#                     # print(elf, elf_nb)
#                 gift_nb += 10*elf_nb
#             # print(i, elf_nb)
#             elf_nb += 1 
#             if elf_nb > i: 
#                 # print("here")
#                 still_elfs = False
                
#         if gift_nb >= input:
#             print(i)
#             final_answer = i
#             at_least = True
#         # print(i, gift_nb)
#         i += 1
#         if i % 1000 == 0: 
#             print(i, gift_nb)
#     print(final_answer)
#     print(final_answer)
#     print(final_answer)


# Source - https://stackoverflow.com/a/22808285
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def runTest(house):
    nb_gift = 0
    # pr_lst = prime_factors(house)
    # print(pr_lst)
    # pr_lst.append(1)
    # elves = []
    # for i in range(len(pr_lst)): 
    #     for values in combinations(pr_lst, i): 
    #         comb = 1
    #         for v in values: 
    #             comb *= v
    #         elves.append(comb)
    # elves.append(1)
    # elves = list(sorted(set(elves)))
    elves = find_divisors_generator_v2(house)
    for fc in elves: 
        nb_gift += fc * 10 
    print(house, nb_gift)
    # print(house)


def find_divisors_generator(n):
    for i in range(1, int(n**0.5) + 1):  # Loop up to √n
        if n % i == 0:
            yield i
            if i != n // i:
                yield n // i      # Yield the paired divisor


def find_divisors_generator_v2(num): 
    divisors = []
    for i in range(1, int(num**0.5) + 1):
        print(i)
        if num % i == 0:       # If 'i' is a divisor of 'num'
            divisors.append(i) # Add 'i' to the list of divisors
            if i != num // i:
                divisors.append(num // i)
        print(divisors)
    return divisors


def runPart1():
    input = 36000000
    # input = 200
    nb_gift = 0
    house = 0
    while nb_gift < input: 
        house += 1
        # pr_lst = prime_factors(house)
        nb_gift = 0
        # pr_lst.append(1)
        # elves = []
        # for i in range(len(pr_lst)): 
        #     for values in combinations(pr_lst, i): 
        #         comb = 1
        #         for v in values: 
        #             comb *= v
        #         elves.append(comb)
        # elves.append(1)
        # elves = list(sorted(set(elves)))
        # print(house, diviseurs)
        diviseurs = find_divisors_generator_v2(house)
        for fc in diviseurs: 
            nb_gift += fc * 10 
        if house % 1000 == 0: 
            print(house, nb_gift)
        # print(house, nb_gift)
        # if nb_gift >= input:
    print(house)

# 1297444330 Too high 


def runPart2(): 
    input = 36000000
    # input = 10000
    nb_gift = 0
    house = 0
    elves_register = {}
    while nb_gift < input: 
        house += 1
        pr_lst = prime_factors(house)
        nb_gift = 0
        pr_lst.append(1)
        elves = []
        for i in range(len(pr_lst)): 
            for values in combinations(pr_lst, i): 
                comb = 1
                for v in values: 
                    comb *= v
                elves.append(comb)
        elves.append(1)
        elves = list(sorted(set(elves)))
        for fc in elves: 
            elves_register[fc] = elves_register.get(fc, 0) + 1
            if elves_register[fc] >= 51: 
                pass
            else: 
                nb_gift += fc * 11 # I should read more carefully
        print('house ',house, 'nb_gift: ', nb_gift)
    print(house)

# 942480 Too high 


if __name__ == '__main__': 
    print('start')
    # runTest(10)
    # runPart1()
    runPart2()
    print('end')
