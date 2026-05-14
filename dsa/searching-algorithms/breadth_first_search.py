"""
Breadth-first search (BFS) explores nodes level by level using a queue.

This file shows two common BFS patterns:
- traversing a binary tree in level order
- traversing a graph from a starting vertex

BFS is useful when you want the shortest path in an unweighted graph or a
layer-by-layer view of a tree structure.

Real-world examples include:
- finding the shortest route in a map or transit network with equal edge costs
- social network features like "people you may know"
- crawling web pages one level at a time
- checking connected components in graphs

Use BFS when you need to explore everything nearest to the starting point first,
or when the problem asks for the shortest path in an unweighted graph.
"""


from queue import SimpleQueue

def breadth_first_search(self):
    if self.root:
        visited_nodes = []
        bfs_queue = SimpleQueue()
        bfs_queue.put(self.root)
        while not bfs_queue.empty():
            current_node = bfs_queue.get()
            visited_nodes.append(current_node.data)
            if current_node.left:
                bfs_queue.put(current_node.left)
            if current_node.right:
                bfs_queue.put(current_node.right)
    return visited_nodes


def breadth_first_search_graph(graph: dict, initial_vertex: int) -> list:
    """Complexity: O(V + E)
       - V: number of vertices
       - E: number of edges
    """
    visited_vertices = []
    bfs_queue = SimpleQueue()
    bfs_queue.put(initial_vertex)
    visited_vertices.append(initial_vertex)
    while not bfs_queue.empty():
        current_vertex = bfs_queue.get()
        for djacent_vertex in graph[current_vertex]:
            if djacent_vertex not in visited_vertices:
                visited_vertices.append(djacent_vertex)
                bfs_queue.put(djacent_vertex)
    return visited_vertices 


graph = {
  '4' : ['6','7'],
  '6' : ['4', '7', '8'],
  '7' : ['4', '6', '9'],
  '8' : ['6', '9'],
  '9' : ['7', '8']
}