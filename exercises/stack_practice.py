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
        if not self.top:
            return None
        current_node = self.top
        self.top = self.top.next
        current_node.next = None
        return current_node.data
        
        
    def peek(self):
        if not self.top:
            return None
        return self.top.data
    
    
