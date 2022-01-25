#How to create Nodes
# ! Classs defined 
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(13)
b = Node(15)
a.next = b 
print(a.data) #? 13
print(b.data) #? 15
print(a.next.data) #? 15
print(a.next)
print(b.next)