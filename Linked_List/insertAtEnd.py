class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        
def PrintList(head):
    cur = head
    while cur != None:
        print(cur.key)
        cur = cur.next 
def insertEnd(head, key):
    if head == None:
        return Node(key)
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = Node(key)
    return head
          

head = None
head = insertEnd(head, 10)
head = insertEnd(head, 20)
head = insertEnd(head, 30)
head = insertEnd(head, 40)
print(PrintList(head))