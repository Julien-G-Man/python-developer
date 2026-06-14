class Node:
    def __init__(self, data: dict):
        self.data = data
        self.next = None
        

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0        
        
    def enqueue(self, data: dict):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
            
    def dequeue(self, data):
        if not self.head:
            self.tail = None
        else:
            current_node = self.head
            self.head = current_node.next
            current_node.next = None
            self.size -= 1
            
            if self.head is None:
                self.tail = None
                
    def display_all(self):
        import json
        current = self.head
        all_nodes = []
        while current:
            all_nodes.append(current.data)
            current = current.next
        return json.dumps(all_nodes, indent=2)

    

student_line = Queue()

students = [
    {'name':'Julien', 'program': 'computer_science'},
    {'name':'Kelvin', 'program': 'mechanical_eng'},
    {'name':'Ali',    'program': 'aerospace_eng'}
]

for std in students:
    student_line.enqueue(std)

print("\nFirst student: ", student_line.head.data)
print("First student's name: ", student_line.head.data.get('name'))
print("Next to first: ", student_line.head.next.data)
print("Queue size: ", student_line.size)
print("All: ", student_line.display_all())
