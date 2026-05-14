"""
Towers of Hanoi
In this exercise, you will implement the Towers of Hanoi puzzle with a recursive algorithm. The aim of this game is to transfer all the disks from one of the three rods to another, following these rules:

 - You can only move one disk at a time.
 - You can only take the upper disk from one of the stacks and place it on top of another stack.
 - You cannot put a larger disk on top of a smaller one.
"""
def hanoi(num_disks, from_rod, to_rod, aux_rod):
    if num_disks >= 1:
        hanoi(num_disks - 1, from_rod, aux_rod, to_rod)
        print("Moving disk", num_disks, "from rod", from_rod,"to rod",to_rod)
        hanoi(num_disks - 1, aux_rod, to_rod, from_rod)   

num_disks = 4
source_rod = 'A'
auxiliar_rod = 'B'
target_rod = 'C'

hanoi(num_disks, source_rod, target_rod, auxiliar_rod)