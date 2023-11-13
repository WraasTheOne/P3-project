import matplotlib.pyplot as plt
import networkx as nx

# Your graph and start/goal nodes
graph = {
    (0, 0): {},
    (0, 1): {},
    (0, 2): {},
    (0, 3): {},
    (0, 4): {(1,4):1},
    (0, 5): {(0,4):1},
    (0, 6): {(0,5):1},
    (0, 7): {(0,6):1},
    (0, 8): {(0,7):1},
    (0, 9): {(0,7):1},
    (0, 10): {(0,9):1},
    (0, 11): {(0,10):1},
    (0, 12): {},
    (0, 13): {},
    (0, 14): {},
    (0, 15): {},
    (1, 0): {},
    (1, 1): {},
    (1, 2): {},
    (1, 3): {},
    (1, 4): {(2,4):1},
    (1, 5): {(1,6):1},
    (1, 6): {(1,7):1},
    (1, 7): {(1,8):1},
    (1, 8): {(1,9):1},
    (1, 9): {(1,10):1},
    (1, 10): {(2,10):1},
    (1, 11): {(0,11):1},
    (1, 12): {},
    (1, 13): {},
    (1, 14): {},
    (1, 15): {},
    (2, 0): {},
    (2, 1): {},
    (2, 2): {},
    (2, 3): {},
    (2, 4): {(3,4):1},
    (2, 5): {(1,5):1},
    (2, 6): {},
    (2, 7): {},
    (2, 8): {},
    (2, 9): {},
    (2, 10): {(3,10):1},
    (2, 11): {(1,11):1},
    (2, 12): {},
    (2, 13): {},
    (2, 14): {},
    (2, 15): {},
    (3, 0): {},
    (3, 1): {},
    (3, 2): {},
    (3, 3): {},
    (3, 4): {(4,4):1},
    (3, 5): {(2,5):1},
    (3, 6): {},
    (3, 7): {},
    (3, 8): {},
    (3, 9): {},
    (3, 10): {(4,10):1},
    (3, 11): {(2,11):1},
    (3, 12): {},
    (3, 13): {},
    (3, 14): {},
    (3, 15): {},
    (4, 0): {},
    (4, 1): {},
    (4, 2): {(5,2):1},
    (4, 3): {(4,2):1},
    (4, 4): {(4,3):1,(5,4):1},
    (4, 5): {(4,4):1,(3,5):1},
    (4, 6): {},
    (4, 7): {},
    (4, 8): {(5,8):1},
    (4, 9): {(4,8):1},
    (4, 10): {(4,9):1,(5,10):1},
    (4, 11): {(4,10):1,(3,11):1},
    (4, 12): {(4,11):1},
    (4, 13): {(4,12):1},
    (4, 14): {},
    (4, 15): {},
    (5, 0): {},
    (5, 1): {},
    (5, 2): {(6,2):1},
    (5, 3): {(5,4):1},
    (5, 4): {(6,4):1,(5,5):1},
    (5, 5): {(4,5):1},
    (5, 6): {},
    (5, 7): {},
    (5, 8): {(6,8):1},
    (5, 9): {(5,10):1},
    (5, 10): {(5,11):1},
    (5, 11): {(4,11):1,(5,12):1},
    (5, 12): {(6,12):1},
    (5, 13): {(4,13):1},
    (5, 14): {},
    (5, 15): {},
    (6, 0): {},
    (6, 1): {(6,0):1},
    (6, 2): {(6,1):1,(7,2):1},
    (6, 3): {(6,2):1,(5,3):1},
    (6, 4): {(7,4):1},
    (6, 5): {(5,5):1},
    (6, 6): {},
    (6, 7): {},
    (6, 8): {},
    (6, 9): {},
    (6, 10): {},
    (6, 11): {},
    (6, 12): {},
    (6, 13): {},
    (6, 14): {},
    (6, 15): {},
    (7, 0): {},
    (7, 1): {},
    (7, 2): {},
    (7, 3): {},
    (7, 4): {},
    (7, 5): {},
    (7, 6): {},
    (7, 7): {},
    (7, 8): {},
    (7, 9): {},
    (7, 10): {},
    (7, 11): {},
    (7, 12): {},
    (7, 13): {},
    (7, 14): {},
    (7, 15): {},
    (8, 0): {},
    (8, 1): {},
    (8, 2): {},
    (8, 3): {},
    (8, 4): {},
    (8, 5): {},
    (8, 6): {},
    (8, 7): {},
    (8, 8): {},
    (8, 9): {},
    (8, 10): {},
    (8, 11): {},
    (8, 12): {},
    (8, 13): {},
    (8, 14): {},
    (8, 15): {},
    (9, 0): {},
    (9, 1): {},
    (9, 2): {},
    (9, 3): {},
    (9, 4): {},
    (9, 5): {},
    (9, 6): {},
    (9, 7): {},
    (9, 8): {},
    (9, 9): {},
    (9, 10): {},
    (9, 11): {},
    (9, 12): {},
    (9, 13): {},
    (9, 14): {},
    (9, 15): {},
    (10, 0): {},
    (10, 1): {},
    (10, 2): {},
    (10, 3): {},
    (10, 4): {},
    (10, 5): {},
    (10, 6): {},
    (10, 7): {},
    (10, 8): {},
    (10, 9): {},
    (10, 10): {},
    (10, 11): {},
    (10, 12): {},
    (10, 13): {},
    (10, 14): {},
    (10, 15): {},
    (11, 0): {},
    (11, 1): {},
    (11, 2): {},
    (11, 3): {},
    (11, 4): {},
    (11, 5): {},
    (11, 6): {},
    (11, 7): {},
    (11, 8): {},
    (11, 9): {},
    (11, 10): {},
    (11, 11): {},
    (11, 12): {},
    (11, 13): {},
    (11, 14): {},
    (11, 15): {}
}

start_node = (0, 0)
goal_node = (3, 1)

# Updated path
path = [(0, 0), (0, 1), (1, 1), (2, 1), (3, 1)]

# Filter the path to include only nodes that are in the graph
filtered_path = [node for node in path if node in graph]

# Create a NetworkX DiGraph (Directed Graph)
G = nx.DiGraph()

for node, neighbors in graph.items():
    G.add_node(node)
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Draw the graph
pos = {node: (node[1], -node[0]) for node in G.nodes()}  # Adjust coordinates for visualization

plt.figure(figsize=(8, 8))
nx.draw_networkx(G, pos, with_labels=False, node_color='white', node_size=500, font_size=10, font_color='black')

# Mark the start and goal nodes
start_color = 'green'
goal_color = 'green'
node_colors = ['black' if node not in (start_node, goal_node) else start_color if node == start_node else goal_color for node in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=500)

# Draw the path with arrowheads
path_edges = [(filtered_path[i], filtered_path[i + 1]) for i in range(len(filtered_path) - 1)]
path_colors = ['red' for _ in path_edges]
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='green', width=2, arrowsize=20)

plt.axis('off')
plt.show()
