# AoC 2015 - Day22


from itertools import product


def which_spell(name):
    if name == "Missile": 
        return 53, 4, 0, 0
    if name == "Drain": 
        return 73, 2, 2, 0
    if name == "Shield": 
        return 113, 0, 0, 6
    if name == "Poison": 
        return 173, 0, 0, 6
    if name == "Recharge": 
        return 229, 0, 0, 5
    

def calculate_mana(spells): 
    mana = 0
    for spell in spells: 
        if spell == "Missile": 
            mana += 53
        elif spell == "Drain": 
            mana += 73
        elif spell == "Shield": 
            mana += 113
        elif spell == "Poison": 
            mana += 173
        elif spell == "Recharge": 
            mana += 229
    return mana


def all_possibles_cast(spells, lenght, mode): 
    best_mana = 99999
    solution_found = False
    for i in range(1, lenght + 1): 
        if solution_found: 
            break 
        for combi in product(spells, repeat=i): 
            win, cast_spells = battle(combi, mode)
            if win: 
                mana = calculate_mana(cast_spells)
                if mana <= best_mana: 
                    # print(cast_spells)
                    solution_found = True
                    best_mana = mana
                    # print(best_mana)
    return best_mana


def battle(all_spells, mode): 

    player_hit = 50
    player_mana = 500

    player = (player_hit, player_mana)

    # Change input manually
    boss_hit = 55 
    boss_damage = 8

    boss = (boss_hit, boss_damage)

    effects = []
    win = False
    spells_cast = []
    for spell in all_spells: 
        spells_cast.append(spell)
        if mode == 'easy':
            end, correct, player, boss, effects, poison = turn(player, boss, spell, effects)
        if mode == 'hard': 
            end, correct, player, boss, effects, poison = hard_turn(player, boss, spell, effects)

        if end: 
            if not correct: 
                win = False
                break
            player_h, _ = player 
            boss_h, _ = boss
            if player_h <= 0: 
                win = False
                break 
            if boss_h <= 0: 
                win = True
                if poison: 
                    spells_cast.pop()
                break    
    if not win: 
        return False, []
    if win: 
        return True, spells_cast


def turn(player, boss, spell_n, effects):

    player_hit, player_mana = player
    boss_hit, boss_damage = boss
    player_armor = 0

    # Effects [Name, last]
    up_effects = []

    for effect in effects: 
        if effect[0] == "Shield": 
            player_armor = 7
        if effect[0] == "Poison": 
            boss_hit -= 3
        if effect[0] == "Recharge": 
            player_mana += 101

        last = effect[1] - 1
        if last != 0:
            new_effect = [effect[0]] + [last] 
            up_effects.append(new_effect)

    # Poison check 
    if boss_hit <= 0: 
        end = True # Boss is dead
        player = (player_hit, player_mana)
        boss = (boss_hit, boss_damage)
        correct = True 
        poison = True 
        return end, correct, player, boss, up_effects, poison

    # Player Spell 
    mana_cost, damage, heal, last = which_spell(spell_n)

    player_mana -= mana_cost

    if player_mana < 0: 
        return True, False, player, boss, up_effects, False
    
    if spell_n == "Missile" or spell_n == "Drain": 
        boss_hit -= damage
        player_hit += heal

    else: 
        for effect in up_effects: 
            if effect[0] == spell_n: 
                return True, False, player, boss, up_effects, False
        up_effects.append([spell_n, last])

    if boss_hit <= 0: 
        end = True # Boss is dead
        player = (player_hit, player_mana)
        boss = (boss_hit, boss_damage)
        return end, True, player, boss, up_effects, False

    # Boss Attack
    up_up_effects = []
    for effect in up_effects: 
        if effect[0] == "Shield": 
            player_armor = 7
        if effect[0] == "Poison": 
            boss_hit -= 3
        if effect[0] == "Recharge": 
            player_mana += 101

        last = effect[1] - 1
        if last != 0:
            new_effect = [effect[0]] + [last] 
            up_up_effects.append(new_effect)

    # Poison check 
    if boss_hit <= 0: 
        end = True # Boss is dead
        player = (player_hit, player_mana)
        boss = (boss_hit, boss_damage)
        correct = True 
        poison = False 
        return end, correct, player, boss, up_effects, poison
    
    boss_to_player = boss_damage - player_armor
    if boss_to_player <= 0: 
        boss_to_player = 1

    player_hit -= boss_to_player
    if player_hit <= 0: 
        end = True # Player is dead
        player = (player_hit, player_mana)
        boss = (boss_hit, boss_damage)
        return end, True, player, boss, up_effects, False

    end = False
    player = (player_hit, player_mana)
    boss = (boss_hit, boss_damage)
    return end, True, player, boss, up_up_effects, False


def runPart1():
    spells_n = ["Missile", "Drain", "Shield", "Poison", "Recharge"]
    best_mana = all_possibles_cast(spells_n, 30, 'easy')
    print(best_mana)

# 840 Too low


def hard_turn(player, boss, spell_n, effects):

    player_hit, player_mana = player
    boss_hit, boss_damage = boss
    player_armor = 0

    # Hard mode 
    player_hit -= 1
    if player_hit <= 0: 
        end = True # Player is dead
        player = (player_hit, player_mana)
        boss = (boss_hit, boss_damage)
        return end, False, player, boss, [], False

    # Effects [Name, last]
    up_effects = []

    for effect in effects: 
        if effect[0] == "Shield": 
            player_armor = 7
        if effect[0] == "Poison": 
            boss_hit -= 3
        if effect[0] == "Recharge": 
            player_mana += 101

        last = effect[1] - 1
        if last != 0:
            new_effect = [effect[0]] + [last] 
            up_effects.append(new_effect)

    # Poison check 
    if boss_hit <= 0: 
        end = True # Boss is dead
        player = (player_hit, player_mana)
        boss = (boss_hit, boss_damage)
        correct = True 
        poison = True 
        return end, correct, player, boss, up_effects, poison

    # Player Spell 
    mana_cost, damage, heal, last = which_spell(spell_n)

    player_mana -= mana_cost

    if player_mana < 0: 
        return True, False, player, boss, up_effects, False
    
    if spell_n == "Missile" or spell_n == "Drain": 
        boss_hit -= damage
        player_hit += heal

    else: 
        for effect in up_effects: 
            if effect[0] == spell_n: 
                return True, False, player, boss, up_effects, False
        up_effects.append([spell_n, last])

    if boss_hit <= 0: 
        end = True # Boss is dead
        player = (player_hit, player_mana)
        boss = (boss_hit, boss_damage)
        return end, True, player, boss, up_effects, False

    # Boss Attack
    player_hit -= 1  # Not clear that "Player turn" is boss AND player 
    if player_hit <= 0: 
        end = True # Player is dead
        player = (player_hit, player_mana)
        boss = (boss_hit, boss_damage)
        return end, False, player, boss, [], False

    up_up_effects = []
    for effect in up_effects: 
        if effect[0] == "Shield": 
            player_armor = 7
        if effect[0] == "Poison": 
            boss_hit -= 3
        if effect[0] == "Recharge": 
            player_mana += 101

        last = effect[1] - 1
        if last != 0:
            new_effect = [effect[0]] + [last] 
            up_up_effects.append(new_effect)

    # Poison check 
    if boss_hit <= 0: 
        end = True # Boss is dead
        player = (player_hit, player_mana)
        boss = (boss_hit, boss_damage)
        correct = True 
        poison = False 
        return end, correct, player, boss, up_effects, poison
    
    boss_to_player = boss_damage - player_armor
    if boss_to_player <= 0: 
        boss_to_player = 1

    player_hit -= boss_to_player
    if player_hit <= 0: 
        end = True # Player is dead
        player = (player_hit, player_mana)
        boss = (boss_hit, boss_damage)
        return end, True, player, boss, up_effects, False

    end = False
    player = (player_hit, player_mana)
    boss = (boss_hit, boss_damage)
    return end, True, player, boss, up_up_effects, False


def runPart2(): 
    spells_n = ["Missile", "Drain", "Shield", "Poison", "Recharge"]
    best_mana = all_possibles_cast(spells_n, 30, 'hard')
    print(best_mana)
    

if __name__ == '__main__': 
    print('start')
    runPart1()
    runPart2()
    print('end')
