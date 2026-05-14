"""
Binary Search Tree (BST): a binary tree where each node's left subtree contains values
less than the node and the right subtree contains values greater than the node.
When balanced, common operations — search, insert, delete — run in O(log n) time.
Inorder traversal of a BST yields values in sorted order.
Uses: fast searching, ordered data storage, and keeping values sorted for traversal.
Compared with linked lists, BSTs can search faster when balanced, while linked lists are simpler but require linear search.
Compared with arrays, BSTs keep insert/search efficient without shifting elements, but arrays are better for direct indexing.
"""

class TreeNode:
    def __init__(self, data, left=None, right=None):
        """Initialize a tree node with data and optional left/right children."""
        self.data = data
        self.left_child = left
        self.right_child = right
        

class BinarySearchTree:
    def __init__(self):
        """Initialize an empty BST with no root node."""
        self.root = None
        
    def search(self, search_value):
        """Search for a value in the BST. Returns True if found, False otherwise."""
        current_node = self.root
        while current_node:
            if search_value == current_node.data:
                return True
            elif search_value < current_node.data:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        return False
    
    def insert(self, data):
        """Insert a value into the BST at the correct position."""
        new_node = TreeNode(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            current_node = self.root
            while True:
                if data < current_node.data:
                    if not current_node.left_child:
                        current_node.left_child = new_node
                        return
                    current_node = current_node.left_child
                elif data > current_node.data:
                    if not current_node.right_child:
                        current_node.right_child = new_node
                        return
                    current_node = current_node.right_child
                    
    def delete(self, data):
        """Delete a value from the BST by calling the recursive helper on the root."""
        self.root = self._delete_node(self.root, data)
    
    def _delete_node(self, node, data):
        """Recursively delete a node.

        If the value is smaller, keep going left.
        If the value is larger, keep going right.
        If the node has two children, replace it with its successor:
        the smallest value in the right subtree, found by moving right once
        and then following left children until the end.
        """
        if not node:
            return None
        
        if data < node.data:
            node.left_child = self._delete_node(node.left_child, data)
        elif data > node.data:
            node.right_child = self._delete_node(node.right_child, data)
        else:
            if not node.left_child and not node.right_child:
                return None
            if not node.left_child:
                return node.right_child
            if not node.right_child:
                return node.left_child
            successor = node.right_child
            while successor.left_child:
                successor = successor.left_child
            node.data = successor.data
            node.right_child = self._delete_node(node.right_child, successor.data)
        
        return node