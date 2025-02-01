import networkx as nx
from itertools import product

def isin(x, y):
    return 0 <= x < xmax and 0 <= y < ymax


with open('2024/input/18.txt') as fr:
    corrupted = [tuple(map(int, row.split(','))) for row in fr.readlines()]
    corrupted_set = set(corrupted)

xmax = ymax = 70 + 1

def create_graph(xmax, ymax, corrupted_set):
    nodes = {f'{x}_{y}': (x, y) for x, y in product(range(xmax), range(ymax)) if (x, y) not in corrupted_set}
    edges = [(f'{x}_{y}', f'{x + xm}_{y + ym}') 
             for x, y in product(range(xmax), range(ymax)) if (x, y) not in corrupted_set 
             for xm, ym in [[0, 1], [0, -1], [-1, 0], [1, 0]] if isin(x + xm, y + ym) and (x + xm, y + ym) not in corrupted_set]

    G = nx.Graph()
    G.add_nodes_from(nodes.keys())
    nx.set_node_attributes(G, nodes, 'coords')
    G.add_edges_from(edges)
    return G

part_1 = nx.shortest_path_length(create_graph(xmax, ymax, set(corrupted[:1024])), '0_0', f'{xmax - 1}_{ymax - 1}')

G = create_graph(xmax, ymax, corrupted_set)

i = 1
while True:
    try:
        nx.shortest_path_length(G, '0_0', f'{xmax - 1}_{ymax - 1}')
        break
    except nx.NetworkXNoPath:
        x, y = corrupted[-i]
        corrupted_set.discard((x, y))
        G.add_node(f'{x}_{y}', coords=(x, y))
        for xm, ym in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
            if isin(x + xm, y + ym) and (x + xm, y + ym) not in corrupted_set:
                G.add_edge(f'{x}_{y}', f'{x + xm}_{y + ym}')
        i += 1

print(f'{part_1=}')
print(f'part_2: {x},{y}')