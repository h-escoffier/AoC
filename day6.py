# Day6 - AoC 2024 


import numpy as np 
from tqdm import tqdm
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import itertools


def load_data(file): 
    with open(file, 'r') as file:
        data = [line.strip() for line in file]
    return data


def find_guard(data):
    for x, row in enumerate(data): 
        for y, value in enumerate(row):  
            if value == "^":  
                return x, y 


# Because using try is not always a good idea :(
# def mouvement(data, guard, direction, counter, counter_direction, list_of_alreay_visited): 
#     directions = ['up', 'right', 'down', 'left']
#     moves = {'up': (-1, 0),     
#              'right': (0, 1),   
#              'down': (1, 0),    
#              'left': (0, -1)}   
#     x, y = guard
#     dx, dy = moves[direction]
#     # new_x, new_y = move((x, y), direction)
#     new_x, new_y = x + dx, y + dy
#     # print(new_x, new_y)
#     try : 
#         if data[new_x][new_y] == '.' or data[new_x][new_y] == '^':
#             if (new_x, new_y) not in list_of_alreay_visited: 
#                 # print('Here')
#                 counter += 1
#                 list_of_alreay_visited.append((new_x, new_y))
#             return (new_x, new_y), direction, counter, counter_direction, list_of_alreay_visited
#         else:
#             # print(counter)
#             # exit()
#             new_direction = directions[(directions.index(direction) + 1) % 4]
#             counter_direction += 1
#             return guard, new_direction, counter, counter_direction, list_of_alreay_visited
#     except : 
#         return guard, 'END', counter, counter_direction, list_of_alreay_visited


def mouvement(data, guard, direction, counter, counter_direction, list_of_already_visited): 
    directions = ['up', 'right', 'down', 'left']
    moves = {'up': (-1, 0),     
             'right': (0, 1),   
             'down': (1, 0),    
             'left': (0, -1)}   
    x, y = guard
    dx, dy = moves[direction]
    new_x, new_y = x + dx, y + dy
    if not (0 <= new_x < len(data) and 0 <= new_y < len(data[0])):
        return guard, 'END', counter, counter_direction, list_of_already_visited
    elif data[new_x][new_y] == '.' or data[new_x][new_y] == '^':
        if (new_x, new_y) not in list_of_already_visited:
            counter += 1
            list_of_already_visited.append((new_x, new_y))
        return (new_x, new_y), direction, counter, counter_direction, list_of_already_visited
    else: 
        new_direction = directions[(directions.index(direction) + 1) % 4]
        counter_direction += 1
        return guard, new_direction, counter, counter_direction, list_of_already_visited


def run_part1_with_animation():
    data = load_data('data/day6_input.txt') 
    guard = find_guard(data)  
    direction = 'up'
    animate_movement(data, guard, direction) 


def animate_movement(data, guard_start, direction_start):
    fig, ax = plt.subplots()
    ax.set_xticks(np.arange(len(data[0])))
    ax.set_yticks(np.arange(len(data)))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    
    grid = np.array([list(row) for row in data])
    im = ax.imshow(grid == '.', cmap='Greys', interpolation='nearest')
    guard_marker, = ax.plot([], [], 'go', markersize=12) 

    def update(frame):
        nonlocal guard_start, direction_start
        guard_start, direction_start, _, _, _= mouvement(data, guard_start, direction_start, frame, 0, [])
        # Update the grid
        grid = np.array([list(row) for row in data])
        x, y = guard_start
        grid[x, y] = '^' 
        # Update the guard
        im.set_data(grid == '.')  
        guard_marker.set_data([y], [x]) 
        return guard_marker, im
    # Animation time
    ani = FuncAnimation(fig, update, frames=100, interval=1, blit=False)
    plt.show()


def run_part1(): 
    data = load_data('data/day6_input.txt')
    guard = find_guard(data)
    # print(guard)
    direction = 'up'
    counter = 0
    counter_direction = 0
    list_of_already_visited = [guard]
    with tqdm(desc="Progress Report - 1", unit="Steps") as pbar:
        while direction != 'END':
            guard, direction, counter, counter_direction, list_of_already_visited = mouvement(data, guard, direction, counter, counter_direction, list_of_already_visited)
            pbar.update(1)
    print(len(list_of_already_visited))


# 2nd Part 
# 1st Approach - Work on the test but not on the real input
# def find_all_obstacles(data):
#     obstacles = []
#     for x, row in enumerate(data): 
#         for y, value in enumerate(row):  
#             if value == '#':  
#                 obstacles.append((x, y))
#     return obstacles


# def find_neighbors(data):
#     neighbors = []
#     rows, cols = len(data), len(data[0])
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#     for i in range(rows):
#         for j in range(cols):
#             if data[i][j] == "#":
#                 for di, dj in directions:
#                     ni, nj = i + di, j + dj
#                     if 0 <= ni < rows and 0 <= nj < cols:  
#                         neighbors.append((ni, nj))
#     return neighbors


# def is_point_on_segment(p, p1, p2):
#     cross_product = (p[1] - p1[1]) * (p2[0] - p1[0]) - (p[0] - p1[0]) * (p2[1] - p1[1])
#     if cross_product != 0:
#         return False
#     if min(p1[0], p2[0]) <= p[0] <= max(p1[0], p2[0]) and min(p1[1], p2[1]) <= p[1] <= max(p1[1], p2[1]):
#         return True
#     return False


# def is_there_loop(obstacles, position_before_obstacles_encountered, all_position_around_obstacles, list_of_already_visited):     
#     pos1, pos2, pos3 = position_before_obstacles_encountered
#     x4 = pos1[0] + pos3[0] - pos2[0]
#     y4 = pos1[1] + pos3[1] - pos2[1]
#     pos4 = (x4, y4) 
#     if not (0 <= x4 < 9 and 0 <= y4 < 9):
#         return False
#     if not (pos1 in list_of_already_visited or
#             pos2 in list_of_already_visited or
#             pos3 in list_of_already_visited or
#             pos4 in list_of_already_visited):
#         return False
#     # print(pos1, pos2, pos3, pos4)   
#     for point in obstacles:
#         if (is_point_on_segment(point, pos1, pos2) or
#             is_point_on_segment(point, pos2, pos3) or
#             is_point_on_segment(point, pos3, pos4) or
#             is_point_on_segment(point, pos4, pos1)):
#             return False
#     print(pos1, pos2, pos3, pos4)
#     return True


# def is_rectangle(triplet):
#     p1, p2, p3 = triplet
#     d1 = (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 
#     d2 = (p3[0] - p2[0])**2 + (p3[1] - p2[1])**2  
#     d3 = (p1[0] - p3[0])**2 + (p1[1] - p3[1])**2 
#     distances = sorted([d1, d2, d3])
#     return distances[0] + distances[1] == distances[2] 


# def mouvement_advanced(data, guard, direction, counter, list_of_already_visited, position_before_obstacles_encountered, all_positions): 
#     directions = ['up', 'right', 'down', 'left']
#     moves = {'up': (-1, 0),     
#              'right': (0, 1),   
#              'down': (1, 0),    
#              'left': (0, -1)}   
#     x, y = guard
#     dx, dy = moves[direction]
#     new_x, new_y = x + dx, y + dy
#     if not (0 <= new_x < len(data) and 0 <= new_y < len(data[0])):
#         return guard, 'END', counter, list_of_already_visited, position_before_obstacles_encountered, all_positions
#     elif data[new_x][new_y] == '.' or data[new_x][new_y] == '^':
#         if (new_x, new_y) not in list_of_already_visited:
#             list_of_already_visited.append((new_x, new_y))
#         return (new_x, new_y), direction, counter, list_of_already_visited, position_before_obstacles_encountered, all_positions
#     else: 
#         position_before_obstacles_encountered.append((x, y))
#         all_positions.append((x, y))
#         new_direction = directions[(directions.index(direction) + 1) % 4]
#         if len(position_before_obstacles_encountered) == 3: # Test if there is a potential loop
#             # print(position_before_obstacles_encountered)
#             # is_loop = is_there_loop(all_obstacles, position_before_obstacles_encountered)
#             # if is_loop: 
#             #     counter += 1        
#             new_list = position_before_obstacles_encountered[1:]
#             return guard, new_direction, counter, list_of_already_visited, new_list, all_positions
#         return guard, new_direction, counter, list_of_already_visited, position_before_obstacles_encountered, all_positions


# def run_part2():
#     data = load_data('data/day6_input_test.txt')
#     print(len(data), len(data[0]))
#     guard = find_guard(data)
#     obstacles = find_all_obstacles(data)
#     direction = 'up'
#     counter = 0
#     list_of_already_visited = [guard]
#     position_before_obstacles_encountered = []
#     all_positions = []
#     with tqdm(desc="Progress Report - 2", unit="Steps") as pbar:
#         while direction != 'END':
#             guard, direction, counter, list_of_already_visited, position_before_obstacles_encountered, all_positions = mouvement_advanced(data, guard, direction, counter, list_of_already_visited, position_before_obstacles_encountered, all_positions)
#             pbar.update(1)
#     # print(counter)
#     # print(len(list_of_already_visited))
#     # The problem is to find is a loop is possible with adding a point but not in the last three points
#     final_countdown = 0 # Tututuuuu tu tu tu tu
#     all_3_combination = list(itertools.combinations(all_positions, 3))
#     # print(len(all_3_combination))
#     all_position_around_obstacles = find_neighbors(data)
#     for triplet in tqdm(iterable=all_3_combination):
#         if is_rectangle(triplet): 
#             is_loop = is_there_loop(obstacles, triplet, all_position_around_obstacles, list_of_already_visited)
#             if is_loop: 
#                 final_countdown += 1
#     print(final_countdown)


# 2nd Approach - Did with AI 
def read_input(file_path):
    # Read the data
    with open(file_path, 'r') as f:
        grid = [list(line.strip()) for line in f.readlines()]
    # Find guards
    directions = {'^', '>', 'v', '<'}
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell in directions:
                return grid, (i, j), cell


def simulate_guard(grid, start_pos, start_dir):
    directions = ['^', '>', 'v', '<'] 
    deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]  
    infinite_loop_positions = set()

    def move(pos, dir_idx):
        return (pos[0] + deltas[dir_idx][0], pos[1] + deltas[dir_idx][1])
    
    for i in tqdm(iterable=range(len(grid)), desc='Progress Report - 2'):
        for j in range(len(grid[0])):
            if grid[i][j] != '.': # Skip if obstacle
                continue
            grid[i][j] = 'O'  # Place an obstacle
            pos, dir_idx = start_pos, directions.index(start_dir)
            already_visited = set()
            loop_detected = False
            while True:
                if (pos, dir_idx) in already_visited:
                    loop_detected = True
                    break
                already_visited.add((pos, dir_idx))
                # Move
                next_pos = move(pos, dir_idx)
                if next_pos[0] < 0 or next_pos[0] >= len(grid) or \
                   next_pos[1] < 0 or next_pos[1] >= len(grid[0]):
                    break  # Exit 
                if grid[next_pos[0]][next_pos[1]] == '#':
                    dir_idx = (dir_idx + 1) % 4  # Turn 
                elif grid[next_pos[0]][next_pos[1]] == 'O':
                    dir_idx = (dir_idx + 1) % 4  # Turn 
                else:
                    pos = next_pos  # Move forward
            if loop_detected:
                infinite_loop_positions.add((i, j))        
            grid[i][j] = '.'  # Remove the obstacle
    return infinite_loop_positions


def run_part2(): 
    grid, guard_pos, guard_dir = read_input("data/day6_input.txt")
    infinite_loop_positions = simulate_guard(grid, guard_pos, guard_dir)
    print(len(infinite_loop_positions)) 


if __name__ == "__main__":
    print('start')
    run_part1()
    run_part1_with_animation()
    run_part2()
    print('end')

