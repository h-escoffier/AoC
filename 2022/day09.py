# Day9 - AoC 2022


def read_input(path): 
    with open(path) as f: 
        content = [line.rstrip().split(" ") for line in f.readlines()]
    return content


def coordinates(previous, direction):
    x, y = previous
    if direction == 'U': 
        return (x, y + 1)
    if direction == 'D': 
        return (x, y - 1)
    if direction == 'R': 
        return (x + 1, y)
    if direction == 'L': 
        return (x - 1, y)
    

def coordinates_tail(head, tail): 
    # superposition 
    if head == tail: 
        return tail
    
    x_h, y_h = head
    x_t, y_t = tail

    directions = ['U', 'R', 'D', 'L', 'UL', 'UR', 'DL', 'DR']
    moves = {'U':  (0, 1),     
             'R':  (1, 0),   
             'D':  (0, -1),    
             'L':  (-1, 0),
             'UR': (1, 1),
             'UL': (-1, 1),
             'DL': (-1, -1),
             'DR': (1, -1)}   

    # one 
    for direction in directions: 
        dx, dy = moves[direction]
        new_x_t, new_y_t = x_t + dx, y_t + dy
        if new_x_t == x_h and new_y_t == y_h: 
            return tail 

    # two 
    directions_complete = ['U', 'R', 'D', 'L', 'RU', 'RD', 'DL', 'DR', 'LU', 'LD', 'UL', 'UR']
    moves = {'U':  (0, 2),     
             'R':  (2, 0),   
             'D':  (0, -2),    
             'L':  (-2, 0),
             'RU': (2, 1),
             'RD': (2, -1),
             'DL': (-1, -2),
             'DR': (1, -2),
             'LU': (-2, 1),
             'LD': (-2, -1),
             'UL': (-1, 2),
             'UR': (1, 2)}   
    for direction in directions_complete: 
        dx, dy = moves[direction]
        new_x_t, new_y_t = x_t + dx, y_t + dy
        if new_x_t == x_h and new_y_t == y_h: 
            if dx == 2: 
                dx = 1
            if dx == -2: 
                dx = -1
            if dy == 2: 
                dy = 1 
            if dy == -2: 
                dy = -1 
            new_x_t, new_y_t = x_t + dx, y_t + dy
            return (new_x_t, new_y_t) 

    print('Error')
    return tail 


def run_part1(path): 
    content = read_input(path)
    head_coord, tail_coord = (0, 0), (0, 0)
    head_coords, tail_coords = [head_coord], [tail_coord]
    for move in content: 
        direction, nb = move 
        # print(direction, nb)
        # print("")
        for _ in range(int(nb)): 
            head_coord = coordinates(head_coord, direction)
            tail_coord = coordinates_tail(head_coord, tail_coord)
            # print('head', head_coord, 'tail', tail_coord)
            head_coords.append(head_coord)
            tail_coords.append(tail_coord)
    visited = []
    # print(tail_coords)
    for elm in tail_coords: 
        if elm not in visited: 
            visited.append(elm)
    print(len(visited))


def coordinates_tail(head, tail): 
    # superposition 
    if head == tail: 
        return tail
    
    x_h, y_h = head
    x_t, y_t = tail

    directions = ['U', 'R', 'D', 'L', 'UL', 'UR', 'DL', 'DR']
    moves = {'U':  (0, 1),     
             'R':  (1, 0),   
             'D':  (0, -1),    
             'L':  (-1, 0),
             'UR': (1, 1),
             'UL': (-1, 1),
             'DL': (-1, -1),
             'DR': (1, -1)}   

    # one 
    for direction in directions: 
        dx, dy = moves[direction]
        new_x_t, new_y_t = x_t + dx, y_t + dy
        if new_x_t == x_h and new_y_t == y_h: 
            return tail 

    # two 
    directions_complete = ['U', 'R', 'D', 'L', 
                           'RU', 'RD', 'DL', 'DR', 'LU', 'LD', 'UL', 'UR', 
                           'TLU', 'TLD', 'TRU', 'TRD']

    moves = {'U':  (0, 2), 'R':  (2, 0), 'D':  (0, -2),'L':  (-2, 0),
             'RU': (2, 1), 'RD': (2, -1), 'DL': (-1, -2), 'DR': (1, -2), 'LU': (-2, 1), 'LD': (-2, -1), 'UL': (-1, 2), 'UR': (1, 2), 
             'TLU': (-2, 2), 'TRU': (2, 2), 'TRD': (2, -2), 'TLD': (-2, -2)}   # New moves
    for direction in directions_complete: 
        dx, dy = moves[direction]
        new_x_t, new_y_t = x_t + dx, y_t + dy
        if new_x_t == x_h and new_y_t == y_h: 
            if dx == 2: 
                dx = 1
            if dx == -2: 
                dx = -1
            if dy == 2: 
                dy = 1 
            if dy == -2: 
                dy = -1 
            new_x_t, new_y_t = x_t + dx, y_t + dy
            return (new_x_t, new_y_t) 

    print('Error')
    return tail 


def run_part2(path): 
    content = read_input(path)
    head_coord = (0, 0)
    t1, t2, t3, t4, t5, t6, t7, t8, t9 = (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)
    head_coords, tail_coords = [head_coord], [t9]
    for move in content: 
        direction, nb = move 
        # print(direction, nb)
        # print("")
        for _ in range(int(nb)): 
            head_coord = coordinates(head_coord, direction)
            t1 = coordinates_tail(head_coord, t1)
            t2 = coordinates_tail(t1, t2)
            t3 = coordinates_tail(t2, t3)
            t4 = coordinates_tail(t3, t4)
            t5 = coordinates_tail(t4, t5)
            t6 = coordinates_tail(t5, t6)
            t7 = coordinates_tail(t6, t7)
            t8 = coordinates_tail(t7, t8)
            t9 = coordinates_tail(t8, t9)
            # print('head', head_coord, 'tail', t1, t2,t3, t4, t5, t6, t7, t8, t9)
            head_coords.append(head_coord)
            tail_coords.append(t9)
    visited = []
    # print(tail_coords)
    for elm in tail_coords: 
        if elm not in visited: 
            visited.append(elm)
    print(len(visited))


if __name__ == '__main__': 
    print('start')
    input_path = '2022/data/input_day09.txt'
    # input_path = '2022/data/input_test.txt'
    
    # Test function
    # print(coordinates_tail((2,4), (4,3)))
    
    run_part1(input_path)
    run_part2(input_path)
    print('end')