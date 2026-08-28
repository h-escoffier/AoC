# AoC 2015 - Day21


from itertools import combinations
from tqdm import tqdm


def read_input(path): 
    with open(path) as f: 
        content = [line.rstrip().split(" ") for line in f.readlines()]
    clean = []
    for line in content: 
        new_line = []
        for elm in line: 
            if elm != '': 
                new_line.append(elm)
        clean.append(new_line)
    return clean


def create_shop(categorie, shop): 
    correct = False
    new_shop = []
    for line in shop: 
        if ':' in line[0]: 
                  correct = False
        if line[0] == categorie + ':': 
            correct = True
        elif correct: 
            name, cost, damage, armor = line 
            new_shop.append([name, int(cost), int(damage), int(armor)])
    return new_shop


def extract_combination(combi): 
    if combi == (): 
        return 0, 0, 0
    total_cost, total_damage, total_armor = 0, 0, 0
    for elm in combi: 
        _, cost, damage, ar = elm
        total_cost += cost
        total_damage += damage
        total_armor += ar
    return total_cost, total_damage, total_armor


def create_all_warriors(weapons, armors, rings): 
    # cost, damage, armor
    stuffs = []
    total_cost, total_damage, total_armor = 0, 0, 0
    for i in range(1, 2): 
        for combi_w in combinations(weapons, i): 
            total_cost, total_damage, total_armor = 0, 0, 0          
            cost, damage, ar = extract_combination(combi_w)
            total_cost += cost
            total_damage += damage
            total_armor += ar
            for j in range(0, 6): 
                for combi_a in combinations(armors, j): 
                    total_cost_w, total_damage_w, total_armor_w = total_cost, total_damage, total_armor
                    cost, damage, ar = extract_combination(combi_a)
                    total_cost_w += cost
                    total_damage_w += damage
                    total_armor_w += ar
                    for k in range(0, 3): 
                        for combi_r in combinations(rings, k): 
                            total_cost_wa, total_damage_wa, total_armor_wa = total_cost_w, total_damage_w, total_armor_w
                            cost, damage, ar = extract_combination(combi_r)
                            total_cost_wa += cost
                            total_damage_wa += damage
                            total_armor_wa += ar
                            # print([total_cost, total_damage, total_armor])
                            stuffs.append([total_cost_wa, total_damage_wa, total_armor_wa])
    return stuffs


def battle(player, boss): 
    player_hit, player_damage, player_armor = player
    boss_hit, boss_damage, boss_armor = boss

    player_to_boss = player_damage - boss_armor
    if player_to_boss <= 0: 
        player_to_boss = 1

    boss_to_player = boss_damage - player_armor
    if boss_to_player <= 0: 
        boss_to_player = 1

    # print(boss_to_player)
    
    while player_hit > 0 or boss_hit > 0: 
        boss_hit -= player_to_boss
        if boss_hit <= 0: 
            return True
        player_hit -= boss_to_player
        if player_hit <= 0: 
            return False 

    return 'Unexpected'


def runPart1():
    shop = read_input("2015/data/input_day21.txt")
    weapons = create_shop('Weapons', shop)
    armors = create_shop('Armor', shop)
    rings = create_shop('Rings', shop)

    warriors_stuff = create_all_warriors(weapons, armors, rings)

    min_cost = 9999
    for stuff in tqdm(iterable=warriors_stuff, desc='part1'): 
        
        # Init
        player_hit = 100
        player_damage = 0
        player_armor = 0
        
        boss_hit = 104
        boss_damage = 8
        boss_armor = 1

        cost, damage, armor = stuff
        player_damage += damage
        player_armor += armor

        player = player_hit, player_damage, player_armor
        boss = boss_hit, boss_damage, boss_armor

        result = battle(player, boss)

        if result: 
            if cost <= min_cost:
                min_cost = cost

    print(min_cost)


def runPart2(): 
    shop = read_input("2015/data/input_day21.txt")
    weapons = create_shop('Weapons', shop)
    armors = create_shop('Armor', shop)
    rings = create_shop('Rings', shop)

    warriors_stuff = create_all_warriors(weapons, armors, rings)

    max_cost = 0 
    for stuff in tqdm(iterable=warriors_stuff, desc='part2'): 
        
        # Init
        player_hit = 100
        player_damage = 0
        player_armor = 0
        
        boss_hit = 104
        boss_damage = 8
        boss_armor = 1

        cost, damage, armor = stuff
        player_damage += damage
        player_armor += armor

        player = player_hit, player_damage, player_armor
        boss = boss_hit, boss_damage, boss_armor

        result = battle(player, boss)

        if not result: 
            if cost >= max_cost:
                max_cost = cost

    print(max_cost)


if __name__ == '__main__': 
    print('start')
    runPart1()
    runPart2()
    print('end')
