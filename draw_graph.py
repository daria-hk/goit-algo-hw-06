import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

G = nx.Graph()
G.add_nodes_from(["A","B", "C", "D", "E", "F", "G"])
G.add_edges_from([("A", "C"), ("A", "C"), ("B", "D"), ("E", "A"), ("C", "E"), ("D", "C"), ("D", "F"), ("C", "G"), ("B", "C")])

options = {
    "node_color": "orange",
    "edge_color": "black",
    "node_size": 600,
    "width": 1,
    "with_labels": True
}
nx.draw(G,**options)
plt.title("Transport network betwen neighbor cities")

number_of_nodes = G.number_of_nodes()
number_of_edges = G.number_of_edges()
print(f" Number of nodes: {number_of_nodes}\n Number of edges: {number_of_edges}\n")
plt.show()


#Task 2#

graph = {node: list(neighbors) for node, neighbors in G.adjacency()}
print('Graph:')
for node, neighbors in graph.items():
    print(f"  {node}: {neighbors},")

def dfs_iterative(graph, start_vertex):
    visited = set()
    stack = [start_vertex]
    print('dfs algorithm:') 

    while stack:
        vertex = stack.pop()  
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            stack.extend(reversed(graph[vertex]))  

dfs_iterative(graph, 'A')
print('\n')


def bfs_iterative(graph, start):
    visited = set()
    queue = deque([start])
    print('bfs algorithm:') 
    while queue:  
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)

    return visited  

bfs_iterative(graph, 'A')
