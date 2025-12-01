# Day6 - AoC 2024 


import numpy as np 
from tqdm import tqdm
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import itertools
import matplotlib.colors as mcolors
import matplotlib.cm as cm



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


def animate_movement(data, guard_start, direction_start):
    fig, ax = plt.subplots()
    ax.set_xticks([])  # Remove x-axis ticks
    ax.set_yticks([])  # Remove y-axis ticks
    ax.set_xticklabels([])  # Remove x-axis labels
    ax.set_yticklabels([])  # Remove y-axis labels

    # Create the grid based on the input data
    grid = np.array([list(row) for row in data])

    # Create a custom colormap with 'obstacles' in red, 'visited' cells in black, and others in white
    cmap = mcolors.ListedColormap(['white', 'red', 'black'])  # White for unvisited, Black for visited, Red for obstacles
    bounds = [0, 0.5, 1, 1.5]  # 0 for unvisited, 1 for visited, 2 for obstacles
    norm = mcolors.BoundaryNorm(bounds, cmap.N)

    # Initialize the grid with zeros (unvisited)
    grid_display = np.zeros_like(grid, dtype=int)

    # Mark obstacles (assuming '#' represents obstacles in the data)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i, j] == '#':  # Assuming obstacles are represented by '#'
                grid_display[i, j] = 2  # Mark obstacles with 2 (red)

    # Show the grid
    im = ax.imshow(grid_display, cmap=cmap, interpolation='nearest')
    list_of_already_visited = [guard_start]

    # Marker for the guard position
    guard_marker, = ax.plot([], [], marker='o', color='black', markersize=5) 
    print(guard_marker)

    def update(frame):
        nonlocal guard_start, direction_start, list_of_already_visited
        guard_start, direction_start, _, _, list_of_already_visited = mouvement(data, guard_start, direction_start, frame, 0, list_of_already_visited)

        # Update the grid (grid of characters for logic, display is handled separately)
        grid = np.array([list(row) for row in data])
        x, y = guard_start
        grid[x, y] = '^'

        # Update the visited cells in the display grid
        for visited_x, visited_y in list_of_already_visited:
            grid_display[visited_x, visited_y] = 1  # Mark as visited (1 for black)


        # Update the guard position
        guard_marker.set_data([y], [x])

        # Update the display grid with the new data
        im.set_data(grid_display)

        return guard_marker, im
    
    # Animation time
    ani = FuncAnimation(fig, update, frames=100, interval=1, blit=False)
    plt.show()


def run_part1_with_animation():
    data = load_data('data/day6_input.txt') 
    guard = find_guard(data)  
    direction = 'up'
    animate_movement(data, guard, direction) 


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
    # print(infinite_loop_positions)
    print(len(infinite_loop_positions)) 
    return infinite_loop_positions


# def read_cyrille_output(file_path): 
#     all_positions_cyrille = []
#     with open(file_path, 'r') as f:
#         for line in f.readlines():
#             x, y = line.strip().split(',')
#             all_positions_cyrille.append((int(y), int(x)))
#     print(len(all_positions_cyrille))
#     return all_positions_cyrille


if __name__ == "__main__":
    print('start')
    # run_part1()
    # run_part1_with_animation()
    run_part2()
    # cyrille_pos = read_cyrille_output('data/serialc_output.txt')
    # diff = False
    # diff_pos = []
    # for pos in cyrille_pos: 
    #     if pos not in loop_position: 
    #         diff = True
    #         diff_pos.append(pos)
    #         # print(pos)
    # if not diff: 
    #     print('No difference')
    # print(len(diff_pos))
    print('end')

