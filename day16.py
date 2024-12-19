# Day15 - AoC 2024 

import numpy as np


def load_data(path):
    with open(path, "r") as file:
        lines = file.readlines()
    maze = []
    for line in lines:
        line = line.strip()
        maze.append(list(line))
    maze_matrix = np.array([list(row) for row in maze])
    return maze_matrix


def find_start_and_exit(maze):
    pos_start = np.where(maze == "S")
    pos_exit = np.where(maze == "E")
    return (pos_start[0][0], pos_start[1][0]), (pos_exit[0][0], pos_exit[1][0])


def calculate_new_pos(pos, direction):
    if direction == "^":
        return (pos[0] - 1, pos[1])
    elif direction == "v":
        return (pos[0] + 1, pos[1])
    elif direction == "<":
        return (pos[0], pos[1] - 1)
    elif direction == ">":
        return (pos[0], pos[1] + 1)


def change_direction(direction):
    if direction == "^":
        return "<"
    elif direction == "<":
        return "v"
    elif direction == "v":
        return ">"
    elif direction == ">":
        return "^"


def next_move(maze, pos, direction, is_exit=False):
    # Check if the next move is a wall
    new_pos = calculate_new_pos(pos, direction)
    if maze[new_pos] == "#":
        direction = change_direction(direction)
        return maze, pos, direction, is_exit
    elif maze[new_pos] == ".":
        # Update the maze
        maze[pos] = "."
        maze[new_pos] = "S"
        return maze, new_pos, direction, is_exit
    else: # maze[new_pos] == "E"
        is_exit = True
        return maze, new_pos, direction, is_exit
    
def run_part1():
    maze = load_data("data/input_test.txt")
    start, exit = find_start_and_exit(maze)
    direction = '>'
    path = []



if __name__ == "__main__":
    print('start')
    run_part1()  
    print('end')