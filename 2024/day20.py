# Day20 - AoC 2024 

import numpy as np
from collections import deque, Counter
from tqdm import tqdm


def load_data(path):
    with open(path, "r") as file:
        lines = file.readlines()
    maze = []
    for line in lines:
        line = line.strip()
        maze.append(list(line))
    return maze


def print_maze(maze):
    for row in maze:
        print("".join(row))


def find_s_and_e(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == "S":
                start_pt = (col, row)
            if maze[row][col] == "E":
                end_pt = (col, row)
    return start_pt, end_pt


def print_path(maze, path):
    maze_copy = [row[:] for row in maze]  # Create a copy to avoid modifying the original maze
    for y, x in path:
        maze_copy[x][y] = "O"
    print_maze(maze_copy)


def print_maze(maze):
    for row in maze:
        print("".join(row))

def bfs_shortest_path(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = set()
    queue = deque()
    
    # Each element: (x, y, path_so_far)
    queue.append((start[0], start[1], [start]))
    visited.add(start)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Left, Right, Up, Down

    while queue:
        x, y, path = queue.popleft()

        if (x, y) == end:
            return path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (0 <= nx < cols and 0 <= ny < rows and
                (nx, ny) not in visited and
                maze[ny][nx] in ('.', 'E')):  # Can walk on '.' or reach 'E'
                queue.append((nx, ny, path + [(nx, ny)]))
                visited.add((nx, ny))

    return None  # No path found


def find_all_cheating_combinations_of_one(maze):
    all_mazes = []
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == '#':
                new_maze = [r.copy() for r in maze]
                new_maze[i][j] = '.'
                all_mazes.append(new_maze)
    return all_mazes


def find_all_cheating_combinations_of_two_consecutive(maze):
    all_mazes = []
    seen = set()
    rows = len(maze)
    cols = len(maze[0])
    for i in range(rows):
        for j in range(cols):
            # Horizontal pair
            if j < cols - 1 and maze[i][j] == '#' and maze[i][j + 1] == '#':
                new_maze = [r.copy() for r in maze]
                new_maze[i][j] = '.'
                new_maze[i][j + 1] = '.'
                maze_tuple = tuple(tuple(r) for r in new_maze)
                if maze_tuple not in seen:
                    seen.add(maze_tuple)
                    all_mazes.append(new_maze)
            # Vertical pair
            if i < rows - 1 and maze[i][j] == '#' and maze[i + 1][j] == '#':
                new_maze = [r.copy() for r in maze]
                new_maze[i][j] = '.'
                new_maze[i + 1][j] = '.'
                maze_tuple = tuple(tuple(r) for r in new_maze)
                if maze_tuple not in seen:
                    seen.add(maze_tuple)
                    all_mazes.append(new_maze)

    return all_mazes


def run_part1():
    # maze = load_data("data/input_test.txt")
    maze = load_data("data/day20_input.txt")
    start, end = find_s_and_e(maze)
    theoritical_time = len(bfs_shortest_path(maze, start, end)) - 1
    # print("Theoretical Time:", theoritical_time)
    # Find all cheating combinations of one
    counter_of_cheating = 0
    all_mazes = find_all_cheating_combinations_of_one(maze)
    for maze in tqdm(iterable=all_mazes, desc='Progress Report - Part 1'):
        new_time = len(bfs_shortest_path(maze, start, end)) - 1
        # if new_time <= theoritical_time - 64:
        if new_time <= theoritical_time - 100:    
            counter_of_cheating += 1
    # all_mazes = find_all_cheating_combinations_of_two_consecutive(maze)
    # for maze in tqdm(iterable=all_mazes, desc='Progress Report - Part 1 - Two Cheating'):
    #     new_time = len(bfs_shortest_path(maze, start, end)) - 1
    #     # if new_time <= theoritical_time - 64:
    #     if new_time <= theoritical_time - 100:
    #         print("Found a cheating maze with time:", new_time)
    #         print_maze(maze)
    #         print('')
    #         counter_of_cheating += 1
    print(counter_of_cheating)


def run_part_test():
    maze = load_data("data/input_test.txt")
    start, end = find_s_and_e(maze)
    theoritical_time = len(bfs_shortest_path(maze, start, end)) - 1
    print("Theoretical Time:", theoritical_time)
    # Find all cheating combinations of one
    counter_of_cheating = 0
    all_saved_times = []
    all_mazes = find_all_cheating_combinations_of_one(maze)
    for maze in tqdm(iterable=all_mazes, desc='Progress Report - Part 1 - One Cheating'):
        new_time = len(bfs_shortest_path(maze, start, end)) - 1
        # if new_time <= theoritical_time - 64:
        if new_time < theoritical_time :
            all_saved_times.append(theoritical_time - new_time)
            counter_of_cheating += 1
            print_maze(maze)
            print('')
    # all_mazes = find_all_cheating_combinations_of_two_consecutive(maze)
    # for maze in tqdm(iterable=all_mazes, desc='Progress Report - Part 1 - Two Cheating'):
    #     new_time = len(bfs_shortest_path(maze, start, end)) - 1
    #     if new_time <= theoritical_time - 64:
    #     # if new_time < theoritical_time:
    #         all_saved_times.append(theoritical_time - new_time)
    #         print_maze(maze)
    #         print('')
    #         counter_of_cheating += 1
    counts = Counter(all_saved_times)
    print(counts)


if __name__ == "__main__":
    print('start')
    # run_part_test()
    run_part1()  
    print('end')