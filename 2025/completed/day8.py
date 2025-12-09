# Day8 - AoC 2025 


import numpy as np 
import pandas as pd 
import networkx as nx


# Thanks to @ginolhac for the tip about Quick Union algorithm


def read_input(path): 
    with open(path) as f: 
        content = [line.split() for line in f.readlines()]
        new_content, final_content = [], []
        for elm in content: 
            new_content.append(elm[0].split(','))
        for elm in new_content: 
            x, y, z = int(elm[0]), int(elm[1]), int(elm[2])
            final_content.append((x,y,z))
    return final_content


def get_dist(pos1, pos2): 
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    dist = np.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
    return dist


def get_neighbors(content): 
    list_of_dists = []
    for i in range(len(content)): 
        list_of_dist = []
        for j in range(len(content)): 
            if i == j: 
                list_of_dist.append(np.inf)
                continue
            dist = get_dist(content[i], content[j])
            list_of_dist.append(dist)
        list_of_dists.append(list_of_dist)
    return list_of_dists


def closest(list_dist): 
    nb_connection = 0 
    connected = []
    for i in range(len(list_dist)): 
        index_min = list_dist[i].index(min(list_dist[i]))
        # index_min = np.argmin(list_dist[i]).astype(int)
        is_append = False
        for elm in connected: 
            if i in elm or index_min in elm: 
                elm.append(index_min)
                is_append = True
        if not is_append: 
            connected.append([i, index_min])
        nb_connection += 1
        if nb_connection == 10: 
            break 
    return connected


# def closest(list_dist): 
#     nb_connection = 0 
#     connected, already_connected, dist_already_chosen = [], [], []
#     for i in range(len(list_dist)): 
#         min_dist = np.inf
#         for j in range(len(list_dist)):
#             for dist in list_dist[j]: 
#                 if dist < min_dist: 
#                     index_min = list_dist[j].index(min(list_dist[j]))
#                     if dist in dist_already_chosen: 
#                         # print(dist)
#                         continue
#                     else: 
#                         selected_j = j 
#                         selected_index_min = index_min
#                         min_dist = dist
#                         # print(selected_i, selected_index_min, dist)      
#         j = selected_j
#         index_min = selected_index_min
#         print(selected_index_min, selected_j, min_dist)
#         dist_already_chosen.append(min_dist)
#         already_connected.append([i, index_min])
#         # index_min = np.argmin(list_dist[i]).astype(int)
#         is_append = False
#         for elm in connected: 
#             if i in elm: 
#                 elm.append(index_min)
#                 is_append = True
#             elif index_min in elm: 
#                 elm.append(i)
#                 is_append = True
#         if not is_append: 
#             connected.append([i, index_min])
#         # print(connected)
#         nb_connection += 1
#         if nb_connection == 10: 
#             break 
#     return connected


def find_shortest(connected): 
    df = pd.DataFrame(connected)
    grah = nx.Graph()
    for i in range(len(connected)):
        grah.add_node(i)
    # print(grah)
    while grah.number_of_edges() < 1000: 
        # print(connected)
        # min_dist = df.idxmin()
        s = df.stack()
        # min_dist = s.min()
        i, j = s.idxmin()
        # print(i,j)
        grah.add_edge(i,j)
        df.iloc[i,j] = np.inf
        df.iloc[j,i] = np.inf
        # print(grah)
    return grah
    

def run_part1(): 
    content = read_input('2025/data/input_day8.txt')
    # content = read_input('2025/data/input_test.txt')
    list_of_dists = get_neighbors(content)
    graph = find_shortest(list_of_dists)
    all_len = [len(c) for c in sorted(nx.connected_components(graph), key=len, reverse=True)]
    sum_part1 = all_len[0] * all_len[1] * all_len[2]
    print(sum_part1)


# Part2 
def until_is_complete(connected): 
    df = pd.DataFrame(connected)
    grah = nx.Graph()
    for i in range(len(connected)):
        grah.add_node(i)
    # print(grah)
    while True: 
        # print(connected)
        # min_dist = df.idxmin()
        s = df.stack()
        # min_dist = s.min()
        i, j = s.idxmin()
        # print(i,j)
        grah.add_edge(i,j)
        df.iloc[i,j] = np.inf
        df.iloc[j,i] = np.inf
        total = [len(c) for c in sorted(nx.connected_components(grah), key=len, reverse=True)]
        # print(f"{total[0]}/{len(connected)}")
        if total[0] == len(connected): 
            break
    return i, j 


def run_part2():
    content = read_input('2025/data/input_day8.txt')
    # content = read_input('2025/data/input_test.txt')
    list_of_dists = get_neighbors(content)
    i, j = until_is_complete(list_of_dists)
    # print(f"Last connection between {i} and {j}")
    print(content[i][0] * content[j][0])


if __name__ == '__main__': 
    print('start')
    run_part1()
    run_part2()
    print('end')
