class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        
def PrintList(head):
        cur = head
        while cur != None:
            print(cur.key)
            cur = cur.next                    
                
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

print(PrintList(head))