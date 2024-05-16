### Conclusions to  draw_graph.py
**Results of Task 1:**
In the given example we have: 
    - nodes= (["A", "B", "C", "D", "E", "F", "G"]) and
    - edges = ("A", "C"), ("A", "C"), ("B", "D"), ("E", "A"), ("C", "E"), ("D", "C"), ("D", "F"), ("C", "G"), ("B", "C")
*  A: ['C', 'E'],
*  B: ['D', 'C'],
*  C: ['A', 'E', 'D', 'G', 'B'],
*  D: ['B', 'C', 'F'],
*  E: ['A', 'C'],
*  F: ['D'],
*  G: ['C'],


    - Number of nodes: 7.
    - Number of edges: 8.


The graph is good connected, which means there is a path between every pair of nodes. There are no isolated components or nodes.

**Results of Task 2**
* dfs algorithm:
  - A C E D B F G 
* bfs algorithm:
  - A C E G D B F 