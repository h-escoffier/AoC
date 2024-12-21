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
    if direction == "^":
        return (pos[0] - 1, pos[1])
    elif direction == "v":
        return (pos[0] + 1, pos[1])
    elif direction == "<":
        return (pos[0], pos[1] - 1)
    elif direction == ">":
        return (pos[0], pos[1] + 1)


def change_direction(current_direction):
    directions = ["^", "<", "v", ">"]  
    return directions[(directions.index(current_direction) + 1) % 4]


# def is_there_a_crossroads(maze, pos, path, score): 
#     all_crossroads = []
#     directions = ["^", "v", "<", ">"]
#     for direction in directions:
#         new_pos = calculate_new_pos(pos, direction)
#         if maze[new_pos] == ".":
#             all_crossroads.append([(new_pos), path, direction, score + 1001])
#     return all_crossroads


def is_there_a_crossroads(maze, pos, path, score):
    all_crossroads = []
    directions = ["^", "v", "<", ">"]
    for direction in directions:
        new_pos = calculate_new_pos(pos, direction)
        if maze[new_pos[0]][new_pos[1]] == "." and new_pos not in path:
            all_crossroads.append([new_pos, path.copy(), direction, score + 1001])
    return all_crossroads


# def next_move(maze, pos, direction, score, path, crossroads, best_score, is_exit=False):
#     potential_crossroad = is_there_a_crossroads(maze, pos, path, score)
#     print(potential_crossroad)
#     new_pos = calculate_new_pos(pos, direction)
#     for potential in potential_crossroad:
#         if potential[0] not in path and potential[0] != new_pos:
#             crossroads.append(potential)
#     print(crossroads)
#     # If already be here, go back to the previous crossroads or score > best_score 
#     if (new_pos in path) or (score > best_score) or (is_exit == True):
#         if new_pos in path:
#             print('Already be here')
#         if score > best_score:
#             print('Score > best_score')
#         if is_exit == True:
#             print('Exit')
#         maze[pos] = "."
#         new_pos = crossroads[-1][0]
#         maze[new_pos] = "S"
#         path = crossroads[-1][1]
#         direction = crossroads[-1][2]
#         score = crossroads[-1][3]
#         crossroads.pop()
#         is_exit = False
#         print(pos)
#         print(direction)
#         print(crossroads)
#         print(maze)
#         exit()
#         return maze, new_pos, direction, score, path, crossroads, best_score, is_exit 
#     if maze[new_pos] == "#":
#         direction = change_direction(direction)
#         score += 1000
#         return maze, new_pos, direction, score, path, crossroads, best_score, is_exit 
#     elif maze[new_pos] == ".":
#         # Update the maze
#         maze[pos] = "."
#         maze[new_pos] = "S"
#         path.append(new_pos)
#         score += 1
#         return maze, new_pos, direction, score, path, crossroads, best_score, is_exit 
#     else: # maze[new_pos] == "E"
#         score += 1
#         print("Exit")
#         is_exit = True
#         return maze, new_pos, direction, score, path, crossroads, best_score, is_exit 
    

def next_move(maze, pos, direction, score, path, crossroads, best_score, is_exit=False):
    """
    Determine the next move based on the maze configuration and logic.
    """
    potential_crossroads = is_there_a_crossroads(maze, pos, path, score)
    for potential in potential_crossroads:
        if potential[0] not in path:
            crossroads.append(potential)

    new_pos = calculate_new_pos(pos, direction)
    if (new_pos in path) or (score > best_score) or is_exit:
        if new_pos in path:
            print("Already visited this position.")
        if score > best_score:
            print("Score exceeded best score.")
        if is_exit:
            print("Exit found.")
        if crossroads:
            last_crossroad = crossroads.pop()
            new_pos, path, direction, score = last_crossroad
            maze[pos[0]][pos[1]] = "."  # Mark the current position as free
            maze[new_pos[0]][new_pos[1]] = "S"  # Mark the new position as the start
        else:
            print("No crossroads left to explore.")
        return maze, new_pos, direction, score, path, crossroads, best_score, is_exit
    if maze[new_pos[0]][new_pos[1]] == "#":
        direction = change_direction(direction)
        score += 1000
        return maze, pos, direction, score, path, crossroads, best_score, is_exit
    elif maze[new_pos[0]][new_pos[1]] == ".":
        maze[pos[0]][pos[1]] = "."  # Mark the current position as free
        maze[new_pos[0]][new_pos[1]] = "S"  # Mark the new position as the start
        path.append(new_pos)  # Add to path
        score += 1
        return maze, new_pos, direction, score, path, crossroads, best_score, is_exit
    elif maze[new_pos[0]][new_pos[1]] == "E":
        score += 1
        print("Exit reached!")
        is_exit = True
        return maze, new_pos, direction, score, path, crossroads, best_score, is_exit


def find_best_path():
    """
    Main function to solve the maze using the best score path without external packages.
    """
    best_score = float("inf")  # Initialize the best score
    maze = load_data("data/input_test.txt")  # Load maze
    start = find_start(maze)  # Find start position
    direction = ">"  # Initial direction
    paths_to_explore = [[0, start, direction, [], []]]  # Initialize exploration list

    while paths_to_explore:
        # Select the path with the lowest score to explore next
        paths_to_explore.sort(key=lambda x: x[0])  # Sort by score (ascending)
        score, pos, direction, path, crossroads = paths_to_explore.pop(0)

        if maze[pos[0]][pos[1]] == "E":  # If exit is reached
            if score < best_score:
                best_score = score
            print(f"Best score: {best_score}")
            continue

        # Explore the next move
        maze, new_pos, new_direction, new_score, new_path, new_crossroads, _, _ = next_move(
            maze, pos, direction, score, path, crossroads, best_score
        )

        # Add the next move to the list of paths to explore
        paths_to_explore.append([new_score, new_pos, new_direction, new_path, new_crossroads])

    print(f"Final best score: {best_score}")


# def run_part1():
#     best_score = 1000000000 # Init best scorea
#     maze = load_data("data/input_test.txt")
#     start = find_start(maze)
#     direction = '>'
#     crossroads = []
#     path = []
#     score = 0
#     is_exit = False
#     while is_exit == False or len(crossroads) != 0:
#         # print(maze)
#         # print(path)
#         # print(direction)
#         maze, start, direction, score, path, crossroads, best_score, is_exit = next_move(maze, start, direction, score, path, crossroads, best_score, is_exit)
#         if is_exit == True:
#             if score < best_score:
#                 best_score = score
#             print(f"Score: {score}")


if __name__ == "__main__":
    print('start')
    # run_part1()  
    find_best_path()
    print('end')