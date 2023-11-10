import matplotlib.pyplot as plt
import networkx as nx

# Your graph and start/goal nodes
graph = {
    (0, 0): {(0, 1): 1, (1, 0): 1},
    (0, 1): {(0, 0): 1, (0, 2): 1, (1, 1): 1},
    (0, 2): {(0, 1): 1, (0, 3): 1, (1, 2): 1},
    (0, 3): {(0, 2): 1, (0, 4): 1, (1, 3): 1},
    (0, 4): {(0, 3): 1, (1, 4): 1},

    (1, 0): {(0, 0): 1, (1, 1): 1, (2, 0): 1},
    (1, 1): {(0, 1): 1, (1, 0): 1, (1, 2): 1, (2, 1): 1},
    (1, 2): {(0, 2): 1, (1, 1): 1, (1, 3): 1, (2, 2): 1},
    (1, 3): {(0, 3): 1, (1, 2): 1, (1, 4): 1, (2, 3): 1},
    (1, 4): {(0, 4): 1, (1, 3): 1, (2, 4): 1},

    (2, 0): {(1, 0): 1, (2, 1): 1, (3, 0): 1},
    (2, 1): {(1, 1): 1, (2, 0): 1, (2, 2): 1, (3, 1): 1},
    (2, 2): {(1, 2): 1, (2, 1): 1, (2, 3): 1, (3, 2): 1},
    (2, 3): {(1, 3): 1, (2, 2): 1, (2, 4): 1, (3, 3): 1},
    (2, 4): {(1, 4): 1, (2, 3): 1, (3, 4): 1},

    (3, 0): {(2, 0): 1, (3, 1): 1, (4, 0): 1},
    (3, 1): {(2, 1): 1, (3, 0): 1, (3, 2): 1, (4, 1): 1},
    (3, 2): {(2, 2): 1, (3, 1): 1, (3, 3): 1, (4, 2): 1},
    (3, 3): {(2, 3): 1, (3, 2): 1, (3, 4): 1, (4, 3): 1},
    (3, 4): {(2, 4): 1, (3, 3): 1, (4, 4): 1},

    (4, 0): {(3, 0): 1, (4, 1): 1},
    (4, 1): {(3, 1): 1, (4, 0): 1, (4, 2): 1},
    (4, 2): {(3, 2): 1, (4, 1): 1, (4, 3): 1},
    (4, 3): {(3, 3): 1, (4, 2): 1, (4, 4): 1},
    (4, 4): {(3, 4): 1, (4, 3): 1}
}

start_node = (0, 0)
goal_node = (4, 4)
path = [(0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (4, 4)]

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
path_colors = ['green' for _ in path_edges]
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='green', width=2, arrowsize=20)


plt.axis('off')
plt.show()
