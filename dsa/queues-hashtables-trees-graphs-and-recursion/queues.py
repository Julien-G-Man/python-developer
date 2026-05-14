"""
Queues are First-In-First-Out (FIFO) data structures.
Basic operations: enqueue (add) and dequeue (remove) — both are O(1).
Common uses: task scheduling, buffering, print queues, and breadth-first search.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def enqueue(self, data):
        """Add new node to tail"""
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
            
    def dequeue(self):
        """remove node from head"""
        if self.head:
            current_node = self.head
            self.head = current_node.next
            current_node.next = None # hmmm, the tutorial might be wrong here
            # current not is meant to get removed, not it's next cos it's next becomes the head
            self.size -= 1
            
            if self.head == None:
                self.tail = None
        else: 
            self.tail = None
            
    def is_empty(self):
        return False if self.head else True
    
    def display_all(self):
        current = self.head
        all_nodes = []
        while current:
            all_nodes.append(current.data)
            current = current.next
        return all_nodes
    
  
  
queue = Queue()    
for fruit in ["apple", "mango", "banana"]:
    queue.enqueue(fruit)
   
print(queue.display_all()) 
print(queue.size)    
print("Empty: ", queue.is_empty())

# Using SimpleQueue in Python

"""
from queue import SimpleQueue, Queue

orders_queue = SimpleQueue()

print("Enqueueing...")
orders_queue.put("Sushi")
orders_queue.put("Lasagna")
orders_queuse.put("Paella")
print("Size: ", orders_queue.qsize())

print("\nEnqueueing from first to last...") 
print(orders_queue.get())
print(orders_queue.get())
print(orders_queue.get())
print("Empty queue: ", orders_queue.empty())
"""