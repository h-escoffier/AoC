# Day13 - AoC 2024 

import re 
import numpy as np 
from scipy.optimize import lsq_linear #, minimize
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpStatus
from pulp import PULP_CBC_CMD, GLPK_CMD
from tqdm import tqdm


def extract_coordinates(line, pattern):
    match = re.search(pattern, line)
    if match:
        x, y = int(match.group(1)), int(match.group(2))
        return x, y
    return None


def load_data(file):
    lst_a, lst_b, lst_prize = [], [], []
    with open(file, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 4): 
            line_a = lines[i].strip()
            line_b = lines[i + 1].strip()
            line_prize = lines[i + 2].strip()
            lst_a.append(extract_coordinates(line_a, r'X\+(\d+), Y\+(\d+)'))
            lst_b.append(extract_coordinates(line_b, r'X\+(\d+), Y\+(\d+)'))
            lst_prize.append(extract_coordinates(line_prize, r'X=(\d+), Y=(\d+)'))
    return lst_a, lst_b, lst_prize


# Approach 1
def is_equation_solvable(a, b, prize):  # Work on the test 
    xa, ya = a
    xb, yb = b
    xp, yp = prize
    A = np.array([[xa, xb],
                  [ya, yb]])
    b = np.array([xp, yp])
    bounds = ([0, 0], [100, 100])
    result = lsq_linear(A, b, bounds=bounds, method='trf')
    return round(result.x[0]), round(result.x[1])


def token_cost(nb_a, nb_b): 
    return 3 * nb_a + nb_b


# Approach 2
def minimize_cost_integer(a, b, prize, scale):
    xa, ya = a
    xb, yb = b
    xp, yp = prize
    
    xa, xb, xp = xa / scale, xb / scale, xp / scale
    ya, yb, yp = ya / scale, yb / scale, yp / scale

    problem = LpProblem("Minimize_Cost", LpMinimize)

    # x0 = LpVariable("x0", lowBound=0, upBound=100, cat="Integer")
    x0 = LpVariable("x0", lowBound=0, cat="Integer")
    # x1 = LpVariable("x1", lowBound=0, upBound=100, cat="Integer")
    x1 = LpVariable("x1", lowBound=0, cat="Integer")

    problem += 3 * x0 + x1
    problem += xa * x0 + xb * x1 == xp
    problem += ya * x0 + yb * x1 == yp

    status = problem.solve()

    if LpStatus[status] == "Optimal":
        x0_value = int(x0.varValue)
        x1_value = int(x1.varValue)
        cost = 3 * x0_value + x1_value
        return cost
    else:
        return None


def run_part1(): # 39252 Too high / 28181 Too low
    total_cost = 0
    lst_a, lst_b, lst_prize = load_data('data/day13_input.txt')
    for a, b, prize in zip(lst_a, lst_b, lst_prize):
        # print(a, b, prize)
        # nb_a, nb_y = is_equation_solvable(a, b, prize)
        cost = minimize_cost_integer(a, b, prize, 1)
        if cost != None: 
            total_cost += cost
    print(total_cost)
    

def run_part2(): 
    total_cost = 0
    lst_a, lst_b, lst_prize = load_data('data/day13_input.txt')
    for a, b, prize in zip(lst_a, lst_b, lst_prize):
        new_prize = (prize[0] + 10000000000000, prize[1] + 10000000000000)
        # print(a, b)
        # print(new_prize)
        cost = minimize_cost_integer(a, b, new_prize, 1e13)
        # cost = 0 
        if cost != None: 
            total_cost += cost
    print(total_cost)
    

if __name__ == '__main__': 
    print('start')
    run_part1()
    # run_part2()
    print('end')