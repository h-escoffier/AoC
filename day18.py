from tqdm import tqdm


def load_data(path): 
    with open(path, 'r') as file: 
        data = file.readlines()
        data = [x.strip().split(',') for x in data]
    return data


def create_matrix(coords, size, nb_coords): 
    # Initialize the grid with spaces
    matrix = [['_' for _ in range(size)] for _ in range(size)]
    for x, y in coords[: nb_coords]:
        matrix[int(x)][int(y)] = '#'
    return matrix


# # Not working correclty
# def print_matrix(matrix):  
#     for row in matrix: 
#         print(''.join(row))
#     print('')

# # Not working correclty
# def print_path(matrix, path):
#     for y, x in path: 
#         matrix[y][x] = 'O'
#     print_matrix(matrix)


# Take from Stackoverflow : https://stackoverflow.com/questions/59237704/maze-finding-the-shortest-path-from-start-point-to-end-point
def shortest_path(maze):
    ''' Maze Properties'''
    num_rows = len(maze)
    num_cols = len(maze[0])
    end_pt = (num_cols - 1, num_rows - 1)
    start_pt = (0, 0)
    '''BFS'''
    visited = {end_pt: None}
    queue = [end_pt]
    while queue:
        current = queue.pop(0)
        if current == start_pt:
            shortest_path = []
            while current:
                shortest_path.append(current)
                current = visited[current]
            return shortest_path
        adj_points = []
        '''FIND ADJACENT POINTS'''
        current_col, current_row = current
        #UP
        if current_row > 0:
            if maze[current_row - 1][current_col] == "_":
                adj_points.append((current_col, current_row - 1))
        #RIGHT
        if current_col < (len(maze[0]) - 1):
            if maze[current_row][current_col + 1] == "_": 
                adj_points.append((current_col + 1, current_row))
        #DOWN
        if current_row < (len(maze) - 1):
            if maze[current_row + 1][current_col] == "_":
                adj_points.append((current_col, current_row + 1))
        #LEFT
        if current_col > 0:
            if maze[current_row][current_col - 1] == "_":
                adj_points.append((current_col - 1, current_row))

        '''LOOP THROUGH ADJACENT PTS'''
        # for point in adj_points_checked:
        for point in adj_points:
            if point not in visited:
                visited[point] = current
                queue.append(point)


def run_part1(): 
    data = load_data('data/day18_input.txt')
    # matrix = create_matrix(data, 7, 12)
    matrix = create_matrix(data, 71, 1024)
    # print_matrix(matrix)
    short_path = shortest_path(matrix)
    # print(short_path)
    print(len(short_path) - 1)
    print('')
    # print_path(matrix, short_path)
    

def run_part2(): 
    data = load_data('data/day18_input.txt')
    matrix = create_matrix(data, 71, 1024)
    # matrix = create_matrix(data, 7, 12)
    # for i in tqdm(iterable = range(12, len(data) + 1), desc=('Progress Report - Part 2')): 
    for i in range(1024, len(data) + 1):
        matrix = create_matrix(data, 71, i)
        # matrix = create_matrix(data, 7, i)
        short_path = shortest_path(matrix)
        # print(len(short_path) - 1)
        if short_path == None:
            print('No path found')
            print(i)
            print(data[i - 1])
            break 


if __name__ == "__main__": 
    print('start')
    run_part1() 
    run_part2()
    print('end')