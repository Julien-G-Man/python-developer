"""
Stacks are Last-In-First-Out (LIFO) data structures.
Basic operations: push (add), pop (remove), and peek (view item at the top) — all O(1).
Common uses: function call stacks (managing calls and returns), undo mechanisms, DFS traversal, 
and expression evaluation.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        
    def push(self, data):
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node
           
    def pop(self):
        if self.top is None:
            return None
        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None
        return popped_node.data
        
    def peek(self):
        if self.top:
            return self.top.data
        return None
    
    
# Using LifoQueue in Python
# - Python's queue module, behaves like a stack

import queue

book_stack = queue.LifoQueue(maxsize=0) # infinit size
book_stack.put("The beginning")
book_stack.put("Persepolis")
book_stack.put("1984")
print("Size: ", book_stack.qsize())
# remove and display elements from last to first
print(book_stack.get())
print(book_stack.get())
print(book_stack.get())
print("Empty stack: ", book_stack.empty())