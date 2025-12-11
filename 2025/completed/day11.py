# Day11 - AoC 2025 


import networkx as nx 
from tqdm import tqdm 
import matplotlib.pyplot as plt
from pyvis.network import Network


def read_input(path):
    with open(path) as f: 
        content = [line.strip() for line in f.readlines()]
    new_content = []
    for line in content: 
        node = line.split(':')[0]
        node_to = line.split(':')[1].split(' ')
        node_to.pop(0)
        new_content.append([node, node_to])
    return new_content


# Part1
def create_graph(content):
    graph = dict()
    for elm in content: 
        graph.update({elm[0]: elm[1]})
    return graph


def dfs(graph, pos, end, path, all_paths): 
    path.append(pos)
    if pos == end: 
        all_paths.append(path.copy())
    else: 
        for adj in graph.get(pos): 
            dfs(graph, adj, end, path, all_paths)
    path.pop()


def run_part1(): 
    content = read_input('2025/data/input_day11.txt')
    # content = read_input('2025/data/input_test.txt')
    graph = create_graph(content)
    # Init DFS
    path, all_path = [], [] 
    start = 'you'
    end = 'out'
    dfs(graph, start, end, path, all_path)
    print(len(all_path))


# Part2
def pass_through(all_path): 
    counter = 0 
    for path in tqdm(all_path): 
        if 'fft' in path and 'dac' in path: 
            counter += 1 
    return counter


def all_path_from_to(graph, init_start, init_end, forbidden):
    path, all_path = [], [] 
    start = init_start
    end = init_end
    
    update_graph = dict()
    for key, values in graph.items(): 
        if key not in forbidden: 
            new_values = []
            for elm in values: 
                if elm not in forbidden: 
                    new_values.append(elm)
            update_graph.update({key : new_values})
    dfs(update_graph, start, end, path, all_path)
    return all_path


def create_networkx_graph(content): 
    graph = nx.DiGraph()
    for elm in content: 
        graph.add_node(elm[0])
        for node in elm[1]: 
            graph.add_edge(elm[0], node)
    return graph


def plot_the_graph(graph): 
    g = Network(notebook=True)
    g.from_nx(graph)
    g.show('figures/day11_graph.html')
    # Nodes have been colored manually 


def calcul_final_output(output_graph): 
    paths = nx.all_simple_paths(output_graph, 'svr', 'out')
    total = 0 
    for path in map(nx.utils.pairwise, paths):
        nb_paths = 1
        for edge in path: 
            weight = output_graph.get_edge_data(edge[0], edge[1]).get('weight')
            nb_paths = nb_paths*weight
        total += nb_paths
    return total 
    

def run_part2(): 
    content = read_input('2025/data/input_day11.txt')
    # content = read_input('2025/data/input_test.txt')
    graph = create_graph(content)
     
    # nx_graph = create_networkx_graph(content)
    # plot_the_graph(nx_graph)

    # Build a weighted graph with the number of paths as weights
    output_graph = nx.DiGraph()
    output_graph.add_node('svr')
    graph.update({'out': []})
    nb_path = []

    # 1 

    first_stop = ['tim', 'ejm', 'qad', 'ony', 'gcp']
    for i in range(len(first_stop)):
        elm = first_stop[i]
        output_graph.add_node(elm)
        other_stops = []
        for j in range(len(first_stop)): 
            if i != j: 
                other_stops.append(first_stop[j])
        nb_path = len(all_path_from_to(graph, 'svr', elm, other_stops))
        output_graph.add_edge('svr', elm, weight=nb_path)

    # 2 

    second_stop = ['nno', 'idq', 'vpw', 'dsj', 'uur']
    for start in first_stop: 
        for i in range(len(second_stop)): 
            elm = second_stop[i]
            other_stops = []
            for j in range(len(second_stop)): 
                if i != j: 
                    other_stops.append(second_stop[j])          
            paths = all_path_from_to(graph, start, elm, other_stops)
            weight = 0
            for path in paths: 
                if 'fft' in path: 
                    weight += 1 
            if weight != 0:         
                output_graph.add_node(elm)            
                output_graph.add_edge(start, elm, weight=weight)

    # 3 

    third_stop = ['nqc', 'qsv', 'gzw', 'oeh']
    for start in second_stop: 
        for i in range(len(third_stop)): 
            elm = third_stop[i]
            output_graph.add_node(elm)
            other_stops = []
            for j in range(len(third_stop)): 
                if i != j: 
                    other_stops.append(third_stop[j])          
            nb_path = len(all_path_from_to(graph, start, elm, other_stops))
            output_graph.add_edge(start, elm, weight=nb_path)

    # 4 

    fourth_stop = ['kgc', 'wsv', 'hav', 'sar']
    for start in third_stop: 
        for i in range(len(fourth_stop)): 
            elm = fourth_stop[i]
            output_graph.add_node(elm)
            other_stops = []
            for j in range(len(fourth_stop)): 
                if i != j: 
                    other_stops.append(fourth_stop[j])          
            nb_path = len(all_path_from_to(graph, start, elm, other_stops))
            output_graph.add_edge(start, elm, weight=nb_path)
    
    # Final 
    for start in fourth_stop: 
        output_graph.add_node('out')
        paths = all_path_from_to(graph, start, 'out', [])
        weight = 0 
        for path in paths: 
            if 'dac' in path: 
                weight += 1 
        if weight != 0:       
            output_graph.add_node(elm)            
            output_graph.add_edge(start, 'out', weight=weight)
    
    total = calcul_final_output(output_graph)
    print(total)


if __name__ == '__main__': 
    print('start')
    run_part1()
    run_part2()
    print('end')

