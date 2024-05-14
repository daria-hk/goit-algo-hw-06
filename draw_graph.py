import networkx as nx
import matplotlib.pyplot as plt

G = nx.complete_graph(9)
pos = [[0], [1, 2, 3], [4, 5], [6, 7, 8]] 
pos = nx.shell_layout(G, pos)
options = {
    "node_color": "orange",
    "edge_color": "black",
    "node_size": 600,
    "width": 1,
    "with_labels": True
}
nx.draw(G, pos,**options)
plt.title("Transport network of city A")

number_of_nodes = G.number_of_nodes()
number_of_edges = G.number_of_edges()
print(f" Number of nodes: {number_of_nodes}\n Number of edges: {number_of_edges}\n")

plt.show()
