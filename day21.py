# Day21 - AoC 2024


from collections import deque
import itertools
from tqdm import tqdm


def load_data(path):
    with open(path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines if line.strip()]


def keypad():
    return {
        '7': (0, 0), '8': (0, 1), '9': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '1': (2, 0), '2': (2, 1), '3': (2, 2),
                     '0': (3, 1), 'A': (3, 2)
    }


def directional_keypad():
    return {
        '^': (0, 1), 'A': (0, 2),
        '<': (1, 0), 'v': (1, 1), '>': (1, 2),
    }


def neighbors(pos, valid_positions):
    x, y = pos
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    return [(x+dx, y+dy) for dx, dy in directions if (x+dx, y+dy) in valid_positions]


def from_path_to_moves(path):
    moves = []
    for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]
        if x2 < x1:
            moves.append('^')
        elif x2 > x1:
            moves.append('v')
        elif y2 < y1:
            moves.append('<')
        elif y2 > y1:
            moves.append('>')
    return moves


def bfs_all_shortest_paths(start_key, end_key, kpad):
    start = kpad[start_key]
    goal = kpad[end_key]
    valid_positions = set(kpad.values())
    queue = deque()
    queue.append((start, [start]))
    visited = {start: 0}
    shortest_paths = []
    min_length = None
    while queue:
        current, path = queue.popleft()
        if current == goal:
            if min_length is None:
                min_length = len(path)
            if len(path) == min_length:
                shortest_paths.append(path)
            continue
        for n in neighbors(current, valid_positions):
            if n not in visited or visited[n] >= len(path):
                visited[n] = len(path)
                queue.append((n, path + [n]))
    return shortest_paths


def robot_all_shortest_paths(code, kpad):
    all_sequences = []
    def recurse(i, start_key, current_moves):
        if i == len(code):
            all_sequences.append(current_moves + ['A'])
            return
        end_key = code[i]
        pos_paths = bfs_all_shortest_paths(start_key, end_key, kpad)
        for path in pos_paths:
            moves = from_path_to_moves(path)
            recurse(i + 1, end_key, current_moves + moves + ['A'])
    recurse(0, 'A', [])
    return all_sequences


def keep_shortest(codes):
    min_len = min(len(s) for s in codes)
    return [s for s in codes if len(s) == min_len]


def robot_all_global_shortest_paths(code, keypad_map, directional_map):
    all_paths = []
    start = 'A'
    for end in code:
        paths = bfs_all_shortest_paths(start, end, keypad_map)
        all_paths.append(paths)
        start = end
    sequences = list(itertools.product(*all_paths))
    best_code = None
    best_length = float('inf')
    for seq in sequences:
        moves1 = []
        for segment in seq:
            moves1.extend(from_path_to_moves(segment))
            moves1.append('A')
        code1 = ''.join(moves1)
        code2_options = robot_all_shortest_paths(code1, directional_map)
        code2_options = keep_shortest(code2_options)
        for code2 in code2_options:
            code2_correct_version = code2[:-1]
            code3_options = robot_all_shortest_paths(''.join(code2_correct_version), directional_map)
            code3_options = keep_shortest(code3_options)
            for code3 in code3_options:
                code3_correct_version = code3[:-1]
                l = len(code3_correct_version)
                if l < best_length:
                    best_code = ''.join(code3_correct_version)
                    best_length = l
    return best_code


def run_part1():
    # codes = load_data('data/input_test.txt')
    codes = load_data('data/day21_input.txt')   
    keypad_map = keypad()
    directional_keypad_map = directional_keypad()
    total_complexity = 0
    for code in tqdm(codes, desc='Progress Report - Part 1'):
        result = robot_all_global_shortest_paths(code, keypad_map, directional_keypad_map)
        complexity = len(result) * int(code[:-1])
        total_complexity += complexity
    print(total_complexity)


# Old Approach (Not recurcive using permutations) -> Not working do to the 'gap' problem

# def build_position_lookup(keypad):
#     return {v: k for k, v in keypad.items()}


# def bfs(start_key, end_key, kpad):
#     pos_to_key = build_position_lookup(kpad)
#     start = kpad[start_key]
#     goal = kpad[end_key]
#     visited = set()
#     parent = {}
#     queue = deque([start])
#     visited.add(start)
#     while queue:
#         current = queue.popleft()
#         if current == goal:
#             path = []
#             path_directions = []
#             while current != start:
#                 path.append(pos_to_key[current])
#                 path_directions.append(current)
#                 current = parent[current]
#             path.append(start_key)
#             path_directions.append(start)
#             path.reverse()
#             path_directions.reverse()
#             return path, path_directions
#         for n in neighbors(current, set(kpad.values())):
#             if n not in visited:
#                 visited.add(n)
#                 parent[n] = current
#                 queue.append(n)
#     return None  


# def robot(code, kpad): 
#     full_code = []
#     start = 'A'
#     for i in range(len(code)):
#         end = code[i]
#         path, path_directions = bfs(start, end, kpad)
#         # print(path_directions)
#         # print(path)
#         moves = from_path_to_moves(path_directions)
#         full_code.extend(moves)
#         full_code.append('A')
#         if i + 1 < len(code):
#             start = code[i]
#             end = code[i + 1]
#     # print(full_code)
#     return full_code


# def create_perm_from_code(code): 
#     all_shortest_codes = [[]]
#     sections = code.split('A') 
#     # print(sections)
#     for sec in sections:
#         # print(all_shortest_codes)
#         unique_perms = set(tuple(p) for p in permutations(sec))
#         # print(unique_perms)
#         if len(unique_perms) > 1:
#             new_all_shortest_codes = []
#             for perm in unique_perms:
#                 for code in all_shortest_codes:
#                     new_code = code + list(perm) + ['A']
#                     new_all_shortest_codes.append(new_code)
#             all_shortest_codes = new_all_shortest_codes
#         else:
#             for i in range(len(all_shortest_codes)):
#                 all_shortest_codes[i] = all_shortest_codes[i] + list(sec) + ['A']
#     all_shortest_strings = []
#     for code in all_shortest_codes:
#         # print(len(code))
#         code.pop() # Remove the last 'A'
#         string_code = ''.join(code)
#         all_shortest_strings.append(string_code)
#     return all_shortest_strings


# def sign_with_direction(direction):
#     if direction == 'up':
#         return '^'
#     elif direction == 'down':
#         return 'v'
#     elif direction == 'left':
#         return '<'
#     elif direction == 'right':
#         return '>'
#     else:
#         raise ValueError("Invalid direction")
    

# def run_part1(): 
#     codes = load_data('data/input_test.txt')
#     # codes = load_data('data/day21_input.txt')   
#     total_complexity = 0
#     keypad_map = keypad()
#     directional_keypad_map = directional_keypad()
#     for code in codes: 
#         # First robot 
#         print(code)
#         original_code = code
#         # full_code = robot(code, keypad_map)
#         full_codes = robot_all_shortest_paths(code, keypad_map)
#         full_strings = []
#         for code in full_codes:
#             string_code = ''.join(code)
#             full_strings.append(string_code)
#         print(full_strings)  # All the shortest paths
#         # Second robot 
#         full_strings_r2 = []
#         for code_r2 in full_strings:
#             # print(code_r2)
#             full_codes_r2 = robot_all_shortest_paths(code_r2, directional_keypad_map)
#             for full_code_r2 in full_codes_r2:
#                 string_code_r2 = ''.join(full_code_r2)
#                 full_strings_r2.append(string_code_r2)
#         full_strings_r2 = keep_shortest(full_strings_r2)
#         print(full_strings_r2[0])
#         print('v<<A>>^A<A>AvA<^AA>A<vAAA>^A')
#         print(len('v<<A>>^A<A>AvA<^AA>A<vAAA>^A')) 
#         print(len(full_strings_r2[0]))
#         # Third robot
#         full_strings_r3 = []
#         for code_r3 in full_strings_r2:
#             full_codes = robot_all_shortest_paths(code_r3, directional_keypad_map)
#             for full_code in full_codes:
#                 string_code = ''.join(full_code)
#                 full_strings_r3.append(string_code)
#         full_strings_r3 = keep_shortest(full_strings_r3)
#         print(len(full_strings_r3[0]))
#         break
#         complexity = len(full_strings_r3[0]) * int(original_code[:-1])
#         total_complexity += complexity
#     print('Total complexity:', total_complexity)


if __name__ == "__main__":
    print("start")
    run_part1()
    print("end")
