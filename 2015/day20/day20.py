# AoC 2015 - Day20


from itertools import combinations


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


def runPart1():
    input = 36000000
    # input = 150
    nb_gift = 0
    house = 0
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
            nb_gift += fc * 10 
        # print(house, nb_gift)
    print(house)

# 1297444330 Too high 


def runPart2(): 
    input = 36000000
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
        # print(house, nb_gift)
    print(house)

# 942480 Too high 


if __name__ == '__main__': 
    print('start')
    # runPart1()
    runPart2()
    print('end')
