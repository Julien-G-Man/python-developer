"""
Trees are hierarchical data structures with nodes and edges. 
Root has no parent; leaves have no children.
Graphs generalize trees: any node can connect to any other. Can be directed or undirected, cyclic or acyclic.
Graph is a set of nodes/vertices connected by edges/links

Trees are a special type of graph with a strict hierarchy and no cycles, 
while graphs can be more general and may contain cycles.

Traversals: DFS (depth-first), BFS (breadth-first).
Common uses: file systems, social networks, routing, and dependency resolution.

Binary trees: Each node has at most two children (left, right).
Balanced binary search trees (BSTs) maintain O(log n) search/insert/delete.
Types: Complete, full, perfect, balanced, and degenerate (linked list).
"""

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left_child = left
        self.right_child = right
        
        
node1 = TreeNode("B")
node2 = TreeNode("C")
root_node = TreeNode("A", node1, node2)

class Graph:
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, vertex):
        self.vertices[vertex] = []
        
    def add_edge(self, source, target):
        self.vertices[source].append(target)

graph = Graph()
graph.add_vertex('David')
graph.add_vertex('Mariam')
graph.add_vertex('Martin')

graph.add_edge('David', 'Mariam')
graph.add_edge('David', 'Martin')
graph.add_edge('Mariam', 'Martin')

print(graph.vertices)


class WeightedGraph:
    def __init__(self):
        self.vertices = {}
        
    def add_vertex(self, vertex):
        self.vertices[vertex] = []
        
    def add_edge(self, source, target, weight):
        self.vertices[source].append([target, weight])
