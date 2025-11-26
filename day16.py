# Day16 - AoC 2024 


import heapq


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


def print_path(maze, path):
    maze_copy = [row[:] for row in maze]  # Create a copy to avoid modifying the original maze
    for y, x in path:
        maze_copy[x][y] = "O"
    print_maze(maze_copy)


def find_all_paths(maze, start_pt, end_pt, best_score):
    maze[start_pt[1]][start_pt[0]] = "."
    maze[end_pt[1]][end_pt[0]] = "."
    best_score_container = [best_score]  
    def dfs(current_path, visited):
        current = current_path[-1]
        # If the end is reached, store the path
        current_score = calcul_score_path(current_path)
        if current_score > best_score_container[0]:
            # print('Score too high, current best score:', best_score_container[0])
            return
        elif current == end_pt:
            all_paths.append(list(current_path))
            best_score_container[0] = current_score
            print(best_score_container[0])
            return
        current_col, current_row = current
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # UP, RIGHT, DOWN, LEFT
        for d_col, d_row in directions:
            new_col, new_row = current_col + d_col, current_row + d_row
            new_pos = (new_col, new_row)
            if (0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and 
                maze[new_row][new_col] == "." and new_pos not in visited):
                visited.add(new_pos)
                current_path.append(new_pos)
                dfs(current_path, visited)
                # Backtrack
                current_path.pop()
                visited.remove(new_pos)
    all_paths = []

    dfs([start_pt], {start_pt})
    return all_paths


def find_s_and_e(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == "S":
                start_pt = (col, row)
            if maze[row][col] == "E":
                end_pt = (col, row)
    return start_pt, end_pt


def calcul_score_path(path):
    nb_steps = len(path)
    cost_turns = 0 
    direction = '>'
    old_pos = path[0]
    for pos in path[1:]: 
        is_change, new_direction = is_direction_change(old_pos, pos, direction)
        if is_change:
            # print('Change')
            # nb_rotation = count_rotations(direction, new_direction)
            # print(nb_rotation)
            cost_turns = cost_turns + (1000)
        old_pos = pos
        direction = new_direction
    return nb_steps + cost_turns
        

# def count_rotations(old_direction, new_direction):
#     directions = {">": 0, "^": 1, "<": 2, "v": 3}
#     return (directions[new_direction] - directions[old_direction]) % 4


def is_direction_change(old_pos, new_pos, dir):
    old_y, old_x = old_pos
    new_y, new_x = new_pos
    if new_y > old_y:
        new_dir = 'v'
    elif new_y < old_y:
        new_dir = '^'
    elif new_x > old_x:
        new_dir = '>'
    elif new_x < old_x:
        new_dir = '<'
    if new_dir == dir:
        return False, new_dir
    else:
        return True, new_dir


def dijkstra_algo(maze, start, end):
    directions = [(-1,0,'U'), (1,0,'D'), (0,-1,'L'), (0,1,'R')]
    rows, cols = len(maze), len(maze[0])
    visited = set()
    heap = []

    # (score, x, y, previous_direction)
    heapq.heappush(heap, (0, start[0], start[1], (0,1,'R')))

    while heap:
        score, x, y, prev_dir = heapq.heappop(heap)
        if (x, y, prev_dir) in visited:
            continue
        visited.add((x, y, prev_dir))

        if (x, y) == end:
            return score

        for dx, dy, dir_label in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != '#':
                if prev_dir is None or dir_label == prev_dir:
                    new_score = score + 1
                else:
                    new_score = score + 1001
                heapq.heappush(heap, (new_score, nx, ny, dir_label))
    return float('inf') 


# def run_part1():
#     maze = load_data("data/day16_input.txt")
#     # maze = load_data("data/input_test.txt")
#     best_score = np.inf
#     start, end = find_s_and_e(maze)
#     paths = find_all_paths(maze, start, end, best_score)
#     print(len(paths))
#     print('')
#     for path in tqdm(iterable=paths, desc='Progress Report - Part 1'):
#         score = calcul_score_path(path)
#         if score < best_score:
#             best_score = score
#             best_path = path
#     print(best_score - 1)
#     print('')
#     print_path(maze, best_path)


def run_part1():
    maze = load_data("data/day16_input.txt")
    # maze = load_data("data/input_test.txt")
    # print_maze(maze)
    start, end = find_s_and_e(maze)
    best_score = dijkstra_algo(maze, start, end)
    print(best_score)  


if __name__ == "__main__":
    print('start')
    run_part1()  
    print('end')