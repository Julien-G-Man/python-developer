"""
Queues and Stacks are both data structures that can hold a collection of items. 
They both aren’t built into Python, but we can leverage Python’s built-in data structures, such as lists, to create them. 
We’ll be using node definitions to implement them
The difference between the two is that a queue stores items in a first-in, first-out (FIFO) format
whereas stack stores items in a last-in, first-out (LIFO) format
"""

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

# --- QUEUE: First-In, First-Out (FIFO) ---
class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.size = 0
        self.max_size = max_size
  
    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)
            print(f"Adding {item_to_add.get_value()} to the queue!")
            if self.is_empty():
                self.head = self.tail = item_to_add                
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print("Sorry, no more room!")
       
    def dequeue(self):
        if not self.is_empty():
            item_to_remove = self.head
            print(f"{item_to_remove.get_value()} is served!")
            if self.size == 1:
                self.head = self.tail = None
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("The queue is totally empty!")
  
    def peek(self):
        if not self.is_empty():
            return self.head.get_value()
        print("No orders waiting!")
        return None

    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0

    def has_space(self):
        if self.max_size is None:
            return True
        return self.max_size > self.size

# --- STACK: Last-In, First-Out (LIFO) ---
class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.size = 0
        self.limit = limit
        
    def push(self, value):
        if self.has_space(): 
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            print("All out of space!")
            
    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("This stack is totally empty.")
            return None
                
    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        print("Nothing to see here!")
        return None
  
    def is_empty(self):
        return self.size == 0

    def has_space(self):
        return self.limit > self.size


# --- TEST EXECUTION ---

print("Creating a deli line with up to 10 orders...\n------------")
deli_line = Queue(10)
orders = [
    "egg and cheese", "bacon egg and cheese", "toasted bagel", 
    "roll with butter", "plain bagel", "two fried eggs", 
    "jalapeno egg and cheese", "cream cheese bagel", 
    "muffin", "bacon bagel", "western omelet"
]

for order in orders:
    deli_line.enqueue(order)

print(f"------------\nOur first order will be: {deli_line.peek()}")
print("------------\nNow serving...\n------------")

while not deli_line.is_empty():
    deli_line.dequeue()