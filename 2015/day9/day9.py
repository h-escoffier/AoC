# AoC 2015 - Day9


from itertools import permutations
import networkx as nx 
import matplotlib.pyplot as plt


def readInput(path): 
    with open(path) as f: 
        content = [line.rstrip().split(" ") for line in f.readlines()]
    return content


def updateGraph(graph, nodes, weight): 
    graph.add_edge(nodes[0], nodes[1], weight=weight)
    return graph


def drawGraph(graph): 
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos, node_size = 500)
    nx.draw_networkx_labels(graph, pos)
    nx.draw_networkx_edges(graph, pos)
    plt.show()


def runPart1(): 
    lines = readInput('2015/data/input_day9.txt')
    # lines = readInput('2015/data/input_test.txt')
    graph = nx.Graph()
    for line in lines: 
        graph = updateGraph(graph, (line[0], line[2]), int(line[4]))
    nodes = list(graph.nodes)
    minWeight = 9999
    for perm in permutations(nodes): 
        totalWeight = 0 
        for i in range(0, len(perm) - 1): 
            totalWeight += graph[perm[i]][perm[i + 1]]["weight"]
        if minWeight > totalWeight: 
            minWeight = totalWeight
    print(minWeight)
    

def runPart2(): 
    lines = readInput('2015/data/input_day9.txt')
    # lines = readInput('2015/data/input_test.txt')
    graph = nx.Graph()
    for line in lines: 
        graph = updateGraph(graph, (line[0], line[2]), int(line[4]))
    nodes = list(graph.nodes)
    maxWeight = 0
    for perm in permutations(nodes): 
        totalWeight = 0 
        for i in range(0, len(perm) - 1): 
            totalWeight += graph[perm[i]][perm[i + 1]]["weight"]
        if maxWeight < totalWeight: 
            maxWeight = totalWeight
    print(maxWeight)


if __name__ == '__main__': 
    print('start')
    runPart1()
    runPart2()
    print('end')