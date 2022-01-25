class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        
def PrintList(head):
        cur = head
        while cur != None:
            print(cur.key)
            cur = cur.next 
def search(head, x):
    pos =1
    curr = head
    while curr != None:
        if curr.key == x:
            return pos
        pos = pos + 1
        curr = curr.next
    return -1                    
                
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
x=30
print(search(head, x))
print(PrintList(head))