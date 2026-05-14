"""
Sequence of data connected through links.
Each element is called a node.
Each node has data and a pointer to the next node.
First node  --> Head
Last node   --> Tail

If each node has 1 link                       --> singly linked list
Each node has two links in either direction   --> doubly linked list


Can be used to implement other data structures:
 - stacks
 - queues
 - graphs
 
Access information by navigating backward and forward
 - web browser
 - music playlist
"""

# Linked lists - Node class

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

# Linked lists - LinkedList class

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.tail = new_node
            self.head = new_node
            
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
            
    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            else:
                current_node = current_node.next
        return False
    

sushi_preparation = LinkedList()
print(sushi_preparation.insert_at_end("prepare"),
      sushi_preparation.insert_at_end("end"),
      sushi_preparation.insert_at_beginning("assemble"),
      sushi_preparation.search("roll"),
      sushi_preparation.search("mixing"),
      sushi_preparation.head)