# Day13 - AoC 2024 


import re 
import gurobipy as gp


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


def solve_problem(var_a_x, var_a_y, var_b_x, var_b_y, prize_x, prize_y): 
    # Create a Gurobi model
    m = gp.Model()
    m.setParam("NumericFocus", 3)
    # Create variables 
    a = m.addVar(vtype=gp.GRB.INTEGER, name='a')
    b = m.addVar(vtype=gp.GRB.INTEGER, name='b')
    cost = m.addVar(vtype=gp.GRB.INTEGER, name='cost')
    # Set the objective function
    m.setObjective(cost, gp.GRB.MINIMIZE)
    # Add constraints
    m.addConstr(cost == 3 * a + b)
    m.addConstr(a <= 100)
    m.addConstr(b <= 100)
    m.addConstr(var_a_x * a + var_b_x * b == prize_x)
    m.addConstr(var_a_y * a + var_b_y * b == prize_y)
    m.optimize()
    return int(cost.X) if m.status == gp.GRB.OPTIMAL else None


def solve_problem_part2(var_a_x, var_a_y, var_b_x, var_b_y, prize_x, prize_y): 
    # Create a Gurobi model
    m = gp.Model()
    # Create variables 
    a = m.addVar(vtype=gp.GRB.INTEGER, name='a')
    b = m.addVar(vtype=gp.GRB.INTEGER, name='b')
    cost = m.addVar(vtype=gp.GRB.INTEGER, name='cost')
    # Set the objective function
    m.setObjective(cost, gp.GRB.MINIMIZE)
    # Add constraints
    m.addConstr(cost == 3 * a + b)
    m.addConstr(a >= 0)
    m.addConstr(b >= 0)
    m.addConstr(var_a_x * a + var_b_x * b == prize_x)
    m.addConstr(var_a_y * a + var_b_y * b == prize_y)
    m.optimize()
    return int(cost.X) if m.status == gp.GRB.OPTIMAL else None


# Approach 1
# def is_equation_solvable(a, b, prize):  # Work on the test 
#     xa, ya = a
#     xb, yb = b
#     xp, yp = prize
#     A = np.array([[xa, xb],
#                   [ya, yb]])
#     b = np.array([xp, yp])
#     bounds = ([0, 0], [100, 100])
#     result = lsq_linear(A, b, bounds=bounds, method='trf')
#     return round(result.x[0]), round(result.x[1])


# def token_cost(nb_a, nb_b): 
#     return 3 * nb_a + nb_b


# Approach 2
# def minimize_cost_integer(a, b, prize, scale):
#     xa, ya = a
#     xb, yb = b
#     xp, yp = prize
    
#     xa, xb, xp = xa / scale, xb / scale, xp / scale
#     ya, yb, yp = ya / scale, yb / scale, yp / scale

#     problem = LpProblem("Minimize_Cost", LpMinimize)

#     # x0 = LpVariable("x0", lowBound=0, upBound=100, cat="Integer")
#     x0 = LpVariable("x0", lowBound=0, cat="Integer")
#     # x1 = LpVariable("x1", lowBound=0, upBound=100, cat="Integer")
#     x1 = LpVariable("x1", lowBound=0, cat="Integer")

#     problem += 3 * x0 + x1
#     problem += xa * x0 + xb * x1 == xp
#     problem += ya * x0 + yb * x1 == yp

#     status = problem.solve()

#     if LpStatus[status] == "Optimal":
#         x0_value = int(x0.varValue)
#         x1_value = int(x1.varValue)
#         cost = 3 * x0_value + x1_value
#         return cost
#     else:
#         return None


# def run_part1(): # 39252 Too high / 28181 Too low
#     total_cost = 0
#     lst_a, lst_b, lst_prize = load_data('data/day13_input.txt')
#     for a, b, prize in zip(lst_a, lst_b, lst_prize):
#         # print(a, b, prize)
#         # nb_a, nb_y = is_equation_solvable(a, b, prize)
#         cost = minimize_cost_integer(a, b, prize, 1)
#         if cost != None: 
#             total_cost += cost
#     print(total_cost)


def run_part1(): 
    total_cost = 0
    lst_a, lst_b, lst_prize = load_data('data/day13_input.txt')
    for a_value, b_value, prize in zip(lst_a, lst_b, lst_prize):
        cost = solve_problem(a_value[0], a_value[1], b_value[0], b_value[1], prize[0], prize[1])
        if cost is not None:
            total_cost += cost
    print(total_cost)


def run_part2(): # 57443519543982 Too low
    total_cost = 0
    # lst_a, lst_b, lst_prize = load_data('data/input_test.txt')
    lst_a, lst_b, lst_prize = load_data('data/day13_input.txt')
    for a_value, b_value, prize in zip(lst_a, lst_b, lst_prize):
        new_prize_0 = prize[0] + 10000000000000
        new_prize_1 = prize[1] + 10000000000000
        cost = solve_problem_part2(a_value, a_value[1], b_value[0], b_value[1], new_prize_0, new_prize_1)
        if cost is not None:
            total_cost += cost
    print(total_cost)


if __name__ == '__main__':
    print('start')
    # run_part1()
    run_part2()
    print('end')