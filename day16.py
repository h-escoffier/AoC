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


def find_start(maze):
    pos_start = np.where(maze == "S")
    return (pos_start[0][0], pos_start[1][0])


def calculate_new_pos(pos, direction):
    moves = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
    return (pos[0] + moves[direction][0], pos[1] + moves[direction][1])


def change_direction(current_direction):
    directions = ["^", "<", "v", ">"]  
    return directions[(directions.index(current_direction) + 1) % 4]


def is_other_direction_explorable(maze, pos, score, path, current_direction):
    directions = ["^", "v", "<", ">"]
    valid_moves = []
    for direction in directions:
        new_pos = calculate_new_pos(pos, direction)
        if (
            maze[new_pos] in [".", "E"]  
            and new_pos not in path  
            and direction != current_direction 
        ):
            valid_moves.append((new_pos, direction, score, path))
    return valid_moves


def cost_of_the_direction_changment(current_direction, new_direction):
    directions = ['^', '<', 'v', '>']
    current_index = directions.index(current_direction)
    new_index = directions.index(new_direction)
    nb_changes = (new_index - current_index) % 4
    return 1000*nb_changes


def next_move(maze, start, direction, score, path, all_valid_moves, best_score, is_exit, original_maze):
    new_pos = calculate_new_pos(start, direction)
    if maze[new_pos] == "E":
        maze = original_maze.copy() # Restore previous state
        is_exit = True # Handle exit condition
        score += 1
        return maze, new_pos, direction, score, path, all_valid_moves, best_score, is_exit
    if maze[new_pos] == ".":
        score += 1
        # maze = original_maze.copy()
        maze[new_pos] = "P"
        path.append(new_pos)
        # Check if there are other directions to explore
        valid_moves = is_other_direction_explorable(maze, new_pos, score, path, direction)
        if valid_moves:
            all_valid_moves.extend(valid_moves)
        return maze, new_pos, direction, score, path, all_valid_moves, best_score, is_exit
    if maze[new_pos] == "#":
        # print(len(all_valid_moves))
        print(maze)
        old_direction = direction
        # Return to the last crossroad
        # maze = original_maze.copy()
        last_pos_to_explore = all_valid_moves.pop()
        pos = last_pos_to_explore[0]
        direction = last_pos_to_explore[1]
        score = last_pos_to_explore[2]
        path = last_pos_to_explore[3]
        score += cost_of_the_direction_changment(direction, old_direction)
        return maze, pos, direction, score, path, all_valid_moves, best_score, is_exit


def run_part1():
    best_score = float("inf") 
    maze = load_data("data/input_test.txt")
    original_maze = maze.copy()
    start = find_start(maze)
    direction = ">"
    all_valid_moves = is_other_direction_explorable(maze, start, 0, [start], direction)
    path = []
    score = 0
    is_exit = False
    i = 0 
    while not is_exit or all_valid_moves:
        print(all_valid_moves)
        maze, start, direction, score, path, all_valid_moves, best_score, is_exit = next_move(
            maze, start, direction, score, path, all_valid_moves, best_score, is_exit, original_maze
        )
        if is_exit and score < best_score:
            print(f"New best path found with score: {score}")
            best_score = score
        if i == 10: 
            exit()
        i += 1
    print(f"Lowest score: {best_score}")


if __name__ == "__main__":
    print('start')
    run_part1()  
    print('end')