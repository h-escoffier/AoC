# Day15 - AoC 2024 


import numpy as np


def load_data(path): 
    with open(path, "r") as file:
        lines = file.readlines()
    warehouse, moves = [], []
    for line in lines:
        line = line.strip()
        if line.startswith("#"):  
            warehouse.append(list(line))
        elif line: 
            moves.extend(line)
    warehouse_matrix = np.array([list(row) for row in warehouse])
    return warehouse_matrix, moves


def calculate_new_pos(pos, direction):
    if direction == "^":
        return (pos[0] - 1, pos[1])
    elif direction == "v":
        return (pos[0] + 1, pos[1])
    elif direction == "<":
        return (pos[0], pos[1] - 1)
    elif direction == ">":
        return (pos[0], pos[1] + 1)


def push_multiple_boxes(warehouse, pos_robot, direction):
    # find the non-box in the continuity of the box
    init_box_pos = calculate_new_pos(pos_robot, direction)
    # print(init_box_pos)
    new_pos = calculate_new_pos(pos_robot, direction)
    while warehouse[new_pos] == "O":
        new_pos = calculate_new_pos(new_pos, direction)
        # print(new_pos)
    if warehouse[new_pos]  == "#":
        return warehouse, pos_robot
    elif warehouse[new_pos]  == ".":
        warehouse[pos_robot] = "."
        warehouse[init_box_pos] = "@"
        warehouse[new_pos] = "O"
        return warehouse, new_pos


def move_robot(warehouse, pos_robot, direction):
    new_pos = calculate_new_pos(pos_robot, direction)
    if warehouse[new_pos] == "#": # Wall
        return warehouse, pos_robot
    elif warehouse[new_pos] == ".": # Empty space
        warehouse[pos_robot] = "."
        warehouse[new_pos] = "@"
        return warehouse, new_pos
    elif warehouse[new_pos] == "O": # Box
        new_pos_box = calculate_new_pos(new_pos, direction) # Check if it is possible to push the box
        if warehouse[new_pos_box] == "#": # Box against the wall
            return warehouse, pos_robot
        elif warehouse[new_pos_box] == ".": # Box can be pushed
            warehouse[pos_robot] = "."
            warehouse[new_pos] = "@"
            warehouse[new_pos_box] = "O"
            return warehouse, new_pos
        elif warehouse[new_pos_box] == "O": # Box against another box
            warehouse, new_pos = push_multiple_boxes(warehouse, pos_robot, direction)
            return warehouse, new_pos
    

def calcul_gps(warehouse):
    sum = 0 
    boxes = np.where(warehouse == "O")
    for pos_y, pos_x in list(zip(boxes[0], boxes[1])): 
        sum += 100*pos_y + pos_x
    return sum


def run_part1(): 
    warehouse, moves = load_data("data/day15_input.txt")
    for move in moves:
        pos_robot = np.where(warehouse == "@")
        warehouse, pos_robot = move_robot(warehouse, pos_robot, move)
    print(warehouse)
    sum = calcul_gps(warehouse)
    print(sum)


if __name__ == "__main__":
    print('start')
    run_part1()
    print('end')