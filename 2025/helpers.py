# Helpers
from collections import deque


# Load a maze from a file
def load_maze(path_file):
    with open(path_file, "r") as file:
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
    """
    Find the start (S) and end (E) points in the maze.
    Returns a tuple of (start_point, end_point) where each point is a tuple (col, row).
    """
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == "S":
                start_pt = (col, row)
            if maze[row][col] == "E":
                end_pt = (col, row)
    return start_pt, end_pt


def maze_to_graph(maze):
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1)
    }

    rows, cols = len(maze), len(maze[0])
    graph = {}
    
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == '#':
                continue
            neighbors = []
            for d, (di, dj) in directions.items():
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and maze[ni][nj] != '#':
                    neighbors.append(((ni, nj), d))
            graph[(i,j)] = neighbors
    return graph


def print_path(maze, path):
    maze_copy = [row[:] for row in maze]  # Create a copy to avoid modifying the original maze
    for i, j in path:
        if maze_copy[i][j] not in ('S','E'):
            maze_copy[i][j] = 'O'
    print_maze(maze_copy)


# Find shortest path algorithm (BFS)
def bfs(graph, start, end, path=None, visited=None):
    # Remove information about the direction 
    graph = {k: [v[0] for v in neighbors] for k, neighbors in graph.items()}

    queue = deque([[start]])  
    visited = set([start])
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node == end:
            return path
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None


# Find shortest path on a weighted graph (Dijkstra)
def dijkstra(graph, start, end, step_cost=1, turn_cost=1000):
    distances = {}
    paths = {}
    
    to_visit = [(0, start[0], start[1], None)]
    paths[(start[0], start[1], None)] = [start]
    
    while to_visit:
        to_visit.sort(key=lambda x: x[0])
        cost, i, j, dir_from = to_visit.pop(0)
        state = (i, j, dir_from)
        
        if state in distances:
            continue
        distances[state] = cost

        if (i,j) == end:
            return paths[state], cost
        
        for (ni, nj), new_dir in graph.get((i,j), []):
            new_cost = cost + step_cost
            if dir_from is not None and dir_from != new_dir:
                new_cost += turn_cost
            new_state = (ni, nj, new_dir)
            if new_state not in distances:
                to_visit.append((new_cost, ni, nj, new_dir))
                paths[new_state] = paths[state] + [(ni, nj)]
    
    return None, float('inf')


if __name__ == "__main__":
    pass
    