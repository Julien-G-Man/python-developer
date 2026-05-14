"""
Depth First Search (DFS) explores as far as possible down one path before backtracking.
It can be implemented with recursion or an explicit stack.
Common uses: tree traversal, graph traversal, path finding, and topological sorting.
DFS is usually memory-efficient compared with BFS because it keeps only the current path.
"""


class TreeNode:
    def __init__(self, data, left=None, right=None):
        """Initialize a tree node with data and optional left/right children."""
        self.data = data
        self.left_child = left
        self.right_child = right
        

def in_order(self, current_node):
    """left -> current -> right
    Used in bST to obtain the node's values in ascending order
    """
    if current_node:
        self.in_order(current_node.left_child)
        print(current_node.data)
        self.in_order(current_node.right_child)
        

def pre_order(self, current_node):
    """current -> left -> right
    Used to:
      - create copies of a tree
      - get prefix expressions
    """
    if current_node:
        print(current_node.data)
        self.pre_order(current_node.left_child)
        self.pre_order(current_node.right_child)
        
        
def post_order(self, current_node):
    """left -> right -> current
    Used to:
      - delete binary tree
      - get postfix expressions
    """
    if current_node:
        print(current_node.data)
        self.post_order(current_node.left_child)
        self.post_order(current_node.right_child)
        
        
def depth_first_search(visited_vertices: list, graph: dict, current_vertex):
    """DFS for graphs (with cycles):
    - Keep a visited set/list to avoid revisiting vertices.
    - Start from any vertex and mark it as visited.
    - For each adjacent vertex:
      - If already visited, ignore it.
      - If not visited, recursively perform DFS on it.
    """
    if current_vertex not in visited_vertices:
        print(current_vertex)
        visited_vertices.add(current_vertex)
        for adjacent_vertex in graph[current_vertex]:
            depth_first_search(visited_vertices, graph, adjacent_vertex)